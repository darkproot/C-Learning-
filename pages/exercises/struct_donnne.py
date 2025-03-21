from flet import Container, ListView, Page, padding
from modules.fonctions import pourcentage
from modules.qcm import Qcm
from modules.title import Titre, GrandTitre
from modules.texte import Spacing
from modules.point import Point
from modules.code import ExerciceCode, MiniCode
from modules.tableau import Table

MINICODE1: str = """\
int tab[5] = {1, 3, 2, 5, 4};
printf("tab[%d] = %d", 4, tab[4]);"""

TABLEAU: list[list[str]] = [
    ["Matricules", "Noms", "Prénoms"],
    ["23P517", "Chaltouang", "Manasse"],
    ["23P434", "Elbaa", "Carine"],
    ["23P567", "Takam", "Ulrich"],
]

CODE1: str = """\
#include <stdio.h>

int main() {
    const short tab_lenght = 7;
    short tab[] = {1, 3, 5, 7, 11, 13, 17};

    return 0;
}"""
SOLUTION1: str = r"""# include <stdio.h>

void main() {
    const short tab_lenght = 7;
    short tab[] = {1, 3, 5, 7, 11, 13, 17};
    for (short i = 0; i < tab_lenght; i++) 
        printf("Indice %d => %d\n", i, (tab[i] * tab[i]));
}"""
CODE2: str = """\
#include <stdio.h>

#define NUM 3
#define MAX_NOM 20
#define MAX_PRENOM 10
#define MAX_MATRICULE 7
struct ELEVE {
        char nom[MAX_NOM];
        char prenom[MAX_PRENOM];
        char matricule[MAX_MATRICULE];
};

struct ELEVE data_base[NUM]; // Création d'un tableau de structure
char NOMS[NUM][MAX_NOM] = {"Chaltouang", "Elbaa", "Takam"};
char PRENOMS[NUM][MAX_PRENOM] = {"Manasse", "Carine", "Ulrich"};
char MATRICULES[NUM][MAX_MATRICULE] = {"23P517", "23P434", "23P567"};

int main() {

    return 0;
}"""
SOLUTION2: str = r"""# include <stdio.h>

#define NUM 3
#define MAX_NOM 20
#define MAX_PRENOM 10
#define MAX_MATRICULE 7
struct ELEVE {
        char nom[MAX_NOM];
        char prenom[MAX_PRENOM];
        char matricule[MAX_MATRICULE];
};

struct ELEVE data_base[NUM]; 
char NOMS[NUM][MAX_NOM] = {"Chaltouang", "Elbaa", "Takam"};
char PRENOMS[NUM][MAX_PRENOM] = {"Manasse", "Carine", "Ulrich"};
char MATRICULES[NUM][MAX_MATRICULE] = {"23P517", "23P434", "23P567"};

int main() {
    // Remplissage de la Base de donnee
    for (short i = 0; i < NUM; i++) {
        for (short j = 0; j < MAX_NOM; j++)
            data_base[i].nom[j] = NOMS[i][j];
        for (short j = 0; j < MAX_PRENOM; j++)
            data_base[i].prenom[j] = PRENOMS[i][j];
        for (short j = 0; j < MAX_MATRICULE; j++)
            data_base[i].matricule[j] = MATRICULES[i][j];
    }

    // Affichage
    for (short i = 0; i < NUM; i++) {
        printf("%d. Nom: %s\n", (i+1), data_base[i].nom);
        printf("   Prenom: %s\n", data_base[i].prenom);
        printf("   Matricule: %s\n\n", data_base[i].matricule);
    }
    return 0;
}"""
CODE3: str = """\
#include <stdio.h>

typedef struct {
    float num;
    float denum;
} Fraction;

int main() {
    
}"""
SOLUTION3: str = r"""#include <stdio.h>

typedef struct {
    float num;
    float denum;
} Fraction;

int main() {
    Fraction p, q, s;
    p.num = 1.5; p.denum = 2;
    q.num = -3; q.denum = 4;
    s.num = p.num * q.num;
    s.denum = p.denum * q.denum;

    printf(
        "Le produit de %.1f/%.1f et de %.1f/%.1f est de: %.1f/%.1f", 
        p.num, p.denum,
        q.num, q.denum,
        s.num, s.denum
    );
    return 0;
}"""

