import sqlite3

from io import BytesIO


def connect_to_db(string):
    con = sqlite3.connect(string)
    return con


class Rapport:

    def __init__(self, con, wfile):
        self.con = con
        self.cur = self.con.cursor()
        self.wfile = wfile

    def get_a_dict_with_db_data(self):
        query = "SELECT word FROM partie5"
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
            response = BytesIO()
            value = str(key) + ":" + str(d[key]) + " \n"
            response.write(bytes(value, 'utf-8'))
            self.wfile.write(response.getvalue())

    def get_most_used_following_word(self, word):
        self.cur.execute("SELECT following_word from partie5 WHERE word=?", (word,))
        dict_of_words = dict()
        data = self.cur.fetchall()
        for line in data:
            word = "".join(line)
            if word in dict_of_words:
                dict_of_words[word] = dict_of_words[word] + 1
            else:
                dict_of_words[word] = 1
        return dict_of_words

    def print_value(self,value):
        response = BytesIO()
        response.write(bytes(value, 'utf-8'))
        self.wfile.write(response.getvalue())

    def sort_a_dict_in_descending_order_by_value(self, d):
        return dict(reversed(sorted(d.items(), key=lambda item: item[1])))

    def get_first_value_from_dict(self, dict):
        d = self.sort_a_dict_in_descending_order_by_value(dict)
        first_value = list(d.keys())[0]
        return first_value

    def run(self):
        d = self.get_a_dict_with_db_data()
        sorted_d = self.sort_a_dict_in_reverse_order(d)
        self.print_key_and_value_from_a_dict(sorted_d)
