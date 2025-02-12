import sys
from PyQt5.QtWidgets import QWidget, QApplication

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.ozellikEkle()
    def ozellikEkle(self):
        self.resize(500, 500)
        self.move(700, 100)
        self.setWindowTitle('Pencere')

app = QApplication(sys.argv)
pencere = Pencere()
pencere.show()
sys.exit(app.exec_())
