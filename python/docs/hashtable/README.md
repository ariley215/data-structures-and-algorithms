
```python

def find_max_word(input_string):
  """
  Finds the word with the maximum frequency in a string.

  Args:
    input_string: A string of words.

  Returns:
    The word with the maximum frequency in the string, or None if no words exist.
  """

  # Create an empty hash table.
  hash_table = {}

  # Split input string into individual strings of words.
  words = input_string.lower().split()

  # Put the words in the hash table with their frequencies.
  for word in words:
    if word in hash_table:
      hash_table[word] += 1
    else:
      hash_table[word] = 1

  # Find the word with the maximum frequency.
  max_value = 0
  max_word = None

  for word, count in hash_table.items():
    if count > max_value:
      max_value = count
      max_word = word

  return max_word

```
