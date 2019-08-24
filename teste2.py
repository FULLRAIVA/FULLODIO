# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teste2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from calculadoraFINAL import calculadora
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from math import sqrt
class Ui_Form(object):
    def setupUi(self, Form):
        
        Form.setObjectName("Form")
        Form.resize(242, 286)
        Form.setFixedSize(242,286)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        Form.setFont(font)
        Form.setStyleSheet("QWidget{\n"
"    background: rgb(0, 170, 255);\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"    background:rgb(0, 255, 127);\n"
"    color: rgb(255, 170, 0);\n"
"    border: 1px solid blue;\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 90, 41, 41))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background:lightblue;\n"
"    color: blue;\n"
"    border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background:white;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 90, 41, 41))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background:lightblue;\n"
"    color: blue;\n"
"    border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background:white;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 90, 41, 41))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    background:lightblue;\n"
"    color: blue;\n"
"    border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background:white;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 90, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    background:lightblue;\n"
"    color: blue;\n"
"    border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background:white;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 140, 41, 41))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    background:lightblue;\n"
"    color: blue;\n"
"    border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background:white;\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 140, 41, 41))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    background:lightblue;\n"
"    color: blue;\n"
"    border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background:white;\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(100, 140, 41, 41))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"    background:lightblue;\n"
"    color: blue;\n"
"    border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background:white;\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(150, 140, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"    background:lightblue;\n"
"    color: blue;\n"
"    border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background:white;\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(0, 190, 41, 41))
        self.pushButton_10.setStyleSheet("QPushButton{\n"
"    background:lightblue;\n"
"    color: blue;\n"
"    border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background:white;\n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setGeometry(QtCore.QRect(150, 190, 41, 41))
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"    background:lightblue;\n"
"    color: blue;\n"
"    border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background:white;\n"
"}")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(Form)
        self.pushButton_12.setGeometry(QtCore.QRect(100, 190, 41, 41))
        self.pushButton_12.setStyleSheet("QPushButton{\n"
"    background:lightblue;\n"
"    color: blue;\n"
"    border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background: white;\n"
"}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(Form)
        self.pushButton_13.setGeometry(QtCore.QRect(50, 190, 41, 41))
        self.pushButton_13.setStyleSheet("QPushButton{\n"
"    background:lightblue;\n"
"    color: blue;\n"
"    border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background:white;\n"
"}")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(Form)
        self.pushButton_14.setGeometry(QtCore.QRect(0, 240, 41, 41))
        self.pushButton_14.setStyleSheet("QPushButton{\n"
"    background:lightblue;\n"
"    color: blue;\n"
"    border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background:white;\n"
"}")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(Form)
        self.pushButton_15.setGeometry(QtCore.QRect(50, 240, 41, 41))
        self.pushButton_15.setStyleSheet("QPushButton{\n"
"    background:lightblue;\n"
"    color: blue;\n"
"    border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background:white;\n"
"}")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(Form)
        self.pushButton_16.setGeometry(QtCore.QRect(200, 240, 41, 41))
        self.pushButton_16.setStyleSheet("QPushButton{\n"
"    background:lightblue;\n"
"    color: blue;\n"
"    border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background:white;\n"
"}")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(Form)
        self.pushButton_17.setGeometry(QtCore.QRect(200, 90, 41, 141))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("QPushButton{\n"
"    background:rgb(255, 170, 0);\n"
"    color: blue;\n"
"    border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background:white;\n"
"}")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(Form)
        self.pushButton_18.setGeometry(QtCore.QRect(100, 240, 41, 41))
        self.pushButton_18.setStyleSheet("QPushButton{\n"
"    background:lightblue;\n"
"    color: blue;\n"
"    border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background:white;\n"
"}")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(Form)
        self.pushButton_19.setGeometry(QtCore.QRect(150, 240, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("QPushButton{\n"
"    background:lightblue;\n"
"    color: blue;\n"
"    border: 2px solid blue;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background:white;\n"
"}")
        self.pushButton_19.setObjectName("pushButton_19")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.entrada = ''
        Form.setWindowTitle(_translate("Form", "Calculadora do Zé"))
        self.pushButton_2.setText(_translate("Form", "7"))
        self.pushButton_3.setText(_translate("Form", "8"))
        self.pushButton_4.setText(_translate("Form", "9"))
        self.pushButton_5.setText(_translate("Form", "+"))
        self.pushButton_6.setText(_translate("Form", "4"))
        self.pushButton_7.setText(_translate("Form", "5"))
        self.pushButton_8.setText(_translate("Form", "6"))
        self.pushButton_9.setText(_translate("Form", "-"))
        self.pushButton_10.setText(_translate("Form", "1"))
        self.pushButton_11.setText(_translate("Form", "/"))
        self.pushButton_12.setText(_translate("Form", "3"))
        self.pushButton_13.setText(_translate("Form", "2"))
        self.pushButton_14.setText(_translate("Form", "0"))
        self.pushButton_15.setText(_translate("Form", "."))
        self.pushButton_16.setText(_translate("Form", "="))
        self.pushButton_17.setText(_translate("Form", "C"))
        self.pushButton_18.setText(_translate("Form", "√"))
        self.pushButton_19.setText(_translate("Form", "*"))



        self.pushButton_2.clicked.connect(self.dig7)
        self.pushButton_3.clicked.connect(self.dig8)
        self.pushButton_4.clicked.connect(self.dig9)
        self.pushButton_5.clicked.connect(self.digmais)
        self.pushButton_6.clicked.connect(self.dig4)
        self.pushButton_7.clicked.connect(self.dig5)
        self.pushButton_8.clicked.connect(self.dig6)
        self.pushButton_9.clicked.connect(self.digmenos)
        self.pushButton_10.clicked.connect(self.dig1)

        self.pushButton_11.clicked.connect(self.digdiv)
        self.pushButton_12.clicked.connect(self.dig3)
        self.pushButton_13.clicked.connect(self.dig2)

        self.pushButton_14.clicked.connect(self.dig0)
        self.pushButton_15.clicked.connect(self.digvir)
        self.pushButton_16.clicked.connect(self.calculaself) 
        self.pushButton_19.clicked.connect(self.digvezes)
        self.pushButton_17.clicked.connect(self.limpa)
        self.pushButton_18.clicked.connect(self.raiz)
        
        

    def dig7(self):
       self.entrada+='7'
       self.label.setText(self.entrada)
    def dig8(self):
       self.entrada+='8'
       self.label.setText(self.entrada)
    def dig9(self):
       self.entrada+='9'
       self.label.setText(self.entrada)
    def dig6(self):
       self.entrada+='6'
       self.label.setText(self.entrada)
    def dig5(self):
       self.entrada+='5'
       self.label.setText(self.entrada)
    def dig4(self):
       self.entrada+='4'
       self.label.setText(self.entrada)
    def dig3(self):
       self.entrada+='3'
       self.label.setText(self.entrada)
    def dig2(self):
       self.entrada+='2'
       self.label.setText(self.entrada)
    def dig1(self):
       self.entrada+='1'
       self.label.setText(self.entrada)
    def dig0(self):
       self.entrada+='0'
       self.label.setText(self.entrada)
    def digmais(self):
       self.entrada+='+'
       self.label.setText(self.entrada)
    def digmenos(self):
       self.entrada+='-'
       self.label.setText(self.entrada)
    def digvezes(self):
       self.entrada+='*'
       self.label.setText(self.entrada)
    def digdiv(self):
       self.entrada+='/'
       self.label.setText(self.entrada)
    def digvir(self):
       self.entrada+='.'
       self.label.setText(self.entrada)

    

    def limpa(self):
        self.entrada = ''
        self.label.setText(self.entrada)
    def calculaself(self):
        teste = ''
        posic = 0
        if(("*" in self.entrada) or ("/" in self.entrada) or ("-" in self.entrada) or ("+" in self.entrada)):
            try:
                calc = calculadora(self.entrada)
                calc.separa
                calc.junta
                calc.converte
                calc.calcula
                self.entrada = str(calc.getresult)
            
                self.label.setText(self.entrada)
            except:
                self.entrada = ''
                self.label.setText("ENTRADA INVALIDA!")
    def raiz(self):
        try:
            verifica =""
            posic = 0
            if(float(self.entrada)>(-1) ):
                self.entrada = sqrt(float(self.entrada))
                self.entrada = str(self.entrada)
                verifica = ""
                posic = 0
                for x in range(len(self.entrada)):
                    if(self.entrada[x]=="."):
                        posic = x
       
                for x in range(posic+1,len(self.entrada)):
                    verifica+=self.entrada[x]
                if(int(verifica)==0):
                    self.entrada = int(float(self.entrada))
                    self.entrada = str(self.entrada)
            else:
                self.entrada='NÚMERO MENOR QUE 1!'
        except:
            self.entrada='ENTRADA INVALIDA!'
        
        self.label.setText(self.entrada)
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    Window = QtWidgets.QMainWindow()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()
