import sys
import cmath
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QColor, QPainter, QFont
from PyQt5.QtCore import Qt


class Window:
    def __init__(self, min_x: int, max_x: int, min_y: int,
                 max_y: int, size_x: int, size_y: int):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.size_x = size_x
        self.size_y = size_y


class Arrow:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width


class Axes:
    def __init__(self, wind: Window):
        self.x_axes = int(wind.size_x * (-wind.min_x / (wind.max_x - wind.min_x)))
        self.y_axes = int(wind.size_y * (-wind.min_y / (wind.max_y - wind.min_y)))


def mandel_func(x, c):
    return x * x + c


class Widget(QWidget):
    def paintEvent(self, event):
        super().paintEvent(event)

        painter = QPainter(self)
        font = QFont("Verdana", 10)
        painter.setFont(font)
        painter.setBrush(Qt.white)
        painter.drawRect(self.rect())

        painter.setPen(QColor(0x00, 0x00, 0x00))

        painter.drawLine(axes.x_axes, 0, axes.x_axes, window.size_y)
        painter.drawLine(0, axes.y_axes, window.size_x, axes.y_axes)

        painter.drawLine(window.size_x, axes.y_axes, window.size_x - arrow.length, axes.y_axes - arrow.width)
        painter.drawLine(window.size_x, axes.y_axes, window.size_x - arrow.length, axes.y_axes + arrow.width)

        painter.drawLine(axes.x_axes, 0, axes.x_axes - arrow.width, 0 + arrow.length)
        painter.drawLine(axes.x_axes, 0, axes.x_axes + arrow.width, 0 + arrow.length)
        painter.drawText(axes.x_axes - 15, axes.y_axes + 18, "0")

    # def mandelbrot(window, M):
    #     matrix = []
    #     for i in range (0, window.sizeX) :
    #         matrix.append([])
    #         for j in range (1, window.sizeY) :
    #             matrix[i].append([window.minX+(window.maxX-window.minX)*(i/window.sizeX),window.minY-(window.maxX-window.minX)*(i/window.sizeX)])
    #             x =complex(0,0);
    #             for l in range (0, M) :
    #                 x= mandel_func(x, complex(matrix[i][j]))
    #                 if(abs(x)>2) painter.drawPoint(i,j)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window(-5, 10, -10, 10, 500, 500)
    arrow = Arrow(10, 5)
    axes = Axes(window)

    w = Widget()
    w.resize(window.size_x, window.size_y)
    w.setFixedSize(w.size())
    w.setWindowTitle('fractal')
    w.show()

    sys.exit(app.exec_())
