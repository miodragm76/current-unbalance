import sys
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget)
from PyQt5.QtGui import QPainter, QColor, QFont,QPixmap, QPen
from PyQt5.QtCore import Qt, QPoint

from ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.point = QPoint()
        self.prev_point = QPoint()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.pix = QPixmap(200, 200)
        self.pix.fill(Qt.white)
        self.ui.draw_area.setPixmap(self.pix)


       
    def paintEvent(self,event):
        pen_width = 20
        pp = QPainter(self.pix)
        #pp.drawPixmap(self.ui.draw_area.rect(), self.pix)

        pen = QPen()
        pen.setWidth(pen_width+3)
        pen.setColor(QColor(255,255,255))
        pp.setRenderHint(QPainter.Antialiasing, True)
        pp.setPen(pen)

        pp.drawPoint(self.prev_point.x()-self.ui.draw_area.x(),self.prev_point.y()-self.ui.draw_area.y()-pen_width)
        pen = QPen()
        pen.setWidth(pen_width)
        pp.setRenderHint(QPainter.Antialiasing, True)
        pp.setPen(pen)
        #self.ui.draw_area.y()
        pp.drawPoint(self.point.x()-self.ui.draw_area.x(),self.point.y()-self.ui.draw_area.y()-pen_width)



        self.ui.draw_area.setPixmap(self.pix)
        

        
  
        #painter = QPainter(self)
        #painter.drawPixmap(0, 0, self.pix)

    def mousePressEvent(self, event) :   
         #   
        if event.button() == Qt.LeftButton :
            self.prev_point = self.point
            self.point = event.pos()
            self.update()



def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()