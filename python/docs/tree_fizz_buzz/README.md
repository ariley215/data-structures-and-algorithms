# Challenge Title

Conduct “FizzBuzz” on a k-ary tree while traversing through it to create a new tree.

Set the values of each of the new nodes depending on the corresponding node value in the source tree.

## Feature Tasks

Write a function called fizz buzz tree
- Arguments: k-ary tree
- Return: new k-ary tree

Determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:

- If the value is divisible by 3, replace the value with “Fizz”
- If the value is divisible by 5, replace the value with “Buzz”
- If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
- If the value is not divisible by 3 or 5, simply turn the number into a String.

## Whiteboard Process

![Whiteboard](/python/docs/tree_fizz_buzz/WBCCBTFizzBuzz.png)

## Approach & Efficiency

**Big O**

Space: O(n) the bigger the input tree the bigger the

Time: O(h) the time it takes is dependant on the height of the tree.

## Solution

python/data_structures/kary_tree.py

## Tests

pytest tests/code_challenges/test_tree_fizz_buzz.py
