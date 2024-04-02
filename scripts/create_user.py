import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        port="8080",
        user="root",
        password="aaa"
    )
    cursor = connection.cursor()

    create_user_query = """
        CREATE USER 'xlnenick'@'%' IDENTIFIED BY 'aaa';
        GRANT ALL PRIVILEGES ON *.* TO 'xlnenick'@'%';
        FLUSH PRIVILEGES;
    """
    cursor.execute(create_user_query)
    print("Uživatel 'xlnenick' vytvořen a oprávnění nastavena.")

except mysql.connector.Error as error:
    print("Chyba při vytváření uživatele:", error)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
