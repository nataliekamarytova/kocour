from kocour.databaze import pridej_vahu 
from kocour.vypocty import prum_prirustek 
import sqlite3
from datetime import datetime

connection = sqlite3.connect("kocour.db")

cursor = connection.cursor()
cursor.execute("CREATE TABLE if not exists vahy (datum TEXT, vaha REAL)")



UVOD =(""" Ahoj, vitej v nasi aplikaci. Muzes zde vybirat z nekolika funkci.
1 - Zadat aktuální vahu kocoura.
2 - Zadat historickou vahu kocoura.
3 - Vypsat postupny vahovy narust.
4 - Spocitat prumerny prirustek kocoura za den.
5 - Vypsat znovu moznosti.
6 - Zavrit aplikaci """)
print(UVOD) 

while True:
    vyber = input('Vyber co chces udelat')
    if vyber == '1':
        vaha = input('Zadej vahu kocoura:')
        from datetime import date
        datum = date.today() 
        cursor.execute("INSERT INTO vahy VALUES (?, ?)",(str(datum), float(vaha)))
        connection.commit()
    elif vyber == '3':
        pass
    elif vyber == '4':
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
    elif vyber == '5':
        print(UVOD)
    elif vyber == '6':
        break
    break

