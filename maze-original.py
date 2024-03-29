from cell import Cell
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y

        self._win = win

        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self._num_cols):
            new_cells = []
            for j in range(self._num_rows):
                cell = Cell(self._win, self._x1 + i * self._cell_size_x, self._y1 + j * self._cell_size_y,
                            self._x1 + (i+1) * self._cell_size_x, self._y1 + (j+1) * self._cell_size_y)
                new_cells.append(cell)
            self._cells.append(new_cells)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
        