ALPHABET_SIZE = 26

class Node():
    def __init__(self):
        self.isLeaf = False
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
            root.isLeaf = True

    def insertList(self, words):
        for word in words:
            root = self.root
            for char in word:
                if char not in root.nodes:
                    root.nodes[char] = Node()
                root = root.nodes[char]
            root.isLeaf = True

    def validPrefix(self, word):
        currNode = self.root
        for char in word:
            if char not in currNode.nodes:
                return False
            currNode = currNode.nodes[char]
        return True

    def contains(self, word):
        return self.search_recur(self.root, word)

    def partialMatch(self, word):
        return self.partialRecur(self.root, word)

    def partialRecur(self, node, word):
        if node.isLeaf:
            return True
        if word:
            for index in node.nodes:
                if self.partialRecur(node.nodes[index], word[1:]):
                    return True
        return node.isLeaf

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
        return root.isLeaf

if __name__ == '__main__':
    t = Trie()
    t.insert("woi", "nice", 'w')
    print(t.contains('w*'))
    print(t.validPrefix('w'))
