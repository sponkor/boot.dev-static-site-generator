from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

def main(): #Currently makes a TextNode object and prints the object to console
    NewTextNode = TextNode('test', 'test', 'test')
    print(NewTextNode)

    NewHTMLNode = HTMLNode('test', 'test', 'test', {'test': 'this is a test'})
    print(NewHTMLNode)
    print(NewHTMLNode.props_to_html())

    NewLeafNode = LeafNode('p', 'test')
    print(NewLeafNode.to_html())

    LeafNodeURL = LeafNode('url', 'testing url', {'Key': 'Value'})
    print(LeafNodeURL.to_html())

    NewParentNode = ParentNode('i', [NewLeafNode])
    print(NewParentNode.to_html())
main()