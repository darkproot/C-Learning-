from flet import Container, padding, Page, ListView
from modules.fonctions import pourcentage
from modules.texte import Spacing
from modules.title import Titre, GrandTitre
from modules.qcm import Qcm
from modules.point import Point
from modules.code import MiniCode, ExerciceCode

MINICODE1: str = """\
#include <stdio.h>

void afficher() {
    printf("Hello !");
}

int main() {
    afficher();
    return 0;
}"""
MINICODE2: str = """\
#include <stdio.h>

int somme(int a, int b) {
    return a + b;
}

int main() {
    printf("%d", somme(2, 3));
    return 0;
}"""

CODE1: str = """\
#include <stdio.h>

// Prototypage
int max(int tab[], int tab_lenght);

int main() {
    const int tab[7] = {2, -4, 6, 0, 10, 3, 7};
    return 0;
}

// Definition
int max(int tab[], int tab_lenght) {

}"""
SOLUTION1: str = r"""#include <stdio.h>

// Prototypage
int max(int tab[], int tab_lenght);

int main() {
    const int tab[7] = {2, -4, 6, 0, 10, 3, 7};
    int idx_max = max((int*)tab, 7);
    printf("Le max est %d d'indice %d.", tab[idx_max], idx_max);
    return 0;
}

// Definition
int max(int tab[], int tab_lenght) {
    int m = 0;
    for (short i = 1; i < tab_lenght; i++)
        if (tab[i] > tab[m])
            m = i;
    return m;
}"""
CODE2: str = """\
#include <stdio.h>

// Prototypage de la procedure
void list_divider(int n);

int main() {
    const short int NUM = 12;
    
}

// Definition de la procedure
void list_divider(int n) {

}"""
SOLUTION2: str = r"""#include <stdio.h>

// Prototypage de la procedure
void list_divider(int n);

int main() {
    const short int NUM = 12;
    list_divider(NUM);
    return 0;
}

// Definition de la procedure
void list_divider(int n) {
    for (int i = 1; i < n; i++)
        if (n % i == 0)
            printf("%d -> ", i);
    printf("%d", n);
}"""
CODE3: str = """\
#include <stdio.h>

typedef struct {
    int num;
    int denum;
} Fraction;

// Prototypage des fonctions
Fraction add(Fraction f1, Fraction f2);
Fraction multiply(Fraction f1, Fraction f2);

int main() {

    return 0;
}

// Definition des fonctions
Fraction add(Fraction f1, Fraction f2) {

}
Fraction multiply(Fraction f1, Fraction f2) {

}"""
SOLUTION3: str = r"""#include <stdio.h>

typedef struct {
    int num;
    int denum;
} Fraction;

// Prototypage des fonctions
Fraction add(Fraction f1, Fraction f2);
Fraction multiply(Fraction f1, Fraction f2);

int main() {
    Fraction f1, f2, f_1, f_2;
    f1.num = 1; f1.denum = 2; 
    f2.num = 2; f2.denum = 5;

    f_1 = add(f1, f2); 
    f_2 = multiply(f1, f2);

    printf(
        "La somme de %d/%d et %d/%d est de: %d/%d\n",
        f1.num, f1.denum, f2.num, f2.denum,
        f_1.num, f_1.denum
    );
    printf(
        "Le produit de %d/%d et %d/%d est de: %d/%d\n",
        f1.num, f1.denum, f2.num, f2.denum,
        f_2.num, f_2.denum
    );
    return 0;
}

// Definition des fonctions
Fraction add(Fraction f1, Fraction f2) {
    Fraction f;
    f.num = (f1.num * f2.denum) + (f2.num * f1.denum); 
    f.denum = f1.denum * f2.denum;
    return f;
}
Fraction multiply(Fraction f1, Fraction f2) {
    Fraction f;
    f.num = f1.num * f2.num;
    f.denum = f1.denum * f2.denum;
    return f;
}"""


