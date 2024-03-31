class TreeNode:  
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value): 
    if root is None:
        return TreeNode(value)  
    if value < root.value:
        root.left = insert(root.left, value)  
    else:
        root.right = insert(root.right, value) 
    return root

def range_search(root, low, high):  
    results = []  
    if root is not None:  
        if low <= root.value <= high: 
            results.append(root.value)  
        results.extend(range_search(root.left, low, high)) 
        results.extend(range_search(root.right, low, high))  
    return results

values = list(map(int, input("Enter values for the tree separated by spaces: ").split()))

root = None
for value in values:
    root = insert(root, value)

low = int(input("Enter the lower bound of the range: "))
high = int(input("Enter the upper bound of the range: "))

results = range_search(root, low, high)
print("Values in the range [{}, {}]: {}".format(low, high, results))

