import sqlite3


# Script pour la creation de la base de donnees
#con = sqlite3.connect("insertion.sql")
#cur  = con.cursor()
#cur.execute('''CREATE TABLE partie5 (word text, following_word text)''')
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

    def write_in_db(self, string, string2):
        self.cur.execute('INSERT INTO partie5 VALUES(?,?)', [string,string2])
        self.con.commit()




