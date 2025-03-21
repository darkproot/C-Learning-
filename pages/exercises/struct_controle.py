from flet import Container, ListView, Page, padding
from modules.fonctions import pourcentage
from modules.qcm import Qcm
from modules.title import Titre, GrandTitre
from modules.texte import Spacing
from modules.point import Point
from modules.code import ExerciceCode, MiniCode

MINICODE1: str = r"""int i = 0;
while (i < 3) {
    printf("%d ", i);
    i++;
}"""
MINICODE2: str = r"""int i = 0;
do {
    printf("%d ", i);
    i++;
} while (i < 3);"""
MINICODE3: str = r"""int i = 0;
while (i < 5);
{
    printf("%d ", i);
    i++;
}"""

CODE1: str = """\
#include <stdio.h>

void main() {
    const short BASE = 7;
}"""
SOLUTION1: str = r"""#include <stdio.h>

void main() {
    const short BASE = 7;
    for (short i = 0; i < 13; i++){
        printf("%d x %d = %d\n", i, BASE, BASE*i);
    }
}"""
CODE2: str = """\
#include <stdio.h>

void main() {
    const short NOMBRE = -31;
}"""
SOLUTION2: str = r"""#include <stdio.h>

void main() {
    const short NOMBRE = -31;
    if (NOMBRE < 0) printf("%d est négatif et ", NOMBRE);
    else if (NOMBRE > 0) printf("%d est positif et ", NOMBRE);
    else printf("%d est nul et");
    
    if (NOMBRE % 2 == 0) printf("paire.\n");
    else printf("impaire.\n");
}"""
CODE3: str = """\
#include <stdio.h>

void main() {
    const short NOMBRE = 10;
}"""
SOLUTION3: str = r"""#include <stdio.h>

void main() {
    const short NOMBRE = 10;
    short i = 1;
    while (i < 10) {
        if (i % 2 == 0)
            printf("%d\n", i);
        i++;
    }
}"""

QCM1: dict[str, str] = {
    'question_id': 1,
    'question': "Quelle est la structure de contrôle utilisée pour exécuter un bloc de code sous une condition donnée ?",
    'proposition': ["for", "if", "while", "switch"],
    'reponse': 1,
}
QCM2: dict[str, str] = {
    'question_id': 2,
    'question': "Quelle est la syntaxe correcte d'une boucle for en C ?",
    'proposition': ["for (i = 0; i < 10; i++) { ... }", "for i = 0; i < 10; i++ { ... }", "loop (i = 0; i < 10; i++) { ... }", "for (i < 10; i++) { ... }"],
    'reponse': 0,
}
QCM3: dict[str, str] = {
    'question_id': 3,
    'question': "Quelle instruction permet d'arrêter une boucle prématurément ?",
    'proposition': ["continue", "exit()", "break", "return"],
    'reponse': 2,
}
QCM4: dict[str, str] = {
    'question_id': 4,
    'question': "Quelle est la sortie du code suivant ?",
    'proposition': ["0 1 2", "1 2 3", "0 1 2 3", "0 0 0"],
    'reponse': 0,
    'minicode': MiniCode(MINICODE1),
}
QCM5: dict[str, str] = {
    'question_id': 5,
    'question': "Quel mot-clé est utilisé pour tester plusieurs valeurs d'une même variable ?",
    'proposition': ["if", "switch", "while", "goto"],
    'reponse': 1,
}
QCM6: dict[str, str] = {
    'question_id': 6,
    'question': "Quel sera l'effet de l'instruction continue dans une boucle ?",
    'proposition': ["Elle met fin à la boucle immédiatement.", "Elle redémarre la boucle depuis le début", "Elle saute à l'itération suivante de la boucle.", "Elle affiche une erreur."],
    'reponse': 2,
}
QCM7: dict[str, str] = {
    'question_id': 7,
    'question': "Quelle est la condition de sortie de la boucle do...while ?",
    'proposition': ["Une condition initiale", "Une condition en début de boucle", "Une condition en fin de boucle", "Il n'y a pas de condition"],
    'reponse': 2,
}
QCM8: dict[str, str] = {
    'question_id': 8,
    'question': "Que fait l'instruction goto en C ?",
    'proposition': ["Elle arrête l'exécution du programme.", "Elle saute à une étiquette spécifiée.", "Elle remplace les boucles for.", "Elle est utilisée pour définir des fonctions."],
    'reponse': 1,
}
QCM9: dict[str, str] = {
    'question_id': 9,
    'question': "Quelle est la sortie du programme suivant ?",
    'proposition': ["0 1 2", "1 2 3", "0 1 2 3", "0 0 0"],
    'reponse': 0,
    'minicode': MiniCode(MINICODE2),
}
QCM10: dict[str, str] = {
    'question_id': 10,
    'question': "Quel est le problème avec cette boucle while ?",
    'proposition': ["Il manque une condition de sortie.", "La variable i doit être initialisée avant la boucle.", "Le point-virgule après while empêche la boucle de s'exécuter correctement.", "Il n'y a pas de problème."],
    'reponse': 2,
    'minicode': MiniCode(MINICODE3),
}

EXERCICE1: dict[str, str] = {
    'text': "Ecrire un programme qui affiche les 12 premiers éléments de la table de multiplication par 7.",
    'code': CODE1,
    'solution': SOLUTION1,
}
EXERCICE2: dict[str, str] = {
    'text': "Ecrire un programme qui determine le signe et la parité d'un nombre.",
    'code': CODE2,
    'solution': SOLUTION2,
}
EXERCICE3: dict[str, str] = {
    'text': "Ecrire un programme qui affiche tous les nombres paire entre 0 et 10.",
    'code': CODE3,
    'solution': SOLUTION3,
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
                GrandTitre(text="Structures de contrôle", font_size=30), Spacing(),
                Titre('Question a choix multiple'),
                Spacing(),
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
                Spacing(),
                Titre('Question a reponse ouverte'),
                Spacing(),
                Point('Exercice 1'),
                Spacing(), ExerciceCode(**EXERCICE1),
                Spacing(),
                Point('Exercice 2'),
                Spacing(), ExerciceCode(**EXERCICE2),
                Spacing(),
                Point('Exercice 3'),
                Spacing(), ExerciceCode(**EXERCICE3),
                Spacing(),
            ]
        )