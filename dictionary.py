"""
    A dictionary containing all english words.
    You can query the dictionary for words given a length and character constraint.
    Words are sorted by how often their letters apear in all other words.
"""

import nltk
nltk.download('words')
from nltk.corpus import words
from utils import print_info, print_debug

class Smart_Dictionary:

    def __init__(self):
        print_info("Smart_Dictionary Init Starting")

        self.WORD_LIST = [word.lower() for word in words.words()]
        self.LETTER_PROBABILITIES = {}
        self.SORTED_WORD_LIST = []

        self.__find_letter_probabilities(self.WORD_LIST)

        self.__sort_words_by_probability()

        self.__sort_words_by_length()

        print_info("Smart_Dictionary Init Finished")

# Public
    def test(self):
        self.__find_letter_probabilities(self.WORD_LIST)
        print_debug(self.LETTER_PROBABILITIES)
        print_debug("total probability: {}".format(sum([prob for prob in self.LETTER_PROBABILITIES.values()])))

        print_debug("probablity score of penis is: {}".format(self.__find_word_probability_score("penis")))

    def pop_constrained_word(self, length, constraint):
        # Find a word of given length and that matches the constraing
        # If nothing is found then return None.
        # If found then remove this word from the list.

        retval = None

        if length > len(self.SORTED_WORD_LIST):
            print_info("ERROR: there are no words of length {}".format(length))

        if length != len(constraint):
            print_info("ERROR: length and constraint length do not match: {} {}".format(length, len(constraint)))

        for word in self.SORTED_WORD_LIST[length]:
            for idx, letter in enumerate(word):
                if (constraint[idx] is not "*") and (constraint[idx] is not letter):
                    break
            else:
                retval = word
                self.SORTED_WORD_LIST[length].remove(word)
                break

        return retval


# Private
    def __find_letter_probabilities(self, words):
        total_letters = 0

        # Count how many times each letter appears
        for word in words:
            for letter in word:
                if letter in self.LETTER_PROBABILITIES:
                    self.LETTER_PROBABILITIES[letter] += 1
                else:
                    self.LETTER_PROBABILITIES[letter] = 1

                total_letters += 1

        # Normalize
        self.LETTER_PROBABILITIES = {k: v / total_letters for k, v in self.LETTER_PROBABILITIES.items()}

        print_info("sort_words_by_probability: finished sorting through {} letters".format(total_letters))


    def __find_word_probability_score(self, word):
        # Assumes find_letter_probabilities() has already been called.
        # Kind of a shitty heuristic for how workable a word is.
        score = 0.

        for letter in word:
            score += self.LETTER_PROBABILITIES[letter]

        return score


    def __sort_words_by_probability(self):
        # Assumes __find_letter_probabilities() has already been called.
        self.WORD_LIST = sorted(self.WORD_LIST, key=(lambda x : -1 * self.__find_word_probability_score(x)))

    def __sort_words_by_length(self):
        self.WORD_LIST = sorted(self.WORD_LIST, key=(lambda x : len(x)))

        max_len = len(self.WORD_LIST[-1])

        self.SORTED_WORD_LIST = [[] for _ in range(max_len + 1)]

        idx = 0

        while idx < len(self.WORD_LIST):
            word = self.WORD_LIST[idx]
            self.SORTED_WORD_LIST[len(word)].append(word)

            idx += 1

        # [print("\n\nlen {}\n\n".format(i), words[:10]) for i, words in enumerate(self.SORTED_WORD_LIST)]
        # print(self.SORTED_WORD_LIST[22])



# Tests
if __name__ == "__main__":
    dictionary = Smart_Dictionary()
    dictionary.test()

    constraint = "c****e"
    print_debug("\nPopping a constrained word {}".format(dictionary.pop_constrained_word(6, constraint)))
