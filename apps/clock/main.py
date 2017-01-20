from kivy.app import App
from kivy.core.text import LabelBase

LabelBase.register(
    name='Roboto',
    fn_regular='../../static/fonts/roboto/Roboto-Thin.ttf',
    fn_bold='../../static/fonts/roboto/Roboto-Medium.ttf'
)


class ClockApp(App):
    pass


def run():
    ClockApp().run()


if __name__ == '__main__':
    run()
