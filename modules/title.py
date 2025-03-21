from flet import Container, Row, Text, Border, BorderSide, Icon, MainAxisAlignment
from .color import BG, DEEP_BLUE

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

class GrandTitre(Container):
    def __init__(self, icon: str = None, text: str = "Titre", font_size: int = 50):
        super().__init__(
            border_radius=20,
        )
        self.text = text
        self.font_size = font_size
        self.border = Border(
            BorderSide(5, DEEP_BLUE),
            BorderSide(5, DEEP_BLUE),
            BorderSide(5, DEEP_BLUE),
            BorderSide(5, DEEP_BLUE),
        )
        self.icon = Icon(
            size=50,
            name=icon,
            scale=1.2,
            color=DEEP_BLUE,
        ) if icon else None
        self.texte = Text(
            weight='bold', 
            color=DEEP_BLUE,
            text_align='center',
            font_family='texte',
            size=self.font_size,
            value=self.text.capitalize(),
        )
        self.content = Row(
            controls=[self.icon, self.texte] if self.icon else [self.texte],
            alignment=MainAxisAlignment.CENTER,
        )