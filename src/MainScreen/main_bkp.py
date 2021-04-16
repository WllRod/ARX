from PyQt5.QtGui import QPixmap, QCursor, QFontDatabase, QFont, QPainter, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QHBoxLayout, QPushButton, QMainWindow, QVBoxLayout, QLabel, QLineEdit
from PyQt5.QtCore import QSize, QRect, Qt, QDir
from PyQt5.QtSvg import QSvgRenderer, QSvgWidget
import sys
import os

cwd     = os.path.dirname(sys.argv[0])
assets  = cwd+"/assets"
fonts   = cwd+"/assets/Fonts/Roboto-Italic.ttf"

show                = False

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.open_hamb_menu = False
        self.background()
        self.contents()

        self.setCentralWidget(self.centralWidget)

        self.setMinimumSize(QSize(400, 600))

        self.showMaximized()

    def background(self):
        self.centralWidget      = QWidget()
        self.verticalLayout_1   = QVBoxLayout(self.centralWidget)
        self.verticalLayout_1.setSpacing(0)
        self.verticalLayout_1.setContentsMargins(0, 0, 0, 0)

        self.Background         = QFrame(self.centralWidget)
        self.Background.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.Background.setFrameShape(QFrame.StyledPanel)
        self.Background.setFrameShadow(QFrame.Raised)
        self.verticalLayout_1.addWidget(self.Background)

    def contents(self):

        self.vertical_layout_2   = QVBoxLayout(self.Background)
        self.vertical_layout_2.setSpacing(0)
        self.vertical_layout_2.setContentsMargins(0, 0, 0, 0)

        self.frame_1            = QFrame(self.Background)
        self.frame_1.setFrameShadow(QFrame.Raised)
        self.frame_1.setFrameShape(QFrame.StyledPanel)

        self.frame_1.setStyleSheet("""background-color: red;""")
        self.frame_1.setMaximumHeight(100)

        self.vertical_layout_2.addWidget(self.frame_1)         

        self.frame_2            = QFrame(self.Background)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setFrameShape(QFrame.StyledPanel)

        self.frame_2.setStyleSheet("""background-color: yellow;""")

        self.hamb_menu = QPushButton(self.frame_1)
        self.hamb_menu.setText("Texto")
        self.hamb_menu.clicked.connect(self.hamb_menu_click)
        self.vertical_layout_2.addWidget(self.frame_2)   

    def hamb_menu_click(self):
        print('Teste')
        

App = QApplication(sys.argv)
window = MainWindow()
sys.exit(App.exec())