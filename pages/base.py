from flet import Container, Column, Page, Row, Text, MainAxisAlignment, padding
from flet import Animation, ControlEvent, Border, BorderSide, icons, Icon
from modules.color import DEEP_BLUE, BLUE, BG
from pages import chapitres
from modules.fonctions import pourcentage

def change_page(e: ControlEvent): 
    page: Page = e.page
    data: str = e.control.data.lower()
    display = page.controls[0].controls
    match data:
        case 'chapitres':
            display[-1] = chapitres.Display(page)
        case 'home':
            display[-1] = Display(page)
    page.update()

class SideBar(Container):
    OPTIONS: list[str] = [
        'home',
        'chapitres',
        'exercices',
        'a propos',
    ]
    OPTIONS_ICON: list[str] = [
        icons.HOME,
        icons.KEYBOARD_OPTION_KEY_SHARP,
        icons.PRODUCTION_QUANTITY_LIMITS_OUTLINED,
        icons.HELP,
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
        ),
        self.content = Column([Row([Text("PlaceHolder", text_align='center', expand=True, color=DEEP_BLUE, weight='bold', size=50)])], alignment=MainAxisAlignment.CENTER)