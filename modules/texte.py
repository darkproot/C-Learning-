from flet import Container, Text, Row

class Spacing(Container):
    def __init__(self, spacing: int = 30):
        super().__init__(height=spacing)

class Texte(Container):
    def __init__(self, text: str):
        super().__init__(padding=0,)
        self.content = Row([
            Text(
                f"{'\t'*8}" + text, 
                expand=True,
                size=20,
                color='black',
                font_family='texte',
            )
        ])