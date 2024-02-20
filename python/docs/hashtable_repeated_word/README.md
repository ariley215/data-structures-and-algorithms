# Challenge Title

Find the first repeated word in a book.

## Whiteboard Process

![Whiteboard](/python/docs/hashtable_left_join/WBCC31HashtableRepeat.png)

## Approach & Efficiency

Seperate the words of the input string into a list of strings. Keep count of each string as its added to the hashtable. Find the first string that has a count > 1.

Big O

Space: O(n)

the hashtable could hold every string in the list. its as big as the string list that is being iterated over.

Time: O(n)

there are 2 loops each O(n) and hashtable look up is constant time.

## Solution

python code_challenges.hastable_repeated_word.py
