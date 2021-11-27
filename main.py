#! /usr/bin/python3
# behrouz_ashraf
# garpozir@gmail.com
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3, os, gtts, time
from playsound import playsound

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(500, 320)
        mainWindow.setMinimumSize(QtCore.QSize(500, 320))
        mainWindow.setMaximumSize(QtCore.QSize(500, 320))
        font = QtGui.QFont()
        font.setPointSize(12)
        mainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        mainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 501, 291))
        self.label.setToolTip("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/trance.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setEnabled(False)
        self.comboBox.setGeometry(QtCore.QRect(20, 20, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(True)
        self.comboBox.setMaxCount(50000)
        self.comboBox.setIconSize(QtCore.QSize(20, 20))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(206, 92, 0);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(300, 130, 41, 41))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("img/tik.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setEnabled(True)
        self.pushButton_8.setGeometry(QtCore.QRect(20, 70, 41, 41))
        self.pushButton_8.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon1)
        self.pushButton_8.setIconSize(QtCore.QSize(34, 34))
        self.pushButton_8.setAutoDefault(True)
        self.pushButton_8.setDefault(False)
        self.pushButton_8.setFlat(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 190, 101, 81))
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet("background-color: rgb(206, 92, 0);")
        self.pushButton_3.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/music.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(86, 86))
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setDefault(True)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setEnabled(False)
        self.pushButton_9.setGeometry(QtCore.QRect(130, 190, 101, 81))
        self.pushButton_9.setAutoFillBackground(False)
        self.pushButton_9.setStyleSheet("background-color: rgb(206, 92, 0);")
        self.pushButton_9.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.pushButton_9.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/trance2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon3)
        self.pushButton_9.setIconSize(QtCore.QSize(86, 86))
        self.pushButton_9.setAutoDefault(False)
        self.pushButton_9.setDefault(True)
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(350, 190, 141, 81))
        self.pushButton_10.setTabletTracking(False)
        self.pushButton_10.setAutoFillBackground(False)
        self.pushButton_10.setStyleSheet("background-color: rgb(206, 92, 0);")
        self.pushButton_10.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.pushButton_10.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/iran_language.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon4)
        self.pushButton_10.setIconSize(QtCore.QSize(128, 128))
        self.pushButton_10.setAutoDefault(False)
        self.pushButton_10.setDefault(True)
        self.pushButton_10.setFlat(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(350, 100, 141, 81))
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet("background-color: rgb(206, 92, 0);")
        self.pushButton_6.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.pushButton_6.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img/English_language.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QtCore.QSize(128, 128))
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_6.setDefault(True)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(390, 10, 101, 81))
        self.pushButton_11.setAutoFillBackground(False)
        self.pushButton_11.setStyleSheet("background-color: rgb(206, 92, 0);")
        self.pushButton_11.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.pushButton_11.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("img/history.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon6)
        self.pushButton_11.setIconSize(QtCore.QSize(96, 96))
        self.pushButton_11.setAutoDefault(True)
        self.pushButton_11.setDefault(False)
        self.pushButton_11.setFlat(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setGeometry(QtCore.QRect(320, 20, 51, 41))
        self.pushButton_5.setToolTip("خواندن متن")
        self.pushButton_5.setStyleSheet("")
        self.pushButton_5.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("img/voice.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon7)
        self.pushButton_5.setIconSize(QtCore.QSize(42, 42))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(300, 220, 41, 41))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("img/tik.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 24))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(mainWindow)
        self.action.setCheckable(True)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("img/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action.setIcon(icon8)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(mainWindow)
        self.action_2.setCheckable(True)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("img/icon3.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_2.setIcon(icon9)
        self.action_2.setObjectName("action_2")
        self.action_4 = QtWidgets.QAction(mainWindow)
        self.action_4.setCheckable(True)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("img/icon2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_4.setIcon(icon10)
        self.action_4.setObjectName("action_4")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addSeparator()
        self.menu.addAction(self.action_4)
        self.menubar.addAction(self.menu.menuAction())
        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        self.pushButton_10.clicked.connect(self.dah)
        self.pushButton_6.clicked.connect(self.shish)
        self.pushButton_11.clicked.connect(self.oppdf)
        self.comboBox.currentTextChanged.connect(self.com)
        self.pushButton_3.clicked.connect(self.ply)
        self.pushButton_9.clicked.connect(self.tran)
        self.pushButton_8.clicked.connect(self.dic_add)
        self.pushButton_5.clicked.connect(self.tts)
        self.action.triggered['bool'].connect(self.sabz)
        self.action_2.triggered['bool'].connect(self.zard)
        self.action_4.triggered['bool'].connect(self.gher)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "فرهنگ لغات فارسی-انگلیسی"))
        self.comboBox.setToolTip(_translate("mainWindow", "کلمه ای که میخواهید ترجمه شود را اینجا بنویسید"))
        self.pushButton_8.setToolTip(_translate("mainWindow", "افزودن به فهرست علاقه مندی ها"))
        self.pushButton_8.setShortcut(_translate("mainWindow", "Ctrl+R"))
        self.pushButton_3.setToolTip(_translate("mainWindow", "برو به پخش موسیقی"))
        self.pushButton_3.setShortcut(_translate("mainWindow", "M"))
        self.pushButton_9.setToolTip(_translate("mainWindow", "ترجمه"))
        self.pushButton_9.setShortcut(_translate("mainWindow", "Return"))
        self.pushButton_10.setToolTip(_translate("mainWindow", "فارسی به انگلیسی"))
        self.pushButton_10.setShortcut(_translate("mainWindow", "I"))
        self.pushButton_6.setToolTip(_translate("mainWindow", "انگلیسی به فارسی"))
        self.pushButton_6.setShortcut(_translate("mainWindow", "E"))
        self.pushButton_11.setToolTip(_translate("mainWindow", "برو به فهرست علاقه مندی ها"))
        self.pushButton_11.setShortcut(_translate("mainWindow", "T"))
        self.menu.setTitle(_translate("mainWindow", "اصلاحات"))
        self.action.setText(_translate("mainWindow", "ثبت"))
        self.action.setShortcut(_translate("mainWindow", "Ctrl+S"))
        self.action_2.setText(_translate("mainWindow", "ویرایش"))
        self.action_2.setShortcut(_translate("mainWindow", "Ctrl+X"))
        self.action_4.setText(_translate("mainWindow", "حذف"))
        self.action_4.setShortcut(_translate("mainWindow", "Ctrl+D"))
        self.label_7.hide()
        self.label_6.hide()
        self.pushButton_8.hide()

    def sabz(self):
        with open('change.bg', 'w') as fd:
            fd.write('1')
            fd.close()
        time.sleep(0.5)
        os.system('python add_remove.py')

    def zard(self):
        with open('change.bg', 'w') as fd:
            fd.write('2')
            fd.close()
        time.sleep(0.5)
        os.system('python add_remove.py')

    def gher(self):
        with open('change.bg', 'w') as fd:
            fd.write('3')
            fd.close()
        time.sleep(0.5)
        os.system('python add_remove.py')

    def enb(self):
        self.pushButton_5.setEnabled(True)
        self.pushButton_9.setEnabled(True)
        self.comboBox.setEnabled(True)

    def shish(self):
        self.eng = 'EnglishWord'
        self.in_eng = 'PersianWord'
        self.label_6.show()
        self.label_7.hide()
        self.enb()

    def dah(self):
        self.eng = 'PersianWord'
        self.in_eng = 'EnglishWord'
        self.label_7.show()
        self.label_6.hide()
        self.enb()

    def oppdf(self):
        os.system('start history.txt')

    def ply(self):
        os.system('python music.py')

    def tts(self):
        text_com = self.comboBox.currentText()
        if(ord(text_com[0]) > 122 or ord(text_com[0]) < 65) and ord(text_com[0]) != 32:pass
        else:
            if text_com != '':
                tts_r = gtts.gTTS(text_com)
                tts_r.save("speak.mp3")
                playsound("speak.mp3")

    def dic_add(self):
        d_a = self.label_2.text()
        text_com = self.comboBox.currentText()
        if d_a != 'چیزی پیدا نشد' and text_com != '' and d_a != '':
            with open('history.txt', 'a') as file:
                file.write(f'{d_a} = {text_com}\n')
                file.close()

    def tran(self):
        text_com = self.comboBox.currentText()
        if text_com[-1] == ' ':
            text_com = text_com[:-1]
        conn = sqlite3.connect("dic.db")
        cur = conn.cursor()
        cur.execute(f"Select {self.in_eng} from EnglishPersianWordDatabase where {self.eng} = '{text_com}' limit 7", )
        rows = cur.fetchall()
        conn.close()
        if len(rows) > 0 and text_com != '':
            i_row = ''
            new_lp = 0
            list_tran = []
            for row in rows:
                # to list
                list_tran.append(row[0])
                new_lp += 1
                i_row += f'{row[0]}_'
                if new_lp == 3:
                    i_row += '\n'
            self.label_2.setText(i_row)
            self.\
                    pushButton_8.show()
        else:
            self.label_2.setText('چیزی پیدا نشد')
            self.\
                    pushButton_8.hide()

    def com(self):
        text_com = self.comboBox.currentText()
        conn = sqlite3.connect("dic.db")
        cur = conn.cursor()
        cur.execute(f"Select distinct {self.eng} from EnglishPersianWordDatabase where {self.eng} like '{text_com}%' limit 5", )
        rows = cur.fetchall()
        conn.close()
        if len(rows) > 0 and text_com != '':
            for row in rows:
                self.comboBox.insertItem(0,row[0])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
