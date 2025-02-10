class HTMLNode(): # Parent class for HTMLNodes
    
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag, self.value, self.children, self.props = tag, value, children, props

    def to_html(self): # Parent method to be overwritten by child classes
        raise NotImplementedError
    
    def props_to_html(self): # Parent method that can display the properties and their values for a node
        properties, propertystring = list(self.props.items()), []
        for item in properties:
            propertystring.append(f' {item[0]}="{item[1]}"')
        return ",".join(propertystring)
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
    
    def __eq__(self, other):
        if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props:
            return True
        
class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def props_to_html(self):
        return super().props_to_html()
    
    def __repr__(self):
        return super().__repr__()
    
    def __eq__(self, other):
        return super().__eq__(other)

    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf Node requires a value")
        
        if self.tag == None:
            return f'{self.value}'
        elif self.props == None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def props_to_html(self):
        return super().props_to_html()
    
    def __repr__(self):
        return super().__repr__()
    
    def __eq__(self, other):
        return super().__eq__(other)

    def to_html(self):
        if self.children == None or len(self.children) == 0:
            raise ValueError("Parent Node lacks child nodes")
        self.childlist = list(map(lambda x: x.to_html(), self.children))
        if self.tag == None:
            raise ValueError("Parent Node lacks a tag")
        elif self.props == None:
            return f'<{self.tag}>{"".join(self.childlist)}</{self.tag}>'
        else:
            return f'<{self.tag}{self.props_to_html()}>{"".join(self.childlist)}</{self.tag}>'