from python_datastructs.Node import Node

'''
from a sorted list of unique ints, create a binary search tree of minimal height

Thoughts:
    the median is going to be the root
    do that recursively until you reach the base
'''

def buildBinTreeMinHeight(nums):
    # base case: return a small tree
    if len(nums) == 1:
        return Node(nums[0])
    if len(nums) == 2:
        print(nums)
        newNode = Node(nums[0])
        newNode.setRight(nums[1])
        return newNode
    if len(nums) == 3:
        newNode = Node(nums[1])
        newNode.setLeft(nums[0])
        newNode.setRight(nums[2])
        return newNode
    if len(nums) > 3:
        median = len(nums) // 2
        newNode = Node(nums[median])
        newNode.setLeftNode(buildBinTreeMinHeight(nums[:median]))
        newNode.setRightNode(buildBinTreeMinHeight(nums[median+1:]))
        return newNode

def main():
    nums = [1, 2, 5, 12, 58]
    n = buildBinTreeMinHeight(nums)
    n.printPreOrder()
    print("\n\n")
    n.printInOrder()
    print("\n\n")
    n.printPostOrder()

main()
