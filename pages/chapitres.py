from flet import Container, Page, Column, Row, MainAxisAlignment, Offset, BoxShadow
from flet import colors, Icon, icons, Text, TextStyle, Animation
from flet import ControlEvent, padding, ListView
from modules.color import DEEP_BLUE, BLUE
from modules.fonctions import pourcentage
from pages import variables, fichier, fonction_chapitre, pointeur, operateurs, struct_controle, struct_donnnee

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
    CHAPITRES_DESCRIPTION: list[str] = [
        '02 exercices',
        '03 exercices',
        '11 exercices',
        '04 exercices',
        '10 exercices',
        '05 exercices',
        '03 exercices',
    ]
    def __init__(self, page: Page):
        super().__init__(
            bgcolor='white',
            border_radius=10,
            expand=True,
            height=page.window.height - 70,
            padding=padding.only(pourcentage(page.window.width, 10), 15, pourcentage(page.window.width, 10)),
        )
        self.content = ListView(spacing=20, height=page.window.height - 70)
        for chapitre, icon, description in zip(Display.CHAPITRES, Display.CHAPITRES_ICONS, Display.CHAPITRES_DESCRIPTION):
            self.content.controls.append(Chapitres(chapitre, icon, description))

class Chapitres(Container):
    def __init__(self, chapitre: str, icon: str, description: str):
        super().__init__(
            bgcolor=DEEP_BLUE,
            border_radius=20,
            padding=20,
            animate_offset=Animation(500, 'ease'),
            animate=Animation(500, 'ease'),
            on_hover=self.hover,
            on_click=self.click,
            data=chapitre,
        )
        self.content = Column(
            controls=[
                Row([
                    Container(
                        blur=3,
                        padding=10,
                        content=Icon(icon, color=BLUE, animate_scale=Animation(200, 'ease')),
                        bgcolor=colors.with_opacity(.3, 'black'),
                        border_radius=10,
                    )
                ],
                 alignment=MainAxisAlignment.CENTER),
                Row([Text(chapitre.title(), expand=True, text_align='center', weight='bold', color='white', size=30, style=TextStyle(shadow=BoxShadow(1, 1, 'black38', Offset(2, 2))))]),
                Row([Text(description, expand=True, text_align='center', weight='w_700', color='white', style=TextStyle(shadow=BoxShadow(1, 1, 'black38', Offset(2, 2))))]),
            ]
        )

    @staticmethod
    def click(e: ControlEvent):
        page: Page = e.page
        display = page.controls[0].controls
        data: str = e.control.data.lower()
        print(data)
        match data:
            case 'variables': display[-1] = variables.Display(page)
            case 'fichiers': display[-1] = fichier.Display(page)
            case 'operateurs': display[-1] = operateurs.Display(page)
            case 'structures de controles': display[-1] = struct_controle.Display(page)
            case 'structures de donnees': display[-1] = struct_donnnee.Display(page)
            case 'pointeurs': display[-1] = pointeur.Display(page)
            case 'fonctions': display[-1] = fonction_chapitre.Display(page)
        page.update()
    
    def hover(self, e: ControlEvent): 
        page: Page = e.page
        if e.data == 'true': 
            self.offset = Offset(0, -.05)
            self.shadow = BoxShadow(1, 1, colors.with_opacity(.2, 'black'), Offset(2, 6))
            self.content.controls[0].controls[0].content.scale = 1.2
        else:
            self.content.controls[0].controls[0].content.scale = 1
            self.shadow = None
            self.offset = Offset(0, 0)
        page.update()