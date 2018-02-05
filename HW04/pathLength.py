from bTree import bTree

print("Creating Binary Tree")
t = bTree(1)
# t.addList(random.sample(xrange(10), 10))
print("Adding elements to the tree")
t.addList([-1, -2, -3, 0, 2, 2, 2, 3])
print("Printing Tree")
t.printTree()
print("Internal Path Length:" + str(t.findPathLength()))
