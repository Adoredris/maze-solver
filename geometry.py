class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.__point1 = point1
        self.__point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.__point1.x,
                           self.__point1.y,
                           self.__point2.x,
                           self.__point2.y,
                           fill_color,
                           2)
        self.__canvas.pack(fill=BOTH, expand=1)