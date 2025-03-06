from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        html_str = ""

        if self.tag == None:
            raise ValueError("HTML tag required")
        if self.children == None:
            raise ValueError("HTML child node(s) required")
        html_str = f"<{self.tag}{self.props_to_html()}>"

        for child in self.children:
            html_str += f"{child.to_html()}"
        html_str += f"</{self.tag}>"

        return html_str
