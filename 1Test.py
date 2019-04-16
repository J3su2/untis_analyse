#Import
import pandas as pd 

#Einlesen der Datei / Abstandhalter definieren / encoding definieren (muss nicht, glaube ich macht OpenOffice automatisch. Nur wenn man die Datei noch nie geöffnet hat)
df = pd.read_csv("D:/Desktop/Projekt dv ni/lehrerdaten.csv", delimiter=";", encoding = "ISO-8859-1")

#Zuerst auf die beiden Spalten reduzieren
df = df[["Name", "Ist-Soll"]]
#dann nach "Ist-Soll" abfallend sortieren
df = df.sort_values("Ist-Soll", ascending=False)

#als .csv Datei exportieren, ohne Auto-Index / (Seperator = ",")
df.to_csv("D:/Desktop/Projekt dv ni/lehrerdatenexport.csv", index=False)
#Nochmal als .txt exportieren, diesmal mit ";" als Seperator. 
df.to_csv("D:/Desktop/Projekt dv ni/lehrerdatenexport.txt", sep=";", index=False)


#-------------------------------------Notizen----------------------------------------------------------------------------------------
# print(df)
#print (df.columns)
#print (df[["Name", "Ist-Soll"]][0:5]) 
#print(df.describe())
#print(df.sort_values("Ist-Soll", ascending=False))

