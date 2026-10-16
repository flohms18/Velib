import duckdb

conn = duckdb.connect('my_duck.db')


conn.execute('''
CREATE TABLE tennis_brand (
id INTEGER PRIMARY KEY,
name VARCHAR,
nationality INTEGER,
)
'''
)

conn.execute('SHOW TABLES').df()



