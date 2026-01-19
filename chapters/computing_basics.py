import streamlit as st
import plotly.graph_objects as go
import math
import numpy as np
from infrastructure import render_diagram

TITLE = "01. Computing Basics"

def run():
    st.header("1. Informatik & Computing Basics")

    # --- 0. INTRODUCTION ---
    st.markdown("""
    > *"Die Frage ist nicht 'Wie benutze ich einen Computer?' – sondern 'Wie funktioniert er wirklich?'"*
    """)

    with st.expander("🎯 Lernziele – Was du nach diesem Kapitel kannst", expanded=True):
        st.markdown("""
        | Nr. | Konzept | Du lernst... |
        |-----|---------|--------------|
        | 1 | **Informatik Grundlagen** | Warum Informatik mehr ist als nur Programmieren |
        | 2 | **Bits & Informationsdarstellung** | Wie Bilder, Text und Zahlen nur aus 0 und 1 bestehen |
        | 3 | **Zahlensysteme** | Wie man nahtlos zwischen Dezimal, Binär und Hex wechselt |
        | 4 | **Logik & Hardware** | Wie Strom zu "Denken" wird (Logikgatter, Transistoren) |
        | 5 | **CPU Architektur** | Wie der Prozessor Befehle abarbeitet |
        """)

    st.info("""
    compass **Kapitel-Roadmap:**
    Wir graben uns von der Oberfläche (Apps) tief hinunter bis zur Hardware (Strom), 
    um zu verstehen, wie aus Elektrizität Intelligenz wird.
    """)

    # Definition der Tabs
    tabs = st.tabs([
        "🎓 Was ist Informatik?", 
        "💡 Bits & Bytes", 
        "🔢 Zahlensysteme", 
        "🧠 Logik", 
        "🔌 Transistoren", 
        "➕ Addierer", 
        "⚙️ CPU", 
        "💻 Übungen", 
        "📝 Quiz"
    ])

    # --- TAB 1: WAS IST INFORMATIK? ---
    with tabs[0]:
        st.subheader("Computer Science = Effiziente Automatisierung")

        # 1. Connection
        st.info("""
        📍 **Einstieg:** Wahrscheinlich nutzt du Computer jeden Tag. Aber weißt du, was im Hintergrund passiert, 
        wenn du auf "Senden" klickst?
        """)

        # 2. Cognitive Scaffolding
        st.info("""
        🧠 **Verstehe zuerst:** Informatik ist wie **Kochen**.
        
        *   **Algorithmus:** Das Rezept (Schritt-für-Schritt Anleitung).
        *   **Programmierung:** Das Aufschreiben des Rezepts.
        *   **Computer:** Der Koch, der es stur befolgt.
        *   **Informatik:** Die Wissenschaft, wie man *neue, bessere* Rezepte erfindet.
        """)

        # 3. Theory
        with st.expander("📖 Theorie: Die 4 Säulen", expanded=True):
            st.markdown("""
            Informatik ist NICHT nur Programmieren. Es ist die Wissenschaft der **systematischen Informationsverarbeitung**.
            
            | Bereich | Frage | Beispiel |
            |---|---|---|
            | **Theoretische Informatik** | Was ist berechenbar? | Mathe, Komplexität, Logik |
            | **Technische Informatik** | Wie baut man Computer? | CPU, Chips, Netzwerke |
            | **Praktische Informatik** | Wie baut man Software? | Programmieren, Algorithmen |
            | **Angewandte Informatik** | Wo nutzt man es? | Medizin, KI, Wirtschaft |
            """)

        # 4. Diagram
        render_diagram("""
            graph TD;
                CS[Informatik 🎓] --> TI[Technische Inf.<br/>(Hardware) 🔌];
                CS --> PI[Praktische Inf.<br/>(Software) 💾];
                CS --> AI[Angewandte Inf.<br/>(Einsatz) 🌍];
                CS --> TH[Theoretische Inf.<br/>(Mathe) 📐];
                
                style CS fill:#4a90e2,color:white
        """, height=250)

        # 5. Live Demo
        st.markdown("### 🛠 Live-Demo: Ein Algorithmus")
        st.write("Ein Algorithmus ist eine präzise Anweisung. Beispiel: 'Finde die größte Zahl'.")
        
        numbers_input = st.text_input("Zahlen (kommagetrennt):", "5, 12, 3, 99, 1", key="tab1_nums")
        
        with st.echo():
            # Schritt 1: Eingabe vom Benutzer in eine Liste von Zahlen umwandeln
            try:
                # Text "5, 12, 3" -> Liste [5, 12, 3]
                nums = [int(x.strip()) for x in numbers_input.split(",")]
                # int(x.strip()) wandelt jeden Text in eine Zahl um
                # .strip() entfernt Leerzeichen

                # Schritt 2: Maximum-Algorithmus (wie ein Koch, der das größte Gemüse sucht)
                # Start mit der ersten Zahl als vorläufiges Maximum
                current_max = nums[0]  # Annahme: erste Zahl ist das Maximum

                # Gehe durch jede Zahl in der Liste
                for x in nums:  # x ist die aktuelle Zahl, die wir prüfen
                    # Wenn diese Zahl größer ist als unser bisheriges Maximum...
                    if x > current_max:
                        # ...dann wird sie das neue Maximum!
                        current_max = x  # Update: neues Maximum gefunden

                # Schritt 3: Ergebnis ausgeben
                print(f"Das Maximum ist: {current_max}")  # Zeige das größte Element

            except ValueError:
                # Fehlerbehandlung: Wenn der Benutzer keinen gültigen Text eingibt
                print("Bitte gültige Zahlen eingeben!")

        # 6. Interactive Exploration
        st.markdown("### 🎮 Interaktiv: Abstraktions-Ebenen")
        level = st.select_slider("Zoome in den Computer:", 
                               options=["Anwendung", "Hochsprache", "Maschinencode", "Hardware", "Physik"])
        
        if level == "Anwendung":
            st.success("📱 **App:** Du drückst einen Button 'Foto senden'.")
        elif level == "Hochsprache":
            st.code("send_photo(image_data)", language="python")
        elif level == "Maschinencode":
            st.code("00101101 11000101 00010010", language="text")
        elif level == "Hardware":
            st.warning("🔌 **Chip:** Logikgatter schalten Stromkreise.")
        elif level == "Physik":
            st.error("⚡ **Elektronen:** Teilchen bewegen sich durch Silizium.")

        # 7. Error Prevention
        with st.expander("⚠️ Häufige Missverständnisse", expanded=False):
            st.markdown("""
            **Mythos: "Ich muss gut in Mathe sein."**
            Logisches Denken ist wichtiger als Kopfrechnen. Der Computer rechnet für dich!
            
            **Mythos: "Informatiker reparieren Drucker."**
            Das ist IT-Support. Informatiker *entwickeln* die Technologie von morgen.
            """)

        # 8. Memory Hook
        st.success("""
        🔑 **Merksatz:** "Hardware macht es möglich, Software macht es nützlich."
        """)

        # 9. Transition
        st.caption("👉 *Weiter in Tab 2: Woraus besteht diese 'Software' eigentlich? (Bits & Bytes)*")

    # --- TAB 2: BITS & BYTES ---
    with tabs[1]:
        st.subheader("Die Atome der Information")

        # 1. Connection
        st.info("""
        📍 **Verbindung:** Wir haben gesehen, dass wir dem Computer Anweisungen geben. 
        Aber wie versteht eine Maschine aus Metall und Strom unsere Sprache? Gar nicht. Sie versteht nur **Strom an** oder **Strom aus**.
        """)

        # 2. Scaffolding
        st.info("""
        🧠 **Verstehe zuerst:** Ein Bit ist wie ein **Lichtschalter**.
        
        *   Oben = AN = 1
        *   Unten = AUS = 0
        
        Mehr Zustände gibt es nicht. Aber wenn man *viele* Schalter hat, kann man komplexe Muster codieren.
        """)

        # 3. Theory
        with st.expander("📖 Theorie: Bit & Byte", expanded=True):
            st.markdown("""
            **Bit (Binary Digit):** Kleinste Einheit (0 oder 1).
            **Byte:** Eine Gruppe von 8 Bits.
            
            Damit kann man 256 verschiedene Werte darstellen ($2^8 = 256$).
            
            | Begriff | Größe | Anzahl Möglichkeiten |
            |---|---|---|
            | **Bit** | 1 | 2 (0, 1) |
            | **Nibble** | 4 | 16 |
            | **Byte** | 8 | 256 |
            | **Kilobyte** | 1024 Bytes | ~Tausend |
            """)

        # 4. Diagram
        render_diagram("""
            graph LR;
                Bit[Bit (0/1)] --> Byte[Byte (8 Bits)];
                Byte --> KB[Kilobyte (1024 Bytes)];
                KB --> MB[Megabyte (1024 KB)];
                MB --> GB[Gigabyte (1024 MB)];
                GB --> TB[Terabyte (1024 GB)];
                
                style Bit fill:#fff9c4
                style Byte fill:#ffe0b2
        """, height=200)

        # 5. Live Demo
        st.markdown("### 🛠 Live-Demo: Text zu Bits")
        
        text_input = st.text_input("Gib ein Wort ein:", "Hallo", key="tab2_text")
        
        with st.echo():
            # Wie der Computer Text in Bits umwandelt (Zeichen für Zeichen)
            binary_output = []  # Liste zum Sammeln der Ergebnisse

            # Für jedes Zeichen im eingegebenen Text...
            for char in text_input:  # char ist z.B. 'H', 'a', 'l', 'l', 'o'
                # Schritt 1: ASCII-Code ermitteln
                # ord() gibt den numerischen ASCII-Wert zurück
                code = ord(char)  # 'A' -> 65, 'a' -> 97, '0' -> 48

                # Schritt 2: Zahl in 8-stellige Binärzahl umwandeln
                # format(code, '08b') = "00000000" bis "11111111"
                bits = format(code, '08b')  # '08b' bedeutet: 8 Stellen, binär, mit führenden Nullen

                # Schritt 3: Ergebnis formatieren und speichern
                binary_output.append(f"{char}: {bits}")  # z.B. "H: 01001000"

            # Schritt 4: Alle Zeilen ausgeben
            for line in binary_output:  # Gehe durch jede Zeile
                print(line)  # Zeige "H: 01001000" etc.

        # 6. Interactive Exploration
        st.markdown("### 🎮 Interaktiv: Das Binär-Pixel")
        st.write("Jedes Pixel auf deinem Schirm ist nur eine Zahl (Rot, Grün, Blau).")
        
        r = st.slider("Rot", 0, 255, 100)
        g = st.slider("Grün", 0, 255, 50)
        b = st.slider("Blau", 0, 255, 200)
        
        color_hex = f"#{r:02x}{g:02x}{b:02x}"
        st.markdown(f"""
        <div style='background-color: {color_hex}; width: 100px; height: 100px; border-radius: 10px;'></div>
        """, unsafe_allow_html=True)
        
        st.code(f"RGB({r}, {g}, {b}) = Binär: {format(r,'08b')} {format(g,'08b')} {format(b,'08b')}")

        # 7. Error Prevention
        with st.expander("⚠️ Häufige Fehler", expanded=False):
            st.markdown("""
            **Fehler: Kilobyte vs Kibibyte**
            
            *   In der Physik ist Kilo = 1000 ($10^3$).
            *   In der Informatik ist Kilo oft 1024 ($2^{10}$).
            
            Festplatten-Hersteller nutzen oft 1000 (um größer zu wirken), Windows nutzt 1024. 
            Deshalb hat deine "1 TB" Platte in Windows nur "931 GB".
            """)

        # 8. Memory Hook
        st.success("""
        🔑 **Merksatz:** "8 Bits sind ein Byte – wie 8 Buchstaben ein Wort ergeben."
        """)

        # 9. Transition
        st.caption("👉 *Weiter in Tab 3: Wie zählen wir mit Nullen und Einsen? (Zahlensysteme)*")

    # --- TAB 3: NUMBER SYSTEMS ---
    with tabs[2]:
        st.subheader("Die Sprache der Zahlen: Binär, Dezimal, Hex")

        # 1. Connection
        st.info("""
        📍 **Verbindung:** Wir wissen, dass alles Bits sind. Aber wie wird `00101010` zur Zahl 42? 
        Und warum sehen Fehlercodes oft so aus: `0x4F`?
        """)

        # 2. Scaffolding
        st.info("""
        🧠 **Verstehe zuerst:** Denk an einen **Kilometerzähler**.
        
        *   **Dezimal:** Ziffern 0-9. Nach der 9 springt die nächste Stelle um. ($10^x$)
        *   **Binär:** Ziffern 0-1. Nach der 1 springt die nächste Stelle um. ($2^x$)
        *   **Hex:** Ziffern 0-9, A-F. Erst nach F (15) springt es um. ($16^x$)
        """)

        # 3. Theory (Interactive Table)
        with st.expander("📖 Theorie: Stellenwert-Systeme", expanded=True):
            cols = st.columns(3)
            with cols[0]:
                st.markdown("**Dezimal (Basis 10)**")
                st.markdown("Ziffern: 0-9")
                st.markdown("$14 = 1\\cdot10 + 4\\cdot1$")
            with cols[1]:
                st.markdown("**Binär (Basis 2)**")
                st.markdown("Ziffern: 0, 1")
                st.markdown("$1110 = 1\\cdot8 + 1\\cdot4 + 1\\cdot2 + 0\\cdot1 = 14$")
            with cols[2]:
                st.markdown("**Hex (Basis 16)**")
                st.markdown("Ziffern: 0-9, A-F")
                st.markdown("$E = 14$")

        # 4. Diagram
        render_diagram("""
            graph TD;
                DEC[Dezimal 42] --- BIN[Binär 101010];
                DEC --- HEX[Hex 2A];
                BIN --- HEX;
                
                style DEC fill:#e3f2fd
                style BIN fill:#fff3e0
                style HEX fill:#e8f5e9
        """, height=200)

        # 5. Live Demo
        st.markdown("### 🛠 Live-Demo: Konverter")
        
        val = st.number_input("Dezimalzahl eingeben:", 0, 255, 42, key="tab3_input")
        
        with st.echo():
            # Python-Funktionen für Zahlensystem-Konvertierung

            # Schritt 1: In Binär umwandeln
            b = bin(val)  # bin(42) = "0b101010" (0b zeigt Binär an)
            # Das '0b' ist nur ein Präfix, die eigentlichen Bits sind ab Position 2

            # Schritt 2: In Hexadezimal umwandeln
            h = hex(val)  # hex(42) = "0x2a" (0x zeigt Hex an)
            # Das '0x' ist nur ein Präfix, die eigentlichen Hex-Ziffern sind ab Position 2

            # Schritt 3: Reine Binär-/Hex-Zahlen extrahieren (ohne Präfix)
            b_raw = b[2:]  # "0b101010"[2:] = "101010"
            h_raw = h[2:].upper()  # "0x2a"[2:] = "2a" -> "2A" (groß schreiben)

            # Schritt 4: Alle Darstellungen anzeigen
            print(f"Dezimal: {val}")        # Für Menschen: 42
            print(f"Binär:   {b} (Raw: {b_raw})")  # 0b101010 (mit Präfix) und 101010 (rein)
            print(f"Hex:     {h} (Raw: {h_raw})")  # 0x2a (mit Präfix) und 2A (rein)

        # 6. Interactive Exploration
        st.markdown("### 🎮 Interaktiv: Der Binär-Abakus")
        st.write("Klicke die Bits an, um die Zahl zu bauen:")
        
        # 8 Checkboxes for 8 bits
        b_cols = st.columns(8)
        binary_val = 0
        bits_str = ""
        
        for i in range(8):
            power = 7 - i
            with b_cols[i]:
                is_on = st.checkbox(f"{2**power}", key=f"bit_{i}")
                if is_on:
                    binary_val += 2**power
                    bits_str += "1"
                else:
                    bits_str += "0"
        
        st.metric("Ergebnis (Dezimal)", binary_val)
        st.metric("Ergebnis (Hex)", hex(binary_val)[2:].upper())

        # 7. Error Prevention
        with st.expander("⚠️ Häufige Fehler", expanded=False):
            st.markdown("""
            **Warum Hex?**
            Hex ist keine "andere Art von Zahl", sondern nur eine **kompaktere Schreibweise** für Binär.
            Ein Byte (8 bit) passt immer perfekt in 2 Hex-Ziffern ($255 = FF$).
            Das ist einfacher zu lesen als `11111111`.
            """)

        # 8. Memory Hook
        st.success("""
        🔑 **Merksatz:** "Dezimal für Menschen (10 Finger), Binär für Maschinen (An/Aus)."
        """)

        # 9. Transition
        st.caption("👉 *Weiter in Tab 4: Wie rechnet der Computer damit? (Logik)*")

    # --- TAB 4: LOGIC GATES ---
    with tabs[3]:
        st.subheader("Boolesche Logik: Das Denken des Computers")

        # 1. Connection
        st.info("""
        📍 **Verbindung:** Wir haben Nullen und Einsen. Super. Aber ein Computer soll *Entscheidungen* treffen.
        "Wenn X und Y, dann Z." Das nennen wir **Logik**.
        """)

        # 2. Scaffolding
        st.info("""
        🧠 **Verstehe zuerst:** Du nutzt Logik jeden Tag.
        
        *   **AND:** Ich gehe raus wenn (Regen aufhört) **UND** (ich Zeit habe).
        *   **OR:** Ich esse (Pizza) **ODER** (Pasta).
        *   **NOT:** Ich bin (NICHT müde).
        """)

        # 3. Theory
        with st.expander("📖 Theorie: Die 3 Grundbausteine", expanded=True):
            st.markdown("""
            Ein Computer braucht nur 3 Operationen, um ALLES zu berechnen:
            
            | Gatter | Symbol | Erklärung | Wahrheitstabelle (A, B -> Out) |
            |---|---|---|---|
            | **AND** | `&` | Beide müssen 1 sein | 1,1 -> 1 (Sonst 0) |
            | **OR** | `|` | Einer muss 1 sein | 0,0 -> 0 (Sonst 1) |
            | **NOT** | `!` | Dreht den Wert um | 0->1, 1->0 |
            """)

        # 4. Diagram
        render_diagram("""
            graph LR;
                A[A] --> AND(AND);
                B[B] --> AND;
                AND --> Out[A & B];
                
                C[C] --> OR(OR);
                D[D] --> OR;
                OR --> Out2[C | D];
                
                E[E] --> NOT(NOT);
                NOT --> Out3[!E];
                
                style AND fill:#c8e6c9
                style OR fill:#ffe0b2
                style NOT fill:#ffcdd2
        """, height=200)

        # 5. Live Demo
        st.markdown("### 🛠 Live-Demo: Logik in Python")
        
        a_bool = st.checkbox("Input A", True, key="demo4_a")
        b_bool = st.checkbox("Input B", False, key="demo4_b")
        
        with st.echo():
            # Boolesche Logik in Python (wie echte Entscheidungen)

            # Schritt 1: Variablen für unsere Bedingungen
            is_rainy = a_bool        # True wenn Checkbox "Input A" angehakt
            have_umbrella = b_bool   # True wenn Checkbox "Input B" angehakt

            # Schritt 2: AND-Operation (UND - beide müssen wahr sein)
            # Bleibe ich trocken? Nur wenn es regnet UND ich einen Schirm habe
            stay_dry = is_rainy and have_umbrella  # True nur wenn beide True

            # Schritt 3: OR-Operation (ODER - mindestens einer muss wahr sein)
            # Werde ich nass? Wenn es regnet ODER ich keinen Schirm habe
            get_wet = is_rainy or (not have_umbrella)  # True wenn mindestens einer True
            # not have_umbrella dreht den Wert um: True -> False, False -> True

            # Schritt 4: Ergebnis anzeigen
            print(f"Bleibe ich trocken? {stay_dry}")  # True = ja, False = nein

        # 6. Interactive Exploration
        st.markdown("### 🎮 Interaktiv: Der Logik-Simulator")
        op = st.selectbox("Wähle Gatter:", ["AND", "OR", "XOR"], key="tab4_op")
        
        col1, col2, col3 = st.columns([1,1,2])
        with col1:
            in1 = st.toggle("Eingang 1", key="in1")
        with col2:
            in2 = st.toggle("Eingang 2", key="in2")
        
        with col3:
            if op == "AND":
                res = in1 and in2
            elif op == "OR":
                res = in1 or in2
            else: # XOR
                res = in1 != in2
            
            # Visualisierung als "Licht"
            light = "🟡 AN" if res else "⚫️ AUS"
            st.metric(f"Ausgang ({op})", light)

        # 7. Error Prevention
        with st.expander("⚠️ Häufige Fehler", expanded=False):
            st.markdown("""
            **Fehler: AND vs OR verwechseln**
            "Ich will alle Früchte außer Äpfel und Birnen".
            
            Logisch falsch: `NOT (Apple AND Pear)` -> Das heißt "Nicht beides gleichzeitig".
            Logisch richtig: `(NOT Apple) AND (NOT Pear)` -> Weder Apfel noch Birne.
            (De Morgan'sche Gesetze!)
            """)

        # 8. Memory Hook
        st.success("""
        🔑 **Merksatz:** "AND ist streng (beide), OR ist locker (einer reicht)."
        """)

        # 9. Transition
        st.caption("👉 *Weiter in Tab 5: Wie bauen wir diese Logik physikalisch? (Transistoren)*")

    # --- TAB 5: TRANSISTORS ---
    with tabs[4]:
        st.subheader("Transistoren: Die Hardware-Basis")

        # 1. Connection
        st.info("""
        📍 **Verbindung:** Logik ist mathematisch schön. Aber wie bringt man einem Stück Stein (Silizium) Logik bei?
        Man baut Schalter. Sehr, sehr kleine Schalter.
        """)

        # 2. Scaffolding
        st.info("""
        🧠 **Verstehe zuerst:** Ein Transistor ist wie ein **Wasserhahn**.
        
        *   **Source:** Das Wasser kommt aus der Wand.
        *   **Drain:** Das Wasser fließt in den Abfluss.
        *   **Gate:** Der Griff. Wenn man dreht (Strom anlegt), fließt Wasser.
        """)

        # 3. Theory
        with st.expander("📖 Theorie: Der MOSFET", expanded=True):
            st.markdown("""
            Prozessoren bestehen aus Milliarden von MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistor).
            
            *   **Gate Low (0V):** Schalter OFFEN (Kein Strom) -> 0
            *   **Gate High (5V):** Schalter GESCHLOSSEN (Strom fließt) -> 1
            
            Wir bauen Logikgatter, indem wir Transistoren in Reihe oder Parallel schalten.
            """)

        # 4. Diagram
        render_diagram("""
            graph TD;
                G[Gate (Steuerung)] --> T{Transistor};
                S[Source (Eingang)] --> T;
                T --> D[Drain (Ausgang)];
                
                style T fill:#b3e5fc
        """, height=200)

        # 5. Live Demo - NAND Construction
        st.markdown("### 🛠 Live-Demo: Das universelle NAND")
        st.write("Wusstest du, dass man mit nur einem Gatter-Typ (NAND) **jeden** Computer bauen kann?")
        
        with st.echo():
            # NAND-Gatter simulieren (das "universelle" Gatter)

            # Schritt 1: NAND-Funktion definieren
            # NAND = NOT AND (das Gegenteil von AND)
            def nand_gate(a, b):  # Nimmt zwei Eingänge (0 oder 1)
                if a == 1 and b == 1:  # Wenn BEIDE Eingänge 1 sind...
                    return 0  # ...dann ist Ausgang 0 (FALSE)
                return 1      # Sonst ist Ausgang 1 (TRUE)

            # Schritt 2: NOT-Gatter aus NAND bauen (der Trick!)
            # NOT dreht den Wert um: 0->1, 1->0
            def not_gate(a):  # Nimmt einen Eingang
                return nand_gate(a, a)  # Beide Eingänge gleich machen!
                # Wenn a=0: nand_gate(0,0) -> 1 (NOT 0 = 1)
                # Wenn a=1: nand_gate(1,1) -> 0 (NOT 1 = 0)

            # Schritt 3: Testen
            print(f"NOT(0) = {not_gate(0)}")  # Sollte 1 sein (Umkehrung von 0)
            print(f"NOT(1) = {not_gate(1)}")  # Sollte 0 sein (Umkehrung von 1)
            
        # 6. Interactive Exploration
        st.markdown("### 🎮 Interaktiv: Moore's Law")
        st.write("Wie viele Transistoren passen auf einen Chip?")
        
        year = st.slider("Jahr:", 1970, 2030, 2020)
        
        # Vereinfachtes Moore's Law: Verdopplung alle 2 Jahre
        # 1970 start bei ~2000
        transistors = 2300 * (2 ** ((year - 1971) / 2))
        
        def format_number(n):
            if n > 1e9: return f"{n/1e9:.1f} Milliarden"
            if n > 1e6: return f"{n/1e6:.1f} Millionen"
            return f"{int(n)}"
            
        st.metric("Anzahl Transistoren", format_number(transistors))
        
        if year > 2020:
            st.caption("⚠️ Physikalische Grenze: Atome sind nicht unendlich klein!")

        # 7. Error Prevention
        st.info("Transistoren sind analoge Bauteile, die digital genutzt werden. Wenn sie zu heiß werden, machen sie Fehler!")

        # 8. Memory Hook
        st.success("""
        🔑 **Merksatz:** "Transistoren sind die Ventile für den Stromfluss."
        """)

        # 9. Transition
        st.caption("👉 *Weiter in Tab 6: Und jetzt rechnen wir! (Addierer)*")

    # --- TAB 6: ADDERS ---
    with tabs[5]:
        st.subheader("Rechnen mit Strom: Der Addierer")

        # 1. Connection
        st.info("""
        📍 **Verbindung:** Wir haben Logik-Gatter (AND, XOR).
        Wenn wir die schlau verkabeln, können wir plötzlich **Mathe** machen.
        """)

        # 2. Scaffolding
        st.info("""
        🧠 **Verstehe zuerst:** Schriftliche Addition (Schule).
        
        ```
          1
        + 1
        ---
          0 (und 1 im Sinn -> Übertrag/Carry)
        ```
        
        Ein **Half-Adder** macht genau das für eine Stelle.
        """)

        # 3. Theory (Truth Table)
        with st.expander("📖 Theorie: Half Adder", expanded=True):
            st.markdown("""
            Ein Half-Adder nimmt 2 Bits (A, B) und gibt Summe (S) und Übertrag (Carry) aus.
            
            *   **Summe:** XOR (Entweder A oder B, aber nicht beide)
            *   **Carry:** AND (Nur wenn beide 1 sind)
            
            | A | B | Sum (XOR) | Carry (AND) |
            |---|---|---|---|
            | 0 | 0 | 0 | 0 |
            | 0 | 1 | 1 | 0 |
            | 1 | 0 | 1 | 0 |
            | 1 | 1 | 0 | 1 |
            """)

        # 4. Diagram
        render_diagram("""
            graph LR;
                A[Input A] --> XOR;
                B[Input B] --> XOR;
                A --> AND;
                B --> AND;
                
                XOR[XOR Gatter] --> S[Summe];
                AND[AND Gatter] --> C[Carry];
                
                style XOR fill:#ffe0b2
                style AND fill:#c8e6c9
        """, height=250)

        # 5. Live Demo
        st.markdown("### 🛠 Live-Demo: Adder Code")
        
        with st.echo():
            # Half-Adder simulieren (Addierer für eine Binärstelle)

            # Schritt 1: Half-Adder-Funktion definieren
            def half_adder(a, b):  # Zwei Bits addieren (0 oder 1)
                # XOR (^) für die Summe: 1 wenn genau eines der Bits 1 ist
                sum_bit = a ^ b    # 0^0=0, 0^1=1, 1^0=1, 1^1=0

                # AND (&) für den Übertrag: 1 nur wenn beide Bits 1 sind
                carry_bit = a & b  # 0&0=0, 0&1=0, 1&0=0, 1&1=1

                return sum_bit, carry_bit  # Zwei Werte zurückgeben

            # Schritt 2: Test mit 1 + 1
            s, c = half_adder(1, 1)  # s = summe, c = carry (übertrag)
            # 1 + 1 = 10 in Binär (Summe=0, Carry=1)

            # Schritt 3: Ergebnis anzeigen
            print(f"1 + 1 = {c}{s} (Binär für 2)")  # "10" binär = 2 dezimal

        # 6. Interactive Exploration
        st.markdown("### 🎮 Interaktiv: 4-Bit Rechner")
        
        c1, c2 = st.columns(2)
        val1 = c1.number_input("Zahl 1 (0-15)", 0, 15, 3, key="add1")
        val2 = c2.number_input("Zahl 2 (0-15)", 0, 15, 5, key="add2")
        
        res = val1 + val2
        
        st.write("---")
        # Visualisierung der Binär-Addition
        def to_bin(n): return format(n, '04b')
        
        st.text(f"  {to_bin(val1)} ({val1})")
        st.text(f"+ {to_bin(val2)} ({val2})")
        st.text(f"------")
        st.text(f"  {to_bin(res)} ({res})")
        
        if res > 15:
            st.warning("Overflow! (Wenn wir nur 4 Bits hätten, wäre das Ergebnis falsch)")

        # 7. Error Prevention
        with st.expander("⚠️ Häufige Fehler", expanded=False):
            st.markdown("""
            **Fehler: Overflow (Überlauf)**
            Wenn man `1111` (15) + `0001` (1) rechnet und nur 4 Bits Speicher hat, kommt `0000` (0) raus!
            Das Bit "links raus" geht verloren. Das hat schon Raketen abstürzen lassen (Ariane 5).
            """)

        # 8. Memory Hook
        st.success("""
        🔑 **Merksatz:** "Summe ist XOR, Übertrag ist AND."
        """)

        # 9. Transition
        st.caption("👉 *Weiter in Tab 7: Wer steuert diese ganzen Addierer? (CPU)*")

    # --- TAB 7: CPU ---
    with tabs[6]:
        st.subheader("Das Herz des Computers: Die CPU")

        # 1. Connection
        st.info("""
        📍 **Verbindung:** Jetzt haben wir alles:
        Logikgatter für Entscheidungen und Addierer für Mathe.
        Wenn man Milliarden davon kombiniert, erhält man eine **CPU** (Central Processing Unit).
        """)

        # 2. Scaffolding
        st.info("""
        🧠 **Verstehe zuerst:** Die CPU ist wie ein **Koch**.
        
        1.  **Fetch (Holen):** Koch liest den nächsten Schritt im Rezept.
        2.  **Decode (Verstehen):** Koch versteht "Eier schlagen".
        3.  **Execute (Ausführen):** Koch schlägt die Eier.
        4.  **Repeat:** Zurück zu Schritt 1.
        
        Der Koch macht stur, was im Rezept steht (Programm). Aber er ist *extrem* schnell (Milliarden Mal pro Sekunde).
        """)

        # 3. Theory
        with st.expander("📖 Theorie: Fetch-Decode-Execute Cycle", expanded=True):
            st.markdown("""
            Der "Maschinenzyklus" bestimmt alles, was dein Handy/Laptop tut:
            
            1.  **RAM:** Hier liegt das Programm (die Liste von Befehlen).
            2.  **CPU:** Liest Befehl für Befehl (FETCH), versteht ihn (DECODE) und führt ihn aus (EXECUTE).
            3.  **Clock (Takt):** Gibt das Tempo vor. 3 GHz = 3 Milliarden Takte pro Sekunde.
            """)

        # 4. Diagram
        render_diagram("""
            graph TD;
                RAM[RAM<br/>(Rezept)] -- 1. FETCH --> CPU[CPU<br/>(Koch)];
                CPU -- 2. DECODE --> CU[Control Unit];
                CU -- 3. EXECUTE --> ALU[ALU<br/>(Mathe & Logik)];
                ALU -- 4. STORE --> RAM;
                
                style CPU fill:#fff9c4
        """, height=250)

        # 5. Live Demo
        st.markdown("### 🛠 Live-Demo: Ein Mini-CPU Simulator")
        
        with st.echo():
            # Vereinfachter CPU-Simulator (Fetch-Decode-Execute Zyklus)

            # Schritt 1: Programm definieren (Liste von Befehlen)
            program = [
                ("LOAD", 10),  # Lade 10 in den Akkumulator (Arbeitsspeicher)
                ("ADD", 5),    # Addiere 5 zum aktuellen Wert
                ("STORE", "Ergebnis")  # Speichere Ergebnis (hier nur anzeigen)
            ]

            # Schritt 2: CPU-Zustand initialisieren
            accumulator = 0  # Der "Akkumulator" ist das Arbeitsgedächtnis der CPU

            print("--- CPU START ---")  # Computer einschalten

            # Schritt 3: Fetch-Decode-Execute Schleife (der Herzschlag der CPU)
            for instruction, value in program:  # Für jeden Befehl im Programm...

                if instruction == "LOAD":  # DECODE: Das ist ein Lade-Befehl
                    accumulator = value  # EXECUTE: Wert in Akkumulator laden
                    print(f"FETCH: LOAD {value} -> EXECUTE: Speicher = {accumulator}")

                elif instruction == "ADD":  # DECODE: Das ist ein Addier-Befehl
                    old = accumulator  # Merken des alten Werts für Ausgabe
                    # EXECUTE: Addiere zum Akkumulator (kein += wegen Safe Echo)
                    accumulator = accumulator + value
                    print(f"FETCH: ADD {value} -> EXECUTE: {old} + {value} = {accumulator}")

                elif instruction == "STORE":  # DECODE: Das ist ein Speicher-Befehl
                    # EXECUTE: Ergebnis "speichern" (hier nur anzeigen)
                    print(f"FETCH: STORE -> Resultat {accumulator} gespeichert.")

        # 6. Interactive Exploration
        st.markdown("### 🎮 Interaktiv: Taktfrequenz")
        ghz = st.slider("CPU Takt in GHz:", 0.1, 5.0, 1.0)
        
        cycles_per_sec = ghz * 1_000_000_000
        time_per_op = 1 / cycles_per_sec
        light_travel = 299792458 * time_per_op * 100 # cm
        
        st.metric("Operationen pro Sekunde", f"{cycles_per_sec:,.0f}")
        st.write(f"In einem Taktzyklus kommt Licht nur **{light_travel:.1f} cm** weit!")
        if light_travel < 5:
            st.warning("⚠️ Das Licht ist zu langsam für deinen Chip! (Deshalb werden CPUs nicht mehr viel schneller)")

        # 7. Error Prevention
        st.info("Programmierer denken oft 'Mein Code läuft sofort'. Aber für die CPU sind das Millionen von winzigen Schritten.")

        # 8. Memory Hook
        st.success("""
        🔑 **Merksatz:** "Fetch-Decode-Execute: Der Herzschlag des Computers."
        """)

        # 9. Transition
        st.caption("👉 *Weiter in Tab 8: Das waren viele Infos. Jetzt üben wir! (Übungen)*")

    # --- TAB 8: EXERCISES ---
    with tabs[7]:
        st.subheader("💻 Praktische Übungen")
        st.markdown("Hier wendest du dein Wissen an. Von der Theorie (Big O) bis zur Praxis (Variablen & Debugging).")
        
        # Expanded Tabs to include original content
        ex_tabs = st.tabs(["1️⃣ Binär & Logik", "2️⃣ Komplexität (Big O)", "3️⃣ Algorithmen (Pi)", "4️⃣ Debugging", "5️⃣ Assignment 1 (Basis)", "6️⃣ Komplexes Rechnen", "7️⃣ Chatbot Logic"])
        
        # --- EX SUBTAB 1: Binary & Logic (New from V2) ---
        with ex_tabs[0]:
            st.markdown("### 🔢 Binär & Logik Grundlagen")
            
            col1, col2 = st.columns(2)
            with col1:
                st.info("💡 **Aufgabe 1:** Konvertiere `10101` (Binär) im Kopf.")
                with st.expander("Lösung"):
                    st.write("16 + 4 + 1 = **21**")

            with col2:
                st.info("💡 **Aufgabe 2:** Was ergibt `1 AND 0 OR 1`?")
                with st.expander("Lösung"):
                    st.write("`(1 AND 0) OR 1` = `0 OR 1` = **1**")
            
            st.markdown("---")
            st.markdown("### 📝 Code-Analyse")
            st.code("""
accumulator = 0
data = [1, 0, 1, 0]

for bit in data:
    if bit == 1:
        accumulator = accumulator + 1
            """, language="python")
            
            if st.button("Was macht dieser Code?"):
                st.success("Er zählt die Anzahl der gesetzten Bits (Population Count). Ergebnis: 2")

        # --- EX SUBTAB 2: Big O (Restored) ---
        with ex_tabs[1]:
            st.markdown("### 🚀 Algorithmus-Geschwindigkeit (Big O)")
            st.markdown("""
            Ein Computer ist schnell, aber nicht unendlich schnell. 
            **Big O** beschreibt, wie viel langsamer ein Programm wird, wenn mehr Daten dazukommen.
            """)
            
            n_values = st.slider("Input-Größe (n):", 10, 1000, 100, 10)
            
            # Data generation for plot
            x_vals = list(range(10, n_values + 1, max(1, n_values // 100)))
            
            complexities = {
                "O(1) (Super schnell)": [1 for _ in x_vals],
                "O(log n) (Sehr gut)": [math.log2(n) for n in x_vals],
                "O(n) (Okay)": [n for n in x_vals],
                "O(n²) (Langsam)": [n**2 for n in x_vals],
            }
            
            fig = go.Figure()
            for name, y_vals in complexities.items():
                fig.add_trace(go.Scatter(x=x_vals, y=y_vals, name=name))
            
            fig.update_layout(title="Wie skalieren Algorithmen?", xaxis_title="Datenmenge (n)", yaxis_title="Rechenschritte", yaxis_type="log")
            st.plotly_chart(fig, use_container_width=True, key="fig_big_o")
            
            st.info("""
            *   **O(1):** Array-Zugriff `arr[5]` (Dauert immer gleich lang)
            *   **O(n):** Liste durchsuchen (Dauert doppelt so lang bei doppelter Datenmenge)
            *   **O(n²):** Doppelte Schleife `for i in n: for j in n:` (Explodiert bei vielen Daten!)
            """)

        # --- EX SUBTAB 3: Pi Approximation (Restored) ---
        with ex_tabs[2]:
            st.markdown("### 🥧 Die Leibniz-Reihe für Pi")
            st.markdown(r"$$ \pi = 4 \times (1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + ...) $$")
            
            n_terms = st.slider("Anzahl Iterationen:", 10, 2000, 100)
            
            if st.button("Pi berechnen"):
                pi_approx = 0
                history = []
                sign = 1
                denominator = 1
                
                for _ in range(n_terms):
                    term = 4 / denominator
                    pi_approx += sign * term
                    history.append(pi_approx)
                    sign *= -1
                    denominator += 2
                    
                err = abs(math.pi - pi_approx)
                st.metric("Ergebnis", f"{pi_approx:.5f}", delta=f"Fehler: {err:.5f}", delta_color="inverse")
                
                fig = go.Figure()
                fig.add_trace(go.Scatter(y=history, name="Näherung"))
                fig.add_hline(y=math.pi, line_color="green", annotation_text="Echtes Pi")
                fig.update_layout(title="Konvergenz gegen Pi")
                st.plotly_chart(fig, use_container_width=True, key="fig_pi_conv")

        # --- EX SUBTAB 4: Debugging (Restored) ---
        with ex_tabs[3]:
            st.markdown("### 🕵️‍♀️ Bug Hunter Quiz")
            st.write("Finde den Fehler im Code!")
            
            # Case 1
            st.markdown("**Fall 1:**")
            st.code('a = 5\nb = "5"\nc = a / b', language="python")
            q1 = st.radio("Was passiert?", ["Alles super", "TypeError (Zahl / Text)", "ZeroDivisionError"], key="bug1")
            if q1 == "TypeError (Zahl / Text)":
                st.success("Richtig! Man kann nicht durch Text teilen.")
            elif q1:
                 st.error("Falsch. Python weiß nicht, wie man durch einen String teilt.")
                 
            st.divider()
            
            # Case 2
            st.markdown("**Fall 2:**")
            st.code('def greet(name):\n    print("Hi " + name\ngreet("Bob")', language="python")
            q2 = st.radio("Was ist hier kaputt?", ["NameError", "SyntaxError (Klammer fehlt)", "IndentationError"], key="bug2")
            if q2 == "SyntaxError (Klammer fehlt)":
                st.success("Korrekt! Die Klammer `)` in Zeile 2 fehlt.")
            elif q2:
                st.error("Falsch. Schau dir Zeile 2 genau an.")

            st.divider()

            # Case 3 (Task 3.1 from JSON)
            st.markdown("**Fall 3:**")
            st.code('a = 5\nb = a - 5\nc = a / b', language="python")
            q3 = st.radio("Was passiert hier?", ["NameError", "ZeroDivisionError", "Alles ok"], key="bug3")
            if q3 == "ZeroDivisionError":
                st.success("Richtig! `b` ist 0 (5-5), und durch 0 teilen geht nicht.")
            elif q3:
                st.error("Falsch. Berechne mal den Wert von `b`.")

            st.divider()

            # Case 4 (Task 3.3 from JSON)
            st.markdown("**Fall 4:**")
            st.code('a = 5\nb = a - 3\nc = str(a - b)\n# Vergleich: ist c größer als 7?\ncheck = c > 7', language="python")
            q4 = st.radio("Das Problem ist:", ["c ist nicht definiert", "TypeError (Vergleich Str mit Int)", "Rechenfehler"], key="bug4")
            if q4 == "TypeError (Vergleich Str mit Int)":
                st.success("Korrekt! `c` ist ein String ('2'), `7` ist ein Int. Die kann man in Python 3 nicht vergleichen.")
            elif q4:
                 st.error("Falsch. `c` wird definiert, aber achte auf `str()`.")

            st.divider()

            # Case 5 (Task 3.4 from JSON)
            st.markdown("**Fall 5:**")
            st.code('a = 5\nb = a - 3\nr = a - b\n# Wir testen das Ergebnis\nassert r == 3', language="python")
            st.write("(Hinweis: Wenn im Code `assert_equal(c, 3)` stünde...)")
            q5 = st.radio("Finde den Fehler im Original:", ["Variable c nicht definiert", "AssertionError (falscher Wert)", "Syntax fehler"], key="bug5")
            if q5 == "Variable c nicht definiert":
                 st.success("Richtig! Im Original-Task wurde `c` überprüft, aber nur `r` berechnet.")
            elif q5:
                 st.error("Falsch. Schau welche Variablen definiert wurden.")

        # --- EX SUBTAB 5: Assignment 1 (Restored) ---
        with ex_tabs[4]:
            st.markdown("### 🏗 Assignment 1: Programming Basics")
            st.info("Das ist dein erstes echtes Coding-Assignment. Setze es in deiner IDE um!")
            
            with st.expander("👉 Task 1: Variablen & Rechnen", expanded=True):
                st.markdown("Definiere Variablen und rechne mit ihnen.")
                with st.echo():
                    # Schritt 1: Variablen definieren
                    x = 10  # Erste Zahl
                    y = 4   # Zweite Zahl

                    # Schritt 2: Grundrechenarten
                    add = x + y   # Addition: 10 + 4 = 14
                    sub = x - y   # Subtraktion: 10 - 4 = 6
                    mul = x * y   # Multiplikation: 10 * 4 = 40
                    div = x / y   # Division: 10 / 4 = 2.5 (immer float in Python 3!)
                    pow_ = x ** y # Potenz: 10^4 = 10 * 10 * 10 * 10 = 10000

                    # Schritt 3: Ergebnis anzeigen mit Typ-Info
                    print(f"Div: {div}, Typ: {type(div)}")  # Zeigt 2.5 und <class 'float'>
            
            with st.expander("👉 Task 2: Typ-Konversion"):
                st.markdown("Verwandle Text in Zahlen.")
                with st.echo():
                    # Problem: Text und Zahlen kann man nicht mischen
                    rating_str = "5"  # Das ist Text (String), kein Zahl!

                    # rating_str + 1 würde ERROR geben:
                    # TypeError: can only concatenate str (not "int") to str
                    # score = rating_str + 1  # Wäre ein ERROR!

                    # Lösung: Typ-Konvertierung (Type Casting)
                    rating_int = int(rating_str)  # "5" -> 5 (String zu Integer)
                    score = rating_int + 1        # Jetzt: 5 + 1 = 6 (geht!)

                    print(score)  # Gibt 6 aus
            
            with st.expander("👉 Task 3: Geometrie"):
                st.markdown("Berechne Kreis-Eigenschaften.")
                with st.echo():
                    # Kreis-Berechnungen (Geometrie-Formeln)

                    # Schritt 1: Eingabewerte
                    radius = 5  # Radius in irgendeiner Einheit (cm, m, etc.)
                    pi_approx = 3.14159  # Näherung für π (Pi)

                    # Schritt 2: Berechnungen
                    umfang = 2 * pi_approx * radius  # U = 2πr
                    # 2 * 3.14159 * 5 = 31.4159

                    flaeche = pi_approx * (radius ** 2)  # A = πr²
                    # 3.14159 * (5²) = 3.14159 * 25 = 78.53975

                    # Schritt 3: Formatierung für schöne Ausgabe
                    flaeche_fmt = "{:.2f}".format(flaeche)  # Auf 2 Dezimalstellen runden
                    # 78.53975 -> "78.54"

                    # Schritt 4: Ergebnis ausgeben
                    print(f"Ein Kreis mit r={radius} hat Fläche {flaeche_fmt}")

            with st.expander("👉 Task 4: Modulo (Restwert)"):
                st.markdown("Der Modulo-Operator `%` gibt den Rest einer Division.")
                with st.echo():
                    # Modulo-Operator (%) - gibt den Rest einer Division

                    # Schritt 1: Grundbeispiele
                    res_odd = 5 % 2   # 5 geteilt durch 2 = 2*2=4, Rest=1
                    print(f"5 % 2 = {res_odd} (Rest 1 -> Ungerade)")

                    res_even = 4 % 2  # 4 geteilt durch 2 = 2*2=4, Rest=0
                    print(f"4 % 2 = {res_even} (Rest 0 -> Gerade)")

                    # Schritt 2: Praktische Funktion bauen
                    def is_even(n):  # Funktion, die prüft ob Zahl gerade ist
                        return n % 2 == 0  # True wenn Rest 0 (gerade), False wenn Rest 1 (ungerade)

                    # Schritt 3: Funktion testen
                    print(f"Ist 42 gerade? {is_even(42)}")  # 42 % 2 = 0 -> True


        # --- EX SUBTAB 6: Complex Arithmetic (New from Raw Task 1.3/1.4) ---
        with ex_tabs[5]:
            st.markdown("### 🧮 Komplexes Rechnen")
            st.info("Hier kombinieren wir viele Operationen. Wenn dein Ergebnis stimmt, hast du die Reihenfolge (Operator Precedence) verstanden!")

            with st.expander("👉 Task 5: Kombinierte Arithmetik 1", expanded=True):
                st.markdown("Setze die Variablen und berechne `r`.")
                
                with st.echo():
                    # Vorgabe Werte
                    x, y, z = 3, 41, 7
                    r = 3.145
                    
                    # Berechnungen Schritt für Schritt
                    r = r + x           # 1. Addiere x
                    r = r + (y / z)     # 2. Addiere y geteilt durch z
                    r = r * x           # 3. Multipliziere mit x
                    r = r - (x * z)     # 4. Subtrahiere Produkt von x und z
                    
                    # Ergebnis runden für Vergleichbarkeit
                    print(f"Ergebnis r: {round(r, 2)}")
            
            with st.expander("👉 Task 6: Kombinierte Arithmetik 2"):
                st.markdown("Ein noch wilderer Ausdruck.")
                
                with st.echo():
                    # Vorgabe
                    x, y, z = 4.2, 4, 14
                    r = 2
                    
                    # "Alles in einer Zeile" vs "Schritt für Schritt"
                    # r = ((r * (x + y + z)) + y**2) / (y + 1) ...
                    
                    # Besser lesbar:
                    step1 = x + y + z
                    r = r * step1
                    r = r + (y**2)
                    r = r / (y + 1)
                    
                    # Letzter Schritt: r * (y hoch (y/2))
                    exponent = y / 2
                    factor = y ** exponent
                    r = r * factor
                    
                    print(f"Ergebnis r: {round(r, 2)}")

        # --- EX SUBTAB 7: Chatbot Logic (New from Raw 'first_steps.py') ---
        with ex_tabs[6]:
            st.markdown("### 🤖 Dein erster Chatbot")
            st.write("Programmiere eine Begrüßungs-Logik, die auf Namen reagiert.")
            
            # Input outside echo
            name_input = st.text_input("Wie heißt du?", "Jack")
            
            st.markdown("---")
            st.caption("Code-Logik:")
            
            with st.echo():
                # Die Variable 'name' kommt aus dem Eingabefeld oben
                name = name_input
                
                # Checke den Namen
                if name == "Jack":
                    # Spezielle Begrüßung für Jack
                    greeting = f"Howdy, {name}! 🤠"
                else:
                    # Standard Begrüßung für alle anderen
                    greeting = f"Hallo, {name}! 👋"
                
                # Ausgabe
                print(greeting)
                
            st.markdown("---")
            st.success(f"Output: {greeting}")

    # --- TAB 9: QUIZ ---
    with tabs[8]:
        st.subheader("📝 Abschluss-Quiz")
        
        questions = [
            {
                "q": "Was ist ein Bit?",
                "opts": ["Eine Bohrmaschine", "Eine Maßeinheit für Strom", "Die kleinste Info-Einheit (0/1)", "Ein halbes Byte"],
                "correct": 2,
                "exp": "Richtig! Binary Digit (0 oder 1)."
            },
            {
                "q": "Wie viele Werte hat ein Byte?",
                "opts": ["8", "100", "255", "256"],
                "correct": 3,
                "exp": "Korrekt. 0 bis 255 sind 256 Möglichkeiten."
            },
            {
                "q": "Welches Gatter ist TRUE, wenn BEIDE Eingänge 1 sind?",
                "opts": ["OR", "AND", "XOR", "NOT"],
                "correct": 1,
                "exp": "Genau. AND ist strikt."
            },
            {
                "q": "Was macht die CPU im 'Decode' Schritt?",
                "opts": ["Daten holen", "Befehl verstehen", "Rechnen", "Schlafen"],
                "correct": 1,
                "exp": "Richtig. Sie 'entschlüsselt' den Befehl."
            },
             {
                "q": "Was ist 1001 (binär) in Dezimal?",
                "opts": ["9", "10", "11", "1001"],
                "correct": 0,
                "exp": "Stimmt. 8 + 1 = 9."
            }
        ]
        
        score = 0
        for i, q in enumerate(questions):
            st.markdown(f"**{i+1}. {q['q']}**")
            ans = st.radio("", q['opts'], key=f"q{i}", label_visibility="collapsed")
            if ans == q['opts'][q['correct']]:
                score += 1
                with st.expander("✅ Erklärung", expanded=False):
                    st.success(q['exp'])
            st.divider()
            
        if st.button("Auswerten"):
            st.balloons()
            st.success(f"Du hast {score} von {len(questions)} Punkten!")

        # Summary Table
        st.markdown("### 🎓 Zusammenfassung")
        st.markdown("""
        | Konzept | Merksatz |
        |---|---|
        | **Informatik** | "Hardware macht es möglich, Software nützlich." |
        | **Bits** | "Atome der Information." |
        | **Zahlensysteme** | "Dezimal für Menschen, Binär für Maschinen." |
        | **Logik** | "AND ist streng, OR ist locker." |
        | **Transistoren** | "Ventile für Strom." |
        | **CPU** | "Der Herzschlag (Fetch-Decode-Execute)." |
        """)

if __name__ == "__main__":
    run()
