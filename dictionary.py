import scapegoat as sc
class Dictionary:
    def __init__(self):
        self.word_dict = dict()
        self.tree_keys = sc.Scapegoat_tree(0.6)

    def lookup(self, word):
        found_word = self.tree_keys.search(self.tree_keys.root, word)
        if found_word:
            print(f"{word.upper()} is in the dictionary. It is defined as{self.word_dict[word]}.")
        else:
            print(f"{word} not found")

    def insert(self, text):
        key = text[0]
        found = self.tree_keys.search(self.tree_keys.root, key)
        if found:
            return False
        self.tree_keys.insert(key, self.tree_keys.root)
        self.word_dict[key] = text[1]
        return True

    def dict_size(self):
        size = self.tree_keys.ret_size()
        return size

    def create_dictionary(self, file):
        try:
            f = open(file, 'r')
        except FileNotFoundError as e:
            print("File not found")
            return False
        for word in f:
            text = word.strip().split(":")
            self.tree_keys.insert_util(text[0])
            self.word_dict[text[0]] = text[1]
        return True

    def print_words(self):
        for word in self.word_dict:
            print(word)

    def print_inorder(self):
        self.tree_keys.inorder(self.tree_keys.root)

if __name__ == '__main__':
    my_dictionary = Dictionary()
    my_dictionary.create_dictionary("words.txt")
    while(True):
        print("\nDictionary Menu:\n1. Insert a Word\n2. Print words\n3. Print words inorder\n4. Search word\n5. Print Size of Dictionary\n6. Exit\n")
        print("Enter your choice: ")
        choice = int(input())
        if choice == 1:
            print("Enter a word to insert: ")
            text_input = input().strip().split(":")
            my_dictionary.insert(text_input)
        elif choice == 2:
            my_dictionary.print_words()
        elif choice == 3:
            my_dictionary.print_inorder()
        elif choice == 4:
            print("Enter a string to search: ")
            word = input().strip()
            my_dictionary.lookup(word)
        elif choice == 5:
            print("Size =", my_dictionary.dict_size())
        elif choice == 6:
            break
