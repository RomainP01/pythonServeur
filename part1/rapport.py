class Rapport:

    def __init__(self, file_name):
        self.file_name = file_name

    def get_a_dict_with_file_data(self):
        file = open(self.file_name)
        dict_of_words = dict()
        for line in file:
            line = line.strip()
            words = line.split(" ")
            for word in words:
                if word in dict_of_words:
                    dict_of_words[word] = dict_of_words[word] + 1
                else:
                    dict_of_words[word] = 1
        file.close()
        return dict_of_words

    def sort_a_dict_in_reverse_order(self, dict_to_be_sorted):
        return dict(reversed(sorted(dict_to_be_sorted.items(), key=lambda item: item[1])))

    def print_key_and_value_from_a_dict(self, d):
        for key in list(d.keys()):
            print(str(key) + ":" + str(d[key]))

    def run(self):
        d = self.get_a_dict_with_file_data()
        sorted_d = self.sort_a_dict_in_reverse_order(d)
        self.print_key_and_value_from_a_dict(sorted_d)


if __name__ == '__main__':
    rapport = Rapport("insertion.txt")
    rapport.run()
