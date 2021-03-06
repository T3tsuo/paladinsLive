# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import asyncio

import arez
import os
import urllib.request
from datetime import datetime, date

from PyQt5 import QtCore, QtGui, QtWidgets
import traceback
import pickle

if not os.path.isfile("dev_auth.dat") and not os.path.isfile("default.dat"):
    dev_auth = [0, ""]  # Developer ID and Auth Key
    pickle.dump(dev_auth, open("default.dat", "wb"))

elif os.path.isfile("dev_auth.dat"):
    dev_auth = pickle.load(open("dev_auth.dat", "rb"))

else:
    dev_auth = pickle.load(open("default.dat", "rb"))

title = "Paladins Live Beta 3.0"
name = ""
status = ""
avatar_url = ""
rank = ""
acclvl = ""
lastlogin1 = ""

width = 0


async def main(n):
    global name, avatar_url, status, rank, lastlogin1, acclvl
    # create an API instance
    api = arez.PaladinsAPI(dev_auth[0], dev_auth[1])
    try:
        # fetch Player stats
        player = await api.get_player(n)
    except Exception:
        await api.close()
        return False
    # if it's not a valid player
    if not player:
        # close api
        await api.close()
        # return false
        return False
    # grab players name
    name = player.name
    try:
        # and status
        status = (await player.get_status()).status.name
    except AttributeError:
        status = "Error"
    # and avatar url
    avatar_url = player.avatar_url
    # and rank
    rank = player.ranked_keyboard.rank.name
    # account level
    acclvl = player.level
    # last login
    now = datetime.now()
    time = now.time()
    date1 = datetime.date(now)
    lastlogin1 = grab_time(date1, time, player)
    # or else return true
    await api.close()
    return True


def grab_time(d, t, p):
    date1 = datetime.combine(date.today(), t) - datetime.combine(date.today(), p.last_login.time())
    if (d - p.last_login.date()).days > 0 and date1.days == 0:
        if (d - p.last_login.date()).days >= 365:
            year = (d - p.last_login.date()).days // 365
            if year == 1:
                date1 = str(year) + " year ago"
            else:
                date1 = str(year) + " years ago"
        elif (d - p.last_login.date()).days == 1:
            date1 = str((d - p.last_login.date()).days) + " day ago"
        else:
            date1 = str((d - p.last_login.date()).days) + " days ago"
        return date1
    else:
        if date1.seconds > 0:
            if date1.seconds >= 3600:
                time = date1.seconds // 3600
                if time == 1:
                    time = str(time) + " hour ago"
                else:
                    time = str(time) + " hours ago"
            elif date1.seconds >= 60:
                time = date1.seconds // 60
                if time == 1:
                    time = str(time) + " minute ago"
                else:
                    time = str(time) + " minutes ago"
            else:
                time = date1.seconds
                if time == 1:
                    time = str(time) + " second ago"
                else:
                    time = str(time) + " seconds ago"
        else:
            time = "Now"
        return time


