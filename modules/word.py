from random import choice

def possible_words() -> list:
    return open('storage/words.txt','r').read().splitlines()

def random_word() -> str:
    return choice(possible_words())

def real_word(word) -> bool:
    return ''.join(word) in possible_words()