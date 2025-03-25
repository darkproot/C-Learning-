from flet import Container, padding, Page, ListView
from modules.fonctions import pourcentage
from modules.texte import Spacing
from modules.title import Titre, GrandTitre
from modules.qcm import Qcm
from modules.point import Point
from modules.code import MiniCode, ExerciceCode

MINICODE1: str = """\
#include <stdio.h>

int main() {
    int a = 10;
    int *p = &a;
    printf("%d", *p);
    return 0;
}"""
MINICODE2: str = """\
#include <stdio.h>

int main() {
    int a = 5, b = 10;
    int *p = &a;
    p = &b;
    printf("%d", *p);
    return 0;
}"""
MINICODE3: str = """\
int *p;
p = (int*)malloc(sizeof(int));"""
MINICODE4: str = """\
#include <stdio.h>

void modifie(int *p) {
    *p = 20;
}

int main() {
    int a = 10;
    modifie(&a);
    printf("%d", a);
    return 0;
}"""

CODE1: str = """\
#include <stdio.h>

void swap(int* a, int* b);

int main() {
    int a = 10, b = 7;
    return 0;
}

void swap(int* a, int* b) {

}"""
SOLUTION1: str = r"""#include <stdio.h>

void swap(int* a, int* b);

int main() {
    int a = 10, b = 7;
    swap(&a, &b);
    printf("a = %d et b = %d", a, b);
    return 0;
}

void swap(int* a, int* b) {
    int c = *a;
    *a = *b;
    *b = c;
}"""
CODE2: str = """\
#include <stdio.h>
#include <stdlib.h>
#define N 5

int main() {
    
    return 0;
}"""
SOLUTION2: str = r"""#include <stdio.h>
#include <stdlib.h>
#define N 5

int main() {
    int * tab = (int *) calloc (N, sizeof(int));
    for (short i = 0; i < N; i++)
        *(tab + i) = 2*i + 1;

    for (short i = 0; i < N; i++)
        printf("%d\t", *(tab + i));

    free(tab);
    return 0;
}"""
CODE3: str = """\
#include <stdio.h>
#include <stdlib.h>

void sort(int* tab, int tab_lenght);

int main() {
    int tab[7] = {0, 28, 5, 3, 7, 8, -6};

    return 0;
}

void sort(int* tab, int tab_lenght) {

}"""
SOLUTION3: str = r"""#include <stdio.h>
#include <stdlib.h>

void sort(int* tab, int tab_lenght);
void swap(int* a, int* b);

int main() {
    int tab[7] = {0, 28, 5, 3, 7, 8, -6};
    sort((int*)tab, 7);
    for (short i = 0; i < 7; i++) {
        switch (i) {
            case 0: 
                printf("tab = [%d, ", *(tab + i));
                break;
            case 6: 
                printf("%d]", *(tab + i));
                break;
            default: printf("%d, ", *(tab + i));
        }
    }
    return 0;
}

void sort(int* tab, int tab_lenght) {
    for (short i = 0; i < tab_lenght; i++)
        for (short j = 0; j < tab_lenght - i; j++)
            if (tab[j] > tab[j+1])
                swap(tab+j, tab+j+1);
}

void swap(int* a, int* b) {
    int c = *a;
    *a = *b;
    *b = c;
}"""

QCM1: dict[str, str] = {
    'question_id': 1,
    'question': "Qu'est-ce qu'un pointeur en C ?",
    'proposition': [
        "Une variable qui stocke une adresse mémoire",
        "Une variable qui stocke uniquement des nombres entiers",
        "Un type de boucle",
        "Une structure de données",
    ],
    'reponse': 0,
}
QCM2: dict[str, str] = {
    'question_id': 2,
    'question': "Quel est l'opérateur utilisé pour obtenir l'adresse d'une variable ?",
    'proposition': ["*", "->", "&", "@"],
    'reponse': 2,
}
QCM3: dict[str, str] = {
    'question_id': 3,
    'question': "Comment déclare-t-on un pointeur sur un entier ?",
    'proposition': ["int ptr;", "int *ptr;", "*int ptr;", "int ptr*;"],
    'reponse': 1,
}
QCM4: dict[str, str] = {
    'question_id': 4,
    'question': "Que se passe-t-il si on déréférence un pointeur non initialisé ?",
    'proposition': [
        "Il affiche 0",
        "Il provoque une erreur de compilation",
        "Il peut entraîner un comportement indéfini",
        "Il affiche NULL",
    ],
    'reponse': 2,
}
QCM5: dict[str, str] = {
    'question_id': 5,
    'question': "Quelle est la sortie du programme suivant ?",
    'proposition': ["10", "L'adresse de a", "NULL", "Erreur de compilation"],
    'reponse': 0,
    'minicode': MiniCode(MINICODE1),
}
QCM6: dict[str, str] = {
    'question_id': 6,
    'question': "Quel est l'opérateur de déréférencement ?",
    'proposition': ["#", "%", "&", "*"],
    'reponse': 3,
}
QCM7: dict[str, str] = {
    'question_id': 7,
    'question': "Quelle est la valeur affichée par ce code ?",
    'proposition': ["5", "10", "L'adresse de b", "Erreur de compilation"],
    'reponse': 1,
    'minicode': MiniCode(MINICODE2),
}
QCM8: dict[str, str] = {
    'question_id': 8,
    'question': "Que fait le code suivant ?",
    'proposition': [
        "Il alloue de la mémoire dynamiquement",
        "Il crée un pointeur constant",
        "Il affiche NULL",
        "Il génère une erreur",
    ],
    'reponse': 0,
    'minicode': MiniCode(MINICODE3),
}
QCM9: dict[str, str] = {
    'question_id': 9,
    'question': "Comment libérer la mémoire allouée par malloc ?",
    'proposition': [
        "delete(p);",
        "remove(p);",
        "free(p);",
        "clear(p);",
    ],
    'reponse': 2,
}
QCM10: dict[str, str] = {
    'question_id': 10,
    'question': "Quelle est la sortie du programme suivant ?",
    'proposition': ["10", "20", "0x44636", "Un message d'erreur"],
    'reponse': 1,
    'minicode': MiniCode(MINICODE4),
}

EXERCICE1: dict[str, str] = {
    'text': "Ecrire un programme qui comporte une procedure qui inverse les valeurs de deux entiers.",
    'code': CODE1,
    'solution': SOLUTION1,
}
EXERCICE2: dict[str, str] = {
    'text': "Ecrire un programme qui alloue un espace memoire comportant N nombre impaire.",
    'code': CODE2,
    'solution': SOLUTION2,
}
EXERCICE3: dict[str, str] = {
    'text': "Ecrire un programme qui comporte une procedure qui tri un tableau.",
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
                GrandTitre(text="Pointeurs"), Spacing(),
                Titre("Question a choix multiple"),
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
                Spacing(), Titre("Question a reponse ouverte"),
                Spacing(), Point("Exercice 1"),
                Spacing(), ExerciceCode(**EXERCICE1),
                Spacing(), Point("Exercice 2"),
                Spacing(), ExerciceCode(**EXERCICE2),
                Spacing(), Point("Exercice 3"),
                Spacing(), ExerciceCode(**EXERCICE3),
                Spacing(),
            ]
        )