import mysql.connector
import csv

try:
    connection = mysql.connector.connect(
        host="localhost",
        port="8080",
        user="root",
        password="aaa",
        database="mendelu"  # Přepnutí na existující databázi 'mendelu'
    )
    cursor = connection.cursor()

    # 5b. Vytvoření tabulky 'activity'
    create_table_query = """
        CREATE TABLE IF NOT EXISTS `activity` (
            `datetime` datetime NOT NULL,
            `student` varchar(127) CHARACTER SET ascii COLLATE ascii_general_ci NOT NULL,
            `room` varchar(7) CHARACTER SET ascii COLLATE ascii_general_ci NOT NULL,
            `activity` varchar(63) DEFAULT NULL
        );
    """
    cursor.execute(create_table_query)
    print("Tabulka 'activity' vytvořena.")

    # Nahrání dat z CSV souboru do tabulky 'activity'
    with open('data/student_activity.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            insert_data_query = """
                INSERT INTO activity (`datetime`, `student`, `room`, `activity`)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insert_data_query, row)

    print("Data vložena do tabulky 'activity'.")

except mysql.connector.Error as error:
    print("Chyba při vytváření tabulky 'activity' nebo vkládání dat:", error)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
