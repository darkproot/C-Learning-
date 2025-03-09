from flet import Container, ListView, Page, padding
from modules.fonctions import pourcentage
from modules.qcm import Qcm
from modules.title import Titre
from modules.code import MiniCode

QCM = {
    'question': "Quelle est la bonne déclaration d'une variable entière en C ?",
    'proposition': ["int nombre;", "nombre int;", "integer nombre;", "var nombre;"],
    'reponse': 0,
    'minicode':MiniCode("sfgsdgf\nsdfsdfas\nasdfasdf")
}

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
                Titre('Questions a choix multiples'), 
                Qcm(**QCM)
            ]
        )