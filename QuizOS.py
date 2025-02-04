questions = [
    {
        "question": "Was bewirkt der `fork()`-Befehl in einem Unix-System?",
        "options": [
            "Erstellt eine neue Datei",
            "Erstellt einen neuen Prozess als Kopie des Elternprozesses",
            "Beendet den aktuellen Prozess",
            "Reserviert Speicherplatz"
        ],
        "answer": 1
    },
    {
        "question": "Was unterscheidet den Elternprozess vom Kindprozess nach einem `fork()`?",
        "options": [
            "Der Speicherzugriff",
            "Die Priorität",
            "Der Rückgabewert von `fork()`",
            "Die Prozess-ID bleibt gleich"
        ],
        "answer": 2
    },
    {
        "question": "Was passiert, wenn ein `fork()`-Aufruf fehlschlägt?",
        "options": [
            "Der Prozess wird abgebrochen",
            "Der Aufruf gibt -1 zurück",
            "Das Betriebssystem startet neu",
            "Der Prozess läuft ohne Änderungen weiter"
        ],
        "answer": 1
    },
    {
        "question": "Welche Ressourcen werden nach einem `fork()` zwischen Eltern- und Kindprozess geteilt?",
        "options": [
            "CPU-Zeit",
            "Dateien",
            "Keine Ressourcen, da sie dupliziert werden",
            "Netzwerkverbindungen"
        ],
        "answer": 2
    },
    {
        "question": "Was passiert, wenn ein Kindprozess vor dem Elternprozess beendet wird?",
        "options": [
            "Der Kindprozess wird automatisch gelöscht",
            "Der Elternprozess wird beendet",
            "Der Kindprozess wird zum Zombie-Prozess",
            "Der Speicher wird sofort freigegeben"
        ],
        "answer": 2
    },
    {
        "question": "Wofür wird der Buddy-Algorithmus in der Speicherverwaltung verwendet?",
        "options": [
            "Zur CPU-Verwaltung",
            "Zur dynamischen Speicherzuweisung",
            "Zur Prozesspriorisierung",
            "Zur Dateiverwaltung"
        ],
        "answer": 1
    },
    {
        "question": "Wie funktioniert die Aufteilung des Speichers beim Buddy-Algorithmus?",
        "options": [
            "Speicher wird linear verteilt",
            "Speicher wird in Potenzen von 2 aufgeteilt",
            "Speicher wird zufällig zugewiesen",
            "Speicher wird in Blöcke von gleicher Größe aufgeteilt"
        ],
        "answer": 1
    },
    {
        "question": "Was passiert, wenn zwei benachbarte freie Blöcke der gleichen Größe vorhanden sind?",
        "options": [
            "Einer der Blöcke wird gelöscht",
            "Die Blöcke werden zusammengeführt",
            "Die Blöcke werden gesperrt",
            "Es passiert nichts"
        ],
        "answer": 1
    },
    {
        "question": "Welche Art von Fragmentierung wird durch den Buddy-Algorithmus reduziert?",
        "options": [
            "Keine Fragmentierung",
            "Interne Fragmentierung",
            "Externe Fragmentierung",
            "Virtuelle Fragmentierung"
        ],
        "answer": 2
    },
    {
        "question": "Warum werden Speicherblöcke in Potenzen von 2 geteilt?",
        "options": [
            "Um den Speicherplatz zu maximieren",
            "Um die Adressberechnung zu vereinfachen",
            "Um weniger Speicher zu nutzen",
            "Um Prozesse schneller zu beenden"
        ],
        "answer": 1
    },
    {
        "question": "Was ist Docker?",
        "options": [
            "Eine Programmiersprache",
            "Eine Plattform zur Container-Virtualisierung",
            "Eine Hardware-Sicherheitslösung",
            "Ein Betriebssystem"
        ],
        "answer": 1
    },
    {
        "question": "Was ist ein Docker-Image?",
        "options": [
            "Eine ausführbare Datei",
            "Ein physischer Speicherort",
            "Eine Vorlage zur Erstellung von Containern",
            "Eine Konfigurationsdatei"
        ],
        "answer": 2
    },
    {
        "question": "Mit welchem Befehl kann man ein Docker-Image löschen?",
        "options": [
            "docker delete",
            "docker kill",
            "docker rmi",
            "docker stop"
        ],
        "answer": 2
    },
    {
        "question": "Welche Datei wird typischerweise für `docker-compose` verwendet?",
        "options": [
            "compose.yml",
            "docker-compose.yml",
            "dockerfile.yml",
            "config.yml"
        ],
        "answer": 1
    },
    {
        "question": "Was ist der Unterschied zwischen einem Container und einer virtuellen Maschine?",
        "options": [
            "Container benötigen mehr Speicher als virtuelle Maschinen",
            "Container teilen keine Ressourcen mit dem Host",
            "Container benötigen ein vollständiges Betriebssystem",
            "Container teilen den Host-Kernel"
        ],
        "answer": 3
    },
    {
        "question": "Welche Strategie reduziert die durchschnittliche Wartezeit von Prozessen am besten?",
        "options": [
            "FCFS (First Come, First Served)",
            "SJF (Shortest Job First)",
            "Round Robin",
            "Priority Scheduling"
        ],
        "answer": 1
    },
    {
        "question": "Welche Scheduling-Strategie nutzt feste Zeitquanten?",
        "options": [
            "FCFS",
            "SJF",
            "Round Robin (RR)",
            "Priority Scheduling"
        ],
        "answer": 2
    },
    {
        "question": "Was versteht man unter Aging bei Priority Scheduling?",
        "options": [
            "Die Priorität eines wartenden Prozesses steigt mit der Zeit",
            "Der Prozess wird aus der Warteschlange entfernt",
            "Der Prozess wird abgebrochen",
            "Es gibt keine Aging-Mechanismen"
        ],
        "answer": 0
    },
    {
        "question": "Was passiert, wenn das Zeitquantum bei Round Robin zu groß ist?",
        "options": [
            "Die Performance steigt",
            "Das System degeneriert zu FCFS",
            "Prozesse werden schneller abgeschlossen",
            "Es wird ein Deadlock erzeugt"
        ],
        "answer": 1
    },
    {
        "question": "Welche Art von Scheduling wird bei Echtzeit-Systemen verwendet?",
        "options": [
            "Round Robin",
            "FCFS",
            "Priority Scheduling",
            "Multilevel Queue"
        ],
        "answer": 2
    },
    {
        "question": "Welche Funktion hat ein Kernel?",
        "options": [
            "Er speichert Dateien",
            "Er verwaltet Benutzerzugriffe",
            "Er steuert die Hardware und koordiniert Prozesse",
            "Er optimiert Netzwerke"
        ],
        "answer": 2
    },
    {
        "question": "Was ist der Unterschied zwischen einem Hard und einem Soft Realtime-System?",
        "options": [
            "Hard Realtime-Systeme sind schneller",
            "Soft Realtime-Systeme haben garantierte Antwortzeiten",
            "Hard Realtime-Systeme haben strikte Zeitvorgaben",
            "Es gibt keinen Unterschied"
        ],
        "answer": 2
    },
    {
        "question": "Wie kann Deadlock vermieden werden?",
        "options": [
            "Zyklenerkennung und -vermeidung",
            "Höhere Prioritäten für Prozesse",
            "Manuelle Prozesskontrolle",
            "Parallelisierung"
        ],
        "answer": 0
    },
    {
        "question": "Was passiert bei einer CPU-Auslastung von 100%?",
        "options": [
            "Prozesse werden gestoppt",
            "Das System friert ein",
            "Alle CPU-Ressourcen sind ausgelastet",
            "Der Kernel priorisiert neue Prozesse"
        ],
        "answer": 2
    },
    {
        "question": "Was versteht man unter einer \"Falltür\" (`trap door`) im System?",
        "options": [
            "Ein Softwareinterrupt",
            "Ein Hardwarefehler",
            "Ein Sicherheitsrisiko",
            "Ein Debugging-Tool"
        ],
        "answer": 0
    },
    {
        "question": "Was ist eine Race Condition?",
        "options": [
            "Ein Fehler, der durch unsynchronisierte Zugriffe auf gemeinsam genutzte Ressourcen entsteht",
            "Ein Zustand, in dem der Prozess zu lange läuft",
            "Ein Speicherfehler in Threads",
            "Ein CPU-Engpass"
        ],
        "answer": 0
    },
    {
        "question": "Wie wird ein Zombie-Prozess entfernt?",
        "options": [
            "Der Elternprozess ruft wait() auf",
            "Durch den Befehl kill",
            "Automatisch vom Kernel nach 10 Sekunden",
            "Durch manuelles Entfernen aus der Prozessliste"
        ],
        "answer": 0
    },
    {
        "question": "Wie werden kritische Abschnitte in Threads synchronisiert?",
        "options": [
            "Durch Prozesse",
            "Durch Semaphore oder Locks",
            "Durch Mutexe",
            "Durch Deadlocks"
        ],
        "answer": 2
    },
    {
        "question": "Was ist ein Zombie-Prozess?",
        "options": [
            "Ein Prozess, der unendlich läuft",
            "Ein Prozess, der keine CPU-Ressourcen nutzt",
            "Ein beendeter Prozess, dessen Status noch nicht abgefragt wurde",
            "Ein Prozess, der auf den Speicher anderer Prozesse zugreift"
        ],
        "answer": 2
    },
    {
        "question": "Was passiert bei einer Kontextumschaltung?",
        "options": [
            "Der Prozess wird beendet",
            "Der Scheduler wird deaktiviert",
            "Der Zustand des aktuellen Prozesses wird gespeichert und ein neuer Prozess wird gestartet",
            "Die CPU wechselt den Kernmodus"
        ],
        "answer": 2
    },
    {
        "question": "Was bedeutet \"Virtueller Speicher\"?",
        "options": [
            "Speicher, der ausschließlich für große Anwendungen reserviert ist",
            "Ein Mechanismus, der mehr Speicher bereitstellt, als physisch verfügbar ist",
            "Ein Bereich auf der Festplatte, der permanent genutzt wird",
            "Speicher, der direkt von der CPU genutzt wird"
        ],
        "answer": 1
    }
]

def ask_question(question_data):
    print(question_data["question"])
    for i, option in enumerate(question_data["options"], 1):
        print(f"{i}. {option}")
    # Eingabe validieren
    while True:
        try:
            user_input = input("Ihre Antwort (1-4) oder \"STOP\": ")
            if user_input.upper() == "STOP":
                return "STOP"
            user_input = int(user_input)
            if 1 <= user_input <= 4:
                return user_input - 1  # Index anpassen
        except ValueError:
            print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")

# Quiz ausführen
def quiz():
    print("-"*53)
    print("Willkomen zum OS Quiz!")
    print("-"*53)
    score = 0
    for question in questions:
        user_answer = ask_question(question)
        if user_answer == "STOP":
            break
        if user_answer == question["answer"]:
            print("Richtig!")
            score += 1
        else:
            print(f"Falsch! Richtige Antwort: {question['options'][question['answer']]}")
        print("-" * 20)
    print(f"Sie haben {score} von {len(questions)} richtig beantwortet!")

if __name__ == "__main__":
    quiz()