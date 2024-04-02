import mysql.connector

try:
    # Připojení k MySQL serveru
    connection = mysql.connector.connect(
        host="localhost",
        port="8080",
        user="root",
        password="aaa",
        database="mysql"
    )

    # Začátek transakce
    connection.start_transaction()

    # Vytvoření kurzoru pro provádění příkazů
    cursor = connection.cursor()

    # 2. Vytvoření uživatele s přístupem z vzdáleného testovacího počítače
    create_user_query = """
        CREATE USER 'xlnenick'@'%' IDENTIFIED BY 'aaa';
        GRANT ALL PRIVILEGES ON *.* TO 'xlnenick'@'%';
        FLUSH PRIVILEGES;
    """
    cursor.execute(create_user_query, multi=True)  # Přidání multi=True
    print("Uživatel vytvořen a oprávnění nastavena.")


    # 3. Nastavení role 'student' pro uživatele 'xlnenick'
    set_role_query = """
        GRANT student TO 'xlnenick'@'%';
    """
    cursor.execute(set_role_query)
    print("Role 'student' nastavena pro uživatele 'xlnenick'.")

    # 4. Nastavení role 'student' jako implicitní role pro uživatele 'xlnenick'
    set_default_role_query = """
        GRANT student TO 'xlnenick'@'%';
    """
    cursor.execute(set_default_role_query)
    print("Role 'student' nastavena jako implicitní pro uživatele 'xlnenick'.")


    # 5. Vytvoření databáze 'mendelu' a přepnutí do ní
    create_db_query = "CREATE DATABASE IF NOT EXISTS mendelu;"
    cursor.execute(create_db_query)
    print("Databáze 'mendelu' vytvořena.")

    switch_db_query = "USE mendelu;"
    cursor.execute(switch_db_query)
    print("Přepnuto do databáze 'mendelu'.")

    # 6. Vytvoření tabulky 'activity' a vložení dat
    create_table_query = """
        CREATE TABLE IF NOT EXISTS activity (
            id INT AUTO_INCREMENT PRIMARY KEY,
            student_name VARCHAR(255),
            activity VARCHAR(255),
            room INT
        );
        INSERT INTO activity (student_name, activity, room) VALUES ('xlnenick', 'studying', 101);
        INSERT INTO activity (student_name, activity, room) VALUES ('someoneelse', 'eating', 102);
    """
    cursor.execute(create_table_query, multi=True)  # Přidání multi=True
    print("Tabulka 'activity' vytvořena a naplněna daty.")


    # 6. Vytvoření VIEW 'my_activity' na tabulku 'activity'
    create_view_query = """
        CREATE VIEW my_activity AS
        SELECT * FROM activity WHERE student_name = 'xlnenick' AND room = (SELECT room FROM activity WHERE student_name = 'xlnenick' GROUP BY room ORDER BY COUNT(*) DESC LIMIT 1);
    """
    cursor.execute(create_view_query)
    print("Pohled 'my_activity' vytvořen.")

    # 7. Nastavení oprávnění role 'student' pro čtení sloupců tabulky 'activity' a pohledu 'my_activity'
    grant_permissions_query = """
        GRANT SELECT ON mendelu.activity TO student;
        GRANT SELECT ON mendelu.my_activity TO student;
    """
    cursor.execute(grant_permissions_query)
    print("Oprávnění pro roli 'student' nastavena.")

    # 8. Zajištění řazení v pohledu 'my_activity' podle sloupce 'activity'
    alter_view_query = """
        ALTER VIEW my_activity AS
        SELECT * FROM activity WHERE student_name = 'xlnenick' AND room = (SELECT room FROM activity WHERE student_name = 'xlnenick' GROUP BY room ORDER BY COUNT(*) DESC LIMIT 1) ORDER BY activity;
    """
    cursor.execute(alter_view_query)
    print("Řazení v pohledu 'my_activity' zajištěno.")

    # 9. Nastavení časové zóny pro Brno
    set_timezone_query = """
        SET @@global.time_zone = 'Europe/Prague';
    """
    cursor.execute(set_timezone_query)
    print("Časová zóna pro Brno nastavena.")

    # 10. Snížení velikosti buffer poolu na 64 MB
    set_buffer_pool_size_query = """
        SET GLOBAL innodb_buffer_pool_size = 64 * 1024 * 1024;
    """
    cursor.execute(set_buffer_pool_size_query)
    print("Velikost buffer poolu snížena na 64 MB.")

    # 11. Snížení maximálního počtu připojení
    set_max_connections_query = """
        SET GLOBAL max_connections = 10;
    """
    cursor.execute(set_max_connections_query)
    print("Maximální počet připojení snížen.")

    # Uložení provedených změn
    connection.commit()
    print("Všechny úkoly byly úspěšně provedeny a transakce byla commitována.")

except mysql.connector.Error as error:
    # Pokud dojde k chybě, rollback transakce
    if 'connection' in locals():
        connection.rollback()
    print("Chyba při provádění úkolů:", error)

finally:
    # Uzavření kurzoru a připojení
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
