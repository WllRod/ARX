from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow, QFrame, QSizePolicy, QCheckBox)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic, QtCore
import sys
from datetime import datetime



class Window_Folha(QScrollArea):

    def __init__(self, lists):
        super(Window_Folha, self).__init__()
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

        if(lists == False or lists == []):
            layout.addWidget(QLabel(""))
        else:
        
            
            self.title_frame    = QFrame(widget)
            self.title_frame.setMaximumSize(QSize(800, 65))
            self.title_frame.setMinimumSize(QSize(800, 65))
            self.title_frame.setStyleSheet("border: 2px solid; color: #D6D6D6; background: rgb(30, 30, 30)")

            ##################################TITLE_ID#############################################
            self.frame_title_id     = QFrame()
            self.frame_title_id.setFixedWidth(self.title_frame.width() / 10)
            self.frame_title_id.setStyleSheet("border: 0; border-right: 1px solid;")
            self.label_title_id     = QLabel(self.frame_title_id)
            self.label_title_id.setFixedWidth(self.frame_title_id.width())
            self.label_title_id.setStyleSheet("""font-size: 17px;color: #C2C2C2;""")
            self.label_title_id.setAlignment(QtCore.Qt.AlignCenter)
            self.label_title_id.setText("ID")
            ##################################TITLE_DESC###########################################
            self.frame_title_desc   = QFrame()
            self.frame_title_desc.setStyleSheet("border: 0; border-right: 1px solid;")
            self.frame_title_desc.setFixedWidth(360)
            self.label_desc_title     = QLabel(self.frame_title_desc)
            self.label_desc_title.setFixedWidth(self.frame_title_desc.width())
            self.label_desc_title.setStyleSheet("""font-size: 17px;color: #C2C2C2;""")
            self.label_desc_title.setAlignment(QtCore.Qt.AlignCenter)
            self.label_desc_title.setText("DESCRIÇÃO")
            #################################TITLE_DATA############################################
            self.frame_title_data   = QFrame()
            self.frame_title_data.setStyleSheet("border: 0; border-right: 0")
            self.frame_title_data.setFixedWidth(300)
            self.label_title_data     = QLabel(self.frame_title_data)
            self.label_title_data.setFixedWidth(self.frame_title_data.width())
            self.label_title_data.setStyleSheet("""font-size: 17px;color: #C2C2C2;""")
            self.label_title_data.setAlignment(QtCore.Qt.AlignCenter)
            self.label_title_data.setText("DATA DE CONCLUSÃO")
            
            self.horizontal_layout_2    = QHBoxLayout(self.title_frame)

            self.horizontal_layout_2.addWidget(self.frame_title_id)
            
            self.horizontal_layout_2.addWidget(self.frame_title_desc)
            self.horizontal_layout_2.addWidget(self.frame_title_data)
            
            layout.addWidget(self.title_frame)
            #layout.setSpacing(0)
            #layout.setContentsMargins(0, 0, 0, 0)
            cont    = 0
            self.horizontal         = QHBoxLayout()
            for i in lists:
                self.frame_content  = QFrame(widget)
                self.frame_content.setMinimumSize(QSize(900, 75))
                self.frame_content.setStyleSheet("border: 2px solid; color: #D6D6D6")

                #######################################ID#################################
                self.frame_id           = QFrame()
                self.frame_id.setFixedWidth(self.frame_title_id.width() + 5)
                self.frame_id.setStyleSheet("border: 0; border-right: 1px solid;")

                self.label_id           = QLabel(self.frame_id)
                self.label_id.setStyleSheet("""font-size: 17px;color: #C2C2C2;""")
                self.label_id.setFixedWidth(self.frame_id.width())
                self.label_id.setAlignment(QtCore.Qt.AlignCenter)
                self.label_id.setText(str(i[0]))
                #######################################DESC#################################
                self.frame_desc         = QFrame()
                self.frame_desc.setStyleSheet("border: 0; border-right: 1px solid;")
                self.frame_desc.setFixedWidth(self.frame_title_desc.width() + 9)

                self.label_desc           = QLabel(self.frame_desc)
                self.label_desc.setStyleSheet("""font-size: 17px;color: #C2C2C2;""")
                self.label_desc.setFixedWidth(self.frame_desc.width())
                self.label_desc.setAlignment(QtCore.Qt.AlignCenter)
                self.label_desc.setText(str(i[1]))
                #######################################DATA#################################
                self.frame_data         = QFrame()
                self.frame_data.setStyleSheet("border: 0; border-right: 1px solid;")
                self.frame_data.setFixedWidth(self.frame_title_data.width() + 20)

                self.label_data           = QLabel(self.frame_data)
                self.label_data.setStyleSheet("""font-size: 17px;color: #C2C2C2;""")
                self.label_data.setFixedWidth(self.frame_data.width())
                self.label_data.setAlignment(QtCore.Qt.AlignCenter)
                if(i[2] == None):
                    self.label_data.setText(str(i[2]))
                else:
                    data    = datetime.strptime(str(i[2]), "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y")
                    self.label_data.setText(str(data))
                ############################################################################
                self.frame_check_box    = QFrame()
                self.frame_check_box.setStyleSheet("border: 0; border-right: 0;")

                self.check_box          = QCheckBox(str(i[0]), self.frame_check_box)
                self.check_box.setStyleSheet("color: transparent;margin-left: 35px;margin-top: 15px;")
                self.check_box.setChecked(Qt.Unchecked)
                
                self.horizontal.addWidget(self.check_box)
                self.horizontal_layout  = QHBoxLayout(self.frame_content)

                self.horizontal_layout.addWidget(self.frame_id)
                self.horizontal_layout.addWidget(self.frame_desc)
                self.horizontal_layout.addWidget(self.frame_data)
                self.horizontal_layout.addWidget(self.frame_check_box)
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