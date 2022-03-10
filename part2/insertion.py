import sqlite3


# Script pour la creation de la base de donnees
# con = sqlite3.connect("insertion.sql")
# cur = con.cursor()
# cur.execute('''CREATE TABLE partie2 (word text)''')
# con.commit()

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
        self.cur.execute('INSERT INTO partie2 VALUES(?)', [string])
        self.con.commit()

    def run(self):
        print("Inserez des mots, entrez --fin pour arreter l'insertion")
        end = False
        while not end:
            a = str(input())
            if self.is_end(a):
                end = True
            else:
                list_input = [a]
                for word in list_input[0].split():
                    self.write_in_db(word)


if __name__ == '__main__':
    insertion = Insertion(connect_to_db('insertion.sql'))
    insertion.run()
