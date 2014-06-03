import string
import random
import re


class MarkovChain(object):

    def __init__(self, text):
        """Generates the underlying Markov Chain."""

        # Declare some 'constants'
        self._ENDSENTENCE = 'endsentence'
        self._BEGINSENTENCE = 'beginsentence'

        random.seed()                                           # set seed based on current time
        self._markov_chain = self._construct_chain(text)        # the underlyng markov chain
        self._stop_p = 0.10                                     # set probabality that a generated phrase ends

    def __iter__(self):
        """Iterates over the terms in the underlying Markov Chain."""

        for term, consecutive_terms in self._markov_chain.iteritems():
            yield term, consecutive_terms

    def __getitem__(self, key):
        """Returns the bigrams for a given term."""

        return self._markov_chain[key]

    def _construct_chain(self, text):
        """Constructs the underlying Markov Chain."""

        if not text:
            raise TypeError('Expected a non empty value for "text."')

        words = self._extract_words(text)
        bigrams = {}

        for i in range(len(words) - 1):

            # Get bigram
            first = words[i]
            second = words[i+1]

            # Add the current word-pair to bigrams
            if not first in bigrams:
                bigrams[first] = {}
            if not second in bigrams[first]:
                bigrams[first][second] = 0

            # Increment the bigram count
            bigrams[first][second] += 1

        return bigrams

    def _extract_words(self, s):
        """Strips input string of punctuation and splits on whitespace."""

        stripped = self._strip_punctuation(s)
        return stripped.split()

    def _strip_punctuation(self, s):
        """Strips punctuation (except periods) from input string and sets all characters to lowercase."""

        # Convert to utf-8
        s = s.encode('utf-8', 'replace')

        # Convert all periods to markers denoting the end and beginning
        # of a sentence.
        end_sentence = ' %s ' % (self._ENDSENTENCE)
        s = re.sub('\.{1}', end_sentence, s)

        # Strip punctuation
        table = string.maketrans("", "")
        stripped = s.translate(table, string.punctuation)

        # Replace periods
        stripped = re.sub(self._ENDSENTENCE, '.', stripped)

        return stripped.lower()

    def generate_phrase(self, max_size=None, min_words=None):
        """Generates a phrase by performing random walk on the Markov chain."""

        # Invalid input values raise an exception
        valid = True

        if max_size:
            valid = type(max_size) is int and max_size >= 0

        if min_words:
            valid = valid and type(min_words) is int and min_words >= 0

        if not valid:
            raise ValueError("Expected positive int value(s) for input.")

        # If both parameters are present, make sure parameters are reasonable
        if max_size and min_words:
            if 5*min_words >= max_size:
                raise ValueError("max_size paramemeter must be at least five times larger than min_words.")

        new_word = ''
        msg = ''
        word_count = 0

        while 1:

            # Generate a successor word
            if new_word in self._markov_chain:
                new_word = self._get_next_term(self._markov_chain[new_word])

            # Generate a random word if new_word is not a key in the markov chain
            else:
                new_word = random.choice(self._markov_chain.keys())

            # Check if new word will push us over the character limit
            if max_size and len(msg) + len(new_word) >= max_size:
                break

            # Append successor to word
            msg += new_word + ' '

            # Increment word_count if min_words specified (and 'word' is not a period)
            if min_words and new_word is not '.':
                word_count += 1

            # probabalistically decide to stop
            if not min_words or word_count >= min_words:
                if random.random() <= self._stop_p:
                    break

        return msg.rstrip().capitalize()

    def _get_next_term(self, tf):
        """Stochastically chooses the next generated term."""

        total_occurences = 0
        count = 0

        for term in tf:
            total_occurences += tf[term]

        # will be used to "randomly" return one of the options
        idx = random.randrange(total_occurences)

        # Return one of the words based on idx. Words with a higher requency
        # will be chosen more often
        for term, freq in tf.iteritems():
            count += freq
            if idx <= count:
                return term

        raise Exception('Error: could not generate a successor term.')
