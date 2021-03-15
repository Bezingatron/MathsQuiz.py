from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
import sys
import pyqtgraph as pg
import random


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
        if self.usernameEntry.text() in users:
            if self.passwordEntry.text() == users.get(self.usernameEntry.text()):
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
        self.loginErrorLabel.hide()
        self.newUserButton.hide()


class HomeScreen:
    def __init__(self):
        self.year = "Year 1"
        self.strand = "Number and place value"
        self.substrand = "Counting in multiples"
        self.objective = "1N1a"

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

        # Stats label 1
        self.statsLabel1 = QtWidgets.QLabel("Questions taken:\n\n"
                                            "Questions answer:\n\n"
                                            "Highest score:\n\n"
                                            "Top maths areas:\n\n"
                                            "Key target:", win)
        self.statsLabel1.setGeometry(200, 475, 200, 400)
        self.statsLabel1.setStyleSheet("color: rgb(25, 40, 65);")
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

        # Graphs button
        self.graphsButton = QtWidgets.QPushButton(win)
        self.graphsButton.setGeometry(650, 400, 150, 60)
        self.graphsButton.setFont(button_font)
        self.graphsButton.setStyleSheet("background-color: rgb(197, 180, 227);")
        self.graphsButton.setText("Graphs")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(50)
        self.graphsButton.setGraphicsEffect(shadow)
        self.graphsButton.clicked.connect(lambda: self.show_graphs())

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
        year_group_list = ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5", "Year 6"]
        for item in year_group_list:
            self.yearCombo.addItem(item)

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
        objective_list = ["1N1a", "1N1b", "2N1", "3N1b", "4N1", "5N1"]
        for item in objective_list:
            self.objectiveCombo.addItem(item)

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
        self.graphsButton.show()
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
        self.graphsButton.hide()
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

    def show_graphs(self):
        graph_window = pg.plot()
        title = "Maths quiz graphs"
        graph_window.setWindowTitle(title)
        y1 = [5, 5, 7, 10, 3, 8, 9, 1, 6, 2]
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        bar_graph = pg.BarGraphItem(x=x, height=y1, width=0.6, brush='g')
        graph_window.addItem(bar_graph)
        graph_window.setBackground('w')
        graph_window.setTitle("Quiz graphs", size="16pt")
        graph_window.showGrid(x=False, y=True)

    def start_quiz(self, quiz_type):
        self.hide_widgets()
        if quiz_type == "year":
            print("Quiz selected: {}".format(self.yearCombo.currentText()))
        elif quiz_type == "strand":
            print("Strand quiz")
        elif quiz_type == "sub-strand":
            print("Sub-strand quiz")
        elif quiz_type == "objective":
            print("Objective quiz")
        else:
            raise TypeError
        quiz.show_widgets()
        quiz.question_number = 1
        quiz.answerEntry.setFocus()
        quiz.ask_question("3N1")

    def update_substrand_combo(self):
        substrand_bank = {"Number and place value":
                              ("Counting in multiples", "Read, write, order & compare", "Place value", "Rounding",
                               "Negative numbers", "Number problems"
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
        objective_bank = {"Counting in multiples": ("1N1a", "1N1b", "2N1", "3N1b", "4N1", "5N1"),
                          "Read, write, order & compare": ("1N2a", "1N2b", "1N2c", "2N2a", "2N2b", "3N2a", "3N2b",
                                                           "4N2a", "4N2b", "5N2", "6N2"),
                          "Place value": ("2N3", "3N3", "4N3a", "4N3b", "5N3a", "5N3b", "6N3"),
                          "Rounding": ("1N4", "2N4", "3N4", "4N4a", "4N4b", "5N4", "6N4"),
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


class Quiz:
    def __init__(self):
        self.question_number = 1

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

    def show_widgets(self):
        self.questionNumberLabel.show()
        self.questionLabel.show()
        self.answerEntry.show()
        self.submitAnswerButton.show()
        self.quitQuizButton.show()

    def hide_widgets(self):
        self.questionNumberLabel.hide()
        self.questionLabel.hide()
        self.answerEntry.hide()
        self.submitAnswerButton.hide()
        self.quitQuizButton.hide()

    def ask_question(self, objective):
        question = Question(objective)
        question_text = question.question_text()
        self.questionLabel.setText(question_text)

    def submit_answer(self):
        user_answer = self.answerEntry.text()
        self.answerEntry.setText("")
        self.question_number += 1
        self.questionNumberLabel.setText("Question {} of 30".format(self.question_number))
        self.answerEntry.setFocus()
        print("Your answer is {}".format(user_answer))
        if self.question_number > 30:
            self.questionLabel.setText("End of quiz")
        else:
            self.ask_question("3N1")

    def quit_quiz(self):
        self.hide_widgets()
        home_screen.show_widgets()


class Question:
    def __init__(self, objective):
        # Initiates relevant question object and determines the question and correct answer
        if objective == "1N1":
            self.question = Objective1N1()
        elif objective == "2N1":
            self.question = Objective2N1()
        elif objective == "3N1":
            self.question = Objective3N1()
        # All answers are converted to strings to allow for both numeric and written answers
        self.correct_answer = str(self.question.correct_answer).lower()

    def question_text(self):
        return self.question.question_text

    #def check_answer(self):
        #if self.user_answer == self.correct_answer:
        #    print("Correct! The answer is {}.\n".format(self.correct_answer))
        #else:
        #    print("Incorrect. Your answer was {}. The correct answer is {}.\n".
        #          format(self.user_answer, self.correct_answer))


def question_text_objective_n1(direction, highest_value, multiple):
    if direction:
        return "What is the next number in the sequence?\n\n{}, {}, {}... ". \
            format(highest_value, highest_value - multiple, highest_value - 2 * multiple)
    else:
        return "What is the next number in the sequence?\n\n{}, {}, {}... ". \
            format(highest_value - 2 * multiple, highest_value - multiple, highest_value)


class BasicN1:
    def __init__(self, year_group, multiples):
        self.year_group = year_group
        self.multiples = multiples
        self.direction = random_boolean()
        self.multiple = self.multiple()
        self.highest_value = self.highest_value()
        self.correct_answer = self.correct_answer()
        self.question_text = self.question_text()

    def multiple(self):
        return self.multiples[random.randint(0, len(self.multiples) - 1)]

    def highest_value(self):
        multiplier = random.randint(3, 10)
        return self.multiple * multiplier

    def correct_answer(self):
        if self.direction:
            return self.highest_value - 3 * self.multiple
        else:
            return self.highest_value + self.multiple

    def question_text(self):
        return question_text_objective_n1(self.direction, self.highest_value, self.multiple)


class Objective1N1:
    def __init__(self):
        basic = BasicN1(1, (2, 5, 10))
        self.direction = basic.direction
        self.multiple = basic.multiple
        self.highest_value = basic.highest_value
        self.correct_answer = basic.correct_answer
        self.question_text = basic.question_text


class Objective2N1:
    def __init__(self):
        self.question_type = random_boolean()
        self.direction = random_boolean()
        self.multiples = (2, 3, 5)
        self.multiple = self.multiple()
        self.highest_value = self.highest_value()
        self.correct_answer = self.correct_answer()
        self.question_text = self.question_text()

    def multiple(self):
        if self.question_type:
            return self.multiples[random.randint(0, len(self.multiples) - 1)]
        else:
            return 10

    def highest_value(self):
        if self.question_type:
            return random.randrange(self.multiple * 3, self.multiple * 12, self.multiple)
        else:
            highest_value = random.randint(31, 99)
            while highest_value % 10 == 0:
                highest_value = random.randint(31, 99)
            return highest_value

    def correct_answer(self):
        if self.direction:
            return self.highest_value - 3 * self.multiple
        else:
            return self.highest_value + self.multiple

    def question_text(self):
        return question_text_objective_n1(self.direction, self.highest_value, self.multiple)


class Objective3N1:
    def __init__(self):
        basic = BasicN1(3, (4, 8, 50, 100))
        self.correct_answer = basic.correct_answer
        self.question_text = basic.question_text


def random_boolean():
    return random.randint(0, 1)


def place_widget_centre(widget, width, height, y):
    widget.setGeometry((screen_size.width() // 2) - width // 2, y, width, height)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    screen = app.primaryScreen()
    screen_size = screen.size()
    win = MyWindow()
    win.show()
    login = LoginScreen()
    login.show_widgets()
    home_screen = HomeScreen()
    quiz = Quiz()

    sys.exit(app.exec_())
