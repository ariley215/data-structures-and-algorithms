from data_structures.hashtable import Hashtable


def first_repeated_word(string):
    hashtable = Hashtable()
    hashtable = {}
    input_string_list = string.lower().split(" ")
    for word in range(len(input_string_list)):
      if input_string_list[word] in hashtable:
        hashtable [input_string_list[word]] += 1
      else:
        hashtable [input_string_list[word]] = 1

    for word in range(len(input_string_list)):
      if hashtable[input_string_list[word]] > 1:
        return input_string_list[word]
    return "There are not repeating words in the string."


