class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs_surch(knot):
    if knot is None:
        return
    
    print(f"Ich bin bei Knoten: {knot.value}")
    
    dfs_surch(knot.left)
    
    dfs_surch(knot.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

dfs_surch(root)



