import sys
sys.path.append('..')

import lyricscramble.lyric_chain as lc
import unittest


class lyric_chain_test(unittest.TestCase):
    def setup(self):
        self.chain = lc.lyric_chain("ignore this text")

    def test_extract_words_no_punctuation(self):
        self.setup()
        txt = "I just call her boo"
        expected_words = ["i", "just", "call", "her", "boo", ]
        words = self.chain.extract_words(txt)
        self.assertEqual(expected_words, words)

    def test_extract_words_with_punctuation(self):
        self.setup()
        txt = "./what@*# $(@)the@# !@#fudge( ))W"
        expected_words = ["what", "the", "fudge", "w"]
        words = self.chain.extract_words(txt)
        self.assertEqual(expected_words, words)

    def test_extract_words_with_no_txt(self):
        self.setup()
        self.assertRaises(BaseException, self.chain.extract_words, "")


if __name__ == '__main__':
    unittest.main()
