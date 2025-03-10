from flet import Container, ListView, Page, padding
from modules.fonctions import pourcentage
from modules.qcm import Qcm
from modules.title import Titre
from modules.code import MiniCode


MINICODE1: str = """int x = 5;\nprintf("%d", x++);"""
MINICODE2: str = """char c = 'A';\nprintf("%c", c + 1);"""

QCM1 = {
    'question': "Quelle est la bonne déclaration d'une variable entière en C ?",
    'proposition': ["int nombre;", "nombre int;", "integer nombre;", "var nombre;"],
    'reponse': 0,
}
QCM2 = {
    'question_id': 2,
    'question': "Quelle est la portée d'une variable déclarée à l'intérieur d'une fonction ?",
    'proposition': ["Globale", "Locale", "Dynamique", "Statique"],
    'reponse': 1,
}
QCM3 = {
    'question_id': 3,
    'question': "Quelle est la taille typique d'un entier (int) en C sur un système 32 bits ?",
    'proposition': ["1 octet", "2 octets", "4 octets", "8 octets"],
    'reponse': 1,
}
QCM4 = {
    'question_id': 4,
    'question': "Quelle est la valeur initiale d'une variable locale non initialisée en C ?",
    'proposition': ["0", "NULL", "Une valeur aléatoire", "Dépend du compilateur"],
    'reponse': 1,
}
QCM5 = {
    'question_id': 5,
    'question': "Quelle est la bonne syntaxe pour déclarer une constante en C ?",
    'proposition': ["const int x = 10;", "int const x = 10;", "#define x 10", "Toutes les réponses ci-dessus sont valides"],
    'reponse': 0,
}
QCM6 = {
    'question_id': 6,
    'question': "Quelle est la sortie du code suivant ?",
    'proposition': ["5", "6", "Erreur de compilation", "Comportement indéfini"],
    'reponse': 0,
    'minicode': MiniCode(MINICODE1)
}
QCM7 = {
    'question_id': 7,
    'question': "Quelle est la différence entre float et double en C ?",
    'proposition': ["float a une précision plus élevée que double", "double a une précision plus élevée que float", "Il n'y a aucune différence", "double prend moins d'espace en mémoire que float"],
    'reponse': 1,
}
QCM8 = {
    'question_id': 8,
    'question': "Quelle est la sortie du code suivant ?",
    'proposition': ["A", "Erreur de compilation", "B", "66"],
    'reponse': 2,
    'minicode': MiniCode(MINICODE2)
}
QCM9 = {
    'question_id': 9,
    'question': "Quelle est la bonne déclaration d'une variable de type unsigned int ?",
    'proposition': ["unsigned int x;", "int unsigned x;", "unsigned x;", "Toutes les réponses ci-dessus sont valides"],
    'reponse': 3,
}
QCM10 = {
    'question_id': 10,
    'question': "Que se passe-t-il si une variable globale et une variable locale ont le même nom ?",
    'proposition': ["La variable globale est utilisée", "Erreur de compilation", "Comportement indéfini", "La variable locale est utilisée"],
    'reponse': 3,
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
                Container(height=40)
            ]
        )