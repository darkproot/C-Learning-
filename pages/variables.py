from flet import Container, padding, Page, Column, Text, Row, MainAxisAlignment
from modules.fonctions import pourcentage
from modules.color import DEEP_BLUE
from modules.syntaxe import Syntaxe

class Display(Container):
    def __init__(self, page: Page):
        super().__init__(
            bgcolor='white',
            border_radius=10,
            expand=True,
            height=page.window.height - 70,
            padding=padding.only(pourcentage(page.window.width, 10), 15, pourcentage(page.window.width, 10)),
        )
        self.content = Column(
            controls=[Syntaxe(page, content="for (int i; i < 10; i++){\n\tprintf('%d', i);\n}")],
            alignment=MainAxisAlignment.CENTER,
        )