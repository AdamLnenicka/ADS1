import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        port="8080",
        user="root",
        password="aaa",
        database="mendelu"  # Přepnutí na existující databázi 'mendelu'
    )
    cursor = connection.cursor()

    # 9. Nastavení časové zóny pro Brno
    set_timezone_query = """
        SET @@global.time_zone = 'Europe/Prague';
    """
    cursor.execute(set_timezone_query)
    print("Časová zóna pro Brno nastavena.")

except mysql.connector.Error as error:
    print("Chyba při nastavování časové zóny pro Brno:", error)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
