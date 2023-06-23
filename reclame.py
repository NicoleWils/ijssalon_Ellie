from algemene_functies import mijn_functie_2

def aanbieding_1(smaak,prijs,korting):
    nieuwe_prijs=prijs-prijs*korting
    uitvoer=f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs} euro."
    return uitvoer
print (aanbieding_1("aardbei",4,0.1))

def inkomsten_totaal(inkomsten,btw):
    res=0
    for i in inkomsten:
        res=res+i
    btw=res*btw
    uitvoer=f"Het totaal van alle inkomsten van deze week is {res} euro, waarover {btw} euro BTW betaald dient te worden."
    return uitvoer
inkomsten=[220,430,125,160,205,90,345]
print (inkomsten_totaal(inkomsten,0.09))

def hoog_en_laag(mijn_lijst):
    hoog=max(mijn_lijst)
    laag=min(mijn_lijst)
    hooglaag=[hoog,laag]
    return hooglaag
mijn_lijst=inkomsten
print (hoog_en_laag(mijn_lijst))

import statistics
def gemiddelde(mijn_lijst):
    gem=statistics.mean(mijn_lijst)
    uitvoer=f"De gmiddelde inkomsten deze week zijn {gem} euro."
    return uitvoer
print (gemiddelde(mijn_lijst))

def meervoudig(invoer_lijst):
    return hoog_en_laag(invoer_lijst)
invoer_lijst=[10,5,3,2,1,2,9]
print (meervoudig(invoer_lijst))

def combinatie(invoer_lijst_2):
    korte_lijst=hoog_en_laag(invoer_lijst_2)
    uitvoer=mijn_functie_2(korte_lijst[0],korte_lijst[1])
    return uitvoer


