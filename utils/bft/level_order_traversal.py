class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Tree:
    def createNode(self, data):
        return Node(data)

    def traverse(self, root):
        if root is not None:
            self.traverse(root.left)
            print(root.data, end=' ')
            self.traverse(root.right)



''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

"""
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
"""
# Your task is to complete this function
# Function should print the level order of the tree in required format
# only input to function is the root of the tree


def traverse_level_order(root):
    # Code here
    curr_level_queue = [root]
    next_level_queue = []
    while len(curr_level_queue) > 0:
        for n in curr_level_queue:
            if n.left is not None:
                next_level_queue.append(n.left)
            if n.right is not None:
                next_level_queue.append(n.right)
            print(n.data, end=" ")
        curr_level_queue = next_level_queue[:]
        next_level_queue.clear()


# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        tree = Tree()
        lis = {}
        root = None
        root = tree.createNode(int(arr[0]))
        lis[root.data] = root
        k = 0
        for j in range(n):
            if int(arr[k]) in lis:
                ptr = tree.createNode(int(arr[k + 1]))
                if arr[k + 2] == 'L':
                    lis[int(arr[k])].left = ptr
                else:
                    lis[int(arr[k])].right = ptr
                lis[int(arr[k + 1])] = ptr
                k += 3
        traverse_level_order(root)
        print()
# Contributed by: Harshit Sidhwa