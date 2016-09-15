import random
# might want to import weakrefs later on

class probDS(object):
    '''Supports two methods:
    set() will set the weight of an object in the
    data structure (or instantiate the weight if the object does not yet exist
    in the data structure.
    get() will then return a random object from the data structure. The probability
    of returning an object = weight of the obj divided by weight of all objects
    '''
    weights = {}
    ids = {}
    size = 0
    def set(self, weight, obj):
        if weight > 0:
            if id(obj) in self.weights:
                self.size -= self.weights[id(obj)]
            self.weights[id(obj)] = weight
            self.ids[id(obj)] = obj
            self.size += weight
        else:
            if id(obj) in self.weights:
                self.size -= self.weights[id(obj)]
                del self.weights[id(obj)]
                del self.ids[id(obj)]

    def get(self):
        random.seed()
        r = random.randint(0, self.size-1)
        for objID in self.weights:
            r -= self.weights[objID]
            if r < 0:
                return self.ids[objID]

prob = probDS()
a = {'tokyo': "japan"}
b = "america"
c = "spain"
prob.set(6, a)
prob.set(3, b)
for i in range(20):
    print(prob.get())
prob.set(0, b)
prob.set(8, c)
print('\n\nboink\n\n')
for i in range(20):
    print(prob.get())

