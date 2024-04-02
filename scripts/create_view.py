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

    # 6. Vytvoření VIEW 'my_activity' na tabulku 'activity'
    create_view_query = """
        CREATE VIEW my_activity AS
        SELECT * FROM activity WHERE student = 'xlnenick' AND room = (SELECT room FROM activity WHERE student = 'xlnenick' GROUP BY room ORDER BY COUNT(*) DESC LIMIT 1);
    """
    cursor.execute(create_view_query)
    print("Pohled 'my_activity' vytvořen.")

except mysql.connector.Error as error:
    print("Chyba při vytváření pohledu 'my_activity':", error)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
