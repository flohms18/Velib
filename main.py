import duckdb

conn = duckdb.connect('my_duck.db')




conn.execute('SELECT * FROM tennis_brand').df()



