Podle zadaní projektu, všechny požadavky budou realizovány v databázi `mendelu`, která je součástí instance MySQL běžícího v Docker kontejneru. Níže jsou uvedeny jednotlivé úkoly a v jaké databázi budou provedeny:

1. Vytvoření uživatele `<vaslogin>` (např. `xnovak`) s heslem `aaa` - tento úkol se provede v databázi MySQL (většinou se používá systémová databáze `mysql` pro správu uživatelů a jejich oprávnění).
2. Vytvoření role `student` - rovněž se provede v databázi MySQL.
3. Přiřazení role `student` uživateli `<vaslogin>` a nastavení role jako implicitní - opět v databázi MySQL.
4. Vytvoření databáze `mendelu` - v databázi MySQL.
5. Vytvoření tabulky `activity` a naplnění daty - v databázi `mendelu`.
6. Vytvoření VIEW `my_activity` - opět v databázi `mendelu`.
7. Nastavení oprávnění role `student` pro čtení sloupců tabulky `activity` a pohledu `my_activity` - v databázi `mendelu`.
8. Zajištění řazení v pohledu `my_activity` podle sloupce `activity` - v databázi `mendelu`.
9. Nastavení časové zóny pro Brno - v databázi MySQL.
10. Snížení velikosti buffer poolu na 64 MB - v databázi MySQL.
11. Snížení maximálního počtu připojení - v databázi MySQL.

Celkově je tedy většina úkolů prováděna v databázi `mendelu`, ale některé nastavení a správa uživatelů a systémových parametrů se provádí v databázi MySQL.


progress;

Uživatel vytvořen a oprávnění nastavena.
Role 'student' nastavena pro uživatele 'xlnenick'.
Role 'student' nastavena jako implicitní pro uživatele 'xlnenick'.
Databáze 'mendelu' vytvořena.
Přepnuto do databáze 'mendelu'.
Tabulka 'activity' vytvořena a naplněna daty.
Chyba při provádění úkolů: 1146 (42S02): Table 'mendelu.activity' doesn't exist