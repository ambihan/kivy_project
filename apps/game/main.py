from kivy.app import App
from kivy.graphics import BorderImage, Color
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex

spacing = 15
game_size = 6


def all_cells():
    for x in range(game_size):
        for y in range(game_size):
            yield x, y


class Board(Widget):
    def __init__(self, **kwargs):
        super(Board, self).__init__(**kwargs)
        self.resize()

    def resize(self, *args):
        self.cell_size = (1.0 / game_size * (self.width - (game_size + 1) * spacing),) * 2
        self.canvas.before.clear()
        with self.canvas.before:
            BorderImage(pos=self.pos, size=self.size, source='../../static/image/board/board.png')
            Color(*get_color_from_hex('CCC0B4'))
            for board_x, board_y in all_cells():
                BorderImage(pos=self.cell_pos(board_x, board_y),
                            size=self.cell_size,
                            source='../../static/image/board/cell.png')

    on_pos = resize
    on_size = resize
    b = None

    def cell_pos(self, board_x, board_y):
        return (self.x + board_x * (self.cell_size[0] + spacing) + spacing,
                self.y + board_y * (self.cell_size[1] + spacing) + spacing)

    def reset(self):
        self.b = [[None for i in range(game_size)] for j in range[game_size]]

class GameApp(App):
    pass


def run():
    GameApp().run()


if __name__ == '__main__':
    run()
