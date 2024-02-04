from graphics import Window#, Point, Line
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    #line = Line(Point(20, 50), Point(200, 300))
    #win.draw_line(line, "red")
    
    #test = Cell(win, 5, 6, 30, 50)
    #test.draw()

    #test2 = Cell(win, 170, 190, 130, 150, has_left_wall = False)
    #test2.draw()

    #test.draw_move(test2, True)

    maze = Maze(50, 20, 5, 5, win)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0,0)
    maze._reset_cells_visited()

    maze.solve()

    win.wait_for_close()


main()