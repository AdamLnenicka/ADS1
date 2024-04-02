import mysql.connector

def test_mysql_connection():
    try:
        # Připojení k MySQL serveru
        connection = mysql.connector.connect(
            host="localhost",
            port="8080",
            user="root",
            password="aaa",
            database="mysql"
        )
        print("Připojení k MySQL serveru bylo úspěšné.")
        return True
    except mysql.connector.Error as error:
        print("Chyba při připojování k MySQL serveru:", error)
        return False
    finally:
        if connection.is_connected():
            connection.close()

def test_created_user():
    try:
        # Připojení k MySQL serveru
        connection = mysql.connector.connect(
            host="localhost",
            port="8080",
            user="xlnenick",
            password="aaa",
            database="mysql"
        )
        print("Uživatel 'xlnenick' byl úspěšně vytvořen.")
        return True
    except mysql.connector.Error as error:
        print("Chyba při připojování jako uživatel 'xlnenick':", error)
        return False
    finally:
        if connection.is_connected():
            connection.close()

# Spuštění testů
if __name__ == "__main__":
    print("Spouštím testování...")
    if test_mysql_connection():
        test_created_user()
    else:
        print("Testování nemůže pokračovat kvůli chybě při připojování k MySQL serveru.")
