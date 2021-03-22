from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QAbstractTableModel, Qt
from questionbank import Question as Qu
import sys
import os
import pyqtgraph as pg
import random
import sqlite3
import pandas as pd


button_font = QtGui.QFont()
button_font.setFamily("Segoe UI")
button_font.setPointSize(14)

button_font_small = QtGui.QFont()
button_font_small.setFamily("Segoe UI")
button_font_small.setPointSize(10)

entry_box_font = QtGui.QFont()
entry_box_font.setFamily("Arial")
entry_box_font.setPointSize(14)

title_font = QtGui.QFont()
title_font.setFamily("Segoe UI")
title_font.setPointSize(28)

sub_title_font = QtGui.QFont()
sub_title_font.setFamily("Segoe UI")
sub_title_font.setPointSize(20)
sub_title_font.setBold(True)

stats_font = QtGui.QFont()
stats_font.setFamily("Segoe UI")
stats_font.setPointSize(18)

test_font = QtGui.QFont()
test_font.setFamily("Segoe UI")
test_font.setPointSize(16)

combo_font = QtGui.QFont()
combo_font.setFamily("Segoe UI")
combo_font.setPointSize(10)

question_font = QtGui.QFont()
question_font.setFamily("Segoe UI")
question_font.setPointSize(18)

objectives_tuple = ("1N1", "2N1", "3N1", "4N1", "5N1", "1N2a", "1N2b", "1N2c", "2N2a", "2N2b", "3N2a", "3N2b", "4N2a",
                    "4N2b", "5N2", "6N2", "2N3", "3N3", "4N3a", "4N3b", "5N3a", "5N3b", "6N3", "1N4", "2N4", "3N4",
                    "4N4a", "4N4b", "5N4", "6N4", "4N5", "5N5", "6N5", "2N6", "3N6", "4N6", "5N6", "6N6", "1C1", "2C1",
                    "3C1", "5C1", "1C2a", "1C2b", "2C2a", "2C2b", "3C2", "4C2", "5C2", "2C3", "3C3", "4C3", "5C3",
                    "6C3", "1C4", "2C4", "3C4", "4C4", "5C4", "6C4", "5C5a", "5C5b", "5C5c", "5C5d", "6C5", "2C6",
                    "3C6", "4C6a", "4C6b", "4C6c", "5C6a", "5C6b", "6C6", "2C7", "3C7", "4C67", "5C7a", "5C7b", "6C7a",
                    "6C7b", "6C7c", "1C8", "2C8", "3C8", "4C8", "5C8a", "5C8b", "5C8c", "6C8", "2C9a", "2C9b", "6C9",
                    "1F1a", "1F1b", "2F1a", "2F1b", "3F1a", "3F1b", "3F1c", "4F1", "2F2", "3F2", "4F2", "5F2a", "5F2b",
                    "6F2", "3F3", "5F3", "6F3", "3F4", "4F4", "5F4", "6F4", "5F5", "6F5a", "6F5b", "4F6a", "4F6b",
                    "5F6a", "5F6b", "6F6", "4F7", "5F7", "4F8", "5F8", "4F9", "6F9a", "6F9b", "6F9c", "3F10", "4F10a",
                    "4F10b", "5F10", "6F10", "5F11", "6F11", "5F12", "6R1", "6R2", "6R3", "6R4", "6A1", "6A2", "6A3",
                    "6A4", "6A5", "1M1", "2M1", "3M1a", "3M1b", "3M1c", "4M1", "1M2", "2M2", "3M2a", "3M2b", "3M2c",
                    "4M2", "1M3", "2M3a", "2M3b", "1M4a", "1M4b", "1M4c", "2M4a", "2M4b", "2M4c", "3M4a", "3M4b",
                    "3M4c", "3M4d", "3M4e", "3M4f", "4M4a", "4M4b", "4M4c", "5M4", "4M5", "5M5", "6M5", "5M6", "6M6",
                    "3M7", "4M7a", "4M7b", "5M7a", "5M7b", "6M7a", "6M7b", "6M7c", "5M8", "6M8a", "6M8b", "2M9", "3M9a",
                    "3M9b", "3M9c", "3M9d", "4M9", "5M9a", "5M9b", "5M9c", "5M9d", "6M9", "1G1a", "1G1b", "2G1a",
                    "2G1b", "2G2a", "2G2b", "3G2", "4G2a", "4G2b", "4G2c", "5G2a", "5G2b", "6G2a", "6G2b", "2G3",
                    "3G3a", "3G3b", "5G3", "6G3a", "6G3b", "3G4a", "3G4b", "4G4", "5G4a", "5G4b", "5G4c", "6G4a",
                    "6G4b", "6G5", "2P1", "1P2", "2P2", "4P2", "5P2", "6P2", "4P3a", "4P3b", "6P3", "2S1", "3S1", "4S1",
                    "5S1", "6S1", "2S2a", "2S2b", "3S2", "4S2", "5S2", "6S3")

strand_index = {
    "Number and place value": "N", "Calculations": "C", "Fractions, decimals and percentages": "F",
    "Ratio and proportion": "R", "Algebra": "A", "Measurement": "M", "Shape": "G",
    "Position and direction": "P", "Statistics": "S"
}

substrand_index = {
    "Counting in multiples": "N1", "Read, write, order & compare": "N2", "Place value": "N3",
    "Identify, represent, estimate; rounding": "N4", "Negative numbers": "N5", "Number problems": "N6",
    "Add/subtract mentally": "C1", "Add/subtract using written methods": "C2", "Estimate and use inverses": "C3",
    "Add/subtract to solve problems": "C4", "Properties of number": "C5", "Multiply/divide mentally": "C6",
    "Multiply/divide using written methods": "C7", "Solve problems using all 4 operations": "C8",
    "Order of operations": "C9", "Recognise & count fractions": "F1", "Equivalent fractions": "F2",
    "Comparing & ordering fractions": "F3", "Add/subtract fractions": "F4", "Multiply/divide fractions": "F5",
    "Fractions/decimals equivalence": "F6", "Rounding decimals": "F7", "Compare & order decimals": "F8",
    "Multiply/divide decimals": "F9", "Solve fraction & decimal problems": "F10",
    "Fractions/decimals/% equivalence": "F11", "Solve percentage problems": "F12",
    "Relative sizes and similarity": "R1", "Use of percentages for comparison": "R2", "Scale factors": "R3",
    "Unequal sharing and grouping": "R4", "Missing number problems in algebra": "A1",
    "Simple formulae expressed in words": "A2", "Generate & describe linear number sequences": "A3",
    "Number sentences involving two unknowns": "A4", "Enumerate all combinations of two variables": "A5",
    "Compare, describe and order measures": "M1", "Estimate, measure and read scales": "M2", "Money": "M3",
    "Time": "M4", "Convert between metric units": "M5", "Convert metric/imperial": "M6", "Perimeter and area": "M7",
    "Volume": "M8", "Solve problems involving measures": "M9", "Compare and sort shapes": "G1",
    "Describe properties and classify shapes": "G2", "Draw & make shapes & relate 2-D to 3-D": "G3",
    "Angles – measuring and properties": "G4", "Circles": "G5", "Order in patterns and sequences": "P1",
    "Describe position, direction and movement": "P2", "Co-ordinates": "P3", "Interpret and represent data": "S1",
    "Solve problems involving data": "S2a", "Mean average": "S3"
}


