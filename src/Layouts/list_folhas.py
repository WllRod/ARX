from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow, QFrame, QSizePolicy, QCheckBox)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic, QtCore
import sys
from datetime import datetime

#from Layouts.loading_screen import LoadignScreen

class Folhas_Window(QScrollArea):

    def __init__(self, lists):
        super(Folhas_Window, self).__init__()
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
        if(lists == [] or lists == False or lists[0] == None or lists[0][0] == None):
            pass
        else:
        
            ####################################ID###############################################
            self.frame_id_title             = QFrame()
            self.frame_id_title.setStyleSheet("border: 0; border-right: 1px solid;")
            self.frame_id_title.setFixedWidth(self.title_frame.width() / 10)

            self.label_id_title   = QLabel(self.frame_id_title)
            self.label_id_title.setStyleSheet("""font-size: 17px;color: #C2C2C2;""")
            self.label_id_title.setFixedWidth(self.frame_id_title.width())
            self.label_id_title.setAlignment(QtCore.Qt.AlignCenter)
            self.label_id_title.setText("ID")
            ###################################DESC##############################################
            self.frame_id_desc              = QFrame()
            self.frame_id_desc.setStyleSheet("border: 0; border-right: 1px solid;")
            self.frame_id_desc.setFixedWidth(self.title_frame.width() / 3)

            self.label_desc_title   = QLabel(self.frame_id_desc)
            self.label_desc_title.setStyleSheet("""font-size: 17px;color: #C2C2C2;""")
            self.label_desc_title.setFixedWidth(self.frame_id_desc.width())
            self.label_desc_title.setAlignment(QtCore.Qt.AlignCenter)
            self.label_desc_title.setText("DESCRIÇÃO")

            ##################################DATA_INICIAL########################################
            self.frame_dataInicial_title    = QFrame()    
            self.frame_dataInicial_title.setStyleSheet("border: 0; border-right: 1px solid;")
            self.frame_dataInicial_title.setFixedWidth(self.title_frame.width() / 4)

            self.label_data_inicial_title   = QLabel(self.frame_dataInicial_title)
            self.label_data_inicial_title.setStyleSheet("""font-size: 17px;color: #C2C2C2;""")
            self.label_data_inicial_title.setFixedWidth(self.frame_dataInicial_title.width())
            self.label_data_inicial_title.setAlignment(QtCore.Qt.AlignCenter)
            self.label_data_inicial_title.setText("DATA INICIAL")
            
            ##################################DATA_FINAL###########################################
            self.frame_dataFinal_title      = QFrame()    
            self.frame_dataFinal_title.setFixedWidth(self.title_frame.width() / 4)
            self.frame_dataFinal_title.setStyleSheet("border: 0; border-right: 0;")

            self.label_data_final_title   = QLabel(self.frame_dataFinal_title)
            self.label_data_final_title.setStyleSheet("""font-size: 17px;color: #C2C2C2;""")
            self.label_data_final_title.setFixedWidth(self.frame_dataFinal_title.width())
            self.label_data_final_title.setAlignment(QtCore.Qt.AlignCenter)
            self.label_data_final_title.setText("DATA FINAL")
            ########################################################################################
            self.horizontal_layout_2    = QHBoxLayout(self.title_frame)



            self.horizontal_layout_2.addWidget(self.frame_id_title)
            self.horizontal_layout_2.addWidget(self.frame_id_desc)
            self.horizontal_layout_2.addWidget(self.frame_dataInicial_title)
            self.horizontal_layout_2.addWidget(self.frame_dataFinal_title)
            
            layout.addWidget(self.title_frame)
            #layout.setSpacing(0)
            #layout.setContentsMargins(0, 0, 0, 0)
            cont    = 0
            self.horizontal         = QHBoxLayout()
            for i in lists:
                
                self.frame_content  = QFrame(widget)
                self.frame_content.setMinimumSize(QSize(1000, 75))
                self.frame_content.setStyleSheet("border: 2px solid; color: #D6D6D6")

                ###########################id####################################
                self.frame_id           = QFrame()
                self.frame_id.setFixedWidth(self.frame_id_title.width() + 4) 
                self.frame_id.setStyleSheet("border: 0; border-right: 1px solid;")

                self.label_id           = QLabel(self.frame_id)
                self.label_id.setFixedWidth(self.frame_id.width())
                self.label_id.setAlignment(QtCore.Qt.AlignCenter)
                self.label_id.setStyleSheet("""font-size: 17px;color: #C2C2C2;""")
                self.label_id.setText(str(i[0]))
                ###########################obra####################################
                self.frame_desc         = QFrame()
                self.frame_desc.setFixedWidth(self.frame_id_desc.width() + 5) 
                self.frame_desc.setStyleSheet("border: 0; border-right: 1px solid;")

                self.label_desc           = QLabel(self.frame_desc)
                self.label_desc.setFixedWidth(self.frame_desc.width())
                self.label_desc.setAlignment(QtCore.Qt.AlignCenter)
                self.label_desc.setStyleSheet("""font-size: 17px;color: #C2C2C2;""")
                self.label_desc.setText(str(i[1]))
                ##########################DATAINICIAL#############################
                self.frame_data_inicial = QFrame()
                self.frame_data_inicial.setFixedWidth(self.frame_dataInicial_title.width() + 8)
                self.frame_data_inicial.setStyleSheet("border: 0; border-right: 1px solid;")

                self.label_data_inicial           = QLabel(self.frame_data_inicial)
                self.label_data_inicial.setFixedWidth(self.frame_data_inicial.width())
                self.label_data_inicial.setAlignment(QtCore.Qt.AlignCenter)
                self.label_data_inicial.setStyleSheet("""font-size: 17px;color: #C2C2C2;""")
                try:
                    data_inicial    = datetime.strptime(str(i[2]), "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y")
                    self.label_data_inicial.setText(data_inicial)
                except Exception as e:
                    pass

                ##########################DATAFINAL###############################
                self.frame_data_final   = QFrame()
                self.frame_data_final.setFixedWidth(self.frame_dataFinal_title.width() + 14) 
                self.frame_data_final.setStyleSheet("border: 0; border-right: 1px solid;")

                self.label_data_final           = QLabel(self.frame_data_final)
                self.label_data_final.setFixedWidth(self.frame_data_final.width())
                self.label_data_final.setAlignment(QtCore.Qt.AlignCenter)
                self.label_data_final.setStyleSheet("""font-size: 17px;color: #C2C2C2;""")
                try:
                    data_final  = datetime.strptime(str(i[3]), "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y")
                    self.label_data_final.setText(data_final)
                except Exception as e:
                    pass
                

                self.check_box_frame    = QFrame()
                self.check_box_frame.setStyleSheet("border: 0; border-right: 0;")

                self.check_box          = QCheckBox(str(i[0]), self.check_box_frame)
                self.check_box.setStyleSheet("color: transparent;margin-left: 35px;margin-top: 15px;")
                self.check_box.setChecked(Qt.Unchecked)
                    
                

                self.horizontal_layout  = QHBoxLayout(self.frame_content)

                self.horizontal_layout.addWidget(self.frame_id)
                self.horizontal_layout.addWidget(self.frame_desc)
                self.horizontal_layout.addWidget(self.frame_data_inicial)
                self.horizontal_layout.addWidget(self.frame_data_final)
                self.horizontal_layout.addWidget(self.check_box_frame)
                self.horizontal.addWidget(self.check_box)

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