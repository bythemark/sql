import sqlite3
import math


def matka(lat1, lon1, lat2, lon2):
    R = 6371.0

    lon1 = float(lon1) * math.pi/180
    lat1 = float(lat1) * math.pi/180
    lon2 = float(lon2) * math.pi/180
    lat2 = float(lat2) * math.pi/180

    kulma = math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon2-lon1))
    # print(kulma)
    matkan_pituus = kulma * R

    return matkan_pituus


def hae_kaupunki(nimi, dbname):

    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    sqlitecommand = 'select * from kaupungit where nimi=? order by populaatio desc;'

    c.execute(sqlitecommand, [nimi])
    result = c.fetchone()
    conn.close()

    return result


if __name__ == "__main__":
    dbname = 'kaupungit.db'

    inputstring1 = input("Ensimmäisen kaupungin nimi:")
    inputstring2 = input("Toisen kaupungin nimi:")

    queryresult1 = hae_kaupunki(inputstring1, dbname)
    queryresult2 = hae_kaupunki(inputstring2, dbname)

    if queryresult1 and queryresult2:

        _, nimi1, _, _, _, lat1, lon1 = queryresult1
        _, nimi2, _, _, _, lat2, lon2 = queryresult2

        matkan_pituus = matka(lat1, lon1, lat2, lon2)
        print(nimi1, lat1, lon1)
        print(nimi2, lat2, lon2)
        print("Etäisyys", nimi1, "ja", nimi2, "välillä on", matkan_pituus, "km.")

    else:

        print("Ei löytynyt")
