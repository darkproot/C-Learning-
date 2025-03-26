from flet import Container, Column, Page, Row, Text, MainAxisAlignment, padding, colors, CrossAxisAlignment
from flet import Animation, ControlEvent, Border, BorderSide, icons, Icon, Image, TextStyle, Offset, BoxShadow
from modules.color import DEEP_BLUE, BLUE, BG
from pages import chapitres
from modules.fonctions import pourcentage
from pages.exercises import base
from pages import a_propos
from pages import dev_info

def change_page(e: ControlEvent): 
    page: Page = e.page
    data: str = e.control.data.lower()
    display = page.controls[0].controls
    match data:
        case 'chapitres':
            display[-1] = chapitres.Display(page)
        case 'home':
            display[-1] = Display(page)
        case 'exercices':
            display[-1] = base.Display(page)
        case 'a propos':
            display[-1] = a_propos.Display(page)
        case 'dev infomations':
            display[-1] = dev_info.Display(page)
    page.update()

class SideBar(Container):
    OPTIONS: list[str] = [
        'home',
        'chapitres',
        'exercices',
        'a propos',
        'dev infomations',
    ]
    OPTIONS_ICON: list[str] = [
        icons.HOME,
        icons.KEYBOARD_OPTION_KEY_SHARP,
        icons.ASSIGNMENT,
        icons.HELP,
        icons.DEVELOPER_MODE,
    ]
    def __init__(self, page: Page):
        super().__init__(
            padding=10,
            width=pourcentage(page.window.width, 10),
            height=page.window.height - 70,
            bgcolor=BG,
            border_radius=10,
            animate=Animation(500, 'bounceOut'),
            on_hover=self.hover,
        )
        self.content = Column(
            alignment=MainAxisAlignment.CENTER
        )
        for option, icon in zip(SideBar.OPTIONS, SideBar.OPTIONS_ICON):
            self.content.controls.append(Option(icon, option, change_page))

    def hover(self, e: ControlEvent):
        page: Page = e.page
        options: list[Option] = page.controls[0].controls[0].content.controls
        if e.data == 'true':
            self.width = pourcentage(page.window.width, 30)
            for option in options:
                option.content.controls[0].expand = False
                option.content.controls.append(Text(option.data, text_align='center', weight='bold'))
        else:
            self.width = pourcentage(page.window.width, 10)
            for option in options:
                option.content.controls[0].expand = True
                option.content.controls.pop()
        page.update()

class Option(Container):
    def __init__(self, icon_name: str, text: str, on_click = None):
        super().__init__(
            padding=padding.only(5, 10, 5, 10),
            border_radius=20,
            border=Border(
                BorderSide(2, BLUE),
                BorderSide(2, BLUE),
                BorderSide(2, BLUE),
                BorderSide(2, BLUE),
            ),
            on_hover=self.hover,
            animate=Animation(500, 'ease'),
            data=text.capitalize(),
            on_click=on_click,
        )
        self.icon_name = icon_name
        self.text = text
        self.content = Row([Icon(self.icon_name, expand=True, color=BLUE, animate_scale=Animation(200, 'ease'))])

    def hover(self, e: ControlEvent):
        page: Page = e.page
        if e.data == 'true':
            self.bgcolor = BLUE
            self.content.controls[0].scale = 1.2
            self.content.controls[0].color = 'white'
        else: 
            self.content.controls[0].color = BLUE
            self.content.controls[0].scale = 1
            self.bgcolor = None
        page.update()

class Display(Container):
    def __init__(self, page: Page):
        super().__init__(
            bgcolor='white',
            border_radius=10,
            expand=True,
            height=page.window.height - 70,
            padding=padding.only(pourcentage(page.window.width, 10), 15, pourcentage(page.window.width, 10)),
        )
        self.content = Column(
            controls=[
                Container(
                    content=Column([
                        Row([Logo(r"assets\logo.png")], expand=True, alignment=MainAxisAlignment.CENTER),
                        Row([Name("C Learning")], expand=True, alignment=MainAxisAlignment.CENTER),
                    ], spacing=40)
                )
            ],
            alignment=MainAxisAlignment.CENTER,
        )

class Logo(Container):
    def __init__(self, path: str):
        super().__init__(
            blur=5,
            border_radius=150,
            bgcolor=colors.with_opacity(.2, DEEP_BLUE),
        )
        self.data = 'a propos'
        self.path = path
        self.animate = Animation(200, 'ease')
        self.content = Image(
            self.path, 
            border_radius=20,
            animate_scale=self.animate,
            height=250,
            width=250,
        )
        self.on_hover = self.hover
        self.on_click = change_page

    def hover(self, e: ControlEvent):
        page: Page = e.page
        if e.data == 'true':
            self.content.scale = 1.15
        else:
            self.content.scale = 1
        page.update()

class Name(Container):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.expand = True
        self.text_style = TextStyle(
            size=70,
            weight='bold',
            color=colors.with_opacity(.5, BLUE),
            font_family='texte',
            shadow=BoxShadow(0, 1, 'black12', Offset(3, 3)),
        )
        self.content = Column(
            controls=[
                Text("Bienvenue sur", font_family='texte', color='black', weight='bold', size=30),
                Text(self.name, style=self.text_style, expand=True),
            ],
            spacing=0,
            expand=True,
            horizontal_alignment=CrossAxisAlignment.CENTER,
        )