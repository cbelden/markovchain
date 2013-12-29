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
        polished = txt.translate(string.maketrans("", ""), string.punctuation).lower()
        words = polished.split()
        return words

    def create_chain(self, words):
        """
        Constructs the underlying data type.  This is a dictionary with word keys.
        The value associated with each key is a dictionary containing all words that
        occur immediately following the key in the text used to construct the chain.
        The value associated with these secondary keys is a frequency value.

        ie self.chain = {word1: {subword1:freq1, subword2:freq2, ...}, ...}
        """
        l_chain = {}

        for i in range(len(words) - 1):
            if words[i] in l_chain and words[i+1] in l_chain[words[i]]:
                    l_chain[words[i]][words[i+1]] += 1
            else:
                l_chain[words[i]] = {words[i+1]: 1}

        return l_chain

    def generate_phrase(self, n):
        """
        Generate a phrase of length n based off the markov dict
        """

        if self.chain is None:
            raise "No markov chain in memory"

        start = random.randrange(len(self.words))
        new_word = self.words[start]
        msg = ''

        print "...generating phrase\n"

        for i in range(n):
            msg += new_word.strip() + ' '

            if new_word in self.chain:
                new_word = self.get_randword(self.chain[new_word])
            else:
                new_word = self.get_randword(self.words)

        return msg.capitalize()

    def get_randword(self, words):
        n = 0
        count = 0

        for word in words:
            n += words[word]

        idx = random.randrange(n)

        for word in words:
            count += words[word]
            if idx <= count:
                return word
