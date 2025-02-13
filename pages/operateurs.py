from flet import Container, padding, Page, MainAxisAlignment, Row, Column, Text
from modules.fonctions import pourcentage
from modules.title import Titre

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
            controls=[Titre()],
            alignment=MainAxisAlignment.CENTER,
        )