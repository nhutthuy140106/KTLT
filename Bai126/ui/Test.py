from PyQt6.QtWidgets import QApplication, QMainWindow

from K24406H.Chuong6_ThuVien.Bai126.ui.MainWindow126EXT import MainWindow126EXT

app=QApplication([])
MainWindow=QMainWindow()
myui=MainWindow126EXT()
myui.setupUi(MainWindow)
myui.showWindow()
app.exec()