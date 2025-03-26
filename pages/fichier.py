from flet import Container, padding, Page, ListView
from modules.fonctions import pourcentage
from modules.code import Code
from modules.exemple import Exemple
from modules.syntaxe import Syntaxe
from modules.texte import Texte, Spacing
from modules.title import Titre, GrandTitre
from modules.point import Point
from modules.tableau import Table

INTRO: str = """En C, la gestion des fichiers permet de lire, écrire et manipuler des fichiers sur le disque. Le langage C fournit une bibliothèque standard (stdio.h) avec des fonctions pour interagir avec les fichiers."""

TABLE1: list[list[str]] = [
    ["Mode", "Description"],
    ['"r"', "Lecture seule, erreur si le fichier n'existe pas."],
    ['"w"', "Ecriture seule, cree un fichier s'il n'existe pas et ecrase s'il existe."],
    ['"a"', "Ajout (append), cree un fichier s'il n'existe pas."],
    ['"r+"', "Lecture et ecriture, erreur si le fichier n'existe pas."],
    ['"w+"', "Lecture et ecriture, cree un fichier et ecrase l'ancien."],
    ['"a+"', "Lecture et ajout a la fin, cree un fichier si inexistant."],
]
TABLE2: list[list[str]] = [
    ["Fonction", "Description"],
    ["fseek(FILE *f, long offset, int origine)", "Deplace le curseur a une position."],
    ["ftell(FILE *f)", "Renvoie la position actuelle du curseur."],
    ["rewind(FILE *f)", "Replace le curseur au debut."],
]

PARAM1: str = """Avant d'utiliser un fichier, il faut l'ouvrir avec la fonction fopen()."""
SYNTAXE1: str = """FILE *fopen(const char *nomFichier, const char *mode);"""
PARAM2: str = """nomFichier : Nom du fichier (ex. "data.txt")"""
PARAM3: str = """mode : Mode d'ouverture (lecture, écriture, etc.)"""
PARAM4: str = """Retourne un pointeur de type FILE* ou NULL en cas d'échec."""
EXEMPLE1: str = """\
#include <stdio.h>
#include <direct.h>

int main() {
    FILE *f = fopen("test.txt", "w");
    if (f == NULL) {
        printf("Erreur lors de l'ouverture du fichier.");
        return 1;
    }
    printf("Fichier ouvert avec succès.");
    fclose(f); // Ferme le fichier
    return 0;
}"""
PARAM5: str = """Utilisation de fprintf() et fputc()"""
SYNTAXE2: str = """fprintf(FILE *f, "format", ...) : Écrit du texte formaté."""
SYNTAXE3: str = """\nfputc(int c, FILE *f) : Écrit un caractère."""
EXEMPLE2: str = r"""#include <stdio.h>

int main() {
    FILE *f = fopen("test.txt", "w");
    if (f == NULL) {
        printf("Erreur lors de l'ouverture du fichier.\n");
        return 1;
    }

    fprintf(f, "Bonjour, ceci est un test.\n");
    fputc('A', f); // Écrit 'A' dans le fichier

    fclose(f);
    return 0;
}"""
PARAM6: str = """Utilisation de fscanf() et fgetc()"""
SYNTAXE4: str = """fscanf(FILE *f, "format", ...) : Lit du texte formaté."""
SYNTAXE5: str = """\nfgetc(FILE *f) : Lit un caractère."""
EXEMPLE3: str = r"""#include <stdio.h>

int main() {
    FILE *f = fopen("test.txt", "r");
    if (f == NULL) {
        printf("Erreur : fichier introuvable.\n");
        return 1;
    }
    char ligne[100];
    while (fgets(ligne, sizeof(ligne), f) != NULL) {
        printf("%s", ligne);
    }
    fclose(f);
    return 0;
}
"""
PARAM7: str = """fgets(ligne, sizeof(ligne), f) lit une ligne entière."""
EXEMPLE4: str = r"""#include <stdio.h>

int main() {
    FILE *f = fopen("test.txt", "a");
    if (f == NULL) {
        printf("Erreur d'ouverture du fichier.\n");
        return 1;
    }

    fprintf(f, "Nouvelle ligne ajoutée.\n");
    fclose(f);
    return 0;
}"""
PARAM8: str = """Cela ajoute une ligne sans écraser le contenu précédent."""
PARAM9: str = """Utilisation de remove()"""
EXEMPLE5: str = r"""#include <stdio.h>

int main() {
    if (remove("test.txt") == 0) {
        printf("Fichier supprimé avec succès.\n");
    } else {
        printf("Erreur lors de la suppression.\n");
    }
    return 0;
}"""
PARAM10: str = """remove("test.txt") supprime le fichier."""
PARAM11: str = """Les fonctions fseek(), ftell(), et rewind() permettent de naviguer dans un fichier"""
EXEMPLE6: str = r"""#include <stdio.h>

int main() {
    FILE *f = fopen("test.txt", "r");
    if (f == NULL) {
        printf("Erreur lors de l'ouverture du fichier.\n");
        return 1;
    }

    fseek(f, 5, SEEK_SET); // Déplace à la position 5
    char c = fgetc(f);
    printf("Caractère à la position 5 : %c\n", c);

    fclose(f);
    return 0;
}"""
PARAM12: str = """Les fichiers binaires sont utilisés pour stocker des structures."""
EXEMPLE7: str = r"""#include <stdio.h>

typedef struct {
    char nom[20];
    int age;
} Personne;

int main() {
    FILE *f = fopen("personne.bin", "wb");
    if (f == NULL) {
        printf("Erreur d'ouverture.\n");
        return 1;
    }

    Personne p = {"Alice", 25};
    fwrite(&p, sizeof(Personne), 1, f); // Écrit la structure

    fclose(f);
    return 0;
}"""
EXEMPLE8: str = r"""#include <stdio.h>

typedef struct {
    char nom[20];
    int age;
} Personne;

int main() {
    FILE *f = fopen("personne.bin", "rb");
    if (f == NULL) {
        printf("Erreur de lecture.\n");
        return 1;
    }

    Personne p;
    fread(&p, sizeof(Personne), 1, f); // Lit la structure

    printf("Nom : %s, Âge : %d\n", p.nom, p.age);

    fclose(f);
    return 0;
}"""

