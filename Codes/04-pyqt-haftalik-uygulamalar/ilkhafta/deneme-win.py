import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

pencere = QWidget()
pencere.resize(500, 500)
pencere.move(700, 100)
pencere.setWindowTitle('Pencere')
pencere.show()
sys.exit(app.exec_())
