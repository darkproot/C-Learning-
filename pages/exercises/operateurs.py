from flet import Container, ListView, Page, padding
from modules.title import Titre, GrandTitre
from modules.fonctions import pourcentage
from modules.constantes import HEIGHT
from modules.texte import Spacing
from modules.qcm import Qcm

QCM1 = {
    'question': "Quel est l'opérateur utilisé pour l'affectation en C ?",
    'proposition': ["==", "=", ":=", "->"],
    'reponse': 1,
}
QCM2 = {
    'question_id': 2,
    'question': "Que renvoie l'opérateur % en C ?",
    'proposition': ["La division entière", "Le quotient de la division", "Le reste de la division entière", "Une erreur si utilisé avec des flottants"],
    'reponse': 2,
}
QCM3 = {
    'question_id': 3,
    'question': "Quel opérateur est utilisé pour incrémenter une variable de 1 ?",
    'proposition': ["++", "--", "+=", "=+"],
    'reponse': 0,
}
QCM4 = {
    'question_id': 4,
    'question': "Quel est le résultat de l'expression (5 > 3) && (2 < 4) en C ?",
    'proposition': ["true", "false", "0", "1"],
    'reponse': 3,
}
QCM5 = {
    'question_id': 5,
    'question': "Quelle est la différence entre == et = en C ??",
    'proposition': ["Aucune différence", "== est une comparaison, = est une affectation", "= est une comparaison, == est une affectation", "Les deux sont utilisés pour la comparaison"],
    'reponse': 1,
}
QCM6 = {
    'question_id': 6,
    'question': "Que signifie l'opérateur ! en C ?",
    'proposition': ["Négation logique", "Multiplication", "Puissance", "Modulo"],
    'reponse': 0,
}
QCM7 = {
    'question_id': 7,
    'question': "Quelle est la sortie de l'expression (10 / 4) si 10 et 4 sont des entiers ?",
    'proposition': ["2.5", "2", "3", "4"],
    'reponse': 1,
}
QCM8 = {
    'question_id': 8,
    'question': "Quel opérateur est utilisé pour effectuer un ET bit à bit en C ?",
    'proposition': ["&&", "||", "&", "|"],
    'reponse': 2,
}
QCM9 = {
    'question_id': 9,
    'question': "Que fait l'opérateur ^ en C lorsqu'il est utilisé entre deux entiers ?",
    'proposition': ["Additionne les deux nombres", "Effectue une comparaison logique", "Effectue un OU exclusif bit à bit (XOR)", "Multiplie les deux nombres"],
    'reponse': 2,
}
QCM10 = {
    'question_id': 10,
    'question': "Quelle est la priorité des opérateurs +, *, et - en C ?",
    'proposition': ["+ a la plus haute priorité", "* a la plus haute priorité", "- a la plus haute priorité", "Tous ont la même priorité"],
    'reponse': 1,
}

class Display(Container):
    def __init__(self, page: Page):
        super().__init__(
            bgcolor='white',
            border_radius=10,
            expand=True,
            height=page.window.height - HEIGHT,
            padding=padding.only(pourcentage(page.window.width, 10), 15, pourcentage(page.window.width, 10)),
        )
        self.content = ListView(
            controls=[
                GrandTitre(text="opérateurs"), Spacing(),
                Titre("Question à choix multiple"),
                Qcm(**QCM1),
                Qcm(**QCM2),
                Qcm(**QCM3),
                Qcm(**QCM4),
                Qcm(**QCM5),
                Qcm(**QCM6),
                Qcm(**QCM7),
                Qcm(**QCM8),
                Qcm(**QCM9),
                Qcm(**QCM10),
                Spacing()
            ]
        )