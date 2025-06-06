class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # A string representing the tag name (e.g. "p", "a", "h1", etc.). 
        self.value = value # A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        self.children = children # A list of HTMLNode objects representing the children of this node
        self.props = props # A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}

# An HTMLNode without a tag will just render as raw text
# An HTMLNode without a value will be assumed to have children
# An HTMLNode without children will be assumed to have a value
# An HTMLNode without props simply won't have any attributes
    
    def to_html(self):
        raise NotImplementedError
        # Child clases will override this method to render themselves as HTML.

    def props_to_html(self):
        # return a string that represents the HTML attributes of the node
        if self.props == None:
            return ""
        else:
            result = ""
            for key,value in self.props.items():
                result += f' {key}="{value}"'         
            return result
                
    def __repr__(self):
        print(f"HTMLNode: tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props}")

    
    def __eq__(self, other):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )