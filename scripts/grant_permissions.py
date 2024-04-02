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

    # 7. Nastavení oprávnění role 'student' pro čtení sloupců tabulky 'activity' a pohledu 'my_activity'
    grant_permissions_query = """
        GRANT SELECT ON activity TO student;
        GRANT SELECT ON my_activity TO student;
    """
    cursor.execute(grant_permissions_query, multi=True)
    print("Oprávnění pro roli 'student' nastavena.")

except mysql.connector.Error as error:
    print("Chyba při nastavování oprávnění pro roli 'student':", error)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
