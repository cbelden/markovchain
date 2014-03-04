import string
import random


class language_model(object):
    def __init__(self, txt):
            self.corpus = self.extract_words(txt)                               # stores all words from input text
            self.bigrams = self.generate_language_model(self.corpus)            # bigram language model for phrase generation
            self.continue_p = 0.9                                               # probabality that a phrase adds another word

    def __iter__(self):
        for key in self.bigrams:
            yield key, self.bigrams[key]

    def __getitem__(self, key):
        return self.bigrams[key]

    def extract_words(self, corpus):
        """
        Splits the string of text into a list determined by spaces.  All text is stripped of punctuation.
        """
        if not corpus:
            raise BaseException("No lyric text to generate chain from")

        polished = corpus.translate(string.maketrans("", ""), string.punctuation).lower()
        words = polished.split()
        return words

    def generate_language_model(self, words):
        """
        Constructs the underlying bigram language model.
        Input:
            -words: a list of ordered words generated from a corpous
        Output:
            -a bigram language model implemented as a dictionary of words and their successors. Each
             successor word has a corresponding term frequency (number of times it appeared in the corpus)
        """

        bigrams = {}

        for i in range(len(words) - 1):
            current_word = words[i]
            subsequent_word = words[i+1]

            if current_word in bigrams:
                if subsequent_word in bigrams[current_word]:
                    bigrams[current_word][subsequent_word] += 1
                else:
                    bigrams[current_word][subsequent_word] = 1
            else:
                bigrams[current_word] = {subsequent_word: 1}

        return bigrams

    def generate_string(self):
        """
        Generates a string based on the language model
        """

        if self.bigrams is None and self.corpus is None:
            raise BaseException("No language model or corpus in memory")

        new_word = ''
        msg = ''

        print "...generating phrase\n"

        while 1:

            if new_word in self.bigrams:
                new_word = self.get_successor(self.bigrams[new_word])
            else:
                new_word = self.corpus[random.randrange(len(self.corpus))]

            # append successor to word
            msg += new_word + ' '

            # probabalistically decide to continue
            if random.random() > self.continue_p:
                break

        return msg.capitalize()

    def get_successor(self, tf):
        """
        Input
            A dictionary of words and their term frequency

        Returns
            One of the words in the given dictionary.
        """
        total_occurences = 0
        count = 0

        for word in tf:
            total_occurences += tf[word]

        # will be used to "randomly" return one of the options
        idx = random.randrange(total_occurences)

        # Return one of the words based on idx. Words with a higher
        # frequency should be chosen more often
        for word in tf:
            count += tf[word]
            if idx <= count:
                return word
