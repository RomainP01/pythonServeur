import sqlite3


def connect_to_db(string):
    con = sqlite3.connect(string)
    return con


class Rapport:

    def __init__(self,con):
        self.con = con
        self.cur = self.con.cursor()

    def get_a_dict_with_db_data(self):
        query = "SELECT word FROM partie2"
        self.cur.execute(query)
        dict_of_words = dict()
        for line in self.cur:
            word = "".join(line)
            if word in dict_of_words:
                dict_of_words[word] = dict_of_words[word] + 1
            else:
                dict_of_words[word] = 1

        return dict_of_words

    def sort_a_dict_in_reverse_order(self, dict_to_be_sorted):
        return dict(reversed(sorted(dict_to_be_sorted.items(), key=lambda item: item[1])))

    def print_key_and_value_from_a_dict(self, d):
        for key in list(d.keys()):
            print(str(key) + ":" + str(d[key]))

    def run(self):
        d = self.get_a_dict_with_db_data()
        sorted_d = self.sort_a_dict_in_reverse_order(d)
        self.print_key_and_value_from_a_dict(sorted_d)

if __name__ == '__main__':
    rapport = Rapport(connect_to_db('insertion.sql'))
    rapport.run()