class Data:
    def __init__(self):
        self.score = 0
        self.users = {}
        self.data_frame = []
        self.total_quizzes = 0
        self.total_questions = 0
        self.top_score = ""
        self.top_area = ""
        self.bottom_area = ""

    def set_stats(self):
        self.set_total_quizzes()
        self.set_total_questions()
        self.set_top_score()
        self.set_top_area()
        self.set_bottom_area()
        home_screen.statsLabel2.setText("{}\n\n{}\n\n{}\n\n{}\n\n{}".format(self.total_quizzes, self.total_questions,
                                                                            self.top_score, self.top_area,
                                                                            self.bottom_area))

    def set_total_quizzes(self):
        connection = sqlite3.connect("{}.db".format(login.username))
        data_frame = pd.read_sql_query("SELECT * FROM QUIZ", connection)
        try:
            self.total_quizzes = int((data_frame['Quiz number'].max()))
        except:
            pass
        connection.close()

    def set_total_questions(self):
        connection = sqlite3.connect("{}.db".format(login.username))
        data_frame = pd.read_sql_query("SELECT * FROM QUIZ", connection)
        self.total_questions = data_frame.shape[0]
        connection.close()

    def set_top_score(self):
        connection = sqlite3.connect("{}.db".format(login.username))
        data_frame = pd.read_sql_query("SELECT * FROM QUIZ", connection)
        total_quizzes = [i for i in range(1, self.total_quizzes + 1)]
        quiz_dictionary = {}
        for entry in total_quizzes:
            marks = 0
            total = 0
            for row in data_frame.itertuples():
                if int(row[2]) == entry:
                    marks += int(row[8])
                    total += 1
            quiz_dictionary[entry] = round(100 * (marks / total))

        maximum = (max(quiz_dictionary, key=quiz_dictionary.get))
        self.top_score = "{}%    (Quiz {})".format(quiz_dictionary[maximum], maximum)
        connection.close()

    def set_top_area(self):
        connection = sqlite3.connect("{}.db".format(login.username))
        data_frame = pd.read_sql_query("SELECT * FROM QUIZ", connection)
        quiz_dictionary = {}
        for key in strand_index:
            value = strand_index[key]
            marks = 0
            total = 0
            for row in data_frame.itertuples():
                if (row[4][1]) == value:
                    marks += int(row[8])
                    total += 1
            if total == 0:
                pass
            elif marks == 0:
                quiz_dictionary = 0
            else:
                quiz_dictionary[value] = round(100 * (marks / total))

        maximum = (max(quiz_dictionary, key=quiz_dictionary.get))
        switch = {}
        for key in strand_index:
            switch[strand_index[key]] = key
        self.top_area = switch[maximum]
        connection.close()

    def set_bottom_area(self):
        connection = sqlite3.connect("{}.db".format(login.username))
        data_frame = pd.read_sql_query("SELECT * FROM QUIZ", connection)
        quiz_dictionary = {}
        for key in strand_index:
            value = strand_index[key]
            marks = 0
            total = 0
            for row in data_frame.itertuples():
                if (row[4][1]) == value:
                    marks += int(row[8])
                    total += 1
            if total == 0:
                pass
            elif marks == 0:
                quiz_dictionary = 0
            else:
                quiz_dictionary[value] = round(100 * (marks / total))

        minimum = (min(quiz_dictionary, key=quiz_dictionary.get))
        switch = {}
        for key in strand_index:
            switch[strand_index[key]] = key
        self.bottom_area = switch[minimum]
        connection.close()


def increase_score():
    data.score += 1


def load_usernames_passwords():
    if os.path.isfile("Usernames and passwords.db"):
        connection = sqlite3.connect("Usernames and passwords.db")
        c = connection.cursor()
        c.execute("SELECT Username,Password from USERS")
        result = c.fetchall()
        for Username, Password in result:
            data.users[Username] = Password
    else:
        connection = sqlite3.connect("Usernames and passwords.db")
        c = connection.cursor()
        c.execute("""CREATE TABLE USERS
                        ([generated_id] INTEGER PRIMARY KEY, [Username] text, [Password] text, [Class] text) """)
        connection.commit()
        connection.close()


def read_data(username):
    connection = sqlite3.connect("{}.db".format(username))
    data.data_frame = pd.read_sql_query("SELECT * FROM QUIZ",
                                        connection)
    data.data_frame.pop("generated_id")
    data.data_frame.pop("Username")
    connection.close()


