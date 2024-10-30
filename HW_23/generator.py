import random
import string

def generator_of_unique_words(word_count: int):
    if not (1 <= word_count <= 10_000):
        raise ValueError("word_count must be between 1 and 10000")

    unique_words = set()
    word_lengths = range(3, 10)
    words = string.ascii_lowercase

    while len(unique_words) < word_count:
        words_batch = {
            ''.join(random.choices(words, k=random.choice(word_lengths)))
            for _ in range(word_count - len(unique_words))
        }
        unique_words.update(words_batch)

    return iter(unique_words)


for word in generator_of_unique_words(10_000):
    print(word)