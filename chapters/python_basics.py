import streamlit as st
import numpy as np
from infrastructure import render_diagram
import math
import random

TITLE = "02. Python Basics"

def run():
    st.header("2. Python Grundlagen")
    
    # --- CHAPTER INTRODUCTION ---
    st.markdown("""
    > *"Python liest sich fast wie Englisch – genau deshalb ist es die perfekte erste Programmiersprache."*
    
    In Kapitel 1 hast du verstanden, **wie** ein Computer funktioniert – von Bits über Logik-Gatter bis zur CPU.
    Jetzt lernst du, **wie du mit ihm kommunizierst**: durch **Python**, eine Sprache, die Kraft und Einfachheit vereint.
    """)
    
    with st.expander("🎯 Lernziele – Was du nach diesem Kapitel kannst", expanded=True):
        st.markdown("""
        **Deine Reise durch die Python-Grundlagen:**
        
        | Nr. | Konzept | Du lernst... |
        |-----|---------|--------------|
        | 1 | **Warum Python?** | Vorteile interpretierter Sprachen |
        | 2 | **Variablen** | Namen für Werte, Speichermodell |
        | 3 | **Datentypen** | str, int, float, bool – und Konversion |
        | 4 | **Arithmetik** | Rechnen mit +, -, *, /, **, % |
        | 5 | **Input/Output** | print(), input(), F-Strings |
        | 6 | **If-Else** | Entscheidungen im Code |
        | 7 | **Schleifen** | while und for – Wiederholungen |
        | 8 | **Zufall** | Das random-Modul |
        
        💡 **Der rote Faden:** Von einzelnen Bausteinen zu vollständigen Programmen!
        """)
    
    st.info("""
    🧭 **Kapitel-Roadmap:**  
    Du startest mit dem **Warum** (warum Python?), lernst dann die **Bausteine** (Variablen, Typen, Operatoren),
    und kombinierst sie zu **Logik** (if/else, Schleifen). Am Ende schreibst du deine ersten eigenen Programme!
    """)
    
    tabs = st.tabs([
        "🐍 Warum Python?",
        "📦 Variablen",
        "📥 Datentypen",
        "➕ Arithmetik",
        "🎤 I/O",
        "❓ If-Else",
        "🔁 Schleifen",
        "🎲 Zufall",
        "💻 Übungen",
        "📝 Quiz & Zusammenfassung"
    ])

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB 1: WARUM PYTHON?
    # ═══════════════════════════════════════════════════════════════════════════
    with tabs[0]:
        st.subheader("Warum Python?")
        
        # 📍 CONNECTION
        st.info("""
        📍 **Verbindung zum Vorherigen:** In Kapitel 1 hast du gelernt, wie Computer auf Hardware-Ebene funktionieren.
        Jetzt lernst du eine **Hochsprache**, die diese Komplexität versteckt und dich produktiv macht!
        """)
        
        # 🧠 COGNITIVE SCAFFOLDING
        st.info("""
        🧠 **Verstehe zuerst: Warum gerade Python?**
        
        Es gibt hunderte Programmiersprachen. Python ist so beliebt, weil es **Einfachheit mit Kraft** verbindet:
        - Du schreibst weniger Code für mehr Ergebnis
        - Der Code liest sich fast wie Englisch
        - Du kannst sofort loslegen, ohne kompliziertes Setup
        
        *Python ist wie ein Schweizer Taschenmesser: Gut für fast alles.*
        """)
        
        # 📖 THEORY
        with st.expander("📖 Theorie: Was ist Python?", expanded=True):
            st.markdown("""
            | Eigenschaft | Beschreibung |
            |-------------|--------------|
            | **Interpretiert** | Code wird direkt ausgeführt (kein Kompilieren) |
            | **Objekt-orientiert** | Alles ist ein Objekt |
            | **Große Community** | Riesig beliebt weltweit |
            | **Einfach zu lernen** | Klare, lesbare Syntax |
            
            **Einsatzgebiete:**
            - 📊 Data Science & Machine Learning
            - 🌐 Web Development
            - 💰 Finanzbereich
            - 🔬 Wissenschaftliche Berechnungen
            """)
        
        # 📊 DIAGRAM
        st.markdown("### 📊 Interpretiert vs. Kompiliert")
        render_diagram("""
            rankdir=TB;
            subgraph cluster_compiled {
                label="KOMPILIERT (C, Java)";
                style=filled;
                fillcolor="#ffebee";
                C1 [label="Code schreiben\\n.c, .java", fillcolor="#ffcdd2"];
                C2 [label="Kompilieren\\nMaschinencode", fillcolor="#ef9a9a"];
                C3 [label="Binärdatei\\nprogram.exe", fillcolor="#e57373"];
                C4 [label="Ausführen\\nSchnell!", fillcolor="#c8e6c9"];
                C1 -> C2 -> C3 -> C4;
            }
            subgraph cluster_interpreted {
                label="INTERPRETIERT (Python)";
                style=filled;
                fillcolor="#e3f2fd";
                I1 [label="Code schreiben\\n.py", fillcolor="#bbdefb"];
                I2 [label="Interpreter\\nZeile für Zeile", fillcolor="#90caf9"];
                I3 [label="Ausführen\\nFlexibel!", fillcolor="#c8e6c9"];
                I1 -> I2 -> I3;
            }
        """, height=350)
        
        # 💻 LIVE CODE DEMO
        st.markdown("### 💻 Python in Aktion")
        
        with st.echo():
            # Schritt 1: Variablen definieren
            # Variablen sind wie beschriftete Schubladen für Daten
            name = "Python"        # String (Text)
            year = 1991           # Integer (Ganze Zahl)
            is_awesome = True     # Boolean (Wahrheitswert)

            # Schritt 2: Mit F-Strings ausgeben
            # f vor dem String aktiviert Variable-Einsetzung
            print(f"{name} wurde {year} erfunden")  # Python wurde 1991 erfunden
            print(f"Ist Python großartig? {is_awesome}")  # Ist Python großartig? True
        
        # 🎮 INTERACTIVE EXPLORATION
        st.markdown("### 🎮 Interaktiv: Vergleich")
        
        lang_type = st.radio("Vergleiche:", ["Kompiliert (C, Java)", "Interpretiert (Python)"], key="lang_compare")
        
        if lang_type == "Kompiliert (C, Java)":
            st.markdown("""
            **Ablauf:**
            1. Code schreiben (.c, .java)
            2. **Compiler** übersetzt in Maschinencode
            3. Binärdatei erstellen (.exe)
            4. Ausführen
            
            ✅ Schnelle Ausführung | ❌ Langsame Kompilierung | ❌ Plattform-spezifisch
            """)
        else:
            st.markdown("""
            **Ablauf:**
            1. Code schreiben (.py)
            2. **Interpreter** übersetzt Zeile für Zeile
            3. Direkt ausführen
            
            ✅ Schnelle Entwicklung | ✅ Plattform-unabhängig | ❌ Langsamere Ausführung
            """)
        
        # ⚠️ ERROR PREVENTION
        with st.expander("⚠️ Häufige Missverständnisse", expanded=False):
            st.markdown("""
            **Missverständnis 1: "Python ist langsam, also schlecht"**
            - ❌ Für die meisten Aufgaben spielt Geschwindigkeit keine Rolle
            - ✅ Entwicklungszeit ist oft wichtiger als Laufzeit
            
            **Missverständnis 2: "Ich brauche Python 2"**
            - ❌ Python 2 ist seit 2020 nicht mehr unterstützt
            - ✅ Immer Python 3 verwenden!
            
            **Missverständnis 3: "Python ist nur für Anfänger"**
            - ❌ Python wird bei Google, Netflix, NASA verwendet
            - ✅ Einfach UND professionell
            """)
        
        # 🔑 MEMORY HOOK
        st.success("""
        🔑 **Merksatz:** *"Python = Produktivität vor Performance"*
        
        Python ist langsamer als C, aber du schreibst Programme 5x schneller. Für die meisten Aufgaben ist das der bessere Deal!
        """)
        
        # 👉 TRANSITION
        st.caption("👉 *Weiter in Tab 2: Wie speichern wir Daten? → Variablen*")

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB 2: VARIABLEN
    # ═══════════════════════════════════════════════════════════════════════════
    with tabs[1]:
        st.subheader("Variablen und Zuweisungen")
        
        # 📍 CONNECTION
        st.info("""
        📍 **Verbindung zum Vorherigen:** Python ist flexibel und interpretiert.
        Aber wie speichern wir Daten? Mit **Variablen** – benannte Behälter für Werte!
        """)
        
        # 🧠 COGNITIVE SCAFFOLDING
        st.info("""
        🧠 **Verstehe zuerst: Was sind Variablen?**
        
        Stell dir Variablen wie **beschriftete Schubladen** vor:
        - Die **Beschriftung** (Name) = `alter`
        - Der **Inhalt** (Wert) = `25`
        
        Du gibst der Schublade einen Namen, legst etwas rein, und kannst es später wiederfinden.
        
        *Variable = beschriftete Schublade für Daten.*
        """)
        
        # 📖 THEORY
        with st.expander("📖 Theorie: Variablen in Python", expanded=True):
            st.markdown("""
            **Syntax:** `name = wert`
            
            | Konzept | Erklärung | Beispiel |
            |---------|-----------|----------|
            | **Zuweisung** | Wert speichern | `x = 5` |
            | **Referenz** | Name zeigt auf Objekt | `name = "Alice"` |
            | **Neuzuweisung** | Wert ändern | `x = x + 1` |
            | **Augmented** | Kurzform | `x += 1` |
            
            **Naming Rules:**
            - ✅ `snake_case` für Variablen
            - ✅ `UPPER_CASE` für Konstanten
            - ❌ Nicht mit Zahl beginnen
            - ❌ Keine reservierten Wörter (if, for, class...)
            """)
        
        # 📊 DIAGRAM
        st.markdown("### 📊 Python Memory Model")
        render_diagram("""
            rankdir=LR;
            subgraph cluster_namespace {
                label="NAMESPACE (Namen)";
                style=filled;
                fillcolor="#e3f2fd";
                name_var [label="name", fillcolor="#bbdefb"];
                age_var [label="age", fillcolor="#bbdefb"];
                gpa_var [label="gpa", fillcolor="#bbdefb"];
            }
            subgraph cluster_memory {
                label="MEMORY (Objekte)";
                style=filled;
                fillcolor="#f3e5f5";
                O1 [label="'Alice'\\nType: str", fillcolor="#ce93d8"];
                O2 [label="25\\nType: int", fillcolor="#ce93d8"];
                O3 [label="3.75\\nType: float", fillcolor="#ce93d8"];
            }
            name_var -> O1 [label="referenziert"];
            age_var -> O2 [label="referenziert"];
            gpa_var -> O3 [label="referenziert"];
        """, height=300)
        
        # 💻 LIVE CODE DEMO
        st.markdown("### 💻 Variablen in Aktion")
        
        with st.echo():
            # Schritt 1: Verschiedene Variablen erstellen
            # Jede Variable = Name + Wert + Typ
            first_name = "Alice"     # str (String) für Text
            student_id = 12345       # int (Integer) für ganze Zahlen
            gpa = 3.75              # float für Dezimalzahlen
            is_active = True        # bool (Boolean) für Ja/Nein

            # Schritt 2: Werte mit F-Strings ausgeben
            print(f"Name: {first_name}")    # Alice
            print(f"ID: {student_id}")      # 12345
            print(f"GPA: {gpa}")           # 3.75
            print(f"Aktiv: {is_active}")   # True
        
        st.markdown("### 💻 Augmented Assignment")
        
        with st.echo():
            # Schritt 1: Variable initialisieren
            x = 10  # Startwert
            print(f"Start: x = {x}")  # Ausgabe: Start: x = 10

            # Schritt 2: Langform der Zuweisung
            x = x + 5  # Rechts: x(10) + 5 = 15, dann x = 15 zuweisen
            print(f"Nach x = x + 5: {x}")  # Ausgabe: Nach x = x + 5: 15

            # Schritt 3: Kurzform (Augmented Assignment)
            # x *= 2 ist gleichbedeutend mit x = x * 2
            x = x * 2  # Rechts: x(15) * 2 = 30, dann x = 30 zuweisen
            print(f"Nach x = x * 2: {x}")  # Ausgabe: Nach x = x * 2: 30

            # Andere Kurzformen: +=, -=, /=, //=, %=, **=
        
        # 🎮 INTERACTIVE EXPLORATION
        st.markdown("### 🎮 Interaktiv: Variablen-Namens-Checker")
        
        var_name = st.text_input("Teste einen Variablennamen:", "my_variable", key="var_check")
        
        is_valid = True
        reasons = []
        
        if not var_name:
            is_valid = False
            reasons.append("Name darf nicht leer sein")
        elif var_name[0].isdigit():
            is_valid = False
            reasons.append("Darf nicht mit Zahl beginnen")
        elif "-" in var_name:
            is_valid = False
            reasons.append("Bindestriche nicht erlaubt (nutze _)")
        elif " " in var_name:
            is_valid = False
            reasons.append("Leerzeichen nicht erlaubt")
        elif var_name in ["if", "for", "while", "class", "def", "return", "import"]:
            is_valid = False
            reasons.append("Reserviertes Python-Keyword")
        
        if is_valid:
            st.success(f"✅ `{var_name}` ist ein gültiger Variablenname!")
        else:
            st.error(f"❌ `{var_name}` ist ungültig: {', '.join(reasons)}")
        
        # ⚠️ ERROR PREVENTION
        with st.expander("⚠️ Häufige Fehler", expanded=False):
            st.markdown("""
            **Fehler 1: Ungültige Variablennamen**
            ```python
            # ❌ FALSCH
            1student = "Alice"    # Beginnt mit Zahl!
            my-name = "Bob"       # Bindestrich!
            
            # ✅ RICHTIG
            student_1 = "Alice"
            my_name = "Bob"
            ```
            
            **Fehler 2: Variable vor Zuweisung verwenden**
            ```python
            # ❌ FALSCH
            print(age)  # NameError!
            age = 25
            
            # ✅ RICHTIG
            age = 25
            print(age)
            ```
            
            **Fehler 3: = vs == verwechseln**
            ```python
            # ❌ FALSCH
            if x = 5:  # SyntaxError!
            
            # ✅ RICHTIG
            if x == 5:  # Vergleich!
            ```
            """)
        
        # 🔑 MEMORY HOOK
        st.success("""
        🔑 **Merksatz:** *"Variable = Beschriftete Schublade"*
        
        Der Name ist die Beschriftung, der Wert ist der Inhalt. Mit `=` legst du etwas rein.
        """)
        
        # 👉 TRANSITION
        st.caption("👉 *Weiter in Tab 3: Welche Arten von Werten gibt es? → Datentypen*")

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB 3: DATENTYPEN
    # ═══════════════════════════════════════════════════════════════════════════
    with tabs[2]:
        st.subheader("Datentypen – Die Basics")
        
        # 📍 CONNECTION
        st.info("""
        📍 **Verbindung zum Vorherigen:** Variablen speichern Werte.
        Aber **welche Art** von Wert? Python unterscheidet verschiedene **Datentypen**!
        """)
        
        # 🧠 COGNITIVE SCAFFOLDING
        st.info("""
        🧠 **Verstehe zuerst: Warum Datentypen?**
        
        Stell dir verschiedene **Behältertypen** vor:
        - **Wasserglas** (int) → Nur ganze Zahlen
        - **Messbecher** (float) → Zahlen mit Komma
        - **Briefumschlag** (str) → Text
        - **Lichtschalter** (bool) → An/Aus
        
        *Der Typ bestimmt, was du mit dem Wert machen kannst!*
        """)
        
        # 📖 THEORY
        with st.expander("📖 Theorie: Python Datentypen", expanded=True):
            st.markdown("""
            | Typ | Name | Beschreibung | Beispiel |
            |-----|------|--------------|----------|
            | `int` | Integer | Ganze Zahlen | `42`, `-7`, `0` |
            | `float` | Float | Dezimalzahlen | `3.14`, `-0.5` |
            | `str` | String | Text in Anführungszeichen | `"Hallo"`, `'Welt'` |
            | `bool` | Boolean | Wahrheitswerte | `True`, `False` |
            | `None` | NoneType | Kein Wert | `None` |
            
            **Spezialfall Strings:**
            - `"` oder `'`: Für einzeiligen Text (äquivalent).
            - `\"\"\"` oder `'''`: Für **mehrzeiligen Text** (Triple-Quoted Strings).
            
            ```python
            multi_line = \"\"\"Das ist ein Text,
            der über mehrere
            Zeilen geht.\"\"\"
            ```
            
            **Typ-Konversion:**
            ```python
            int("42")      # String → Integer
            float("3.14")  # String → Float
            str(42)        # Integer → String
            bool(1)        # Integer → Boolean
            ```
            """)
        
        # 📊 DIAGRAM
        st.markdown("### 📊 Datentyp-Hierarchie")
        render_diagram("""
            TYPES [label="Python Datentypen", fillcolor="#4a90e2", fontcolor="white"];
            
            NUM [label="Numerisch", fillcolor="#c8e6c9"];
            TEXT [label="Text", fillcolor="#fff9c4"];
            LOGIC [label="Logisch", fillcolor="#ffccbc"];
            NONE [label="Nichts", fillcolor="#e0e0e0"];
            
            INT [label="int\\n42", fillcolor="#a5d6a7"];
            FLOAT [label="float\\n3.14", fillcolor="#a5d6a7"];
            STR [label="str\\n'Hello'", fillcolor="#fff59d"];
            BOOL [label="bool\\nTrue/False", fillcolor="#ffab91"];
            NONETYPE [label="None", fillcolor="#bdbdbd"];
            
            TYPES -> NUM;
            TYPES -> TEXT;
            TYPES -> LOGIC;
            TYPES -> NONE;
            
            NUM -> INT;
            NUM -> FLOAT;
            TEXT -> STR;
            LOGIC -> BOOL;
            NONE -> NONETYPE;
        """, height=300)
        
        # 💻 LIVE CODE DEMO
        st.markdown("### 💻 Typen in Aktion")
        
        with st.echo():
            # Schritt 1: Verschiedene Datentypen erstellen
            age = 25              # int - ganze Zahlen (positiv/negativ/null)
            height = 1.75         # float - Dezimalzahlen (Fließkomma)
            name = "Alice"        # str - Text in Anführungszeichen
            is_student = True     # bool - Wahrheitswerte (True/False)

            # Schritt 2: Typ mit type() ermitteln
            # type(objekt) gibt den Typ zurück, .__name__ macht ihn zum String
            age_type = type(age).__name__        # "int"
            height_type = type(height).__name__  # "float"
            name_type = type(name).__name__      # "str"
            student_type = type(is_student).__name__  # "bool"

            # Schritt 3: Ergebnisse ausgeben
            print(f"type(age) = {age_type}")           # int
            print(f"type(height) = {height_type}")     # float
            print(f"type(name) = {name_type}")         # str
            print(f"type(is_student) = {student_type}") # bool
        
        st.markdown("### 💻 Typ-Konversion")
        
        with st.echo():
            # Schritt 1: String zu Zahl konvertieren
            text_num = "42"           # Das ist Text, keine Zahl!
            real_num = int(text_num)  # int() wandelt String zu Integer
            print(f"'{text_num}' als int: {real_num}")  # '42' -> 42

            # Schritt 2: Zahl zu String konvertieren
            number = 3.14159          # Float-Zahl
            text = str(number)        # str() wandelt alles zu String
            print(f"{number} als str: '{text}'")  # 3.14159 -> '3.14159'

            # Schritt 3: Wahrheitswerte (Truthy/Falsy)
            # bool() konvertiert Werte zu True/False
            print(f"bool(1) = {bool(1)}")         # Zahlen ≠ 0 sind True
            print(f"bool(0) = {bool(0)}")         # 0 ist False
            print(f"bool('') = {bool('')}")       # Leerer String ist False
            print(f"bool('text') = {bool('text')}")  # Nicht-leerer String ist True
        
        # 🎮 INTERACTIVE EXPLORATION
        st.markdown("### 🎮 Interaktiv: Typ-Explorer")
        
        user_val = st.text_input("Gib einen Wert ein:", "42", key="type_explorer")
        
        with st.echo():
            # Schritt 1: Eingabewert übernehmen
            test_val = user_val  # Wert aus dem Textfeld

            # Schritt 2: Verschiedene Typ-Konversionen versuchen
            results = []  # Liste für die Ergebnisse

            # int() versuchen - funktioniert nur bei "ganzzahligen" Strings
            try:
                as_int = int(test_val)  # "42" -> 42, "3.14" -> Fehler
                results.append(f"int: {as_int}")  # Erfolg
            except:
                results.append("int: ❌ nicht möglich")  # Fehler

            # float() versuchen - funktioniert bei Dezimalzahlen
            try:
                as_float = float(test_val)  # "3.14" -> 3.14, "42" -> 42.0
                results.append(f"float: {as_float}")  # Erfolg
            except:
                results.append("float: ❌ nicht möglich")  # Fehler

            # str() geht immer - macht alles zum String
            results.append(f"str: '{test_val}'")  # Immer möglich

            # bool() geht immer - konvertiert zu True/False
            results.append(f"bool: {bool(test_val)}")  # Immer möglich

            # Schritt 3: Alle Ergebnisse ausgeben
            for r in results:
                print(r)  # Jedes Ergebnis in neuer Zeile
        
        # ⚠️ ERROR PREVENTION
        with st.expander("⚠️ Häufige Fehler", expanded=False):
            st.markdown("""
            **Fehler 1: Typ-Konversion vergessen**
            ```python
            # ❌ FALSCH
            age = input("Alter: ")  # Gibt String zurück!
            next_year = age + 1     # TypeError!
            
            # ✅ RICHTIG
            age = int(input("Alter: "))
            next_year = age + 1
            ```
            
            **Fehler 2: Falsche Konversion**
            ```python
            # ❌ FALSCH
            int("3.14")  # ValueError!
            
            # ✅ RICHTIG
            int(float("3.14"))  # 3
            ```
            
            **Fehler 3: String + Zahl mischen**
            ```python
            # ❌ FALSCH
            "Alter: " + 25  # TypeError!
            
            # ✅ RICHTIG
            "Alter: " + str(25)
            f"Alter: {25}"  # F-String!
            ```
            """)
        
        # 🔑 MEMORY HOOK
        st.success("""
        🔑 **Merksatz:** *"Typ bestimmt, was du tun kannst"*
        
        Mit Zahlen rechnen, mit Strings verketten. Falsche Typen = Fehler!
        """)
        
        # 👉 TRANSITION
        st.caption("👉 *Weiter in Tab 4: Wie rechnet Python? → Arithmetik*")

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB 4: ARITHMETIK
    # ═══════════════════════════════════════════════════════════════════════════
    with tabs[3]:
        st.subheader("Arithmetik – Rechnen mit Python")
        
        # 📍 CONNECTION
        st.info("""
        📍 **Verbindung zum Vorherigen:** Du weißt jetzt, dass es Zahlentypen (int, float) gibt.
        Jetzt lernst du, **was du mit diesen Zahlen machen kannst** – Rechnen!
        """)
        
        # 🧠 COGNITIVE SCAFFOLDING
        st.info("""
        🧠 **Verstehe zuerst: Python als Taschenrechner**
        
        Python kennt alle Rechenoperationen:
        - **Grundrechenarten:** `+ - * /`
        - **Spezial:** `//` (Ganzzahl-Division), `%` (Rest), `**` (Potenz)
        
        *Python = Taschenrechner mit Superkräften.*
        """)
        
        # 📖 THEORY
        with st.expander("📖 Theorie: Operatoren", expanded=True):
            st.markdown("""
            | Operator | Bedeutung | Beispiel | Ergebnis |
            |----------|-----------|----------|----------|
            | `+` | Addition | `5 + 3` | `8` |
            | `-` | Subtraktion | `5 - 3` | `2` |
            | `*` | Multiplikation | `5 * 3` | `15` |
            | `/` | Division (float) | `7 / 2` | `3.5` |
            | `//` | Ganzzahl-Division | `7 // 2` | `3` |
            | `%` | Modulo (Rest) | `7 % 2` | `1` |
            | `**` | Potenz | `2 ** 3` | `8` |
            
            **Priorität:** `**` → `* / // %` → `+ -` (wie in Mathe!)
            """)
        
        # 📊 DIAGRAM
        st.markdown("### 📊 Operator-Priorität")
        render_diagram("""
            rankdir=TB;
            HIGH [label="HÖCHSTE PRIORITÄT\\n**", fillcolor="#c8e6c9"];
            MED [label="MITTLERE PRIORITÄT\\n* / // %", fillcolor="#fff9c4"];
            LOW [label="NIEDRIGSTE PRIORITÄT\\n+ -", fillcolor="#ffccbc"];
            
            HIGH -> MED -> LOW;
            
            EX [label="2 + 3 * 4 = 14\\n(nicht 20!)", shape=note, fillcolor="#e3f2fd"];
        """, height=220)
        
        # 💻 LIVE CODE DEMO
        st.markdown("### 💻 Operatoren in Aktion")
        
        with st.echo():
            # Schritt 1: Zahlen definieren
            a = 17  # Dividend/Zahl 1
            b = 5   # Divisor/Zahl 2

            # Schritt 2: Grundrechenarten
            print(f"{a} + {b} = {a + b}")   # Addition: 17 + 5 = 22
            print(f"{a} - {b} = {a - b}")   # Subtraktion: 17 - 5 = 12
            print(f"{a} * {b} = {a * b}")   # Multiplikation: 17 * 5 = 85
            print(f"{a} / {b} = {a / b}")   # Division (float): 17 / 5 = 3.4

            # Schritt 3: Spezielle Operatoren
            print(f"{a} // {b} = {a // b}")  # Ganzzahl-Division: 17 // 5 = 3 (schneidet ab)
            print(f"{a} % {b} = {a % b}")   # Modulo (Rest): 17 % 5 = 2 (17 = 3*5 + 2)
            print(f"{a} ** 2 = {a ** 2}")   # Potenz: 17² = 289
            
            # Schritt 4: Nützliche Built-in Funktionen
            print(f"min({a}, {b}) = {min(a, b)}")  # Minimum: Kleinere Zahl
            print(f"max({a}, {b}) = {max(a, b)}")  # Maximum: Größere Zahl
            print(f"abs(-10) = {abs(-10)}")        # Betrag (absoluter Wert)
        
        # 🎮 INTERACTIVE EXPLORATION
        st.markdown("### 🎮 Interaktiv: Rechner")
        
        c1, c2, c3 = st.columns(3)
        calc_a = c1.number_input("a =", value=10, key="arith_a")
        calc_op = c2.selectbox("Operator:", ["+", "-", "*", "/", "//", "%", "**"], key="arith_op")
        calc_b = c3.number_input("b =", value=3, key="arith_b")
        
        with st.echo():
            # Schritt 1: Variablen aus der Benutzereingabe
            result = None  # Variable für das Ergebnis

            # Schritt 2: Operator mit if-elif-else prüfen
            if calc_op == "+":  # Addition
                result = calc_a + calc_b
            elif calc_op == "-":  # Subtraktion
                result = calc_a - calc_b
            elif calc_op == "*":  # Multiplikation
                result = calc_a * calc_b
            elif calc_op == "/" and calc_b != 0:  # Division (mit Null-Prüfung)
                result = calc_a / calc_b
            elif calc_op == "//" and calc_b != 0:  # Ganzzahl-Division
                result = calc_a // calc_b
            elif calc_op == "%" and calc_b != 0:  # Modulo
                result = calc_a % calc_b
            elif calc_op == "**":  # Potenz
                result = calc_a ** calc_b
            else:  # Fehlerfall (Division durch 0)
                result = "Error: Division durch 0!"

            # Schritt 3: Ergebnis ausgeben
            print(f"{calc_a} {calc_op} {calc_b} = {result}")
        
        st.metric("Ergebnis", str(result))
        
        # ⚠️ ERROR PREVENTION
        with st.expander("⚠️ Häufige Fehler", expanded=False):
            st.markdown("""
            **Fehler 1: Division durch Null**
            ```python
            # ❌ FALSCH
            10 / 0  # ZeroDivisionError!
            
            # ✅ RICHTIG – Vorher prüfen
            if b != 0:
                result = 10 / b
            ```
            
            **Fehler 2: // vs / verwechseln**
            ```python
            7 / 2   # 3.5 (Float!)
            7 // 2  # 3   (Integer, abgeschnitten!)
            ```
            
            **Fehler 3: Operator-Priorität vergessen**
            ```python
            2 + 3 * 4    # = 14 (Punkt vor Strich!)
            (2 + 3) * 4  # = 20 (Klammern helfen)
            ```
            """)
        
        # 🔑 MEMORY HOOK
        st.success("""
        🔑 **Merksatz:** *"// schneidet ab, / gibt Komma"*
        
        Integer-Division (//) kappt Dezimalen, normale Division (/) gibt immer float.
        """)
        
        # 👉 TRANSITION
        st.caption("👉 *Weiter in Tab 5: Wie kommuniziert Python mit der Welt? → Input/Output*")

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB 5: INPUT/OUTPUT
    # ═══════════════════════════════════════════════════════════════════════════
    with tabs[4]:
        st.subheader("Input und Output")
        
        # 📍 CONNECTION
        st.info("""
        📍 **Verbindung zum Vorherigen:** Du kannst rechnen und Ergebnisse speichern.
        Aber wie **zeigst du sie an** und **bekommst Eingaben**? Mit I/O!
        """)
        
        # 🧠 COGNITIVE SCAFFOLDING
        st.info("""
        🧠 **Verstehe zuerst: Was ist Input/Output?**
        
        Ein Programm ist wie ein **Rezept**:
        - **Input:** Die Zutaten (Benutzereingaben)
        - **Verarbeitung:** Das Kochen (Code)
        - **Output:** Das fertige Gericht (Ausgabe)
        
        *I/O = Die Kommunikation zwischen Mensch und Programm.*
        """)
        
        # 📖 THEORY
        with st.expander("📖 Theorie: print() und F-Strings", expanded=True):
            st.markdown("""
            | Funktion | Beschreibung | Beispiel |
            |----------|--------------|----------|
            | `print()` | Ausgabe auf Konsole | `print("Hallo")` |
            | `input()` | Eingabe vom Benutzer | `name = input("Name: ")` |
            | F-String | Variablen in Text | `f"Hallo {name}"` |
            
            **F-String Formatierung:**
            ```python
            f"{zahl:.2f}"   # 2 Dezimalstellen
            f"{zahl:>10}"   # 10 Zeichen rechtsbündig
            f"{zahl:,}"     # Tausendertrennzeichen
            ```
            
            **Escape-Sequenzen (Sonderzeichen):**
            | Sequenz | Bedeutung |
            |---------|-----------|
            | `\\n` | Neue Zeile (New Line) |
            | `\\t` | Tabulator (Einrücken) |
            | `\\\\` | Backslash selbst |
            | `\\"` | Anführungszeichen im String |
            """)
        
        # 📊 DIAGRAM
        st.markdown("### 📊 Input-Verarbeitung-Output")
        render_diagram("""
            rankdir=LR;
            INPUT [label="INPUT\\ninput()\\nDateien\\nSensoren", fillcolor="#b3e5fc"];
            PROCESS [label="VERARBEITUNG\\nBerechnung\\nLogik\\nTransformation", fillcolor="#fff9c4"];
            OUTPUT [label="OUTPUT\\nprint()\\nDateien\\nGrafik", fillcolor="#c8e6c9"];
            
            INPUT -> PROCESS -> OUTPUT;
        """, height=150)
        
        # 💻 LIVE CODE DEMO
        st.markdown("### 💻 F-Strings in Aktion")
        
        with st.echo():
            # Schritt 1: Variablen definieren
            name = "Alice"    # String
            age = 25         # Integer
            gpa = 3.75321    # Float mit vielen Dezimalstellen

            # Schritt 2: Basis F-String (f vor String aktiviert Variable-Einsetzung)
            print(f"Name: {name}, Alter: {age}")  # Variablen werden eingesetzt

        # Zusätzliche Formatierungsbeispiele (außerhalb von st.echo für separate Anzeige)
        st.code("""
# Schritt 3: Formatierung innerhalb der {}
print(f"GPA auf 2 Stellen: {gpa:.2f}")  # :.2f = 2 Dezimalstellen, f=Float
print(f"GPA auf 1 Stelle: {gpa:.1f}")  # :.1f = 1 Dezimalstelle
""", language="python")

        # Ausführen der formatierten Ausgaben
        print(f"GPA auf 2 Stellen: {gpa:.2f}")  # 3.75 (auf 2 Stellen gerundet)
        print(f"GPA auf 1 Stelle: {gpa:.1f}")   # 3.8 (auf 1 Stelle gerundet)
        
        # 🎮 INTERACTIVE EXPLORATION
        st.markdown("### 🎮 Interaktiv: F-String Builder")
        
        user_name = st.text_input("Dein Name:", "Student", key="io_name")
        user_score = st.slider("Deine Punktzahl:", 0, 100, 85, key="io_score")
        
        st.code(f"""
formatted = f"Hallo {{user_name}}! Du hast {{user_score}} Punkte."
print(formatted)

# Mit Formatierung
percentage = user_score / 100
formatted2 = f"Das sind {{percentage:.1%}} der moeglichen Punkte."
print(formatted2)
""", language="python")

        formatted = f"Hallo {user_name}! Du hast {user_score} Punkte."
        print(formatted)
        
        percentage = user_score / 100
        formatted2 = f"Das sind {percentage:.1%} der möglichen Punkte."
        print(formatted2)
        
        st.success(f"Hallo {user_name}! Du hast {user_score} Punkte ({user_score}%).")
        
        # ⚠️ ERROR PREVENTION
        with st.expander("⚠️ Häufige Fehler", expanded=False):
            st.markdown("""
            **Fehler 1: f vergessen**
            ```python
            # ❌ FALSCH – Kein f!
            print("Hallo {name}!")  # Gibt wörtlich "{name}" aus
            
            # ✅ RICHTIG
            print(f"Hallo {name}!")  # Gibt "Hallo Alice!" aus
            ```
            
            **Fehler 2: input() gibt immer String**
            ```python
            # ❌ FALSCH
            age = input("Alter: ")
            next_year = age + 1  # TypeError!
            
            # ✅ RICHTIG
            age = int(input("Alter: "))
            next_year = age + 1
            ```
            """)
        
        # 🔑 MEMORY HOOK
        st.success("""
        🔑 **Merksatz:** *"f vor String = Formatierung an"*
        
        `f"Text {variable}"` – Das f aktiviert die Magie, geschweifte Klammern fügen Variablen ein.
        """)
        
        # 👉 TRANSITION
        st.caption("👉 *Weiter in Tab 6: Wie trifft Python Entscheidungen? → If-Else*")

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB 6: IF-ELSE
    # ═══════════════════════════════════════════════════════════════════════════
    with tabs[5]:
        st.subheader("Entscheidungen mit If-Else")
        
        # 📍 CONNECTION
        st.info("""
        📍 **Verbindung zum Vorherigen:** Du kannst Daten einlesen und ausgeben.
        Aber wie reagiert dein Programm **unterschiedlich** auf verschiedene Eingaben? Mit **Bedingungen**!
        """)
        
        # 🧠 COGNITIVE SCAFFOLDING
        st.info("""
        🧠 **Verstehe zuerst: Was sind Bedingungen?**
        
        Stell dir einen **Türsteher** vor:
        - **WENN** du 18+ bist → Du darfst rein
        - **SONST** → Du darfst nicht rein
        
        *If-Else = Türsteher für deinen Code.*
        """)
        
        # 📖 THEORY
        with st.expander("📖 Theorie: If-Elif-Else", expanded=True):
            st.markdown("""
            **Syntax:**
            ```python
            if bedingung1:
                # Code wenn bedingung1 wahr
            elif bedingung2:
                # Code wenn bedingung2 wahr
            else:
                # Code wenn keine wahr
            ```
            
            **Vergleichsoperatoren:**
            | Operator | Bedeutung |
            |----------|-----------|
            | `==` | Gleich |
            | `!=` | Ungleich |
            | `<`, `>` | Kleiner/Größer |
            | `<=`, `>=` | Kleiner-gleich/Größer-gleich |
            """)
        
        # 📊 DIAGRAM
        st.markdown("### 📊 Entscheidungsbaum")
        render_diagram("""
            START [label="Start", fillcolor="#fff9c4"];
            CHECK1 [label="age >= 18?", shape=diamond, fillcolor="#b3e5fc"];
            CHECK2 [label="age >= 13?", shape=diamond, fillcolor="#b3e5fc"];
            ADULT [label="Volljährig", fillcolor="#c8e6c9"];
            TEEN [label="Teenager", fillcolor="#ffe0b2"];
            CHILD [label="Kind", fillcolor="#ffccbc"];
            
            START -> CHECK1;
            CHECK1 -> ADULT [label="Ja"];
            CHECK1 -> CHECK2 [label="Nein"];
            CHECK2 -> TEEN [label="Ja"];
            CHECK2 -> CHILD [label="Nein"];
        """, height=280)
        
        # 💻 LIVE CODE DEMO
        st.markdown("### 💻 If-Else in Aktion")
        
        demo_age = st.slider("Alter:", 0, 100, 18, key="if_age")
        
        with st.echo():
            # Schritt 1: Variable aus Slider übernehmen
            age = demo_age  # Alter aus dem Slider (0-100)

            # Schritt 2: Entscheidungsbaum mit if-elif-else
            if age >= 18:  # Wenn Alter >= 18
                status = "Volljährig"  # Dann: Volljährig
                can_vote = True        # Und: Darf wählen
            elif age >= 13:  # Sonst, wenn Alter >= 13
                status = "Teenager"   # Dann: Teenager
                can_vote = False      # Und: Darf nicht wählen
            else:  # In allen anderen Fällen (age < 13)
                status = "Kind"       # Dann: Kind
                can_vote = False      # Und: Darf nicht wählen

            # Schritt 3: Ergebnis ausgeben
            print(f"Alter: {age}")           # Eingabealter
            print(f"Status: {status}")       # Berechneter Status
            print(f"Wahlberechtigt: {can_vote}")  # Wahlberechtigung
        
        col1, col2 = st.columns(2)
        col1.metric("Status", status)
        col2.metric("Wahlberechtigt", "✅" if can_vote else "❌")
        
        # 🎮 INTERACTIVE EXPLORATION
        st.markdown("### 🎮 Interaktiv: Notenrechner")
        
        points = st.slider("Punkte:", 0, 100, 75, key="grade_points")
        
        with st.echo():
            # Schritt 1: Punkte aus Slider übernehmen
            p = points  # Punkte von 0-100

            # Schritt 2: Notenberechnung mit if-elif-Kette
            # Python prüft von oben nach unten und führt nur den ersten passenden Block aus
            if p >= 90:      # Wenn 90 oder mehr Punkte
                grade = "A"  # Dann: Beste Note
            elif p >= 80:    # Wenn nicht 90+, aber 80+
                grade = "B"  # Dann: Gut
            elif p >= 70:    # Wenn nicht 80+, aber 70+
                grade = "C"  # Dann: Befriedigend
            elif p >= 60:    # Wenn nicht 70+, aber 60+
                grade = "D"  # Dann: Ausreichend
            else:            # In allen anderen Fällen (unter 60)
                grade = "F"  # Dann: Nicht bestanden

            # Schritt 3: Ergebnis ausgeben
            print(f"{p} Punkte = Note {grade}")  # z.B. "85 Punkte = Note B"
        
        st.metric("Note", grade)
        
        # ⚠️ ERROR PREVENTION
        with st.expander("⚠️ Häufige Fehler", expanded=False):
            st.markdown("""
            **Fehler 1: = statt ==**
            ```python
            # ❌ FALSCH – Zuweisung statt Vergleich!
            if x = 5:  # SyntaxError!
            
            # ✅ RICHTIG – Doppeltes Gleichheitszeichen
            if x == 5:
            ```
            
            **Fehler 2: Einrückung vergessen**
            ```python
            # ❌ FALSCH
            if age >= 18:
            print("Volljährig")  # IndentationError!
            
            # ✅ RICHTIG – 4 Leerzeichen
            if age >= 18:
                print("Volljährig")
            ```
            
            **Fehler 3: Doppelpunkt vergessen**
            ```python
            # ❌ FALSCH
            if age >= 18  # SyntaxError!
            
            # ✅ RICHTIG
            if age >= 18:
            ```
            
            **Fehler 4: Logikfehler durch Einrückung**
            ```python
            # ⚠️ ACHTUNG: Die letzte Zeile wird IMMER ausgeführt!
            if grade >= 60:
                print('Bestanden')
            else:
                print('Nicht bestanden')
            print('Kurs wiederholen') # ❌ Falsch eingerückt!
            
            # ✅ RICHTIG: Nur im Else-Fall wiederholen
            if grade >= 60:
                print('Bestanden')
            else:
                print('Nicht bestanden')
                print('Kurs wiederholen')
            ```
            """)
        
        # 💡 PRO TIP: CONDITIONAL EXPRESSIONS
        with st.expander("💡 Profi-Tipp: Einzeiler (Ternary Operator)", expanded=False):
            st.markdown("""
            Manchmal ist ein ganzes `if-else` zu lang. Python hat dafür eine Kurzform:
            
            ```python
            # Langform
            if grade >= 60:
                result = 'Bestanden'
            else:
                result = 'Durchgefallen'
            
            # ✨ Kurzform (Conditional Expression)
            result = 'Bestanden' if grade >= 60 else 'Durchgefallen'
            ```
            
            
            Syntax: `Wert_wenn_Wahr if Bedingung else Wert_wenn_Falsch`
            
            **Noch ein Pro-Tipp: Verkettete Vergleiche**
            Statt `if age >= 18 and age <= 65:` kannst du schreiben:
            ```python
            if 18 <= age <= 65:
                print("Arbeitsfähig")
            ```
            Das ist wie in der Mathematik ($18 \le age \le 65$) und sehr elegant!
            """)
        
        # 🔑 MEMORY HOOK
        st.success("""
        🔑 **Merksatz:** *"Wenn-Dann-Sonst = If-Elif-Else"*
        
        Python prüft von oben nach unten und führt den ersten passenden Block aus.
        """)
        
        # 👉 TRANSITION
        st.caption("👉 *Weiter in Tab 7: Wie wiederholt Python Aktionen? → Schleifen*")

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB 7: SCHLEIFEN
    # ═══════════════════════════════════════════════════════════════════════════
    with tabs[6]:
        st.subheader("Schleifen – Wiederholungen")
        
        # 📍 CONNECTION
        st.info("""
        📍 **Verbindung zum Vorherigen:** Mit If-Else triffst du einmalige Entscheidungen.
        Aber was, wenn du etwas **mehrmals** tun willst? Dann brauchst du **Schleifen**!
        """)
        
        # 🧠 COGNITIVE SCAFFOLDING
        st.info("""
        🧠 **Verstehe zuerst: Was sind Schleifen?**
        
        Stell dir eine **Waschmaschine** vor:
        - Sie wiederholt den Waschzyklus **X mal** (= `for`-Schleife)
        - Oder sie läuft, **bis** die Wäsche sauber ist (= `while`-Schleife)
        
        *for = bekannte Anzahl, while = bis Bedingung erfüllt.*
        """)
        
        # 📖 THEORY
        with st.expander("📖 Theorie: for und while", expanded=True):
            st.markdown("""
            **for-Schleife:** Bekannte Anzahl Durchläufe
            ```python
            for i in range(5):
                print(i)  # 0, 1, 2, 3, 4
            ```
            
            **while-Schleife:** Läuft bis Bedingung falsch
            ```python
            x = 0
            while x < 5:
                print(x)
                x += 1
            ```
            
            | Schleife | Wann verwenden? |
            |----------|----------------|
            | `for` | Anzahl bekannt, über Liste iterieren |
            | `while` | Anzahl unbekannt, bis Bedingung erfüllt |
            """)
        
        # 📊 DIAGRAM
        st.markdown("### 📊 For vs While")
        render_diagram("""
            rankdir=TB;
            subgraph cluster_for {
                label="FOR-SCHLEIFE";
                style=filled;
                fillcolor="#e8f5e9";
                F1 [label="i = 0", fillcolor="#c8e6c9"];
                F2 [label="i < n?", shape=diamond, fillcolor="#a5d6a7"];
                F3 [label="Code ausführen", fillcolor="#81c784"];
                F4 [label="i += 1", fillcolor="#c8e6c9"];
                F5 [label="Ende", fillcolor="#66bb6a"];
                F1 -> F2;
                F2 -> F3 [label="Ja"];
                F3 -> F4 -> F2;
                F2 -> F5 [label="Nein"];
            }
            subgraph cluster_while {
                label="WHILE-SCHLEIFE";
                style=filled;
                fillcolor="#e3f2fd";
                W1 [label="Start", fillcolor="#bbdefb"];
                W2 [label="Bedingung?", shape=diamond, fillcolor="#90caf9"];
                W3 [label="Code ausführen", fillcolor="#64b5f6"];
                W4 [label="Ende", fillcolor="#42a5f5"];
                W1 -> W2;
                W2 -> W3 [label="Ja"];
                W3 -> W2;
                W2 -> W4 [label="Nein"];
            }
        """, height=350)
        
        # 💻 LIVE CODE DEMO
        st.markdown("### 💻 For-Schleife")
        
        with st.echo():
            # Schritt 1: for-Schleife mit range()
            # range(5) erzeugt die Zahlen 0, 1, 2, 3, 4
            for i in range(5):  # i nimmt nacheinander jeden Wert aus range(5) an
                print(f"Durchlauf {i}")  # Gibt aus: Durchlauf 0, Durchlauf 1, etc.

            # Schritt 2: Was passiert hier?
            # 1. Schleife startet mit i = 0
            # 2. print(f"Durchlauf 0") wird ausgeführt
            # 3. i wird auf 1 gesetzt
            # 4. print(f"Durchlauf 1") wird ausgeführt
            # 5. ... bis i = 4 erreicht ist
            # 6. Nach i = 4 ist range(5) zu Ende, Schleife stoppt
        
        st.markdown("### 💻 While-Schleife")
        
        st.code("""
# While mit Zähler
count = 0
while count < 3:
    print(f"Zähler: {count}")
    count += 1
print("Fertig!")
""", language="python")
        
        # Execute for display
        count = 0
        while count < 3:
            st.write(f"Zähler: {count}")
            count = count + 1
        st.write("Fertig!")
        
        # 🎮 INTERACTIVE EXPLORATION
        st.markdown("### 🎮 Interaktiv: Summe berechnen")
        
        n = st.slider("Summe von 1 bis n:", 1, 20, 5, key="loop_n")
        
        with st.echo():
            total = 0
            for i in range(1, n + 1):
                total = total + i
            print(f"Summe von 1 bis {n} = {total}")
        
        # Zeige Formel
        expected = n * (n + 1) // 2
        st.metric("Summe", total)
        st.caption(f"Formel: n*(n+1)/2 = {expected}")
        
        # ⚠️ ERROR PREVENTION
        with st.expander("⚠️ Häufige Fehler", expanded=False):
            st.markdown("""
            **Fehler 1: Endlos-Schleife**
            ```python
            # ❌ FALSCH – Läuft ewig!
            x = 0
            while x < 5:
                print(x)
                # x wird nie erhöht!
            
            # ✅ RICHTIG – Variable ändern
            x = 0
            while x < 5:
                print(x)
                x += 1
            ```
            
            **Fehler 2: Off-by-One Fehler**
            ```python
            # range(5) gibt 0, 1, 2, 3, 4 (nicht 5!)
            for i in range(5):
                print(i)  # 0 bis 4
            
            # Wenn du 1 bis 5 willst:
            for i in range(1, 6):
                print(i)  # 1 bis 5
            ```
            
            **Fehler 3: Liste während Iteration ändern**
            ```python
            # ❌ GEFÄHRLICH
            for item in liste:
                liste.remove(item)  # Probleme!
            
            # ✅ SICHER – Kopie iterieren
            for item in liste.copy():
                liste.remove(item)
            ```
            """)
        
        # 🔑 MEMORY HOOK
        st.success("""
        🔑 **Merksatz:** *"for = bekannte Anzahl, while = bis Bedingung"*
        
        Weißt du vorher, wie oft? → `for`. Weißt du es nicht? → `while`.
        """)
        
        # 👉 TRANSITION
        st.caption("👉 *Weiter in Tab 8: Wie bringt man Zufall ins Programm? → Random*")

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB 8: ZUFALL
    # ═══════════════════════════════════════════════════════════════════════════
    with tabs[7]:
        st.subheader("Zufall mit dem random-Modul")
        
        # 📍 CONNECTION
        st.info("""
        📍 **Verbindung zum Vorherigen:** Mit Schleifen kannst du Aktionen wiederholen.
        Aber was, wenn du **unvorhersehbare Ergebnisse** brauchst? Das `random`-Modul hilft!
        """)
        
        # 🧠 COGNITIVE SCAFFOLDING
        st.info("""
        🧠 **Verstehe zuerst: Kontrollierter Zufall**
        
        Computer sind **deterministisch** – sie berechnen immer dasselbe.
        Aber mit dem `random`-Modul simulieren wir Zufall:
        - Würfeln 🎲
        - Karten mischen 🃏
        - Zufällige Auswahl 🎯
        
        *random = kontrollierter Zufall für Spiele, Simulationen, Tests.*
        """)
        
        # 📖 THEORY
        with st.expander("📖 Theorie: random-Funktionen", expanded=True):
            st.markdown("""
            ```python
            import random
            ```
            
            | Funktion | Beschreibung | Beispiel |
            |----------|--------------|----------|
            | `random.randint(a, b)` | Zufällige Ganzzahl a bis b | `randint(1, 6)` → 🎲 |
            | `random.random()` | Float zwischen 0 und 1 | `0.7234...` |
            | `random.choice(liste)` | Zufälliges Element | `choice(["A", "B"])` |
            | `random.shuffle(liste)` | In-place mischen | Ändert Original |
            | `random.sample(liste, n)` | n Elemente ohne Zurücklegen | Neue Liste |
            """)
        
        # 📊 DIAGRAM – Simple visualization
        st.markdown("### 📊 Random-Funktionen Übersicht")
        render_diagram("""
            RANDOM [label="import random", fillcolor="#4a90e2", fontcolor="white"];
            
            INT [label="randint(a, b)\\nGanzzahl", fillcolor="#c8e6c9"];
            FLOAT [label="random()\\nFloat 0-1", fillcolor="#fff9c4"];
            CHOICE [label="choice(liste)\\n1 Element", fillcolor="#b3e5fc"];
            SHUFFLE [label="shuffle(liste)\\nMischen", fillcolor="#ffccbc"];
            
            RANDOM -> INT;
            RANDOM -> FLOAT;
            RANDOM -> CHOICE;
            RANDOM -> SHUFFLE;
        """, height=200)
        
        # 💻 LIVE CODE DEMO
        st.markdown("### 💻 Random in Aktion")
        
        with st.echo():
            # Schritt 1: random-Modul importieren
            import random  # Muss am Anfang stehen!

            # Schritt 2: Verschiedene Zufallsfunktionen
            # randint(a, b) - zufällige ganze Zahl zwischen a und b (inklusive!)
            dice = random.randint(1, 6)  # Wie ein Würfel: 1, 2, 3, 4, 5 oder 6
            print(f"Würfel: {dice}")

            # random() - zufällige Float-Zahl zwischen 0.0 und 1.0
            r = random.random()  # z.B. 0.7234...
            print(f"Random 0-1: {round(r, 4)}")  # Auf 4 Dezimalstellen runden

            # choice(liste) - zufälliges Element aus einer Liste auswählen
            colors = ["Rot", "Grün", "Blau"]  # Liste mit Farben
            pick = random.choice(colors)      # Wählt zufällig eine Farbe aus
            print(f"Zufällige Farbe: {pick}")  # z.B. "Rot" oder "Grün" oder "Blau"
        
        # 🎮 INTERACTIVE EXPLORATION
        st.markdown("### 🎮 Interaktiv: Würfeln")
        
        if st.button("🎲 Würfeln!", key="dice_roll"):
            dice_result = random.randint(1, 6)
            st.metric("Ergebnis", f"🎲 {dice_result}")
        
        st.markdown("### 🎮 Münzwurf-Simulation")
        
        num_flips = st.slider("Anzahl Würfe:", 10, 1000, 100, key="coin_flips")
        
        if st.button("Münzen werfen", key="coin_btn"):
            heads = 0
            tails = 0
            
            for _ in range(num_flips):
                if random.random() < 0.5:
                    heads = heads + 1
                else:
                    tails = tails + 1
            
            heads_pct = round(heads / num_flips * 100, 1)
            tails_pct = round(tails / num_flips * 100, 1)
            
            st.code(f"""
# Simulation mit {num_flips} Würfen
heads = 0
tails = 0

for _ in range({num_flips}):
    if random.random() < 0.5:
        heads += 1
    else:
        tails += 1

# Ergebnis:
print(f"Kopf: {heads} ({heads_pct}%)")
print(f"Zahl: {tails} ({tails_pct}%)")
""", language="python")
            
            col1, col2 = st.columns(2)
            col1.metric("Kopf", f"{heads} ({heads_pct}%)")
            col2.metric("Zahl", f"{tails} ({tails_pct}%)")
        
        # ⚠️ ERROR PREVENTION
        with st.expander("⚠️ Häufige Fehler", expanded=False):
            st.markdown("""
            **Fehler 1: import vergessen**
            ```python
            # ❌ FALSCH
            dice = randint(1, 6)  # NameError!
            
            # ✅ RICHTIG
            import random
            dice = random.randint(1, 6)
            ```
            
            **Fehler 2: shuffle() Rückgabewert**
            ```python
            # ❌ FALSCH – shuffle gibt None zurück!
            cards = [1, 2, 3]
            shuffled = random.shuffle(cards)  # shuffled ist None!
            
            # ✅ RICHTIG – shuffle ändert original
            random.shuffle(cards)  # cards ist jetzt gemischt
            ```
            
            **Fehler 3: randint ist inklusive!**
            ```python
            random.randint(1, 6)  # 1, 2, 3, 4, 5, oder 6
            # Beide Grenzen sind INKLUSIVE!
            ```
            """)
        
        # 🔑 MEMORY HOOK
        st.success("""
        🔑 **Merksatz:** *"random = kontrollierter Zufall"*
        
        Computer können keinen echten Zufall – aber `random` simuliert ihn gut genug für Spiele und Tests!
        """)
        
        # 👉 TRANSITION
        st.caption("👉 *Weiter in Tab 9: Jetzt wird geübt! → Praktische Übungen*")

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB 9: ÜBUNGEN
    # ═══════════════════════════════════════════════════════════════════════════
    with tabs[8]:
        st.subheader("💻 Praktische Programmierübungen")
        
        st.markdown("""
        **5 progressive Übungen** – von einfach bis fortgeschritten!
        Jede Übung baut auf den vorherigen Konzepten auf.
        """)
        

        ex_tabs = st.tabs([
            "1️⃣ Variablen",
            "2️⃣ Typen",
            "3️⃣ Rechner",
            "4️⃣ Ratespiel",
            "5️⃣ Programm",
            "6️⃣ Algorithmus-Training"
        ])
        
        # --- EXERCISE 1: Variable Calculator ---
        with ex_tabs[0]:
            st.markdown("### Übung 1: Variablen-Steckbrief ⭐")
            
            st.success("💡 **Lernziel:** Variablen erstellen und F-Strings nutzen.")
            
            st.markdown("""
            **Aufgabe:** Erstelle Variablen für deinen Steckbrief und gib ihn aus.
            """)
            
            with st.expander("📝 Lösung anzeigen", expanded=False):
                st.code("""
name = "Max"
age = 20
city = "Berlin"
hobby = "Programmieren"

print(f"Name: {name}")
print(f"Alter: {age}")
print(f"Stadt: {city}")
print(f"Hobby: {hobby}")
                """, language="python")
            
            st.markdown("### 🎮 Interaktiv: Dein Steckbrief")
            
            ex_name = st.text_input("Dein Name:", "Student", key="ex1_name")
            ex_age = st.number_input("Dein Alter:", 1, 120, 20, key="ex1_age")
            
            with st.echo():
                # Schritt 1: Eingaben aus den Widgets übernehmen
                profile_name = ex_name  # Name aus Textfeld
                profile_age = ex_age    # Alter aus Zahlenfeld

                # Schritt 2: Informationen mit F-Strings ausgeben
                print(f"Name: {profile_name}")      # Eingabe-Name anzeigen
                print(f"Alter: {profile_age}")      # Eingabe-Alter anzeigen
                print(f"In 10 Jahren: {profile_age + 10}")  # Berechnung: Alter + 10
        
        # --- EXERCISE 2: Type Converter ---
        with ex_tabs[1]:
            st.markdown("### Übung 2: Typ-Konverter ⭐⭐")
            
            st.success("💡 **Lernziel:** Typ-Konversion beherrschen.")
            
            st.markdown("""
            **Aufgabe:** Konvertiere Eingaben in verschiedene Typen.
            """)
            
            with st.expander("📝 Lösung anzeigen", expanded=False):
                st.code("""
text = "42.5"
as_float = float(text)
as_int = int(as_float)
as_str = str(as_int)

print(f"Original: '{text}' (str)")
print(f"Als float: {as_float}")
print(f"Als int: {as_int}")
print(f"Zurück als str: '{as_str}'")
                """, language="python")
            
            ex_input = st.text_input("Eingabe:", "42.5", key="ex2_input")
            
            with st.echo():
                # Schritt 1: Eingabe übernehmen
                original = ex_input  # Text aus dem Eingabefeld

                # Schritt 2: Typ-Konversion mit Fehlerbehandlung
                try:  # Versuche diese Operationen...
                    as_float = float(original)  # String zu Float konvertieren
                    as_int = int(as_float)      # Float zu Integer (schneidet Dezimalen ab)
                    print(f"Original: '{original}'")  # Originaltext in Anführungszeichen
                    print(f"Als float: {as_float}")   # Als Dezimalzahl
                    print(f"Als int: {as_int}")       # Als ganze Zahl
                except:  # Wenn ein Fehler auftritt...
                    print("Konversion fehlgeschlagen!")  # Fehlermeldung ausgeben
        
        # --- EXERCISE 3: Calculator ---
        with ex_tabs[2]:
            st.markdown("### Übung 3: Temperatur-Umrechner ⭐⭐")
            
            st.success("💡 **Lernziel:** Arithmetik und Formeln anwenden.")
            
            st.markdown("""
            **Aufgabe:** Celsius ↔ Fahrenheit umrechnen.
            
            Formeln:
            - F = C * 9/5 + 32
            - C = (F - 32) * 5/9
            """)
            
            direction = st.radio("Richtung:", ["C → F", "F → C"], key="ex3_dir")
            temp_input = st.number_input("Temperatur:", value=20.0, key="ex3_temp")
            
            st.code(f"""
if direction == "C -> F":
    celsius = {temp_input}
    fahrenheit = celsius * 9/5 + 32
    print(f"{{celsius}}C = {{fahrenheit:.1f}}F")
else:
    fahrenheit = {temp_input}
    celsius = (fahrenheit - 32) * 5/9
    print(f"{{fahrenheit}}F = {{celsius:.1f}}C")
""", language="python")
            
            # Schritt 1: Richtung prüfen und konvertieren
            if direction == "C -> F":  # Celsius nach Fahrenheit
                celsius = temp_input                    # Eingabetemperatur
                fahrenheit = celsius * 9/5 + 32        # Formel: F = C * 9/5 + 32
                print(f"{celsius}C = {fahrenheit:.1f}F") # Ausgabe mit 1 Dezimalstelle
            else:  # Fahrenheit nach Celsius
                fahrenheit = temp_input                 # Eingabetemperatur
                celsius = (fahrenheit - 32) * 5/9      # Formel: C = (F - 32) * 5/9
                print(f"{fahrenheit}F = {celsius:.1f}C") # Ausgabe mit 1 Dezimalstelle
        
        # --- EXERCISE 4: Number Guessing ---
        with ex_tabs[3]:
            st.markdown("### Übung 4: Zahlen-Ratespiel ⭐⭐⭐")
            
            st.success("💡 **Lernziel:** If-Else, Schleifen und Random kombinieren.")
            
            if 'secret_number' not in st.session_state:
                st.session_state.secret_number = random.randint(1, 100)
                st.session_state.attempts = 0
            
            guess = st.number_input("Deine Zahl (1-100):", 1, 100, 50, key="ex4_guess")
            
            if st.button("Raten!", key="ex4_btn"):
                st.session_state.attempts += 1
                
                with st.echo():
                    # Schritt 1: Daten aus Session-State holen
                    target = st.session_state.secret_number  # Die versteckte Zahl
                    my_guess = guess                        # Die geratene Zahl
                    attempts = st.session_state.attempts     # Anzahl Versuche

                    # Schritt 2: Vergleich mit if-elif-else
                    if my_guess == target:  # Richtig geraten!
                        print(f"🎉 Richtig! In {attempts} Versuchen!")
                    elif my_guess < target:  # Zu niedrig
                        print("⬆️ Höher!")  # Hinweis: höher raten
                    else:  # my_guess > target (zu hoch)
                        print("⬇️ Niedriger!")  # Hinweis: niedriger raten
                
                if guess == st.session_state.secret_number:
                    st.balloons()
                    st.success(f"Glückwunsch! Die Zahl war {st.session_state.secret_number}!")
                    if st.button("Neues Spiel", key="ex4_new"):
                        st.session_state.secret_number = random.randint(1, 100)
                        st.session_state.attempts = 0
                        st.rerun()
            
            st.caption(f"Versuche: {st.session_state.attempts}")
        
        # --- EXERCISE 5: Mini Program ---
        with ex_tabs[4]:
            st.markdown("### Übung 5: Einkaufslisten-Rechner ⭐⭐⭐⭐")
            
            st.success("💡 **Lernziel:** Alle Konzepte kombinieren!")
            
            st.markdown("""
            **Aufgabe:** Berechne den Gesamtpreis einer Einkaufsliste.
            """)
            
            st.code("""
# Einkaufsliste
items = ["Brot", "Milch", "Aepfel", "Kaese"]
prices = [2.50, 1.20, 3.00, 4.50]

total = 0
print("=== EINKAUFSLISTE ===")
for i, item in enumerate(items):
    price = prices[i]
    print(f"{i+1}. {item}: {price:.2f} Euro")
    total = total + price

print(f"\\nGesamt: {total:.2f} Euro")

tax = total * 0.19
print(f"MwSt (19%): {tax:.2f} Euro")
print(f"Mit MwSt: {total + tax:.2f} Euro")
""", language="python")

            # Execute logic for display (redundant but needed for output if we want to show it below)
            # Actually for this exercise we can just show the metric results below
            total = 2.5 + 1.2 + 3.0 + 4.5
            
            brutto_calc = total * 1.19
            col1, col2 = st.columns(2)
            col1.metric("Netto", f"{total:.2f}€")
            col2.metric("Brutto", f"{brutto_calc:.2f}€")

            col1.metric("Netto", f"{total:.2f}€")
            col2.metric("Brutto", f"{brutto_calc:.2f}€")

        # --- EXERCISE 6: Algorithm Training (New from Raw Logic Tasks) ---
        with ex_tabs[5]:
            st.markdown("### 🧠 Algorithmus-Training")
            st.info("Hier trainieren wir algorithmisches Denken mit Schleifen (wie im CS-Studium).")

            with st.expander("👉 Task 1: Zahlen-Kette (1-50)", expanded=True):
                st.markdown("Erstelle einen String `solution1`, der alle Zahlen von 1 bis 49 enthält (**ohne** Leerzeichen).")
                st.code('Expected: "1234567891011...49"', language="text")
                
                with st.echo():
                    solution1 = ""
                    # range(1, 50) geht von 1 bis 49
                    for i in range(1, 50):
                        solution1 = solution1 + str(i)
                    
                    # Überprüfung (nur Anfang und Ende zeigen)
                    print(f"Start: {solution1[:15]}...")
                    print(f"Ende: ...{solution1[-5:]}")
                    print(f"Länge: {len(solution1)}")

            with st.expander("👉 Task 2: Gerade Zahlen (2-50)"):
                st.markdown("Erstelle einen String `solution2` mit allen **geraden** Zahlen von 2 bis 48.")
                st.code('Expected: "24681012...48"', language="text")
                
                with st.echo():
                    solution2 = ""
                    # Schrittweite 2 nutzen!
                    for i in range(2, 50, 2):
                        solution2 = solution2 + str(i)
                        
                    print(f"Ergebnis: {solution2[:20]}...")

            with st.expander("👉 Task 3: Quersummen-Kette (100-200)"):
                st.markdown("Für jede Zahl von 100 bis 199: Berechne die Quersumme (Digit Sum) und hänge sie an.")
                st.markdown("""
                Beispiel:
                - 100 -> 1+0+0 = 1
                - 101 -> 1+0+1 = 2
                - ...
                - String: "12345..."
                """)
                
                with st.echo():
                    solution3 = ""
                    
                    for num in range(100, 200):
                        # 1. Zahl in String wandeln um an Ziffern zu kommen
                        digits = str(num)
                        
                        # 2. Ziffern summieren (Innere Schleife)
                        digit_sum = 0
                        for d in digits:
                            digit_sum = digit_sum + int(d)
                            
                        # 3. Ergebnis an solution3 anhängen
                        solution3 = solution3 + str(digit_sum)
                        
                    print(f"Ergebnis-Start: {solution3[:20]}...")
                    
                    # Test: Die ersten 5 sind 100->1, 101->2, 102->3, 103->4, 104->5
                    # Also "12345..."
    # TAB 10: QUIZ & ZUSAMMENFASSUNG
    # ═══════════════════════════════════════════════════════════════════════════
    with tabs[9]:
        st.subheader("📝 Quiz & Kapitel-Zusammenfassung")
        
        quiz_questions = [
            {
                "q": "Was ist der Unterschied zwischen = und ==?",
                "opts": ["Kein Unterschied", "= weist zu, == vergleicht", "= vergleicht, == weist zu", "Beide werfen Fehler"],
                "correct": 1,
                "exp": "= ist Zuweisung (x = 5), == ist Vergleich (x == 5)"
            },
            {
                "q": "Welcher Typ ist `3.14`?",
                "opts": ["int", "float", "str", "bool"],
                "correct": 1,
                "exp": "Zahlen mit Dezimalpunkt sind float (Fließkommazahlen)"
            },
            {
                "q": "Was gibt `7 // 2` zurück?",
                "opts": ["3.5", "3", "4", "Error"],
                "correct": 1,
                "exp": "// ist Ganzzahl-Division, schneidet Dezimalen ab: 7/2=3.5 → 3"
            },
            {
                "q": "Was macht `f'Hallo {name}'`?",
                "opts": ["Gibt 'Hallo {name}' aus", "Setzt Variablen-Wert ein", "Fehler", "Erstellt Variable"],
                "correct": 1,
                "exp": "F-Strings (mit f vor String) setzen Variablenwerte in {} ein"
            },
            {
                "q": "Was fehlt: `if x > 5` (Fehler!)",
                "opts": ["Klammern", "Doppelpunkt :", "Semikolon ;", "Einrückung"],
                "correct": 1,
                "exp": "if-Statements brauchen einen Doppelpunkt am Ende: if x > 5:"
            },
            {
                "q": "Welche Schleife, wenn Anzahl bekannt?",
                "opts": ["while", "for", "if", "switch"],
                "correct": 1,
                "exp": "for für bekannte Anzahl (range), while für unbekannte (bis Bedingung)"
            },
            {
                "q": "Was gibt `range(5)` zurück?",
                "opts": ["1,2,3,4,5", "0,1,2,3,4", "0,1,2,3,4,5", "5,4,3,2,1"],
                "correct": 1,
                "exp": "range(n) startet bei 0 und endet VOR n: 0,1,2,3,4"
            },
            {
                "q": "Was macht `random.randint(1, 6)`?",
                "opts": ["Immer 1 oder 6", "1 bis 5", "1 bis 6 (inklusive)", "0 bis 6"],
                "correct": 2,
                "exp": "randint ist inklusive beider Grenzen: 1, 2, 3, 4, 5, oder 6"
            }
        ]
        
        st.markdown("### 🎯 Teste dein Wissen!")
        
        if 'pb_quiz_score' not in st.session_state:
            st.session_state.pb_quiz_score = 0
            st.session_state.pb_quiz_submitted = False
        
        answers = {}
        for i, q in enumerate(quiz_questions):
            st.markdown(f"**Frage {i+1}:** {q['q']}")
            answers[i] = st.radio(
                f"Antwort {i+1}:",
                q['opts'],
                key=f"pb_quiz_q{i}",
                index=None,
                label_visibility="collapsed"
            )
        
        if st.button("🎯 Quiz auswerten", key="pb_quiz_submit"):
            score = 0
            for i, q in enumerate(quiz_questions):
                if answers[i] and q['opts'].index(answers[i]) == q['correct']:
                    score += 1
            
            st.session_state.pb_quiz_score = score
            st.session_state.pb_quiz_submitted = True
        
        if st.session_state.pb_quiz_submitted:
            pct = (st.session_state.pb_quiz_score / len(quiz_questions)) * 100
            
            if pct >= 75:
                st.success(f"🎉 Ausgezeichnet! {st.session_state.pb_quiz_score}/{len(quiz_questions)} ({pct:.0f}%)")
                st.balloons()
            elif pct >= 50:
                st.warning(f"📚 Gut! {st.session_state.pb_quiz_score}/{len(quiz_questions)} ({pct:.0f}%) – Wiederhole die schwächeren Themen.")
            else:
                st.error(f"📖 {st.session_state.pb_quiz_score}/{len(quiz_questions)} ({pct:.0f}%) – Lies das Kapitel nochmal durch!")
            
            with st.expander("📖 Erklärungen"):
                for i, q in enumerate(quiz_questions):
                    correct_ans = q['opts'][q['correct']]
                    st.markdown(f"**Frage {i+1}:** {correct_ans}")
                    st.caption(q['exp'])
        
        st.divider()
        
        # --- SUMMARY ---
        st.markdown("## 🎓 Kapitel-Zusammenfassung")
        
        st.success("""
        **🎉 Geschafft!** Du beherrschst jetzt die Python-Grundlagen:
        
        **Python** → **Variablen** → **Typen** → **Arithmetik** → **I/O** → **If-Else** → **Schleifen** → **Random**
        """)
        
        with st.expander("🔑 Alle Merksätze", expanded=True):
            st.markdown("""
            | Konzept | Merksatz |
            |---------|----------|
            | **Python** | *"Produktivität vor Performance"* |
            | **Variablen** | *"Variable = Beschriftete Schublade"* |
            | **Datentypen** | *"Typ bestimmt, was du tun kannst"* |
            | **Arithmetik** | *"// schneidet ab, / gibt Komma"* |
            | **F-Strings** | *"f vor String = Formatierung an"* |
            | **If-Else** | *"Wenn-Dann-Sonst = If-Elif-Else"* |
            | **Schleifen** | *"for = bekannte Anzahl, while = bis Bedingung"* |
            | **Random** | *"random = kontrollierter Zufall"* |
            """)
        
        st.info("""
        ➡️ **Weiter geht's in Kapitel 3: Kontrollstrukturen & Funktionen**
        
        Du vertiefst Boolean-Logik, lernst Funktionen zu definieren, und arbeitest mit Listen und Tuples!
        """)



