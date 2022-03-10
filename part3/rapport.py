import argparse
import sqlite3


def connect_to_db(string):
    con = sqlite3.connect(string)
    return con


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--char', help='Print occurences of each chars instead of words', action='store_true')
    args = parser.parse_args()
    return args


class Rapport:

    def __init__(self, con, args):
        self.con = con
        self.cur = self.con.cursor()
        self.args = args

    def choose_between_words_and_chars(self):
        if self.args.char:
            return self.get_a_dict_with_db_data_char()
        else:
            return self.get_a_dict_with_db_data()

    def get_a_dict_with_db_data(self):
        query = "SELECT word FROM partie3"
        self.cur.execute(query)
        dict_of_words = dict()
        for line in self.cur:
            word = "".join(line)
            if word in dict_of_words:
                dict_of_words[word] = dict_of_words[word] + 1
            else:
                dict_of_words[word] = 1

        return dict_of_words

    def get_a_dict_with_db_data_char(self):
        dict_of_chars = dict()
        d = self.get_a_dict_with_db_data()
        for word in d:
            for char in word:
                if char in dict_of_chars:
                    dict_of_chars[char] = dict_of_chars[char] + 1
                else:
                    dict_of_chars[char] = 1
        return dict_of_chars

    def sort_a_dict_in_reverse_order(self, dict_to_be_sorted):
        return dict(reversed(sorted(dict_to_be_sorted.items(), key=lambda item: item[1])))

    def print_key_and_value_from_a_dict(self, d):
        for key in list(d.keys()):
            print(str(key) + ":" + str(d[key]))

    def run(self):
        d = self.choose_between_words_and_chars()
        sorted_d = self.sort_a_dict_in_reverse_order(d)
        self.print_key_and_value_from_a_dict(sorted_d)


if __name__ == '__main__':
    rapport = Rapport(connect_to_db('insertion.sql'), create_parser())
    rapport.run()
