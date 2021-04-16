from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *    
from Layouts.frame import Frame
from DB_Connect.SQL import DB_Alter
import threading
    
class FrameBox(object):
    def frame_box(self, user, name, passw, ID, refresh):
        self.id         = ID
        self.name       = name
        self.user       = user
        self.refresh    = refresh
        self.password   = passw
        self.plain_passw    = passw
        self.sql  = DB_Alter()
        self.dlg = QDialog()
        self.dlg.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.dlg.setWindowTitle("Cadastro de Usuário")
        self.dlg.setStyleSheet(u"background-color: rgb(201, 198, 177); ")
        
        self.dlg.setMaximumSize(QSize(500, 500))
        self.dlg.setMinimumSize(QSize(500, 500))
        self.dlg_frame  = QFrame(self.dlg)
        self.dlg_frame.setStyleSheet("background: rgb(40, 40, 40)")

        self.horizontalLayout_5 = QHBoxLayout(self.dlg)
        self.horizontalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.addWidget(self.dlg_frame)

        self.frame_1    = QFrame(self.dlg_frame)
        

        
        self.frame_2    = QFrame(self.dlg_frame)
        
        self.frame_3    = QFrame(self.dlg_frame)
        self.frame_4    = QFrame(self.dlg_frame)
        self.error_frame    = QFrame(self.frame_4)
        
        self.verticalLayout_11  = QVBoxLayout(self.frame_4)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_11.addWidget(self.error_frame)
        

        self.verticalLayout_9   = QVBoxLayout(self.dlg_frame)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)

        self.verticalLayout_9.addWidget(self.frame_1)
        self.verticalLayout_9.addWidget(self.frame_2)
        self.verticalLayout_9.addWidget(self.frame_3)
        self.verticalLayout_9.addWidget(self.frame_4)

        self.frame_1_cadastro_fFrame    = QFrame(self.frame_1)
        self.first_frame_label          = QFrame(self.frame_1_cadastro_fFrame)
        self.second_frame_label        = QFrame(self.frame_1_cadastro_fFrame)

        self.horizontalLayout_6         = QHBoxLayout(self.frame_1_cadastro_fFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.addWidget(self.first_frame_label)
        self.horizontalLayout_6.addWidget(self.second_frame_label)

        self.label_3    = QLabel(self.first_frame_label)
        self.label_3.setText("Usuário")
        self.label_3.setStyleSheet("""
        margin-left: 10px; 
        margin-top: 10px;
        font-size: 17px;
        color: rgb(201, 198, 177);""")

        self.label_4    = QLabel(self.second_frame_label)
        self.label_4.setText("Nome Completo")
        self.label_4.setStyleSheet("""
        margin-left: 8px; 
        margin-top: 10px;
        font-size: 17px;
        color: rgb(201, 198, 177);""")
        
        self.frame_1_cadastro_fFrame.setMaximumHeight(40)
    
        self.frame_2_cadastro_fFrame    = QFrame(self.frame_1)
        

        self.frame_input_1  = QFrame(self.frame_2_cadastro_fFrame)
        self.input_user     = QLineEdit(self.frame_input_1)
        self.input_user.setText(user)
        self.input_user.setStyleSheet("background-color: white; margin-left: 12px; margin-top: 10px;border-radius: 2px;")
        self.input_user.setMinimumSize(QSize(230, 38))
        self.input_user.textChanged.connect(self.handle_user)
        self.frame_input_2  = QFrame(self.frame_2_cadastro_fFrame)
        self.input_name     = QLineEdit(self.frame_input_2)
        self.input_name.setText(name)
        self.input_name.setStyleSheet("background-color: white; margin-left: 12px; margin-top: 10px;border-radius: 2px;")
        self.input_name.setMinimumSize(QSize(230, 38))
        self.input_name.textChanged.connect(self.handle_name)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2_cadastro_fFrame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_7.addWidget(self.frame_input_1)
        self.horizontalLayout_7.addWidget(self.frame_input_2)

        self.verticalLayout_10  = QVBoxLayout(self.frame_1)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)

        self.verticalLayout_10.addWidget(self.frame_1_cadastro_fFrame)
        self.verticalLayout_10.addWidget(self.frame_2_cadastro_fFrame)
        
        self.frame_second_content_1    = Frame()
        self.frame_second_content_1.verticalFrame(self.frame_2)
        self.frame_second_content_1.frame_1.setMaximumHeight(40)
        

        self.horizontal_frame = Frame()
        self.horizontal_frame.horizontalFrame(self.frame_second_content_1.frame_1)
        self.label_password = QLabel(self.horizontal_frame.horizontal_frame_1)
        self.label_password.setText("Senha")
        self.label_password.setStyleSheet("""
        margin-left: 10px; 
        margin-top: 10px;
        font-size: 17px;
        color: #D6D6D6;""")
        
        self.label_permissao    = QLabel(self.horizontal_frame.horizontal_frame_2)
        self.label_permissao.setText("Permissão Como:")
        self.label_permissao.setStyleSheet("""
        margin-left: 10px; 
        margin-top: 10px;
        font-size: 17px;
        color: rgb(201, 198, 177);""")

        self.horizontal_frame.horizontalFrame(self.frame_second_content_1.frame_2)

        self.input_password = QLineEdit(self.horizontal_frame.horizontal_frame_1)
        self.input_password.setStyleSheet("background-color: white; margin-left: 12px; margin-top: 10px;border-radius: 2px;")
        self.input_password.setMinimumSize(QSize(230, 38))
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_password.setText(passw)
        self.input_password.textChanged.connect(self.handle_password)

        self.frame_combo_box    = QFrame(self.horizontal_frame.horizontal_frame_2)
        self.comboBox   = QComboBox(self.frame_combo_box)
        self.frame_combo_box.setStyleSheet("""
        margin-left: 10px; 
        margin-top: 10px;
        font-size: 17px;
        color: rgb(201, 198, 177);""")
        self.comboBox.addItems(['Administrador', 'Gerente', 'Operador'])
        self.comboBox.setStyleSheet("""selection-background-color: transparent""")
        self.comboBox.setMinimumSize(QSize(230, 38))
        #self.comboBox.currentTextChanged.connect(self.handle_permission)
        
        self.frame_button   = QFrame(self.frame_3)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_3)

        self.horizontalLayout_8.addWidget(self.frame_button)
        self.sub_button = QPushButton(self.frame_button)
        self.sub_button.setText("Atualizar dados")
        
        self.sub_button.setStyleSheet("""
        background-color: rgb(201, 198, 177);
        margin-left: 80%;
        font-size: 17px;
        
        """)
        self.sub_button.setCheckable(True)
        self.sub_button.clicked.connect(self.handle_click)
        self.sub_button.setMinimumSize(QSize(360, 30))
        self.sub_button.setCursor(Qt.PointingHandCursor)

        self.dlg.exec_()

    def handle_user(self, text):
        self.user   = text
    
    def handle_name(self, text):
        self.name   = text
    
    def handle_password(self, text):
        self.password   = text
    
    def handle_click(self):

        if(self.plain_passw == self.password):
            hash    = False
        else:
            hash    = True
        self.sql.update(
            self.id,
            self.user,
            self.name, 
            self.password,
            self.comboBox.currentIndex(),
            hash
        )
        self.refresh()
        self.dlg.close()


        