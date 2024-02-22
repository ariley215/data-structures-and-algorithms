from data_structures.hashtable import Hashtable


def left_join(ht1, ht2):
    output = []
    for key, value in ht1.words():
        synonym_pair = [key, value]
        synonym_pair.append(ht2.get(key, None))
        output.append(synonym_pair)
    return output


