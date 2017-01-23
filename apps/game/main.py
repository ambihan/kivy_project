from kivy.app import App
from kivy.graphics import BorderImage, Color
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
from kivy.properties import ListProperty, NumericProperty
from kivy.core.window import Keyboard

import random

key_vectors = {
    Keyboard.keycodes['up']: (0, 1),
    Keyboard.keycodes['down']: (0, -1),
    Keyboard.keycodes['left']: (-1, 0),
    Keyboard.keycodes['right']: (1, 0)
}


class Board(Widget):
    def __init__(self, **kwargs):
        print '__init__'
        super(Board, self).__init__(**kwargs)
        self.cell_size = (0, 0)
        self.spacing = 15
        self.game_size = 5
        self.b = [[None for i in range(self.game_size)] for j in range(self.game_size)]
        self.resize()

    def on_key_down(self, window, key, *args):
        if key in key_vectors:
            self.move(*key_vectors[key])

    def new_tile(self, *args):
        empty_cells = [(x, y) for x, y in self.all_cells() if self.b[x][y] is None]
        x, y = random.choice(empty_cells)
        tile = Tile(pos=self.cell_pos(x, y), size=self.cell_size)
        self.b[x][y] = tile
        self.add_widget(tile)

    def resize(self, *args):
        print 'resize'
        self.cell_size = (1.0 / self.game_size * (self.width - (self.game_size + 1) * self.spacing),) * 2
        self.canvas.before.clear()
        with self.canvas.before:
            BorderImage(pos=self.pos, size=self.size, source='../../static/image/board/board.png')
            Color(*get_color_from_hex('CCC0B4'))
            for board_x, board_y in self.all_cells():
                BorderImage(pos=self.cell_pos(board_x, board_y),
                            size=self.cell_size,
                            source='../../static/image/board/cell.png')
                tile = self.b[board_x][board_y]
                if tile:
                    tile.resize(pos=self.cell_pos(board_x, board_y), size=self.cell_size)

    def reset(self):
        print 'reset'
        self.b = [[None for i in range(self.game_size)] for j in range(self.game_size)]
        self.new_tile()
        self.new_tile()

    def all_cells(self):
        for x in range(self.game_size):
            for y in range(self.game_size):
                yield x, y

    def cell_pos(self, board_x, board_y):
        return (self.x + board_x * (self.cell_size[0] + self.spacing) + self.spacing,
                self.y + board_y * (self.cell_size[1] + self.spacing) + self.spacing)

    def valid_cell(self, board_x, board_y):
        return 0 <= board_x < self.game_size and 0 <= board_y < self.game_size

    def can_move(self, board_x, board_y):
        return self.valid_cell(board_x, board_y) and self.b[board_x][board_y] is None

    on_pos = resize
    on_size = resize


class Tile(Widget):
    colors = (
        'EEE4DA', 'EDE0C8', 'F2B179', 'F59563',
        'F67C5F', 'F65E3B', 'EDCF72', 'EDCC61',
        'EDC850', 'EDC53F', 'EDC22E')
    tile_colors = {2 ** i: color for i, color in enumerate(colors, start=1)}
    font_size = NumericProperty(24)
    number = NumericProperty(2)
    color = ListProperty(get_color_from_hex(tile_colors[2]))
    number_color = ListProperty(get_color_from_hex('776E65'))

    def __init__(self, number=2, **kwargs):
        super(Tile, self).__init__(**kwargs)
        self.font_size = 0.5 * self.width
        self.number = number
        self.update_colors()

    def update_colors(self):
        self.color = get_color_from_hex(self.tile_colors[self.number])
        if self.number > 4:
            self.number_color = get_color_from_hex('F9F6F2')

    def resize(self, pos, size):
        self.pos = pos
        self.size = size
        self.font_size = 0.5 * self.width


class GameApp(App):
    def on_start(self):
        print 'on_start'
        board = self.root.ids.board
        board.reset()


def run():
    GameApp().run()


if __name__ == '__main__':
    run()
