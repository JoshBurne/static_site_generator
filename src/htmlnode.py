#tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
#value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
#children - A list of HTMLNode objects representing the children of this node
#props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props != None:
            string = ""
            for key in self.props:
                string += (f' {key}="{self.props[key]}"')
            return string
        return ""

    def __repr__(self):
        return f"tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props}"
    