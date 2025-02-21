from flet import Container, padding, Page, ListView
from modules.fonctions import pourcentage
from modules.code import Code
from modules.texte import Spacing, Texte
from modules.title import Titre
from modules.point import Point
from modules.syntaxe import Syntaxe
from modules.exemple import Exemple

INTRO1: str = """En programmation, une structure de données est une manière d'organiser, de stocker et de manipuler les données efficacement. En langage C, les structures de données sont essentielles pour gérer des informations de manière optimisée."""
INTRO2: str = """C est un langage de bas niveau qui offre un contrôle direct sur la mémoire, ce qui permet d'implémenter des structures de données de manière efficace. Comprendre les structures de données en C est fondamental pour améliorer la performance des algorithmes et des programmes."""

PARA1: str = """Un tableau est une structure de données qui stocke plusieurs éléments de même type dans un espace contigu de la mémoire."""
SYNTAXE1: str = """<type> nom_tab[<taille>];\nou\n<type> nom_tab[<taille>] = {initialisation};"""
EXEMPLE1: str = """#include <stdio.h>

int main() {
    int tab[5] = {1, 2, 3, 4, 5}; // Déclaration et initialisation 
    printf("Premier élément : %d", tab[0]); // Accès au premier élément
    return 0;
}"""
PARA2: str = """Avantages : Accès rapide aux éléments via l'index."""
PARA3: str = """Inconvénients : Taille fixe, coûteux en insertion/suppression d'éléments."""
PARA4: str = """Une structure permet de regrouper différentes variables de types différents sous un même nom."""
SYNTAXE2: str = """
struct nom_structure {
    type_1 membre_1;
    type_2 membre_2;
    ...
    type_n membre_n;
};
"""
EXEMPLE2: str = """#include <stdio.h>

struct Etudiant {
    char nom[50];
    int age;
    float moyenne;
};

int main() {
    struct Etudiant e1 = {"Jean", 20, 14.5};
    printf("Nom : %s, Âge : %d, Moyenne : %.2f", e1.nom, e1.age, e1.moyenne);
    return 0;
}"""
PARA5: str = """Avantages : Permet de gérer des données complexes sous un même bloc"""
PARA6: str = """Inconvénients : Accès aux champs plus lent qu'un tableau."""
PARA7: str = """Un tableau multidimensionnel est une extension du tableau simple où chaque élément peut être lui-même un tableau. Le plus utilisé est le tableau à deux dimensions, qui peut être vu comme une matrice."""
EXEMPLE3: str = """#include <stdio.h>

void main() {
    int matrice[3][3] = {
        {1, 2, 3}, 
        {4, 5, 6}, 
        {7, 8, 9}
    };
    printf("Élément en (1,2) : %d", matrice[1][2]); // Affiche 6
}"""
PARA8: str = """L'accès aux éléments se fait via deux indices :"""
PARA9: str = """ matrice[i][j] accède à l'élément situé à la ligne i et à la colonne j."""
PARA10: str = """Une énumération est un type de données permettant d'assigner des noms à des valeurs entières, rendant le code plus lisible."""
SYNTAXE3: str = """enum <nom> {constante_1, constante_2, ... , constante_n};"""
EXEMPLE4: str = """#include <stdio.h>
enum Jour {LUNDI, MARDI, MERCREDI, JEUDI, VENDREDI, SAMEDI, DIMANCHE};

void main() {
    enum Jour today = MERCREDI;
    printf("Valeur de MERCREDI : %d", today); // Affiche 2
}"""
PARA11: str = """On peut aussi attribuer des valeurs spécifiques : (enum Mois {JANVIER = 1, FEVRIER = 2, MARS = 3, DECEMBRE = 12};). Par défaut, les valeurs commencent à 0 et s'incrémentent de 1."""
PARA12: str = """Une union est une structure qui permet de stocker plusieurs types de données dans la même mémoire, mais un seul champ peut être utilisé à la fois."""
SYNTAXE4: str = """union <nom> { \n<type_1> <identifiant_1>;\n ... ; \n<type_n> <identifiant_n>;\n};"""
EXEMPLE5: str = """#include <stdio.h>

union Data {
    int i;
    float f;
    char str[20];
};

void main() {
    union Data data;
    data.i = 10;
    printf("Valeur entière : %d => ", data.i);

    data.f = 5.5;
    printf("Valeur float : %.2f", data.f); // i est maintenant corrompu
}"""
PARA13: str = """Économie de mémoire : L'union utilise la mémoire du plus grand élément."""
PARA14: str = """Utile quand on doit stocker une seule valeur à la fois."""
PARA15: str = """Le mot-clé typedef permet de renommer un type complexe pour le rendre plus facile à utiliser"""
EXEMPLE6: str = """#include <stdio.h>

typedef struct {
    char nom[50];
    int age;
} Etudiant;

int main() {
    Etudiant e1 = {"Alice", 21};
    printf("Nom : %s, Âge : %d", e1.nom, e1.age);
}
"""
EXEMPLE7: str = """typedef unsigned int uint;\nuint nombre = 10;\nvoid main(){}"""
PARA16: str = """Sans typedef, il faudrait écrire struct Etudiant e1 au lieu de Etudiant e1."""
PARA17: str = """Cela simplifie l'écriture et améliore la lisibilité."""