QCM1: dict[str, str] = {
    'question_id': 1,
    'question': "Quel est l'objectif principal d'une structure de données en C ?",
    'proposition': ["Augmenter la vitesse du processeur", "Réduire la taille du code source", "Organiser et stocker les données efficacement", "Améliorer la syntaxe du language"],
    'reponse': 2
}
QCM2: dict[str, str] = {
    'question_id': 2,
    'question': "Quel mot-clé est utilisé pour définir une structure en C ?",
    'proposition': ["struct", "structure", "class", "typedef"],
    'reponse': 0
}
QCM3: dict[str, str] = {
    'question_id': 3,
    'question': "Comment accède-t-on à un membre d'une structure via un pointeur ?",
    'proposition': ["ptr.member", "ptr->member", "*ptr.member", "typeptr:member"],
    'reponse': 1
}
QCM4: dict[str, str] = {
    'question_id': 4,
    'question': "Quelle est la différence entre une structure (struct) et une union (union) en C ?",
    'proposition': [
        "Une structure occupe moins de mémoire qu'une union",
        "Une union partage la mémoire entre ses membres, tandis qu'une structure alloue de la mémoire pour chaque membre",
        "Une structure est plus rapide qu'une union",
        "Une union ne peut contenir que des types de données numériques",
    ],
    'reponse': 1
}
QCM5: dict[str, str] = {
    'question_id': 5,
    'question': "Quelle est la taille d'une structure contenant un int, un char, et un double sur un système 64 bits ?",
    'proposition': ["13 octets", "16 octets", "24 octets", "Dépend de l'alignement mémoire"],
    'reponse': 3
}
QCM6: dict[str, str] = {
    'question_id': 6,
    'question': "Quelle est la bonne façon d'allouer dynamiquement de la mémoire pour une structure en C ?",
    'proposition': [
        "struct Student *s = malloc(sizeof(struct Student));",
        "struct Student s = malloc(sizeof(struct Student));",
        "struct Student *s = new Student();",
        "struct Student *s = allocate(struct Student);",
    ],
    'reponse': 0
}
QCM7: dict[str, str] = {
    'question_id': 7,
    'question': "Quelle est la meilleure manière de copier une structure en C ?",
    'proposition': [
        "struct1 = struct2;",
        "strcpy(struct1, struct2);",
        "memcpy(&struct1, &struct2, sizeof(struct1));",
        "copy(struct1, struct2);",
    ],
    'reponse': 2,
}
QCM8: dict[str, str] = {
    'question_id': 8,
    'question': "Comment peut-on créer un alias de type pour une structure en C ?",
    'proposition': [
        "typedef struct { ... } Student;",
        "alias struct Student;",
        "define Student struct Student;",
        "type struct Student as Student;",
    ],
    'reponse': 0,
}
QCM9: dict[str, str] = {
    'question_id': 9,
    'question': "Quel est l'intérêt d'utiliser une liste chaînée plutôt qu'un tableau en C ?",
    'proposition': [
        "Accès plus rapide aux éléments",
        "Utilisation d'un espace mémoire fixe",
        "Allocation dynamique de mémoire et facilité d'insertion/suppression",
        "Facilité de tri des éléments",
    ],
    'reponse': 2,
}
QCM10: dict[str, str] = {
    'question_id': 10,
    'question': "Quelle est la principale différence entre une liste chaînée simple et une liste doublement chaînée ?",
    'proposition': [
        "Une liste chaînée simple utilise plus de mémoire",
        "Une liste chaînée simple ne peut stocker que des nombres entiers",
        "Une liste doublement chaînée ne peut pas être allouée dynamiquement",
        "Une liste doublement chaînée permet de naviguer dans les deux sens",
    ],
    'reponse': 3,
}
QCM11: dict[str, str] = {
    'question_id': 11,
    'question': "Quelle est la sortie de ce code ?",
    'proposition': ['tab[4] = 5', 'tab[4] = 4', 'tab[5] = 4', 'Un message d\'erreur'],
    'reponse': 1,
    'minicode': MiniCode(MINICODE1),
}

EXERCICE1: dict[str, str] = {
    'text': "Ecrire un programme qui affiche le double des éléments contenus dans un table précédé de leurs indices.",
    'code': CODE1,
    'solution': SOLUTION1,
}
EXERCICE2: dict[str, str] = {
    'text': "Ecrire un programme qui remplie un tableau de structure à partir des listes d'informations sur les élèves et les affiches, en vue d'obtenir une base de donnée comme dans le tableau ci-dessus.",
    'code': CODE2,
    'solution': SOLUTION2,
}
EXERCICE3: dict[str, str] = {
    'text': "Ecrire un programme qui initialise deux fractions, les multiplis et les affiches.",
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
                GrandTitre(text="Structures de données", font_size=30), Spacing(),
                Titre("Questions a choix multiple"),
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
                Qcm(**QCM11),
                Spacing(), Titre("Question a reponses ouverte"),
                Spacing(),
                Point("Exercice 1"),
                Spacing(), ExerciceCode(**EXERCICE1),
                Spacing(),
                Point("Exercice 2"),
                Spacing(), Table(TABLEAU),
                Spacing(), ExerciceCode(**EXERCICE2),
                Spacing(),
                Point("Exercice 3"),
                Spacing(), ExerciceCode(**EXERCICE3),
                Spacing(),
            ],
        )