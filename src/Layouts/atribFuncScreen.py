from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow, QFrame, QSizePolicy, QCheckBox, QDateEdit, QDialog, QMessageBox)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic, QtCore
import sys
from src.DB_Connect.SQL import DB_Login, SQL_Funcionario
#from Layouts.loading_screen import LoadignScreen

class Atrib_Func_Screen(QScrollArea):

    def __init__(self, edited=None, id_obra=None):
        super(Atrib_Func_Screen, self).__init__()
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
            }
            QScrollBar:horizontal{
                background: white;

            }

            QScrollBar::handle:horizontal  {
                background: #A3A3A3;
            }

            QScrollBar::add-line:horizontal{
                height: 0px;
            }

            QScrollBar::sub-line:horizontal{
                height: 0px;
            }""")

        self.return_data    = None
        lists       = SQL_Funcionario().return_all_funcs()
        if(lists    == False):
            message = QMessageBox()
            message.setIcon(QMessageBox.Critical)
            message.setText("É necessário cadastrar um funcionário primeiro!")
            message.setWindowTitle("ERROR")
            QApplication.restoreOverrideCursor()
            message.exec_()
            self.return_data    = False
        else:
            widget = QWidget()
            widget.setStyleSheet("margin-top: 10px;")
            layout = QVBoxLayout(widget)
            layout.setSpacing(0)
            layout.setContentsMargins(0, 0, 0, 0)
            
            self.sql            = DB_Login()
            self.title_frame    = QFrame(widget)
            self.title_frame.setMaximumSize(QSize(500, 65))
            self.title_frame.setMinimumSize(QSize(500, 65))
            self.title_frame.setStyleSheet("color: #D6D6D6; background: rgb(30, 30, 30)")
            
            self.title_id_frame     = QFrame()
            self.title_id_frame.setFixedWidth(50)
            self.label_id_title     = QLabel(self.title_id_frame)
            self.label_id_title.setText("ID")
            self.title_nome_frame   = QFrame()
            self.title_nome_frame.setFixedWidth(100)
            self.label_nome_title     = QLabel(self.title_nome_frame)
            self.label_nome_title.setText("NOME")
            self.title_adc_frame    = QFrame()
            self.label_adc_title    = QLabel(self.title_adc_frame)
            self.label_adc_title.setText("ADICIONAR")
            self.title_rem_frame    = QFrame()
            self.label_rem_title    = QLabel(self.title_rem_frame)
            self.label_rem_title.setText("REMOVER")

            self.horizontal_layout_2    = QHBoxLayout(self.title_frame)
            self.horizontal_layout_2.addWidget(self.title_id_frame)
            
            self.horizontal_layout_2.addWidget(self.title_nome_frame)
            self.horizontal_layout_2.addWidget(self.title_adc_frame)
            
            
            self.funcs_atribuidos        = False
            if(edited != None):
                self.funcs_atribuidos   = SQL_Funcionario().funcs_atribuidos(id_obra)
                self.descricao          = self.funcs_atribuidos['Descricao_Obra']            
                self.funcs              = self.funcs_atribuidos['Funcionarios']
                self.horizontal_layout_2.addWidget(self.title_rem_frame)
                
            
            
            cont    = 0
            layout.addWidget(self.title_frame)
            self.horizontal         = QHBoxLayout()
            for i in lists:
                self.frame_content  = QFrame(widget)
                self.frame_content.setMinimumSize(QSize(500, 75))
                #self.frame_content.setStyleSheet("border: 2px solid; color: #D6D6D6")

                self.frame_id       = QFrame()
                self.frame_id.setFixedWidth(50)
                #self.frame_id.setStyleSheet("border: 0; border-right: 1px solid;")

                self.label_id     = QLabel(self.frame_id)
                #self.label_id.setFixedWidth(self.frame_id.width())
                #self.label_id.setAlignment(QtCore.Qt.AlignCenter)
                self.label_id.setText(str(i[0]))
                ###########################################################################
                self.frame_nome     = QFrame()
                #self.frame_nome.setStyleSheet("border: 0; border-right: 1px solid;")
                self.frame_nome.setFixedWidth(100)

                self.label_nome     = QLabel(self.frame_nome)
                #self.label_nome.setFixedWidth(100*2)
                #self.label_nome.setAlignment(QtCore.Qt.AlignCenter)
                self.label_nome.setText(str(i[1]))
                ###########################################################################
                self.frame_add      = QFrame()
                #self.frame_add.setStyleSheet("border: 0; border-right: 1px solid;")
                #self.frame_add.setFixedWidth(50)

                self.check_box      = QCheckBox(str(i[0]), self.frame_add)
                self.check_box.setChecked(Qt.Unchecked)
                self.check_box.setStyleSheet("color: transparent;margin-left: 35px;margin-top: 15px;border: 0;")
                ###########################################################################
                self.frame_remove   = QFrame()
                self.labeL_remove   = QLabel(self.frame_remove)
                
                #self.frame_remove.setStyleSheet("border: 0; border-right: 1px solid;")
                #self.frame_remove.setFixedWidth(50)

                self.check_box_2      = QCheckBox(str(i[0])+"del", self.frame_remove)
                self.check_box_2.setChecked(Qt.Unchecked)
                self.check_box_2.setStyleSheet("color: transparent;margin-left: 35px;margin-top: 15px;border: 0")

                self.horizontal_layout  = QHBoxLayout(self.frame_content)
                self.horizontal_layout.addWidget(self.frame_id)
                self.horizontal_layout.addWidget(self.frame_nome)
                self.horizontal_layout.addWidget(self.frame_add)

                self.horizontal.addWidget(self.check_box)
                if(self.funcs_atribuidos == False):
                    pass
                else:
                    
                    self.horizontal_layout.addWidget(self.frame_remove)
                    self.horizontal.addWidget(self.check_box_2)
                    for x in self.funcs_atribuidos['Funcionarios']:
                        if(i[0] == x[0]):
                            self.check_box.setEnabled(False)
                            self.check_box_2.setEnabled(True)
                        else:
                            self.check_box_2.setEnabled(False)
                            self.check_box.setEnabled(True)
                
                layout.addWidget(self.frame_content)

                '''self.frame_id           = QFrame()
                self.frame_id.setFixedWidth(self.title_id.width() + 50)
                self.frame_id.setStyleSheet("border: 0; border-right: 1px solid;")
                self.id_label           = QLabel(self.frame_id)
                self.id_label.setFixedWidth(self.title_id.width())
                self.id_label.setStyleSheet("""
                
                margin-top: 10px;
                font-size: 17px;
                color: #C2C2C2;
                border-right: 0""")
                self.id_label.setText(str(i.ID))
                self.frame_name         = QFrame()
                
                self.frame_name.setFixedWidth(self.title_user.width() + 50)
                self.frame_name.setStyleSheet("border: 0; border-right: 1px solid;")

                self.name_label         = QLabel(self.frame_name)
                self.name_label.setFixedWidth(self.frame_name.width())
                self.name_label.setAlignment(Qt.AlignCenter)

                self.name_label.setStyleSheet("""
                margin-top: 10px;
                font-size: 14px;
                color: #C2C2C2;
                border-right: 0""")
                self.name_label.setText(str(i.NOME))

                self.check_frame        = QFrame()
                
                
                self.check_frame.setStyleSheet("border: 0;")    
                

                

                self.check_box_value    = {}

                self.check_box          = QCheckBox(str(i.ID), self.check_frame)
                self.check_box.setChecked(Qt.Unchecked)
            
                
                self.check_box.setStyleSheet("color: transparent;margin-left: 35px;margin-top: 15px;")
                

                if(self.funcs_atribuidos == False):
                    pass
                else:

                    self.check_frame_2      = QFrame(self.frame_content)
                    self.check_frame_2.setStyleSheet("border: 0;")    
                    self.check_box_2        = QCheckBox(str(i.ID)+"del", self.check_frame_2)
                    self.check_box_2.setChecked(Qt.Unchecked)
                    self.check_box_2.setStyleSheet("color: transparent;margin-left: 35px;margin-top: 15px;")
                    for x in self.funcs_atribuidos['Funcionarios']:
                        if(i.ID == x[0]):
                            self.check_box.setEnabled(False)
                        else:
                            self.check_box_2.setEnabled(False)
                    
                
                self.horizontal.addWidget(self.check_box)
                
                
                self.horizontal_layout  = QHBoxLayout(self.frame_content)

                self.horizontal_layout.addWidget(self.frame_id)
                self.horizontal_layout.addWidget(self.frame_name)
                
                self.horizontal_layout.addWidget(self.check_frame)
                if(edited != None):
                    self.horizontal.addWidget(self.check_box_2)
                    self.horizontal_layout.addWidget(self.check_frame_2)'''
                
            
            
            self.setWidget(widget)
        #self.showMaximized()
        
        
    def check_box_func(self):
        
        checked_list = []

        for i in range(self.horizontal.count()):
            chBox = self.horizontal.itemAt(i).widget()
            if chBox.isChecked():
                checked_list.append(chBox.text())
        
        #self.setWidgetResizable(True)
        print(checked_list)
        return list(checked_list)
    
class Atrib_Func_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.screen_Func    = Atrib_Func_Screen()
        self.dialog         = QDialog()
        self.dialog.setStyleSheet("background: rgb(45, 45, 45);")
        self.verticalLayout = QVBoxLayout(self.dialog)

        self.verticalLayout.addWidget(self.screen_Func)
        self.dialog.showMaximized()

