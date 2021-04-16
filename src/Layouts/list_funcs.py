from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow, QFrame, QSizePolicy, QCheckBox)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic
import sys

#from Layouts.loading_screen import LoadignScreen

class Func_Window(QScrollArea):

    def __init__(self, lists):
        super(Func_Window, self).__init__()
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

        if(lists == [] or lists == False):
            pass
        else:
        
            self.title_frame    = QFrame(widget)
            self.title_frame.setMaximumSize(QSize(900, 65))
            self.title_frame.setMinimumSize(QSize(900, 65))
            self.title_frame.setStyleSheet("border: 2px solid; color: #D6D6D6; background: rgb(30, 30, 30)")
            

            self.title_id               = QFrame(self.title_frame)
            self.title_id.setStyleSheet("border: 0; border-right: 1px solid;")
            self.title_id.setMaximumWidth(50)
            self.label_title_id         = QLabel(self.title_id)
            self.label_title_id.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.label_title_id.setAlignment(Qt.AlignCenter)
            self.label_title_id.setStyleSheet("""
                margin-left: 10px; 
                font-size: 17px;
                color: #C2C2C2;
                border-right: 0
            """)
            self.label_title_id.setText("ID")
            self.title_user             = QFrame(self.title_frame)
            self.title_user.setMinimumWidth(200)
            self.title_user.setStyleSheet("border: 0; border-right: 1px solid;")
            
            self.label_title_user       = QLabel(self.title_user)
            self.label_title_user.setFixedWidth(200)
            self.label_title_user.setAlignment(Qt.AlignCenter)
            
            self.label_title_user.setStyleSheet("""
                margin-left: 0;
                font-size: 17px;
                color: #C2C2C2;
                border-right: 0;
                
            """)
            self.label_title_user.setText("Nome")

            self.title_name             = QFrame(self.title_frame)
            self.title_name.setMinimumWidth(400)
            self.title_name.setStyleSheet("border: 0; border-right: 1px solid;")
            
            self.label_title_name       = QLabel(self.title_name)
            self.label_title_name.setFixedWidth(399)
            self.label_title_name.setAlignment(Qt.AlignCenter)
            
            self.label_title_name.setAlignment(Qt.AlignCenter)
            self.label_title_name.setStyleSheet("""
                margin-left: 0;
                font-size: 17px;
                color: #C2C2C2;
                border-right: 0;
                
            """)
            self.label_title_name.setText("CPF")
            self.title_permission       = QFrame(self.title_frame)

            self.title_permission.setStyleSheet("border: 0;")
            
            self.label_title_permission = QLabel(self.title_permission)
            self.label_title_permission.setFixedWidth(200)
            self.label_title_permission.setAlignment(Qt.AlignCenter)
            
            self.label_title_permission.setStyleSheet("""
                font-size: 17px;
                color: #C2C2C2;
                border-right: 0
            """)
            self.label_title_permission.setText("RG")
            self.horizontal_layout_2    = QHBoxLayout(self.title_frame)

            self.horizontal_layout_2.addWidget(self.title_id)
            self.horizontal_layout_2.addWidget(self.title_user)
            self.horizontal_layout_2.addWidget(self.title_name)
            self.horizontal_layout_2.addWidget(self.title_permission)
            layout.addWidget(self.title_frame)
            layout.setSpacing(0)
            layout.setContentsMargins(0, 0, 0, 0)
            cont    = 0
            self.horizontal         = QHBoxLayout()
            for i in lists:
                self.frame_content  = QFrame(widget)
                self.frame_content.setMinimumSize(QSize(1000, 75))
                self.frame_content.setStyleSheet("border: 2px solid; color: #D6D6D6")

                self.frame_id           = QFrame(self.frame_content)
                self.frame_id.setMaximumWidth(50)
                self.frame_id.setStyleSheet("border: 0; border-right: 1px solid;")
                self.id_label           = QLabel(self.frame_id)
                self.id_label.setStyleSheet("""
                
                margin-top: 10px;
                font-size: 17px;
                color: #C2C2C2;
                border-right: 0""")
                self.id_label.setText(str(i[0]))
                self.frame_name         = QFrame(self.frame_content)
                
                self.frame_name.setMinimumWidth(205)
                self.frame_name.setStyleSheet("border: 0; border-right: 1px solid;")

                self.name_label         = QLabel(self.frame_name)
                self.name_label.setFixedWidth(200)
                self.name_label.setAlignment(Qt.AlignCenter)

                self.name_label.setStyleSheet("""
                margin-top: 10px;
                font-size: 14px;
                color: #C2C2C2;
                border-right: 0""")
                self.name_label.setText(str(i[1]))

                self.frame_cpf         = QFrame(self.frame_content)
                self.frame_cpf.setMinimumWidth(400)
                self.frame_cpf.setStyleSheet("border: 0; border-right: 1px solid;")

                self.cpf_label         = QLabel(self.frame_cpf)
                self.cpf_label.setFixedWidth(398)
                self.cpf_label.setAlignment(Qt.AlignCenter)

                self.cpf_label.setStyleSheet("""
                margin-top: 10px;
                font-size: 17px;
                color: #C2C2C2;
                border-right: 0""")
                self.cpf_label.setText(str(i[2]))
                
                self.frame_rg   = QFrame(self.frame_content)
                self.frame_rg.setStyleSheet("border: 0; border-right: 1px solid;")
                self.frame_rg.setMinimumWidth(215)

                self.rg_label         = QLabel(self.frame_rg)
                self.rg_label.setFixedWidth(214)
                self.rg_label.setAlignment(Qt.AlignCenter)

                self.rg_label.setStyleSheet("""
                margin-top: 10px;
                font-size: 17px;
                color: #C2C2C2;
                border-right: 0""")
                self.rg_label.setText(str(i[3]))

                self.check_frame        = QFrame(self.frame_content)
                self.check_frame.setStyleSheet("border: 0;")    

                

                self.check_box_value    = {}
                self.check_box          = QCheckBox(str(i[0]), self.check_frame)
                self.check_box.setStyleSheet("color: transparent;margin-left: 35px;margin-top: 15px;")
                self.check_box.setChecked(Qt.Unchecked)
                
                self.horizontal.addWidget(self.check_box)
                
                self.horizontal_layout  = QHBoxLayout(self.frame_content)

                

                self.horizontal_layout.addWidget(self.frame_id)
                self.horizontal_layout.addWidget(self.frame_name)
                self.horizontal_layout.addWidget(self.frame_cpf)
                self.horizontal_layout.addWidget(self.frame_rg)
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