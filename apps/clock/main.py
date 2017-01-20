from kivy.app import App
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

from time import strftime

LabelBase.register(
    name='Roboto',
    fn_regular='../../static/fonts/roboto/Roboto-Thin.ttf',
    fn_bold='../../static/fonts/roboto/Roboto-Medium.ttf'
)


class ClockApp(App):
    def update_time(self, seconds):
        self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')

    def on_start(self):
        Clock.schedule_interval(self.update_time, 1)


def run():
    Window.clearcolor = get_color_from_hex('#301216')
    ClockApp().run()


if __name__ == '__main__':
    run()
