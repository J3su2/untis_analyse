import lehrer

class Fach:
    """ Ein Objekt der Klasse Fach """

    def __init__(self):
        print("neues Fach")

        self.lehrerlist = []

    def fuegeLehrerHinzu( self, leh ):
        """ fuegt dem Fach einen Lehrer hinzu """
        print("Fuege den Lehrer hinzu")

        self.lehrerlist.append( leh )

    def lehrerAuflisten(self):
        """diese Methode soll alle Lehrer auflisten, die dieses
        Fach unterrichten
        """
        for lehrer in self.lehrerlist:
            print(lehrer.debug)

    