import sqlite3

def find_city_by_name(city_name, database):
    conn = sqlite3.connect(database)
    c = conn.cursor()

    # Haetaan nimellä, pyydetään tulokset järjestyksessä väkimäärän mukaan
    sqlitecommand = 'select * from kaupungit where nimi=? order by populaatio desc;'

    # Lähetetään sql-kutsu
    c.execute(sqlitecommand, [city_name])

    # Tallennetaan ensimmäinen tulos (se jossa populaatio on suurin)
    queryresult = c.fetchone()

    conn.close()

    # Palautetaan tulos
    return queryresult


if __name__ == "__main__":
    database = "kaupungit.db"

    inputstring = input("Kaupungin nimi:")

    while inputstring != "":
        queryresult = find_city_by_name(inputstring, database)

        if queryresult:
            # Erotetaan queryresultin eri tietokentät
            dbid, city_name, region_name, country, population, lat, lon = queryresult

            print(city_name, ",", region_name, ",", country)
            print("Väkimäärä:", population)
            print("Koordinaatit: lat/lon", lat, "/", lon)

        else:
            print("Ei löytynyt")

        inputstring = input("Kaupungin nimi:")
