class Insertion:

    def __init__(self, file_name):
        self.file_name = file_name

    def is_end(self, string):
        if string == "--fin":
            return True
        else:
            return False

    def write_in_file(self, string):
        file = open(self.file_name, 'a')
        file.write(string + "\n")
        file.close()

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
                    self.write_in_file(word)


if __name__ == '__main__':
    insertion = Insertion("insertion.txt")
    insertion.run()
