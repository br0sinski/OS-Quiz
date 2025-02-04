# 2. Funktion zum Stellen der Fragen
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
        "question": "Welche Funktionalität bietet der Befehl `exec()`?",
        "options": [
            "Startet den aktuellen Prozess neu",
            "Lädt ein neues Programm in den aktuellen Prozess",
            "Beendet den Prozess und erzeugt einen neuen",
            "Wartet auf andere Prozesse"
        ],
        "answer": 1
    },
    {
        "question": "Wie skaliert Docker Container?",
        "options": [
            "Automatisch basierend auf der CPU-Auslastung",
            "Über eine Netzwerkressourcenverwaltung",
            "Mit dem Befehl `docker-compose up --scale`",
            "Durch Erhöhung des Arbeitsspeichers"
        ],
        "answer": 2
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
            "Der Elternprozess ruft `wait()` auf",
            "Durch den Befehl `kill`",
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
        "question": "Welche Art von Ressourcen dupliziert fork() nicht direkt?",
        "options": [
            "Offene Dateien",
            "Heap-Speicher",
            "Signal-Handler",
            "Globale Variablen"
        ],
        "answer": 1
    },
    {
        "question": "Welche Funktionalität bietet der Befehl exec()?",
        "options": [
            "Startet den aktuellen Prozess neu",
            "Lädt ein neues Programm in den aktuellen Prozess",
            "Beendet den Prozess und erzeugt einen neuen",
            "Wartet auf andere Prozesse"
        ],
        "answer": 1
    },
    {
        "question": "Welche Problemart löst der Buddy-Algorithmus nicht?",
        "options": [
            "Speicherauslastung",
            "Speicherzuweisung",
            "Deadlocks",
            "Interne Fragmentierung"
        ],
        "answer": 2
    },
    {
        "question": "Was passiert, wenn eine Speicheranforderung die verfügbare Größe überschreitet?",
        "options": [
            "Der Algorithmus verweigert die Zuweisung",
            "Der Speicher wird automatisch erweitert",
            "Es wird ein Fehlercode zurückgegeben",
            "Der nächstgrößere Block wird zugewiesen"
        ],
        "answer": 3
    },
    {
        "question": "Welche Speichergröße wird bevorzugt vom Buddy-Algorithmus zugewiesen?",
        "options": [
            "Potenzen von 2",
            "Beliebige Größen",
            "Feste Größen von 1 MB",
            "Vom Betriebssystem festgelegte Größen"
        ],
        "answer": 0
    },
    {
        "question": "Was ist der Hauptnachteil von Shortest Job First (SJF)?",
        "options": [
            "Hoher Speicherbedarf",
            "Prozesse mit langer Ausführungszeit können verhungern",
            "Komplexität bei der Implementierung",
            "Schlechte CPU-Auslastung"
        ],
        "answer": 1
    },
    {
        "question": "Warum ist Round Robin eine faire Scheduling-Strategie?",
        "options": [
            "Prozesse mit hoher Priorität werden bevorzugt",
            "Kurze Prozesse werden zuerst beendet",
            "Jeder Prozess erhält gleiche Zeitanteile",
            "Längere Prozesse werden ignoriert"
        ],
        "answer": 2
    },
    {
        "question": "Welche Prozesse profitieren am meisten von Round Robin?",
        "options": [
            "CPU-intensive Prozesse",
            "Kurze interaktive Prozesse",
            "Prozesse mit langer Wartezeit",
            "Prozesse mit hoher Priorität"
        ],
        "answer": 1
    },
    {
        "question": "Welche Strategie kommt bei Echtzeit-Systemen häufig zum Einsatz?",
        "options": [
            "Round Robin",
            "FCFS",
            "Priority Scheduling",
            "Multilevel Queue Scheduling"
        ],
        "answer": 2
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
        "question": "Welche Art von Ressourcen dupliziert fork() nicht direkt?",
        "options": [
            "Offene Dateien",
            "Heap-Speicher",
            "Signal-Handler",
            "Globale Variablen"
        ],
        "answer": 1
    },
    {
        "question": "Welche Funktionalität bietet der Befehl exec()?",
        "options": [
            "Startet den aktuellen Prozess neu",
            "Lädt ein neues Programm in den aktuellen Prozess",
            "Beendet den Prozess und erzeugt einen neuen",
            "Wartet auf andere Prozesse"
        ],
        "answer": 1
    },
    {
        "question": "Welche Problemart löst der Buddy-Algorithmus nicht?",
        "options": [
            "Speicherauslastung",
            "Speicherzuweisung",
            "Deadlocks",
            "Interne Fragmentierung"
        ],
        "answer": 2
    },
    {
        "question": "Was passiert, wenn eine Speicheranforderung die verfügbare Größe überschreitet?",
        "options": [
            "Der Algorithmus verweigert die Zuweisung",
            "Der Speicher wird automatisch erweitert",
            "Es wird ein Fehlercode zurückgegeben",
            "Der nächstgrößere Block wird zugewiesen"
        ],
        "answer": 3
    },
    {
        "question": "Welche Speichergröße wird bevorzugt vom Buddy-Algorithmus zugewiesen?",
        "options": [
            "Potenzen von 2",
            "Beliebige Größen",
            "Feste Größen von 1 MB",
            "Vom Betriebssystem festgelegte Größen"
        ],
        "answer": 0
    },
    {
        "question": "Was ist der Hauptvorteil von Containern gegenüber virtuellen Maschinen?",
        "options": [
            "Schneller Start und geringerer Overhead",
            "Geringerer Speicherverbrauch",
            "Direkte Hardware-Zugriffe",
            "Kein Betriebssystem erforderlich"
        ],
        "answer": 0
    },
    {
        "question": "Was ist ein Dockerfile?",
        "options": [
            "Ein ausführbarer Container",
            "Eine Konfigurationsdatei zur Erstellung eines Images",
            "Eine Netzwerkkonfiguration für Docker",
            "Eine Datei, die Volumes definiert"
        ],
        "answer": 1
    },
    {
        "question": "Welche Rolle spielt der Befehl docker push?",
        "options": [
            "Lädt ein Image vom Docker Hub herunter",
            "Lädt ein Image in das Docker Hub hoch",
            "Startet einen neuen Container",
            "Aktualisiert ein laufendes Image"
        ],
        "answer": 1
    },
    {
        "question": "Wie skaliert Docker Container?",
        "options": [
            "Automatisch basierend auf der CPU-Auslastung",
            "Über eine Netzwerkressourcenverwaltung",
            "Mit dem Befehl docker-compose up --scale",
            "Durch Erhöhung des Arbeitsspeichers"
        ],
        "answer": 2
    },
    {
        "question": "Was ist der Vorteil der Nutzung von Volumes in Docker?",
        "options": [
            "Container laufen schneller",
            "Daten bleiben auch nach Neustart des Containers erhalten",
            "Container nutzen weniger Speicherplatz",
            "Netzwerke werden optimiert"
        ],
        "answer": 1
    },
    {
        "question": "Was ist der Hauptnachteil von Shortest Job First (SJF)?",
        "options": [
            "Hoher Speicherbedarf",
            "Prozesse mit langer Ausführungszeit können verhungern",
            "Komplexität bei der Implementierung",
            "Schlechte CPU-Auslastung"
        ],
        "answer": 1
    },
    {
        "question": "Warum ist Round Robin eine faire Scheduling-Strategie?",
        "options": [
            "Prozesse mit hoher Priorität werden bevorzugt",
            "Kurze Prozesse werden zuerst beendet",
            "Jeder Prozess erhält gleiche Zeitanteile",
            "Längere Prozesse werden ignoriert"
        ],
        "answer": 2
    },
    {
        "question": "Welche Prozesse profitieren am meisten von Round Robin?",
        "options": [
            "CPU-intensive Prozesse",
            "Kurze interaktive Prozesse",
            "Prozesse mit langer Wartezeit",
            "Prozesse mit hoher Priorität"
        ],
        "answer": 1
    },
    {
        "question": "Welche Strategie kommt bei Echtzeit-Systemen häufig zum Einsatz?",
        "options": [
            "Round Robin",
            "FCFS",
            "Priority Scheduling",
            "Multilevel Queue Scheduling"
        ],
        "answer": 2
    },
    {
        "question": "Was ist der Nachteil von Multilevel Queue Scheduling?",
        "options": [
            "Keine Differenzierung zwischen Prozessen",
            "Hoher Speicherbedarf",
            "Komplexe Verwaltung und viele Parameter",
            "Schlechte CPU-Nutzung"
        ],
        "answer": 2
    },
    {
        "question": "Was ist eine typische Aufgabe eines Betriebssystems?",
        "options": [
            "Erstellung von Benutzerprogrammen",
            "Verwaltung von Ressourcen und Prozessen",
            "Optimierung von Hardware-Leistung",
            "Verbesserung der Netzwerkgeschwindigkeit"
        ],
        "answer": 1
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
        "question": "Welche Aufgabe übernimmt ein Scheduler?",
        "options": [
            "Daten zwischen Festplatten zu verteilen",
            "Prozesse zu priorisieren und CPU-Zeit zuzuweisen",
            "Den Arbeitsspeicher zu verwalten",
            "Netzwerkverbindungen zu überwachen"
        ],
        "answer": 1
    },
    {
        "question": "Was ist der Hauptzweck eines Kernels?",
        "options": [
            "Dateien zu verwalten",
            "Benutzeroberflächen bereitzustellen",
            "Die Kommunikation zwischen Hardware und Software zu steuern",
            "Systemabstürze zu verhindern"
        ],
        "answer": 2
    },
    {
        "question": "Was ist der Unterschied zwischen einem Prozess und einem Thread?",
        "options": [
            "Prozesse benötigen mehr Speicherplatz",
            "Threads sind unabhängig von Prozessen",
            "Threads teilen sich Ressourcen innerhalb eines Prozesses",
            "Prozesse können parallel laufen, Threads nicht"
        ],
        "answer": 2
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
        "question": "Was bedeutet 'Virtueller Speicher'?",
        "options": [
            "Speicher, der ausschließlich für große Anwendungen reserviert ist",
            "Ein Mechanismus, der mehr Speicher bereitstellt, als physisch verfügbar ist",
            "Ein Bereich auf der Festplatte, der permanent genutzt wird",
            "Speicher, der direkt von der CPU genutzt wird"
        ],
        "answer": 1
    },
    {
        "question": "Was ist eine typische Aufgabe eines Semaphors?",
        "options": [
            "Prozesse zu priorisieren",
            "Zugriffe auf eine Ressource zu synchronisieren",
            "Prozessbeendigungen zu steuern",
            "Speicheradressen zu reservieren"
        ],
        "answer": 1
    },
    {
        "question": "Was ist eine Deadlock-Bedingung?",
        "options": [
            "Prozesse teilen Speicher",
            "Prozesse arbeiten synchronisiert",
            "Prozesse warten gegenseitig auf Ressourcen, die blockiert sind",
            "Prozesse werden vorzeitig beendet"
        ],
        "answer": 2
    },
    {
        "question": "Wie kann Deadlock vermieden werden?",
        "options": [
            "Zyklenerkennung und Vermeidung von wechselseitigem Warten",
            "Automatische Priorisierung aller Prozesse",
            "Begrenzung der CPU-Auslastung",
            "Reduzierung der Prozessanzahl"
        ],
        "answer": 0
    },
    {
        "question": "Was macht der Systemaufruf kill in Unix?",
        "options": [
            "Entfernt einen Prozess aus der Liste",
            "Priorisiert den aktuellen Prozess",
            "Beendet einen Prozess durch das Senden eines Signals",
            "Wartet auf einen Prozess"
        ],
        "answer": 2
    },
    {
        "question": "Wie können Prozesse mit gemeinsamer Ressourcennutzung synchronisiert werden?",
        "options": [
            "Durch Threads",
            "Durch Systemaufrufe",
            "Durch Semaphore und Mutexe",
            "Durch den Scheduler"
        ],
        "answer": 2
    },
    {
        "question": "Welche Eigenschaft beschreibt den Unterschied zwischen einem 'Monolithischen Kernel' und einem 'Mikrokernel'?",
        "options": [
            "Die Anzahl der Benutzer",
            "Modularität und Kontextwechsel",
            "Die Komplexität des Hauptspeichers",
            "Die grafische Oberfläche"
        ],
        "answer": 1  # Modularität und Kontextwechsel
    },
    {
        "question": "Welche Funktion übernimmt ein 'Dispatcher' im Scheduling?",
        "options": [
            "Er legt die Reihenfolge der Prozesse fest.",
            "Er wechselt zwischen Prozessen.",
            "Er optimiert den Speicherverbrauch.",
            "Er erhöht die Priorität wartender Prozesse."
        ],
        "answer": 1  # Er wechselt zwischen Prozessen
    },
    {
        "question": "Welche Aussage trifft auf Shortest Job First (SJF) Scheduling zu?",
        "options": [
            "Es basiert auf einer Zufallsauswahl.",
            "Es bevorzugt Prozesse mit kürzeren CPU-Bursts.",
            "Es ist nicht preemptiv.",
            "Es führt immer zu maximaler Wartezeit."
        ],
        "answer": 1  # Es bevorzugt Prozesse mit kürzeren CPU-Bursts
    },
    {
        "question": "Welche Systemaufrufe gehören typischerweise zu Unix?",
        "options": [
            "Speicherverwaltung, Benutzerverwaltung, Rechtemanagement",
            "fork(), exec(), wait()",
            "Shutdown, Restart, Session Management",
            "Alle Antworten sind korrekt."
        ],
        "answer": 1  # fork(), exec(), wait()
    },
    {
        "question": "Was bedeutet 'Time Sharing' bei Linux-Scheduling?",
        "options": [
            "Gleichmäßige Ressourcennutzung unabhängig von der Priorität.",
            "Die höchste Priorität wird immer bevorzugt.",
            "Prozesse mit mehr Credits werden zuerst verarbeitet.",
            "Die CPU teilt Prozesse nach Zeitplänen auf."
        ],
        "answer": 2  # Prozesse mit mehr Credits werden zuerst verarbeitet
    },

    {
        "question": "Welche Funktion kann ein Elternprozess verwenden, um auf den Abschluss eines Kindprozesses zu warten?",
        "options": [
            "exec()",
            "sleep()",
            "wait()",
            "kill()"
        ],
        "answer": 2  # wait()
    },
    {
        "question": "Was geschieht mit Kindprozessen, wenn der Elternprozess beendet wird?",
        "options": [
            "Sie werden zu Waisenprozessen und vom init-Prozess übernommen",
            "Sie werden ebenfalls beendet",
            "Sie laufen weiter ohne Einschränkungen",
            "Sie verlieren alle Ressourcen"
        ],
        "answer": 0  # Waisenprozesse
    },
    {
        "question": "Was unterscheidet vfork() von fork()?",
        "options": [
            "vfork() ist langsamer als fork()",
            "vfork() dupliziert alle Ressourcen",
            "vfork() teilt den Speicher zwischen Eltern und Kind, bis exec() aufgerufen wird",
            "Es gibt keinen Unterschied"
        ],
        "answer": 2  # Speicherteilung
    },
    {
        "question": "Welche Systemaufrufe folgen typischerweise nach einem fork()?",
        "options": [
            "wait() und exit()",
            "exec() oder exit()",
            "kill() und stop()",
            "getpid() und sleep()"
        ],
        "answer": 1  # exec() oder exit()
    },
    {
        "question": "Wie nennt man die Hierarchie, die durch fork()-Aufrufe entsteht?",
        "options": [
            "Prozessbaum",
            "Prozesshierarchie",
            "Prozessstruktur",
            "Prozessnetzwerk"
        ],
        "answer": 0  # Prozessbaum
    },
    {
        "question": "Was passiert, wenn der angeforderte Speicher kleiner ist als der kleinste verfügbare Block?",
        "options": [
            "Der Speicher wird gesperrt",
            "Der nächstgrößere Block wird zugewiesen",
            "Die Anfrage wird abgelehnt",
            "Es wird ein Fehler ausgegeben"
        ],
        "answer": 1  # Nächstgrößerer Block
    },
    {
        "question": "Was ist der Hauptvorteil des Buddy-Algorithmus?",
        "options": [
            "Maximale Ressourcennutzung",
            "Effiziente Speicherverwaltung mit einfacher Zusammenführung freier Blöcke",
            "Geringe interne Fragmentierung",
            "Flexible Speicherzuteilung"
        ],
        "answer": 1  # Effiziente Speicherverwaltung
    },
    {
        "question": "Was ist ein typisches Problem des Buddy-Algorithmus?",
        "options": [
            "Interne Fragmentierung bei kleinen Speicheranforderungen",
            "Hohe externe Fragmentierung",
            "Unzureichende Speicherfreigabe",
            "Zu lange Zuteilungszeiten"
        ],
        "answer": 0  # Interne Fragmentierung
    },
    {
        "question": "Welche Informationen werden benötigt, um den Buddy-Algorithmus zu implementieren?",
        "options": [
            "Speicherort und Dateisystem",
            "Liste verfügbarer Speicherblöcke und ihre Größen",
            "Prozessprioritäten",
            "Speicher-Busbreite"
        ],
        "answer": 1  # Speicherblöcke und Größen
    },
    {
        "question": "Was passiert, wenn kein Block verfügbar ist, der groß genug für eine Anforderung ist?",
        "options": [
            "Der Prozess muss warten oder Speicher wird als erschöpft betrachtet",
            "Ein Fehler wird ausgegeben",
            "Ein zufälliger Block wird zugewiesen",
            "Der Speicher wird erweitert"
        ],
        "answer": 0  # Speicher erschöpft
    },
    {
        "question": "Was ist der Zweck von Docker Volumes?",
        "options": [
            "Die Performance zu verbessern",
            "Persistente Daten zwischen Container-Neustarts zu speichern",
            "Container schneller zu starten",
            "Netzwerke zu verwalten"
        ],
        "answer": 1  # Persistente Daten
    },
    {
        "question": "Mit welchem Befehl kann man ein Docker-Image erstellen?",
        "options": [
            "docker-compose",
            "docker pull",
            "docker build",
            "docker save"
        ],
        "answer": 2  # docker build
    },
    {
        "question": "Wie startet man einen Container aus einem Image?",
        "options": [
            "docker create",
            "docker init",
            "docker run",
            "docker start"
        ],
        "answer": 2  # docker run
    },
    {
        "question": "Was ist Docker Compose?",
        "options": [
            "Ein Werkzeug zur Optimierung von Images",
            "Eine Alternative zu Kubernetes",
            "Ein Tool zur Verwaltung mehrerer Container",
            "Ein Befehl zum Erstellen von Netzwerken"
        ],
        "answer": 2  # Verwaltung mehrerer Container
    },
    {
        "question": "Welche Netzwerkmodi unterstützt Docker?",
        "options": [
            "Host und NAT",
            "Bridge, Host, None, Overlay",
            "VLAN und TCP",
            "Hybrid-Netzwerk"
        ],
        "answer": 1  # Bridge, Host, None, Overlay
    },
    {
        "question": "Was ist der Nachteil von FCFS (First Come, First Served)?",
        "options": [
            "Es ist schwer zu implementieren",
            "Prozesse werden zufällig sortiert",
            "Der Konvoi-Effekt",
            "Es unterstützt keine Prioritäten"
        ],
        "answer": 2  # Konvoi-Effekt
    },
    {
        "question": "Welche Scheduling-Strategie nutzt Aging?",
        "options": [
            "Priority Scheduling",
            "FCFS",
            "Round Robin",
            "Multilevel Feedback Queue"
        ],
        "answer": 0  # Priority Scheduling
    },
    {
        "question": "Was versteht man unter Dispatcher Latency?",
        "options": [
            "Die Zeit, die ein Prozess auf I/O wartet",
            "Die Zeit, die benötigt wird, um zwischen Prozessen zu wechseln",
            "Die Zeit zur Ausführung eines Prozesses",
            "Die Zeit, die ein Prozess blockiert ist"
        ],
        "answer": 1  # Zeit für Kontextwechsel
    },
    {
        "question": "Welche Scheduling-Kriterien gibt es?",
        "options": [
            "Durchsatz und Netzwerkgeschwindigkeit",
            "CPU-Auslastung und Speichergröße",
            "CPU-Nutzung, Durchsatz, Wartezeit, Antwortzeit",
            "Prozessanzahl und Prioritäten"
        ],
        "answer": 2  # CPU-Nutzung, Durchsatz, Wartezeit, Antwortzeit
    },
    {
        "question": "Was ist das Ziel von Multilevel Feedback Queue Scheduling?",
        "options": [
            "Prozesse nach Größe zu sortieren",
            "Prozesse mit gleichen Ressourcen zusammenzufassen",
            "Dynamische Anpassung der Prozessprioritäten",
            "Lange Prozesse zu bevorzugen"
        ],
        "answer": 2  # Dynamische Anpassung der Prioritäten
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
        "question": "Welche Art von Ressourcen dupliziert fork() nicht direkt?",
        "options": [
            "Offene Dateien",
            "Heap-Speicher",
            "Signal-Handler",
            "Globale Variablen"
        ],
        "answer": 1
    },
    {
        "question": "Welche Funktionalität bietet der Befehl exec()?",
        "options": [
            "Startet den aktuellen Prozess neu",
            "Lädt ein neues Programm in den aktuellen Prozess",
            "Beendet den Prozess und erzeugt einen neuen",
            "Wartet auf andere Prozesse"
        ],
        "answer": 1
    },
    {
        "question": "Welche Problemart löst der Buddy-Algorithmus nicht?",
        "options": [
            "Speicherauslastung",
            "Speicherzuweisung",
            "Deadlocks",
            "Interne Fragmentierung"
        ],
        "answer": 2
    },
    {
        "question": "Was passiert, wenn eine Speicheranforderung die verfügbare Größe überschreitet?",
        "options": [
            "Der Algorithmus verweigert die Zuweisung",
            "Der Speicher wird automatisch erweitert",
            "Es wird ein Fehlercode zurückgegeben",
            "Der nächstgrößere Block wird zugewiesen"
        ],
        "answer": 3
    },
    {
        "question": "Welche Speichergröße wird bevorzugt vom Buddy-Algorithmus zugewiesen?",
        "options": [
            "Potenzen von 2",
            "Beliebige Größen",
            "Feste Größen von 1 MB",
            "Vom Betriebssystem festgelegte Größen"
        ],
        "answer": 0
    },
    {
        "question": "Was ist der Hauptvorteil von Containern gegenüber virtuellen Maschinen?",
        "options": [
            "Schneller Start und geringerer Overhead",
            "Geringerer Speicherverbrauch",
            "Direkte Hardware-Zugriffe",
            "Kein Betriebssystem erforderlich"
        ],
        "answer": 0
    },
    {
        "question": "Was ist ein Dockerfile?",
        "options": [
            "Ein ausführbarer Container",
            "Eine Konfigurationsdatei zur Erstellung eines Images",
            "Eine Netzwerkkonfiguration für Docker",
            "Eine Datei, die Volumes definiert"
        ],
        "answer": 1
    },
    {
        "question": "Welche Rolle spielt der Befehl docker push?",
        "options": [
            "Lädt ein Image vom Docker Hub herunter",
            "Lädt ein Image in das Docker Hub hoch",
            "Startet einen neuen Container",
            "Aktualisiert ein laufendes Image"
        ],
        "answer": 1
    },
    {
        "question": "Wie skaliert Docker Container?",
        "options": [
            "Automatisch basierend auf der CPU-Auslastung",
            "Über eine Netzwerkressourcenverwaltung",
            "Mit dem Befehl docker-compose up --scale",
            "Durch Erhöhung des Arbeitsspeichers"
        ],
        "answer": 2
    },
    {
        "question": "Was ist der Vorteil der Nutzung von Volumes in Docker?",
        "options": [
            "Container laufen schneller",
            "Daten bleiben auch nach Neustart des Containers erhalten",
            "Container nutzen weniger Speicherplatz",
            "Netzwerke werden optimiert"
        ],
        "answer": 1
    },
    {
        "question": "Was ist der Hauptnachteil von Shortest Job First (SJF)?",
        "options": [
            "Hoher Speicherbedarf",
            "Prozesse mit langer Ausführungszeit können verhungern",
            "Komplexität bei der Implementierung",
            "Schlechte CPU-Auslastung"
        ],
        "answer": 1
    },
    {
        "question": "Warum ist Round Robin eine faire Scheduling-Strategie?",
        "options": [
            "Prozesse mit hoher Priorität werden bevorzugt",
            "Kurze Prozesse werden zuerst beendet",
            "Jeder Prozess erhält gleiche Zeitanteile",
            "Längere Prozesse werden ignoriert"
        ],
        "answer": 2
    },
    {
        "question": "Welche Prozesse profitieren am meisten von Round Robin?",
        "options": [
            "CPU-intensive Prozesse",
            "Kurze interaktive Prozesse",
            "Prozesse mit langer Wartezeit",
            "Prozesse mit hoher Priorität"
        ],
        "answer": 1
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
        "question": "Was ist der Hauptzweck eines Kernels?",
        "options": [
            "Dateien zu verwalten",
            "Benutzeroberflächen bereitzustellen",
            "Die Kommunikation zwischen Hardware und Software zu steuern",
            "Systemabstürze zu verhindern"
        ],
        "answer": 2
    },
    {
        "question": "Was ist der Unterschied zwischen einem Prozess und einem Thread?",
        "options": [
            "Prozesse benötigen mehr Speicherplatz",
            "Threads sind unabhängig von Prozessen",
            "Threads teilen sich Ressourcen innerhalb eines Prozesses",
            "Prozesse können parallel laufen, Threads nicht"
        ],
        "answer": 2
    },
    {
        "question": "Was bedeutet 'Virtueller Speicher'?",
        "options": [
            "Speicher, der ausschließlich für große Anwendungen reserviert ist",
            "Ein Mechanismus, der mehr Speicher bereitstellt, als physisch verfügbar ist",
            "Ein Bereich auf der Festplatte, der permanent genutzt wird",
            "Speicher, der direkt von der CPU genutzt wird"
        ],
        "answer": 1
    }
]


def ask_question(question_data, duplicate_qustions: bool):
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

    inp = str(input("Willst du dass die Fragen sich widerholen? (y/n)"))
    repeated_questions = False
    if inp == 'y' or inp == 'Y':
        repeated_questions = True

    score = 0
    asked_questions = set()
    for question in questions:
        if not repeated_questions and question["question"] in asked_questions:
            continue
        asked_questions.add(question["question"])
        user_answer = ask_question(question, repeated_questions)
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