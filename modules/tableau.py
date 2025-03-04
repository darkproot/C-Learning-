from flet import Container, Row, DataTable, DataCell, DataRow, DataColumn, Text
from flet import MainAxisAlignment, Border, BorderSide
from .color import DEEP_BLUE, BLUE

class Table(Container):
    def __init__(self, data: list[list[str | int]]):
        super().__init__(
            padding=0,
            border_radius=20,
        )
        self.data = data
        self.content = Row(
            controls=[
                DataTable(
                    border=Border(
                        BorderSide(2, DEEP_BLUE),
                        BorderSide(2, DEEP_BLUE),
                        BorderSide(2, DEEP_BLUE),
                        BorderSide(2, DEEP_BLUE),
                    ),
                    border_radius=20,
                    horizontal_lines=BorderSide(2, DEEP_BLUE),
                    vertical_lines=BorderSide(2, DEEP_BLUE),
                    expand=True,
                    columns=[]
                )
            ],
            expand=True, 
            alignment=MainAxisAlignment.CENTER,
        )
        for column in data[0]:
            self.content.controls[0].columns.append(DataColumn(Row([Texte(column, weight='bold', color=BLUE)]))) 
        for row in data[1:]:
            cache: list[DataCell] = []
            for i in row:
                cache.append(DataCell(Texte(i)))
            self.content.controls[0].rows.append(DataRow(cache))
           
class Texte(Text):
    def __init__(self, value: str, color: str = 'black', weight: str | None = None):
        super().__init__(
            font_family='texte',
            color=color,
            size=15,
            expand=True,
            weight=weight,
            text_align='center',
            value=value if type(value) == str else value,
        )