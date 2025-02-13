from flet import Container, Row, Text
from .color import BG

class Titre(Container):
    def __init__(self, content: str = '1- Les variables'):
        super().__init__(
            height=50,
            padding=10,
            border_radius=20,
            bgcolor=BG,
        )
        self.content = Row([
            Text(content, size=20, expand=True, text_align='center', color='white', weight='bold')
        ])