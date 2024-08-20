from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize, word_tokenize
import string
import nltk





# Class to prep words from source for trie structure
class wordsource:
    # Initializer
    def __init__(self, text):
        self.text = gutenberg.raw('austen-emma.txt')

    # Tokenize words from text
    def tokenizewords(self):
        self.tokens = word_tokenize(self.text)
        return self.tokens
    

    # Converts tokenized words to lowerrcase and removes punctuation
    def cleantokens(self, tokens):
        self.clean_tokens = [word.lower() for word in tokens if word.isalpha()]
        return self.clean_tokens
    


    # Prepares word into char for trie structure
    def charsequence(self):
        self.char_sequence = [list(word) for word in self.clean_tokens]
        return self.char_sequence

    

