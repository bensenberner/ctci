ALPHABET_SIZE = 26

class Node():
    def __init__(self):
        self.leaf = False
        self.nodes = {}

class Trie():
    def __init__(self):
        self.root = Node()

    def insert(self, *args):
        for word in args:
            root = self.root
            for char in word:
                if char not in root.nodes:
                    root.nodes[char] = Node()
                root = root.nodes[char]
            root.leaf = True

    def search(self, word):
        return self.search_recur(self.root, word)

    def search_recur(self, root, word):
        if word:
            index = word[0]
            if index != '*':
                if index in root.nodes:
                    return self.search_recur(root.nodes[index], word[1:])
                else:
                    return False
            else:
                for index in root.nodes:
                    if self.search_recur(root.nodes[index], word[1:]):
                        return True
                return False
        return root.leaf



t = Trie()
t.insert("woi", "nice", 'w')
print(t.search('w'))
