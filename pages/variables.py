from flet import Container, padding, Page, ListView, Row
from modules.fonctions import pourcentage
from modules.syntaxe import Syntaxe
from modules.title import Titre
from modules.texte import Texte, Spacing
from modules.exemple import Exemple
from modules.code import Code
from modules.point import Point

INTRO: str = """En langage C, une variable est un espace mémoire réservé permettant de stocker des données. Les variables jouent un rôle fondamental en programmation, car elles permettent de manipuler des informations dynamiquement au cours de l'exécution d'un programme."""
INTRO2: str = """Chaque variable en C possède un type (int, float, char, etc.), qui définit la nature des données qu'elle peut contenir, ainsi qu'un nom qui permet d'y accéder. Avant d'utiliser une variable, il est nécessaire de la déclarer, et dans certains cas, de l'initialiser avec une valeur par défaut."""
INTRO3: str = """L'utilisation efficace des variables est essentielle pour écrire des programmes optimisés et compréhensibles. Dans la suite, nous explorerons les différents types de variables, leur déclaration, leur portée et leur durée de vie en langage C."""

PARA1: str = """Avant d'utiliser une variable, il faut la déclarer en précisant son type. Voici la syntaxe de base :"""
SYNTAXE1: str = """<type> nom_variable;\nou\n<type> nom_variable = <valeur>;"""
EXEMPLE1: str = """int number;\nint age = 19;\nfloat prix = 12.5;\nhar lettre = 'A';"""
INT: str = f"""Nombre Entier: (1, 2, 4){'\t\t'*3}Taile: 2 ou 4 octets"""
CHAR: str = f"""Caractere: ('r, '2', '$'){'\t\t'*3}Taile: 1 octet"""
SHORT_INT: str = f"""Entier de petite taile: ('0, '1', '4'){'\t\t'*3}Taile: 2 octets"""
VOID: str = f"""Aucune valeur{'\t\t'*3}Taile: 0 octet"""
LONG: str = f"""Entier de grande taille{'\t\t'*3}Taile: 4 octets"""
LONG_LONG: str = f"""Entier de  tres grande taille{'\t\t'*3}Taile: 8 octets"""
FLOAT: str = f"""Reels: (1, 0.3, -23.5){'\t\t'*3}Taile: 4 octets"""
DOUBLE: str = f"""Reels de grande taille{'\t\t'*3}Taile: 8 octets"""
LONG_DOUBLE: str = f"""Reels de tres grande taille{'\t\t'*3}Taile: 10 octets"""

PARA2: str = """Le langage C propose plusieurs types de variables :"""
PARA3: str = """Chaque variable est stockée à une adresse mémoire spécifique. On peut afficher cette adresse avec l'opérateur & et la fonction printf :"""
EXEMPLE2: str = """int nombre = 10;\nprintf("Adresse mémoire de nombre : %p", &nombre);\n"""
PARA4: str = """Une variable constante est une variable dont la valeur ne peut pas être modifiée après l'initialisation. On utilise le mot-clé const :"""
EXEMPLE3: str = """const float PI = 3.14159;"""
PARA5: str = """Toute tentative de modification d'une constante entraînera une erreur de compilation."""
PARA6: str = """La portée d'une variable définit où elle peut être utilisée. En C, il existe trois types principaux de portée :"""
PARA7: str = """La variable est définie dans une fonction et n'est accessible que dans cette fonction."""
PARA8: str = """La variable est définie en dehors de toute fonction et peut être utilisée partout dans le programme."""
PARA9: str = """La variable conserve sa valeur même après la fin de l'exécution de la fonction."""
EXEMPLE4: str = f"""int globale = 100;\n\nvoid fonction() {{\n{'\t\t'*3}int locale = 10;\n{'\t\t'*3}static int statique = 5;\n{'\t\t'*3}statique++;\n}}"""
EXEMPLE5: str = """int score = 0;\nscore = 10;\nscore += 5;"""
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
                Exemple(page, enonce='', code=Code(EXEMPLE1, 4), height=430),
                Spacing(),
                Titre("2- Types de Variables en C"),
                Texte(PARA2),
                Spacing(20), Point('void'), Texte(VOID),
                Spacing(20), Point('char'), Texte(CHAR),
                Spacing(20), Point('short int'), Texte(SHORT_INT),
                Spacing(20), Point('int'), Texte(INT),
                Spacing(20), Point('long'), Texte(LONG),
                Spacing(20), Point('long long'), Texte(LONG_LONG),
                Spacing(20), Point('float'), Texte(FLOAT),
                Spacing(20), Point('double'), Texte(DOUBLE),
                Spacing(20), Point('long double'), Texte(LONG_DOUBLE),
                Spacing(),
                Titre("3- Les Variables et la Mémoire"),
                Spacing(),
                Texte(PARA3),
                Exemple(page, 420, '', Code(EXEMPLE2, 3)),
                Spacing(),
                Titre("4- Les Variables Constantes"),
                Spacing(),
                Texte(PARA4),
                Exemple(page, 380, '', Code(EXEMPLE3, 1)),
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
                Exemple(page, 400, '', Code(EXEMPLE5, 3)),
                Spacing(),
                Titre('Conclusion'),
                Spacing(),
                Texte(CONCLUSION),
                Spacing(),
            ]
        )