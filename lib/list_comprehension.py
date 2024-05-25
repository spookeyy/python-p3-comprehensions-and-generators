#!/usr/bin/env python3

def return_evens(num_list):
    #returns empty list when num_list has no evens - assert None == []
    for n in num_list:
        if n % 2 != 0:
            return []
        # returns evens from num_list - assert [] == [0, 2, 4, 6, 8]
        return [n for n in num_list if n % 2 == 0]
    return [n for n in num_list if n % 2 == 0]

def make_exclamation(sentence_list):
    #returns empty list when sentence_list is empty - assert [] == []
    if not sentence_list:
        return []
    # returns list of sentences with exclamation marks
    return [sentence + "!" for sentence in sentence_list]
