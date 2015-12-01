END = '_end_'
ALPHABET_SIZE = 26

class Node():
    def __init__(self):
        self.leaf = False
        self.nodes = [None] * ALPHABET_SIZE

class Trie():
    def __init__(self):
        self.root = Node()

    def insert(self, *args):
        for word in args:
            root = self.root
            for i in range(len(word)):
                index = ord(word[i]) - ord('a')
                if not root.nodes[index]:
                    root.nodes[index] = Node()
                root = root.nodes[index]
            root.leaf = True

    def search(self, word):
        return self.search_recur(self.root, word)

    def search_recur(self, root, word):
        if word:
            if word[0] != '*':
                index = ord(word[0]) - ord('a')
                if not root.nodes[index]:
                    return False
                else:
                    return self.search_recur(root.nodes[index], word[1:])
            else:
                for node in root.nodes:
                    if node:
                        if self.search_recur(node, word[1:]):
                            return True
                return False
        return root.leaf



t = Trie()
t.insert("wow", "nice", 'woa')
print(t.search('w*aw'))
