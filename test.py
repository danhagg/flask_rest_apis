import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# This query defines the schema
create_table = "CREATE TABLE users (id int, username text, password text)"

cursor.execute(create_table)

# user tuple
user = (1, 'dan', 'pass')

insert_query = "INSERT INTO users VALUES (?, ?, ?)"

# cursor smart enough to swap tuple for ?'s
cursor.execute(insert_query, user)

# save
connection.commit()
connection.close()