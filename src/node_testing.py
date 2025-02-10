from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

def main(): 
    BoldNode = LeafNode('b', 'This text would be BOLD')
    ItalicNode = LeafNode('i', 'This text would probably be italicized')
    NormalNode = LeafNode(None, 'This node is boring...')
    BINode = ParentNode('c1', [BoldNode, ItalicNode])
    ININode = ParentNode('c2', [ItalicNode, NormalNode, ItalicNode])
    HighNode = ParentNode('C1', [BINode, ININode])
    BadNode = ParentNode(None, [ININode])
    print(HighNode.to_html())
main()