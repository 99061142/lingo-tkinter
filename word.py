from random import choice

def possible_words() -> list:
    return open('words.txt','r').read().splitlines()

def random_word() -> str:
    return choice(possible_words())

def real_word(word) -> bool:
    return word in possible_words()