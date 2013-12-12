import random
import string


class lyric_chain(object):
    def __init__(self, lyric_fp):
        self.words = self.extract_words(lyric_fp)
        self.chain = self.create_chain()

    def __iter__(self):
        for key in self.chain:
            yield key, self.chain[key]

    def __getitem__(self, key):
        return self.chain[key]

    def extract_words(self, lyric_fp):
        f = open(lyric_fp, 'r')
        txt = f.read()
        f.close()

        polished = txt.translate(string.maketrans("", ""), string.punctuation).lower()
        words = polished.split()
        return words

    def create_chain(self):
        l_chain = {}
        words = self.words

        for i in range(len(words) - 1):
            if words[i] in l_chain:
                l_chain[words[i]].append(words[i+1])
            else:
                l_chain[words[i]] = [words[i+1]]

        return l_chain

    def generate_phrase(self, n):
        """Generate a phrase of length n based off the markov dict"""

        if self.chain is None:
            raise "No markov chain in memory"

        start = random.randrange(len(self.chain))
        new_word = self.words[start % len(self.words)]
        msg = ''

        for i in range(n):
            msg += new_word.strip() + ' '

            if new_word in self.chain:
                new_word = self.get_randword(self.chain[new_word])
            else:
                new_word = self.get_randword(self.words)

        return msg.capitalize()

    def get_randword(self, words):
        i = random.randrange(len(words))
        return words[i]

if __name__ == '__main__':
    mychain = lyric_chain('pimps_lyrics.txt')
    print mychain.generate_phrase(15)
