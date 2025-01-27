from helper import som
from presentatie import presenteer
import csv

mijn_dict = {
    "Aardbeiden-ijs-totaal" : 1000,
    "Vanille-ijs-totaal" : 2000,
    "Chocolade-ijs-totaal" : 1500,
    "Waterijsjes-totaal" : 750
}
totaal_inkomsten = som(mijn_dict)

presenteer(mijn_dict, totaal_inkomsten)

with open('boekhouding.csv', 'w', newline=') as csvfile:
    for key, value in inkomsten.items():
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow([key,value])