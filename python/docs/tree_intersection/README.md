# Challenge Title

Find common values in 2 binary trees.

## Whiteboard Process


## Approach & Efficiency

Approach was similar to yesterday's code challenge. traverse one tree and add each value as a key and a counter as it value, to a hash table. Then traverse the second tree and check if the values exisit in the hashtable. then return any that do.

## Solution

python/code_challenges/tree_intersection.py

Tests

pytest tests/code_challenges/test_tree_intersection.py
