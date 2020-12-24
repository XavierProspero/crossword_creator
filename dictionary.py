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

        print_debug(self.WORD_LIST[:10])
        self.__sort_words_by_probability()
        print_debug(self.WORD_LIST[:10])

        self.__sort_words_by_length()

        print_info("Smart_Dictionary Init Finished")

# Public
    def test(self):
        self.__find_letter_probabilities(self.WORD_LIST)
        print_debug(self.LETTER_PROBABILITIES)
        print_debug("total probability: {}".format(sum([prob for prob in self.LETTER_PROBABILITIES.values()])))

        print_debug("probablity score of penis is: {}".format(self.__find_word_probability_score("penis")))



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

        self.SORTED_WORD_LIST = [[]] * (max_len + 1)

        idx = 0
        word_len = 1

        while idx < len(self.WORD_LIST):
            word = self.WORD_LIST[idx]

            if len(word) == word_len:
                self.SORTED_WORD_LIST[word_len].append(word)
            else:
                word_len += 1
                self.SORTED_WORD_LIST[word_len].append(word)

            idx += 1



# Tests
dictionary = Smart_Dictionary()
dictionary.test()
