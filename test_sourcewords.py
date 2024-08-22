import unittest
from sourcewords import wordsource
from nltk.corpus import gutenberg
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')



class test_wordsource(unittest.TestCase):

    def setUp(self):
            self.words_source = wordsource()
            self.text = gutenberg.raw('austen-emma.txt')
            self.actualtext = self.text[:1000]
            self.source = str(self.actualtext)
            print(f"text = {self.actualtext}")
            logging.debug(f"SetUP: {self.words_source} Initialized")
        


    
     # Tests tokenize method
    def test_tokenize(self):
        tokens = self.words_source.tokenizewords()
        self.assertTrue((tokens))
    


     # tests clean tokens method
    def test_cleantokens(self):
        clean_tokens = self.words_source.cleantokens()
        self.assertTrue((clean_tokens))


     # tests char sequence method
    def test_charsequence(self):
        char_sequence = self.words_source.charsequence()
        self.assertTrue((char_sequence))

if __name__ == "__main__":
    unittest.main()