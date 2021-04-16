from PyQt5.QtWidgets import (QWidget, QSlider, QDateEdit, QComboBox, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow, QFrame, QSizePolicy, QCheckBox, QDialog, QTimeEdit)
from PyQt5.QtCore import Qt, QSize, QDate, QTime
from PyQt5 import QtWidgets, uic
import sys
from datetime import datetime

class Window_Form_Despesa(QScrollArea):

    def __init__(self):
        super(Window_Form_Despesa, self).__init__()
        self.dlg = QDialog()
        self.dlg.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.dlg.setWindowTitle("Adição de Título")
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
        self.num_titulo_frame = QFrame(self.frame)
        self.num_titulo_frame.setObjectName(u"num_titulo_frame")
        self.num_titulo_frame.setFrameShape(QFrame.StyledPanel)
        self.num_titulo_frame.setFrameShadow(QFrame.Raised)
        self.vertical_num_titulo_layout    = QVBoxLayout(self.num_titulo_frame)

        self.num_titulo_label = QLabel("Num. Título")
        self.num_titulo_input = QLineEdit()
        self.num_titulo_input.setStyleSheet("background: white; border-radius: 2px; color: black;")

        self.vertical_num_titulo_layout.addWidget(self.num_titulo_label)
        self.vertical_num_titulo_layout.addWidget(self.num_titulo_input)

        self.horizontalLayout.addWidget(self.num_titulo_frame)

        self.descricao_frame = QFrame(self.frame)
        self.descricao_frame.setObjectName(u"CPF")
        self.descricao_frame.setFrameShape(QFrame.StyledPanel)
        self.descricao_frame.setFrameShadow(QFrame.Raised)

        self.vertical_descricao_layout    = QVBoxLayout(self.descricao_frame)

        self.descricao_label = QLabel("Descrição")
        self.descricao_input = QLineEdit()
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

        self.fornecedor_label = QLabel("Fornecedor")
        self.fornecedor_input = QLineEdit()
        self.fornecedor_input.setStyleSheet("background: white; border-radius: 2px; color: black;")

        self.verticalFornecedor.addWidget(self.fornecedor_label)
        self.verticalFornecedor.addWidget(self.fornecedor_input)

        self.horizontalLayout_2.addWidget(self.fornecedor_frame)

        self.valor_frame = QFrame(self.frame_5)
        self.valor_frame.setObjectName(u"valor_frame")
        self.valor_frame.setFrameShape(QFrame.StyledPanel)
        self.valor_frame.setFrameShadow(QFrame.Raised)
        
        self.verticalValor_layout    = QVBoxLayout(self.valor_frame)
        self.valor_label = QLabel("Valor")
        self.valor_input = QLineEdit()
        self.valor_input.setStyleSheet("background: white; border-radius: 2px; color: black;")

        self.verticalValor_layout.addWidget(self.valor_label)
        self.verticalValor_layout.addWidget(self.valor_input)


        self.horizontalLayout_2.addWidget(self.valor_frame)

        


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_3 = QFrame(self.dlg)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        
        

        self.observacao_frame = QFrame(self.frame_3)
        self.observacao_frame.setObjectName(u"email")
        self.observacao_frame.setFrameShape(QFrame.StyledPanel)
        self.observacao_frame.setFrameShadow(QFrame.Raised)

        self.verticalObservacao_layout    = QVBoxLayout(self.observacao_frame)
        self.observacao_label = QLabel("Observação")
        self.observacao_input = QLineEdit()
        self.observacao_input.setStyleSheet("background: white; border-radius: 2px; color: black;")

        self.verticalObservacao_layout.addWidget(self.observacao_label)
        self.verticalObservacao_layout.addWidget(self.observacao_input)

        self.frame_data             = QFrame(self.frame_3)
        self.verticalLayout_data    = QVBoxLayout(self.frame_data)
        self.label_data             = QLabel("Data da Baixa")
        self.input_data             = QDateEdit(calendarPopup=True)
        self.input_data.setStyleSheet("background: white; border-radius: 2px; color: black;")

        self.verticalLayout_data.addWidget(self.label_data)
        self.verticalLayout_data.addWidget(self.input_data)

        self.horizontalLayout_3.addWidget(self.observacao_frame)
        self.horizontalLayout_3.addWidget(self.frame_data)
 
        self.verticalLayout.addWidget(self.frame_3)
        
        self.vincular_obra_frame    = QFrame(self.dlg)
        self.verticalObra_layout    = QHBoxLayout(self.vincular_obra_frame)
        self.vincular_obra_label    = QLabel("Deseja vincular despesa a obras?")
        self.vincular_obra_check_box    = QCheckBox("Sim")
        
        self.verticalObra_layout.addWidget(self.vincular_obra_label)
        self.verticalObra_layout.addWidget(self.vincular_obra_check_box)

        self.verticalLayout.addWidget(self.vincular_obra_frame)
        #self.verticalLayout.addWidget(self.frame_data)
        self.frame_teste    = QFrame(self.dlg)
        
        self.verticalLayout_obras   = QVBoxLayout(self.frame_teste)
        self.verticalLayout.addWidget(self.frame_teste)

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