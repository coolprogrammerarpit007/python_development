# PyQt5 Introduction

import sys
import os
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
# from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
# file_exists = os.path.exists("profile.jpg")
# print(file_exists)
# exit(1)
class MainWindow(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.setWindowTitle("My First GUI Application")
        self.setGeometry(700,300,500,500)
        # self.setWindowIcon(QIcon("profile.ico"))

        label = QLabel("Hello",self)
        label.setFont(QFont("Arial",50))
        label.setGeometry(0,0,500,100)
        label.setStyleSheet("color:blue;background-color:#6fdcf7;font-weight:bold;font-style:italic;text-decoration:underline")


def main():

    # creating app and window objects and calling their respective constructors.
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()