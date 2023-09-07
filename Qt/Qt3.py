#from _typeshed import FileDescriptor
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QMenuBar, QMenu, QMessageBox

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Редактор жидкого поноса")
        self.setGeometry(650, 250, 600, 500)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.createMenuBar()

    def createMenuBar(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        self.fileMenu = QMenu("&Файл", self)
        self.menuBar.addMenu(self.fileMenu)

        self.fileMenu.addAction("Открыть", self.action_clicked)
        self.fileMenu.addAction("Сохранить", self.action_clicked)


    @QtCore.pyqtSlot()
    def action_clicked(self):
        action = self.sender()
        if action.text() == "Открыть":
            f_open = QFileDialog.getOpenFileName(self)[0]

            try:
                f = open(f_open, "r")
                with f:
                    data = f.read()
                    self.text_edit.setText(data)
                f.close()
            except FileNotFoundError:
                error1 = QMessageBox()
                error1.setWindowTitle("Обосрался?)")
                error1.setText("                            Такого файла нет :(                               ")
                error1.setIcon(QMessageBox.Warning)
                error1.setStandardButtons(QMessageBox.Yes)
                

                error1.exec_()

        elif action.text() == "Сохранить":
            f_save = QFileDialog.getSaveFileName(self)[0]

            try:
                f = open(f_save, "w")
                text_file = self.text_edit.toPlainText()
                f.write(text_file)
                f.close()

            except FileNotFoundError:
                error1 = QMessageBox()
                error1.setWindowTitle("Обосрался?)")
                error1.setText("                            А чё не сохранил?                               ")
                error1.setIcon(QMessageBox.Warning)
                error1.setStandardButtons(QMessageBox.Yes)
                

                error1.exec_()



def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()