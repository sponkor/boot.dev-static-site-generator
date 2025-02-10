import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_eq(self): # Tests equivalency between two HTML nodes
        node = HTMLNode('Test', 'Test', 'Test', 'Test')
        node2 = HTMLNode('Test', 'Test', 'Test', 'Test')
        self.assertEqual(node, node2)

    def test_diftag(self): # Tests if two nodes with different tags are identified separately 
        node = HTMLNode('test tag')
        node2 = HTMLNode('different tag')
        self.assertNotEqual(node, node2)

    def test_props2html(self): # Tests if the props_to_html method works properly
        node = HTMLNode(None,None,None,{'Key': 'Value', 'Key2': 'Value2'})
        if node.props_to_html() != ' Key="Value", Key2="Value2"':
            raise Exception(".props_to_html method printed incorrectly")
        else: return None
    
class TestLeafNode(unittest.TestCase):

    def test_eq(self): # Tests equivalency between two leaf nodes
        leaf = LeafNode('p', 'test')
        leaf2 = LeafNode('p', 'test')
        self.assertEqual(leaf, leaf2)

    def test_2htmlnoURL(self): # Tests the .to_html() method of a leaf node
        leaf = LeafNode('p', 'test')
        if leaf.to_html() != '<p>test</p>':
            raise Exception(".to_html method printed incorrectly")
        else: return None

    def test_2htmlwithURL(self): # Tests the .to_html() method of a leaf node with a URL/property value
        leaf = LeafNode('p', 'test', {'Key': 'Value'})
        if leaf.to_html() != '<p Key="Value">test</p>':
            raise Exception(".to_html method (with property) printed incorrectly")
        else: return None

if __name__ == '__main__':
    unittest.main()