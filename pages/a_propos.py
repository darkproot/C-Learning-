from flet import Container, Page, Column, MainAxisAlignment, padding
from modules.title import GrandTitre
from modules.fonctions import pourcentage
from modules.constantes import HEIGHT
from modules.texte import Texte, Spacing

A_PROPOS: str = """C Learning est une application PC conçue pour apprendre la programmation en C de manière interactive et structurée. Que vous soyez débutant ou que vous souhaitiez approfondir vos connaissances, C Learning vous guide à travers les concepts fondamentaux du langage C, avec des explications claires et des exercices pratiques pour chaque sujet."""
A_PROPOS1: str = """C Learning vous aide à maîtriser le langage C à votre propre rythme. Que vous soyez étudiant, professionnel ou passionné par la programmation, cette application est conçue pour vous accompagner dans votre apprentissage avec des outils pratiques et des contenus adaptés."""

class Display(Container):
    def __init__(self, page: Page):
        super().__init__(
            bgcolor='white',
            border_radius=10,
            expand=True,
            height=page.window.height - HEIGHT,
            padding=padding.only(pourcentage(page.window.width, 10), 15, pourcentage(page.window.width, 10)),
        )
        self.content = Column(
            controls=[
                GrandTitre(text="A propos"),
                Spacing(), Texte(A_PROPOS), Texte(A_PROPOS1),
            ],
            alignment=MainAxisAlignment.CENTER,
        )