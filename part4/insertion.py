import sqlite3


# Script pour la creation de la base de donnees
#con = sqlite3.connect("insertion.sql")
#cur  = con.cursor()
#cur.execute('''CREATE TABLE partie4 (word text)''')
#con.commit()

def connect_to_db(string):
    con = sqlite3.connect(string)
    return con


class Insertion:

    def __init__(self,con):
        self.con = con
        self.cur = self.con.cursor()

    def is_end(self, string):
        if string == "--fin":
            return True
        else:
            return False

    def write_in_db(self, string):
        self.cur.execute('INSERT INTO partie4 VALUES(?)', [string])
        self.con.commit()



