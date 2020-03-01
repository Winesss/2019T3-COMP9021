# COMP9021 19T3 - Rachid Hamadi
# Quiz 4 *** Due Thursday Week 5
#
# Prompts the user for an arity (a natural number) n and a word.
# Call symbol a word consisting of nothing but alphabetic characters
# and underscores.
# Checks that the word is valid, in that it satisfies the following
# inductive definition:
# - a symbol, with spaces allowed at both ends, is a valid word;
# - a word of the form s(w_1,...,w_n) with s denoting a symbol and
#   w_1, ..., w_n denoting valid words, with spaces allowed at both ends
#   and around parentheses and commas, is a valid word.


import sys,re


def regularexpression(input_word):
    input_word=input_word.strip()
    if input_word =='':
        return False
    if re.match("^[a-zA-Z\_]*$",input_word) == None:
        return False
    return True

def is_valid(word, arity):

    str(word)
    express = []
    n=0
    if arity == 0:
        if regularexpression(word):
            return True
        else:
            return False
    if arity > 0:
        if ')' in word and '(' not in word:
            return False
        if '(' in word and ')' not in word:
            return False
        if '(' and ')' not in word:
            return False
        while word.find('(') and word.find(')') > 0:
            if ')' in word and '(' not in word:
                return False
            if '(' in word and ')' not in word:
                return False
            if '(' and ')' not in word:
                return False
            r_word = list(reversed(word))
            right_para = word.index(')')
            left_para = r_word[len(word) - right_para:-1].index('(')
            left_para = right_para - left_para - 1
            express = word[left_para + 1:right_para].split(',')
            for n in express:
                if regularexpression(n)==False:
                    return False
                if n=='':
                    return False
            if len(express) != arity:
                    return False
            word = word[:left_para] + word[right_para + 1:]
        if regularexpression(word):
            return True
        else:
            return False

try:
    arity = int(input('Input an arity : '))
    if arity < 0:
        raise ValueError
except ValueError:
    print('Incorrect arity, giving up...')
    sys.exit()
word = input('Input a word: ')
if is_valid(word, arity):
    print('The word is valid.')
else:
    print('The word is invalid.')

