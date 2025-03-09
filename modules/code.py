from flet import Container, CupertinoTextField, Column, TextStyle, FilledButton, Row, IconButton, ButtonStyle, MainAxisAlignment
from flet import ControlEvent, Page
import subprocess
import tempfile

def create_tmp_file(data: str, extension: str = '.c') -> str:
    """Fonction qui cree un fichier temporaire et renvoit le chemin vers ce fichier

    Args:
        data (str): donnee a ecrire
        extension (str, optional): Extension du fichier. Defaults to '.c'.

    Returns:
        str: Chemin vers le fichier
    """
    with tempfile.NamedTemporaryFile(suffix=extension, delete=False) as file:
        file.write(data.encode())
        return file.name

class MiniCode(Container):
    def __init__(self, code: str = "void main() {}"):
        super().__init__(
            padding=10,
        )
        self.number_line = code.count('\n') + 1 if code.count('\n') != 0 else 1
        self.texteField = CupertinoTextField(
                value=code,
                expand=True,
                min_lines=self.number_line, 
                max_lines=self.number_line, 
                text_style=TextStyle(font_family='code'),
        )
        self.content = Row([self.texteField], alignment=MainAxisAlignment.CENTER, expand=True)


class Code(Container):
    def __init__(self, code: str = "void main() {}", num_line: int = 7):
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
            value='...',  
            expand=True,
            min_lines=4, 
            max_lines=4,
            read_only=True, 
            text_style=TextStyle(font_family='code'),
        )
        self.content = Column(
            controls=[
                Row([self.input_code], alignment=MainAxisAlignment.CENTER, expand=True),
                Row([FilledButton('Compile', icon='cupertino_play', icon_color='white', expand=True, style=ButtonStyle('white', bgcolor='green'), on_click=self.execute, on_hover=self.hover_btn), Container(IconButton('cupertino_refresh', 'white', bgcolor='red', on_click=self.reset))], expand=True),
                Row([self.output_code], alignment=MainAxisAlignment.CENTER, expand=True),
            ]
        )
        self.data = code

    def hover_btn(self, e: ControlEvent):
        btn: FilledButton = e.control
        style = btn.style
        if e.data == 'true': style.icon_size = 30
        else: style.icon_size = 25
        e.page.update()

    def reset(self, e: ControlEvent):
        """Fonction pour reinitialise le code"""
        page: Page = e.page
        self.output_code.value = '...'
        self.input_code.value = self.data
        page.update()

    def execute(self, e: ControlEvent):
        """Fonction qui execute le code de self.input_code et le met dans self.output_code"""
        page: Page = e.page
        data: str = self.input_code.value
        output = subprocess.run(['utils\\tcc\\tcc.exe', '-run', create_tmp_file(data)], capture_output=True, text=True)
        self.output_code.value = output.stderr + output.stdout
        if output.stderr == output.stdout == '':
            self.output_code.value = "Code execute avec succes"
        page.update()