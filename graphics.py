from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__height = height
        self.__width = width

    # using the canvas winfo_height property seems kind of cool, 
    # but the initial value of that method is a 1, then quickly changes to the real value
    def get_height(self):
        #return self.__canvas.winfo_height()
        return self.__height
    
    # using the canvas winfo_width property seems kind of cool, 
    # but the initial value of that method is a 1, then quickly changes to the real value
    def get_width(self):
        #return self.__canvas.winfo_width()
        return self.__width

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while (self.__running):
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    #def draw_cell(self, cell, fill_color="black"):
    #    cell.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.__point1 = point1
        self.__point2 = point2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.__point1.x,
                           self.__point1.y,
                           self.__point2.x,
                           self.__point2.y,
                           fill=fill_color,
                           width=2)
        canvas.pack(fill=BOTH, expand=1)


