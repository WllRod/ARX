from PyQt5.QtWidgets import (QWidget, QSlider, QDateEdit, QComboBox, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow, QFrame, QSizePolicy, QCheckBox, QDialog, QTimeEdit)
from PyQt5.QtCore import Qt, QSize, QDate, QTime
from PyQt5 import QtWidgets, uic
import sys
from datetime import datetime

class Add_Obra(QScrollArea):

    def __init__(self):
        super(Add_Cargo, self).__init__()
        self.dlg = QDialog()
        self.dlg.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.dlg.setWindowTitle("Cadastro de Cargo")
        self.dlg.setStyleSheet(u"""
        background-color: rgb(40, 40, 40); 
        
        font-size: 17px;
        color: rgb(201, 198, 177);""")
        
        
        
        self.dlg.setMinimumSize(QSize(250, 350))

        self.verticalLayout = QVBoxLayout(self.dlg)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.dlg)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Name_Frame = QFrame(self.frame)
        self.Name_Frame.setObjectName(u"Name_Frame")
        self.Name_Frame.setFrameShape(QFrame.StyledPanel)
        self.Name_Frame.setFrameShadow(QFrame.Raised)
        self.verticalName_Layout    = QVBoxLayout(self.Name_Frame)

        self.name_label = QLabel("Nome")
        self.name_input = QLineEdit()
        self.name_input.setStyleSheet("background: white; border-radius: 2px; color: black;")
        self.name_input.setText("")
        self.verticalName_Layout.addWidget(self.name_label)
        self.verticalName_Layout.addWidget(self.name_input)

        self.verticalLayout.addWidget(self.Name_Frame)

        
        self.frame_4 = QFrame(self.dlg)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.layoutButton   = QVBoxLayout(self.frame_4)
        self.sub_button = QPushButton("Salvar")
        
        
        self.sub_button.setStyleSheet("""
        background-color: rgb(201, 198, 177);
        font-size: 17px;
        color: black;
        """)
        
        self.sub_button.setMinimumSize(QSize(360, 30))
        self.sub_button.setMaximumSize(QSize(360, 30))
        self.sub_button.setCursor(Qt.PointingHandCursor)
        self.layoutButton.addWidget(self.sub_button, alignment=Qt.AlignCenter)

        self.verticalLayout.addWidget(self.frame_4)

class Edit_Obra(QScrollArea):
    def __init__(self, data):
        super(Edit_Cargo, self).__init__()
        self.dialog = Add_Cargo()
        
        self.dialog.name_input.setText(data[0][1])
        
