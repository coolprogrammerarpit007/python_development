# PyQt5 Introduction

import sys
import os
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QWidget
from PyQt5.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.setGeometry(700,300,500,500)

       

def main():

    # creating app and window objects and calling their respective constructors.
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()