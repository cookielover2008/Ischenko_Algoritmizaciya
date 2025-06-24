# Приложение ПРОМЫШЛЕННОСТЬ для автоматизированного учета
# информации о промышленных предприятиях республики.

import sqlite3

def execute_sql_from_file(conn, sql_file):
    with open(sql_file, 'r', encoding='utf-8') as file:
        sql_script = file.read()
        cursor = conn.cursor()
        cursor.executescript(sql_script)  # Исправлено: выполняем весь скрипт
        conn.commit()

if __name__ == "__main__":
    conn = sqlite3.connect("Enterprises.db")
    execute_sql_from_file(conn, "D:\PzManakova\pz15\code.sql")
    conn.close()
    print("База данных и таблица успешно созданы.")
