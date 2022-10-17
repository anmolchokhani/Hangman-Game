from all_words import words
import random


def random_word():
    word = random.choice(words)
    length_of_word= len(word)
    return word, length_of_word