from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import random

class Window(QMainWindow):
    # Создание конструктора
    def __init__(self):
        super(Window, self).__init__()
        # Называет окно
        self.setWindowTitle("Govno iz jopy") 
        # Первые два аргкмента указывают на смещение окна по X и Y, а вторые два указывают его размер в пикселях
        self.setGeometry(800, 400, 350, 250)

        self.new_text = QtWidgets.QLabel(self)
        # Указывает окно в котором будет расположен наш текст
        self.main_text = QtWidgets.QLabel(self)
        # Вводит сам текст
        self.main_text.setText("Jopa")
        # Позволяет двигать обьект
        self.main_text.move(155, 75)
        # Позволяет настроить размер выделенный в окне под текст
        self.main_text.adjustSize()
        # Создаёт кнопку
        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(130, 100)
        self.btn.setText("Nasrst'")
        self.btn.adjustSize()
        self.btn.clicked.connect(self.add_button)

    def add_button(self):
        x = random.randint(10, 340)
        y = random.randint(10,240)
        self.new_text.setText('Govno')
        self.new_text.adjustSize()
        self.new_text.move(x, y)
        

def application():
    # Создаёт программу
    app = QApplication(sys.argv)
    window = Window()
    # Позволяет нам увидеть наше окно
    window.show()
    # Позволяет нам закрыть программу
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()