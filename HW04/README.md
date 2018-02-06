# HW 04 Problem 5.3.10
## Prompt
> Write a program for computing the internal path length of an extended binary tree. Use it to investigate empirically the average number of key comparisons for searching in a randomly generated binary search tree.

## Run the program
I've created an example program you can run using the following command.
```
python pathLengthExample.py
```

### Code Run-through
1. **Creating the binary tree:** This is accomplished by importing and instantiating custom built `bTree()` class from the `bTree.py` file.
```
t = bTree()
```

2. **Adding elements to the tree:** You can do this one of two ways. 1) using the `add()` method or 2) using the `addList()` method which iteratively calls the `add` method. **Note:** Child nodes are represented as `None` in the leaves and are not shown below.
```
t.addList([[-1, -2, -3, 0, 2, 2, 2, 3])
```
This will render a tree that looks like...
```
1
-1 2
-2 0 2 3
-3 2
```
or if you align everything properly...
```
            1
        -1        2
    -2    0     2   3
-3            2
```
3. **Finding the Path Length:** The `findPathLength()` method calculates the internal path length of the tree. It starts with the tree head and recursively calls itself while keeping track of the current path length. In this specific case the path length is found to be `16`. This is the sum of the lengths from the root node to every parent node.
4. **Find the number of nodes:** I built the `count()` method which returns the number of nodes. This is important when calculating the average number of paths per node. Ex `9`
5. **Calculate the average number of key comparisons:** Use these two pieces of information to calculate the "average number of key comparisons for searching in a randomly generated binary search tree." You do this according to the following formula. `(Path length)/(# of nodes)` The result for this specific example is `1.7778`.


### RNG Version
If you'd like to look at some larger random cases, you can run the `pathLengthRandom.py` file to check it out.
```
python pathLengthRandom.py
```
