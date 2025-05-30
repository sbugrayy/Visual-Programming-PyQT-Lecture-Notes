import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtGui import QPixmap

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.im = QPixmap("C:/Users/bugra/Documents/GitHub/Visual-Programming-PyQT-Lecture-Notes/Codes/04-pyqt-haftalik-uygulamalar/altincihafta/images/icon.png")
        self.label = QLabel()
        self.label.setPixmap(self.im)

        if self.im.isNull():
            self.label = QLabel("Resim yüklenemedi!")
        else:
            self.label = QLabel()
            self.label.setPixmap(self.im)

        self.grid = QGridLayout()
        self.grid.addWidget(self.label,1,1)
        self.setLayout(self.grid)

        self.setGeometry(50,50,320,200)
        self.setWindowTitle("PyQT show image")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
