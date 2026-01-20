import streamlit as st

TITLE = "12. Quick Reference (Demo)"


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


def run():
    st.header("12. Quick Reference - Demo Vorschau")
    
    st.info("""
    📚 **Quick Reference** enthält eine Komplettübersicht aller Syntax-Elemente aus **allen 12 Kapiteln**.
    In dieser Demo ist nur der **Computing Basics** Tab verfügbar.
    """)
    
    tabs = st.tabs([
        "💻 Computing Basics ✅", 
        "🐍 Python Basics 🔒", 
        "🔁 Control & Functions 🔒", 
        "📦 Data Structures 🔒", 
        "🏗 OOP 🔒", 
        "📊 Data Science 🔒", 
        "🤖 ML 🔒"
    ])
    
    # --- TAB 1: Computing Basics (Available in Demo) ---
    with tabs[0]:
        st.subheader("💻 Computing Basics - Quick Reference")
        
        col_ref1, col_ref2 = st.columns(2)
        
        with col_ref1:
            st.markdown("""
            ### Zahlensysteme - Formeln
            ```text
            Binär → Dezimal:  1101₂ = 1×2³ + 1×2² + 0×2¹ + 1×2⁰ = 13
            Hex → Dezimal:    2A₁₆ = 2×16¹ + 10×16⁰ = 42
            
            Bit/Byte Größen:
            1 Bit    = 0 oder 1
            1 Nibble = 4 Bits (0-15, 1 Hex-Ziffer)
            1 Byte   = 8 Bits (0-255, 2 Hex-Ziffern)
            1 KB     = 1024 Bytes (2¹⁰)
            1 MB     = 1024 KB (2²⁰)
            1 GB     = 1024 MB (2³⁰)
            ```
            
            ### Zahlensysteme in Python
            ```python
            # Dezimal -> Binär
            bin(42)           # '0b101010'
            format(42, 'b')   # '101010'
            
            # Dezimal -> Hexadezimal
            hex(255)          # '0xff'
            format(255, 'x')  # 'ff'
            
            # Binär -> Dezimal
            int('101010', 2)  # 42
            
            # Hexadezimal -> Dezimal
            int('FF', 16)     # 255
            ```
            
            ### ASCII & Unicode
            ```python
            ord('A')          # 65 (Zeichen -> Zahl)
            chr(65)           # 'A' (Zahl -> Zeichen)
            ord('a')          # 97
            ord('0')          # 48
            
            # Text zu Binär
            format(ord('H'), '08b')  # '01001000'
            ```
            """)
        
        with col_ref2:
            st.markdown("""
            ### Logik-Gatter (Wahrheitstabellen)
            ```text
            AND: Beide müssen 1 sein
            A B | OUT     OR: Mindestens einer 1
            0 0 |  0      A B | OUT
            0 1 |  0      0 0 |  0
            1 0 |  0      0 1 |  1
            1 1 |  1      1 0 |  1
                          1 1 |  1
            
            XOR: Genau einer 1    NOT: Umkehrung
            A B | OUT             A | OUT
            0 0 |  0              0 |  1
            0 1 |  1              1 |  0
            1 0 |  1
            1 1 |  0
            
            NAND: NOT(AND) - Universelles Gatter!
            A B | OUT
            0 0 |  1
            0 1 |  1
            1 0 |  1
            1 1 |  0
            ```
            
            ### Bitweise Operatoren
            ```python
            # Boolesche Operatoren (für True/False)
            True and False    # False
            True or False     # True
            not True          # False
            
            # Bitweise Operatoren (für Zahlen)
            5 & 3             # 1 (0101 & 0011 = 0001) AND
            5 | 3             # 7 (0101 | 0011 = 0111) OR
            5 ^ 3             # 6 (0101 ^ 0011 = 0110) XOR
            ~5                # -6 (Bitweise NOT)
            5 << 1            # 10 (Links: ×2)
            10 >> 1           # 5 (Rechts: ÷2)
            ```
            
            ### CPU Fetch-Decode-Execute
            ```text
            1. FETCH:   Befehl aus RAM holen
            2. DECODE:  Befehl interpretieren
            3. EXECUTE: ALU führt aus
            4. STORE:   Ergebnis speichern
            → Repeat (Milliarden mal/sec)
            ```
            """)
        
        st.success("✅ **Merksatz:** Dezimal für Menschen (10 Finger), Binär für Maschinen (An/Aus).")
    
    # --- LOCKED TABS ---
    for i in range(1, 7):
        with tabs[i]:
            st.markdown("""
            <div style="
                background: linear-gradient(145deg, #f5f7fa 0%, #e4e8f0 100%);
                border: 2px dashed #ccc;
                border-radius: 16px;
                padding: 3rem;
                text-align: center;
                margin-top: 1rem;
            ">
                <div style="font-size: 4rem; margin-bottom: 1rem;">🔒</div>
                <h3 style="color: #555;">Dieser Tab ist in der Demo nicht verfügbar</h3>
                <p style="color: #777;">
                    Die Vollversion enthält Quick References für alle Themen.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            show_cta_banner()


if __name__ == "__main__":
    run()
