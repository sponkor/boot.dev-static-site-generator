from textnode import TextType
from htmlnode import LeafNode

def text_node_to_html_node(textNode):
    match textNode.text_type:
        case TextType.NORMAL:
            return LeafNode(None, textNode.text)
        case TextType.BOLD:
            return LeafNode('b', textNode.text)
        case TextType.ITALIC:
            return LeafNode('i', textNode.text)
        case TextType.CODE:
            return LeafNode('code', textNode.text)
        case TextType.LINK:
            return LeafNode('a', textNode.text, {'href': textNode.url})
        case TextType.IMAGE:
            return LeafNode('img', '', {'src': textNode.url, 'alt': textNode.text})
        case _:
            raise Exception("Text type not found")