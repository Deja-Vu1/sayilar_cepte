# -*- coding: utf-8 -*-
#              ,  ,
#             / \/ \,'| _
#            ,'    '  ,' |,|
#           ,'           ' |,'|
#          ,'                 ;'| _
#         ,'                    '' |
#        ,'                        ;-,
#       (___                        /
#     ,'    `.  ___               ,'  +------------+
#    :       ,`'   `-.           /    | BIS TECH.  |
#    |-._ o /         \         /    <_____________+
#   (    `-(           )       /
#  ,'`.     \      o  /      ,'
# /    `     `.     ,'      /
#(             `"""'       /
# `._                     /
#    `--.______        ''`.
#       \__,__,`---._   '`;
#            ))`-^--')`,-'
#          ,',_____,'  |
#          \_          `).
#  -DejaVu- `.      _,'  `
#            /`-._,-'      \


from PyQt5 import QtCore, QtGui, QtWidgets
import random


class Ui_Sayilar(object):
    def setupUi(self, Sayilar):
        self.quests = ["ASAL SAYI","TAM SAYI","DOĞAL SAYI","İRRASYONEL"]
        self.allnum = {"e":"İrrasyonel","φ":"İrrasyonel","Ω":"İrrasyonel","π":"İrrasyonel","-12":"Tam Sayı","-11":"Tam Sayı","-10":"Tam Sayı","-9":"Tam Sayı","-8":"Tam Sayı","-7":"Tam Sayı","-6":"Tam Sayı","-5":"Tam Sayı","-4":"Tam Sayı","-3":"Tam Sayı","-2":"Tam Sayı","-1":"Tam Sayı","0":"Doğal Sayı","1":"Doğal Sayı","2":"Asal Sayı","3":"Asal Sayı","4":"Doğal Sayı","5":"Asal Sayı","6":"Doğal Sayı","7":"Asal Sayı","8":"Doğal Sayı","9":"Doğal Sayı","10":"Doğal Sayı","11":"Asal Sayı","12":"Doğal Sayı","√2":"İrrasyonel","√3":"İrrasyonel","√4":"Doğal Sayı","√7":"İrrasyonel","√11":"İrrasyonel","√13":"İrrasyonel","³√64":"Doğal Sayı","²√16":"Doğal Sayı","0.333...":"Rasyonel Sayı","5.2424...":"Rasyonel Sayı","0.9999...":"Rasyonel Sayı"}
        Sayilar.setObjectName("Sayilar")
        Sayilar.resize(740, 417)
        Sayilar.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.centralwidget = QtWidgets.QWidget(Sayilar)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(2, 2, 2, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setStyleSheet("color:white;\n"
"background-color:rgba(35, 18, 11, 0.56);\n"
"border-radius:2px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setMaximumSize(QtCore.QSize(2, 100))
        self.line.setStyleSheet("background-color: rgb(33, 32, 156);")
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_4.addWidget(self.line)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
"background-color: rgb(253, 184, 39);\n"
"border-radius: 15px;\n"
"color: white;\n"
"font: 40pt \"Helvetica\";\n"
"}\n"
"#pushButton_2:hover{\n"
"background-color: rgb(252, 161, 0);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_3.setStyleSheet("#pushButton_3{\n"
"background-color: rgb(253, 184, 39);\n"
"border-radius: 15px;\n"
"color: white;\n"
"font: 40pt \"Helvetica\";\n"
"}\n"
"#pushButton_3:hover{\n"
"background-color: rgb(252, 161, 0);\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_4.setStyleSheet("#pushButton_4{\n"
"background-color: rgb(253, 184, 39);\n"
"border-radius: 15px;\n"
"color: white;\n"
"font: 40pt \"Helvetica\";\n"
"}\n"
"#pushButton_4:hover{\n"
"background-color: rgb(252, 161, 0);\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setStyleSheet("background-color: rgb(33, 32, 156);")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_5.setStyleSheet("#pushButton_5{\n"
"background-color: rgb(253, 184, 39);\n"
"border-radius: 15px;\n"
"color: white;\n"
"font: 40pt \"Helvetica\";\n"
"}\n"
"#pushButton_5:hover{\n"
"background-color: rgb(252, 161, 0);\n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_6.setStyleSheet("#pushButton_6{\n"
"background-color: rgb(253, 184, 39);\n"
"border-radius: 15px;\n"
"color: white;\n"
"font: 40pt \"Helvetica\";\n"
"}\n"
"#pushButton_6:hover{\n"
"background-color: rgb(252, 161, 0);\n"
"}\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_7.setStyleSheet("#pushButton_7{\n"
"background-color: rgb(253, 184, 39);\n"
"border-radius: 15px;\n"
"color: white;\n"
"font: 40pt \"Helvetica\";\n"
"}\n"
"#pushButton_7:hover{\n"
"background-color: rgb(252, 161, 0);\n"
"}\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem6)
        self.horizontalLayout_4.addWidget(self.widget)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setMaximumSize(QtCore.QSize(2, 100))
        self.line_2.setStyleSheet("background-color: rgb(33, 32, 156);")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_4.addWidget(self.line_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_3.addItem(spacerItem8)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setStyleSheet("#label_2{\n"
"background-color: rgb(162, 187, 243);\n"
"color: white;\n"
"border:none;\n"
"border-radius:10px;\n"
"padding: 10\n"
"}\n"
"")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 0, 3, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 0, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem11, 1, 5, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(110, 50))
        self.pushButton.setStyleSheet("#pushButton{\n"
"background-color: rgb(193, 214, 255);\n"
"color: white;\n"
"border:none;\n"
"}\n"
"#pushButton:hover{\n"
"background-color: rgb(162, 187, 243);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/tekrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 5, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(100, 0))
        self.label_3.setStyleSheet("color:white;\n"
"background-color:rgb(78, 71, 68);\n"
"border-radius:2px;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        Sayilar.setCentralWidget(self.centralwidget)
        self.pushButton.clicked.connect(lambda: self.restart(Sayilar))
        self.pushButton_2.clicked.connect(lambda: self.on_click(self.pushButton_2))
        self.pushButton_3.clicked.connect(lambda: self.on_click(self.pushButton_3))
        self.pushButton_4.clicked.connect(lambda: self.on_click(self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda: self.on_click(self.pushButton_5))
        self.pushButton_6.clicked.connect(lambda: self.on_click(self.pushButton_6))
        self.pushButton_7.clicked.connect(lambda: self.on_click(self.pushButton_7))
        self.soru = "Asal sayı"
        self.point = 0
        self.cntr = 10
        self.retranslateUi(Sayilar)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(1000)
        QtCore.QMetaObject.connectSlotsByName(Sayilar)

    def restart(self, Sayilar):
        self.num1 = random.choice(list(self.allnum.keys()))
        self.num2 = random.choice(list(self.allnum.keys()))
        self.num3 = random.choice(list(self.allnum.keys()))
        self.num4 = random.choice(list(self.allnum.keys()))
        self.num5 = random.choice(list(self.allnum.keys()))
        self.num6 = random.choice(list(self.allnum.keys()))
        self.soru = random.choice(self.quests)
        self.pushButton_2.setText(self._translate("Sayilar", self.num1))
        self.pushButton_3.setText(self._translate("Sayilar", self.num2))
        self.pushButton_4.setText(self._translate("Sayilar", self.num3))
        self.pushButton_5.setText(self._translate("Sayilar", self.num4))
        self.pushButton_6.setText(self._translate("Sayilar", self.num5))
        self.pushButton_7.setText(self._translate("Sayilar", self.num6))
        self.label.setText(self._translate("Sayilar", "Aşağaıdakilerden {0} olanları işaretleyiniz".format(self.soru)))

    def retranslateUi(self, Sayilar):
        self._translate = QtCore.QCoreApplication.translate
        Sayilar.setWindowTitle(self._translate("Sayilar", "Sayılar"))
        self.label.setText(self._translate("Sayilar", "Aşağaıdakilerden ASAL SAYI olanları işaretleyiniz"))
        self.num1 = random.choice(list(self.allnum.keys()))
        self.num2 = random.choice(list(self.allnum.keys()))
        self.num3 = random.choice(list(self.allnum.keys()))
        self.num4 = random.choice(list(self.allnum.keys()))
        self.num5 = random.choice(list(self.allnum.keys()))
        self.num6 = random.choice(list(self.allnum.keys()))
        self.pushButton_2.setText(self._translate("Sayilar", self.num1))
        self.pushButton_3.setText(self._translate("Sayilar", self.num2))
        self.pushButton_4.setText(self._translate("Sayilar", self.num3))
        self.pushButton_5.setText(self._translate("Sayilar", self.num4))
        self.pushButton_6.setText(self._translate("Sayilar", self.num5))
        self.pushButton_7.setText(self._translate("Sayilar", self.num6))
        self.label_2.setText(self._translate("Sayilar", "Puan: {0}".format(str(self.point))))
        self.pushButton.setText(self._translate("Sayilar", "Tekrar Oluştur"))
        self.label_3.setText(self._translate("Sayilar", str(self.cntr)))


    def on_click(self,neki):
        try:
            if str(self.allnum[neki.text()].lower().replace("i","ı")) == str(self.soru.lower().replace("i","ı")):
                self.point += 1
            elif str(self.allnum[neki.text()].lower().replace("i","ı")) == "doğal sayı" and str(self.soru.lower().replace("i","ı")) == "tam sayı":
                self.point += 1
            elif str(self.allnum[neki.text()].lower().replace("i","ı")) == "asal sayı" and str(self.soru.lower().replace("i","ı")) == "doğal sayı":
                self.point += 1
            elif str(self.allnum[neki.text()].lower().replace("i","ı")) == "tam sayı" and int(neki.text()) >= 0 and str(self.soru.lower().replace("i","ı")) == "doğal sayı":
                self.point += 1
            elif str(self.allnum[neki.text()].lower().replace("i","ı")) == "asal sayı" and str(self.soru.lower().replace("i","ı")) == "tam sayı":
                self.point += 1
            self.label_2.setText(self._translate("Sayilar", "Puan: {0}".format(str(self.point))))
                
            neki.setText(self._translate("Sayilar", self.allnum[neki.text()]))
            
        except:
            pass

    def progress(self):
        if self.cntr == 0:
            self.label_3.setText(self._translate("Sayilar", "! OYUN BİTTİ !"))
        else:
            self.cntr -= 1
            self.label_3.setText(self._translate("Sayilar", str(self.cntr)))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Sayilar = QtWidgets.QMainWindow()
    ui = Ui_Sayilar()
    ui.setupUi(Sayilar)
    Sayilar.show()
    sys.exit(app.exec_())
