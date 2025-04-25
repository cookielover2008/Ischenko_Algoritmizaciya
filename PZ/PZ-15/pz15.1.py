# Приложение ПРОМЫШЛЕННОСТЬ для автоматизированного учета
# информации о промышленных предприятиях республики. БД содержит таблицу
# Предприятия, имеющую следующую структуру записи: Код предприятия, Наименование
# предприятия, Физический адрес, Филиалы (количество филиалов), Общая числ. персонала,
# Общая стоим. оборудования, Объем выпускаемой продукции, Дата регистрации.

import sqlite3

conn = sqlite3.connect("Enterprises.db")

def execute_sql_from_file(conn, sql_file):
    with open(sql_file, 'r', encoding='utf-8') as file:
        sql_script = file.read()
        cursor = conn.cursor()
        cursor.execute(sql_script)
        conn.commit()

execute_sql_from_file(conn, 'code.sql')
conn.close()