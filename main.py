import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtCore import Qt

class Widget(QWidget):
    def paintEvent(self, event):
        super().paintEvent(event)

        painter = QPainter(self)
        painter.setBrush(Qt.green)
        painter.drawRect(self.rect())

        painter.setPen(QColor(0x00, 0x00, 0x00))
        painter.drawLine(0,0,50,50)
        painter.drawPoint(self.width() / 2, self.height() / 2)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Widget()
    w.resize(300, 300)
    w.move(300, 300)
    w.setWindowTitle('fractal')
    w.show()

    sys.exit(app.exec_())
