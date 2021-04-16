from PyQt5.QtGui import QPixmap, QCursor, QFontDatabase, QFont, QPainter, QIcon
from PyQt5.QtWidgets import (
    QApplication, 
    QWidget, 
    QFrame, 
    QHBoxLayout, 
    QGridLayout,
    QPushButton, 
    QMainWindow,
    QVBoxLayout, 
    QLabel, 
    QLineEdit,
    QProgressBar,
    QDialog,
    QMessageBox)
from PyQt5.QtCore import QSize, QRect, Qt, QDir, QTimer, QDate

class Title_Bar(QWidget):
    def __init__(self):
        super(Title_Bar, self).__init__()
        self.frame              = QFrame()
        #self.frame.setStyleSheet("background: black;")
        self.frame.setMaximumHeight(40)
        self.horizontalLayout   = QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title        = QFrame()
        self.frame_title.setStyleSheet("background: black;")
        self.frame_title.setFixedWidth(1500)
        self.frame_buttons      = QFrame()
        self.horizontalButtons  = QHBoxLayout(self.frame_buttons)
        #self.frame_buttons.setStyleSheet("background: red;")

        self.button_minimize    = QPushButton()
        self.button_minimize.setIcon(QIcon("assets\\minimize.png"))
        #self.button_minimize.clicked.connect(lambda: self.minimize_screen())
        #self.button_minimize.clicked.connect(self.minimize_screen)
        #self.button_minimize.setIcon(QIcon())
        
        self.button_close       = QPushButton()
        self.button_close.setText("<strong>X</strong>")
        #self.button_close.setIcon(QIcon("assets\\close_screen.png"))
        
        self.button_close.setStyleSheet(
            """
            QPushButton{
                background: transparent;
                color: white;
            }
            QPushButton:hover{
                background: #E81123;
                border: 0;
            }
            """
        )
        

        self.horizontalButtons.addWidget(self.button_minimize)
        
        self.horizontalButtons.addWidget(self.button_close)
        self.horizontalLayout.addWidget(self.frame_title)
        self.horizontalLayout.addWidget(self.frame_buttons)

    def minimize_screen(self):
        self.showMinimized()
