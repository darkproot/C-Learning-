from modules.fonctions import pourcentage, get_absolute_path
from flet import Container, padding, Page, ListView
from modules.code import MiniCode, ExerciceCode
from modules.title import Titre, GrandTitre
from modules.constantes import HEIGHT
from modules.texte import Spacing
from modules.point import Point
from modules.qcm import Qcm

MINICODE1: str = """\
#include <stdio.h>

int main() {
    FILE *file = fopen("data.txt", "r");
    char buffer[10];
    if (file) {
        fgets(buffer, 10, file);
        printf("%s", buffer);
        fclose(file);
    }
    return 0;
}"""

FILE: str = str(get_absolute_path("Training files")).replace('\\', '/')

CODE1_1: str = """\
#include <stdio.h>
#include <direct.h>
#include <stdlib.h>
#define FICHIER "file1.txt"

int main() {
"""
CODE1_2: str = f"""\
    _chdir("{FILE}");

    return 0;
"""
CODE1: str = CODE1_1 + CODE1_2 + '}'
SOLUTION1_1: str = f"""\
    _chdir("{FILE}");
    FILE * file = fopen(FICHIER, "r");
"""
SOLUTION1_2: str = """\
    int c;
    while ((c = fgetc(file)) != EOF)
        printf("%c", c);
    fclose(file);
    return 0;
}"""
SOLUTION1: str = CODE1_1 + SOLUTION1_1 + SOLUTION1_2

CODE2_1: str = """\
#include <stdio.h>
#include <direct.h>
#include <stdlib.h>
#define FICHIER "user_file1.txt"

int main() {
"""
CODE2: str = CODE2_1 + CODE1_2 + '}'
SOLUTION2_1: str = f"""\
    _chdir("{FILE}");
    FILE * file = fopen(FICHIER, "w");
""" 
SOLUTION2_2: str = r"""
    for (short i = 0; i < 10; i++)
        fprintf(file, "%d\n", i*i);
    fclose(file);
    
    return 0;
}"""
SOLUTION2: str = CODE2_1 + SOLUTION2_1 + SOLUTION2_2

CODE3_1: str = """\
#include <stdio.h>
#include <direct.h>
#include <stdlib.h>
#define FICHIER "file2.txt"

int main() {
    const char PERSONNES[2][20] = {"Takam Ulrich", "TOumpe Eric"};
"""
CODE3: str = CODE3_1 + CODE1_2 + '}'
SOLUTION3_1: str = f"""\
    _chdir("{FILE}");
    FILE * file = fopen(FICHIER, "a");
"""
SOLUTION3_2: str = r"""
    for (short i = 0; i < 2; i++)
        fprintf(file, "%s\n", PERSONNES[i]);
    fclose(file);

    return 0;
}"""
SOLUTION3: str = CODE3_1 + SOLUTION3_1 + SOLUTION3_2

QCM1: dict[str, str] = {
    'question_id': 1,
    'question': "Quelle bibliothèque faut-il inclure pour manipuler les fichiers en C ?",
    'proposition': [
        "#include <file.h>",
        "#include <stdlib.h>",
        "#include <stdio.h>",
        "#include <fichier.h>",
    ],
    'reponse': 2,
}
QCM2: dict[str, str] = {
    'question_id': 2,
    'question': "Quel type est utilisé pour manipuler un fichier en C ?",
    'proposition': ["int", "char *", "FILE *", "file"],
    'reponse': 2,
}
QCM3: dict[str, str] = {
    'question_id': 3,
    'question': "Que fait la fonction fopen() en C ?",
    'proposition': [
        "Elle alloue de la mémoire",
        "Elle ouvre un fichier",
        "Elle lit une ligne d'un fichier",
        "Elle ferme un fichier",
    ],
    'reponse': 1,
}
QCM4: dict[str, str] = {
    'question_id': 4,
    'question': "Quelle est la bonne syntaxe pour ouvrir un fichier en mode écriture ?",
    'proposition': [
        'fopen("data.txt", "w");',
        'fopen("data.txt", "r");',
        'open("data.txt", "write");',
        'open("data.txt", "w");',
    ],
    'reponse': 0,
}
QCM5: dict[str, str] = {
    'question_id': 5,
    'question': "Que signifie le mode \"a\" dans fopen() ?",
    'proposition': [
        'Lire un fichier',
        'Ajouter du contenu à la fin du fichier',
        'Écraser le fichier existant',
        'Lire et écrire en même temps',
    ],
    'reponse': 1,
}
QCM6: dict[str, str] = {
    'question_id': 6,
    'question': "Quelle fonction est utilisée pour lire un fichier ligne par ligne ?",
    'proposition': ["fgets()", "fputs()", "fscanf()", "fgetc()"],
    'reponse': 0,
}
QCM7: dict[str, str] = {
    'question_id': 7,
    'question': "Que fait la fonction fclose() en C ?",
    'proposition': [
        "Elle efface le contenu du fichier",
        "Elle supprime un fichier",
        "Elle ferme un fichier",
        "Elle crée un fichier",
    ],
    'reponse': 2,
}
QCM8: dict[str, str] = {
    'question_id': 8,
    'question': "Quelle fonction permet d'écrire une ligne dans un fichier ?",
    'proposition': ["fprintf()", "fwrite()", "fscanf()", "fgets()"],
    'reponse': 0,
}
QCM9: dict[str, str] = {
    'question_id': 9,
    'question': "Que retourne fopen() si l'ouverture du fichier échoue ?",
    'proposition': ["1", "0", "NULL", "Un message d'erreur"],
    'reponse': 2,
}
QCM10: dict[str, str] = {
    'question_id': 9,
    'question': "Quelle est la sortie du programme suivant si data.txt contient Hello ?",
    'proposition': [
        "Hello",
        "data.txt",
        "fichier",
        "Erreur de compilation",
    ],
    'reponse': 0,
    'minicode': MiniCode(MINICODE1),
}

EXERCICE1: dict[str, str] = {
    'text': "Ecrire un programme qui affiche le contenu d'un fichier nommee 'file1.txt'.",
    'code': CODE1,
    'solution': SOLUTION1,
}
EXERCICE2: dict[str, str] = {
    'text': "Ecrire un programme qui vas écrire le carré des 10 premiers nombre paire sur chaque ligne dans le fichier 'user_file1.txt'.",
    'code': CODE2,
    'solution': SOLUTION2,
}
EXERCICE3: dict[str, str] = {
    'text': "Ecrire un programme qui ajoute le nom et le prénom d'une personne dans un fichier 'file2.txt' constituant la liste de présence.",
    'code': CODE3,
    'solution': SOLUTION3,
}

class Display(Container):
    def __init__(self, page: Page):
        super().__init__(
            bgcolor='white',
            border_radius=10,
            expand=True,
            height=page.window.height - HEIGHT,
            padding=padding.only(pourcentage(page.window.width, 10), 15, pourcentage(page.window.width, 10)),
        )
        self.content = ListView(
            controls=[
                GrandTitre(text='Fichiers'), Spacing(), 
                Titre("Question à choix multiples"),
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
                Spacing(), Titre("Question à reponses ouverte"),
                Spacing(), Point("Exercice 1"),
                Spacing(), ExerciceCode(**EXERCICE1),                          
                Spacing(), Point("Exercice 2"),
                Spacing(), ExerciceCode(**EXERCICE2),                          
                Spacing(), Point("Exercice 3"),
                Spacing(), ExerciceCode(**EXERCICE3),   
                Spacing(),                       
            ]
        )