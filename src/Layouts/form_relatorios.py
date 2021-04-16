from PyQt5.QtWidgets import (QWidget, QSlider, QDateEdit, QComboBox, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow, QFrame, QSizePolicy, QCheckBox, QDialog, QTimeEdit, QFileDialog)
from PyQt5.QtCore import Qt, QSize, QDate, QTime
from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore
import sys
from datetime import datetime

class Window_Form_Relatorio(QScrollArea):

    def __init__(self):
        super(Window_Form_Relatorio, self).__init__()
        self.dlg = QDialog()
        self.dlg.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.dlg.setWindowTitle("Relatórios")
        self.dlg.setStyleSheet(u"""
        background-color: rgb(40, 40, 40); 
        
        font-size: 17px;
        color: rgb(201, 198, 177);""")
        
        
        
        self.dlg.setMinimumSize(QSize(500, 200))

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
        self.num_titulo_frame = QFrame(self.frame)
        self.num_titulo_frame.setObjectName(u"num_titulo_frame")
        self.num_titulo_frame.setFrameShape(QFrame.StyledPanel)
        self.num_titulo_frame.setFrameShadow(QFrame.Raised)
        self.vertical_num_titulo_layout    = QVBoxLayout(self.num_titulo_frame)

        self.num_titulo_label = QLabel("Período Inicial")
        self.num_titulo_input = QDateEdit(calendarPopup=True)
        self.num_titulo_input.setStyleSheet("background: white; border-radius: 2px; color: black;")

        self.vertical_num_titulo_layout.addWidget(self.num_titulo_label)
        self.vertical_num_titulo_layout.addWidget(self.num_titulo_input)

        self.horizontalLayout.addWidget(self.num_titulo_frame)

        self.descricao_frame = QFrame(self.frame)
        self.descricao_frame.setObjectName(u"CPF")
        self.descricao_frame.setFrameShape(QFrame.StyledPanel)
        self.descricao_frame.setFrameShadow(QFrame.Raised)

        self.vertical_descricao_layout    = QVBoxLayout(self.descricao_frame)

        self.descricao_label = QLabel("Período Final")
        self.descricao_input = QDateEdit(calendarPopup=True)
        self.descricao_input.setStyleSheet("background: white; border-radius: 2px; color: black;")

        self.vertical_descricao_layout.addWidget(self.descricao_label)
        self.vertical_descricao_layout.addWidget(self.descricao_input)


        self.horizontalLayout.addWidget(self.descricao_frame)


        self.verticalLayout.addWidget(self.frame)

        self.frame_5 = QFrame(self.dlg)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fornecedor_frame = QFrame(self.frame_5)
        self.fornecedor_frame.setObjectName(u"Telefone")
        self.fornecedor_frame.setFrameShape(QFrame.StyledPanel)
        self.fornecedor_frame.setFrameShadow(QFrame.Raised)

        self.verticalFornecedor    = QVBoxLayout(self.fornecedor_frame)

        self.fornecedor_label = QLabel("Tipo de Relatório")
        self.fornecedor_input = QComboBox()
        self.fornecedor_input.addItems(['Folha de Ponto', 'Despesas', 'Folha de Ponto Detalhado'])
        self.fornecedor_input.setStyleSheet("background: white; border-radius: 2px; color: black;")

        self.verticalFornecedor.addWidget(self.fornecedor_label)
        self.verticalFornecedor.addWidget(self.fornecedor_input)

        self.horizontalLayout_2.addWidget(self.fornecedor_frame)



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
        #self.sub_button.clicked.connect(self.openfile_screen)
        self.sub_button.setCursor(Qt.PointingHandCursor)
        self.layoutButton.addWidget(self.sub_button, alignment=Qt.AlignCenter)

        self.verticalLayout.addWidget(self.frame_4)

    def openfile_screen(self):
        dialog = QFileDialog()
        dialog.setFilter(dialog.filter() | QtCore.QDir.Hidden)
        dialog.setDefaultSuffix('json')
        dialog.setAcceptMode(QFileDialog.AcceptSave)
        dialog.setNameFilters(['JSON (*.json)'])
        if dialog.exec_() == QDialog.Accepted:
            print(dialog.selectedFiles())
        else:
            print('Cancelled')
        
class Edit_Func(QScrollArea):
    def __init__(self, data):
        self.dialog = Window_Add_Func()
        self.dialog.num_titulo_input.setText(data[0][1])
        self.dialog.descricao_input.setText(data[0][2])
        self.dialog.fornecedor_input.setText(data[0][3])
        self.dialog.salario_input.setText(str(data[0][4]))
        self.dialog.email_inpit.setDate(QDate(data[0][5]))
        self.dialog.observacao_input.setText(data[0][6])
        self.dialog.Telefone_input.setText(data[0][7])
        str_to_time = datetime.strptime(str(data[0][8]), "%H:%M:%S")
        self.dialog.Horas_Trab_Dia_input.setTime(QTime(
            int(str_to_time.strftime("%H")),
            int(str_to_time.strftime("%M")),
            int(str_to_time.strftime("%S")),
        ))
                
        #self.dialog.num_titulo_label.setText

'''app = QApplication(sys.argv)
window  = Window_Form_Despesa()
sys.exit(window.dlg.exec_())'''