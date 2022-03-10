import unittest
import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from part1.insertion import Insertion
from part1.rapport import Rapport


class MyTestCase(unittest.TestCase):
    def check_if_word_in_file(self, filename, word):
        file = open(filename, 'r')
        if word in file.read():
            file.close()
            return True
        file.close()
        return False

    def test_should_end_the_input(self):
        insert_test = Insertion("text.txt")
        string = "--fin"
        self.assertTrue(insert_test.is_end(string))

    def test_should_not_end_the_input(self):
        insert_test = Insertion("text.txt")
        string = "fin"
        self.assertFalse(insert_test.is_end(string))

    def test_word_should_be_in_file(self):
        insert_test = Insertion("text.txt")
        insert_test.write_in_file("phrase")
        self.assertTrue(self.check_if_word_in_file("text.txt", "phrase"))
        os.remove("text.txt")

    def test_word_should_not_be_in_file(self):
        insert_test = Insertion("text.txt")
        insert_test.write_in_file("phrase")
        self.assertFalse(self.check_if_word_in_file("text.txt", "3"))
        os.remove("text.txt")

    def test_get_a_dict_of_three_words(self):
        file = open("test.txt", "a")
        file.write("1" + '\n')
        file.write("2" + '\n')
        file.write("3" + '\n')
        file.close()
        rapport = Rapport("test.txt")
        dict_of_words = rapport.get_a_dict_with_file_data()
        self.assertEqual(len(dict_of_words), 3)
        os.remove("test.txt")

    def test_sort_a_dict_in_reverse_order(self):
        rapport = Rapport("test.txt")
        dict_of_words = {1: 1, 2: 2, 3: 3}
        sorted_dict = dict(reversed(sorted(dict_of_words.items(), key=lambda item: item[1])))
        first_value = list(sorted_dict.keys())[0]
        self.assertEqual(first_value, 3)


if __name__ == '__main__':
    unittest.main()
