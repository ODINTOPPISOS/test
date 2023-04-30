from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from instr import *
#from second_win import *
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI() 
        self.connects() 
        self.show() 
    def set_appear(self): 
        self.setWindowTitle(txt_title)
        self.resize(1000, 600)
        self.move(200, 100)
    def connects(self):
        self.b4.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()

    def initUI(self):
        self.l1 = QLabel('Введите Ф.И.О.:')
        self.l2 = QLabel('Полных лет:')
        self.l3 = QLabel('Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер.Результат запишите в соответствующее поле.')
        self.l4 = QLabel('Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания",чтобы запустить счетчик приседаний.')
        self.l5 = QLabel(txt_test3)
        self.l6 = QLabel('147')
        self.b1 = QPushButton('Начать первый тест')
        self.b2 = QPushButton('Начать делать приседания')
        self.b3 = QPushButton('Начать финальный тест')
        self.b4 = QPushButton('Результаты')
        self.e1 = QLineEdit("Ф.И.О.")
        self.e2 = QLineEdit('0')
        self.e3 = QLineEdit('0')
        self.e4 = QLineEdit('0')
        self.e5 = QLineEdit('0')
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.l_line.addWidget(self.l1)
        self.l_line.addWidget(self.e1)
        self.l_line.addWidget(self.l2)
        self.l_line.addWidget(self.e2)
        self.l_line.addWidget(self.l3)
        self.l_line.addWidget(self.b1)
        self.l_line.addWidget(self.e3)
        self.l_line.addWidget(self.l4)
        self.l_line.addWidget(self.b2)
        self.l_line.addWidget(self.l5)
        self.l_line.addWidget(self.b3)
        self.l_line.addWidget(self.e4)
        self.l_line.addWidget(self.e5)
        self.l_line.addWidget(self.b4)

        self.r_line.addWidget(self.l6)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

app = QApplication([])
mw = MainWin()
mw.show()
app.exec_()