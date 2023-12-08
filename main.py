from cmath import exp
import sys
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow


form_class = uic.loadUiType('MagFieldCal.ui')[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.ResultButton.clicked.connect(self.result)

    


    def result(self):
        def initialize(self): #입력값 초기화
            self.pos1.clear()
            self.pos2.clear()
            self.inten1.clear()
            self.inten2.clear()
            self.DirectResult.clear()
            self.IntenResult.clear()
        #수직으로 올라가는 방향을 + / 수직으로 내려가는 방향을 -
        
        #-----------------------------------------------------------------------------------
        try:
            pos1 = float(self.pos1.text()) #도선 1 위치
            pos2 = float(self.pos2.text()) #도선 2 위치
            inten1 = float(self.inten1.text()) #도선 1 전류 세기
            inten2 = float(self.inten2.text()) #도선 2 전류 세기
            calpos = float(self.calpos.text()) #측정하고자 하는 지점의 위치
            pm1 = 1 
            pm2 = 1
            self.ErrorMsg.setText("") #에러 메세지 초기화
            if pos1 > pos2:
                self.ErrorMsg.setText("도선 1의 위치값이 도선 2의 위치값보다 큽니다.") #도선 1 위치 > 도선 2 위치일 경우
                initialize(self)
                return 0
            if self.down1.isChecked() is False and self.up1.isChecked() is False: #도선 1의 방향이 정의되지 않았을 경우
                self.ErrorMsg.setText("도선 1의 전류의 방향이 정의되지 않았습니다.")
                initialize(self)
                return 0
            if self.down2.isChecked() is False and self.up2.isChecked() is False: #도선 2의 방향이 정의되지 않았을 경우
                self.ErrorMsg.setText("도선 2의 전류의 방향이 정의되지 않았습니다.")
                initialize(self)
                return 0
            if pos1 == calpos:
                self.ErrorMsg.setText("측정하려는 위치가 도선1의 위치와 같습니다.") #ZeroDivisonError 방지
                initialize(self)
                return 0
            if pos2 == calpos:
                self.ErrorMsg.setText("측정하려는 위치가 도선2의 위치와 같습니다.") #ZeroDivisonError 방지
                initialize(self)
                return 0
            Magby1 = inten1 / abs(pos1 - calpos) #도선 1에 의한 자기장
            Magby2 = inten2 / abs(pos2 - calpos) #도선 2에 의한 자기장
            if calpos > pos1: #도선 1의 위치값보다 측정 하려는 위치의 위치값이 [더 큰 경우]
                if self.down1.isChecked():
                    pm1 = 1
                else:
                    pm1 = -1
            else: #도선 1의 위치값보다 측정 하려는 위치의 위치값이 [더 작은 경우]
                if self.down1.isChecked():
                    pm1 = -1
                else:
                    pm1 = 1
            if calpos > pos2: #도선 2의 위치값보다 측정 하려는 위치의 위치값이 [더 큰 경우]
                if self.down1.isChecked():
                    pm2 = 1
                else:
                    pm2 = -1
            else: #도선 2의 위치값보다 측정 하려는 위치의 위치값이 [더 작은 경우]
                if self.down1.isChecked():
                    pm2 = -1
                else:
                    pm2 = 1
            MagForce = Magby1 * pm1 + Magby2 * pm2 #측정하고자 하는 지점의 자기장 세기
            if MagForce > 0:
                self.DirectResult.setText("수직으로 나오는 방향")
            elif MagForce < 0:
                self.DirectResult.setText("수직으로 들어가는 방향")
            else:
                self.DirectResult.setText("None")
            self.IntenResult.setText(f"{round(abs(MagForce), 3)}B")
            return 0
        #-----------------------------------------------------------------------------------
        except ValueError:
            self.ErrorMsg.setText("어떤 입력값에 유리수가 아닌 것이 들어갔거나, 비어있습니다.")
            initialize(self)
            return 0
        except:
            self.ErrorMsg.setText("에러가 발생했습니다.")
            initialize(self)
            return 0

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
