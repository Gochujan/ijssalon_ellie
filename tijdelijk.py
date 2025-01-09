prijzen = {
    'aardbei' : 3,
    'vanille' : 4,
    'chocolade' : 5
}
aanbieding = prijzen['vanille'] * 0.8
print(aanbieding)
reclame_tekst = (f'vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding:.2f}')
#Ik heb opdracht 5 op een andere manier opgelost
reclame_tekst3 = reclame_tekst.upper()
reclame_tekst4 = reclame_tekst3.split()
for el in reclame_tekst4:
    if len(el) >= 5:
        print(el.upper())
    else:
        print(el.lower())
