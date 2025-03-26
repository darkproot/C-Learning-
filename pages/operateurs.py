from flet import Container, padding, Page, ListView
from modules.fonctions import pourcentage
from modules.title import Titre, GrandTitre
from modules.texte import Texte, Spacing
from modules.tableau import Table
from modules.exemple import Exemple
from modules.code import Code

# Liste de tous les tableau
TABLEAU1: list[list[str]] = [
    ['Opérateur', 'Description', 'Exemple', 'Résultat'],
    ['+', 'Addition', 'a + b', 'Somme de a et b'],
    ['-', 'Soustraction', 'a - b', 'Soustration de a et b'],
    ['*', 'Multiplication', 'a * b', 'Produit de a et b'],
    ['/', 'Division', 'a / b', 'Quotient de a par b (entier s\'ils le sont tous les deux)'],
    ['%', 'Modulo', 'a % b', 'Reste de la division entiere de a par b'],
]
TABLEAU2: list[list[str]] = [
    ['Opérateur', 'Description', 'Exemple', 'Résultat'],
    ['==', 'Egale a', 'a == b', '1 si a est egale a b sinon 0'],
    ['!=', 'Différent de a', 'a != b', '1 si a est différent a b sinon 0'],
    ['>', 'Supérieur a', 'a > b', '1 si a est strictement supérieur a b sinon 0'],
    ['<', 'Inférieure a', 'a < b', '1 si a est strictement inférieure a b sinon 0'],
    ['>=', 'Supérieur ou égale', 'a >= b', '1 si a est supérieur ou égale a b sinon 0'],
    ['<=', 'Inférieure ou égale', 'a <= b', '1 si a est inférieure ou égale a b sinon 0'],
]
TABLEAU3: list[list[str]] = [
    ['Opérateur', 'Description', 'Exemple', 'Résultat'],
    ['&&', 'ET logique', '(a > 0) && (b < 0)', '1 si les deux conditions sont vraies, sinon 0'],
    ['||', 'OU logique', '(a > 0) || (b < 0)', '1 si au moins une des deux conditions est vraies, sinon 0'],
    ['!', 'NON logique', '!(a > 0)', 'Inverse la valeur logique'],
]
TABLEAU4: list[list[str]] = [
    ['Opérateur', 'Description', 'Exemple', 'Résultat'],
    ['=', 'Affectation', 'a = 5', 'a prend la valeur 5'],
    ['+=', 'Addition avec affectation', 'a += 3', 'a = a + 3'],
    ['-=', 'Soustraction avec affectation', 'a -= 2', 'a = a - 2'],
    ['*=', 'Multiplication avec affectation', 'a *= 4', 'a = a * 4'],
    ['/=', 'Division avec affectation', 'a /= 2', 'a = a / 2'],
    ['%=', 'Modulo avec affectation', 'a %= 3', 'a = a % 3'],
]
TABLEAU5: list[list[str]] = [
    ['Opérateur', 'Description', 'Exemple', 'Résultat'],
    ['++', 'Incrémentation', 'a++ ou ++a', 'Ajoute 1 a a'],
    ['--', 'Décrémentation', 'a-- ou --a', 'Soustrait 1 a a'],
]
TABLEAU6: list[list[str]] = [
    ['Opérateur', 'Description', 'Exemple', 'Résultat'],
    ['&', 'ET bit-a-bit', '23 & 4', '...'],
    ['|', 'OU bit-a-bit', '23 | 4', '...'],
    ['^', 'OU exclusif (XOR)', '23 ^ 4', '...'],
    ['~', 'NON bit-a-bit (complément)', '~6', '...'],
    ['<<', 'Décalage a gauche', '5 << 2', '...'],
    ['>>', 'Décalage a droite', '5 >> 2', '...'],
]

INTRO: str = """En langage C, les opérateurs sont des symboles qui permettent d'effectuer des opérations sur des variables et des valeurs. Ils sont essentiels pour écrire des programmes fonctionnels et efficaces."""

PARA1: str = """Ces opérateurs permettent d'effectuer des calculs mathématiques de base."""
EXEMPLE1: str = r"""#include <stdio.h>

void main() {
    int a = 10, b = 3;
    printf("Addition: %d\n", a + b);
    printf("Soustraction: %d\n", a - b);
    printf("Multiplication: %d\n", a * b);
    printf("Division: %d\n", a / b);
    printf("Modulo: %d", a % b);
}
"""
PARA2: str = """Ils permettent de comparer deux valeurs et retournent un résultat booléen (1 pour vrai, 0 pour faux)"""
EXEMPLE2: str = r"""#include <stdio.h>

void main() {
    int a = 5, b = 10;
    printf("a == b: %d\n", a == b);
    printf("a != b: %d\n", a != b);
    printf("a > b: %d\n", a > b);
    printf("a < b: %d", a < b);
}
"""
EXEMPLE3: str = r"""#include <stdio.h>

void main() {
    int a = 5, b = 10;
    printf("(a > 0) && (b > 0) => %d\n", (a > 0) && (b > 0));
    printf("(a > 10) || (b > 10) => %d\n", (a > 10) || (b > 10));
    printf("!(a > 0) => %d ", !(a > 0));
}
"""
EXEMPLE4: str = r"""#include <stdio.h>

void main() {
    int a = 10;
    a += 5;
    printf("a += 5: %d\n", a);
    a *= 2;
    printf("a *= 2: %d", a);
}
"""
CONCLUSION1: str = """Les opérateurs sont des éléments fondamentaux du langage C. Ils permettent d'effectuer des calculs, des comparaisons et des opérations logiques essentielles au bon fonctionnement d'un programme. En maîtrisant les opérateurs arithmétiques, de comparaison, logiques, d'affectation et binaires, on peut écrire du code plus concis et efficace."""
CONCLUSION2: str = """Cependant, les opérateurs seuls ne suffisent pas pour structurer un programme de manière logique. Pour prendre des décisions et exécuter certaines instructions sous certaines conditions, nous avons besoin d'outils de contrôle du flux d'exécution."""

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
                GrandTitre(text="Opérateurs"), Spacing(),
                Titre('Introduction'),
                Spacing(), Texte(INTRO),
                Spacing(), Titre("1- Les opérateurs arithmétiques"),
                Spacing(), Texte(PARA1),
                Spacing(), Table(TABLEAU1),
                Spacing(), Exemple(page, 570, enonce='', code=Code(EXEMPLE1, 11)),
                Spacing(), Titre("2- Les opérateurs de comparaison"),
                Spacing(), Texte(PARA2),
                Spacing(), Table(TABLEAU2),
                Spacing(), Exemple(page, 580, '', Code(EXEMPLE2, 10)),
                Spacing(), Titre("3- Les opérateurs logiques"),
                Spacing(), Texte('Ils sont utilisés pour combiner plusieurs conditions.'),
                Spacing(), Table(TABLEAU3),
                Spacing(), Exemple(page, 550, '', Code(EXEMPLE3, 9)),
                Spacing(), Titre('4- Les opérateurs d\'affectation'),
                Spacing(), Texte("Ces opérateurs permettent d'assigner des valeurs aux variables."),
                Spacing(), Table(TABLEAU4),
                Spacing(), Exemple(page, 530, '', Code(EXEMPLE4, 10)),
                Spacing(), Titre("Conclusion"),
                Spacing(), 
                Texte(CONCLUSION1),
                Texte(CONCLUSION2),
                Spacing(), 
            ]
        )