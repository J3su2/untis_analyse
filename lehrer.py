class Lehrer:
    def __init__(self):
        print("Neuer Lehrer erstellt")

        self.name = ""
        self.vorname = ""
        self.nachname = ""
        self.minusstunden = 0.0 # Wie viele Minusstunden hat ein Lehrer auf dem Konto?
        self.soll = 0.0 # Wie viel Unterricht muss ein Lehrer geben?
        self.abteilungen = [] # Eine Abteilung ist z.B. "GSW-Faecher" oder "NTW"
        self.lfb = [] # Welche Lehrbefaehigungen hat ein Lehrer. Zum Beispiel Bio+Chemie gy 
                      # waere dann BI (2 -  3); CH (2 - 3)
                      # die Zahlen stehen für HZ, RZ und GZ
                      # Alle Lehrer haben eine Befaehigung, wenige haben bis zu 3 
                      # Die meisten Lehrer haben zwei

    def debug(self):
        """ Diese Methode soll die Daten eines Lehrer uebersichtlich
        darstellen, so dass man testen kann, ob das Einlesen und speichern
        der Daten geklappt hat
        """
        print(self.nachname)