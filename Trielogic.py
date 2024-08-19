from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import os


nltk.download()

# Class for Trie node
class TrieNode:
    # initializer
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children ={}






# Class for Trie structure
class Trie(object):
    # Initializer
    def __init__(self):
        self.root = TrieNode("")



