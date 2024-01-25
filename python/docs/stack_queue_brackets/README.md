# Challenge Title

Multi-bracket Validation

## Whiteboard Process

![WhiteBoard](/python/docs/stack_queue_brackets/WBCodeChallenge13.png)

## Approach & Efficiency

Big O is O(n) for time and space complexity

iterates through each character in the input string once, and the operations within the loop are constant time.

- Iterating through each character in the input string: O(n)
- Stack operations (append and pop): O(1) each (constant time)

Stack size could grow to be proportional to the length of the input string.

## Solution

Solution Code: python/code_challenges/stack_queue_brackets.py

Test Solution Code:
pytest tests/code_challenges/test_stack_queue_brackets.py
