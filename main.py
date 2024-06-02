from kocour.databaze import pridej_vahu 
from kocour.vypocty import prum_prirustek 
import sqlite3

connection = sqlite3.connect("kocour.db")

cursor = connection.cursor()
cursor.execute("CREATE TABLE if not exists vahy (datum TEXT, vaha REAL)")



UVOD =(""" Ahoj, vitej v nasi aplikaci. Muzes zde vybirat z nekolika funkci.
1 - Zadat vahu kocoura.
2 - Vypsat postupny vahovy narust.
3 - Spocitat prumerny prirustek kocoura za den.
4 - Vypsat znovu moznosti.
5 - Zavrit aplikaci. """)
print(UVOD) 

while True:
    vyber = input('Vyber co chces udelat')
    if vyber == '1':
        vaha = input('Zadej vahu kocoura:')
        from datetime import date
        datum = date.today() 
        cursor.execute("INSERT INTO vahy VALUES (?, ?)",(str(datum), float(vaha)))
        connection.commit()
    elif vyber == '2':
        pass
    elif vyber == '3':
        vahy = []
        datumy = []
        rows = cursor.execute("SELECT * FROM vahy").fetchall()
        for (datum,vaha) in rows:
            vahy.append(vaha)
        prirustek = vahy[-1]-vahy[0]
        print(prirustek)

        '''print(prum_prirustek(vahy))
        for (datum,vaha) in rows:
            datumy.append(datum)
        print(datumy)
            # extrahovat si datumy tak jak nahoře
            # date.time --->převést datovy typ string na datovy typ datum
            # odecist prvni datum od posledniho 
            # prevest si datum na cislo a vydelit prumerny prirustek'''
    elif vyber == '4':
        print(UVOD)
    elif vyber == '5':
        break
    break

