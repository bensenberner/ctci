class Node:
    def __init__(self, val, level):
        self.val = val
        self.nodes = []
        self.count = 1
        self.level = level


def add_call(root, components):
    if not (root and components): return
    curr = components[0]
    node_present = False
    for node in root.nodes:
        if node.val == curr:
            node.count += 1
            add_call(node, components[1:])
            node_present = True
            break
    if not node_present:
        new_node = Node(curr, root.level + 1)
        add_call(new_node, components[1:])
        root.nodes.insert(0, new_node)


def countAPI(calls):
    root = Node(None, 0)
    for call in calls:
        components = call[1:].split("/")
        add_call(root, components)
    queue = [root]
    responses = []
    while queue:
        curr = queue.pop()
        responses.append(curr)
        for newNode in curr.nodes:
            queue.append(newNode)
    responses = responses[1:]
    return ["{}{} ({})".format(2*node.level*"-", node.val, node.count) for node in responses]

calls = [
        "/project1/subproject1/method1",
        "/project2/subproject1/method1",
        "/project1/subproject1/method1",
        "/project1/subproject2/method1",
        "/project1/subproject1/method2",
        "/project1/subproject2/method1",
        "/project2/subproject1/method1",
        "/project1/subproject2/method1"
]

print(countAPI(calls))