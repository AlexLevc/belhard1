import sqlite3

conn = sqlite3.connect('db.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS statuses(
    id INTEGER PRIMARY KEY,
    name VARCHAR(10) UNIQUE
);
''')
conn.commit()

cur.execute('''
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name VARCHAR(24),
    email VARCHAR(24) UNIQUE
);
''')
conn.commit()

cur.execute('''
CREATE TABLE IF NOT EXISTS categories(
    id INTEGER PRIMARY KEY,
    name VARCHAR(24) UNIQUE
 );
 ''')
conn.commit()

cur.execute('''
CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    status_id INTEGER,
    FOREIGN KEY (status_id) REFERENCES statuses(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
''')
conn.commit()

cur.execute('''CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY,
    title VARCHAR(36),
    description VARCHAR(140),
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(id)
); ''')
conn.commit()

cur.execute('''
CREATE TABLE IF NOT EXISTS order_items(
    id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
    );
''')
conn.commit()






