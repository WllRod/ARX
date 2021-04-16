from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow, QFrame, QSizePolicy, QCheckBox)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic
import sys



class Window(QScrollArea):

    def __init__(self, lists):
        super(Window, self).__init__()
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
        
        self.title_frame    = QFrame(widget)
        self.title_frame.setMaximumSize(QSize(900, 65))
        self.title_frame.setMinimumSize(QSize(900, 65))
        self.title_frame.setStyleSheet("border: 2px solid; color: #D6D6D6; background: rgb(30, 30, 30)")
        
        if(lists == [] or lists == False):
            pass
        else:
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
            self.label_title_user.setText("Usuário")

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
            self.label_title_name.setText("Nome")
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
            self.label_title_permission.setText("Tipo de Permissão")
            self.horizontal_layout_2    = QHBoxLayout(self.title_frame)

            self.horizontal_layout_2.addWidget(self.title_id)
            self.horizontal_layout_2.addWidget(self.title_user)
            self.horizontal_layout_2.addWidget(self.title_name)
            self.horizontal_layout_2.addWidget(self.title_permission)
            layout.addWidget(self.title_frame)
            #layout.setSpacing(0)
            #layout.setContentsMargins(0, 0, 0, 0)
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
                self.id_label.setText(str(i.ID))
                self.frame_user         = QFrame(self.frame_content)
                
                self.frame_user.setMinimumWidth(205)
                self.frame_user.setStyleSheet("border: 0; border-right: 1px solid;")

                self.user_label         = QLabel(self.frame_user)
                self.user_label.setFixedWidth(200)
                self.user_label.setAlignment(Qt.AlignCenter)

                self.user_label.setStyleSheet("""
                margin-top: 10px;
                font-size: 17px;
                color: #C2C2C2;
                border-right: 0""")
                self.user_label.setText(str(i.USER))

                self.frame_name         = QFrame(self.frame_content)
                self.frame_name.setMinimumWidth(400)
                self.frame_name.setStyleSheet("border: 0; border-right: 1px solid;")

                self.name_label         = QLabel(self.frame_name)
                self.name_label.setFixedWidth(398)
                self.name_label.setAlignment(Qt.AlignCenter)

                self.name_label.setStyleSheet("""
                margin-top: 10px;
                font-size: 17px;
                color: #C2C2C2;
                border-right: 0""")
                self.name_label.setText(str(i.NAME))
                
                self.frame_permission   = QFrame(self.frame_content)
                self.frame_permission.setStyleSheet("border: 0; border-right: 1px solid;")
                self.frame_permission.setMinimumWidth(215)

                self.permission_label         = QLabel(self.frame_permission)
                self.permission_label.setFixedWidth(214)
                self.permission_label.setAlignment(Qt.AlignCenter)

                self.permission_label.setStyleSheet("""
                margin-top: 10px;
                font-size: 17px;
                color: #C2C2C2;
                border-right: 0""")
                if(i.PERMISSION == 0):
                    self.permission_label.setText("Administrador")
                elif(i.PERMISSION == 1):
                    self.permission_label.setText("Gerente")
                elif(i.PERMISSION == 2):
                    self.permission_label.setText("Operador")


                self.check_frame        = QFrame(self.frame_content)
                self.check_frame.setStyleSheet("border: 0;")    

                

                self.check_box_value    = {}
                self.check_box          = QCheckBox(str(i.ID), self.check_frame)
                self.check_box.setStyleSheet("color: transparent;margin-left: 35px;margin-top: 15px;")
                self.check_box.setChecked(Qt.Unchecked)
                
                self.horizontal.addWidget(self.check_box)
                
                self.horizontal_layout  = QHBoxLayout(self.frame_content)

                

                self.horizontal_layout.addWidget(self.frame_id)
                self.horizontal_layout.addWidget(self.frame_user)
                self.horizontal_layout.addWidget(self.frame_name)
                self.horizontal_layout.addWidget(self.frame_permission)
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