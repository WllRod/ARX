from PyQt5.QtWidgets import (QWidget, QSlider, QDateEdit, QComboBox, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow, QFrame, QSizePolicy, QCheckBox, QDialog, QTimeEdit)
from PyQt5.QtCore import Qt, QSize, QDate, QTime
from PyQt5 import QtWidgets, uic
import sys
from datetime import datetime

class Folha_Params(QScrollArea):

    def __init__(self):
        super(Folha_Params, self).__init__()
        self.dialog = QDialog()
        self.dialog.setWindowTitle("Folha de Ponto")
        self.dialog.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        
        self.dialog.setStyleSheet(u"""
        background-color: grey; 
        
        font-size: 17px;
        color: rgb(201, 198, 177);""")
        
        
        
        self.dialog.setMinimumSize(QSize(500, 250))
        self.dialog.setMaximumSize(QSize(500, 250))
        frame_1 = QFrame(self.dialog)
        frame_1.setStyleSheet(u"""
        background-color: rgb(40, 40, 40); 
        
        font-size: 17px;
        color: rgb(201, 198, 177);""")
        
        
        self.verticalLayout_back    = QVBoxLayout(self.dialog)
        self.verticalLayout_back.setSpacing(0)
        self.verticalLayout_back.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_back.addWidget(frame_1)
        

        self.verticalLayout = QVBoxLayout(frame_1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(frame_1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setMinimumSize(QSize(500, 50))
        self.frame.setMaximumSize(QSize(500, 50))
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_Label    = QLabel(self.frame)
        self.title_Label.setText("Preencha os parametros")
        self.title_Label.setStyleSheet("margin-top: 15px;")
        self.title_Label.setFixedWidth(500)
        self.title_Label.setAlignment(Qt.AlignCenter)


        self.verticalLayout.addWidget(self.frame)

        self.frame_5 = QFrame(frame_1)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.data_Inicial = QFrame(self.frame_5)
        self.data_Inicial.setObjectName(u"Data Inicial")
        self.data_Inicial.setFrameShape(QFrame.StyledPanel)
        self.data_Inicial.setFrameShadow(QFrame.Raised)
        
        self.verticaldata_Inicial_Layout    = QVBoxLayout(self.data_Inicial)
        self.data_Inicial_label = QLabel("Data Inicial")
        self.data_Inicial_input = QDateEdit(calendarPopup=True)
        self.data_Inicial_input.setStyleSheet("background: white; border-radius: 2px; color: black;")
        self.data_Inicial_input.setMaximumWidth(230)
        self.data_Inicial_input.setMinimumWidth(230)

        self.verticaldata_Inicial_Layout.addWidget(self.data_Inicial_label)
        self.verticaldata_Inicial_Layout.addWidget(self.data_Inicial_input)


        self.horizontalLayout_2.addWidget(self.data_Inicial)
#==========================================================================================
        self.Data_final = QFrame(self.frame_5)
        self.Data_final.setObjectName(u"Data_final")
        self.Data_final.setFrameShape(QFrame.StyledPanel)
        self.Data_final.setFrameShadow(QFrame.Raised)
        
        self.verticalData_final_Layout    = QVBoxLayout(self.Data_final)
        self.Data_final_label = QLabel("Data Final")
        self.Data_final_input = QDateEdit(calendarPopup=True)
        self.Data_final_input.setStyleSheet("background: white; border-radius: 2px; color: black;")
        self.Data_final_input.setMaximumWidth(230)
        self.Data_final_input.setMinimumWidth(230)

        self.verticalData_final_Layout.addWidget(self.Data_final_label)
        self.verticalData_final_Layout.addWidget(self.Data_final_input)


        self.horizontalLayout_2.addWidget(self.Data_final)

        


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_2    = QFrame(frame_1)
        
        #self.frame_2.setStyleSheet("background: red;")
        self.verticalLayout.addWidget(self.frame_2)
       
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.funcao             = QFrame()
        self.read_only          = QFrame()
        self.vertical_read_only = QVBoxLayout(self.read_only)
        self.check_box          = QCheckBox()
        self.vertical_read_only.addWidget(QLabel("Visualizar apenas:"))
        self.vertical_read_only.addWidget(self.check_box)
        
        self.horizontalLayout_3.addWidget(self.funcao)
        self.horizontalLayout_3.addWidget(self.read_only)
        self.verticalFuncao     = QVBoxLayout(self.funcao)

        self.label_1    = QLabel("Escolha a obra:")
        self.label_1.setFixedWidth(1000)
        self.obra_input = QComboBox()
        self.obra_input.setFixedWidth(230)
        self.obra_input.setFixedHeight(30)
        self.verticalFuncao.addWidget(self.label_1)
        self.verticalFuncao.addWidget(self.obra_input)
        

        '''self.frame_3 = QFrame(frame_1)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        
        
        

        self.funcao         = QFrame(self.frame_3)
        self.funcao.setStyleSheet("background: red;")
        #self.funcao.setFrameShadow(QFrame.StyledPanel)
        #self.funcao.setFrameShadow(QFrame.Raised)
        
        self.vertical_funcao    = QVBoxLayout(self.funcao)
        self.funcao_label       = QLabel("Função")
        self.funcao_input       = QComboBox()
        
        self.funcao_input.setStyleSheet("selection-background-color: transparent")

        self.vertical_funcao.addWidget(self.funcao_label)
        self.vertical_funcao.addWidget(self.funcao_input)

        self.verticalLayout.addWidget(self.frame_3)'''

        

        self.frame_4 = QFrame(frame_1)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.layoutButton   = QVBoxLayout(self.frame_4)
        self.sub_button = QPushButton("Gerar tabela")
        
        
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

    
'''
app = QApplication(sys.argv)
window  = Folha_Params()
window.dialog.show()
app.exec_()
'''

