import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
#C:\\Users\\rahul\mbox.txt

fh = open(fname)

for line in fh:
    if not line.startswith('From:'): 
        continue
    pieces = line.split()
    email = pieces[1]
    domain = email.split('@')
    email = domain[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (email,))
conn.commit()


sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

total_count = 0
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
    total_count = total_count + int(row[1])

print(total_count)
    
cur.close()
