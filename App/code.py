from PyQt5 import QtWidgets
from App.design import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox


class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)  # here we setup ui file
        self.XScore = 0
        self.YScore = 0
        self.msg = QMessageBox()
        self.dic = {}
        self.reset()
        self.turn = 'X'
        self.Restart_Button.clicked.connect(self.reset)
        self.Button_0.clicked.connect(lambda: self.game(self.Button_0, self.turn, 0))
        self.Button_1.clicked.connect(lambda: self.game(self.Button_1, self.turn, 1))
        self.Button_2.clicked.connect(lambda: self.game(self.Button_2, self.turn, 2))
        self.Button_3.clicked.connect(lambda: self.game(self.Button_3, self.turn, 3))
        self.Button_4.clicked.connect(lambda: self.game(self.Button_4, self.turn, 4))
        self.Button_5.clicked.connect(lambda: self.game(self.Button_5, self.turn, 5))
        self.Button_6.clicked.connect(lambda: self.game(self.Button_6, self.turn, 6))
        self.Button_7.clicked.connect(lambda: self.game(self.Button_7, self.turn, 7))
        self.Button_8.clicked.connect(lambda: self.game(self.Button_8, self.turn, 8))

    def message_box(self, message_info):
        self.msg.setWindowTitle("Result's")
        self.msg.setText(message_info)
        self.msg.setIcon(QMessageBox.Information)
        self.msg.exec_()
        self.reset()

    def game(self, button, turn, position):
        if self.dic[position] is None:
            button.setText(str(turn))
            self.dic[position] = turn
            check = self.check_dic(position)
            if check == 'Draw':
                self.message_box(check)
            elif check != 0:
                self.result()
                self.message_box(f"{turn} Win's")
            else:
                self.change_turn()

    def result(self):
        if self.turn == 'X':
            self.XScore = self.XScore + 1
            self.XScoreLabel.setText(str(self.XScore))
        else:
            self.YScore = self.YScore + 1
            self.OScoreLabel.setText(str(self.YScore))

    def change_turn(self):
        if self.turn == 'X':
            self.MessageLabel.setText("O's Turn")
            self.turn = 'O'
        elif self.turn == 'O':
            self.MessageLabel.setText("X's Turn")
            self.turn = 'X'

    def check_dic(self, position):
        valid_combinations = {
            0: [[0, 1, 2], [0, 3, 6], [0, 4, 8]],
            1: [[1, 4, 7], [0, 1, 2]],
            2: [[0, 1, 2], [2, 5, 8], [2, 4, 6]],
            3: [[3, 4, 5], [0, 3, 6]],
            4: [[0, 4, 8], [1, 4, 7], [2, 4, 6], [3, 4, 5]],
            5: [[2, 5, 8], [3, 4, 5]],
            6: [[6, 7, 8], [0, 3, 6], [2, 4, 6]],
            7: [[1, 4, 7], [6, 7, 8]],
            8: [[0, 4, 8], [2, 5, 8], [6, 7, 8]]
        }
        temp_list = valid_combinations[position]
        for temp1 in temp_list:
            if (self.dic[temp1[0]] is None) or (self.dic[temp1[1]] is None) or (self.dic[temp1[2]] is None):
                continue
            elif self.dic[temp1[0]] == self.dic[temp1[1]] == self.dic[temp1[2]]:
                return self.dic[temp1[0]]
            else:
                t = []
                for key in self.dic.keys():
                    if self.dic[key] == 'X' or self.dic[key] == 'O':
                        t.append(True)
                    else:
                        t.append(False)
                if all(t):
                    return "Draw"
        else:
            return 0

    def reset(self):
        self.turn = 'X'
        self.Button_6.setText("")
        self.Button_7.setText("")
        self.Button_8.setText("")
        self.Button_5.setText("")
        self.Button_4.setText("")
        self.Button_3.setText("")
        self.Button_2.setText("")
        self.Button_1.setText("")
        self.Button_0.setText("")
        self.MessageLabel.setText("X's Turn")
        for i in range(9):
            self.dic[i] = None


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = MyMainWindow()
    win.show()
    app.exec_()