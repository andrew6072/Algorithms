class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.key}"


def createNode(x):
    return Node(x)


def insertNode(root, x):  # O(log(N)) worst case O(N)
    if root == None:
        return createNode(x)
    if x < root.key:
        root.left = insertNode(root.left, x)
    elif x > root.key:
        root.right = insertNode(root.right, x)
    return root


def createTree(a):  # O(N*h) h=log(N) in best case
    root = None
    for x in a:
        root = insertNode(root, x)
    return root


def searchNode(root, x):  # O(h) worst case O(N)
    if root == None or root.key == x:
        return root
    if x > root.key:
        return searchNode(root.right, x)
    return searchNode(root.left, x)


"""
Delete a value in the BST
Case 1: Delete a leaf node in the tree.

Case 2: Delete a node with one or two child nodes. Replace the value of this node
with value of suitable child node (max value node of left subtree of min value node
of right subtree) and then delete that suitable child node.

Case 3: Delete the root node (or node with multiple child nodes - subtree). Find
value of suitable child node, replace that value with this root's node then delete
the found suitable node.
"""


def deleteNode(root, x):
    if root == None:
        return root

    # Traverse left to find the value to delete
    if x < root.key:
        root.left = deleteNode(root.left, x)

    # Traverse right to find the value to delete
    elif x > root.key:
        root.right = deleteNode(root.right, x)

    # When x == root.key
    else:
        """
        When node doesn't have left child, we connect the parent node to the right child of this node 
        (in other word, we skip this node), then delete this node
        """
        if root.left == None:
            temp = root.right
            del root
            return temp

        # Same logic with the case when node doesn't have right child
        elif root.right == None:
            temp = root.left
            del root
            return temp


        temp = minValueNode(root.right)

        root.key = temp.key

        root.right = deleteNode(root.right, temp.key)

    return root


def minValueNode(root):
    if root.left == None:
        return root
    return minValueNode(root.left)


def traversalTree(root):  # O(N)
    if root != None:
        traversalTree(root.left)
        val = root.key
        print(val, end=" ")
        traversalTree(root.right)


def rotateLeft(root, pivot):  # O(1)
    root.right = minValueNode(root.right)
    pivot.left = root
    root = pivot
    return root


def maxValueNode(root):  # O(h) worst case O(N)
    if root.right == None:
        return root
    return maxValueNode(root.right)


def rotateRight(root, pivot):  # O(1)
    root.left = maxValueNode(pivot)
    pivot.right = root
    root = pivot
    return root


a = [5, 3, 7, 2, 4]
root = createTree(a)
traversalTree(root)

print()

print(root.left, root.right)
root = rotateRight(root, root.left)
print(root.right.left, root.right.right)
