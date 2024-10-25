import sys
import cmath
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QColor, QPainter, QFont, QPen
from PyQt5.QtCore import Qt, QRectF


class Window:
    def __init__(self, min_x: float, max_x: float, min_y: float,
                 max_y: float, size_x: int, size_y: int):
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


def mandel_func(x: complex, c: complex):
    return x ** 2 + c

def mandel_func_ship(x: complex, c: complex):
    return (complex(abs(x.real)+complex(0,1)*complex(abs(x.imag)))) ** 2 + c


class Widget(QWidget):

    def __init__(self, M: int, fractal: str, c_for_julia: complex):
        super().__init__()
        self.M = M
        self.fractal = fractal
        self.c_for_julia = c_for_julia

    def paintEvent(self, event):
        super().paintEvent(event)

        painter = QPainter(self)
        font = QFont("Verdana", 10)
        painter.setFont(font)
        painter.setBrush(Qt.white)
        painter.drawRect(self.rect())
        if self.fractal == "julia":
            self.julia(window, self.M, self.c_for_julia, painter)
        else:
            self.mandelbrot(window, self.M, painter)
        print("show")
        painter.setPen(QColor(0xFF, 0xFF, 0xFF))

        painter.drawLine(axes.x_axes, 0, axes.x_axes, window.size_y)
        painter.drawLine(0, axes.y_axes, window.size_x, axes.y_axes)

        painter.drawLine(window.size_x, axes.y_axes, window.size_x - arrow.length, axes.y_axes - arrow.width)
        painter.drawLine(window.size_x, axes.y_axes, window.size_x - arrow.length, axes.y_axes + arrow.width)

        painter.drawLine(axes.x_axes, 0, axes.x_axes - arrow.width, 0 + arrow.length)
        painter.drawLine(axes.x_axes, 0, axes.x_axes + arrow.width, 0 + arrow.length)
        painter.drawText(axes.x_axes - 15, axes.y_axes + 18, "0")

    def mandelbrot(self, window: Window, M: int, painter):
        scale = window.size_x / (window.max_x - window.min_x)
        for y in range(-window.size_y, window.size_y):
            for x in range(-window.size_x, window.size_x):
                a = x / scale
                b = y / scale
                c = complex(a, b)
                if abs(c) > 2:
                    continue
                z = complex(0)
                n = 0
                for n in range(M):
                    z = mandel_func(z, c)
                    if abs(z) > 2:
                        break
                if n == M - 1:

                    r = g = b = 0
                    painter.setPen(QPen(QColor(r, g, b)))
                    painter.drawPoint(x + axes.x_axes, -y + axes.y_axes)
                else:
                    r = (n % 2) * 32 + 128
                    g = (n % 4) * 64
                    b = (n % 2) * 16 + 128
                    painter.setPen(QPen(QColor(r, g, b)))
                    painter.drawRect(x + axes.x_axes, -y + axes.y_axes, 1, 1)

    def julia(self, window: Window, M: int, c: complex, painter):
        scale = window.size_x / (window.max_x - window.min_x)
        for y in range(-window.size_y, window.size_y):
            for x in range(-window.size_x, window.size_x):
                a = x / scale
                b = y / scale
                z = complex(a, b)
                n = 0
                for n in range(M):
                    z = mandel_func(z, c)
                    if abs(z) > 2:
                        break
                if n == M - 1:

                    r = g = b = 0
                    painter.setPen(QPen(QColor(r, g, b)))
                    painter.drawPoint(x + axes.x_axes, -y + axes.y_axes)
                else:
                    r = (n % 2) * 32 + 128
                    g = (n % 4) * 64
                    b = (n % 2) * 16 + 128
                    painter.setPen(QPen(QColor(r, g, b)))
                    painter.drawRect(x + axes.x_axes, -y + axes.y_axes, 1, 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window(-3, -1, -1, 1, 1000, 1000)
    arrow = Arrow(10, 5)
    axes = Axes(window)

    w = Widget(M=200, fractal="mandelbrot", c_for_julia=complex(-0.32993, 0.724465654))
    w.resize(window.size_x, window.size_y)
    w.setFixedSize(w.size())
    w.setWindowTitle('fractal')
    w.show()

    sys.exit(app.exec_())
