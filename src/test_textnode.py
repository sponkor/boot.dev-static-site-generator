import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase): #These test cases check whether two textnodes are equivalent
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_url(self):
        node = TextNode("This tests differences in URL", TextType.NORMAL, 'http://localhost:8888')
        node2 = TextNode("This tests differences in URL", TextType.NORMAL)
        self.assertNotEqual(node, node2)
    
    def test_diftext(self):
        node = TextNode("This is text node 1", TextType.NORMAL)
        node2 = TextNode("This is text node 2", TextType.NORMAL)
        self.assertNotEqual(node, node2)

    def test_diftype(self):
        node = TextNode("This text is looks different", TextType.BOLD)
        node2 = TextNode("This text is looks different", TextType.CODE) 
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main() 