from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont 
from PyQt5.QtWidgets import *
from instr import *

class FinalWin(QWidget):
    def __init__(self, exp):
        ''' окно, в котором проводится опрос '''
        super().__init__()
        self.exp = exp
        print(self.exp)
        self.index = (4 * (int(self.exp[1]) + int(self.exp[2]) + int(self.exp[3])) - 200) / 10
       #получаем данные об эксперименте

        # создаём и настраиваем графические элементы:
        self.initUI()


        #устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()
        
        # старт:
        self.show()

    def results(self):
        if self.exp.age < 7:
            self.index = 0
            return "нет данных для такого возраста"
        self.index = (4 * (int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t3)) - 200) / 10
        if self.exp.age == 7 or self.exp.age == 8:
            if self.index >= 21:
                return txt_res1
            elif self.index < 21 and self.index >= 17:
                return txt_res2
            elif self.index < 17 and self.index >= 12:
                return txt_res3
            elif self.index < 12 and self.index >= 6.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 9 or self.exp.age == 10:
            if self.index >= 19.5:
                return txt_res1
            elif self.index < 19.5 and self.index >= 15.5:
                return txt_res2
            elif self.index < 15.5 and self.index >= 10.5:
                return txt_res3
            elif self.index < 10.5 and self.index >= 5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 11 or self.exp.age == 12:
            if self.index >= 18:
                return txt_res1
            elif self.index < 18 and self.index >= 14:
                return txt_res2
            elif self.index < 14 and self.index >= 9:
                return txt_res3
            elif self.index < 9 and self.index >= 3.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 13 or self.exp.age == 14:
            if self.index >= 16.5:
                return txt_res1
            elif self.index < 16.5 and self.index >= 12.5:
                return txt_res2
            elif self.index < 12.5 and self.index >= 7.5:
                return txt_res3
            elif self.index < 7.5 and self.index >= 2:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index < 15 and self.index >= 11:
                return txt_res2
            elif self.index < 11 and self.index >= 6:
                return txt_res3
            elif self.index < 6 and self.index >= 0.5:
                return txt_res4
            else:
                return txt_res5


    def initUI(self):
        ''' создаёт графические элементы '''
        table = f'Уровень От 15 лет и старше 13–14 лет 11–12 лет 9–10 лет 7–8 лет \n\
Низкий От 15 и более 16.5 и более 18 и более 19.5 и более 21 и более \n\
Удовлет 11–14.9 12.5–16.4 14–17.9 15.5–19.4 17–20.9\n\
Средний 6–10.9 7.5–12.4 9–13.9 10.5–15.4 12–16.9\n\
Выше среднего 0.5–5.9 2–7.4 3.5–8.9 5–10.4 6.5–11.9\n\
Высокий 0.4 и менее 1.9 и менее 3.4 и менее 4.9 и менее 6.4 и менее'
        self.work_text = QLabel(table)
        self.index_text = QLabel(txt_index + str(self.index))


        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.work_text, alignment = Qt.AlignCenter)        
        self.setLayout(self.layout_line)


    ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)


        