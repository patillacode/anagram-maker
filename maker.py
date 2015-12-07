#!/usr/bin/env python
"""maker.py: Makes anagrams from given words."""

import itertools
import unicodedata

word_list = 'palabras.txt'


def get_word():
    # Word from user via terminal
    input_word = str(raw_input('Enter your word/phrase: '))
    # ASCII encode and set in lower case
    input_word = flat_word(input_word)
    return input_word


def flat_word(word):
    # unicode normalize
    word = unicodedata.normalize('NFKD', word.decode('utf-8'))
    # encode it as ASCII
    word = word.encode('ASCII', 'ignore')
    # remove line jumps and set as lower case
    word = word.lower().replace('\n', '')
    return word


def create_permutations(word):
    permutations = list()
    all_permutations = itertools.permutations(word)
    # Create all (no repeat) permutations
    for p in list(all_permutations):
        new_perm = "".join(p)
        if new_perm not in permutations:
            permutations.append(new_perm)
    return permutations


def create_combinations(word):
    combinations = list()
    # Create all (no repeat) combinations
    for i in range(len(word)):
        for c in itertools.combinations(word, i + 1):
            new_comb = ''.join(c)
            if new_comb not in combinations:
                combinations.append(new_comb)
    return combinations


def match_real_words(word, word_list):
    permutations = []
    matched_words = []
    # Get all combinations of given word (from 2 chars onwards)
    combinations = create_combinations(word)
    for c in combinations:
        # Create the permutations for each combination
        perms = create_permutations(c)
        # Store each permutation that combination generated
        for p in perms:
            if p not in permutations:
                permutations.append(p)
    # open dictionary file
    words = open(word_list)
    # match all combinations with real words
    for w in words:
        w = flat_word(w)
        if w in permutations:
            matched_words.append(w)
    # close dictionary file
    words.close()
    return matched_words


if __name__ == '__main__':
    for w in sorted(match_real_words(get_word(), word_list)):
        print w
