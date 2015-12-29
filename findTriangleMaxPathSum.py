def findMaxSum(root):
    if not root:
        return 0

    if root.maxVal:
        return root.maxVal
    
    # has two children
    if root.left and root.right:
        root.maxVal = root.val + max(findMaxSum(root.left), findMaxSum(root.right))
        return root.maxVal  
    
    # has zero children
    if not (root.left and root.right):
        root.maxVal = root.val
        return root.maxVal
    
    # has one child on the right
    if root.right:
        root.maxVal = root.val + findMaxSum(root.right)
        return root.maxVal
    # has one child on the left
    else:
        root.maxVal = root.val + findMaxSum(root.left)
        return root.maxVal