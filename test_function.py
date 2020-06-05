from data_functions import *

delete_data("data1")
create_data("data1")
conn = new_user("data1")
cursor = conn.cursor()

tables_and_procedures(cursor)
cursor.execute("SELECT add_product(\'Cake\', 50)")
cursor.execute("SELECT add_product(\'Carrot\', 15)")
cursor.execute("SELECT add_sale(1, 5)")
cursor.execute("SELECT add_sale(1, 1)")
cursor.execute("SELECT add_sale(1, 2)")

cursor.execute("SELECT * FROM get_all_sale()")
rows = cursor.fetchall()
print(rows)

cursor.execute("SELECT * FROM get_all_product()")
rows = cursor.fetchall()
print(rows)

cursor.execute("SELECT * FROM get_trigger()")
rows = cursor.fetchall()
print(rows)

cursor.execute("SELECT * FROM find_product(\'Cake\')")
rows = cursor.fetchall()
print(rows)

cursor.execute("SELECT delete_product(\'Cake\')")
cursor.execute("SELECT * FROM get_all_product()")
rows = cursor.fetchall()
print(rows)

cursor.execute("SELECT delete_sale(2)")
cursor.execute("SELECT * FROM get_all_sale()")
rows = cursor.fetchall()
print(rows)

cursor.close()
conn.close()
delete_data("data1")

