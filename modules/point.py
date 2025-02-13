from flet import Container, cupertino_icons, Row, Text, Icon, TextStyle, BoxShadow, Offset
from .color import BLUE

class Point(Container):
    def __init__(self, titre: str):
        super().__init__(
            border_radius=10,
            padding=10,
            bgcolor=BLUE,
            width=len(titre) + 5,
        )
        self.titre = titre
        self.text_style = TextStyle(shadow=BoxShadow(1, 1, 'black54', Offset(2, 2)))
        self.content = Row(
            controls=[
                Icon(cupertino_icons.ARROW_RIGHT_SQUARE, color='white'),
                Text(self.titre, font_family='texte', weight='bold', size=15, color='white', style=self.text_style),
            ]
        )