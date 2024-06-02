import functools

def prum_prirustek(vahy):
    vysledek = []
    predchozi=0
    # protože od první hodnoty nic nechci odečíst nastavím si proměnnou = 0
    for i,vaha in enumerate(vahy) : 
    # https://stackoverflow.com/questions/522563/how-to-access-the-index-value-in-a-for-loop
    # zde si nastavím, aby cyklus jel přes jednotlivé indexy a mohla jsem pak s nimi dale pracovat
        if i ==0:
            predchozi=vaha    
            continue  
        # od prvního indexu nechci nic odečíst, takže si ho dám do proměnné předchozí a další kroky přeskočím
        vysledek.append(vaha-predchozi)
        # s další váhou již pracuji dále, odečítám od ní váhu předchozí a přidávám do nového seznamu definovaneho na prvním řádku proměnou vysledek
        predchozi=vaha
        # do promenne predchozi si nastavuji dalsi vahu, kterou pak budu odecitat od vahy nasledujici
    return vysledek

print(prum_prirustek([1,3,5]))

