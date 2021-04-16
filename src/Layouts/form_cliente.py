from PyQt5.QtWidgets import (QWidget, QSlider, QDateEdit, QComboBox, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow, QFrame, QSizePolicy, QCheckBox, QDialog, QTimeEdit)
from PyQt5.QtCore import Qt, QSize, QDate, QTime
from PyQt5 import QtWidgets, uic
import sys
from datetime import datetime

class Window_Add_Cliente(QScrollArea):

    def __init__(self):
        super(Window_Add_Cliente, self).__init__()
        self.dlg = QDialog()
        self.dlg.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.dlg.setWindowTitle("Cadastro de Cliente")
        self.dlg.setStyleSheet(u"""
        background-color: rgb(40, 40, 40); 
        
        font-size: 17px;
        color: rgb(201, 198, 177);""")
        
        
        
        self.dlg.setMinimumSize(QSize(500, 350))

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
        self.cnpj_frame = QFrame(self.frame)
        self.cnpj_frame.setObjectName(u"cnpj_frame")
        self.cnpj_frame.setFrameShape(QFrame.StyledPanel)
        self.cnpj_frame.setFrameShadow(QFrame.Raised)
        self.verticalCnpj_layout    = QVBoxLayout(self.cnpj_frame)

        self.cnpj_label = QLabel("CNPJ")
        self.cnpj_input = QLineEdit()
        self.cnpj_input.setStyleSheet("background: white; border-radius: 2px; color: black;")

        self.verticalCnpj_layout.addWidget(self.cnpj_label)
        self.verticalCnpj_layout.addWidget(self.cnpj_input)

        self.horizontalLayout.addWidget(self.cnpj_frame)

        self.nome_frame = QFrame(self.frame)
        self.nome_frame.setObjectName(u"CPF")
        self.nome_frame.setFrameShape(QFrame.StyledPanel)
        self.nome_frame.setFrameShadow(QFrame.Raised)

        self.verticalNome_layout    = QVBoxLayout(self.nome_frame)

        self.nome_label = QLabel("Nome")
        self.nome_input = QLineEdit()
        self.nome_input.setStyleSheet("background: white; border-radius: 2px; color: black;")

        self.verticalNome_layout.addWidget(self.nome_label)
        self.verticalNome_layout.addWidget(self.nome_input)


        self.horizontalLayout.addWidget(self.nome_frame)


        self.verticalLayout.addWidget(self.frame)

        self.frame_5 = QFrame(self.dlg)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Telefone_frame = QFrame(self.frame_5)
        self.Telefone_frame.setObjectName(u"Telefone")
        self.Telefone_frame.setFrameShape(QFrame.StyledPanel)
        self.Telefone_frame.setFrameShadow(QFrame.Raised)

        self.verticalTelefone_Layout    = QVBoxLayout(self.Telefone_frame)

        self.telefoneLabel = QLabel("Telefone")
        self.telefoneInput = QLineEdit()
        self.telefoneInput.setStyleSheet("background: white; border-radius: 2px; color: black;")

        self.verticalTelefone_Layout.addWidget(self.telefoneLabel)
        self.verticalTelefone_Layout.addWidget(self.telefoneInput)

        self.horizontalLayout_2.addWidget(self.Telefone_frame)

        self.email_Frame = QFrame(self.frame_5)
        self.email_Frame.setObjectName(u"email_Frame")
        self.email_Frame.setFrameShape(QFrame.StyledPanel)
        self.email_Frame.setFrameShadow(QFrame.Raised)
        
        self.verticalEmail_Layout    = QVBoxLayout(self.email_Frame)
        self.email_label = QLabel("Email")
        self.email_input = QLineEdit()
        self.email_input.setStyleSheet("background: white; border-radius: 2px; color: black;")

        self.verticalEmail_Layout.addWidget(self.email_label)
        self.verticalEmail_Layout.addWidget(self.email_input)


        self.horizontalLayout_2.addWidget(self.email_Frame)

        


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_3 = QFrame(self.dlg)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        
        

        self.endereco_frame = QFrame(self.frame_3)
        self.endereco_frame.setObjectName(u"email")
        self.endereco_frame.setFrameShape(QFrame.StyledPanel)
        self.endereco_frame.setFrameShadow(QFrame.Raised)

        self.verticalEndereco_layout    = QVBoxLayout(self.endereco_frame)
        self.endereco_label = QLabel("Endereço")
        self.endereco_input = QLineEdit()
        self.endereco_input.setStyleSheet("background: white; border-radius: 2px; color: black;")

        self.verticalEndereco_layout.addWidget(self.endereco_label)
        self.verticalEndereco_layout.addWidget(self.endereco_input)

        self.horizontalLayout_3.addWidget(self.endereco_frame)
 
        self.verticalLayout.addWidget(self.frame_3)

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

class Edit_Func(QScrollArea):
    def __init__(self, data):
        self.dialog = Window_Add_Func()
        self.dialog.cnpj_input.setText(data[0][1])
        self.dialog.nome_input.setText(data[0][2])
        self.dialog.telefoneInput.setText(data[0][3])
        self.dialog.salario_input.setText(str(data[0][4]))
        self.dialog.email_inpit.setDate(QDate(data[0][5]))
        self.dialog.endereco_input.setText(data[0][6])
        self.dialog.Telefone_input.setText(data[0][7])
        str_to_time = datetime.strptime(str(data[0][8]), "%H:%M:%S")
        self.dialog.Horas_Trab_Dia_input.setTime(QTime(
            int(str_to_time.strftime("%H")),
            int(str_to_time.strftime("%M")),
            int(str_to_time.strftime("%S")),
        ))
                
        #self.dialog.cnpj_label.setText
        
        