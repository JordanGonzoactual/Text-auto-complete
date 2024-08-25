from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize
import nltk





# Class to prep words from source for trie structure
class wordsource(object):
     # Initializer
    def __init__(self):
        self.text = gutenberg.raw('austen-emma.txt')
        self.actualtext = self.text[:10000]
        self.source = str(self.actualtext)
        self.tokenized = self.tokenizewords()
        self.cleaned = self.cleantokens()
        self.tokenizewords()
        self.cleantokens()
        self.charsequence()
        self.listofwords()
        #print(str(self.listofwords()))

        
   
      
       
      

     # Tokenize words from text
    def tokenizewords(self):
        self.tokens = word_tokenize(self.source)
        return self.tokens
    

     # Converts tokenized words to lowerrcase and removes punctuation
    def cleantokens(self):
        self.clean_tokens = [word.lower() for word in self.tokenized if word.isalpha()]
        return self.clean_tokens
    


     # Prepares word into char for trie structure
    def charsequence(self):  
        cleanedtokens = self.cleaned
        self.char_sequence = [list(word) for word in cleanedtokens]
        return self.char_sequence

     # Returns list of words
    def listofwords(self):
    
        return [''.join(word) for word in self.char_sequence]
    
 



if __name__== "__main__":
    wordsource()
    
    