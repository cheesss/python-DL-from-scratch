import sys
import openpyxl
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("saeon.ui")[0]



class MainClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.button_save_Function)
        # self.pushButton_2.clicked.connect(self.button_info_Function)

    # product_list = []   #전역 리스트 선언 시도해보기!
        # btn_save이 눌리면 작동할 함수
    def button_save_Function(self):
        list_num = []
        self.lineEdit.text()
        print(self.lineEdit.text())
        list_num.append(self.lineEdit.text())
        print(list_num)
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet['A1'] = self.lineEdit.text()
        wb.save('list_num.xlsx')
        # ============================
        self.lineEdit_2.text()
        print(self.lineEdit_2.text())
        list_num.append(self.lineEdit_2.text())
        print(list_num)
        # wb = openpyxl.Workbook()
        sheet = wb.active
        sheet['B1'] = self.lineEdit_2.text()
        wb.save('list_num.xlsx')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainClass()
    window.show()
    app.exec_()