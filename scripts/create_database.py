import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        port="8080",
        user="root",
        password="aaa"
    )
    cursor = connection.cursor()

    create_db_query = "CREATE DATABASE IF NOT EXISTS mendelu;"
    cursor.execute(create_db_query)
    print("Databáze 'mendelu' vytvořena.")

    switch_db_query = "USE mendelu;"
    cursor.execute(switch_db_query)
    print("Přepnuto do databáze 'mendelu'.")

except mysql.connector.Error as error:
    print("Chyba při vytváření databáze:", error)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
