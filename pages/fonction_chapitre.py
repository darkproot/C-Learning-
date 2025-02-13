from flet import Container, padding, Page, MainAxisAlignment, Column, Row, Text
from modules.fonctions import pourcentage
from modules.texte import Texte

class Display(Container):
    def __init__(self, page: Page):
        super().__init__(
            bgcolor='white',
            border_radius=10,
            expand=True,
            height=page.window.height - 70,
            padding=padding.only(pourcentage(page.window.width, 10), 15, pourcentage(page.window.width, 10)),
        )
        self.content = Column([Texte("En langage C, une variable est un espace mémoire réservé permettant de stocker des données. Les variables jouent un rôle fondamental en programmation, car elles permettent de manipuler des informations dynamiquement au cours de l’exécution d’un programme")], alignment=MainAxisAlignment.CENTER)