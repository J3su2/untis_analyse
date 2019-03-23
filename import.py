import csv

path = "lehrerdaten.CSV"

file = open(path, newline='')

reader = csv.reader(file, delimiter=";")

header = next(reader) # Die erste Zeile ist die Ueberschrift

data = []

for row in reader:
    # Kuerzel, Vorname, Name, ABT1 -> ABT4, SOLL, IST-SOLL, FAECHER, LBF1, LBF2, LBF3
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
    faecher = row[10]
    lbf1 = row[11]
    lbf2 = row[12]
    lbf3 = row[13]

    data.append([kuerzel,vorname,name,abt1,abt2,abt3,abt4,abt5,soll,ist,faecher,lbf1,lbf2,lbf3])

print(data[1])


print(data.sort())