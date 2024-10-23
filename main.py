import sys
import cmath
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QColor, QPainter, QFont
from PyQt5.QtCore import Qt

class Window :
    def __init__(self,minX, maxX, minY, maxY, sizeX, sizeY):
        self.minX = minX
        self.maxX = maxX
        self.minY = minY
        self.maxY = maxY
        self.sizeX = sizeX
        self.sizeY = sizeY

class Arrow :
    def __init__(self,length, width):
        self.length = length
        self.width = width
        
class Axes :
    def __init__(self, window):
        self.xAxes = window.sizeX*(-window.minX/(window.maxX-window.minX))
        self.yAxes = window.sizeY*(-window.minY/(window.maxY-window.minY))

def mandel_func(x, c):
    return x*x+c

class Widget(QWidget):
    def paintEvent(self, event):
        super().paintEvent(event)

        painter = QPainter(self)
        font =  QFont("Verdana", 10);
        painter.setFont(font)
        painter.setBrush(Qt.white)
        painter.drawRect(self.rect())

        painter.setPen(QColor(0x00, 0x00, 0x00))

        painter.drawLine(axes.xAxes,0,axes.xAxes,window.sizeY)
        painter.drawLine(0,axes.yAxes,window.sizeX,axes.yAxes)

        painter.drawLine(window.sizeX, axes.yAxes, window.sizeX-arrow.length, axes.yAxes-arrow.width)
        painter.drawLine(window.sizeX, axes.yAxes, window.sizeX-arrow.length, axes.yAxes+arrow.width)

        painter.drawLine(axes.xAxes, 0, axes.xAxes-arrow.width, 0+arrow.length)
        painter.drawLine(axes.xAxes, 0, axes.xAxes+arrow.width, 0+arrow.length)
        painter.drawText(axes.xAxes-15, axes.yAxes+18, "0")

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
    w.resize(window.sizeX, window.sizeY)
    w.setFixedSize(w.size())
    w.setWindowTitle('fractal')
    w.show()

    sys.exit(app.exec_())
