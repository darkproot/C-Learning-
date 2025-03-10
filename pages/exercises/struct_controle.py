from flet import Container, ListView, Page, padding
from modules.fonctions import pourcentage
from modules.qcm import Qcm
from modules.title import Titre
from modules.texte import Spacing, Texte
from modules.code import ExerciceCode


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
                Texte('Exercice 1:'),
                ExerciceCode("Ecriver un code qui affiche 'Hello World!'"),
            ]
        )