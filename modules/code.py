from flet import Container, CupertinoTextField, Column, TextStyle, FilledButton, Row, IconButton, ButtonStyle, MainAxisAlignment, icons
from flet import ControlEvent, Page, Animation
from modules.texte import Texte, Spacing
import subprocess
import tempfile

BASE: str = r"""#include <stdio.h>

int main() {
    printf("Hello World!\n");
}"""

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
                read_only=True,
        )
        self.content = Row([self.texteField], alignment=MainAxisAlignment.CENTER, expand=True)

class ExerciceCode(Container):
    def __init__(self, text: str = '', code: str = BASE, number_of_line: int = 0, solution: str = 'void main() {}'):
        super().__init__()
        self.solution = solution
        self.texte = text
        self.code = code
        self.number_line = code.count('\n') + 1 if not number_of_line else number_of_line
        self.compile_btn = FilledButton('Compile', icon='cupertino_play', icon_color='white', expand=True, style=ButtonStyle('white', bgcolor='green'), on_click=self.execute, on_hover=self.hover_btn)
        self.revill_btn = Container(IconButton('upload', 'white', bgcolor='orange', on_click=self.revill))
        self.clear_btn = Container(IconButton('cupertino_refresh', 'white', bgcolor='red', on_click=self.reset))
        self.add_line_btn = Container(IconButton('add', 'white', bgcolor='blue400', on_click=self.number_of_line_update, data='add'))
        self.remove_line_btn = Container(IconButton('remove', 'white', bgcolor='blue', on_click=self.number_of_line_update, data='remove'))
        self.texteField = CupertinoTextField(
                value=code,
                expand=True,
                multiline=True,
                min_lines=self.number_line, 
                max_lines=self.number_line, 
                text_style=TextStyle(font_family='code'),
                animate_size=Animation(600, 'ease'),
        )
        self.output_code = CupertinoTextField(
                value='...',  
                expand=True,
                min_lines=4, 
                max_lines=4,
                read_only=True, 
                text_style=TextStyle(font_family='code'),
        )
        self.content = Column([
            Texte(self.texte), Spacing(),
            Row([self.texteField], alignment=MainAxisAlignment.CENTER, expand=True),
            Row([self.compile_btn, self.clear_btn, self.revill_btn, self.add_line_btn, self.remove_line_btn], expand=True),
            Row([self.output_code]),
        ])

    def number_of_line_update(self, e: ControlEvent): 
        page: Page = e.page
        input_code: CupertinoTextField = self.texteField
        number_of_line: int = 1 if e.control.data == 'add' else -1
        input_code.min_lines += number_of_line
        input_code.max_lines += number_of_line
        page.update()

    def hover_btn(self, e: ControlEvent):
        btn: FilledButton = e.control
        style = btn.style
        if e.data == 'true': style.icon_size = 30
        else: style.icon_size = 25
        e.page.update()

    def reset(self, e: ControlEvent):
        """Fonction pour reinitialise le code"""
        page: Page = e.page
        number_of_line: int = self.code.count('\n') + 1
        self.output_code.value = '...'
        self.texteField.value = self.code
        self.texteField.max_lines = number_of_line
        self.texteField.min_lines = number_of_line
        page.update()

    def revill(self, e: ControlEvent): 
        """Fonction pour afficher la solution a de l'exercise"""
        page: Page = e.page
        number_of_line: int = self.solution.count('\n') + 1
        self.texteField.value = self.solution
        self.texteField.max_lines = number_of_line
        self.texteField.min_lines = number_of_line
        page.update()

    def execute(self, e: ControlEvent):
        """Fonction qui execute le code de self.input_code et le met dans self.output_code"""
        page: Page = e.page
        data: str = self.texteField.value
        output = subprocess.run(['utils\\tcc\\tcc.exe', '-run', create_tmp_file(data)], capture_output=True, text=True)
        self.output_code.value = output.stderr + output.stdout
        if output.stderr == output.stdout == '':
            self.output_code.value = "Code execute avec succes"
        page.update()

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
            multiline=True,
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