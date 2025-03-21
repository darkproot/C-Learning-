from flet import Container, padding, Page, ListView
from modules.fonctions import pourcentage
from modules.code import Code
from modules.syntaxe import Syntaxe
from modules.exemple import Exemple
from modules.texte import Texte, Spacing
from modules.title import Titre, GrandTitre
from modules.point import Point

INTRO: str = """Les pointeurs sont l'un des concepts fondamentaux et puissants du langage C. Ils permettent de manipuler directement la mémoire, ce qui rend le langage très efficace."""
PARAM1: str = """Un pointeur est une variable qui stocke l'adresse mémoire d'une autre variable. Plutôt que de stocker une valeur comme un entier ou un caractère, un pointeur stocke une adresse."""
PARAM2: str = """La déclaration d'un pointeur se fait comme suit :"""
SYNTAXE1: str = """<type> *nom_du_pointeur;"""
PARAM3: str = """\
type : type de données pointé (int, char, float, etc.).
* : indique qu'il s'agit d'un pointeur.
nom_du_pointeur : nom de la variable pointeur.
"""
EXEMPLE1: str = """\
void main() {
    int *p;   // Pointeur vers un entier
    char *c;  // Pointeur vers un caractère
    float *f; // Pointeur vers un flottant
}
"""
PARAM4: str = """L'opérateur & permet d'obtenir l'adresse mémoire d'une variable."""
EXEMPLE2: str = """\
#include <stdio.h>

int main() {
    int a = 10;
    printf("Valeur de a : %d => ", a);
    printf("Adresse de a : %p ", &a); // %p pour afficher une adresse mémoire
    return 0;
}
"""
PARAM5: str = """L'opérateur * (appelé opérateur de déréférencement) permet d'accéder à la valeur stockée à une adresse mémoire."""
EXEMPLE3: str = """\
#include <stdio.h>

int main() {
    int a = 10;
    int *p = &a;  // Pointeur qui stocke l'adresse de a
    printf("Adresse de a : %p => ", p);
    printf("Valeur de a via pointeur : %d", *p); // Déférencement
    return 0;
}"""
PARAM6: str = """On peut modifier la valeur d'une variable à travers un pointeur."""
EXEMPLE4: str = """\
#include <stdio.h>

int main() {
    int a = 10;
    int *p = &a;
    *p = 20; // Modification de la valeur de a via le pointeur
    printf("Nouvelle valeur de a : %d", a); 
    return 0;
}"""
PARAM7: str = """Un tableau en C est un pointeur constant vers son premier élément."""
EXEMPLE5: str = """\
#include <stdio.h>

void main() {
    int tab[3] = {10, 20, 30};
    int *p = tab; // tab est déjà un pointeur vers le premier élément
    printf("Premier élément : %d -> ", *p);
    printf("Deuxième élément : %d -> ", *(p + 1));
    printf("Troisième élément : %d", *(p + 2));
}"""
PARAM8: str = """L'allocation dynamique permet de réserver de la mémoire à l'exécution avec malloc() et free()."""
EXEMPLE6: str = """\
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *p = (int*) malloc(sizeof(int)); // Allocation de mémoire pour un entier
    if (p == NULL) {
        printf("Échec de l'allocation mémoire");
        return 1;
    }
    *p = 42;
    printf("Valeur stockée : %d ", *p);
    free(p); // Libération de la mémoire
    return 0;
}"""
PARAM9: str = """Un pointeur peut aussi stocker l'adresse d'un autre pointeur."""
EXEMPLE7: str = """\
#include <stdio.h>

void main() {
    int a = 10;
    int *p = &a;
    int **pp = &p; // Pointeur vers un pointeur
    printf("Valeur de a : %d", **pp);
}"""
PARAM10: str = """On peut passer des pointeurs en argument à une fonction."""
EXEMPLE8: str = """\
#include <stdio.h>

void modifier(int *p) {
    *p = 20; // Modification de la valeur pointée
}

void main() {
    int a = 10;
    printf("Avant : %d => ", a);
    modifier(&a);
    printf("Après : %d", a);
}"""
CONCLUSION1: str = """Les pointeurs sont essentiels en C pour la gestion efficace de la mémoire et la manipulation des structures complexes comme les tableaux et les structures. Ils sont également utilisés pour l'allocation dynamique et la gestion des chaînes de caractères."""
CONCLUSION2: str = """Si tu veux approfondir un aspect particulier (pointeurs sur structures, pointeurs fonctionnels, etc.), dis-moi !"""

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
                GrandTitre(text="Pointeurs"), Spacing(),
                Titre('Pointeur'),
                Spacing(), Texte(INTRO),
                Spacing(), Titre('1- Introduction aux Pointeurs'),
                Spacing(), Texte(PARAM1),
                Spacing(), Point('Déclaration d\'un pointeur'),
                Spacing(), Texte(PARAM2),
                Syntaxe(page, 150, content=SYNTAXE1),
                Spacing(), Texte(PARAM3),
                Exemple(page, 480, '', Code(EXEMPLE1, 6)),
                Spacing(), Titre('2- Adresse et Opérateur &'),
                Spacing(), Texte(PARAM4),
                Exemple(page, 500, '', Code(EXEMPLE2, 9)),
                Spacing(), Titre('3- Déférencement et Opérateur *'),
                Spacing(), Texte(PARAM5),
                Exemple(page, 520, '', Code(EXEMPLE3, 9)),
                Spacing(), Titre('4- Modification d\'une variable via un pointeur'),
                Spacing(), Texte(PARAM6),
                Exemple(page, 520, '', Code(EXEMPLE4, 9)),
                Spacing(), Titre('5- Pointeurs et Tableaux'),
                Spacing(), Texte(PARAM7),
                Exemple(page, 520, '', Code(EXEMPLE5, 9)),
                Spacing(), Titre('6- Pointeurs et Allocation Dynamique'),
                Spacing(), Texte(PARAM8),
                Exemple(page, 640, '', Code(EXEMPLE6, 15)),
                Spacing(), Titre('7- Pointeur vers Pointeur'),
                Spacing(), Texte(PARAM9),
                Exemple(page, 480, '', Code(EXEMPLE7, 8)),
                Spacing(), Titre('8. Pointeurs et Fonctions'),
                Spacing(), Texte(PARAM10),
                Exemple(page, 580, '', Code(EXEMPLE8, 12)),
                Spacing(), Titre('Conclusion'),
                Spacing(), Texte(CONCLUSION1), Texte(CONCLUSION2),
            ]
        )