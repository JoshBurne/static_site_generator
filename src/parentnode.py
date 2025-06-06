from HTMLNode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError ("ParentNode must accept a 'tag' argument.")
        if self.children is None:
            raise ValueError ("ParentNode must accept a 'children' argument.")
        result = ""
        for child in self.children:        
            result += child.to_html()
        return f"<{self.tag}>{result}</{self.tag}>"

