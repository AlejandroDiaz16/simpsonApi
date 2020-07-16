import pandas as pd
from sqlalchemy import create_engine

db_connect = create_engine('sqlite:///simpson.db')
# rutas excel
df = pd.read_csv('./characters.csv')
cant = int(df['Name'].apply(type).value_counts())
df_characters = pd.read_csv('./characters.csv')
cant_characters = int(df_characters['Name'].apply(type).value_counts())


def insertAllCharacters():
    conn = db_connect.connect()
    query1 = conn.execute('delete from characters')
    for i in range(cant_characters):
        query = conn.execute("insert into characters values("
                             "'%s','%s','%s','%s','%s','%s','%s'"
                             ",'%s','%s','%s','%s')" % (i+1, df_characters['Name'][i],
                                                        df_characters['Age'][i],
                                                        df_characters['Status'][i],
                                                        df_characters['Gender'][i],
                                                        df_characters['Image'][i],
                                                        df_characters['Occupation'][i],
                                                        df_characters['Apparition'][i],
                                                        df_characters['Voice'][i],
                                                        df_characters['Created'][i],
                                                        df_characters['Edited'][i]))
    conn.close()


def insertAllEpisodes():
    conn = db_connect.connect()
    #query1 = conn.execute('delete from episodes')
    for i in range(cant):
        query = conn.execute("insert into characters values("
                             "'%s','%s','%s','%s','%s','%s','%s')" % (
                                                        i+1,
                                                        df['Name'][i],
                                                        df['Air_date'][i],
                                                        df['Season'][i],
                                                        df['Episode'][i],
                                                        df['Created'][i],
                                                        df['Edited'][i]))
    conn.close()


def insertAllCities():
    conn = db_connect.connect()
    #query1 = conn.execute('delete from episodes')
    for i in range(cant):
        query = conn.execute("insert into cities values("
                             "'%s','%s','%s','%s','%s','%s')" % (
                                                        i+1,
                                                        df['Name'][i],
                                                        df['Population'][i],
                                                        df['Image'][i],
                                                        df['Created'][i],
                                                        df['Edited'][i]))
    conn.close()


def insertAllLocations():
    conn = db_connect.connect()
    #query1 = conn.execute('delete from locations')
    for i in range(cant):
        query = conn.execute("insert into locations values("
                             "'%s','%s','%s','%s','%s','%s','%s')" % (
                                                        i+1,
                                                        df['Name'][i],
                                                        df['Type'][i],
                                                        df['Use'][i],
                                                        df['Image'][i],
                                                        df['Created'][i],
                                                        df['Edited'][i]))
    conn.close()


operationsAdd = {'1': insertAllCharacters()}
option = input("What do you want to do today:\n1 - Add\n2 - Delete\n3 - Update\n")

if option == 1:
    secondary = input("1 allcharacters 2 allcities 3 onecharacter")
    operationsAdd[secondary]

conn = db_connect.connect()
query = conn.execute("select * from characters")
result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
print(result)
