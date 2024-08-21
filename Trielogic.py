import nltk
import os

# Class for Trie node
class TrieNode:
     # initializer
    def __init__(self,  char =''):
        self.char = char
        self.children ={}
        self.is_word = False
       
# Class for Trie structure
class Trie(object):
     # Initializer
    def __init__(self):
        self.root = TrieNode()
  
       
     # Inserts char into trie
    def insertchar(self, word):
        current = self.root
       
        for i, char in enumerate(word):
            if char not in current.children:
                prefix = word[0:i+1]
                current.children[char] = TrieNode(prefix)
               
            current = current.children[char]
        current.is_word = True
        return True  
        
        

        # Finds char in trie
    def findchar(self, word):
        current = self.root
      
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
       
        return current.is_word
       


     #looks for prefix in node
    def startswith(self, prefix):
        current = self.root
        
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
    
    
    





