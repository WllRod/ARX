from PyQt5.QtWidgets import (QWidget, QSlider, QDateEdit, QComboBox, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow, QFrame, QSizePolicy, QCheckBox, QDialog, QTimeEdit)
from PyQt5.QtCore import Qt, QSize, QDate, QTime
from PyQt5 import QtWidgets, uic
import sys
from datetime import datetime

class Add_Obra(QScrollArea):

    def __init__(self):
        super(Add_Obra, self).__init__()
        self.dlg = QDialog()
        self.dlg.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.dlg.setWindowFlag(Qt.WindowStaysOnTopHint)

        #self.dlg.setWindowTitle("Cadastro de Cargo")
        self.dlg.setStyleSheet(u"""
        background-color: rgb(40, 40, 40); 
        
        font-size: 17px;
        color: rgb(201, 198, 177);""")
        
        
        
        self.dlg.setMinimumSize(QSize(250, 350))
        self.dlg.setWindowTitle("Obras")

        self.verticalLayout = QVBoxLayout(self.dlg)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.dlg)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Name_Frame = QFrame(self.frame)
        self.Name_Frame.setObjectName(u"Name_Frame")
        self.Name_Frame.setFrameShape(QFrame.StyledPanel)
        self.Name_Frame.setFrameShadow(QFrame.Raised)
        self.verticalName_Layout    = QVBoxLayout(self.Name_Frame)

        self.name_label = QLabel("Descrição")
        self.name_input = QLineEdit()
        self.name_input.setStyleSheet("background: white; border-radius: 2px; color: black;")
        self.name_input.setText("")
        self.verticalName_Layout.addWidget(self.name_label)
        self.verticalName_Layout.addWidget(self.name_input)

        self.verticalLayout.addWidget(self.Name_Frame)

        self.cliente_frame  = QFrame(self.frame)
        self.verticalCliente_frame  = QVBoxLayout(self.cliente_frame)

        self.label_cliente  = QLabel("Cliente")
        self.input_cliente  = QComboBox()
        self.input_cliente.setStyleSheet("background: white; border-radius: 2px; color: black;")
        self.verticalCliente_frame.addWidget(self.label_cliente)
        self.verticalCliente_frame.addWidget(self.input_cliente)

        self.verticalLayout.addWidget(self.cliente_frame)

        ######################################################################
        self.data_frame  = QFrame(self.frame)
        self.verticaldata_frame  = QVBoxLayout(self.data_frame)

        self.label_data  = QLabel("Data de Conclusão")
        self.input_data  = QDateEdit(calendarPopup=True)
        self.input_data.setStyleSheet("background: white; border-radius: 2px; color: black;")
        self.verticaldata_frame.addWidget(self.label_data)
        self.verticaldata_frame.addWidget(self.input_data)

        self.verticalLayout.addWidget(self.data_frame)
        self.frame_5    = QFrame(self.dlg)
        self.label_funcionarios = QLabel("Vincular Funcionários")
        self.label_funcionarios.setStyleSheet("margin-left: 4px;")
        
        self.verticalLayout_frame_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout.addWidget(self.label_funcionarios)
        self.verticalLayout.addWidget(self.frame_5)
        
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
        
'''app = QApplication(sys.argv)
window  = Add_Obra()
sys.exit(window.dlg.exec_())'''