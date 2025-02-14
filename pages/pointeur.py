from flet import Container, padding, Page, MainAxisAlignment, ListView, Row, Text
from modules.fonctions import pourcentage
from modules.color import DEEP_BLUE
from modules.tableau import Table

DATA: list[list[str | int]] = [
    ['Opérateur', 'Description', 'Exemple', 'Résultat'],
    ['++', 'Incrémentation', 'a++ ou ++a', 'Ajoute 1 a a'],
    ['--', 'Décrémentation', 'a-- ou --a', 'Soustrait 1 a a'],
]

class Display(Container):
    def __init__(self, page: Page):
        super().__init__(
            bgcolor='white',
            border_radius=10,
            expand=True,
            height=page.window.height - 70,
            padding=padding.only(pourcentage(page.window.width, 10), 15, pourcentage(page.window.width, 10)),
        )
        self.content = ListView(
            controls=[
                Table(DATA),
            ]
        )