from flet import Container, Column, Page, padding, Text, Row, Icon, icons, MainAxisAlignment
from flet import ControlEvent, Animation, TextStyle, BoxShadow, Offset
from modules.fonctions import pourcentage
from pages.exercises import variables
from pages.exercises import operateurs
from pages.exercises import struct_controle
from pages.exercises import struct_donnne
from pages.exercises import fonctions_exercices
from modules.color import DEEP_BLUE

def change_page(e: ControlEvent): 
    page: Page = e.page
    data: str = e.control.data.lower()
    display = page.controls[0].controls
    match data:
        case 'variables':
            display[-1] = variables.Display(page)
        case 'operateurs':
            display[-1] = operateurs.Display(page)
        case 'structures de controles':
            display[-1] = struct_controle.Display(page)
        case 'structures de donnees':
            display[-1] = struct_donnne.Display(page)
        case 'fonctions':
            display[-1] = fonctions_exercices.Display(page)
    page.update()

class Display(Container):
    CHAPITRES: list[str] = [
        'variables',
        'operateurs',
        'structures de controles',
        'structures de donnees',
        'Fonctions',
        'Pointeurs',
        'Fichiers',
    ]
    CHAPITRES_ICONS: list[str] = [
        icons.GIF_BOX,
        icons.CALCULATE,
        icons.THREE_K,
        icons.DATA_ARRAY,
        icons.FUNCTIONS,
        icons.DEW_POINT,
        icons.FILE_OPEN,
    ]
    def __init__(self, page: Page):
        super().__init__(
            bgcolor='white',
            border_radius=10,
            expand=True,
            height=page.window.height - 70,
            padding=padding.only(pourcentage(page.window.width, 10), 15, pourcentage(page.window.width, 10)),
        )
        self.content = Column(alignment=MainAxisAlignment.CENTER)
        for chapitre, icon in zip(Display.CHAPITRES, Display.CHAPITRES_ICONS):
            self.content.controls.append(Chapitre(chapitre, icon, change_page))

class Chapitre(Container):
    def __init__(self, chapitre: str, icon: str, on_click = None):
        super().__init__(
            bgcolor=DEEP_BLUE,
            border_radius=20,
            padding=20,
            on_click=on_click,
            on_hover=self.hover,
            data=chapitre,
        )
        self.animation = Animation(200, 'ease')
        self.animate = self.animation
        self.icon = Icon(icon, 'white', animate_scale=self.animation)
        self.texte = Text(chapitre.capitalize(), font_family='texte', color='white', size=20, expand=True)
        self.content = Row(
            controls=[self.icon, Container(width=10), self.texte]
        )

    def hover(self, e: ControlEvent): 
        page: Page = e.page
        texte: Text = self.content.controls[2]
        texte_style: TextStyle = TextStyle(shadow=BoxShadow(5, 1, 'black', Offset(3, 3)))
        icon: Icon = self.content.controls[0]
        if e.data == 'true': 
            icon.scale = 1.2
            texte.style = texte_style
            self.padding = padding.only(25, 20, 25, 20)
        else: 
            self.padding = 20
            texte.style = None
            icon.scale = 1
        page.update()