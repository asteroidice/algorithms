class Leaf:
    # This leaf node contains data, left and right.
    # Data: the thing that is stored on the leaf.
    # Left & Right: The pointers to the other leaves.
    data = None
    left = None
    right = None

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        left = ""
        r = ""
        if self.left:
            left = " L: " + str(self.left.data)
        if self.right:
            r = " R: " + str(self.right.data)
        return "Leaf: " + str(self.__str__()) + left + r


class bTree:
    # This is the binary tree class that has helper functions including
    # `findPathLength()` which returns the internal path length.
    head = None

    def __init__(self, data):
        self.head = Leaf(data)

    def add(self, data):
        # this function adds a leaf to the tree.
        # Data being put into the tree should be able to be compared using >=
        # If the new data is equal size to the leaf data it is treated as if
        # it was smaller.
        current_leaf = self.head
        while current_leaf:
            if current_leaf.data >= data:
                if current_leaf.left:
                    current_leaf = current_leaf.left
                else:
                    current_leaf.left = Leaf(data)
                    current_leaf = None
            else:
                if current_leaf.right:
                    current_leaf = current_leaf.right
                else:
                    current_leaf.right = Leaf(data)
                    current_leaf = None

    def addList(self, list):
        # this function can be used to add a list to the tree.
        for i in list:
            self.add(i)

    def findPathLength(self, leaf=None, pathLength=0):
        # Recursively finds the internal path length.

        # When the function gets called initially, it starts with the head leaf
        if not leaf:
            leaf = self.head

        # If the current node is the last parent, return the pathLength.
        if not leaf.right and not leaf.left:
            return pathLength

        # Count the current pathLength and then recursively repeat the process.
        left = pathLength + 1
        right = pathLength + 1
        if leaf.right:
            right = self.findPathLength(leaf.right, pathLength + 1)
        if leaf.left:
            left = self.findPathLength(leaf.left, pathLength + 1)
        return left + right

    # Found here: https://stackoverflow.com/a/34013268/9041594
    def printTree(self):
        current_level = [self.head]
        while current_level:
            print(' '.join(str(node) for node in current_level))
            next_level = list()
            for n in current_level:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
                current_level = next_level

# # Example usage.
# t = bTree(1)
# t.addList([-1,-2,-3,0,2,2,2,3])
# t.findPathLength()
