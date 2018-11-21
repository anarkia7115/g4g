class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


def traverseInorder(root):
    if root is not None:
        traverseInorder(root.left)
        print(root.data, end=" ")
        traverseInorder(root.right)


# Your task is to complete this function
# Function should return root node
def insertinBST(root:Node, node:Node):
    # Code here
    l = root.left
    r = root.right
    val = node.data
    if val < root.data:
        if l is not None:
            insertinBST(l, node)
        else:
            root.left = node
    elif val > root.data:
        if r is not None:
            insertinBST(r, node)
        else:
            root.right = node
    else:
        pass
    return root


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        root = None
        for j in arr:
            if root is None:
                root = Node(j)
            else:
                insertinBST(root, Node(j))
        traverseInorder(root)
        print('')
# Contributed by: Harshit Sidhwa


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''
