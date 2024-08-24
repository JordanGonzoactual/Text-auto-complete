import nltk
from sourcewords import wordsource
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

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
        self.source_of_words = wordsource()
        self.wordlist = self.source_of_words.listofwords()
        self.casefolded_word = [[''.join(char).casefold()for char in word] for word in self.wordlist for char in word]
        
        
        
  
       
     # Inserts char into trie
    def insertchar(self, word):       
        #logging.debug("Inserting Char")
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode(char)
            current = current.children[char]
        current.is_word = True
        logging.debug(f"Inserted word :{word}")
        
        return True  
        
        

        # Finds char in trie
    def findchar(self, word):        
        current = self.root
        word = self.casefolded_word
      
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
                logging.debug(f"No match found for prefix: {prefix}")
                return None
            current = current.children[char]
         # If the loop completes, the prefix exists in the Trie
        suggestions = self.get_suggestions_from_node(current)
        logging.debug(f"Suggestions for prefix '{prefix}': {suggestions}")
        return suggestions
            
    def get_suggestions_from_node(self, node):
    # This method would gather all words that start from the given node
        suggestions = []
        if node.is_word ==True:
            suggestions.append(node.char)  # Collect the word here
        for child in node.children.values():
            suggestions.extend(self.get_suggestions_from_node(child))
        return suggestions
            
 
if __name__== "__main__":
    Trie()    
    
    





