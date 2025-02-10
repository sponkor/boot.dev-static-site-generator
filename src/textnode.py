from enum import Enum

class TextType(Enum): #This enum is used to assign the type of text to a text node
    NORMAL = 'normal'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'

class TextNode(): #This TextNode class defines how our TextNodes are setup
    def __init__(self, text, text_type, url=None):
        self.text, self.text_type, self.url = text, text_type, url

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    