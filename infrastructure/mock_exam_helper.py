"""
Mock Exam Helper Module

Provides consistent UI components for all mock exams using Streamlit native features.
"""

import streamlit as st
from typing import Dict, List, Tuple, Any
import re
import os

def render_question_with_images(question_text: str, base_path: str = None):
    """
    Render question text that may contain image references using st.image().
    Supports both markdown image syntax and direct image paths.

    Args:
        question_text: The question text that may contain image references
        base_path: Base path to resolve relative image paths (optional)
    """
    # Split text by image references
    parts = re.split(r'(!\[([^\]]*)\]\(([^)]+)\))', question_text)

    for i, part in enumerate(parts):
        if i % 4 == 0:  # Text parts
            if part.strip():
                st.markdown(part)
        elif i % 4 == 1:  # Full image markdown
            alt_text = parts[i + 1]
            image_path = parts[i + 2]

            # Try multiple path resolutions in order of preference
            possible_paths = []

            # 1. If base_path provided, use it with image_path
            if base_path:
                possible_paths.append(os.path.join(base_path, image_path))

            # 2. Try various absolute/relative paths
            possible_paths.extend([
                os.path.join("subjects", "CS", "assets", image_path),  # Full relative path
                os.path.join("subjects", "CS", "assets", "mock_exam_images", os.path.basename(image_path)),  # Just filename in mock_exam_images
                os.path.join(os.getcwd(), "subjects", "CS", "assets", image_path),  # Absolute path
                image_path  # Original path as fallback
            ])

            # Find first existing path
            final_path = None
            for path in possible_paths:
                if os.path.exists(path):
                    final_path = path
                    break

            if final_path:
                try:
                    st.image(final_path, caption=alt_text, width=500)
                except Exception as e:
                    st.error(f"Fehler beim Laden des Bildes {final_path}: {e}")
            else:
                st.warning(f"❌ Bild nicht gefunden: {image_path}")
                st.markdown(f"*[Bild: {alt_text}]*")

# ============================================================================
# QUESTION RENDERING (During Exam)
# ============================================================================

def render_question(q: Dict, key_prefix: str) -> Tuple[Any, bool]:
    """
    Render a question during the exam and return user's answer + validity.
    
    Args:
        q: Question dictionary with 'id', 'title', 'question', 'type', 'options', 'hint', 'explanation'
        key_prefix: Unique prefix for Streamlit widget keys
        
    Returns:
        Tuple of (user_answer, is_valid)
    """
    st.markdown(f"### Question {q['id']}: {q['title']}")
    # Get the base path for image resolution - try multiple possible locations
    possible_paths = [
        os.path.join(os.path.dirname(__file__), "..", "chapters"),  # Demo app: chapters directory
        os.path.join(os.getcwd(), "chapters"),  # Demo app: chapters from cwd
        os.path.join(os.path.dirname(__file__), "..", "subjects", "CS", "assets"),  # Development path
        "subjects/CS/assets",  # Relative to app root
        "./subjects/CS/assets",  # Explicit relative
        os.path.join(os.getcwd(), "subjects", "CS", "assets")  # Absolute from cwd
    ]

    base_path = None
    for path in possible_paths:
        test_path = os.path.join(path, "mock_exam_images")
        if os.path.exists(test_path):
            base_path = path
            break

    if base_path is None:
        # Try current working directory as fallback
        cwd_base = os.path.join(os.getcwd(), "subjects", "CS", "assets")
        if os.path.exists(os.path.join(cwd_base, "mock_exam_images")):
            base_path = cwd_base
        # Fallback silently, images will show error individually
    render_question_with_images(q['question'], base_path)
    
    # Hint expander (always available)
    hint_text = q.get('hint', "**💡 Hint:** Read the question carefully.")
    with st.expander("💡 Hint", expanded=False):
        st.markdown(hint_text)

    key = f"{key_prefix}_{q['id']}"
    q_type = q.get('type', 'single')

    if q_type == 'multi':
        st.caption("**Select all that apply:**")
        selected = []
        for idx, (option, _) in enumerate(q['options']):
            if st.checkbox(option, key=f"{key}_{idx}"):
                selected.append(idx)

        # Solution expander (beneath answer options)
        explanation_text = q.get('explanation', "**📝 Solution:** No explanation available.")
        with st.expander("📝 Solution", expanded=False):
            st.markdown(explanation_text)

        return selected, True

    elif q_type == 'matching':
        st.caption("**Match the following items:**")
        selected = []
        # Get all unique possible outcomes from all matching options
        possible_outcomes = sorted(list(set([opt[1] for opt in q['options']])))
        options_text = ["-- Select --"] + possible_outcomes

        for idx, (label, _) in enumerate(q['options']):
            col1, col2 = st.columns([2, 1])
            with col1:
                st.markdown(f"**{label}**")
            with col2:
                selected_text = st.selectbox(
                    f"Match for {label}",
                    options_text,
                    key=f"{key}_match_{idx}",
                    label_visibility="collapsed"
                )
                if selected_text != "-- Select --":
                    selected.append(selected_text)
                else:
                    selected.append(None)

        # Solution expander (beneath answer options)
        explanation_text = q.get('explanation', "**📝 Solution:** No explanation available.")
        with st.expander("📝 Solution", expanded=False):
            st.markdown(explanation_text)

        # Valid only if all items have a selection
        return selected, all(s is not None for s in selected)

    else:  # single
        st.caption("**Select one:**")
        options_text = [opt for opt, _ in q['options']]
        selected_idx = st.radio(
            "Choice",
            range(len(options_text)),
            format_func=lambda x: options_text[x],
            key=key,
            label_visibility="collapsed"
        )

        # Solution expander (beneath answer options)
        explanation_text = q.get('explanation', "**📝 Solution:** No explanation available.")
        with st.expander("📝 Solution", expanded=False):
            st.markdown(explanation_text)

        return [selected_idx], True


