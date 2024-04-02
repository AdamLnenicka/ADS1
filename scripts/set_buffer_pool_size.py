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

    # 10. Snížení velikosti buffer poolu na 64 MB
    set_buffer_pool_size_query = """
        SET GLOBAL innodb_buffer_pool_size = 64 * 1024 * 1024;
    """
    cursor.execute(set_buffer_pool_size_query)
    print("Velikost buffer poolu snížena na 64 MB.")

except mysql.connector.Error as error:
    print("Chyba při snižování velikosti buffer poolu:", error)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
