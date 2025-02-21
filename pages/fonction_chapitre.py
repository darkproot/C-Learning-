from flet import Container, padding, Page, ListView
from modules.fonctions import pourcentage
from modules.texte import Texte, Spacing
from modules.syntaxe import Syntaxe
from modules.title import Titre
from modules.exemple import Exemple
from modules.code import Code
from modules.point import Point

INTRO: str = """En langage C, une fonction est un bloc de code qui effectue une tâche spécifique. Elle permet d'organiser le programme, d'améliorer la réutilisabilité du code et de faciliter la maintenance."""
SYNTAXE1: str = """
<type_de_retour> nom_de_la_fonction(paramètres) {
    // Corps de la fonction
    return valeur; // (si le type de retour n'est pas `void`)
}"""
EXEMPLE1: str = """#include <stdio.h>

// Fonction qui retourne la somme de deux entiers
int addition(int a, int b) {
    return a + b;
}

int main() {
    int resultat = addition(5, 3);
    printf("La somme est : %d", resultat);
    return 0;
}"""
PARA1: str = """int addition(int a, int b): Déclaration d'une fonction qui prend deux entiers et retourne un entier."""
PARA2: str = """return a + b; : Retourne la somme des deux nombres."""
PARA3: str = """int resultat = addition(5, 3); : Appel de la fonction."""
PARA4: str = """Il est possible de séparer la déclaration et la définition d'une fonction."""
PARA5: str = """Avant d'utiliser une fonction, on peut la déclarer en haut du programme :"""
EXEMPLE2: str = """#include <stdio.h>

// Prototypage
int soustraction(int a, int b);

void main() {
    int a = 5, b = 3;
    printf("%d - %d = %d", a, b, soustraction(b, a));
}

// Défintion
int soustraction(int a, int b) {
    return a - b;
}"""
PARA6: str = """Les fonctions peuvent être classées en plusieurs catégories selon leur type de retour et paramètres."""
EXEMPLE3: str = """#include <stdio.h>

void modifier(int x) {
    x = 10; 
}

int main() {
    int nombre = 5;
    modifier(nombre);
    printf("%d", nombre); // Affichera 5, car x a été modifié localement
    return 0;
}"""
EXEMPLE4: str = """#include <stdio.h>

void modifier(int *x) {
    *x = 10;
}

int main() {
    int nombre = 5;
    modifier(&nombre);
    printf("%d", nombre); // Affichera 10, car on modifie directement l’adresse mémoire
    return 0;
}"""
PARA7: str = """La fonction main() est le point d'entrée de tout programme en C."""
PARA8: str = """return 0; indique que le programme s'est terminé correctement."""
EXEMPLE5: str = """#include <stdio.h>

long factorielle(int n) {
    if (n == 0) return 1;
    return n * factorielle(n - 1);
}

int main() {
    printf("5! = %d", factorielle(5));
    return 0;
}"""
CONCLUSION: str = """Les fonctions en C sont essentielles pour structurer un programme. Elles améliorent la modularité, la réutilisabilité et la lisibilité du code. La maîtrise des fonctions (passage de paramètres, récursivité, prototypes) est cruciale pour programmer efficacement en C."""

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
                Titre("Introduction"),
                Spacing(), Texte(INTRO),
                Spacing(), Titre('1- Définition d\'une Fonction'),
                Spacing(), Texte('Une fonction en C suit une structure générale :'),
                Syntaxe(page, 230, SYNTAXE1, 15),
                Exemple(page, 600, '', Code(EXEMPLE1, 12)),
                Spacing(), Point('Explication'),
                Spacing(), Texte(PARA1), Texte(PARA2), Texte(PARA3),
                Spacing(), Titre('2. Déclaration et Définition d\'une Fonction'),
                Spacing(), Texte(PARA4),
                Spacing(), Point('Déclaration (Prototype)'),
                Spacing(), Texte(PARA5),
                Syntaxe(page, content='<type> <nom_fonc>(param_1, param_n);'),
                Spacing(), Point('Définition'),
                Spacing(), Texte('La définition est le bloc où on implémente la logique de la fonction.'),
                Exemple(page, 610, '', Code(EXEMPLE2, 14)),
                Spacing(), Titre('3- Passage de Paramètres'),
                Spacing(), Texte('Les arguments peuvent être passés de deux façons :'),
                Spacing(), Point('Passage par Valeur (Copie)'),
                Spacing(), Texte('Les modifications des paramètres ne changent pas les valeurs originales.'),
                Exemple(page, 600, '', Code(EXEMPLE3, 12)),  
                Spacing(), Point('Passage par Référence (Utilisation des Pointeurs)'),
                Spacing(), Texte('Permet de modifier directement la valeur originale.'),
                Exemple(page, 600, '', Code(EXEMPLE4, 13)),  
                Spacing(), Titre('4- Fonction main() et son Rôle'),
                Spacing(), Texte(PARA7), Texte(PARA8),
                Spacing(), Titre('5- Fonctions Récursives'),
                Spacing(), Texte('Une fonction récursive s\'appelle elle-même pour résoudre un problème.'),
                Exemple(page, 600, 'Fonction factorielle', Code(EXEMPLE5, 11)),
                Spacing(), Titre('Conclusion'),
                Spacing(), Texte(CONCLUSION), Spacing(),  
            ]
        )