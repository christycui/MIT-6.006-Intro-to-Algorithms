## 1. The Role of Algorithms in Computing
### 1.1 Algorithms

- well-defined computational procedure
- an **instance of a problem** consists of the input needed to compute a solution to the problem
- an algorithm is said to be **correct** if it halts with the correct output for every input instance
- Characters of problems solved by algorithm
    + many candidate solutions -> find "best" one
    + practical applications

### 1.2 Algorithms as a technology

## 2. Getting Started
### 2.1 Insertion sort
- insertion sort is an efficient algo for sorting a small number of elements
- Loop invariants and the correctness of insertion sort:
    + Initialization: it is true prior to the first iteration of the loop
    + Maintenance: if it is true before an iteration of the loop, it remains true before the next iteration
    + Termination: when the loop terminates, the invariant gives us a useful property that helps show that the algo is correct

## 2.2 Analyzing algorithms
- the best notion for **input size** depends on the problem being studied. e.g. number of items in the input or total number of bits needed or even two numbers for a graph
- **running time** is the number of primitive operations or steps executed
- usually **worst-case** running time; in some particular cases, we shall be interested in the **average-case** running time. Often, we shall assume that all inputs of a given size are equally likely, when violated we can use **randomized algorithm**, to allow **probabilistic analysis** and yield an **expected** return
- it is **the rate of growth** or **order of growth** that interests us

## 2.3 Designing algorithms
- insertion sort is incremental approach: \Theta(n^2)
- merge sort is divide-and-conquer approach: \Theta(nlgn)

## 3. Growth of Functions
**asymptotic** efficiency of algorithms: we are concerned with how the running time of an algorithm increases with the size of the input *in the limit*, as the size of the input increases without bound

### 3.1 Asymptotic notation
- \theta-notation: upper-bound and lower-bound. 0 <= c1g(n) <= f(n) <= c2g(n)
    + g(n) is **asymptotically tight bound** for f(n)
    + the definition requires that every member of f(n) be **asymptotically nonnegative**
    + the important thing is *some* choices exist for c1 and c2
- O-notation
    + when we have only an **asymptotic upper bound: 0 <= f(n) <= cg(n)
    + note that f(n) = \theta(g(n)) implies that f(n) = O(g(n))
- \omega-notation
    + **asymptotically lower bound**: 0 <= cg(n) <= f(n)
    + f(n) = \theta(g(n)) implies that f(n) = O(g(n)) and f(n) = \omega(g(n))
- asymptotic notation in equations and inequalities
    + there is *some* function f(n) E \Theta(n) such that 2n^2 + 3n + 1 = 2n^2 + f(n)
    + for *any* function g(n) E \Theta(n), there is *some* function h(n) E \Theta(n^2) such that 2n^2 + g(n) = h(n)
- o-notation: an upper bound that is not asymptotically tight
- w-notation: an lower bound that is not asymptotically tight
- Comparing functions
    + Transitivity
    + Reflexivity
    + Symmetry: f(n) = \Theta(g(n)) if and only if g(n) = \Theta(f(n))
    + Transpose symmetry

### 3.2 Standard notations and common functions
- Exponentials: any exponential function with a base strictly greater than 1 grows faster than any polynomial function
- Logarithms: any positive polynomial function grows faster than any polylogarithmic function
    + a = b^(log^b a)
    + We say that a function f(n) is polylogarithmically bounded if f(n) = O(lg^k n) for some constant k.
    + lg^b n = o(n^a) for any constant a > 0. 
- Factorial
    + n! = o(n^n)
    + n! = w(2^n)
    + lg(n!) = \Theta(n lgn)
- functional iteration and the iterated log function
- Fibonacci numbers grow exponentially

## 4. Divide and Conquer
### 4.3 The substitution method for solving recurrences
### 4.4 The recursion-tree method for solving recurrences
### 4.5 The master method for solving recurrences

## 6. Heap Sort
### 6.1 Heaps
- heap property: for every node other than the the root, A[Parent(i) >= A[i]]
- max_heapify: O(lgn)
- build_max_heap: O(n), produces a max-heap from an unordered input array
- heapsort: O(nlgn)
- max_heap_insert, heap_extract_max, heap_increase_key and heap_maximum: O(lgn)

### 6.2 Maintaining the heap property

## 10. Elementary Data Structures
### 10.4 Representing rooted trees
- binary trees: p, left, right
- rooted trees with unbounded branching: left-child, right-sibling
- other tree representations

## 12. Binary Search Trees
### 12.1 What is a binary search tree?
- **binary-search-tree property**: Let x be a node in the binary search tree. If y is a node in the left subtree of x, then y.key <= x.key. If y is a node in the right subtree of x, then y.key >= x.key
- **inorder tree walk**: it prints the key of the root of a subtree between printing the values in its left subtree and printing those in its right subtree
- **preorder tree walk**: prints the root before the values in either subtree
- **postorder tree walk**: prints the root after the values in its subtrees
- it takes \Theta(n) time to walk an n-node binary search tree

### 12.2 Querying a binary search tree
- searching takes O(h) time where h is the height of the BTS tree
- minimum and maximum: O(h)
- successor and predecessor: O(h)
- insertion and deletion: insertion - O(h); deletion - O(h) with 3 cases
