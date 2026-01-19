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
CONTACT_EMAIL = "luca.hagenmayer@student.unisg.ch"

# Chapter definitions with metadata
CHAPTERS = [
    {"id": "01", "title": "01. Computing Basics", "emoji": "🖥️", "description": "Bits, Logik-Gatter, CPU – Die Grundlagen der Informatik", "available": True},
    {"id": "02", "title": "02. Python Basics", "emoji": "🐍", "description": "Variablen, Typen, I/O – Dein erster Python-Code", "available": False},
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
    {"id": "mock1", "title": "📝 Mock Exam 1", "description": "Vollständige Prüfungssimulation mit 25 Fragen", "available": False},
    {"id": "mock2", "title": "📝 Mock Exam 2", "description": "Zweite Prüfungssimulation mit 32 Fragen", "available": False},
]


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
            ✉️ Schreibe eine Mail an: <a href="mailto:luca.hagenmayer@student.unisg.ch" style="color: #667eea;">luca.hagenmayer@student.unisg.ch</a>
        </div>
    </div>
    """, unsafe_allow_html=True)


def show_locked_chapter(chapter):
    """Display a locked chapter placeholder with preview"""
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
    
    show_cta_banner()


def show_home():
    """Display home page with overview"""
    st.title("🎓 Lernapp Demo – Computer Science")
    
    st.markdown("""
    ### Willkommen zur Demo!
    
    Dies ist eine **Vorschau** der vollständigen Lernapp für Computer Science & Machine Learning.
    In der Vollversion erhältst du Zugang zu:
    """)
    
    # Feature overview
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 1.5rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 12px; color: white;">
            <div style="font-size: 2rem;">📚</div>
            <h4>12 Kapitel</h4>
            <p style="font-size: 0.9rem; opacity: 0.9;">Von Bits bis Machine Learning</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 1.5rem; background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); border-radius: 12px; color: white;">
            <div style="font-size: 2rem;">📝</div>
            <h4>2 Mock Exams</h4>
            <p style="font-size: 0.9rem; opacity: 0.9;">Realistische Prüfungssimulation</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="text-align: center; padding: 1.5rem; background: linear-gradient(135deg, #fc4a1a 0%, #f7b733 100%); border-radius: 12px; color: white;">
            <div style="font-size: 2rem;">🎮</div>
            <h4>Interaktive Übungen</h4>
            <p style="font-size: 0.9rem; opacity: 0.9;">Lernen durch Experimentieren</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Chapter overview table
    st.subheader("📋 Kapitelübersicht")
    
    st.markdown("""
    | # | Thema | Status |
    |---|-------|--------|
    | 01 | Computing Basics (Bits, Logik, CPU) | ✅ **In Demo verfügbar** |
    | 02 | Python Basics | 🔒 Vollversion |
    | 03 | Kontrollstrukturen & Funktionen | 🔒 Vollversion |
    | 04 | Datenstrukturen | 🔒 Vollversion |
    | 05 | Objektorientierte Programmierung | 🔒 Vollversion |
    | 06 | Data Science 1: NumPy & Pandas | 🔒 Vollversion |
    | 07 | Data Science 2: Wrangling & Viz | 🔒 Vollversion |
    | 08 | Datenbanken & SQL | 🔒 Vollversion |
    | 09 | Netzwerke & APIs | 🔒 Vollversion |
    | 10 | Von Statistik zu ML | 🔒 Vollversion |
    | 11 | Klassifikation | 🔒 Vollversion |
    | 12 | Quick Reference | 🔒 Vollversion |
    """)
    
    st.info("👆 **Tipp:** Wähle 'Kapitel 01' in der Sidebar, um die Demo zu starten!")
    
    show_cta_banner()


def main():
    st.sidebar.title("📚 CS Demo Navigation")
    st.sidebar.markdown("---")
    
    # Build menu
    menu_options = ["🏠 Home"]
    
    # Add chapters
    for ch in CHAPTERS:
        status = "✅" if ch["available"] else "🔒"
        menu_options.append(f"{status} {ch['title']}")
    
    # Add mock exams
    st.sidebar.markdown("---")
    for exam in MOCK_EXAMS:
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
    elif "01. Computing Basics" in selected:
        # Import and run the available chapter
        from chapters import computing_basics
        computing_basics.run()
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
