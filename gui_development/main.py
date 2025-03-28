import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QPixmap

# Best way to load images is load with Label
# QPixmap is used to handle images.
# we will load our images on QPixmap then QPinmap on label to display images
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)

        label = QLabel(self)
        label.setGeometry(0,0,250,250)

        pixmap = QPixmap("peacock.jpg")
        label.setPixmap(pixmap)
        label.setScaledContents(True)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()