from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont 
from PyQt5.QtWidgets import *
from instr import *
from second_win import *

class MainWin(QWidget):
    def __init__(self):
        ''' окно, в котором располагается приветствие '''
        super().__init__()
        # создаём и настраиваем графические элементы:
        self.initUI()
        #устанавливает связи между элементами
        self.connects()
        #устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()
        # старт:
        self.show()

    def initUI(self):
        ''' создаёт графические элементы '''
        self.btn_next = QPushButton(txt_next, self)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.v = QVBoxLayout()
        self.l1 = QLabel('123')
        self.v.addWidget(self.l1)  
        self.v.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.v.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.v.addWidget(self.btn_next, alignment = Qt.AlignCenter)
         
        self.setLayout(self.v)

    def next_click(self):
        self.tw = TestWin()
        self.hide()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)


app = QApplication([])
mw = MainWin()
app.exec_()
