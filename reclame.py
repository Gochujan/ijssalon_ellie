from algemene_functies import mijn_functie_2

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1 - korting)
    uitvoer = f"vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro."
    return uitvoer
print(aanbieding_1('aardbei', 4, 0.1))

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    resultaat = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag:.2f} euro btw betaald dient te worden."
    return resultaat
inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
btw_percentage = 0.09
print(inkomsten_totaal(inkomsten_per_dag, btw_percentage))

def laag_en_hoog(mijn_lijst):
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    return laagste, hoogste

mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
print(laag_en_hoog(mijn_lijst))

def gemiddelde(mijn_lijst):
    return sum(mijn_lijst) / len (mijn_lijst)
mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
gemiddelde = gemiddelde(mijn_lijst)
print(f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro.")

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)
invoer_lijst = [10,5,3,2,1,2,9]

print(laag_en_hoog(invoer_lijst))