QCM1 = {
    'question_id': 1,
    'question': "Quelle est la bonne syntaxe pour déclarer une fonction en C ?",
    'proposition': [
        "fonction(int a, int b) int;",
        "int fonction(a, b) {}",
        "int fonction(int a, int b);",
        "fonction = int(a, b);"
    ],
    'reponse': 2,
}
QCM2 = {
    'question_id': 2,
    'question': "Quelle est la valeur de retour par défaut d'une fonction si aucune n'est spécifiée ?",
    'proposition': ["void", "int", "char", "float"],
    'reponse': 1,
}
QCM3 = {
    'question_id': 3,
    'question': "Que signifie void dans une déclaration de fonction ?",
    'proposition': [
        "La fonction ne prend pas d'arguments",
        "La fonction ne retourne rien",
        "La fonction retourne un entier",
        "La fonction est privée",
    ],
    'reponse': 1,
}
QCM4 = {
    'question_id': 4,
    'question': "Où doit-on placer la déclaration d'une fonction si elle est définie après main() ?",
    'proposition': [
        "Juste avant main()",
        "Après main() sans déclaration",
        "À l'intérieur de main()",
        "N'importe où dans le code",
    ],
    'reponse': 0,
}
QCM5 = {
    'question_id': 5,
    'question': "Quel mot-clé est utilisé pour retourner une valeur dans une fonction ?",
    'proposition': ["return", "break", "exit", "continue"],
    'reponse': 0,
}
QCM6 = {
    'question_id': 6,
    'question': "Quelle est la sortie du programme suivant ?",
    'proposition': ["afficher", "Hello ! afficher", "Erreur de compilation", "Hello !"],
    'reponse': 3,
    'minicode': MiniCode(MINICODE1),
}
QCM7 = {
    'question_id': 7,
    'question': "Quel est l'intérêt des fonctions en C ?",
    'proposition': [
        "Éviter la répétition du code",
        "Rendre le code plus compliqué",
        "Augmenter la vitesse d'exécution",
        "Aucune de ces réponses",
    ],
    'reponse': 0,
}
QCM8 = {
    'question_id': 8,
    'question': "Quelle est la bonne déclaration pour une fonction qui prend un tableau en argument ?",
    'proposition': [
        "void fonction(int tab);",
        "void fonction(int tab[]);",
        "void fonction(int *tab);",
        "Les réponses (2) et (3)",
    ],
    'reponse': 3,
}
QCM9 = {
    'question_id': 9,
    'question': "Quelle est la différence entre une fonction void et une fonction int ?",
    'proposition': [
        "Une fonction void ne prend pas d'arguments",
        "Une fonction void peut être appelée uniquement dans main()",
        "Une fonction int retourne une valeur alors qu'une fonction void ne retourne rien",
        "Il n'y a aucune différence",
    ],
    'reponse': 2,
}
QCM10 = {
    'question_id': 10,
    'question': "Quelle est la sortie du programme suivant ?",
    'proposition': ["2", "3", "5", "Erreur de compilation"],
    'reponse': 2,
    'minicode': MiniCode(MINICODE2),
}

EXERCICE1: dict[str, str] = {
    'text': "Ecrire un programme qui comporte une fonction qui renvoit l'indice du plus grand element d'un tableau d'entier.",
    'code': CODE1,
    'solution': SOLUTION1,
}
EXERCICE2: dict[str, str] = {
    'text': "Ecrire un programme qui comporte une procedure qui affiche tous les diviseurs d'un nombre.",
    'code': CODE2,
    'solution': SOLUTION2,
}
EXERCICE3: dict[str, str] = {
    'text': "Ecrire un programme qui comporte deux fonctions permettant d'additioner et multiplier deux structures (type Fraction) et l'appliquer.",
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
                GrandTitre(text="Fonctions"), Spacing(),
                Titre("Questions a choix multiples"),
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
                Titre("Questions a reponse ouverte"),
                Spacing(), Point("Exercice 1"), 
                Spacing(), ExerciceCode(**EXERCICE1),
                Spacing(), Point("Exercice 2"), 
                Spacing(), ExerciceCode(**EXERCICE2),
                Spacing(), Point("Exercice 3"), 
                Spacing(), ExerciceCode(**EXERCICE3),
                Spacing(),
            ]
        )