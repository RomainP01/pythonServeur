import argparse
import unittest
import sys
import os
import sqlite3

sys.path.insert(0, os.path.abspath('..'))

from part3.insertion import Insertion
from part3.insertion import connect_to_db

from part3.rapport import Rapport


class MyTestCase(unittest.TestCase):

    def check_if_word_in_db(self, con, word):
        args=[]
        rapport = Rapport(con, args)
        d = rapport.get_a_dict_with_db_data()
        if word in d:
            return True
        return False

    def check_if_args_char_is_true(self,args):
        if args.char:
            return True
        return False

    def test_connection_to_db(self):
        self.assertIsInstance(connect_to_db('insertion.sql'), sqlite3.Connection)

    def test_creation_of_a_cursor(self):
        self.assertIsInstance(connect_to_db('insertion.sql').cursor(), sqlite3.Cursor)

    def test_should_end_the_input(self):
        insert_test = Insertion(connect_to_db('insertion.sql'))
        string = "--fin"
        self.assertTrue(insert_test.is_end(string))

    def test_should_not_end_the_input(self):
        insert_test = Insertion(connect_to_db('insertion.sql'))
        string = "fin"
        self.assertFalse(insert_test.is_end(string))

    def test_word_should_be_in_db(self):
        con = sqlite3.connect(":memory:")
        cur = con.cursor()
        query = "CREATE TABLE partie3 (word text)"
        con.execute(query)
        insert_test = Insertion(con)
        insert_test.write_in_db("1")
        self.assertTrue(self.check_if_word_in_db(con, "1"))
        con.close()

    def test_word_should_not_be_in_db(self):
        con = sqlite3.connect(":memory:")
        cur = con.cursor()
        query = "CREATE TABLE partie3 (word text)"
        con.execute(query)
        insert_test = Insertion(con)
        insert_test.write_in_db("1")
        self.assertFalse(self.check_if_word_in_db(con, "2"))
        con.close()

    def test_get_a_dict_of_three_words(self):
        con = sqlite3.connect(":memory:")
        cur = con.cursor()
        query = "CREATE TABLE partie3 (word text)"
        con.execute(query)
        con.commit()
        cur.execute("INSERT INTO partie3 VALUES('1')")
        con.commit()
        cur.execute("INSERT INTO partie3 VALUES('2')")
        con.commit()
        cur.execute("INSERT INTO partie3 VALUES('3')")
        con.commit()

        args = []
        rapport = Rapport(con, args)
        dict_of_words = rapport.get_a_dict_with_db_data()
        self.assertEqual(len(dict_of_words), 3)
        con.close()

    def test_sort_a_dict_in_reverse_order(self):
        dict_of_words = {1: 1, 2: 2, 3: 3}
        sorted_dict = dict(reversed(sorted(dict_of_words.items(), key=lambda item: item[1])))
        first_value = list(sorted_dict.keys())[0]
        self.assertEqual(first_value,3)

    def test_args_should_detect_char_is_true(self):
        args = argparse.Namespace(char=True)
        self.assertTrue(self.check_if_args_char_is_true(args))

    def test_args_should_detect_char_is_false(self):
        args = argparse.Namespace(char=False)
        self.assertFalse(self.check_if_args_char_is_true(args))

    def test_char_should_be_chosen(self):
        args = argparse.Namespace(char=True)
        con = sqlite3.connect(":memory:")
        cur = con.cursor()
        query = "CREATE TABLE partie3 (word text)"
        con.execute(query)
        con.commit()
        cur.execute("INSERT INTO partie3 VALUES('test')")
        con.commit()
        cur.execute("INSERT INTO partie3 VALUES('maquillage')")
        con.commit()
        cur.execute("INSERT INTO partie3 VALUES('individuelle')")
        con.commit()
        rapport = Rapport(con, args)
        self.assertEqual(rapport.choose_between_words_and_chars(), rapport.get_a_dict_with_db_data_char())
        con.close()

    def test_word_should_be_chosen(self):
        args = argparse.Namespace(char=False)
        con = sqlite3.connect(":memory:")
        cur = con.cursor()
        query = "CREATE TABLE partie3 (word text)"
        con.execute(query)
        con.commit()
        cur.execute("INSERT INTO partie3 VALUES('test')")
        con.commit()
        cur.execute("INSERT INTO partie3 VALUES('maquillage')")
        con.commit()
        cur.execute("INSERT INTO partie3 VALUES('individuelle')")
        con.commit()
        rapport = Rapport(con, args)
        self.assertEqual(rapport.choose_between_words_and_chars(), rapport.get_a_dict_with_db_data())
        con.close()

if __name__ == '__main__':
    unittest.main()
