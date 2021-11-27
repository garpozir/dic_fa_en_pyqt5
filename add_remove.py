#! /usr/bin/python3
# behrouz_ashraf
# garpozir@gmail.com
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter, sqlite3
from tkinter import messagebox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 205)
        MainWindow.setMinimumSize(QtCore.QSize(380, 205))
        MainWindow.setMaximumSize(QtCore.QSize(380, 205))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 10, 91, 20))
        self.label.setStyleSheet("color: rgb(143, 89, 2);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 40, 91, 20))
        self.label_2.setStyleSheet("color: rgb(143, 89, 2);")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(12, 10, 261, 31))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(30)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(10, 50, 261, 130))
        self.textEdit.setMinimumSize(QtCore.QSize(261, 130))
        self.textEdit.setMaximumSize(QtCore.QSize(261, 130))
        self.textEdit.setReadOnly(False)
        self.textEdit.setOverwriteMode(False)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(288, 70, 81, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton.setFont(font)
        self.pushButton.setToolTip("")
        self.pushButton.setWhatsThis("")
        self.pushButton.setAccessibleName("")
        self.pushButton.setAccessibleDescription("")
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setShortcut("")
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setAutoRepeatDelay(300)
        self.pushButton.setAutoRepeatInterval(100)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 110, 81, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setToolTip("")
        self.pushButton_2.setWhatsThis("")
        self.pushButton_2.setAccessibleName("")
        self.pushButton_2.setAccessibleDescription("")
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setAutoFillBackground(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/icon2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_2.setShortcut("")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setAutoRepeat(False)
        self.pushButton_2.setAutoExclusive(False)
        self.pushButton_2.setAutoRepeatDelay(300)
        self.pushButton_2.setAutoRepeatInterval(100)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 150, 81, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setToolTip("")
        self.pushButton_3.setWhatsThis("")
        self.pushButton_3.setAccessibleName("")
        self.pushButton_3.setAccessibleDescription("")
        self.pushButton_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_3.setAutoFillBackground(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_3.setShortcut("")
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_3.setAutoRepeat(False)
        self.pushButton_3.setAutoExclusive(False)
        self.pushButton_3.setAutoRepeatDelay(300)
        self.pushButton_3.setAutoRepeatInterval(100)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.tar)
        self.pushButton_2.clicked.connect(self.ex)
        self.pushButton_3.clicked.connect(self.sabt)

        with open('change.bg', 'r') as fd:
            m_mod = fd.readline()
            fd.close()
        if int(m_mod) not in (1,2,3):exit()
        if int(m_mod) == 1:
            self.pushButton.setDisabled(True)

        if int(m_mod) == 3:
            self.textEdit.setDisabled(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ثبت/ویرایش-حذف"))
        self.label.setText(_translate("MainWindow", "متن انگلیسی"))
        self.label_2.setText(_translate("MainWindow", "ترجمه فارسی"))
        self.lineEdit.setToolTip(_translate("MainWindow", "متن انگلیسی را اینجا بنویسید"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Exmp: hard"))
        self.textEdit.setToolTip(_translate("MainWindow", "ترجمه فارسی را اینجا بنویسید"))
        self.pushButton_2.setToolTip(_translate("MainWindow", "بازگشت به پنجره اصلی"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "لغات را با ـ از هم جدا کنید"))
        self.pushButton.setText(_translate("MainWindow", "ترجمه"))
        self.pushButton_2.setText(_translate("MainWindow", "انصراف"))
        self.pushButton_3.setText(_translate("MainWindow", "ذخیره"))

    def sbt(self):
        text_com = self.lineEdit.text()
        if text_com == '' or text_com == ' ':return 0
        text_com_edit = self.textEdit.toPlainText()
        if text_com_edit == '' or text_com_edit == ' ':text_com_edit = 'چیزی پیدا نشد'
        if text_com[-1] == ' ':
            text_com = text_com[:-1]
        if text_com[0] == ' ':
            text_com = text_com[1:]
        conn = sqlite3.connect("dic.db")
        cur = conn.cursor()
        cur.execute(f"Select count(*) from EnglishPersianWordDatabase where EnglishWord = '{text_com}'", )
        rows = cur.fetchall()
        conn.close()
        if int(rows[0][0]) == 0 and text_com != '':
            sqliteConnection = sqlite3.connect('dic.db')
            cursor = sqliteConnection.cursor()
            sqlite_insert_query = '''INSERT INTO EnglishPersianWordDatabase(EnglishWord, PersianWord)VALUES("'''+text_com+'''","'''+text_com_edit +'''")'''
            count = cursor.execute(sqlite_insert_query)
            sqliteConnection.commit()
            cursor.close()
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo("ثبت", "با موفقیت انجام شد")
        else:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror("خطا", "این کلمه قبلا ثبت شده است")

    def et(self):
        text_com = self.lineEdit.text()
        if text_com == '':return 0
        text_com_edit = self.textEdit.toPlainText()
        if text_com_edit == '':text_com_edit = 'چیزی پیدا نشد'
        if text_com[-1] == ' ':
            text_com = text_com[:-1]
        if text_com[0] == ' ':
            text_com = text_com[1:]
        conn = sqlite3.connect("dic.db")
        cur = conn.cursor()
        cur.execute(f"Select count(*) from EnglishPersianWordDatabase where EnglishWord = '{text_com}'", )
        rows = cur.fetchall()
        conn.close()
        if int(rows[0][0]) > 0 and text_com != '':
            sqliteConnection = sqlite3.connect('dic.db')
            cursor = sqliteConnection.cursor()
            sqlite_insert_query = ("DELETE FROM EnglishPersianWordDatabase WHERE EnglishWord='%s'"%(text_com ))
            count = cursor.execute(sqlite_insert_query)
            sqliteConnection.commit()
            cursor.close()
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo("ویرایش", "با موفقیت انجام شد")
            sqliteConnection = sqlite3.connect('dic.db')
            cursor = sqliteConnection.cursor()
            sqlite_insert_query = '''INSERT INTO EnglishPersianWordDatabase(EnglishWord, PersianWord)VALUES("'''+text_com+'''","'''+text_com_edit +'''")'''
            count = cursor.execute(sqlite_insert_query)
            sqliteConnection.commit()
            cursor.close()
        else:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror("خطا", "این کلمه برای ویرایش پیدا نشد")

    def dl(self):
        text_com = self.lineEdit.text()
        if text_com == '':return 0
        if text_com[-1] == ' ':
            text_com = text_com[:-1]
        if text_com[0] == ' ':
            text_com = text_com[1:]
        conn = sqlite3.connect("dic.db")
        cur = conn.cursor()
        cur.execute(f"Select count(*) from EnglishPersianWordDatabase where EnglishWord = '{text_com}'", )
        rows = cur.fetchall()
        conn.close()
        if int(rows[0][0]) > 0 and text_com != '':
            sqliteConnection = sqlite3.connect('dic.db')
            cursor = sqliteConnection.cursor()
            sqlite_insert_query = ("DELETE FROM EnglishPersianWordDatabase WHERE EnglishWord='%s'"%(text_com ))
            count = cursor.execute(sqlite_insert_query)
            sqliteConnection.commit()
            cursor.close()
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo("حذف", "با موفقیت انجام شد")
        else:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror("خطا", "این کلمه برای حذف پیدا نشد")

    def ex(self):exit()

    def sabt(self):
        with open('change.bg', 'r') as fd:
            m_mod = fd.readline()
            fd.close()
        if int(m_mod) == 1:
            self.sbt()

        if int(m_mod) == 2:
            self.et()

        if int(m_mod) == 3:
            self.dl()

    def tar(self):
        text_com = self.lineEdit.text()
        if text_com == '' or text_com == ' ':return 0
        if text_com[-1] == ' ':
            text_com = text_com[:-1]
        if text_com[0] == ' ':
            text_com = text_com[1:]
        conn = sqlite3.connect("dic.db")
        cur = conn.cursor()
        cur.execute(f"Select PersianWord from EnglishPersianWordDatabase where EnglishWord = '{text_com}' limit 7", )
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
                    pass
            self.textEdit.setText(i_row)
        else:
            self.textEdit.setText('چیزی پیدا نشد')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
