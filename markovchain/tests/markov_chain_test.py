import unittest
from markovchain import MarkovChain


class TestMarkovChain(unittest.TestCase):
    """Tests the public methods for the MarkovChain class."""

    def setUp(self):
        self._corpus = "This is a, sample' corpus.\n How neat is that.\n"
        self._expected_chain = {'this': {'is': 1},
                                'is': {'a': 1, 'that': 1},
                                'a': {'sample': 1},
                                'sample': {'corpus': 1},
                                'corpus': {'.': 1},
                                '.': {'how': 1},
                                'how': {'neat': 1},
                                'neat': {'is': 1},
                                'that': {'.': 1}}

    def tearDown(self):
        pass

    # ~~~~~~~~~~~ CONSTRUCTOR TESTS ~~~~~~~~~~~~~~~
    def test_constructor_valid_input(self):
        """Tests the MarkovChain constructor."""

        chain = MarkovChain(self._corpus)

        # Assert underlying Markov Chain is as expected
        self.assertEqual(chain._markov_chain, self._expected_chain)

    def test_constructor_no_input(self):
        """Tests the MarkovChain constructor with null input."""

        self.assertRaises(TypeError, MarkovChain.__init__, '')

    # ~~~~~~~~~~~ GENERATE PHRASE TESTS ~~~~~~~~~~~~~~~
    def test_generate_phrase_no_params(self):
        """Tests the MarkovChain.generate_phrase method with no input arguments."""

        chain = MarkovChain(self._corpus)
        phrase = chain.generate_phrase()

        # Assert non-None
        self.assertNotEqual(phrase, '')

    def test_generate_phrase_min_words(self):
        """Tests the MarkovChain.generate_phrase method with min_words arg specified."""

        _min_words = 20
        chain = MarkovChain(self._corpus)

        # Generate 10 phrases; test each one
        for i in range(10):
            phrase = chain.generate_phrase(min_words=_min_words)
            self.assertTrue(len(phrase.split(' ')) >= _min_words)

    def test_generate_phrase_invalid_min_words(self):
        """Tests the MarkovChain.generate_phrase method with invalid min_words arg specified."""

        chain = MarkovChain(self._corpus)
        self.assertRaises(ValueError, chain.generate_phrase, -1)

    def test_generate_phrase_max_size(self):
        """Tests the MarkovChain.generate_phrase method with max_size arg specified."""

        _max_size = 140
        chain = MarkovChain(self._corpus)

        # Generate 10 phrases; make sure all under max size.
        for i in range(10):
            phrase = chain.generate_phrase(max_size=_max_size)
            self.assertTrue(len(phrase) <= _max_size)

    def test_generate_phrase_invalid_max_size(self):
        """Tests the MarkovChain.generate_phrase method with invalid max_size arg specified."""

        chain = MarkovChain(self._corpus)
        self.assertRaises(ValueError, chain.generate_phrase, -1)

    def test_generate_phrase_both_valid_params(self):
        """Tests the MarkovChain.generate_phrase method with min_words and max_size args specified."""

        _max_size = 140
        _min_words = 5
        chain = MarkovChain(self._corpus)

        for i in range(10):
            phrase = chain.generate_phrase(max_size=_max_size, min_words=_min_words)
            valid = len(phrase.split(' ')) >= _min_words and len(phrase) < 140
            self.assertTrue(valid)

    def test_generate_phrase_invalid_parameters(self):
        """Tests the MarkovChain.generate_phrase with conflicting parameters."""

        _max_size = 5
        _min_words = 10
        chain = MarkovChain(self._corpus)

        self.assertRaises(ValueError, chain.generate_phrase, max_size=_max_size, min_words=_min_words)



if __name__ == '__main__':

    # Run Tests
    unittest.main()
