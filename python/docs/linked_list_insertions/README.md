# Challenge Title

Extend a Linked List to allow various insertion methods.

## Feature Tasks

Write the following methods for the Linked List class:

- append
  - arguments: new value

adds a new node with the given value to the end of the list

- insert before
  - arguments: value, new value

adds a new node with the given new value
immediately before the first node that has the value specified

- insert after
  - arguments: value, new value

adds a new node with the given new value immediately after the first node that has the value specified

## Whiteboard Process

![Whiteboard](/python/docs/linked_list_insertions/WBCodeChallenge6LinkedListInsert.png)

## Approach & Efficiency

Big O

Time: O(n) - the longer the list the more time to go through the whole list

Space: O(1) - only creates a new node in each function

## Solution

python/data_structures/linked_list.py
