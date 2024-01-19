# Challenge Title

Zip two linked lists.

## Feature Tasks

- Write a function called zip lists
- Arguments: 2 linked lists
- Return: New Linked List, zipped as noted below
- Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the the zipped list.
- Try and keep additional space down to O(1)
- You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Whiteboard Process

![whiteboard](docs/linked_list_zip/whiteboardCodeChallenge8.png)

## Approach & Efficiency

Big O

Time: O(n) the longer the lists the more time to change the values to become one zipped list

Space: O(1) only the values of the nodes are changed. The lists use the same space when they are zipped as when they are seperate.

## Solution

python code_challenges.linked_list.py
