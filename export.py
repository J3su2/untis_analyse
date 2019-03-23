import csv

# In dieser Datei sol pro Fach eine .csv-Datei generiert werden. Das bedeutet
# zumindestens fuer die erste Version fuer Mathe, Englisch, Biologie, Chemie und Physik
#
# Dabei sollen die Dateien ma.csv, en.csv, bi.csv, ch.csv und ph.csv entstehen
#
# Außerdem soll eine nach Minusstunden sortiere Datei ausgegeben werden. Die haette im 
# Falle der Beispieldaten dann diese Strukur:
#
# Name;Minder
# DDD;6.62
# FFF;6.53
# EE;-2.23
# GG;-5
# BB;-7.48
# CCC;-11.88
# AAA;-19.15


# So geht es grundsaetzlich, in eine .csv-Datei zu schreiben. Die ersten
# beiden Zeilen sind schon korrekt, die letzte Zeile muss ersetzt werden
# durch eine eigenen Logik...
#
#
#with open('minusstunden.csv', mode='w') as minusstunden_file:
#    writer = csv.writer(minusstunden_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#    writer.writerow(['DDD', '6.22'])