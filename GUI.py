from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QGraphicsDropShadowEffect, QVBoxLayout,\
    QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure
import seaborn as sb
import matplotlib
import sys


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

users = {"Michael Berry": "ABC", "Barry": "ABCD"}


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

        # New user button
        self.newUserButton = QtWidgets.QPushButton(win)
        place_widget_centre(self.newUserButton, 350, 60, 580)
        self.newUserButton.setFont(button_font)
        self.newUserButton.setStyleSheet("color: rgb(255, 255, 255); background-color: transparent;"
                                         "text-decoration: underline;")
        self.newUserButton.setText("Click to add new user")
        self.newUserButton.clicked.connect(self.new_user)

    def check_login(self):
        if self.usernameEntry.text() in users:
            if self.passwordEntry.text() == users.get(self.usernameEntry.text()):
                self.username = self.usernameEntry.text()
                self.login_user()
            else:
                print("Wrong password")
        else:
            print("Username not found")
        self.usernameEntry.setText("")
        self.passwordEntry.setText("")

    def login_user(self):
        self.hide_widgets()
        home_screen.usernameLabel.setText(self.username)
        home_screen.show_widgets()

    def new_user(self):
        self.hide_widgets()
        home_screen.show_widgets()

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
        self.newUserButton.hide()


