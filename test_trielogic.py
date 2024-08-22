import unittest
from trielogic import Trie
import logging

# Logging config
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class Testtrie(unittest.TestCase):
    
     # Test trie structure
    def setUp(self):
        
        try :
            self.trie = Trie()
            logging.debug("Inializing Trie structure")
       
        except TypeError as e:
            logging.debug(f"Type Error just occured: {e}")
        
     # Test insert method
    def test_insert(self):     
        self.trie.insertchar("Hello") 
        self.assertTrue(self.trie.findchar("Hello"))
        self.assertFalse(self.trie.findchar("hell"))
        self.assertFalse(self.trie.findchar("Helloo"))
        self.assertFalse(self.trie.findchar("world"))
           


     # Test start with method
    def test_startswith(self):       
        self.trie.insertchar("Hello")
        self.assertTrue(self.trie.startswith("He"))
        self.assertTrue(self.trie.startswith("hell"))
        self.assertTrue(self.trie.startswith("Hello"))
        self.assertFalse(self.trie.startswith("Helloo"))
        self.assertFalse(self.trie.startswith("world"))
        
     
     #Test find char method
    def test_findchar(self):
        self.trie.insertchar("Hello")
        self.assertTrue(self.trie.findchar("Hello"))
        self.assertFalse(self.trie.findchar("Helloo"))
        self.assertFalse(self.trie.findchar("world"))
        


    
       

if __name__ == "__main__":
    unittest.main()