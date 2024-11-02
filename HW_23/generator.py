import random
import nltk
from nltk.corpus import words


def generator_of_unique_words(word_count: int):
    if not (1 <= word_count <= 10_000):
        raise ValueError("word_count must be between 1 and 10000")

    english_words = {word.lower() for word in words.words() if 3 <= len(word) <= 10}

    english_words = list(english_words)

    if word_count > len(english_words):
        raise ValueError("word_count must be between 1 and 10000")

    unique_words = random.sample(english_words, word_count)

    for word in unique_words:
        yield word

for word in generator_of_unique_words(10_000):
    print(word)