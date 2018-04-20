class nameCount:
    def __init__(self, name):
        self.count = 0
        self.visited = False
        self.name = name


names = {
    "john": 15,
    "jon": 12,
    "chris": 13,
    "kris": 4,
    "christopher": 19
}

synonyms = [
    ("jon", "john"),
    ("john", "johnny"),
    ("chris", "kris"),
    ("chris", "christopher")
]

def babyNames(names, synonyms):
    d = dict()
    for name1, name2 in synonyms:
        if name1 not in d and name2 not in d:
            newCount = nameCount(name1)
            d[name1] = d[name2] = newCount
        elif name1 not in d:
            d[name1] = d[name2]
        elif name2 not in d:
            d[name2] = d[name1]

    for name in names:
        currCount = d[name]
        currCount.count += names[name]

    for counter in d.values():
        if counter.visited: continue
        print("{}:{}".format(counter.name, counter.count))
        counter.visited = True
    print(len(d.values()))

babyNames(names, synonyms)