CONCLUSION: str = """La gestion des fichiers en C est essentielle pour stocker et récupérer des données de manière persistante. Grâce aux fonctions fournies par la bibliothèque standard (stdio.h), nous pouvons ouvrir, lire, écrire et manipuler des fichiers efficacement."""

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
                GrandTitre(text="Fichiers"), Spacing(),
                Titre("Introduction"),
                Spacing(), Texte(INTRO),
                Spacing(), Titre('1- Ouverture d\'un fichier'),
                Spacing(), Texte(PARAM1),
                Spacing(), Syntaxe(page, 200, SYNTAXE1),
                Spacing(), Texte(PARAM2), Texte(PARAM3), Texte(PARAM4),
                Spacing(), Point('Modes d\'ouverture'),
                Spacing(), Table(TABLE1),
                Spacing(), Exemple(page, 600, 'Ouvrir un fichier en écriture', Code(EXEMPLE1, 12)),
                Spacing(), Titre('2- Écriture dans un fichier'),
                Spacing(), Texte(PARAM5), 
                Syntaxe(page, 200, SYNTAXE2 + SYNTAXE3),
                Spacing(), Exemple(page, 650, 'Écriture dans un fichier', Code(EXEMPLE2, 15)),
                Spacing(), Titre('3- Lecture d\'un fichier'),
                Spacing(), Texte(PARAM6), 
                Syntaxe(page, 200, SYNTAXE4 + SYNTAXE5),
                Spacing(), Exemple(page, 670, 'Lecture d\'un fichier', Code(EXEMPLE3, 16)),
                Spacing(), Texte(PARAM7), 
                Spacing(), Titre('4- Ajout de texte dans un fichier (a mode)'),
                Spacing(), Exemple(page, 620, '', Code(EXEMPLE4, 13)),
                Spacing(), Texte(PARAM8), 
                Spacing(), Titre('5- Suppression d\'un fichier'),
                Spacing(), Texte(PARAM9), 
                Spacing(), Exemple(page, 550, '', Code(EXEMPLE5, 10)),
                Spacing(), Texte(PARAM10), 
                Spacing(), Titre('6- Positionnement dans un fichier'),
                Spacing(), Texte(PARAM11), 
                Spacing(), Table(TABLE2),
                Spacing(), Exemple(page, 650, 'Se déplacer dans un fichier', Code(EXEMPLE6, 16)),
                Spacing(), Titre('7- Lecture et écriture de structures dans un fichier'),
                Spacing(), Texte(PARAM12), 
                Spacing(), Point('Écriture d\'une structure dans un fichier binaire'),
                Spacing(), Exemple(page, 750, '', Code(EXEMPLE7, 20)),
                Spacing(), Point('Lecture d\'une structure depuis un fichier binaire'),
                Spacing(), Exemple(page, 790, '', Code(EXEMPLE8, 22)),
                Spacing(), Titre("Conclusion"),
                Spacing(), Texte(CONCLUSION),
                Spacing()
            ]
        )