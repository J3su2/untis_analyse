#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

from lehrer import *




def dateiEinlesen():
    """Diese Methode liest die CSV-Datei ein und gibt am Ende eine
    Liste aller Lehrer zurueck. Dabei gibt es ein Listenelement pro Lehrer
    """
    liste = []

    path = "lehrerdaten.CSV"

    file = open(path, newline='')

    reader = csv.reader(file, delimiter=";")

    header = next(reader)  # Die erste Zeile ist die Ueberschrift

    # Zeilenweise die gesamte Datei durchgehen und pro Zeile ein Listenelement erzeugen
    for row in reader:

        abteilungen = []
        lernbefaehigungen = []

        # Name;Vorname;Nachname;Abt1;Abt2;Abt3;Abt4;Abt5;SOLL;Ist-Soll;LBF1;LBF2;LBF3;
        kuerzel = row[0]
        vorname = row[1]
        name = row[2]
        abt1 = row[3]
        abt2 = row[4]
        abt3 = row[5]
        abt4 = row[6]
        abt5 = row[7]
        soll = float(row[8])
        ist = float(row[9])
        lbf1 = row[10]
        lbf2 = row[11]
        lbf3 = row[12]

        abteilungen.append(abt1)
        abteilungen.append(abt2)
        abteilungen.append(abt3)
        abteilungen.append(abt4)
        abteilungen.append(abt5)

        lernbefaehigungen.append(lbf1)
        lernbefaehigungen.append(lbf2)
        lernbefaehigungen.append(lbf3)

        lehrer = Lehrer()
        lehrer.setData(kuerzel, vorname, name, ist, soll, abteilungen, lernbefaehigungen)

        liste.append(lehrer)

    return liste


def generiererFachListe(lehrer):
    """ Diese Methode geht alle Lehrer durch und generiert zwei Listen.
    Einmal die Liste alle Fachbereiche (Abteilungen), einmal die aller 
    Faecher (also Mathe, Biologie, Kunst und so weiter)
    Am Ende werden beide Liste zurueckgegeben """
    fachliste = []
    fachbereichsliste = []

    for l in lehrer:
        for lfb in l.lfb:
            if lfb not in fachliste:
                fachliste.append(lfb)
        
        for abteilung in l.abteilungen:
            if abteilung not in fachbereichsliste:
                fachbereichsliste.append(abteilung)

    return fachliste, fachbereichsliste


# alle Lehrer werden aus der CSV-Datei eingelesen und in der Liste gespeichert.
# Danach liegen diese als LIste vor. Anleitung dazu hier:
# https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
lehrerliste = dateiEinlesen()

# In Python koennen auch 2 oder mehr Objekte gleichzeitig
# zurueckgegeben werden, daher kann man hier alles in einem Rutsch
# in zwei Objekten speichern
fachliste, fachbereichsliste = generiererFachListe(lehrerliste)
