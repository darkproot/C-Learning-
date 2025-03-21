from flet import Container, padding, Page, ListView, Row
from modules.fonctions import pourcentage
from modules.syntaxe import Syntaxe
from modules.title import Titre, GrandTitre
from modules.texte import Texte, Spacing
from modules.exemple import Exemple
from modules.code import Code
from modules.tableau import Table
from modules.point import Point

TABLEAU: list[list[str]] = [
    ['Type', 'Taille Mémoire', 'Exemples'],
    ["void", "0 octet", "Généralement pour le retour des fonctions"],
    ["char", "1 octet", "45, A, b"],
    ["short int", "2 octets", "100, 4, 0"],
    ["long", "4 octets", "34534, -5134, 34"],
    ["int", "2 ou 4 octets", "59, 517, -3452"],
    ["long long", "8 octets", "34534345, -34234, 0"],
    ["float", "4 octets", "4.343232, 0.0, -7735.0"],
    ["double", "8 octets", "0.000000004, -0.99945, 1327.9"],
    ["long double", "10 octets", "les réels"],
]

INTRO: str = """En langage C, une variable est un espace mémoire réservé permettant de stocker des données. Les variables jouent un rôle fondamental en programmation, car elles permettent de manipuler des informations dynamiquement au cours de l'exécution d'un programme."""
INTRO2: str = """Chaque variable en C possède un type (int, float, char, etc.), qui définit la nature des données qu'elle peut contenir, ainsi qu'un nom qui permet d'y accéder. Avant d'utiliser une variable, il est nécessaire de la déclarer, et dans certains cas, de l'initialiser avec une valeur par défaut."""
INTRO3: str = """L'utilisation efficace des variables est essentielle pour écrire des programmes optimisés et compréhensibles. Dans la suite, nous explorerons les différents types de variables, leur déclaration, leur portée et leur durée de vie en langage C."""

PARA1: str = """Avant d'utiliser une variable, il faut la déclarer en précisant son type. Voici la syntaxe de base :"""
SYNTAXE1: str = """<type> nom_variable;\nou\n<type> nom_variable = <valeur>;"""
EXEMPLE1: str = f"""#include <stdio.h>\n\nvoid main() {{\n{'\t'*4}int number;\n{'\t'*4}int age = 19;\n{'\t'*4}float prix = 12.5;\n{'\t'*4}char lettre = 'A';\n}}"""

PARA2: str = """Le langage C propose plusieurs types de variables :"""
PARA3: str = """Chaque variable est stockée à une adresse mémoire spécifique. On peut afficher cette adresse avec l'opérateur & et la fonction printf :"""
EXEMPLE2: str = f"""#include <stdio.h>\n\nvoid main() {{\n{'\t'*4}int nombre = 10;\n{'\t'*4}printf("Adresse mémoire de nombre : %p", &nombre);\n}}"""
PARA4: str = """Une variable constante est une variable dont la valeur ne peut pas être modifiée après l'initialisation. On utilise le mot-clé const :"""
EXEMPLE3: str = f"""void main() {{\n{'\t'*4}const float PI = 3.14159;\n}}"""
PARA5: str = """Toute tentative de modification d'une constante entraînera une erreur de compilation."""
PARA6: str = """La portée d'une variable définit où elle peut être utilisée. En C, il existe trois types principaux de portée :"""
PARA7: str = """La variable est définie dans une fonction et n'est accessible que dans cette fonction."""
PARA8: str = """La variable est définie en dehors de toute fonction et peut être utilisée partout dans le programme."""
PARA9: str = """La variable conserve sa valeur même après la fin de l'exécution de la fonction."""
EXEMPLE4: str = f"""int globale = 100;\n\nvoid fonction() {{\n{'\t\t'*3}int locale = 10;\n{'\t\t'*3}static int statique = 5;\n{'\t\t'*3}statique++;\n}}\n\nvoid main(){{}}"""
EXEMPLE5: str = f"""void main() {{\n{'\t'*4}int score = 0;\n{'\t'*4}score = 10;\n{'\t'*4}score += 5;\n}}"""
CONCLUSION: str = """Les variables sont essentielles en C car elles permettent de stocker et manipuler des données. Il est important de choisir le bon type pour optimiser l'utilisation de la mémoire et garantir l'exactitude des calculs."""

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
                GrandTitre(text='Variables'),
                Spacing(),
                Titre("Introduction"),
                Spacing(),
                Texte(INTRO),
                Texte(INTRO2),
                Texte(INTRO3),
                Spacing(),
                Titre("1- Déclaration et Initialisation d'une Variable"),
                Spacing(),
                Texte(PARA1),
                Syntaxe(page, content=SYNTAXE1),
                Exemple(page, enonce='', code=Code(EXEMPLE1, 8), height=520),
                Spacing(),
                Titre("2- Types de Variables en C"),
                Spacing(),
                Texte(PARA2),
                Spacing(),
                Table(TABLEAU),
                Spacing(),
                Titre("3- Les Variables et la Mémoire"),
                Spacing(),
                Texte(PARA3),
                Exemple(page, 530, '', Code(EXEMPLE2, 7)),
                Spacing(),
                Titre("4- Les Variables Constantes"),
                Spacing(),
                Texte(PARA4),
                Exemple(page, 380, '', Code(EXEMPLE3, 3)),
                Spacing(20),
                Texte(PARA5),
                Spacing(),
                Titre("5- Portée des Variables"),
                Spacing(),
                Texte(PARA6),
                Spacing(20), Point('Locale'), Spacing(10), Texte(PARA7),
                Spacing(20), Point('Globale'), Spacing(10), Texte(PARA8),
                Spacing(20), Point('Statique (static)'), Spacing(10), Texte(PARA9),
                Exemple(page, 500, '', Code(EXEMPLE4, 7)),
                Spacing(),
                Titre('6- Modification des Variables'),
                Spacing(),
                Texte("Une variable peut être modifiée après sa déclaration en utilisant des opérateurs:"),
                Exemple(page, 450, '', Code(EXEMPLE5, 5)),
                Spacing(),
                Titre('Conclusion'),
                Spacing(),
                Texte(CONCLUSION),
                Spacing(),
            ]
        )