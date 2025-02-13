from flet import Container, CupertinoTextField, Column, TextStyle, FilledButton, Row, IconButton, ButtonStyle, MainAxisAlignment
from .color import DEEP_BLUE

class Code(Container):
    def __init__(self, code: str = "int a = 4;", num_line: int = 7):
        super().__init__(
            padding=20,
            border_radius=20,
            bgcolor=None,
            blur=1,
            expand=True,
            width=400
        )
        self.input_code = CupertinoTextField(
            value=code,
            expand=True,
            min_lines=num_line, 
            max_lines=num_line, 
            text_style=TextStyle(font_family='code'),
        )
        self.output_code = CupertinoTextField(
            value='output',  
            expand=True,
            min_lines=5, 
            max_lines=5, 
            text_style=TextStyle(font_family='code'),
        )
        self.content = Column(
            controls=[
                Row([self.input_code], alignment=MainAxisAlignment.CENTER, expand=True),
                Row([FilledButton('Compile', icon='cupertino_play', icon_color='white', expand=True, style=ButtonStyle('white', bgcolor='green')), IconButton('clear', 'white', bgcolor='red')], expand=True),
                Row([self.output_code], alignment=MainAxisAlignment.CENTER, expand=True),
            ]
        )