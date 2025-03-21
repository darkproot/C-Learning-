from flet import Page, ControlEvent, Animation, Text, TextStyle, Offset, BoxShadow, TextField, margin
from flet import Container, padding, Page, Column, colors, Image, Row, Icon, AlertDialog
from modules.fonctions import pourcentage
from modules.constantes import HEIGHT
from modules.title import GrandTitre
from modules.texte import Spacing
from modules.color import BLUE

class Display(Container):
    DEV_INFO: list[dict[str, str]] = [
        {
            'name': "Github",
            'link': "https://github.com/darkproot",
            'qr_code': r"assets//github.png",
        },
        {
            'name': "Telegram",
            'link': "https://t.me/xverse3",
            'qr_code': r"assets//xverse.png",
        },
        {
            'name': "E-mail",
            'link': "woumojohnny@gmail.com",
            'qr_code': r"assets//email.png",
        },
        {
            'name': "TikTok (X-verse)",
            'link': "https://tiktok.com/@xverse.cm",
            'qr_code': r"assets//tiktok.png",
        },
        {
            'name': "Whatsapp (The X-verse)",
            'link': "https://whatsapp.com/channel/0029Vae66be4IBhFaqZeQB3G",
            'qr_code': r"assets//whatsapp.png",
        },
    ]
    def __init__(self, page: Page):
        super().__init__(
            expand=True,
            bgcolor='white',
            border_radius=10,
            height=page.window.height - HEIGHT,
            padding=padding.only(pourcentage(page.window.width, 10), 15, pourcentage(page.window.width, 10)),
        )
        self.content = Column(
            controls=[GrandTitre(text="Informations sur le developeur", font_size=30), Spacing(20)]
        )
        for info in Display.DEV_INFO:
            self.content.controls.append(DevInformation(**info))

class DevInformation(Container):
    def __init__(self, name: str, link: str, qr_code: str):
        super().__init__(
            blur=5,
            padding=10,
            border_radius=20,
            bgcolor=colors.with_opacity(.2, BLUE),
        )
        self.name = name
        self.link = link
        self.style = TextStyle(
            size=20,
            weight='bold',
            font_family='texte',
            shadow=BoxShadow(1, 1, 'black38', Offset(2, 2)),
        )
        self.qr_code = QRCodeImage(qr_code)
        self.link_text = TextField(
            value=link,
            color='black',
            read_only=True,
            border_width=0,
            border_radius=20,
            text_style=TextStyle(font_family='texte'),
        )
        self.icon = Container(
            margin=margin.only(right=10),
            content=Icon('copy', 'white'),
        )
        self.content = Row(
            controls=[
                self.qr_code,
                Container(),
                Column(
                    expand=True,
                    controls=[
                        Row([Text(name, color='white', style=self.style)]),
                        Container(
                            expand=True,
                            border_radius=10,
                            bgcolor=colors.with_opacity(.2, 'white'),
                            content=Row(
                                controls=[Container(self.link_text, expand=True), self.icon],
                            )
                        ),
                    ]
                )
            ],
        )
        self.on_hover = self.qr_code.hover
        self.on_click = self.qr_code.click

class QRCodeImage(Container):
    IMAGE_SIZE:dict[str, str] = {
        'height': 50,
        'width': 50,
    }
    def __init__(self, path: str):
        super().__init__(
            blur=2,
            padding=10,
            border_radius=10,
            bgcolor=colors.with_opacity(.3, 'white'),
        )
        self.path = path
        self.on_hover = self.hover
        self.animate = Animation(200, 'ease')
        self.content = Image(self.path, **QRCodeImage.IMAGE_SIZE)

    def click(self, e: ControlEvent):
        """Fonction pour afficher le code QR"""
        page: Page = e.page
        page.overlay.clear()
        icon: QRCodeImage = QRCodeImage(self.path)
        icon.content.width = 200
        icon.content.height = 200
        box: AlertDialog = AlertDialog(content=Container(icon))
        page.open(box)
        page.update()


    def hover(self, e: ControlEvent):
        page: Page = e.page
        icon: Image = self.content
        if e.data == 'true':
            icon.scale = 1.1
        else:
            icon.scale = 1
        page.update()