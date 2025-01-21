from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag or self.tag is None:
            raise ValueError("Parent Node missing tag")
        elif not self.children or self.children is None:
            raise ValueError("Parent node has no children")
        else:
            html_string = f"<{self.tag}{self.props_to_html()}>" # opening tag + props
            for child in self.children:
                html_string += child.to_html()
            html_string += f"</{self.tag}>"
        
        return html_string