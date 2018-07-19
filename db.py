import sqlite3

conn = sqlite3.connect('voicemails.db3')

c = conn.cursor()
c.execute('''CREATE TABLE voicemails(uid integer primary key not null, vmfiles text)''')
conn.commit()

conn.close()