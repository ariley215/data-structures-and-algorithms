# Challenge Title

Write a function that LEFT JOINs two hashmaps into a single data structure.

## Feature Tasks

Write a function called left join

- Arguments: two hash maps
  - The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
  - The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
Return: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic

## Whiteboard Process

![Whiteboard](python/docs/hashtable_left_join/WBCCLeftJoinHT.png)

## Approach & Efficiency

Similar to yesterdays challenge, add all the values from the first hash table to a seperate list. Then check the second hash table for matching keys. Add values of matching keys from second hash table to the return list or Null if the value doesn't exsit.

Big O

Time: O(n^2)

Space: O(n)

## Solution

python/code_challenges/hashtable_left_join.py