class MyWindow(QMainWindow):
    def __init__(self):
        # Main window
        super(MyWindow, self).__init__()
        self.setWindowTitle("Maths quiz")
        self.setGeometry(0, 0, screen_size.width(), screen_size.height())
        self.centre_window()

        # Background image
        self.backgroundLabel = QtWidgets.QLabel(self)
        self.pixmap = QtGui.QPixmap("C:/Users/Michael/Pictures/Saved Pictures/maths_background.jpg")
        self.backgroundLabel.setPixmap(self.pixmap)
        self.backgroundLabel.setGeometry(0, 0, screen_size.width(), screen_size.height())
        self.backgroundLabel.setScaledContents(True)
        self.backgroundLabel.show()

    def centre_window(self):
        win_screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((win_screen.width() - size.width()) // 2, (win_screen.height() - size.height()) // 2)


class LoginScreen:
    def __init__(self):
        self.username = ""

        # Login background shape
        self.loginBackgroundLabel = QtWidgets.QLabel(win)
        self.pixmap = QtGui.QPixmap("C:/Users/Michael/Pictures/Saved Pictures/maths_background.jpg")
        self.loginBackgroundLabel.setPixmap(self.pixmap)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        self.loginBackgroundLabel.setGraphicsEffect(shadow)
        place_widget_centre(self.loginBackgroundLabel, 500, 600, 150)
        self.loginBackgroundLabel.setScaledContents(True)

        # Maths owl image
        self.mathsOwlLabel = QtWidgets.QLabel(win)
        self.pixmap = QtGui.QPixmap("C:/Users/Michael/Pictures/Saved Pictures/maths_owl.png")
        self.mathsOwlLabel.setPixmap(self.pixmap)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        self.mathsOwlLabel.setGraphicsEffect(shadow)
        self.mathsOwlLabel.setGeometry(200, 250, 400, 400)
        self.mathsOwlLabel.setScaledContents(True)

        # Welcome label
        self.welcomeLabel = QtWidgets.QLabel("Welcome!", win)
        place_widget_centre(self.welcomeLabel, 350, 60, 190)
        self.welcomeLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.welcomeLabel.setFont(title_font)
        self.welcomeLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Username entry box
        self.usernameEntry = QtWidgets.QLineEdit(win)
        place_widget_centre(self.usernameEntry, 350, 60, 285)
        self.usernameEntry.setFont(entry_box_font)
        self.usernameEntry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.usernameEntry.setText("")
        self.usernameEntry.setPlaceholderText("Username")

        # Password entry box
        self.passwordEntry = QtWidgets.QLineEdit(win)
        place_widget_centre(self.passwordEntry, 350, 60, 360)
        self.passwordEntry.setFont(entry_box_font)
        self.passwordEntry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.passwordEntry.setText("")
        self.passwordEntry.setPlaceholderText("Password")

        # Login button
        self.loginButton = QtWidgets.QPushButton(win)
        place_widget_centre(self.loginButton, 350, 60, 435)
        self.loginButton.setFont(button_font)
        self.loginButton.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.loginButton.setText("Log in")
        self.loginButton.clicked.connect(self.check_login)

        # Login error label
        self.loginErrorLabel = QtWidgets.QLabel("Username not found", win)
        place_widget_centre(self.loginErrorLabel, 350, 40, 510)
        self.loginErrorLabel.setStyleSheet("color: rgb(255,219,88);")
        self.loginErrorLabel.setFont(button_font_small)
        self.loginErrorLabel.setAlignment(QtCore.Qt.AlignCenter)

        # New user button
        self.newUserButton = QtWidgets.QPushButton(win)
        place_widget_centre(self.newUserButton, 350, 60, 580)
        self.newUserButton.setFont(button_font)
        self.newUserButton.setStyleSheet("color: rgb(255, 255, 255); background-color: transparent;"
                                         "text-decoration: underline;")
        self.newUserButton.setText("Click to add new user")
        self.newUserButton.clicked.connect(self.new_user)

    def check_login(self):
        if self.usernameEntry.text() in data.users:
            if self.passwordEntry.text() == data.users.get(self.usernameEntry.text()):
                self.username = self.usernameEntry.text()
                self.login_user()
            else:
                self.loginErrorLabel.setText("Incorrect password")
                self.passwordEntry.setFocus()
        else:
            self.loginErrorLabel.setText("Username not found")
            self.loginErrorLabel.show()
            self.usernameEntry.setText("")
            self.usernameEntry.setFocus()
        self.passwordEntry.setText("")

    def login_user(self):
        self.hide_widgets()
        home_screen.usernameLabel.setText(self.username)
        home_screen.show_widgets()
        read_data(self.username)
        data.set_stats()

    def new_user(self):
        self.hide_widgets()
        new_user.show_widgets()
        new_user.newUsernameEntry.setFocus()

    def show_widgets(self):
        self.loginBackgroundLabel.show()
        self.mathsOwlLabel.show()
        self.welcomeLabel.show()
        self.usernameEntry.show()
        self.passwordEntry.show()
        self.loginButton.show()
        self.newUserButton.show()

    def hide_widgets(self):
        self.loginBackgroundLabel.hide()
        self.mathsOwlLabel.hide()
        self.welcomeLabel.hide()
        self.usernameEntry.hide()
        self.passwordEntry.hide()
        self.loginButton.hide()
        self.loginErrorLabel.hide()
        self.newUserButton.hide()


class NewUserScreen:
    def __init__(self):
        # New user title label
        self.newUserTitleLabel = QtWidgets.QLabel("Fill in the boxes to\ncreate your profile", win)
        place_widget_centre(self.newUserTitleLabel, 1000, 115, 160)
        self.newUserTitleLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.newUserTitleLabel.setFont(sub_title_font)
        self.newUserTitleLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Return to login screen button
        self.returnToLoginButton = QtWidgets.QPushButton(win)
        place_widget_centre(self.returnToLoginButton, 200, 60, 850)
        self.returnToLoginButton.setFont(button_font)
        self.returnToLoginButton.setStyleSheet("background-color: rgb(169, 169, 169);")
        self.returnToLoginButton.setText("Return to login")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(50)
        self.returnToLoginButton.setGraphicsEffect(shadow)
        self.returnToLoginButton.clicked.connect(self.return_to_login)

        # New username entry box
        self.newUsernameEntry = QtWidgets.QLineEdit(win)
        place_widget_centre(self.newUsernameEntry, 350, 60, 285)
        self.newUsernameEntry.setFont(entry_box_font)
        self.newUsernameEntry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.newUsernameEntry.setText("")
        self.newUsernameEntry.setPlaceholderText("Username")

        # New password entry box
        self.newPasswordEntry = QtWidgets.QLineEdit(win)
        place_widget_centre(self.newPasswordEntry, 350, 60, 360)
        self.newPasswordEntry.setFont(entry_box_font)
        self.newPasswordEntry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.newPasswordEntry.setText("")
        self.newPasswordEntry.setPlaceholderText("Password")

        # Class entry box
        self.newUserClassEntry = QtWidgets.QLineEdit(win)
        place_widget_centre(self.newUserClassEntry, 350, 60, 435)
        self.newUserClassEntry.setFont(entry_box_font)
        self.newUserClassEntry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.newUserClassEntry.setText("")
        self.newUserClassEntry.setPlaceholderText("Class")

        # New user error label
        self.newUserErrorLabel = QtWidgets.QLabel("Username already taken", win)
        place_widget_centre(self.newUserErrorLabel, 350, 40, 510)
        self.newUserErrorLabel.setStyleSheet("color: rgb(255,219,88);")
        self.newUserErrorLabel.setFont(button_font_small)
        self.newUserErrorLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Create new user button
        self.createNewUserButton = QtWidgets.QPushButton(win)
        place_widget_centre(self.createNewUserButton, 350, 60, 580)
        self.createNewUserButton.setFont(button_font)
        self.createNewUserButton.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.createNewUserButton.setText("Create new user")
        self.createNewUserButton.clicked.connect(self.create_new_user)

    def show_widgets(self):
        self.newUserTitleLabel.show()
        login.loginBackgroundLabel.show()
        self.returnToLoginButton.show()
        self.newUsernameEntry.show()
        self.newPasswordEntry.show()
        self.createNewUserButton.show()
        self.newUserClassEntry.show()

    def hide_widgets(self):
        self.newUserTitleLabel.hide()
        login.loginBackgroundLabel.hide()
        self.returnToLoginButton.hide()
        self.newUsernameEntry.hide()
        self.newPasswordEntry.hide()
        self.createNewUserButton.hide()
        self.newUserClassEntry.hide()
        self.newUserErrorLabel.hide()

    def create_new_user(self):
        if self.username_exists():
            self.newUserErrorLabel.setText("Username already taken")
            self.newUserErrorLabel.show()
            self.newUsernameEntry.setText("")
            self.newUsernameEntry.setFocus()
        elif len(self.newUsernameEntry.text()) < 3:
            self.newUserErrorLabel.setText("Username must be at least 3 characters long")
            self.newUserErrorLabel.show()
            self.newUsernameEntry.setText("")
            self.newUsernameEntry.setFocus()
        elif len(self.newPasswordEntry.text()) < 3:
            self.newUserErrorLabel.setText("Password must be at least 3 characters long")
            self.newUserErrorLabel.show()
            self.newPasswordEntry.setText("")
            self.newPasswordEntry.setFocus()
        elif len(self.newUserClassEntry.text()) < 1:
            self.newUserErrorLabel.setText("Class must be selected")
            self.newUserErrorLabel.show()
        else:
            login.username = self.newUsernameEntry.text()
            data.users[login.username] = self.newPasswordEntry.text()
            self.add_user_to_database()
            self.create_user_database()
            self.hide_widgets()
            home_screen.usernameLabel.setText(login.username)
            self.newUsernameEntry.setText("")
            self.newPasswordEntry.setText("")
            self.newUserClassEntry.setText("")
            home_screen.show_widgets()

    def username_exists(self):
        if os.path.isfile("{}.db".format(self.newUsernameEntry.text())):
            return True
        else:
            return False

    def add_user_to_database(self):
        connection = sqlite3.connect("Usernames and passwords.db")
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO USERS
                                  (username, password, class)  VALUES  (?, ?, ?)""", (self.newUsernameEntry.text(),
                                                                                      self.newPasswordEntry.text(),
                                                                                      self.newUserClassEntry.text()))
        connection.commit()
        cursor.close()
        data.users[self.newUsernameEntry.text()] = self.newPasswordEntry.text()

    def create_user_database(self):
        connection = sqlite3.connect("{}.db".format(login.username))
        c = connection.cursor()
        c.execute("""CREATE TABLE QUIZ
                ([generated_id] INTEGER PRIMARY KEY, [Quiz number] integer, [Username] text, [Objective] text,
                [Question] text, [Correct answer] text, [User answer] text, [Marks] integer) """)
        connection.commit()
        connection.close()

    def return_to_login(self):
        self.hide_widgets()
        login.usernameEntry.setText("")
        login.passwordEntry.setText("")
        login.usernameEntry.setFocus()
        login.show_widgets()


class HomeScreen:
    def __init__(self):
        self.year = ""
        self.strand = ""
        self.substrand = ""
        self.objective = ""
        self.chosen_objectives = []

        # Username label
        self.usernameLabel = QtWidgets.QLabel("No one", win)
        self.usernameLabel.setGeometry(475, 115, 600, 65)
        self.usernameLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.usernameLabel.setFont(title_font)
        self.usernameLabel.setAlignment(QtCore.Qt.AlignLeft)

        # Change user button
        self.changeUserButton = QtWidgets.QPushButton(win)
        self.changeUserButton.setGeometry(200, 250, 200, 60)
        self.changeUserButton.setFont(button_font_small)
        self.changeUserButton.setStyleSheet("color: rgb(255, 255, 255); background-color: transparent;"
                                            "text-decoration: underline;")
        self.changeUserButton.setText("Click to change user")
        self.changeUserButton.clicked.connect(self.change_user)

        # User icon
        self.userIconLabel = QtWidgets.QLabel(win)
        self.pixmap = QtGui.QPixmap("C:/Users/Michael/Pictures/Saved Pictures/user_icon.png")
        self.userIconLabel.setPixmap(self.pixmap)
        self.userIconLabel.setGeometry(200, 50, 200, 200)
        self.userIconLabel.setScaledContents(True)

        # Stats background shape
        self.statsBackgroundLabel = QtWidgets.QLabel(win)
        self.statsBackgroundLabel.setGeometry(150, 375, 675, 425)
        self.statsBackgroundLabel.setStyleSheet("background-color: rgb(170, 170, 255);")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        self.statsBackgroundLabel.setGraphicsEffect(shadow)

        # Stats title label
        self.statsTitleLabel = QtWidgets.QLabel(win)
        self.statsTitleLabel.setGeometry(200, 400, 400, 65)
        self.statsTitleLabel.setStyleSheet("text-decoration: underline;")
        self.statsTitleLabel.setText("Stats")
        self.statsTitleLabel.setFont(sub_title_font)
        self.statsTitleLabel.setAlignment(QtCore.Qt.AlignLeft)

        # Stats label 1
        self.statsLabel1 = QtWidgets.QLabel(win)
        self.statsLabel1.setGeometry(200, 475, 250, 400)
        self.statsLabel1.setStyleSheet("color: rgb(25, 40, 65);")
        self.statsLabel1.setText("Quiz taken:\n\nQuestions answered:\n\nHighest score:\n\nTop maths areas:\n\n"
                                 "Key target:")
        self.statsLabel1.setFont(button_font)
        self.statsLabel1.setAlignment(QtCore.Qt.AlignLeft)

        # Stats label 2
        self.statsLabel2 = QtWidgets.QLabel(win)
        self.statsLabel2.setGeometry(475, 475, 400, 400)
        self.statsLabel2.setStyleSheet("")
        self.statsLabel2.setFont(button_font)
        self.statsLabel2.setAlignment(QtCore.Qt.AlignLeft)

        # Quiz answers button
        self.quizAnswersButton = QtWidgets.QPushButton(win)
        self.quizAnswersButton.setGeometry(650, 400, 150, 60)
        self.quizAnswersButton.setFont(button_font)
        self.quizAnswersButton.setStyleSheet("background-color: rgb(197, 180, 227);")
        self.quizAnswersButton.setText("Past quizzes")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(50)
        self.quizAnswersButton.setGraphicsEffect(shadow)
        self.quizAnswersButton.clicked.connect(lambda: self.show_quiz_answers())

        # Quiz background shape
        self.quizBackgroundLabel = QtWidgets.QLabel(win)
        self.quizBackgroundLabel.setGeometry(1000, 375, 775, 425)
        self.quizBackgroundLabel.setStyleSheet("background-color: rgb(170, 170, 255);")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        self.quizBackgroundLabel.setGraphicsEffect(shadow)

        # Quiz title label
        self.quizTitleLabel = QtWidgets.QLabel("Take quiz", win)
        self.quizTitleLabel.setGeometry(1050, 400, 400, 65)
        self.quizTitleLabel.setStyleSheet("text-decoration: underline;")
        self.quizTitleLabel.setFont(sub_title_font)
        self.quizTitleLabel.setAlignment(QtCore.Qt.AlignLeft)

        # Quiz label
        self.quizLabel = QtWidgets.QLabel("Year group\n\n"
                                          "Strand\n\n"
                                          "Sub-strand\n\n"
                                          "Objective", win)
        self.quizLabel.setGeometry(1050, 485, 250, 450)
        self.quizLabel.setStyleSheet("color: rgb(25, 40, 65);")
        self.quizLabel.setFont(test_font)
        self.quizLabel.setAlignment(QtCore.Qt.AlignLeft)

        # Year combo
        self.yearCombo = QtWidgets.QComboBox(win)
        self.yearCombo.setGeometry(1200, 485, 370, 40)
        self.yearCombo.setFont(combo_font)
        year_group_list = ["All", "Year 1", "Year 2", "Year 3", "Year 4", "Year 5", "Year 6"]
        for item in year_group_list:
            self.yearCombo.addItem(item)
        self.yearCombo.activated[str].connect(self.update_quiz_selections)

        # Year group quiz button
        self.yearQuizButton = QtWidgets.QPushButton(win)
        self.yearQuizButton.setGeometry(1600, 475, 150, 60)
        self.yearQuizButton.setFont(button_font)
        self.yearQuizButton.setStyleSheet("background-color: rgb(197, 180, 227);")
        self.yearQuizButton.setText("Launch quiz")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(50)
        self.yearQuizButton.setGraphicsEffect(shadow)
        self.yearQuizButton.clicked.connect(lambda: self.start_quiz("year"))

        # Strand combo
        self.strandCombo = QtWidgets.QComboBox(win)
        self.strandCombo.setGeometry(1200, 559, 370, 40)
        self.strandCombo.setFont(combo_font)
        strand_list = ("Number and place value", "Calculations", "Fractions, decimals and percentages",
                       "Ratio and proportion", "Algebra", "Measurement", "Shape", "Position and direction",
                       "Statistics")
        for item in strand_list:
            self.strandCombo.addItem(item)
        self.strandCombo.activated[str].connect(self.update_substrand_combo)
        self.strandCombo.activated[str].connect(self.update_objective_combo)
        self.strandCombo.activated[str].connect(self.update_quiz_selections)

        # Strand quiz button
        self.strandQuizButton = QtWidgets.QPushButton(win)
        self.strandQuizButton.setGeometry(1600, 549, 150, 60)
        self.strandQuizButton.setFont(button_font)
        self.strandQuizButton.setStyleSheet("background-color: rgb(197, 180, 227);")
        self.strandQuizButton.setText("Launch quiz")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(50)
        self.strandQuizButton.setGraphicsEffect(shadow)
        self.strandQuizButton.clicked.connect(lambda: self.start_quiz("strand"))

        # Sub-strand combo
        self.substrandCombo = QtWidgets.QComboBox(win)
        self.substrandCombo.setGeometry(1200, 633, 370, 40)
        self.substrandCombo.setFont(combo_font)
        self.update_substrand_combo()
        self.substrandCombo.activated[str].connect(self.update_objective_combo)
        self.substrandCombo.activated[str].connect(self.update_quiz_selections)

        # Sub-strand quiz button
        self.substrandQuizButton = QtWidgets.QPushButton(win)
        self.substrandQuizButton.setGeometry(1600, 623, 150, 60)
        self.substrandQuizButton.setFont(button_font)
        self.substrandQuizButton.setStyleSheet("background-color: rgb(197, 180, 227);")
        self.substrandQuizButton.setText("Launch quiz")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(50)
        self.substrandQuizButton.setGraphicsEffect(shadow)
        self.substrandQuizButton.clicked.connect(lambda: self.start_quiz("sub-strand"))

        # Objective combo
        self.objectiveCombo = QtWidgets.QComboBox(win)
        self.objectiveCombo.setGeometry(1200, 707, 370, 40)
        self.objectiveCombo.setFont(combo_font)
        objective_list = ["1N1", "2N1", "3N1b", "4N1", "5N1"]
        for item in objective_list:
            self.objectiveCombo.addItem(item)
        self.objectiveCombo.activated[str].connect(self.update_quiz_selections)

        # Objective quiz button
        self.objectiveQuizButton = QtWidgets.QPushButton(win)
        self.objectiveQuizButton.setGeometry(1600, 697, 150, 60)
        self.objectiveQuizButton.setFont(button_font)
        self.objectiveQuizButton.setStyleSheet("background-color: rgb(197, 180, 227);")
        self.objectiveQuizButton.setText("Launch quiz")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(50)
        self.objectiveQuizButton.setGraphicsEffect(shadow)
        self.objectiveQuizButton.clicked.connect(lambda: self.start_quiz("objective"))

    def show_widgets(self):
        self.usernameLabel.show()
        self.changeUserButton.show()
        self.userIconLabel.show()
        self.statsBackgroundLabel.show()
        self.statsTitleLabel.show()
        self.statsLabel1.show()
        self.statsLabel2.show()
        self.quizAnswersButton.show()
        self.quizBackgroundLabel.show()
        self.quizTitleLabel.show()
        self.quizLabel.show()
        self.yearCombo.show()
        self.strandCombo.show()
        self.substrandCombo.show()
        self.objectiveCombo.show()
        self.yearQuizButton.show()
        self.strandQuizButton.show()
        self.substrandQuizButton.show()
        self.objectiveQuizButton.show()

    def hide_widgets(self):
        self.usernameLabel.hide()
        self.changeUserButton.hide()
        self.userIconLabel.hide()
        self.statsBackgroundLabel.hide()
        self.statsTitleLabel.hide()
        self.statsLabel1.hide()
        self.statsLabel2.hide()
        self.quizAnswersButton.hide()
        self.quizBackgroundLabel.hide()
        self.quizTitleLabel.hide()
        self.quizLabel.hide()
        self.yearCombo.hide()
        self.strandCombo.hide()
        self.substrandCombo.hide()
        self.objectiveCombo.hide()
        self.yearQuizButton.hide()
        self.strandQuizButton.hide()
        self.substrandQuizButton.hide()
        self.objectiveQuizButton.hide()

    def change_user(self):
        self.hide_widgets()
        login.usernameEntry.setText("")
        login.passwordEntry.setText("")
        login.usernameEntry.setFocus()
        login.show_widgets()

    def show_quiz_answers(self):
        """graph_window = pg.plot()
        title = "Maths quiz graphs"
        graph_window.setWindowTitle(title)
        y1 = [5, 5, 7, 10, 3, 8, 9, 1, 6, 2]
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        bar_graph = pg.BarGraphItem(x=x, height=y1, width=0.6, brush='g')
        graph_window.addItem(bar_graph)
        graph_window.setBackground('w')
        graph_window.setTitle("Quiz graphs", size="16pt")
        graph_window.showGrid(x=False, y=True)"""
        model = PandasModel(data.data_frame)
        self.view = QTableView()
        self.view.setModel(model)
        self.view.setWindowTitle("All quiz questions and answers for {}".format(login.username))
        self.view.resize(1200, 600)
        self.view.setColumnWidth(0, 100)
        self.view.setColumnWidth(1, 100)
        self.view.setColumnWidth(2, 570)
        self.view.setColumnWidth(3, 150)
        self.view.setColumnWidth(4, 150)
        self.view.setColumnWidth(5, 100)
        self.view.setAlternatingRowColors(True)
        self.view.show()

    def start_quiz(self, quiz_type):
        if quiz_type == "year" and self.year == "All":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Incorrect quiz selection")
            msg.setText("All objectives cannot be selected for all strands. "
                        "Choose a year group, strand, sub-strand or objective.")
            x = msg.exec_()
        else:
            self.update_quiz_selections()
            quiz.question_list = []
            if quiz_type == "year":
                for objective in objectives_tuple:
                    if objective.startswith(self.year[-1]):
                        quiz.question_list.append(objective)
            elif quiz_type == "strand":
                ref = str(strand_index.get(self.strand))
                for objective in objectives_tuple:
                    if self.year == "All":
                        if objective[1:2] == ref:
                            quiz.question_list.append(objective)
                    else:
                        if objective[1:2] == ref and objective.startswith(self.year[-1]):
                            quiz.question_list.append(objective)
            elif quiz_type == "sub-strand":
                ref = str(substrand_index.get(self.substrand))
                for objective in objectives_tuple:
                    if self.year == "All":
                        if objective[1:3] == ref:
                            quiz.question_list.append(objective)
                    else:
                        if objective[1:3] == ref and objective.startswith(self.year[-1]):
                            quiz.question_list.append(objective)
            elif quiz_type == "objective":
                quiz.question_list = [self.objective]
            else:
                raise TypeError
            self.chosen_objectives = []
            if len(quiz.question_list) == 0:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("No objectives")
                msg.setText("There are no objectives for your chosen selection. Please make another selection.")
                x = msg.exec_()
            else:
                self.hide_widgets()
                for objective in range(30):
                    self.chosen_objectives.append(quiz.question_list[random.randint(0, len(quiz.question_list)-1)])
                data.score = 0
                quiz.question_number = 1
                quiz.set_quiz_number()
                quiz.quiz_number += 1
                quiz.show_widgets()
                quiz.scoreLabel.setText("Score: 0 out of 0")
                quiz.questionNumberLabel.setText("Question 1 of 30")
                quiz.answerEntry.setFocus()
                quiz.ask_question(self.chosen_objectives[0])

    def update_substrand_combo(self):
        substrand_bank = {"Number and place value":
                              ("Counting in multiples", "Read, write, order & compare", "Place value",
                               "Identify, represent, estimate; rounding", "Negative numbers", "Number problems"
                               ),
                          "Calculations":
                              ("Add/subtract mentally", "Add/subtract using written methods",
                               "Estimate and use inverses", "Add/subtract to solve problems", "Properties of number",
                               "Multiply/divide mentally", "Multiply/divide using written methods",
                               "Solve problems using all 4 operations", "Order of operations"
                               ),
                          "Fractions, decimals and percentages":
                              ("Recognise & count fractions", "Equivalent fractions", "Comparing & ordering fractions",
                               "Add/subtract fractions", "Multiply/divide fractions", "Fractions/decimals equivalence",
                               "Rounding decimals", "Compare & order decimals","Multiply/divide decimals",
                               "Solve fraction & decimal problems", "Fractions/decimals/% equivalence",
                               "Solve percentage problems"
                               ),
                          "Ratio and proportion":
                              ("Relative sizes and similarity", "Use of percentages for comparison", "Scale factors",
                               "Unequal sharing and grouping"
                               ),
                          "Algebra":
                              ("Missing number problems in algebra", "Simple formulae expressed in words",
                               "Generate & describe linear number sequences",
                               "Number sentences involving two unknowns",
                               "Enumerate all combinations of two variables"
                               ),
                          "Measurement":
                              ("Compare, describe and order measures", "Estimate, measure and read scales",
                               "Money", "Time", "Convert between metric units", "Convert metric/imperial",
                               "Perimeter and area", "Volume", "Solve problems involving measures"
                               ),
                          "Shape":
                              ("Compare and sort shapes", "Describe properties and classify shapes",
                               "Draw & make shapes & relate 2-D to 3-D", "Angles – measuring and properties",
                               "Circles"
                               ),
                          "Position and direction":
                              ("Order in patterns and sequences", "Describe position, direction and movement",
                               "Co-ordinates"
                               ),
                          "Statistics":
                              ("Interpret and represent data", "Solve problems involving data", "Mean average"
                               )
                          }
        substrand_list = substrand_bank[self.strandCombo.currentText()]
        self.substrandCombo.clear()
        for item in substrand_list:
            self.substrandCombo.addItem(item)

    def update_objective_combo(self):
        objective_bank = {"Counting in multiples": ("1N1", "2N1", "3N1", "4N1", "5N1"),
                          "Read, write, order & compare": ("1N2a", "1N2b", "1N2c", "2N2a", "2N2b", "3N2a", "3N2b",
                                                           "4N2a", "4N2b", "5N2", "6N2"),
                          "Place value": ("2N3", "3N3", "4N3a", "4N3b", "5N3a", "5N3b", "6N3"),
                          "Identify, represent, estimate; rounding": ("1N4", "2N4", "3N4", "4N4a", "4N4b", "5N4", "6N4"),
                          "Negative numbers": ("4N5", "5N5", "6N5"),
                          "Number problems": ("2N6", "3N6", "4N6", "5N6", "6N6"),
                          "Add/subtract mentally": ("1C1", "2C1", "3C1", "5C1"),
                          "Add/subtract using written methods": ("1C2a", "1C2b", "2C2a", "2C2b", "3C2", "4C2", "5C2"),
                          "Estimate and use inverses": ("2C3", "3C3", "4C3", "5C3", "6C3"),
                          "Add/subtract to solve problems": ("1C4", "2C4", "3C4", "4C4", "5C4", "6C4"),
                          "Properties of number": ("5C5a", "5C5b", "5C5c", "5C5d", "6C5"),
                          "Multiply/divide mentally": ("2C6", "3C6", "4C6a", "4C6b", "4C6c", "5C6a", "5C6b", "6C6"),
                          "Multiply/divide using written methods": ("2C7", "3C7", "4C67", "5C7a", "5C7b", "6C7a",
                                                                    "6C7b", "6C7c"),
                          "Solve problems using all 4 operations": ("1C8", "2C8", "3C8", "4C8", "5C8a", "5C8b",
                                                                    "5C8c", "6C8"),
                          "Order of operations": ("2C9a", "2C9b", "6C9"),
                          "Recognise & count fractions": ("1F1a", "1F1b", "2F1a", "2F1b", "3F1a", "3F1b", "3F1c",
                                                          "4F1"),
                          "Equivalent fractions": ("2F2", "3F2", "4F2", "5F2a", "5F2b", "6F2"),
                          "Comparing & ordering fractions": ("3F3", "5F3", "6F3"),
                          "Add/subtract fractions": ("3F4", "4F4", "5F4", "6F4"),
                          "Multiply/divide fractions": ("5F5", "6F5a", "6F5b"),
                          "Fractions/decimals equivalence": ("4F6a", "4F6b", "5F6a", "5F6b", "6F6"),
                          "Rounding decimals": ("4F7", "5F7"),
                          "Compare & order decimals": ("4F8", "5F8"),
                          "Multiply/divide decimals": ("4F9", "6F9a", "6F9b", "6F9c"),
                          "Solve fraction & decimal problems": ("3F10", "4F10a", "4F10b", "5F10", "6F10"),
                          "Fractions/decimals/% equivalence": ("5F11", "6F11"),
                          "Solve percentage problems": "5F12",
                          "Relative sizes and similarity": "6R1",
                          "Use of percentages for comparison": "6R2",
                          "Scale factors": "6R3",
                          "Unequal sharing and grouping": "6R4",
                          "Missing number problems in algebra": "6A1",
                          "Simple formulae expressed in words": "6A2",
                          "Generate & describe linear number sequences": "6A3",
                          "Number sentences involving two unknowns": "6A4",
                          "Enumerate all combinations of two variables": "6A5",
                          "Compare, describe and order measures": ("1M1", "2M1", "3M1a", "3M1b", "3M1c", "4M1"),
                          "Estimate, measure and read scales": ("1M2", "2M2", "3M2a", "3M2b", "3M2c", "4M2"),
                          "Money": ("1M3", "2M3a", "2M3b"),
                          "Time": ("1M4a", "1M4b", "1M4c", "2M4a", "2M4b", "2M4c", "3M4a", "3M4b", "3M4c", "3M4d",
                                   "3M4e", "3M4f", "4M4a", "4M4b", "4M4c", "5M4"),
                          "Convert between metric units": ("4M5", "5M5", "6M5"),
                          "Convert metric/imperial": ("5M6", "6M6"),
                          "Perimeter and area": ("3M7", "4M7a", "4M7b", "5M7a", "5M7b", "6M7a", "6M7b", "6M7c"),
                          "Volume": ("5M8", "6M8a", "6M8b"),
                          "Solve problems involving measures": ("2M9", "3M9a", "3M9b", "3M9c", "3M9d", "4M9", "5M9a",
                                                                "5M9b", "5M9c", "5M9d", "6M9"),
                          "Compare and sort shapes": ("1G1a", "1G1b", "2G1a", "2G1b"),
                          "Describe properties and classify shapes": ("2G2a", "2G2b", "3G2", "4G2a", "4G2b", "4G2c",
                                                                      "5G2a", "5G2b", "6G2a", "6G2b"),
                          "Draw & make shapes & relate 2-D to 3-D": ("2G3", "3G3a", "3G3b", "5G3", "6G3a", "6G3b"),
                          "Angles – measuring and properties": ("3G4a", "3G4b", "4G4", "5G4a", "5G4b", "5G4c", "6G4a",
                                                                "6G4b"),
                          "Circles": "6G5",
                          "Order in patterns and sequences": "2P1",
                          "Describe position, direction and movement": ("1P2", "2P2", "4P2", "5P2", "6P2"),
                          "Co-ordinates": ("4P3a", "4P3b", "6P3"),
                          "Interpret and represent data": ("2S1", "3S1", "4S1", "5S1", "6S1"),
                          "Solve problems involving data": ("2S2a", "2S2b", "3S2", "4S2", "5S2"),
                          "Mean average": "6S3"
                          }
        objective_list = objective_bank[self.substrandCombo.currentText()]
        self.objectiveCombo.clear()
        if type(objective_list) is tuple:
            for item in objective_list:
                self.objectiveCombo.addItem(item)
        else:
            self.objectiveCombo.addItem(objective_list)

    def update_quiz_selections(self):
        self.year = self.yearCombo.currentText()
        self.strand = self.strandCombo.currentText()
        self.substrand = self.substrandCombo.currentText()
        self.objective = self.objectiveCombo.currentText()


class Quiz:
    def __init__(self):
        self.question = ""
        self.question_number = 1
        self.correct_answer = ""
        self.question_list = []
        self.question_text = ""
        self.quiz_number = 0

        # Question number label
        self.questionNumberLabel = QtWidgets.QLabel("Question 1 of 30", win)
        place_widget_centre(self.questionNumberLabel, 500, 60, 190)
        self.questionNumberLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.questionNumberLabel.setFont(title_font)
        self.questionNumberLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Question label
        self.question_number = 1
        self.questionLabel = QtWidgets.QLabel("Question goes here", win)
        place_widget_centre(self.questionLabel, 1200, 150, 350)
        self.questionLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.questionLabel.setFont(question_font)
        self.questionLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Answer entry box
        self.answerEntry = QtWidgets.QLineEdit(win)
        place_widget_centre(self.answerEntry, 350, 60, 600)
        self.answerEntry.setFont(entry_box_font)
        self.answerEntry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.answerEntry.setText("")
        self.answerEntry.setPlaceholderText("Answer here")

        # Submit answer button
        self.submitAnswerButton = QtWidgets.QPushButton(win)
        place_widget_centre(self.submitAnswerButton, 350, 60, 675)
        self.submitAnswerButton.setFont(button_font)
        self.submitAnswerButton.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.submitAnswerButton.setText("Submit answer")
        self.submitAnswerButton.clicked.connect(self.submit_answer)

        # Quit quiz button
        self.quitQuizButton = QtWidgets.QPushButton(win)
        place_widget_centre(self.quitQuizButton, 150, 60, 850)
        self.quitQuizButton.setFont(button_font)
        self.quitQuizButton.setStyleSheet("background-color: rgb(169, 169, 169);")
        self.quitQuizButton.setText("Quit quiz")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(50)
        self.quitQuizButton.setGraphicsEffect(shadow)
        self.quitQuizButton.clicked.connect(lambda: self.quit_quiz())

        # Score label
        self.scoreLabel = QtWidgets.QLabel("Score: 0 out of 0", win)
        place_widget_centre(self.scoreLabel, 200, 60, 75)
        self.scoreLabel.setStyleSheet("background-color: rgb(245, 245, 220);")
        self.scoreLabel.setFont(button_font)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(50)
        self.scoreLabel.setGraphicsEffect(shadow)
        self.scoreLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Final score label
        self.finalScoreLabel = QtWidgets.QLabel("Score: 0 out of 0", win)
        place_widget_centre(self.finalScoreLabel, 1200, 150, 350)
        self.finalScoreLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.finalScoreLabel.setFont(title_font)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(50)
        self.finalScoreLabel.setGraphicsEffect(shadow)
        self.finalScoreLabel.setAlignment(QtCore.Qt.AlignCenter)

        # End of quiz button
        self.endOfQuizButton = QtWidgets.QPushButton(win)
        place_widget_centre(self.endOfQuizButton, 150, 60, 850)
        self.endOfQuizButton.setFont(button_font)
        self.endOfQuizButton.setStyleSheet("background-color: rgb(169, 169, 169);")
        self.endOfQuizButton.setText("Return home")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(50)
        self.endOfQuizButton.setGraphicsEffect(shadow)
        self.endOfQuizButton.clicked.connect(lambda: self.quit_quiz())

        # Image 1 label
        self.image1Label = QtWidgets.QLabel(win)

    def show_widgets(self):
        self.questionNumberLabel.show()
        self.questionLabel.show()
        self.answerEntry.show()
        self.submitAnswerButton.show()
        self.quitQuizButton.show()
        self.scoreLabel.show()

    def hide_widgets(self):
        self.questionNumberLabel.hide()
        self.questionLabel.hide()
        self.answerEntry.hide()
        self.submitAnswerButton.hide()
        self.quitQuizButton.hide()
        self.scoreLabel.hide()
        self.finalScoreLabel.hide()
        self.endOfQuizButton.hide()

    def ask_question(self, objective):
        place_widget_centre(self.questionLabel, 1200, 150, 350)
        self.question = Qu(objective)
        self.correct_answer = self.question.correct_answer()
        self.question_text = self.question.question_text()
        try:
            pixmap = QtGui.QPixmap(self.question.question.image_1_ref)
            self.image1Label.setPixmap(pixmap)
            place_widget_centre(self.image1Label, self.question.question.image_1_width,
                                self.question.question.image_1_height, self.question.question.image_1_y)
            self.image1Label.setScaledContents(True)
            self.image1Label.show()
            place_widget_centre(self.questionLabel, 1200, 150, self.question.question.question_label_y)
        except:
            pass
        self.questionLabel.setText(self.question_text)

    def submit_answer(self):
        self.check_answer()
        self.answerEntry.setText("")
        self.question_number += 1
        self.questionNumberLabel.setText("Question {} of 30".format(self.question_number))
        self.update_score_label()
        self.answerEntry.setFocus()
        if self.question_number > 30:
            self.end_quiz()
        else:
            self.image1Label.hide()
            self.ask_question(home_screen.chosen_objectives[self.question_number - 1])

    def check_answer(self):
        user_answer = self.answerEntry.text()
        if user_answer == self.correct_answer:
            data.score += 1
            self.update_database(user_answer, 1)
        else:
            self.update_database(user_answer, 0)

    def update_database(self, user_answer, marks):
        connection = sqlite3.connect("{}.db".format(login.username))
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO QUIZ
                                          ('Quiz number', Username, Objective, Question, 'Correct answer',
                                          'User answer', Marks) VALUES  (?, ?, ?, ?, ?, ?, ?)""",
                       (quiz.quiz_number, login.username, home_screen.chosen_objectives[self.question_number - 1],
                        self.question_text, self.correct_answer, user_answer, marks)
                       )
        connection.commit()
        cursor.close()

    def update_score_label(self):
        self.scoreLabel.setText("Score: {} out of {}".format(data.score, self.question_number - 1))

    def end_quiz(self):
        read_data(login.username)
        data.set_stats()
        quiz.hide_widgets()
        self.finalScoreLabel.show()
        self.finalScoreLabel.setText("Final score: {} out of {}".format(data.score, self.question_number - 1))
        self.endOfQuizButton.show()

    def quit_quiz(self):
        read_data(login.username)
        data.set_stats()
        self.hide_widgets()
        self.image1Label.hide()
        home_screen.show_widgets()
        
    def set_quiz_number(self):
        connection = sqlite3.connect("{}.db".format(login.username))
        query = pd.read_sql_query("SELECT * FROM QUIZ", connection)
        print(query['Quiz number'].max())
        try:
            quiz.quiz_number = int((query['Quiz number'].max()))
        except:
            pass
        connection.close()


class PandasModel(QAbstractTableModel):

    def __init__(self, data_frame):
        QAbstractTableModel.__init__(self)
        self._data = data_frame

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return str(self._data.iloc[index.row(), index.column()])
        if role == Qt.TextAlignmentRole and index.column() in (0, 3, 4, 5):
            return Qt.AlignVCenter + Qt.AlignRight
        if role == Qt.BackgroundRole and index.column() not in (0, 1):
            value = str(self._data.iloc[index.row(), 5])
            if value == "0":
                return QtGui.QColor(255, 153, 204)
            elif value == "1":
                return QtGui.QColor(153, 255, 204)

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None


def place_widget_centre(widget, width, height, y):
    widget.setGeometry((screen_size.width() // 2) - width // 2, y, width, height)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    screen = app.primaryScreen()
    screen_size = screen.size()
    win = MyWindow()
    win.show()
    data = Data()
    load_usernames_passwords()
    login = LoginScreen()
    login.show_widgets()
    new_user = NewUserScreen()
    home_screen = HomeScreen()
    quiz = Quiz()

    sys.exit(app.exec_())
