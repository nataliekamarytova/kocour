#sem vse funkce z vyberu
from datetime import datetime, date


def pridej_aktualni_vahu(cursor, connection):
    vaha = input('Zadej aktuální váhu kocoura:')
    datum = date.today() 
    cursor.execute("INSERT INTO vahy VALUES (?, ?)",(str(datum), float(vaha)))
    connection.commit()
def pridej_historickou_vahu(cursor,connection):
    vaha = input('Zadej historickou váhu kocoura:')
    datum = input('Zadej datum ze kterého byla tato váha ve formátu yyyy-mm-dd:')
    cursor.execute("INSERT INTO vahy VALUES (?, ?)",(str(datum), float(vaha)))
    connection.commit()
def zobraz_postupny_narust(cursor):
    rows = cursor.execute("SELECT * FROM vahy").fetchall()
    for (datum,vaha) in rows:
        print(datum,vaha)
def vypocitej_prirustek(cursor):
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
    return(denni_prirustek)