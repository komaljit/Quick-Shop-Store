import sqlite3

#Open database
conn = sqlite3.connect('database.db')

#Create table
try:
    conn.execute('''CREATE TABLE users 
                (userId integer primary key autoincrement,
  		password TEXT,
		email TEXT unique,
		firstName TEXT,
		lastName TEXT,
		address1 TEXT,
		address2 TEXT,
		zipcode TEXT,
		city TEXT,
		state TEXT,
		country TEXT, 
		phone TEXT,
                image TEXT
		)''')
except:
    pass
try:
    conn.execute('''CREATE TABLE products
                (productId INTEGER primary key autoincrement,
		name TEXT,
		price REAL,
		description TEXT,
		image TEXT,
		stock INTEGER,
		categoryId INTEGER,
		FOREIGN KEY(categoryId) REFERENCES categories(categoryId)
		)''')
except:
    pass
try:
    conn.execute('''CREATE TABLE kart
		(userId Integer primary key,
		productId INTEGER,
                quantity integer,
		FOREIGN KEY(userId) REFERENCES users(userId),
		FOREIGN KEY(productId) REFERENCES products(productId)
		)''')
except:
    pass

try:
    conn.execute('''CREATE TABLE categories
		(categoryId INTEGER PRIMARY KEY,
		name TEXT,
                image TEXT
		)''')
except:
    pass
         
