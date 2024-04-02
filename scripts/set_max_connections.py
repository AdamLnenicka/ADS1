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

    # 11. Snížení maximálního počtu připojení
    set_max_connections_query = """
        SET GLOBAL max_connections = 10;
    """
    cursor.execute(set_max_connections_query)
    print("Maximální počet připojení snížen.")

except mysql.connector.Error as error:
    print("Chyba při snižování maximálního počtu připojení:", error)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