# ============================================================================
# ANSWER CHECKING
# ============================================================================

def check_answer(q: Dict, user_answer: Any) -> bool:
    """
    Check if the user's answer is correct.
    
    Args:
        q: Question dictionary
        user_answer: User's submitted answer
        
    Returns:
        True if correct, False otherwise
    """
    if user_answer is None:
        return False
    
    q_type = q.get('type', 'single')
    
    if q_type == 'single':
        if not user_answer:
            return False
        return q['options'][user_answer[0]][1]  # Check if selected option is True
    
    elif q_type == 'multi':
        if not user_answer:
            return False
        correct_indices = [i for i, opt in enumerate(q['options']) if opt[1]]
        return set(user_answer) == set(correct_indices)
    
    elif q_type == 'matching':
        if not user_answer or None in user_answer:
            return False
        target_matches = [opt[1] for opt in q['options']]
        return user_answer == target_matches
    
    return False


# ============================================================================
# RESULTS RENDERING (After Submission)
# ============================================================================

def render_results_header(correct_count: int, total_count: int, sections: Dict[str, Tuple[int, int]], questions: List[Dict], answers: Dict):
    """
    Render the exam results header with score overview and section breakdown.
    
    Args:
        correct_count: Number of correct answers
        total_count: Total number of questions
        sections: Section mapping {section_name: (start_id, end_id)}
        questions: List of question dictionaries
        answers: Dictionary of {question_id: user_answer}
    """
    # Calculate section scores
    section_scores = {}
    for sec_name in sections.keys():
        section_scores[sec_name] = {"correct": 0, "total": 0}
    
    for q in questions:
        q_section = q.get('section', 'Other')
        if q_section in section_scores:
            section_scores[q_section]["total"] += 1
            if check_answer(q, answers.get(q['id'])):
                section_scores[q_section]["correct"] += 1
    
    # Score Overview
    percentage = int(correct_count / total_count * 100) if total_count > 0 else 0
    
    # Display using native Streamlit components
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("✅ Correct", f"{correct_count}")
    with col2:
        st.metric("📝 Total", f"{total_count}")
    with col3:
        st.metric("📊 Score", f"{percentage}%")
    
    # Section Breakdown
    st.subheader("📈 Section Breakdown")
    
    for sec_name, scores in section_scores.items():
        if scores["total"] > 0:
            pct = scores["correct"] / scores["total"]
            st.write(f"**{sec_name}:** {scores['correct']} / {scores['total']}")
            st.progress(pct)


