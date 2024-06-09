import sqlite3
from kocour.prikazy import pridej_aktualni_vahu, pridej_historickou_vahu, zobraz_postupny_narust,vypocitej_prirustek

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
        pridej_aktualni_vahu(cursor, connection)
    elif vyber == '2':
        pridej_historickou_vahu(cursor, connection)
    elif vyber == '3':
        zobraz_postupny_narust(cursor)
    elif vyber == '4':
       prirustek = vypocitej_prirustek(cursor)
       print(prirustek)
    elif vyber == '5':
        print(UVOD)
    else:
        break
    break

