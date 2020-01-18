import sqlite3
con = sqlite3.connect("levelcarts.db")
cur = con.cursor()
cur.execute("""INSERT INTO cartslevels(info) VALUES('1')""").fetchall()
con.commit()
con.close()