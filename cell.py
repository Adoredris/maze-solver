from graphics import Point, Line

class Cell:
    def __init__(self, win, *args, **kwargs):
        if len(args) == 0:
            self._x1 = 0
            self._y1 = 0
            self._x2 = 1
            self._y2 = 1
        elif type(args[1]) == Point:
            self._x1 = args[0].x
            self._y1 = args[0].y
            self._x2 = args[1].x
            self._y2 = args[1].y
        else:
            self._x1 = args[0]
            self._y1 = args[1]
            self._x2 = args[2]
            self._y2 = args[3]

        if self._x2 < self._x1:
            self._x2, self._x1 = self._x1, self._x2
        if self._y2 < self._y1:
            self._y2, self._y1 = self._y1, self._y2

        self._win = win
        self.has_top_wall = kwargs.get('has_top_wall', True)
        self.has_bottom_wall = kwargs.get('has_bottom_wall', True)
        self.has_left_wall = kwargs.get('has_left_wall', True)
        self.has_right_wall = kwargs.get('has_right_wall', True)

        self.visited = False

    def get_center(self):
        return Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)

    def draw(self, fill_color="black"):
        if self._win is None:
            return
        top_line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        self._win.draw_line(top_line, self.has_top_wall and "black" or "white")

        bottom_line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        self._win.draw_line(bottom_line, self.has_bottom_wall and "black" or "white")

        left_line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        self._win.draw_line(left_line, self.has_left_wall and "black" or "white")

        right_line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        self._win.draw_line(right_line, self.has_right_wall and "black" or "white")

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        line = Line(self.get_center(), to_cell.get_center())
        if undo:
            fill_color = "gray"
        else:
            fill_color = "red"
        self._win.draw_line(line, fill_color)