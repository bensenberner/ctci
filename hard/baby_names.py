import copy
from typing import Dict, Tuple, List


class NameNode:
    def __init__(self, name: str, count: int = 0):
        self.name = name
        self.count = count
        self.synonyms: List[NameNode] = []

    def __repr__(self):
        return f"<{self.name}|{[synonym.name for synonym in self.synonyms]}>"


def baby_name_sums(names_to_counts: Dict[str, int], synonyms: List[Tuple[str, str]]):
    """
    :param names_to_counts: map of baby names to their counts
    :param synonyms: pairs of baby names that are synonyms
    :return: a dictionary mapping a baby name to the sum of its count along with the count of all of its synonyms.
        this babyname can be any of the synonyms.
    """
    name_to_node = {}
    for name1, name2 in synonyms:
        node1 = name_to_node.get(name1, NameNode(name=name1))
        node2 = name_to_node.get(name2, NameNode(name=name2))

        # they are symmetrical
        node1.synonyms.append(node2)
        node2.synonyms.append(node1)

        name_to_node[name1] = node1
        name_to_node[name2] = node2
    for name, count in names_to_counts.items():
        if name in name_to_node:
            name_to_node[name].count = count
        else:
            name_to_node[name] = NameNode(name=name, count=count)

    unvisited_names = {name for name in name_to_node.keys()}
    result = {}
    while unvisited_names:
        curr_name = unvisited_names.pop()
        curr_node = name_to_node.get(curr_name)
        stack = copy.deepcopy(curr_node.synonyms)
        count = curr_node.count
        while stack:
            traversal_node = stack.pop()
            unvisited_names.remove(traversal_node.name)
            count += traversal_node.count
            for synonym_node in traversal_node.synonyms:
                if synonym_node.name in unvisited_names:
                    stack.append(synonym_node)
        result[curr_name] = count
    return result