def render_question_result(q: Dict, user_answer: Any) -> bool:
    """
    Render a single question result with correct/incorrect highlighting.
    Uses native Streamlit components for best practice.
    
    Args:
        q: Question dictionary
        user_answer: User's submitted answer
        
    Returns:
        True if answer was correct
    """
    is_correct = check_answer(q, user_answer)
    user_answer = user_answer or []
    
    # Get correct answers
    q_type = q.get('type', 'single')
    if q_type == 'matching':
        correct_answers = [opt[1] for opt in q['options']]
    else:
        correct_answers = [i for i, opt in enumerate(q['options']) if opt[1]]
    
    # Status indicator
    if not user_answer or (q_type == 'matching' and None in user_answer):
        status_icon = "⚠️"
        status_text = "Not Answered"
        status_type = "warning"
    elif is_correct:
        status_icon = "✅"
        status_text = "Correct"
        status_type = "success"
    else:
        status_icon = "❌"
        status_text = "Incorrect"
        status_type = "error"
    
    # Question Card using native expander
    with st.expander(f"{status_icon} Q{q['id']}: {q['title']} — {status_text}", expanded=not is_correct):
        # Question text
        st.markdown(q['question'])
        
        # Tabs for organized content
        tab_answer, tab_correct, tab_explain = st.tabs(["🎯 Your Answer", "✅ Correct Answer", "📚 Explanation"])
        
        with tab_answer:
            _render_user_answer(q, user_answer)
        
        with tab_correct:
            _render_correct_answer(q, correct_answers)
        
        with tab_explain:
            st.markdown(q.get('explanation', "*Explanation not available.*"))
    
    return is_correct


def _render_user_answer(q: Dict, user_answer: Any):
    """Render what the user selected."""
    q_type = q.get('type', 'single')
    
    if not user_answer or (q_type == 'matching' and None in user_answer):
        st.warning("No answer selected")
        return
    
    if q_type == 'matching':
        for idx, (label, _) in enumerate(q['options']):
            user_match = user_answer[idx] if idx < len(user_answer) else None
            st.write(f"**{label}** → `{user_match}`")
    else:
        for idx, (option, _) in enumerate(q['options']):
            if idx in user_answer:
                st.info(f"👆 {option}")
            else:
                st.caption(f"○ {option}")


def _render_correct_answer(q: Dict, correct_answers: Any):
    """Render the correct answer(s)."""
    q_type = q.get('type', 'single')
    
    if q_type == 'matching':
        for idx, (label, correct_match) in enumerate(q['options']):
            st.success(f"**{label}** → `{correct_match}`")
    else:
        for idx, (option, is_correct) in enumerate(q['options']):
            if is_correct:
                st.success(f"✅ {option}")
            else:
                st.caption(f"○ {option}")


# ============================================================================
# EXAM FLOW HELPERS
# ============================================================================

def render_exam_intro(title: str, sections: Dict[str, Tuple[int, int]], total_questions: int):
    """Render exam introduction with section overview."""
    st.header(f"📝 {title}")
    
    intro_lines = ["**Exam Coverage:**"]
    for sec_name, (start, end) in sections.items():
        count = end - start + 1
        intro_lines.append(f"- **{sec_name}:** {count} questions")
    intro_lines.append(f"\n**Total: {total_questions} Questions**")
    intro_lines.append("---")
    
    st.markdown("\n".join(intro_lines))


def render_exam_complete(retake_key: str, on_retake: callable):
    """Render exam completion message with retake button."""
    st.success("🎉 **Exam Complete!** Review your answers below.")
    
    if st.button("🔄 Take Exam Again", key=retake_key, type="primary"):
        on_retake()
        st.rerun()
