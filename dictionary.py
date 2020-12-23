import nltk
nltk.download('words')
from nltk.corpus import words
from utils import print_info, print_debug


WORD_LIST = [word.lower() for word in words.words()]

LETTER_PROBABILITIES = {}

def find_letter_probabilities(words):
    total_letters = 0

    global LETTER_PROBABILITIES

    # Count how many times each letter appears
    for word in words:
        for letter in word:
            if letter in LETTER_PROBABILITIES:
                LETTER_PROBABILITIES[letter] += 1
            else:
                LETTER_PROBABILITIES[letter] = 1

            total_letters += 1

    # Normalize
    LETTER_PROBABILITIES = {k: v / total_letters for k, v in LETTER_PROBABILITIES.items()}

    print_info("sort_words_by_probability: finished sorting through {} letters".format(total_letters))


def find_word_probability_score(word):
    # Assumes find_letter_probabilities() has already been called.
    # Kind of a shitty heuristic for how workable a word is.
    score = 0.

    for letter in word:
        score += LETTER_PROBABILITIES[letter]

    return score


def sort_words_by_probability(words):
    return

def sort_words_by_length(words):
    return


# Tests
find_letter_probabilities(WORD_LIST)
print_debug(LETTER_PROBABILITIES)
print_debug("total probability: {}".format(sum([prob for prob in LETTER_PROBABILITIES.values()])))

print_debug("probablity score of penis is: {}".format(find_word_probability_score("penis")))
