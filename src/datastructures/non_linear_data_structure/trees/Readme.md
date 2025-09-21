# DSA Trees

## Overview

The Tree data structure is similar to Linked Lists in that each node contains data and can be linked to other nodes. However, unlike linear data structures (Arrays, Linked Lists, Stacks, and Queues), trees are non-linear. In a Tree, a single element can have multiple 'next' elements, allowing the data structure to branch out in various directions.

The data structure is called a "tree" because it looks like a tree, only upside down.

```
         Root
        /    \
       A      B
      / \    / \
     C   D  E   F
```

## Use Cases

Trees are useful in many scenarios:

- **Hierarchical Data**: File systems, organizational models, etc.
- **Databases**: Used for quick data retrieval
- **Routing Tables**: Used for routing data in network algorithms
- **Sorting/Searching**: Used for sorting data and searching for data
- **Priority Queues**: Priority queue data structures are commonly implemented using trees, such as binary heaps

## Tree Terminology and Rules

### Key Terms:

- **Root Node**: The first node in a tree
- **Edge**: A link connecting one node to another
- **Parent Node**: A node that has links to its child nodes (also called internal node)
- **Child Node**: Nodes linked from a parent node
- **Leaf Nodes**: Nodes without links to other child nodes (also called leaves)
- **Tree Height**: The maximum number of edges from the root node to a leaf node
- **Node Height**: The maximum number of edges between a specific node and a leaf node
- **Tree Size**: The total number of nodes in the tree

### Rules:

- A node can have zero, one, or many child nodes
- A node can only have one parent node
- The root node has no parent

## Types of Trees

### 1. Binary Trees
Each node has up to two children: the left child node and the right child node. This structure is the foundation for more complex tree types.

```
      1
     / \
    2   3
   / \
  4   5
```

### 2. Binary Search Trees (BSTs)
A type of Binary Tree where for each node:
- The left child node has a lower value
- The right child node has a higher value

```
      8
     / \
    3   10
   / \    \
  1   6    14
     / \   /
    4   7 13
```

### 3. AVL Trees
A type of Binary Search Tree that self-balances so that for every node, the difference in height between the left and right subtrees is at most one. This balance is maintained through rotations when nodes are inserted or deleted.

## Tree Properties

- **Height**: Maximum number of edges from root to any leaf
- **Depth**: Number of edges from root to a specific node
- **Level**: All nodes at the same depth are at the same level
- **Degree**: Number of children a node has

## Implementation Considerations

Trees can be implemented using:
- **Linked representation**: Using pointers/references
- **Array representation**: Using indices to represent parent-child relationships

Each implementation has its own advantages depending on the specific use case and operations required.