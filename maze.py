from cell import Cell
import time
import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        win = None,
        seed = None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        if win is None:
            self._cell_size_x = 10
            self._cell_size_y = 10
        else:
            self._cell_size_x = (win.get_width() - x1 * 2) / num_cols
            # I think I actually want some extra empty space at the bottom, but anyway
            self._cell_size_y = (win.get_height() - y1 * 2) / num_rows

        self._win = win

        self._create_cells()

        if seed is not None:
            random.seed(seed)

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

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1,self._num_rows - 1)
        
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while (True):
            possible_cells = []
            if i - 1 >= 0 and self._cells[i - 1][j].visited == False:
                possible_cells.append((i - 1, j))
            if i + 1 < self._num_cols and self._cells[i + 1][j].visited == False:
                possible_cells.append((i + 1, j))

            if j - 1 >= 0 and self._cells[i][j - 1].visited == False:
                possible_cells.append((i, j - 1))
            if j + 1 < self._num_rows and self._cells[i][j + 1].visited == False:
                possible_cells.append((i, j + 1))

            if len(possible_cells) == 0:
                self._draw_cell(i, j)
                return
            
            selected_item = random.choice(possible_cells)
            #definitely need to debug this
            if i < selected_item[0]:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            elif i > selected_item[0]:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            elif j < selected_item[1]:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            elif j > selected_item[1]:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            self._break_walls_r(selected_item[0], selected_item[1])

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    #this is supposed to be some attempt at resizing the cells whenever the window size changes
    #unused right now
    def _recalc_cells(self):
        #print('recalculating')
        self._cell_size_x = (self._win.get_width() - self._x1 * 2) / self._num_cols
        self._cell_size_y = (self._win.get_height() - self._y1 * 2) / self._num_rows
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j]._x1 = self._x1 + i * self._cell_size_x
                self._cells[i][j]._y1 = self._y1 + j * self._cell_size_y
                self._cells[i][j]._x2 = self._x1 + (i+1) * self._cell_size_x
                self._cells[i][j]._y2 = self._y1 + (j+1) * self._cell_size_y

    def _animate(self):
        if self._win is None:
            return
        #theoretically checks if cells need resizing and then calls the method to do so, doesn't seem to work this way
        #if self._cell_size_x != (self._win.get_width() - self._x1 * 2) / self._num_cols or self._cell_size_y != (self._win.get_height() - self._y1 * 2) / self._num_rows:
        #    self._recalc_cells()
        self._win.redraw()
        time.sleep(0.05)
        
    def create_maze(self):
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
        
    def solve(self):
        return self._solve_dfs_r(0, 0)
        

    def _solve_dfs_r(self, i, j):
        self._animate()
        this_cell = self._cells[i][j]
        this_cell.visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        
        if i + 1 < self._num_cols:
            next_cell = self._cells[i + 1][j]
            if next_cell.visited == False and not this_cell.has_right_wall:
                this_cell.draw_move(next_cell)
                if self._solve_dfs_r(i + 1, j):
                    return True
                this_cell.draw_move(next_cell, True)
        
        if j + 1 < self._num_rows:
            next_cell = self._cells[i][j + 1]
            if next_cell.visited == False and not this_cell.has_bottom_wall:
                this_cell.draw_move(next_cell)
                if self._solve_dfs_r(i, j + 1):
                    return True
                this_cell.draw_move(next_cell, True)

        if i - 1 >= 0:
            next_cell = self._cells[i - 1][j]
            if next_cell.visited == False and not this_cell.has_left_wall:
                this_cell.draw_move(next_cell)
                if self._solve_dfs_r(i - 1, j):
                    return True
                this_cell.draw_move(next_cell, True)
            
        if j - 1 >= 0:
            next_cell = self._cells[i][j - 1]
            if next_cell.visited == False and not this_cell.has_top_wall:
                this_cell.draw_move(next_cell)
                if self._solve_dfs_r(i, j - 1):
                    return True
                this_cell.draw_move(next_cell, True)

        return False
            
            
        
        

    def _solve_astar(self, i, j):
        pass