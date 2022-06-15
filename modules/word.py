if __name__ == "__main__":
    error_message = "Start this program with the \"start.py\" file"
    print(f"\033[1;31m{error_message}\033[0m")
    exit()
else:
    from lib.lib import *

def possible_words() -> list:
    return open('storage/words.txt','r').read().splitlines()

def random_word() -> str:
    return choice(possible_words())

def real_word(word) -> bool:
    return ''.join(word) in possible_words()