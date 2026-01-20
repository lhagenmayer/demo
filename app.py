import streamlit as st
import os
import importlib

# Config - MUST be the first command
st.set_page_config(
    page_title="Lernapp Demo - Computer Science",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Contact email for full access
CONTACT_EMAIL = "luca@eatomics.com"

# Chapter definitions with metadata
CHAPTERS = [
    {"id": "01", "title": "01. Computing Basics", "emoji": "🖥️", "description": "Bits, Logik-Gatter, CPU – Die Grundlagen der Informatik", "available": False},
    {"id": "02", "title": "02. Python Basics", "emoji": "🐍", "description": "Variablen, Typen, I/O – Dein erster Python-Code", "available": True},
    {"id": "03", "title": "03. Kontrollstrukturen & Funktionen", "emoji": "🔄", "description": "Schleifen, Listen, Tuples – Algorithmen in Aktion", "available": False},
    {"id": "04", "title": "04. Datenstrukturen", "emoji": "📦", "description": "Rekursion, Dicts, Sets – Effiziente Datenverwaltung", "available": False},
    {"id": "05", "title": "05. Objektorientierte Programmierung", "emoji": "🏗️", "description": "Klassen, Vererbung – Code wie ein Profi strukturieren", "available": False},
    {"id": "06", "title": "06. Data Science 1: NumPy & Pandas", "emoji": "📊", "description": "Arrays, DataFrames – Datenanalyse mit Python", "available": False},
    {"id": "07", "title": "07. Data Science 2: Wrangling & Visualisierung", "emoji": "📈", "description": "Joins, Plots, Cleaning – Daten aufbereiten und visualisieren", "available": False},
    {"id": "08", "title": "08. Datenbanken & SQL", "emoji": "🗄️", "description": "Normalisierung, Queries – Professionelle Datenspeicherung", "available": False},
    {"id": "09", "title": "09. Netzwerke & APIs", "emoji": "🌐", "description": "HTTP, DNS, REST APIs – Das Internet verstehen", "available": False},
    {"id": "10", "title": "10. Von Statistik zu ML", "emoji": "🤖", "description": "Loss, Gradient Descent – Machine Learning Grundlagen", "available": False},
    {"id": "11", "title": "11. Klassifikation", "emoji": "🎯", "description": "Logistic Regression, ROC – ML in der Praxis", "available": False},
    {"id": "12", "title": "12. Quick Reference", "emoji": "📚", "description": "Komplettübersicht aller Syntax – Perfekt zum Lernen", "available": "partial"},
]

# Mock Exams
MOCK_EXAMS = [
    {"id": "mock1", "title": "📝 Mock Exam 1", "description": "5 Beispielfragen mit ausführlichen Erklärungen", "available": "partial"},
    {"id": "mock2", "title": "📝 Mock Exam 2", "description": "32 weitere Fragen mit detaillierten Lösungswegen", "available": False},
]

# Actual tab structure from each chapter for accurate preview
CHAPTER_TABS = {
    "01": ["🎓 Was ist Informatik?", "💡 Bits & Bytes", "🔢 Zahlensysteme", "🧠 Logik", "🔌 Transistoren", "➕ Addierer", "⚙️ CPU", "💻 Übungen", "📝 Quiz"],
    "02": ["🐍 Warum Python?", "📦 Variablen", "📥 Datentypen", "➕ Arithmetik", "🎤 I/O", "❓ If-Else", "🔁 Schleifen", "🎲 Zufall", "💻 Übungen", "📝 Quiz"],
    "03": ["🔁 Kontrollstrukturen", "📎 Funktionen", "📋 Listen", "📦 Tuples", "✂️ Slicing", "🔢 Sequenz-Ops", "💻 Übungen", "📝 Quiz"],
    "04": ["🔄 Rekursion", "λ Lambda", "📝 Comprehensions", "⚙️ Generatoren", "🔑 Dictionaries", "🎯 Sets", "📚 Stacks", "🗺️ map/filter", "🌐 Web-Apps", "💻 Übungen", "📝 Quiz"],
    "05": ["🤔 Warum OOP?", "🏗️ Klassen", "⚙️ self", "🔧 __init__", "🔒 Properties", "🧬 Vererbung", "🎭 Polymorphismus", "🔐 Encapsulation", "💻 Übungen", "📝 Quiz"],
    "06": ["📊 Data Science", "🔢 NumPy Arrays", "🌱 Pandas Series", "📋 DataFrames", "🎯 Boolean Masking", "📊 Datenanalyse", "💻 Übungen", "📝 Quiz"],
    "07": ["🔧 Data Wrangling", "🔗 Merging (Joins)", "📊 GroupBy", "📝 apply()", "🌱 Visualisierung", "🎨 Chart Types", "💻 Übungen", "📝 Quiz"],
    "08": ["🗄 Datenbanken", "📐 ER-Modell", "📊 Normalisierung", "💾 SQL Basics", "📊 GROUP BY", "🔗 JOINs", "✏ DML", "🐍 sqlite3", "💻 Übungen", "📝 Quiz"],
    "09": ["🌐 Netzwerk-Basics", "📶 OSI Stack", "🔌 IP & Routing", "🛰️ TCP vs UDP", "🌍 HTTP", "📛 DNS", "🐍 APIs", "💻 Übungen", "📝 Quiz"],
    "10": ["🤖 Paradigmenwechsel", "📈 KI Geschichte", "📉 Loss", "⬇ Gradient Descent", "✂️ Train/Val/Test", "⚖ Bias-Variance", "🔄 Cross-Validation", "🎯 k-NN", "💻 Übungen", "📝 Quiz"],
    "11": ["🎯 Logistic Regression", "🔲 Confusion Matrix", "📊 Precision/Recall", "📈 ROC & AUC", "⚖ Class Imbalance", "🎯 Multi-Class", "💻 Übungen", "📝 Quiz"],
    "12": ["💻 Computing Basics", "🐍 Python Basics", "🔁 Control & Functions", "📦 Data Structures", "🏗 OOP", "📊 Data Science 1", "📊 Data Science 2", "💾 SQL & Databases", "🌐 Networks & APIs", "🤖 ML Fundamentals", "🎯 ML Classification", "📁 File I/O", "⚡ Advanced Python", "📐 Formeln", "🧠 Mental Models"],
    "mock1": ["🖥️ Computing (Q1-7)", "🗄️ Databases (Q8-13)", "📊 Data Science (Q14-19)", "🤖 ML & Networks (Q20-25)"],
    "mock2": ["🖥️ Computing (Q1-8)", "🗄️ Databases (Q9-16)", "📊 Data Science (Q17-24)", "🤖 ML & Networks (Q25-32)"],
}

def show_cta_banner():
    """Display prominent call-to-action banner for full access"""
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 16px;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);
    ">
        <h2 style="color: white; margin-bottom: 0.5rem;">🔓 Möchtest du vollen Zugang?</h2>
        <p style="color: rgba(255,255,255,0.9); font-size: 1.1rem; margin-bottom: 1.5rem;">
            Schalte alle 12 Kapitel, 2 Mock Exams und interaktive Übungen frei!
        </p>
        <div style="
            background: white;
            display: inline-block;
            padding: 1rem 2rem;
            border-radius: 8px;
            font-weight: bold;
        ">
            ✉️ Schreibe eine Mail an: <a href="mailto:luca@eatomics.com" style="color: #667eea;">luca@eatomics.com</a>
        </div>
    </div>
    """, unsafe_allow_html=True)


def show_locked_chapter(chapter):
    """Display a locked chapter placeholder with preview of actual tabs"""
    chapter_id = chapter.get('id', '')
    tabs_list = CHAPTER_TABS.get(chapter_id, [])
    
    st.markdown(f"""
    <div style="
        background: linear-gradient(145deg, #f5f7fa 0%, #e4e8f0 100%);
        border: 2px dashed #ccc;
        border-radius: 16px;
        padding: 3rem;
        text-align: center;
        margin-top: 2rem;
    ">
        <div style="font-size: 4rem; margin-bottom: 1rem;">🔒</div>
        <h2 style="color: #555; margin-bottom: 0.5rem;">{chapter['emoji']} {chapter['title']}</h2>
        <p style="color: #777; font-size: 1.1rem; margin-bottom: 1rem;">
            {chapter['description']}
        </p>
        <p style="color: #999; font-style: italic;">
            Dieses Kapitel ist in der Demo-Version nicht verfügbar.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Show actual tabs as preview
    if tabs_list:
        st.markdown("### 📑 In diesem Kapitel enthalten:")
        # Create clean tab preview without excessive lock emojis
        tabs_preview = " | ".join(tabs_list)
        st.markdown(f"""
        <div style="
            background: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 8px;
            padding: 1rem;
            margin: 1rem 0;
            overflow-x: auto;
        ">
            <span style="color: #6c757d; font-size: 0.9rem;">{tabs_preview}</span>
        </div>
        """, unsafe_allow_html=True)
        st.caption(f"**{len(tabs_list)} interaktive Tabs** mit Theorie, Übungen und Quiz")
    
    show_cta_banner()


def show_home():
    """Display home page with overview"""
    
    # Hero section
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.4);
    ">
        <h1 style="color: white; font-size: 2.5rem; margin-bottom: 0.5rem;">
            🎓 Lernapp Demo – Computer Science
        </h1>
        <p style="color: rgba(255,255,255,0.95); font-size: 1.3rem; margin-bottom: 1.5rem;">
            Von Python-Basics bis Machine Learning – alles was du für die Prüfung brauchst
        </p>
        <div style="
            display: inline-flex;
            gap: 1rem;
            flex-wrap: wrap;
            justify-content: center;
        ">
            <span style="background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 20px; color: white;">
                ✅ Interaktive Beispiele
            </span>
            <span style="background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 20px; color: white;">
                ✅ Ausführliche Erklärungen
            </span>
            <span style="background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 20px; color: white;">
                ✅ Echte Prüfungsfragen
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📦 Was ist in der Vollversion enthalten?")
    
    # Feature overview
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 1.5rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 12px; color: white;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">📚</div>
            <h4 style="margin: 0.5rem 0;">12 Kapitel</h4>
            <p style="font-size: 0.9rem; opacity: 0.9; margin: 0;">Von Bits bis Machine Learning</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 1.5rem; background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); border-radius: 12px; color: white;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">📝</div>
            <h4 style="margin: 0.5rem 0;">2 Mock Exams</h4>
            <p style="font-size: 0.9rem; opacity: 0.9; margin: 0;">57 echte Prüfungsfragen</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="text-align: center; padding: 1.5rem; background: linear-gradient(135deg, #fc4a1a 0%, #f7b733 100%); border-radius: 12px; color: white;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🎮</div>
            <h4 style="margin: 0.5rem 0;">Interaktive Übungen</h4>
            <p style="font-size: 0.9rem; opacity: 0.9; margin: 0;">Lernen durch Experimentieren</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # What's in demo
    st.success("""
    **🎁 In dieser Demo kannst du testen:**
    - 🐍 **Python Basics** – Vollständiges Kapitel mit allen Tabs, Übungen und Quiz
    - 📝 **Mock Exam 1 Sample** – 5 echte Prüfungsfragen mit ausführlichen Erklärungen
    - 📖 **Quick Reference** – Computing Basics Zusammenfassung
    """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Chapter overview table
    st.subheader("📋 Kapitelübersicht")
    
    st.markdown("""
    | # | Thema | Status |
    |---|-------|--------|
    | 01 | Computing Basics (Bits, Logik, CPU) | Vollversion |
    | 02 | Python Basics | ✅ **In Demo verfügbar** |
    | 03 | Kontrollstrukturen & Funktionen | Vollversion |
    | 04 | Datenstrukturen | Vollversion |
    | 05 | Objektorientierte Programmierung | Vollversion |
    | 06 | Data Science 1: NumPy & Pandas | Vollversion |
    | 07 | Data Science 2: Wrangling & Viz | Vollversion |
    | 08 | Datenbanken & SQL | Vollversion |
    | 09 | Netzwerke & APIs | Vollversion |
    | 10 | Von Statistik zu ML | Vollversion |
    | 11 | Klassifikation | Vollversion |
    | 12 | Quick Reference | 🔓 Teilweise verfügbar |
    | 📝 | Mock Exam 1 | 🔓 **5 Fragen in Demo** |
    | 📝 | Mock Exam 2 | Vollversion |
    """)
    
    st.info("👆 **Tipp:** Wähle 'Python Basics' in der Sidebar, um die Demo zu starten!")
    
    show_cta_banner()


def main():
    st.sidebar.title("📚 CS Demo Navigation")
    st.sidebar.markdown("---")
    
    # Build menu
    menu_options = ["🏠 Home"]
    
    # Add chapters
    for ch in CHAPTERS:
        if ch["available"] == True:
            status = "✅"
        elif ch["available"] == "partial":
            status = "🔓"
        else:
            status = "🔒"
        menu_options.append(f"{status} {ch['title']}")
    
    # Add mock exams
    for exam in MOCK_EXAMS:
        if exam["available"] == True:
            status = "✅"
        elif exam["available"] == "partial":
            status = "🔓"
        else:
            status = "🔒"
        menu_options.append(f"{status} {exam['title']}")
    
    selected = st.sidebar.radio("Wähle ein Kapitel:", menu_options, label_visibility="collapsed")
    
    # Demo badge in sidebar
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 0.8rem;
        border-radius: 8px;
        text-align: center;
        color: white;
        font-weight: bold;
    ">
        🎓 DEMO VERSION
    </div>
    """, unsafe_allow_html=True)
    
    # Route to selected page
    if selected == "🏠 Home":
        show_home()
    elif "02. Python Basics" in selected:
        # Import and run the available chapter
        from chapters import python_basics
        python_basics.run()
    elif "12. Quick Reference" in selected:
        # Import and run the partial Quick Reference chapter
        from chapters import quick_reference
        quick_reference.run()
    elif "Mock Exam 1" in selected:
        # Import and run the demo mock exam
        from chapters import mock1
        mock1.run()
    else:
        # Find the chapter/exam info
        for ch in CHAPTERS:
            if ch["title"] in selected:
                show_locked_chapter(ch)
                return
        
        for exam in MOCK_EXAMS:
            if exam["title"] in selected:
                show_locked_chapter({
                    "title": exam["title"],
                    "emoji": "📝",
                    "description": exam["description"]
                })
                return


if __name__ == "__main__":
    main()
