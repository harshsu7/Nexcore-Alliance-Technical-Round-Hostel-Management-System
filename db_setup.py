import sqlite3

conn = sqlite3.connect("hostel.db")
cursor = conn.cursor()

# Creating admin table
cursor.execute("""
CREATE TABLE IF NOT EXISTS admin (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL
)
""")

# Creating beds table (10 beds)
cursor.execute("""
CREATE TABLE IF NOT EXISTS beds (
    bed_id INTEGER PRIMARY KEY,
    status TEXT DEFAULT 'available'
)
""")

# Inserting 10 beds 
cursor.execute("SELECT COUNT(*) FROM beds")
count = cursor.fetchone()[0]
if count == 0:
    for i in range(1, 11):
        cursor.execute("INSERT INTO beds (bed_id, status) VALUES (?, 'available')", (i,))

# Creating user ka tables 
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    bed_id INTEGER,
    FOREIGN KEY (bed_id) REFERENCES beds(bed_id)
)
""")

# I am inserting my name as admin
cursor.execute("SELECT * FROM admin WHERE username = 'Harsh'")
if not cursor.fetchone():
    cursor.execute("INSERT INTO admin (username, password) VALUES (?, ?)", ('Harsh', 'Harsh123'))

conn.commit()
conn.close()

print("Database setup completed.")
