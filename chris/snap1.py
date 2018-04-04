from copy import deepcopy
"""
given a List[List[]] -- (employeeID, managerID, employeeName)

data = [[1, 1, "bob"], [2, 1, "ben"], [3, 1, "john"]]

Jerry
|_Bob
  |_Chris
  |_Ben
  | |_Andy
  | |_Chris
  |   |_Marvin
  |   |_Marvin2
  |   | |_Marvin3
  |   |   |_Marvin3
  |   |   |_Marvin3
  |   |   |_Marvin3
  |   |   |_Marvin3
  |   |   |_Marvin3
  |   |   |_Marvin3
  |   |_Marvin
  |_John

Jerry
|_rong
|_bob
  |_marv
  |_chris
"""

class Person:
    def __init__(self, name, children):
        self.name = name
        self.children = children

    def __repr__(self):
        return self.name

def printOrg(ceo):
    stack = []
    print(ceo.name)
    for idx, child in enumerate(ceo.children):
        stack.append((child, [], idx == 0))
    while stack:
        curr_person, curr_dir_struct, parent_was_last = stack.pop()
        print((" ".join(curr_dir_struct) + " |_" + curr_person.name))
        for idx, child in enumerate(curr_person.children):
            stack.append((child, curr_dir_struct + [" " if parent_was_last else "|"], idx == 0))

ben = Person("ben", [])
chris = Person("chris", [ben])
marv = Person("marv", [])
bob = Person("bob", [chris, marv])
rong = Person("rong", [])
jerry = Person("Jerry", [rong, bob])
printOrg(jerry)
