from flet import Container, Page, padding, Row, Column, Text, MainAxisAlignment, Border, BorderSide, BorderRadius
from flet import colors, TextStyle, Offset, BoxShadow
from .fonctions import pourcentage
from .color import BG, DEEP_BLUE

class Syntaxe(Container):
    def __init__(self, page: Page, height: int = 200, content: str = 'Container'):
        super().__init__(
            expand=True,
            height=height,
            padding=padding.only(pourcentage(page.window.width, 1), 15, pourcentage(page.window.width, 1)),
            border_radius=20,
        )
        self.text_shadow = TextStyle(shadow=BoxShadow(1, 1, 'black', Offset(2, 2)))
        self.s_height = height
        self.s_content = content
        self.container = Container(
            expand=True,
            border_radius=20,
            bgcolor=DEEP_BLUE,
            padding=0,
            border=Border(
                BorderSide(4, BG),
                BorderSide(4, BG),
                BorderSide(4, BG),
                BorderSide(4, BG),
            ),
            content=Column([
                Container(Row([Text("Syntaxe", text_align='center', expand=True, color='white', weight='bold')]), height=40, bgcolor=BG, border_radius=BorderRadius(10, 10, 0, 0), border=Border(bottom=BorderSide(3, BG))),
                Container(Row([Text(self.s_content, size=20, expand=True, text_align='center', color='white', style=self.text_shadow, font_family='code')]), bgcolor=colors.with_opacity(.4, 'white'), blur=5, expand=True, border_radius=BorderRadius(0, 0, 20, 20))
            ], spacing=0, height=self.s_height)
        )
        self.content = Row([self.container], alignment=MainAxisAlignment.CENTER)