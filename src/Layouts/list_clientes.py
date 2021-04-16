from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow, QFrame, QSizePolicy, QCheckBox)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic, QtCore
import sys



class Clientes_List(QScrollArea):

    def __init__(self, lists=None):
        super(Clientes_List, self).__init__()
        self.setStyleSheet("""
            QScrollBar:vertical{
                background: white;


            }

            QScrollBar::handle:vertical  {
                background: #A3A3A3;
            }

            QScrollBar::add-line:vertical{
                height: 0px;
            }

            QScrollBar::sub-line:vertical{
                height: 0px;
            }""")

        
        widget = QWidget()
        widget.setStyleSheet("margin-top: 10px;")
        layout = QVBoxLayout(widget)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        if(lists == False or lists == [] or lists == None):
            pass
        else:
        
            
            self.title_frame    = QFrame(widget)
            self.title_frame.setMaximumSize(QSize(900, 65))
            self.title_frame.setMinimumSize(QSize(900, 65))
            self.title_frame.setStyleSheet("border: 2px solid; color: #D6D6D6; background: rgb(30, 30, 30)")
            self.horizontal_layout_2    = QHBoxLayout(self.title_frame)
            ##############################ID_TITLE######################################################
            self.frame_id_title         = QFrame()
            self.frame_id_title.setStyleSheet("border: 0; border-right: 1px solid;")
            self.frame_id_title.setFixedWidth(self.title_frame.width() / 10)

            self.label_id_title         = QLabel(self.frame_id_title)
            self.label_id_title.setFixedWidth(self.frame_id_title.width())
            self.label_id_title.setStyleSheet(
                    "font-size: 17px;"
                    "color: #C2C2C2;"
                    )
            self.label_id_title.setAlignment(QtCore.Qt.AlignCenter)
            self.label_id_title.setText("ID")
            ##############################CNPJ_TITLE######################################################
            self.frame_cnpj_title       = QFrame()
            self.frame_cnpj_title.setStyleSheet("border: 0; border-right: 1px solid;")
            self.frame_cnpj_title.setFixedWidth(self.title_frame.width() / 4)

            self.label_cnpj_title         = QLabel(self.frame_cnpj_title)
            self.label_cnpj_title.setFixedWidth(self.frame_cnpj_title.width())
            self.label_cnpj_title.setStyleSheet(
                    "font-size: 17px;"
                    "color: #C2C2C2;"
                    )
            self.label_cnpj_title.setAlignment(QtCore.Qt.AlignCenter)
            self.label_cnpj_title.setText("CNPJ")
            ##############################NOME_TITLE######################################################
            self.frame_nome_title       = QFrame()
            self.frame_nome_title.setStyleSheet("border: 0; border-right: 0;")
            self.frame_nome_title.setFixedWidth(500)
            self.label_nome_title         = QLabel(self.frame_nome_title)
            self.label_nome_title.setFixedWidth(self.frame_nome_title.width())
            self.label_nome_title.setStyleSheet(
                    "font-size: 17px;"
                    "color: #C2C2C2;"
                    )
            self.label_nome_title.setAlignment(QtCore.Qt.AlignCenter)
            self.label_nome_title.setText("NOME DA EMPRESA")
            ########################################################################################

            self.horizontal_layout_2.addWidget(self.frame_id_title)
            self.horizontal_layout_2.addWidget(self.frame_cnpj_title)
            self.horizontal_layout_2.addWidget(self.frame_nome_title)
            
            layout.addWidget(self.title_frame)
            #layout.setSpacing(0)
            #layout.setContentsMargins(0, 0, 0, 0)
            cont    = 0
            self.horizontal         = QHBoxLayout()
            for i in lists:
                self.frame_content  = QFrame(widget)
                self.frame_content.setMinimumSize(QSize(1000, 75))
                self.frame_content.setStyleSheet("border: 2px solid; color: #D6D6D6")
                #####################################ID###################################
                self.frame_id   = QFrame()
                self.frame_id.setFixedWidth(self.frame_id_title.width() + 10)
                self.frame_id.setStyleSheet("border: 0; border-right: 1px solid;")
                self.label_id         = QLabel(self.frame_id)
                self.label_id.setFixedWidth(self.frame_id.width())
                self.label_id.setStyleSheet(
                        "font-size: 17px;"
                        "color: #C2C2C2;"
                        )
                self.label_id.setAlignment(QtCore.Qt.AlignCenter)
                self.label_id.setText(str(i[0]))
                #####################################CNPJ###################################
                self.frame_cnpj   = QFrame()
                self.frame_cnpj.setFixedWidth(self.frame_cnpj_title.width() + 12)
                self.frame_cnpj.setStyleSheet("border: 0; border-right: 1px solid;")
                self.label_cnpj         = QLabel(self.frame_cnpj)
                self.label_cnpj.setFixedWidth(self.frame_cnpj.width())
                self.label_cnpj.setStyleSheet(
                        "font-size: 17px;"
                        "color: #C2C2C2;"
                        )
                self.label_cnpj.setAlignment(QtCore.Qt.AlignCenter)
                self.label_cnpj.setText(str(i[1]))
                #####################################NOME###################################
                self.frame_nome   = QFrame()
                self.frame_nome.setFixedWidth(self.frame_nome_title.width() + 40)
                self.frame_nome.setStyleSheet("border: 0; border-right: 1px solid;")
                self.label_nome         = QLabel(self.frame_nome)
                self.label_nome.setFixedWidth(self.frame_nome.width())
                self.label_nome.setStyleSheet(
                        "font-size: 17px;"
                        "color: #C2C2C2;"
                        )
                self.label_nome.setAlignment(QtCore.Qt.AlignCenter)
                self.label_nome.setText(str(i[2]))
                ############################################################################
                self.check_frame        = QFrame(self.frame_content)
                self.check_frame.setStyleSheet("border: 0;")    

                

                self.check_box_value    = {}
                self.check_box          = QCheckBox(str(i[0]), self.check_frame)
                self.check_box.setStyleSheet("color: transparent;margin-left: 35px;margin-top: 15px;")
                self.check_box.setChecked(Qt.Unchecked)
                
                self.horizontal.addWidget(self.check_box)
                self.horizontal_layout  = QHBoxLayout(self.frame_content)

                

                self.horizontal_layout.addWidget(self.frame_id)
                self.horizontal_layout.addWidget(self.frame_cnpj)
                self.horizontal_layout.addWidget(self.frame_nome)
                
                self.horizontal_layout.addWidget(self.check_frame)
                layout.addWidget(self.frame_content)

        self.setWidget(widget)
        
    def check_box_func(self):
        
        checked_list = []

        for i in range(self.horizontal.count()):
            chBox = self.horizontal.itemAt(i).widget()
            if chBox.isChecked():
                checked_list.append(chBox.text())
        
        #self.setWidgetResizable(True)
        
        return list(checked_list)

    def uncheck_box_func(self):

        checked_list    = []

        for i in range(self.horizontal.count()):
            chBox   = self.horizontal.itemAt(i).widget()
            if(chBox.isChecked()):
                pass
            else:
                checked_list.append(chBox.text())
        
        return list(checked_list)

'''app = QApplication(sys.argv)
window = Clientes_List()
sys.exit(window.exec_())'''