from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread, QTimer, QSize
from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QDialog,
    QApplication,
    QPushButton,
    QGridLayout,
    QProgressBar,
    QLabel,
    QWidget, 
    QMessageBox,
    QMainWindow,
    QHBoxLayout,
    QFrame, 
    QDesktopWidget
    
)
from PyQt5.QtGui import *
import numpy as np

class SpecialDialog(QMainWindow):
    def __init__(self):
        super(SpecialDialog, self).__init__()
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.init_ui()
        self.activateWindow()
        self.variable = np.random.randint(0, 100)

    def init_ui(self):
        self.resize(250, 150)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.widget = QWidget(self)
        self.widget.setStyleSheet("background: red;")
        self.widget.setFixedSize(QSize(250, 150))
        self.movie  = QMovie("assets\\loading.gif")
        self.movie.setScaledSize(QSize(250, 150))
        self.label  = QLabel(self.widget)
        self.label.setFixedSize(QSize(250, 150))
        self.label.setMovie(self.movie)
        self.movie.start()
        
        self.center()
        self.setWindowTitle('Center')
        
        self.show()

    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())
        