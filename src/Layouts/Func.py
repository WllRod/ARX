from PyQt5.QtWidgets import (QWidget, QSlider, QDateEdit, QComboBox, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow, QFrame, QSizePolicy, QCheckBox, QDialog, QTimeEdit)
from PyQt5.QtCore import Qt, QSize, QDate, QTime
from PyQt5 import QtWidgets, uic
import sys
from datetime import datetime

class Window_Add_Func(QScrollArea):

    def __init__(self):
        super(Window_Add_Func, self).__init__()
        self.dlg = QDialog()
        self.dlg.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.dlg.setWindowTitle("Cadastro de Funcionário")
        self.dlg.setStyleSheet(u"""
        background-color: rgb(40, 40, 40); 
        
        font-size: 17px;
        color: rgb(201, 198, 177);""")
        
        
        
        self.dlg.setMinimumSize(QSize(500, 500))

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

        self.verticalName_Layout.addWidget(self.name_label)
        self.verticalName_Layout.addWidget(self.name_input)

        self.horizontalLayout.addWidget(self.Name_Frame)

        self.CPF = QFrame(self.frame)
        self.CPF.setObjectName(u"CPF")
        self.CPF.setFrameShape(QFrame.StyledPanel)
        self.CPF.setFrameShadow(QFrame.Raised)

        self.verticalCPF_Layout    = QVBoxLayout(self.CPF)

        self.cpf_label = QLabel("CPF")
        self.cpf_input = QLineEdit()
        self.cpf_input.setStyleSheet("background: white; border-radius: 2px; color: black;")

        self.verticalCPF_Layout.addWidget(self.cpf_label)
        self.verticalCPF_Layout.addWidget(self.cpf_input)


        self.horizontalLayout.addWidget(self.CPF)


        self.verticalLayout.addWidget(self.frame)

        self.frame_5 = QFrame(self.dlg)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.RG = QFrame(self.frame_5)
        self.RG.setObjectName(u"RG")
        self.RG.setFrameShape(QFrame.StyledPanel)
        self.RG.setFrameShadow(QFrame.Raised)

        self.verticalRG_Layout    = QVBoxLayout(self.RG)

        self.RG_label = QLabel("RG")
        self.RG_input = QLineEdit()
        self.RG_input.setStyleSheet("background: white; border-radius: 2px; color: black;")

        self.verticalRG_Layout.addWidget(self.RG_label)
        self.verticalRG_Layout.addWidget(self.RG_input)

        self.horizontalLayout_2.addWidget(self.RG)

        self.Data_nascimento = QFrame(self.frame_5)
        self.Data_nascimento.setObjectName(u"Data_nascimento")
        self.Data_nascimento.setFrameShape(QFrame.StyledPanel)
        self.Data_nascimento.setFrameShadow(QFrame.Raised)
        
        self.verticalData_nascimento_Layout    = QVBoxLayout(self.Data_nascimento)
        self.Data_nascimento_label = QLabel("Data de Nascimento")
        self.Data_nascimento_input = QDateEdit(calendarPopup=True)
        self.Data_nascimento_input.setStyleSheet("background: white; border-radius: 2px; color: black;")
        self.Data_nascimento_input.setMaximumWidth(230)
        self.Data_nascimento_input.setMinimumWidth(230)

        self.verticalData_nascimento_Layout.addWidget(self.Data_nascimento_label)
        self.verticalData_nascimento_Layout.addWidget(self.Data_nascimento_input)


        self.horizontalLayout_2.addWidget(self.Data_nascimento)

        


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_3 = QFrame(self.dlg)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        
        

        self.email = QFrame(self.frame_3)
        self.email.setObjectName(u"email")
        self.email.setFrameShape(QFrame.StyledPanel)
        self.email.setFrameShadow(QFrame.Raised)

        self.verticalEmail_Layout    = QVBoxLayout(self.email)
        self.Email_label = QLabel("Email")
        self.Email_input = QLineEdit()
        self.Email_input.setStyleSheet("background: white; border-radius: 2px; color: black;")

        self.verticalEmail_Layout.addWidget(self.Email_label)
        self.verticalEmail_Layout.addWidget(self.Email_input)

        self.horizontalLayout_3.addWidget(self.email)

        self.Telefone = QFrame(self.frame_3)
        self.Telefone.setObjectName(u"Telefone")
        self.Telefone.setFrameShape(QFrame.StyledPanel)
        self.Telefone.setFrameShadow(QFrame.Raised)

        self.verticalTelefone_Layout    = QVBoxLayout(self.Telefone)
        self.Telefone_label = QLabel("Telefone")
        self.Telefone_input = QLineEdit()
        self.Telefone_input.setStyleSheet("background: white; border-radius: 2px; color: black;")

        self.verticalTelefone_Layout.addWidget(self.Telefone_label)
        self.verticalTelefone_Layout.addWidget(self.Telefone_input)
        

        self.horizontalLayout_3.addWidget(self.Telefone)

        
        self.verticalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.dlg)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.funcao         = QFrame(self.frame_2)
        #self.funcao.setFrameShadow(QFrame.StyledPanel)
        #self.funcao.setFrameShadow(QFrame.Raised)
        
        self.vertical_funcao    = QVBoxLayout(self.funcao)
        self.funcao_label       = QLabel("Função")
        self.funcao_input       = QComboBox()
        
        self.funcao_input.setStyleSheet("selection-background-color: transparent")

        self.vertical_funcao.addWidget(self.funcao_label)
        self.vertical_funcao.addWidget(self.funcao_input)

        self.horizontalLayout_4.addWidget(self.funcao)

        self.Horas_Trab_Dia = QFrame(self.frame_2)
        self.Horas_Trab_Dia.setObjectName(u"Horas_Trab_Dia")
        self.Horas_Trab_Dia.setFrameShape(QFrame.StyledPanel)
        self.Horas_Trab_Dia.setFrameShadow(QFrame.Raised)

        self.verticalHoras_Trab_Dia_Layout    = QVBoxLayout(self.Horas_Trab_Dia)
        self.Horas_Trab_Dia_label = QLabel("Horas_Trab_Dia")
        self.Horas_Trab_Dia_input = QTimeEdit()
        
        self.Horas_Trab_Dia_input.setStyleSheet("background: white; border-radius: 2px; color: black;")

        self.verticalHoras_Trab_Dia_Layout.addWidget(self.Horas_Trab_Dia_label)
        self.verticalHoras_Trab_Dia_Layout.addWidget(self.Horas_Trab_Dia_input)

        self.horizontalLayout_4.addWidget(self.Horas_Trab_Dia)

        self.Salario_Hora = QFrame(self.frame_2)
        self.Salario_Hora.setObjectName(u"Salario_Hora")
        self.Salario_Hora.setFrameShape(QFrame.StyledPanel)
        self.Salario_Hora.setFrameShadow(QFrame.Raised)
        self.verticalSalario_Layout    = QVBoxLayout(self.Salario_Hora)
        self.salario_label = QLabel("Salario por Hora")
        self.salario_input = QLineEdit()
        self.salario_input.setStyleSheet("background: white; border-radius: 2px; color: black;")

        self.verticalSalario_Layout.addWidget(self.salario_label)
        self.verticalSalario_Layout.addWidget(self.salario_input)

        self.horizontalLayout_4.addWidget(self.Salario_Hora)


        self.verticalLayout.addWidget(self.frame_2)

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
        self.dialog.name_input.setText(data[0][1])
        self.dialog.cpf_input.setText(data[0][2])
        self.dialog.RG_input.setText(data[0][3])
        self.dialog.salario_input.setText(str(data[0][4]))
        self.dialog.Data_nascimento_input.setDate(QDate(data[0][5]))
        self.dialog.Email_input.setText(data[0][6])
        self.dialog.Telefone_input.setText(data[0][7])
        str_to_time = datetime.strptime(str(data[0][8]), "%H:%M:%S")
        self.dialog.Horas_Trab_Dia_input.setTime(QTime(
            int(str_to_time.strftime("%H")),
            int(str_to_time.strftime("%M")),
            int(str_to_time.strftime("%S")),
        ))
                
        #self.dialog.name_label.setText
        