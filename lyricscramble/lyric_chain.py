import string
import random


class lyric_chain(object):
    def __init__(self, txt):
            self.words = self.extract_words(txt)
            self.chain = self.create_chain(self.words)

    def __iter__(self):
        for key in self.chain:
            yield key, self.chain[key]

    def __getitem__(self, key):
        return self.chain[key]

    def extract_words(self, txt):
        if not txt:
            raise BaseException("No lyric text to generate chain from")

        polished = txt.translate(string.maketrans("", ""), string.punctuation).lower()
        words = polished.split()
        return words

    def create_chain(self, words):
        """
        Constructs the underlying data type.  This is a dictionary with word keys.
        The value associated with each key is a dictionary containing all words that
        occur immediately following the key in the text used to construct the chain.
        The value associated with these secondary keys is a frequency value.

        ie self.chain = {word1: {subsequent_word1:freq1, subsequent_word2:freq2, ...}, ...}
        """

        lyric_chain = {}

        for i in range(len(words) - 1):
            current_word = words[i]
            subsequent_word = words[i+1]

            if current_word in lyric_chain:
                if subsequent_word in lyric_chain[current_word]:
                    lyric_chain[current_word][subsequent_word] += 1
                else:
                    lyric_chain[current_word][subsequent_word] = 1
            else:
                lyric_chain[current_word] = {subsequent_word: 1}

        return lyric_chain

    def generate_phrase(self, n):
        """
        Generate a phrase of length n based off the markov dict
        """

        if self.chain is None:
            raise BaseException("No markov chain in memory")

        start = random.randrange(len(self.words))
        new_word = self.words[start]
        msg = ''

        print "...generating phrase\n"

        for i in range(n):
            msg += new_word + ' '

            if new_word in self.chain:
                new_word = self.get_randword(self.chain[new_word])
            else:
                new_word = self.words[random.randrange(len(self.words))]

        return msg.capitalize()

    def get_randword(self, words):
        """
        Input
            A dictionary of words and their frequencies

        Returns
            One of the words in the given dictionary.
        """
        total_occurences = 0
        count = 0

        for word in words:
            total_occurences += words[word]

        # will be used to "randomly" return one of the options
        idx = random.randrange(total_occurences)

        # Return one of the words based on idx. Words with a higher
        # frequency should be chosen more often
        for word in words:
            count += words[word]
            if idx <= count:
                return word
