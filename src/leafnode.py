from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = "", props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if (self.value == "" or self.value == None) and self.tag != "img":
            raise ValueError("HTML value is required")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