class HomeScreen:
    def __init__(self):
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
        self.statsTitleLabel = QtWidgets.QLabel("Stats", win)
        self.statsTitleLabel.setGeometry(200, 400, 400, 65)
        self.statsTitleLabel.setStyleSheet("text-decoration: underline;")
        self.statsTitleLabel.setFont(sub_title_font)
        self.statsTitleLabel.setAlignment(QtCore.Qt.AlignLeft)

        # Stats button
        self.statsButton = QtWidgets.QPushButton(win)
        self.statsButton.setGeometry(150, 825, 150, 60)
        self.statsButton.setFont(button_font)
        self.statsButton.setStyleSheet("background-color: rgb(197, 180, 227);")
        self.statsButton.setText("Stats")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        self.statsButton.setGraphicsEffect(shadow)
        self.statsButton.clicked.connect(lambda: self.show_stats())

        # Stats label 1
        self.statsLabel1 = QtWidgets.QLabel("Questions taken:\n\n"
                                            "Questions answer:\n\n"
                                            "Highest score:\n\n"
                                            "Top maths areas:\n\n"
                                            "Key target:", win)
        self.statsLabel1.setGeometry(200, 475, 200, 400)
        self.statsLabel1.setStyleSheet("")
        self.statsLabel1.setFont(button_font)
        self.statsLabel1.setAlignment(QtCore.Qt.AlignLeft)

        # Stats label 2
        self.statsLabel2 = QtWidgets.QLabel("7\n\n"
                                            "243\n\n"
                                            "92%\n\n"
                                            "Number and place value\n\n"
                                            "Fractions", win)
        self.statsLabel2.setGeometry(450, 475, 400, 400)
        self.statsLabel2.setStyleSheet("")
        self.statsLabel2.setFont(button_font)
        self.statsLabel2.setAlignment(QtCore.Qt.AlignLeft)

        # Year group button
        self.yearGroupButton = QtWidgets.QPushButton(win)
        self.yearGroupButton.setGeometry(325, 825, 150, 60)
        self.yearGroupButton.setFont(button_font)
        self.yearGroupButton.setStyleSheet("background-color: rgb(197, 180, 227);")
        self.yearGroupButton.setText("Year group")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        self.yearGroupButton.setGraphicsEffect(shadow)
        self.yearGroupButton.clicked.connect(lambda: self.show_year())

        # Year group label 1
        self.yearLabel1 = QtWidgets.QLabel("Year group\n\n"
                                           "categories here", win)
        self.yearLabel1.setGeometry(200, 475, 200, 400)
        self.yearLabel1.setStyleSheet("")
        self.yearLabel1.setFont(button_font)
        self.yearLabel1.setAlignment(QtCore.Qt.AlignLeft)

        # Year group label 2
        self.yearLabel2 = QtWidgets.QLabel("Data goes here", win)
        self.yearLabel2.setGeometry(450, 475, 400, 400)
        self.yearLabel2.setStyleSheet("")
        self.yearLabel2.setFont(button_font)
        self.yearLabel2.setAlignment(QtCore.Qt.AlignLeft)

        # Strand button
        self.strandButton = QtWidgets.QPushButton(win)
        self.strandButton.setGeometry(500, 825, 150, 60)
        self.strandButton.setFont(button_font)
        self.strandButton.setStyleSheet("background-color: rgb(197, 180, 227);")
        self.strandButton.setText("By strand")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        self.strandButton.setGraphicsEffect(shadow)
        self.strandButton.clicked.connect(lambda: self.show_strand())

        # Strand label 1
        self.strandLabel1 = QtWidgets.QLabel("Strand\n\n"
                                             "categories here", win)
        self.strandLabel1.setGeometry(200, 475, 200, 400)
        self.strandLabel1.setStyleSheet("")
        self.strandLabel1.setFont(button_font)
        self.strandLabel1.setAlignment(QtCore.Qt.AlignLeft)

        # Strand label 2
        self.strandLabel2 = QtWidgets.QLabel("Data goes here", win)
        self.strandLabel2.setGeometry(450, 475, 400, 400)
        self.strandLabel2.setStyleSheet("")
        self.strandLabel2.setFont(button_font)
        self.strandLabel2.setAlignment(QtCore.Qt.AlignLeft)

        # Objective button
        self.objectiveButton = QtWidgets.QPushButton(win)
        self.objectiveButton.setGeometry(675, 825, 150, 60)
        self.objectiveButton.setFont(button_font)
        self.objectiveButton.setStyleSheet("background-color: rgb(197, 180, 227);")
        self.objectiveButton.setText("By objective")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        self.objectiveButton.setGraphicsEffect(shadow)
        self.objectiveButton.clicked.connect(lambda: self.show_objective())

        # Objective label 1
        self.objectiveLabel1 = QtWidgets.QLabel("Objectives\n\n"
                                                "categories here", win)
        self.objectiveLabel1.setGeometry(200, 475, 200, 400)
        self.objectiveLabel1.setStyleSheet("")
        self.objectiveLabel1.setFont(button_font)
        self.objectiveLabel1.setAlignment(QtCore.Qt.AlignLeft)

        # Strand label 2
        self.objectiveLabel2 = QtWidgets.QLabel("Data goes here", win)
        self.objectiveLabel2.setGeometry(450, 475, 400, 400)
        self.objectiveLabel2.setStyleSheet("")
        self.objectiveLabel2.setFont(button_font)
        self.objectiveLabel2.setAlignment(QtCore.Qt.AlignLeft)

        # Quiz background shape
        self.quizBackgroundLabel = QtWidgets.QLabel(win)
        self.quizBackgroundLabel.setGeometry(1100, 375, 675, 425)
        self.quizBackgroundLabel.setStyleSheet("background-color: rgb(170, 170, 255);")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        self.quizBackgroundLabel.setGraphicsEffect(shadow)

        # Quiz title label
        self.quizTitleLabel = QtWidgets.QLabel("Take quiz", win)
        self.quizTitleLabel.setGeometry(1150, 400, 400, 65)
        self.quizTitleLabel.setStyleSheet("text-decoration: underline;")
        self.quizTitleLabel.setFont(sub_title_font)
        self.quizTitleLabel.setAlignment(QtCore.Qt.AlignLeft)

        # Quiz label
        self.quizLabel = QtWidgets.QLabel("Year group\n\n"
                                          "Strand\n\n"
                                          "Objective\n\n"
                                          "Questions\n\n", win)
        self.quizLabel.setGeometry(1150, 485, 250, 450)
        self.quizLabel.setStyleSheet("")
        self.quizLabel.setFont(test_font)
        self.quizLabel.setAlignment(QtCore.Qt.AlignLeft)

        # Year group quiz button
        self.yearQuizButton = QtWidgets.QPushButton(win)
        self.yearQuizButton.setGeometry(1550, 475, 150, 60)
        self.yearQuizButton.setFont(button_font)
        self.yearQuizButton.setStyleSheet("background-color: rgb(197, 180, 227);")
        self.yearQuizButton.setText("Launch quiz")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        self.yearQuizButton.setGraphicsEffect(shadow)
        self.yearQuizButton.clicked.connect(lambda: self.show_strand())

        # Strand quiz button
        self.strandQuizButton = QtWidgets.QPushButton(win)
        self.strandQuizButton.setGeometry(1550, 549, 150, 60)
        self.strandQuizButton.setFont(button_font)
        self.strandQuizButton.setStyleSheet("background-color: rgb(197, 180, 227);")
        self.strandQuizButton.setText("Launch quiz")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        self.strandQuizButton.setGraphicsEffect(shadow)
        self.strandQuizButton.clicked.connect(lambda: self.show_strand())

        # Objective quiz button
        self.objectiveQuizButton = QtWidgets.QPushButton(win)
        self.objectiveQuizButton.setGeometry(1550, 623, 150, 60)
        self.objectiveQuizButton.setFont(button_font)
        self.objectiveQuizButton.setStyleSheet("background-color: rgb(197, 180, 227);")
        self.objectiveQuizButton.setText("Launch quiz")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        self.objectiveQuizButton.setGraphicsEffect(shadow)
        self.objectiveQuizButton.clicked.connect(lambda: self.show_strand())

    def show_widgets(self):
        self.usernameLabel.show()
        self.changeUserButton.show()
        self.userIconLabel.show()
        self.statsBackgroundLabel.show()
        self.statsTitleLabel.show()
        self.statsLabel1.show()
        self.statsLabel2.show()
        self.statsButton.show()
        self.yearGroupButton.show()
        self.strandButton.show()
        self.objectiveButton.show()
        self.quizBackgroundLabel.show()
        self.quizTitleLabel.show()
        self.quizLabel.show()
        self.yearQuizButton.show()
        self.strandQuizButton.show()
        self.objectiveQuizButton.show()

    def hide_widgets(self):
        self.usernameLabel.hide()
        self.changeUserButton.hide()
        self.userIconLabel.hide()
        self.statsBackgroundLabel.hide()
        self.statsTitleLabel.hide()
        self.statsButton.hide()
        self.hide_stats()
        self.yearGroupButton.hide()
        self.strandButton.hide()
        self.objectiveButton.hide()
        self.quizBackgroundLabel.hide()
        self.quizTitleLabel.hide()
        self.quizLabel.hide()
        self.yearQuizButton.hide()
        self.strandQuizButton.hide()
        self.objectiveQuizButton.hide()

    def hide_stats(self):
        self.statsLabel1.hide()
        self.statsLabel2.hide()
        self.yearLabel1.hide()
        self.yearLabel2.hide()
        self.strandLabel1.hide()
        self.strandLabel2.hide()
        self.objectiveLabel1.hide()
        self.objectiveLabel2.hide()

    def change_user(self):
        self.hide_widgets()
        login.show_widgets()

    def show_stats(self):
        self.yearLabel1.hide()
        self.yearLabel2.hide()
        self.strandLabel1.hide()
        self.strandLabel2.hide()
        self.objectiveLabel1.hide()
        self.objectiveLabel2.hide()
        self.statsLabel1.show()
        self.statsLabel2.show()

    def show_year(self):
        self.statsLabel1.hide()
        self.statsLabel2.hide()
        self.strandLabel1.hide()
        self.strandLabel2.hide()
        self.objectiveLabel1.hide()
        self.objectiveLabel2.hide()
        self.yearLabel1.show()
        self.yearLabel2.show()

    def show_strand(self):
        self.statsLabel1.hide()
        self.statsLabel2.hide()
        self.yearLabel1.hide()
        self.yearLabel2.hide()
        self.objectiveLabel1.hide()
        self.objectiveLabel2.hide()
        self.strandLabel1.show()
        self.strandLabel2.show()

    def show_objective(self):
        self.statsLabel1.hide()
        self.statsLabel2.hide()
        self.yearLabel1.hide()
        self.yearLabel2.hide()
        self.strandLabel1.hide()
        self.strandLabel2.hide()
        self.objectiveLabel1.show()
        self.objectiveLabel2.show()


def place_widget_centre(widget, width, height, y):
    widget.setGeometry((screen_size.width() // 2) - width // 2, y, width, height)


app = QApplication(sys.argv)

screen = app.primaryScreen()
screen_size = screen.size()
win = MyWindow()
win.show()
login = LoginScreen()
login.show_widgets()
home_screen = HomeScreen()

sys.exit(app.exec_())