class Ui_MainWindow(object):
    def __init__(self, y, z, w):
        global dev_auth, title
        # set default devId
        dev_auth[0] = y
        # set default authKey
        dev_auth[1] = z
        # set title
        title = w

    def setupUi(self, MainWindow):
        global width
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        MainWindow.setStyleSheet("background-color: black;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("color: #cccccc;")
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setStyleSheet("background-color: white;")
        self.username.setGeometry(QtCore.QRect(300, 250, 200, 30))
        self.username.setObjectName("lineEdit")
        self.username.setPlaceholderText("Username")
        self.devid = QtWidgets.QLineEdit(self.centralwidget)
        self.devid.setStyleSheet("background-color: white;")
        self.devid.setGeometry(QtCore.QRect(200, 450, 200, 30))
        self.devid.setObjectName("lineEdit")
        self.devid.setPlaceholderText("devid (optional)")
        self.authkey = QtWidgets.QLineEdit(self.centralwidget)
        self.authkey.setStyleSheet("background-color: white;")
        self.authkey.setGeometry(QtCore.QRect(400, 450, 200, 30))
        self.authkey.setObjectName("lineEdit")
        self.authkey.setPlaceholderText("authkey (optional)")

        self.author = QtWidgets.QLabel(self.centralwidget)
        self.author.setStyleSheet("color: #cccccc;")
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.author.setFont(font)
        self.author.setObjectName("author")
        self.author.setText("Made by: Takumi Comeau")
        self.author.adjustSize()
        self.author.move(int(MainWindow.width() - self.author.width()), MainWindow.height() - self.author.height())

        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setStyleSheet("color: black; background-color: grey;")
        self.reset.setGeometry(QtCore.QRect(350, 550, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        self.reset.setFont(font)
        self.reset.setObjectName("Reset")
        self.reset.setText("Reset")

        if not os.path.isfile("dev_auth.dat"):
            self.reset.hide()
            self.info = QtWidgets.QLabel(self.centralwidget)
            self.info.setStyleSheet("color: #cccccc;")
            font = QtGui.QFont()
            font.setFamily("Tw Cen MT Condensed Extra Bold")
            font.setPointSize(16)
            self.info.setFont(font)
            self.info.setObjectName("info")
            self.info.setText("To use personal Developer ID and Authentication Key")
            self.info.adjustSize()
            self.info.move((MainWindow.width() - self.info.width())//2, 400)
            self.info1 = QtWidgets.QLabel(self.centralwidget)
            self.info1.setStyleSheet("color: #cccccc;")
            font = QtGui.QFont()
            font.setFamily("Tw Cen MT Condensed Extra Bold")
            font.setPointSize(14)
            self.info1.setFont(font)
            self.info1.setObjectName("info1")
            self.info1.setText("Learn more on how to get them by visiting my GitHub page")
            self.info1.adjustSize()
            self.info1.move((MainWindow.width() - self.info1.width()) // 2, 500)
        else:
            self.reset.show()
            self.info = QtWidgets.QLabel(self.centralwidget)
            self.info.setStyleSheet("color: #cccccc;")
            font = QtGui.QFont()
            font.setFamily("Tw Cen MT Condensed Extra Bold")
            font.setPointSize(18)
            self.info.setFont(font)
            self.info.setObjectName("info")
            self.info.setText("Current:")
            self.info.adjustSize()
            self.info.move((MainWindow.width() - self.info.width()) // 2, 375)
            self.info1 = QtWidgets.QLabel(self.centralwidget)
            self.info1.setStyleSheet("color: #cccccc;")
            font = QtGui.QFont()
            font.setFamily("Tw Cen MT Condensed Extra Bold")
            font.setPointSize(12)
            self.info1.setFont(font)
            self.info1.setObjectName("info1")
            self.info1.setText("Dev ID: " + str(dev_auth[0]) + "    Auth Key: " + dev_auth[1])
            self.info1.adjustSize()
            self.info1.move((MainWindow.width() - self.info1.width()) // 2, 412)

        self.proceed = QtWidgets.QPushButton(self.centralwidget)
        self.proceed.setStyleSheet("color: black; background-color: grey;")
        self.proceed.setGeometry(QtCore.QRect(330, 300, 140, 50))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        self.proceed.setFont(font)
        self.proceed.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        width = MainWindow.width()

        self.avatar = QtWidgets.QLabel(self.centralwidget)
        self.rank = QtWidgets.QLabel(self.centralwidget)
        self.acclvl = QtWidgets.QLabel(self.centralwidget)
        self.lastlogin = QtWidgets.QLabel(self.centralwidget)

        self.username.returnPressed.connect(self.processUsername)
        self.devid.returnPressed.connect(self.processUsername)
        self.authkey.returnPressed.connect(self.processUsername)
        self.proceed.clicked.connect(MainWindow.close)
        self.reset.clicked.connect(self.reset_default)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def reset_default(self):
        global dev_auth
        if os.path.isfile("dev_auth.dat"):
            os.remove("dev_auth.dat")
            dev_auth = pickle.load(open("default.dat", "rb"))
            self.devid.setText("")
            self.authkey.setText("")
            font = QtGui.QFont()
            font.setFamily("Tw Cen MT Condensed Extra Bold")
            font.setPointSize(16)
            self.info.setFont(font)
            self.info.setObjectName("info")
            self.info.setText("To use personal Developer ID and Authentication Key")
            self.info.adjustSize()
            self.info.move((width - self.info.width()) // 2, 400)
            font = QtGui.QFont()
            font.setFamily("Tw Cen MT Condensed Extra Bold")
            font.setPointSize(14)
            self.info1.setFont(font)
            self.info1.setObjectName("info1")
            self.info1.setText("Learn more on how to get them by visiting my GitHub page")
            self.info1.adjustSize()
            self.info1.move((width - self.info1.width()) // 2, 500)
            self.reset.hide()

    def processUsername(self):
        global name, dev_auth, width, status, avatar_url, lastlogin1, acclvl
        # disconnect openWindow function everytime while cheking for a new player
        try:
            self.proceed.clicked.disconnect(self.openWindow)
        except TypeError:
            pass
        # grab username input
        name = self.username.text()
        # clear input box text
        self.username.clear()
        # if they input their own devId and authKey
        if self.devid.text() != "" and self.authkey.text() != "":
            # replace default devId
            dev_auth[0] = self.devid.text()
            # replace default authKey
            dev_auth[1] = self.authkey.text()
            pickle.dump(dev_auth, open("dev_auth.dat", "wb"))
            self.devid.setText("")
            self.authkey.setText("")
            font = QtGui.QFont()
            font.setFamily("Tw Cen MT Condensed Extra Bold")
            font.setPointSize(18)
            self.info.setFont(font)
            self.info.setText("Current:")
            self.info.adjustSize()
            self.info.move((width - self.info.width()) // 2, 375)
            font = QtGui.QFont()
            font.setFamily("Tw Cen MT Condensed Extra Bold")
            font.setPointSize(12)
            self.info1.setFont(font)
            self.info1.setText("Dev ID: " + str(dev_auth[0]) + "    Auth Key: " + dev_auth[1])
            self.info1.adjustSize()
            self.info1.move((width - self.info1.width()) // 2, 412)
            self.reset.show()
        # if name was inputted
        if len(name) != 0:
            # starts async
            loop = asyncio.get_event_loop()
            # pass name to check in the player database
            isvalid = loop.run_until_complete(main(name))  # run the async loop
        else:
            # if name doesn't exist return false
            isvalid = False
            # if username is not in the player database or nothing was inputted
        if not isvalid:
            # set text to message user that it's an invalid player name
            self.label.setText("Invalid player name")
            self.label.adjustSize()
            # adjust label size and position to be centered
            self.label.setGeometry(QtCore.QRect((width - self.label.width()) // 2, 150, 0, 0))
            self.label.adjustSize()
            self.avatar.hide()
            self.rank.hide()
            self.lastlogin.hide()
            # set button text to quit
            self.proceed.setText("Quit?")
        # if name is in the database
        else:
            # let user know it exists
            self.label.setText(name + ": " + status)
            self.label.adjustSize()
            # resize and center label
            self.label.setGeometry(QtCore.QRect((width - self.label.width()) // 2, 150, 330, 100))
            self.label.adjustSize()
            try:
                image = QtGui.QImage()
                image.loadFromData(urllib.request.urlopen(avatar_url).read())
                self.avatar.show()
                self.avatar.setGeometry(QtCore.QRect(0, 0, 70, 70))
                self.avatar.setPixmap(QtGui.QPixmap(image))
                self.avatar.setScaledContents(True)
            except Exception:
                self.avatar.clear()
                self.avatar.setStyleSheet("color: #cccccc;")
                font = QtGui.QFont()
                font.setFamily("Tw Cen MT Condensed Extra Bold")
                font.setPointSize(26)
                self.avatar.setFont(font)
                self.avatar.setObjectName("avatar")
                self.avatar.setText("New")
                self.avatar.adjustSize()
            self.avatar.move(self.label.x() - 20 - self.avatar.width(), self.label.y() - 10)
            self.rank.show()
            self.rank.setGeometry(QtCore.QRect(self.label.x() + self.label.width() + 5, self.label.y() - 5, 70, 70))
            self.rank.setObjectName("rank1")
            self.rank.setPixmap(QtGui.QPixmap(str(os.getcwd()) + "/img/rank/" + rank + ".png"))
            self.rank.setScaledContents(True)
            self.acclvl.setText("lvl: " + str(acclvl))
            self.acclvl.setStyleSheet("color: #cccccc;")
            font = QtGui.QFont()
            font.setFamily("Tw Cen MT Condensed Extra Bold")
            font.setPointSize(18)
            self.acclvl.setFont(font)
            self.acclvl.setObjectName("acclvl")
            self.acclvl.adjustSize()
            self.acclvl.move(self.label.x() + self.label.width() + 40 - self.acclvl.width()//2, self.label.y() - 5 + 70)
            self.lastlogin.setStyleSheet("color: #cccccc;")
            font = QtGui.QFont()
            font.setFamily("Tw Cen MT Condensed Extra Bold")
            font.setPointSize(20)
            self.lastlogin.hide()
            if status == "Offline":
                self.lastlogin.setFont(font)
                self.lastlogin.setObjectName("lastlogin")
                self.lastlogin.setText(lastlogin1)
                self.lastlogin.adjustSize()
                self.lastlogin.move((width - self.lastlogin.width()) // 2, 200)
                self.lastlogin.show()
            # set button to continue to the next window
            self.proceed.setText("Continue?")
            # connect to openWindow
            self.proceed.clicked.connect(self.openWindow)

    def openWindow(self):
        global name, dev_auth, logfile, title
        # import next window class Ui
        from LiveorFriends import Ui_LiveMatchorFriendsWindow
        try:
            # create window
            self.window = QtWidgets.QMainWindow()
            # grabs ui of second window
            self.ui = Ui_LiveMatchorFriendsWindow(name, dev_auth[0], dev_auth[1], title)
            # sets up the second ui in the new window
            self.ui.setupUi(self.window)
            # set title
            self.window.setWindowTitle(title)
            # display new window
            self.window.show()
        except Exception:
            username = os.getlogin()
            with open(f"C:\\Users\\{username}\\Desktop\\PaladinsLiveBeta-Error.log", "a") as logfile:
                traceback.print_exc(file=logfile)
            raise

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter a player name"))
        self.label.adjustSize()
        self.label.setGeometry(QtCore.QRect((MainWindow.width() - self.label.width()) // 2, 150, 330, 100))
        self.label.adjustSize()
        self.proceed.setText(_translate("MainWindow", "Quit?"))


if __name__ == "__main__":
    import sys

    if __name__ == "__main__":
        try:
            app = QtWidgets.QApplication(sys.argv)
            MainWindow = QtWidgets.QMainWindow()
            ui = Ui_MainWindow(dev_auth[0], dev_auth[1], title)
            ui.setupUi(MainWindow)
            MainWindow.setWindowTitle(title)
            MainWindow.show()
            sys.exit(app.exec_())
        except Exception:
            username = os.getlogin()
            with open(f"C:\\Users\\{username}\\Desktop\\PaladinsLiveBeta-Error.log", "a") as logfile:
                traceback.print_exc(file=logfile)
            raise
