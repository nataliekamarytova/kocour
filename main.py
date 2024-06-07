from kocour.databaze import pridej_vahu 
from kocour.vypocty import prum_prirustek 
import sqlite3
from datetime import datetime
from enum import Enum

class Moznosti(Enum):
    AKTUALNI_VAHA = 1
    HISTORICKA_VAHA = 2
    VAHOVY_NARUST = 3
    PRUM_PRIRUSTEK = 4
    MOZNOSTI = 5
    ZAVRIT = 6

connection = sqlite3.connect("kocour.db")

cursor = connection.cursor()
cursor.execute("CREATE TABLE if not exists vahy (datum TEXT, vaha REAL)")



UVOD =(f""" Ahoj, vitej v nasi aplikaci. Muzes zde vybirat z nekolika funkci.
{Moznosti.AKTUALNI_VAHA.value} - Zadat aktuální vahu kocoura.
{Moznosti.HISTORICKA_VAHA.value} - Zadat historickou vahu kocoura.
{Moznosti.VAHOVY_NARUST.value} - Vypsat postupny vahovy narust.
{Moznosti.PRUM_PRIRUSTEK.value} - Spocitat prumerny prirustek kocoura za den.
{Moznosti.MOZNOSTI.value} - Vypsat znovu moznosti.
{Moznosti.ZAVRIT.value} - Zavrit aplikaci """)
print(UVOD) 

while True:
    vyber = input('Vyber co chces udelat')
    if vyber == str(Moznosti.AKTUALNI_VAHA.value):
        vaha = input('Zadej vahu kocoura:')
        from datetime import date
        datum = date.today() 
        cursor.execute("INSERT INTO vahy VALUES (?, ?)",(str(datum), float(vaha)))
        connection.commit()
    elif vyber == str(Moznosti.HISTORICKA_VAHA.value):
        pass
    elif vyber == str(Moznosti.VAHOVY_NARUST.value):
        pass
    elif vyber == str(Moznosti.PRUM_PRIRUSTEK.value):
        vahy = []
        datumy = []
        rows = cursor.execute("SELECT * FROM vahy").fetchall()
        for (datum,vaha) in rows:
            vahy.append(vaha)
        prirustek = vahy[-1]-vahy[0]

        rows = cursor.execute("SELECT * FROM vahy").fetchall()
        for (datum,vaha) in rows:
            datum = datetime.strptime(datum, "%Y-%m-%d")
            datumy.append(datum)
        rozdíl = (datumy[-1]-datumy[0]).days

        denni_prirustek = prirustek/rozdíl
        print(denni_prirustek)
    elif vyber == str(Moznosti.MOZNOSTI.value):
        print(UVOD)
    elif vyber == str(Moznosti.ZAVRIT.value):
        break
    break

