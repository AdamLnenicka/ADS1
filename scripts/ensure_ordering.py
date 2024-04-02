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

    # 8. Zajištění řazení v pohledu 'my_activity' podle sloupce 'activity'
    alter_view_query = """
        ALTER VIEW my_activity AS
        SELECT * FROM activity WHERE student = 'xlnenick' AND room = (SELECT room FROM activity WHERE student = 'xlnenick' GROUP BY room ORDER BY COUNT(*) DESC LIMIT 1) ORDER BY activity;
    """
    cursor.execute(alter_view_query)
    print("Řazení v pohledu 'my_activity' zajištěno.")

except mysql.connector.Error as error:
    print("Chyba při zajišťování řazení v pohledu 'my_activity':", error)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
