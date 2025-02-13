from flet import Page, app, Row
from pages import base, chapitres
from modules import color

def main(page: Page):
    page.title = "C LEARNING"
    page.bgcolor = color.BG
    page.fonts = {
        'code': r"utils\polices\JetBrainsMono-Medium.ttf",
    }
    page.add(Row(
        [
            base.SideBar(page),
            base.Display(page),
        ]
    ))

if __name__ == '__main__':
    app(main)