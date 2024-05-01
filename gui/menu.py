from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("ToolKit")
        self.setMinimumSize(800, 400)
        self.setStatusBar(QStatusBar(self))
        
        menu = self.menuBar()

        pdfMenu = menu.addMenu('&File')
        
class toolButton(Q)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()