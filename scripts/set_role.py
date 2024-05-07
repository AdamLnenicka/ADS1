import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        port="8080",
        user="root",
        password="aaa"
    )
    cursor = connection.cursor()

    set_role_query = """
        SET DEFAULT ROLE 'student' FOR 'xlnenick'@'%';
    """
    cursor.execute(set_role_query)
    print("Role 'student' nastavena pro uživatele 'xlnenick'.")

except mysql.connector.Error as error:
    print("Chyba při nastavování role:", error)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
