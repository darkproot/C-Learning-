from flet import Container, padding, Page, ListView
from modules.fonctions import pourcentage
from modules.color import DEEP_BLUE
from modules.exemple import Exemple
from modules.code import Code
from modules.syntaxe import Syntaxe
from modules.texte import Texte, Spacing
from modules.title import Titre
from modules.point import Point

INTRO: str = """Le langage C est un langage de programmation impératif qui repose sur des structures de contrôle permettant de diriger le flux d'exécution d'un programme. Ces structures de contrôle sont essentielles pour la prise de décision, la répétition d'instructions et la gestion du flux du programme."""
INTRO2: str = """Dans cette section, nous allons étudier trois grandes catégories de structures de contrôle en C: """

PARA1: str = """Les structures conditionnelles permettent d'exécuter certaines instructions en fonction de conditions spécifiques."""
PARA2: str = """La structure if permet d\'exécuter un bloc d\'instructions uniquement si une condition est vraie."""
SYNTAXE1: str = """
if (condition) {
    // Instructions exécutées si la condition est vraie
}
"""
EXEMPLE1: str = """#include <stdio.h>

int main() {
    int age = 20;
    if (age >= 18) {
        printf("Vous êtes majeur.");
    }
    return 0;
}
"""
PARA3: str = """Elle permet d'exécuter un bloc d'instructions si la condition est vraie et un autre bloc si elle est fausse."""
PARA4: str = """Permet de tester plusieurs conditions successives."""
SYNTAXE2: str = """
if (condition) {
    // Instructions si la condition est vraie
} else {
    // Instructions si la condition est fausse
}
"""
EXEMPLE2: str = """#include <stdio.h>

int main() {
    int nombre = 10;
    if (nombre % 2 == 0) {
        printf("Le nombre est pair.");
    } else {
        printf("Le nombre est impair.");
    }
    return 0;
}
"""
PARA5: str = """Elle permet de tester une variable contre plusieurs valeurs possibles."""
SYNTAXE3: str = """
if (condition1) {
    // Instructions si condition1 est vraie
} else if (condition2) {
    // Instructions si condition2 est vraie
} else {
    // Instructions si aucune condition n'est vraie
}
"""
EXEMPLE3: str = """#include <stdio.h>

int main() {
    int note = 75;
    if (note >= 90) {
        printf("Excellent");
    } else if (note >= 75) {
        printf("Très bien");
    } else if (note >= 50) {
        printf("Passable");
    } else {
        printf("Échec");
    }
    return 0;
}
"""
SYNTAXE4: str = """
switch (expression) {
    case valeur1:
        // Instructions
        break;
    case valeur2:
        // Instructions
        break;
    default:
        // Instructions si aucune valeur ne correspond
}
"""
EXEMPLE4: str = """#include <stdio.h>

void main() {
    int jour = 3;
    switch (jour) {
        case 1:
            printf("Lundi");
            break;
        case 2:
            printf("Mardi");
            break;
        case 3:
            printf("Mercredi");
            break;
        default:
            printf("Jour inconnu");
    }
}
"""
PARA6: str = """Les boucles permettent de répéter des instructions un certain nombre de fois."""
PARA7: str = """La boucle while exécute un bloc tant qu'une condition est vraie."""
SYNTAXE5: str = """
while (condition) {
    // Instructions exécutées tant que la condition est vraie
}
"""
PARA8: str = """Elle garantit l'exécution du bloc au moins une fois, puis continue tant que la condition est vraie."""
EXEMPLE5: str = """#include <stdio.h>

int main() {
    int i = 1;
    while (i <= 5) {
        printf("Iteration %d -> ", i);
        i++;
    }
}
"""
SYNTAXE6: str = """
do {
    // Instructions exécutées au moins une fois
} while (condition);
"""
EXEMPLE6: str = """#include <stdio.h>

void main() {
    int i = 1;
    do {
        printf("Iteration %d -> ", i);
        i++;
    } while (i <= 5);
}
"""
PARA9: str = """Elle permet d'exécuter un bloc un certain nombre de fois en contrôlant l'initialisation, la condition et l'incrémentation en une seule ligne."""
SYNTAXE7: str = """
for (initialisation; condition; mise à jour) {
    // Instructions répétées
}
"""
EXEMPLE7: str = """#include <stdio.h>

void main() {
    for (int i = 1; i <= 5; i++) {
        printf("Iteration %d -> ", i);
    }
}
"""
PARA10: str = """Elle permet de sortir immédiatement d'une boucle ou d'un switch."""
EXEMPLE8: str = """#include <stdio.h>

void main() {
    for (int i = 1; i <= 10; i++) {
        if (i == 5) {
            break; // Arrête la boucle dès que i vaut 5
        }
        printf("%d -> ", i);
    }
}
"""
PARA11: str = """Elle permet de sauter l'itération courante et passer à la suivante."""
EXEMPLE9: str = """#include <stdio.h>

void main() {
    for (int i = 1; i <= 5; i++) {
        if (i == 3) {
            continue; // Ignore le reste du code pour i == 3
        }
        printf("%d -> ", i);
    }
}
"""
PARA12: str = """Elle permet de quitter une fonction et retourner une valeur."""
EXEMPLE10: str = """#include <stdio.h>

int carre(int n) {
    return n * n; // Retourne le carré de n
}

int main() {
    printf("Le carré de 4 est %d", carre(4));
    return 0;
}
"""
PARA13: str = """Elle permet de sauter directement à une étiquette, mais peut rendre le code difficile à lire."""
EXEMPLE11: str = """#include <stdio.h>

int main() {
    printf("Début -> ");
    goto fin;
    printf("Ce message ne s'affichera pas -> ");

fin:
    printf("Fin du programme.");
    return 0;
}
"""
CONCLUSION1: str = """Les structures de contrôle sont indispensables en C pour diriger l'exécution d'un programme. Les conditions (if, switch), les boucles (while, for, do-while) et les instructions de saut (break, continue, return, goto) permettent de rendre un programme dynamique et interactif."""
CONCLUSION2: str = """Si tu veux approfondir, tu peux essayer d’écrire des programmes combinant ces structures pour résoudre des problèmes concrets !"""

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
                Titre('Introduction'),
                Spacing(), Texte(INTRO), Texte(INTRO2),
                Spacing(), Titre("1- Les structures conditionnelles"),
                Spacing(), Texte(PARA1),
                Spacing(), Point('1.1- La structure if'),
                Spacing(), Texte(PARA2),
                Spacing(), Syntaxe(page, content=SYNTAXE1, font_size=15),
                Spacing(), Exemple(page, 530, '', Code(EXEMPLE1, 10)),
                Spacing(), Point('1.2- La structure if-else'),
                Spacing(), Texte(PARA3),
                Spacing(), Syntaxe(page, 250,content=SYNTAXE2, font_size=15),
                Spacing(), Exemple(page, 570, '', Code(EXEMPLE2, 12)),
                Spacing(), Point('1.3- La structure if-else if-else'),
                Spacing(), Texte(PARA4),
                Spacing(), Syntaxe(page, 290,content=SYNTAXE3, font_size=15),
                Spacing(), Exemple(page, 670, '', Code(EXEMPLE3, 16)),
                Spacing(), Point('1.4 La structure switch'),
                Spacing(), Texte(PARA5),
                Spacing(), Syntaxe(page, 300,content=SYNTAXE4, font_size=15),
                Spacing(), Exemple(page, 720, '', Code(EXEMPLE4, 19)),
                Spacing(), Titre('2- Les structures itératives (boucles)'),
                Spacing(), Texte(PARA6),
                Spacing(), Point('2.1- La boucle while'),
                Spacing(), Texte(PARA7),
                Spacing(), Syntaxe(page, 200,content=SYNTAXE5, font_size=15),
                Spacing(), Exemple(page, 550, '', Code(EXEMPLE5, 10)),
                Spacing(), Point('2.2- La boucle do-while'),
                Spacing(), Texte(PARA8),
                Spacing(), Syntaxe(page, 200,content=SYNTAXE6, font_size=15),
                Spacing(), Exemple(page, 550, '', Code(EXEMPLE6, 10)),
                Spacing(), Point('2.3 La boucle for'),
                Spacing(), Texte(PARA9),
                Spacing(), Syntaxe(page, 170,content=SYNTAXE7, font_size=15),
                Spacing(), Exemple(page, 550, '', Code(EXEMPLE7, 8)),
                Spacing(), Titre('3- Les structures de saut'),
                Spacing(), Point('3.1- L\'instruction break'),
                Spacing(), Texte(PARA10),
                Spacing(), Exemple(page, 550, '', Code(EXEMPLE8, 11)),
                Spacing(), Point('3.2- L\'instruction continue'),
                Spacing(), Texte(PARA11),
                Spacing(), Exemple(page, 570, '', Code(EXEMPLE9, 12)),
                Spacing(), Point('3.3- L\'instruction return'),
                Spacing(), Texte(PARA12),
                Spacing(), Exemple(page, 570, '', Code(EXEMPLE10, 12)),
                Spacing(), Point('3.4 L\'instruction goto (déconseillée)'),
                Spacing(), Texte(PARA13),
                Spacing(), Exemple(page, 570, '', Code(EXEMPLE11, 12)),
                Spacing(), Titre('Conclusion'),
                Spacing(), Texte(CONCLUSION1), Texte(CONCLUSION2),
                Spacing()
            ]
        )