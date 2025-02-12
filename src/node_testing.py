from htmlnode import LeafNode, ParentNode
from texttoleaf import text_node_to_html_node
from textnode import TextNode, TextType

def main(): # Testing textnode to leafnode conversion
    BoldText = TextNode('This text will be BOLD!', TextType.BOLD)
    BoldHTML = text_node_to_html_node(BoldText)
    
    BasicText = TextNode('This text will look boring', TextType.NORMAL)
    BasicHTML = text_node_to_html_node(BasicText)
    
    ItalicText = TextNode('This text will be slanted', TextType.ITALIC)
    ItalicHTML = text_node_to_html_node(ItalicText)
    
    CodeText = TextNode('This is code', TextType.CODE)
    CodeHTML = text_node_to_html_node(CodeText)
    
    LinkText = TextNode('This is the anchor text', TextType.LINK, 'https://localhost:8888')
    LinkHTML = text_node_to_html_node(LinkText)
    
    ImageText = TextNode('This is alt text', TextType.IMAGE, 'https://localhost:8888')
    ImageHTML = text_node_to_html_node(ImageText)
    
    BadText = TextNode('This should not work', 'Bad')
    BadHTML = text_node_to_html_node(BadText)
    print(BadHTML.to_html())
main()