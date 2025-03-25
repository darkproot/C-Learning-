from flet import Container, Row, Column, Border, BorderSide, Text, TextStyle, Icon, icons, ControlEvent, Page
from modules.code import MiniCode
from modules.texte import Texte, Spacing

class Qcm(Container):
    def __init__(
            self, 
            question_id: int = 1,
            question: str = None,
            reponse: int = None,
            proposition: list[str] = None,
            minicode: MiniCode = None
    ):
        super().__init__()
        self.minicode = minicode
        self.reponse = reponse
        self.question_id = question_id
        self.question = question
        self.proposition = proposition
        self.question = Texte(f"{question_id}- {self.question}")
        if not self.minicode: 
            self.content = Column([Spacing(), self.question])
        else:
            self.content = Column([Spacing(), self.question, self.minicode])
        for proposition in self.proposition:
            if self.proposition.index(proposition) == self.reponse:
                self.content.controls.append(Proposition(proposition, True))
            else:
                self.content.controls.append(Proposition(proposition, False))

class Proposition(Container):
    def __init__(self, texte: str, state: bool):
        super().__init__(
            padding=10,
            border_radius=10,
            border=Border(
                BorderSide(2, 'black'),
                BorderSide(2, 'black'),
                BorderSide(2, 'black'),
                BorderSide(2, 'black')
            ),
            on_click=self.revill
        ) 
        self.state = state
        self.text_style = TextStyle(20, font_family='texte', color='black')
        self.icon = Container(
            Icon(icons.AIRPLANE_TICKET, color='white'), 
            bgcolor='green', 
            padding=10,
            border_radius=20,
        )
        self.content = Row(
            expand=True,
            controls=[
                Text(texte, style=self.text_style, expand=True),
            ]
        ) 
    def revill(self, e: ControlEvent):
        page: Page = e.page
        color: str = 'green' if self.state else 'red'
        border: Border = Border(
                BorderSide(2, color),
                BorderSide(2, color),
                BorderSide(2, color),
                BorderSide(2, color)
            )
        icon_name: str = 'check' if self.state else 'close'
        icon: Icon = Icon(icon_name, scale=1, color='white')
        self.border = border
        if len(self.content.controls) == 1:
            self.content.controls.append(Container(icon, bgcolor=color, padding=5, border_radius=20))
        page.update()