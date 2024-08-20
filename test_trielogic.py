import unittest
from Trielogic import TrieNode, Trie


class Testtrie(unittest.TestCase):
     # Test Trie node
    def test_trienode(self):
        self.trienode = TrieNode()
   
   
     # Test trie structure
    def test_trie(self):
        self.trie = Trie()

     # Test insert method
    def test_insert(self):
        self.trie.insertchar("Hello") 
        self.assertTrue(self.trie.findchar("hello"))
        self.assertFalse(self.trie.findchar("hell"))
        self.assertFalse(self.trie.findchar("helloo"))
        self.assertFalse(self.trie.findchar("world"))


     # Test start with method
    def test_startswith(self):
        self.trie.insertchar("Hello")
        self.assertTrue(self.trie.startswith("he"))
        self.assertTrue(self.trie.startswith("hello"))
        self.assertFalse(self.trie.startswith("helloo"))
        self.assertFalse(self.trie.startswith("world"))
    
       

if __name__ == "__main__":
    unittest.main()