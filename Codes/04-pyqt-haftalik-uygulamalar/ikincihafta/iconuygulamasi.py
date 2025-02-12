import sys   
from PyQt5 import QtWidgets  
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon

def window(): 
    app = QApplication(sys.argv)
    win = QMainWindow()    
  
    win.setWindowTitle('Ilk Uygulama')  
    win.setGeometry(200,200,500,500)   
    win.setWindowIcon(QIcon('C:/Users/Nano/Desktop/pyqt-deneme/ikincihafta/icon.png'))  
    win.setToolTip('Tooltip Mesaji')   

    lbl_isim = QtWidgets.QLabel(win)
    lbl_isim.setText('Isminiz : ')
    lbl_isim.move(50,30)
  
    lbl_soyisim = QtWidgets.QLabel(win)
    lbl_soyisim.setText('Soyisminiz : ')
    lbl_soyisim.move(50,70)

    txt_isim = QtWidgets.QLineEdit(win)
    txt_isim.move(250, 30)

    txt_soyisim = QtWidgets.QLineEdit(win)
    txt_soyisim.move(250, 70)

    def clicked(self):
        print(txt_isim.text() + ' ' + txt_soyisim.text() + ' kisisi sisteme kaydedilmistir' )

    btn_kaydet = QtWidgets.QPushButton(win)
    btn_kaydet.move(250, 110)
    btn_kaydet.setText('Kaydet')

    btn_kaydet.clicked.connect(clicked) 



    win.show()  #pencere gosteriliyor
    sys.exit(app.exec_())  #pencere kapatmak icin x iconu ekleniyor

window()