CONCLUSION: str = """Ces concepts avancés sont essentiels pour écrire du code efficace, clair et optimisé en C. Voici comment les choisir selon le besoin :"""
CONCLUSION1: str = """Tableaux multidimensionnels : Pour stocker des données matricielles."""
CONCLUSION2: str = """Enumérations : Pour rendre le code plus lisible et éviter l'utilisation de nombres en dur."""
CONCLUSION3: str = """Unions : Pour économiser de la mémoire quand une seule valeur est nécessaire à un moment donné."""
CONCLUSION4: str = """Typedef : Pour rendre le code plus clair et plus portable."""

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
                Spacing(), Texte(INTRO1), Texte(INTRO2),
                Spacing(), Titre('1- Les Tableaux (Arrays)'),
                Spacing(), Point('Definition'),
                Spacing(), Texte(PARA1),
                Spacing(), Point('Déclaration et Initialisation'),
                Spacing(), Syntaxe(page, content=SYNTAXE1, font_size=15),
                Spacing(), Exemple(page, 490, '', code=Code(EXEMPLE1)),
                Spacing(), Texte(PARA2), Texte(PARA3),
                Spacing(), Titre('2- Les Structures (struct)'),
                Spacing(), Point('Definition'),
                Spacing(), Texte(PARA4),
                Spacing(), Point('Déclaration et Initialisation'),
                Spacing(), Syntaxe(page, 230,content=SYNTAXE2, font_size=15),
                Spacing(), Exemple(page, 600, '',code=Code(EXEMPLE2, 13)),
                Spacing(), Texte(PARA5), Texte(PARA6),
                Spacing(), Titre('3- Les Tableaux Multidimensionnels'),
                Spacing(), Point('Definition'),
                Spacing(), Texte(PARA7),
                Spacing(), Exemple(page, 600, '',code=Code(EXEMPLE3, 11)),
                Spacing(), Point('Accès aux Éléments'),
                Spacing(), Texte(PARA8 + PARA9),
                Spacing(), Titre('4- Les Énumérations (enum)'),
                Spacing(), Point('Definition'),
                Spacing(), Texte(PARA10),
                Spacing(), Point('Déclaration et Initialisation'),
                Spacing(), Syntaxe(page, content=SYNTAXE3, font_size=15),
                Spacing(), Exemple(page, 600, '',code=Code(EXEMPLE4, 9)),
                Spacing(), Point('Personnalisation des Valeurs'),
                Spacing(), Texte(PARA11),
                Spacing(), Titre('5- Les Unions (union)'),
                Spacing(), Texte(PARA12),
                Spacing(), Point('Déclaration et Initialisation'),
                Spacing(), Syntaxe(page, content=SYNTAXE4, font_size=15),
                Spacing(), Exemple(page, 680, '',code=Code(EXEMPLE5, 16)),
                Spacing(), Point('Pourquoi Utiliser une Union ?'),
                Spacing(), Texte(PARA13), Texte(PARA14),
                Spacing(), Titre('6- typedef : Définition de Type Personnalisé'),
                Spacing(), Texte(PARA15),
                Spacing(), Exemple(page, 350, 'Exemple avec un typedef sur un type natif', Code(EXEMPLE7, 2)),
                Spacing(), Texte(PARA17),
                Spacing(), Exemple(page, 590, 'Exemple avec une Structure',code=Code(EXEMPLE6, 12)),
                Spacing(), Texte(PARA16),
                Spacing(), Titre('Conclusion'),
                Spacing(), Texte(CONCLUSION), Texte(CONCLUSION1), Texte(CONCLUSION2), Texte(CONCLUSION3), Texte(CONCLUSION4),
                Spacing(),
            ]
        )