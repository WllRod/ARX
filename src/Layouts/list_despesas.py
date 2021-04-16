from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow, QFrame, QSizePolicy, QCheckBox)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic, QtCore
import sys



class Despesas_List(QScrollArea):

    def __init__(self, lists):
        super(Despesas_List, self).__init__()
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
        
        if(lists == [] or lists == None or lists == False):
            pass
        else:

            self.title_frame    = QFrame(widget)
            self.title_frame.setMaximumSize(QSize(900, 65))
            self.title_frame.setMinimumSize(QSize(900, 65))
            self.title_frame.setStyleSheet("border: 2px solid; color: #D6D6D6; background: rgb(30, 30, 30)")
            self.horizontal_layout_title    = QHBoxLayout(self.title_frame)
            self.frame_num_titulo_title     = QFrame()
            self.frame_num_titulo_title.setStyleSheet("border: 0; border-right: 1px solid;")
            self.frame_num_titulo_title.setFixedWidth(self.title_frame.width() / 5)

            self.label_num_titulo_title     = QLabel(self.frame_num_titulo_title)
            self.label_num_titulo_title.setStyleSheet("""font-size: 17px;color: #C2C2C2;""")
        
            self.label_num_titulo_title.setFixedWidth(self.frame_num_titulo_title.width())
            self.label_num_titulo_title.setAlignment(QtCore.Qt.AlignCenter)
            self.label_num_titulo_title.setText("NUM. TÍTULO")
            ########################################################################################
            self.frame_descricao_title      = QFrame()
            self.frame_descricao_title.setStyleSheet("border: 0; border-right: 1px solid;")
            self.frame_descricao_title.setFixedWidth(self.title_frame.width() / 3)

            self.label_descricao_title     = QLabel(self.frame_descricao_title)
            self.label_descricao_title.setStyleSheet("""font-size: 17px;color: #C2C2C2;""")
        
            self.label_descricao_title.setFixedWidth(self.frame_descricao_title.width())
            self.label_descricao_title.setAlignment(QtCore.Qt.AlignCenter)
            self.label_descricao_title.setText("DESCRIÇÃO")
            ########################################################################################
            self.frame_valor_title          = QFrame()
            self.frame_valor_title.setStyleSheet("border: 0; border-right: 1px solid;")
            self.frame_valor_title.setFixedWidth(self.title_frame.width() / 5)

            self.label_valor_title     = QLabel(self.frame_valor_title)
            self.label_valor_title.setStyleSheet("""font-size: 17px;color: #C2C2C2;""")
        
            self.label_valor_title.setFixedWidth(self.frame_valor_title.width())
            self.label_valor_title.setAlignment(QtCore.Qt.AlignCenter)
            self.label_valor_title.setText("VALOR")
            ########################################################################################
            self.frame_obra_title           = QFrame()
            self.frame_obra_title.setStyleSheet("border: 0; border-right: 0;")
            self.frame_obra_title.setFixedWidth(200)
            self.label_obra_title     = QLabel(self.frame_obra_title)
            self.label_obra_title.setStyleSheet("""font-size: 17px;color: #C2C2C2;""")
        
            self.label_obra_title.setFixedWidth(self.frame_obra_title.width())
            self.label_obra_title.setAlignment(QtCore.Qt.AlignCenter)
            self.label_obra_title.setText("OBRA")

            self.horizontal_layout_title.addWidget(self.frame_num_titulo_title)
            self.horizontal_layout_title.addWidget(self.frame_descricao_title)
            self.horizontal_layout_title.addWidget(self.frame_valor_title)
            self.horizontal_layout_title.addWidget(self.frame_obra_title)

            
            layout.addWidget(self.title_frame)
            #layout.setSpacing(0)
            #layout.setContentsMargins(0, 0, 0, 0)
            cont    = 0
            self.horizontal         = QHBoxLayout()
            for i in lists:
                self.frame_content  = QFrame(widget)
                self.frame_content.setMinimumSize(QSize(1000, 75))
                self.frame_content.setStyleSheet("border: 2px solid; color: #D6D6D6")

                self.frame_num_titulo   = QFrame()
                
                self.frame_num_titulo.setStyleSheet("border:0; border-right: 1px solid;")
                self.frame_num_titulo.setFixedWidth(self.frame_num_titulo_title.width())
                self.label_num_titulo   = QLabel(self.frame_num_titulo)
                self.label_num_titulo.setStyleSheet("""font-size: 17px;color: #C2C2C2;""")
                self.label_num_titulo.setFixedWidth(self.frame_num_titulo_title.width())
                self.label_num_titulo.setAlignment(QtCore.Qt.AlignCenter)
                self.label_num_titulo.setText(str(i[1]))
                self.frame_descricao    = QFrame()
                self.frame_descricao.setStyleSheet("border:0; border-right: 1px solid;")
                self.frame_descricao.setFixedWidth(self.frame_descricao_title.width())
                self.label_descricao   = QLabel(self.frame_descricao)
                self.label_descricao.setStyleSheet("""font-size: 17px;color: #C2C2C2;""")
                self.label_descricao.setFixedWidth(self.frame_descricao_title.width())
                self.label_descricao.setAlignment(QtCore.Qt.AlignCenter)
                self.label_descricao.setText(str(i[2]))
                self.frame_valor        = QFrame()
                self.frame_valor.setStyleSheet("border:0; border-right: 1px solid;")
                self.frame_valor.setFixedWidth(self.frame_valor_title.width())
                self.label_valor   = QLabel(self.frame_valor)
                self.label_valor.setStyleSheet("""font-size: 17px;color: #C2C2C2;""")
                self.label_valor.setFixedWidth(self.frame_valor_title.width())
                self.label_valor.setAlignment(QtCore.Qt.AlignCenter)
                self.label_valor.setText(str(i[3]))
                self.frame_obra         = QFrame()
                self.frame_obra.setStyleSheet("border:0; border-right: 1px solid;")
                self.frame_obra.setFixedWidth(self.frame_obra_title.width() + 10)
                self.label_obra   = QLabel(self.frame_obra)
                self.label_obra.setStyleSheet("""font-size: 17px;color: #C2C2C2;""")
                self.label_obra.setFixedWidth(self.frame_obra_title.width() + 10)
                self.label_obra.setAlignment(QtCore.Qt.AlignCenter)
                self.label_obra.setText(str(i[4]))
                

                self.check_frame        = QFrame()
                self.check_frame.setStyleSheet("border: 0;")   

                self.check_box          = QCheckBox(str(i[0]), self.check_frame)
                self.check_box.setStyleSheet("color: transparent;margin-left: 35px;margin-top: 15px;")
                self.check_box.setChecked(Qt.Unchecked)
                
                self.horizontal.addWidget(self.check_box)
                

                self.horizontal_layout_content  = QHBoxLayout(self.frame_content)
                self.horizontal_layout_content.addWidget(self.frame_num_titulo)
                self.horizontal_layout_content.addWidget(self.frame_descricao)
                self.horizontal_layout_content.addWidget(self.frame_valor)
                self.horizontal_layout_content.addWidget(self.frame_obra)
                self.horizontal_layout_content.addWidget(self.check_frame)

                '''self.frame_id           = QFrame(self.frame_content)
                self.frame_id.setMaximumWidth(100)
                self.frame_id.setStyleSheet("border: 0; border-right: 1px solid;")
                self.id_label           = QLabel(self.frame_id)
                self.id_label.setStyleSheet("""
                
                margin-top: 10px;
                font-size: 17px;
                color: #C2C2C2;
                border-right: 0""")
                self.id_label.setText(str(i[1]))
                self.frame_user         = QFrame(self.frame_content)
                
                self.frame_user.setMinimumWidth(100)
                self.frame_user.setStyleSheet("border: 0; border-right: 1px solid;")

                self.user_label         = QLabel(self.frame_user)
                #self.user_label.setFixedWidth(100)
                self.user_label.setAlignment(Qt.AlignCenter)

                self.user_label.setStyleSheet("""
                margin-top: 10px;
                font-size: 17px;
                color: #C2C2C2;
                border-right: 0""")
                self.user_label.setText(str(i[2]))

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
                self.name_label.setText(str(i[3]))
                
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
                
                self.permission_label.setText(str(i[4]))


                self.check_frame        = QFrame(self.frame_content)
                self.check_frame.setStyleSheet("border: 0;")    

                

                self.check_box_value    = {}
                self.check_box          = QCheckBox(str(i[0]), self.check_frame)
                self.check_box.setStyleSheet("color: transparent;margin-left: 35px;margin-top: 15px;")
                self.check_box.setChecked(Qt.Unchecked)
                
                self.horizontal.addWidget(self.check_box)
                
                self.horizontal_layout  = QHBoxLayout(self.frame_content)

                

                self.horizontal_layout.addWidget(self.frame_id)
                self.horizontal_layout.addWidget(self.frame_user)
                self.horizontal_layout.addWidget(self.frame_name)
                self.horizontal_layout.addWidget(self.frame_permission)
                self.horizontal_layout.addWidget(self.check_frame)'''
                layout.addWidget(self.frame_content)

            
            
        self.setWidget(widget)
        
    def check_box_func(self):
        
        checked_list = []
        try:
            for i in range(self.horizontal.count()):
                chBox = self.horizontal.itemAt(i).widget()
                if chBox.isChecked():
                    checked_list.append(chBox.text())
            
            #self.setWidgetResizable(True)
            
            return list(checked_list)
        except Exception as e:
            pass
        