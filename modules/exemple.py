from flet import Container, Row, Text, Page, padding, MainAxisAlignment, Border, BorderSide
from flet import Column, BorderRadius, colors, TextStyle, Offset, BoxShadow
from .color import BG
from .fonctions import pourcentage
from .code import Code

CODE = Container(Row([Text('code', font_family='code', expand=True, text_align='center')]), padding=10, bgcolor=BG)
class Exemple(Container):
    def __init__(self, page: Page, height: int = 190, enonce: str = '...', code: Code = None):
        super().__init__(
            expand=True,
            height=height,
            padding=padding.only(pourcentage(page.window.width, 1), 15, pourcentage(page.window.width, 1)),
            border_radius=20,
        )
        self.text_style = TextStyle(color='white', shadow=BoxShadow(1, 1, 'black', Offset(2, 2)), weight='w_700', size=20)
        self.s_height = height
        self.container = Container(
                blur=5,
                expand=True,
                border_radius=20,
                bgcolor=colors.with_opacity(.3, BG),
                padding=0,
                border=Border(
                    BorderSide(4, BG),
                    BorderSide(4, BG),
                    BorderSide(4, BG),
                    BorderSide(4, BG),
                ),
                content=Column([
                    Container(Row([Text("Exemple", text_align='center', expand=True, color='white', weight='bold')]), height=40, bgcolor=BG, border_radius=BorderRadius(10, 10, 0, 0), border=Border(bottom=BorderSide(3, BG))),
                    Container(Row([Text(enonce, expand=True, text_align='center', style=self.text_style)], alignment=MainAxisAlignment.CENTER)),
                    Container(Row([code])),
                ], spacing=0, height=self.s_height)
        )
        self.content = Row([self.container], alignment=MainAxisAlignment.CENTER)