from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow, QFrame, QSizePolicy, QCheckBox)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic, QtCore
import sys

#from Layouts.loading_screen import LoadignScreen

class Cargos_List(QScrollArea):

    def __init__(self, lists):
        super(Cargos_List, self).__init__()
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
            self.title_frame.setMaximumSize(QSize(525, 80))
            self.title_frame.setMinimumSize(QSize(525, 80))
            self.title_frame.setStyleSheet("border: 2px solid;color: #D6D6D6; background: rgb(30, 30, 30)")
            self.horizontal_titles  = QHBoxLayout(self.title_frame)
            #############################################################
            self.frame_id   = QFrame()
            self.frame_id.setStyleSheet("border: 0;border-right: 1px solid; ")
            self.frame_id.setMaximumWidth(50)
            self.frame_id.setMaximumHeight(self.title_frame.height())
            
            self.label_id   = QLabel(self.frame_id)
            self.label_id.setFixedWidth(self.frame_id.width())
            self.label_id.setFixedHeight(self.frame_id.height()/2)
            self.label_id.setStyleSheet(
                    "font-size: 17px;"
                    "color: #C2C2C2;"
                    )
            self.label_id.setAlignment(QtCore.Qt.AlignCenter)
            self.label_id.setText("ID")
            #############################################################
            self.frame_descricao    = QFrame()
            self.frame_descricao.setMaximumHeight(self.title_frame.height())
            self.frame_descricao.setMaximumWidth(self.title_frame.width())
            
            self.frame_descricao.setStyleSheet("border: 0; ")
            self.label_descricao    = QLabel(self.frame_descricao)
            self.label_descricao.setFixedWidth(self.frame_descricao.width() - 70)
            self.label_descricao.setFixedHeight(self.frame_descricao.height()/2)
            self.label_descricao.setStyleSheet(
                    "font-size: 17px;"
                    "color: #C2C2C2;"
                    )
            self.label_descricao.setAlignment(QtCore.Qt.AlignCenter)
            self.label_descricao.setText("DESCRIÇÃO")
            #self.frame_descricao.setFixedSize(self.frame_descricao.frameGeometry().width())
            
            #############################################################
            
            self.horizontal_titles.addWidget(self.frame_id)
            self.horizontal_titles.addWidget(self.frame_descricao)
            


            layout.addWidget(self.title_frame)
            self.horizontal         = QHBoxLayout()
            for i in lists:
                self.frame_content  = QFrame(widget)
                self.frame_content.setMinimumSize(QSize(595, 75))
                self.frame_content.setStyleSheet("border: 2px solid; color: #D6D6D6")

                self.horizontal_layout  = QHBoxLayout(self.frame_content)
                #######################################################################
                self.frame_id_content   = QFrame()
                self.frame_id_content.setStyleSheet("border: 0;border-right: 1px solid; ")
                self.frame_id_content.setMaximumWidth(50)
                self.frame_id_content.setMaximumHeight(self.frame_content.height())
                self.label_id_content   = QLabel(self.frame_id_content)
                self.label_id_content.setFixedWidth(self.frame_id.width())
                self.label_id_content.setFixedHeight(self.frame_id.height()/2)
                self.label_id_content.setStyleSheet(
                        "font-size: 17px;"
                        "color: #C2C2C2;"
                        )
                self.label_id_content.setAlignment(QtCore.Qt.AlignCenter)
                self.label_id_content.setText(str(i[1]))

                #######################################################################
                self.frame_desc_content = QFrame()
                self.frame_desc_content.setStyleSheet("background: yellow;")
                self.frame_desc_content.setMinimumWidth(460)
                self.frame_desc_content.setMaximumWidth(460)
                #self.frame_desc_content.setMaximumHeight(self.frame_content.height())
                #self.frame_desc_content.setMaximumWidth(self.frame_content.width() - 50)
                print(self.frame_desc_content.width())
                
                self.frame_desc_content.setStyleSheet("border: 0; border-right: 1px solid;")
                self.label_desc_content   = QLabel(self.frame_desc_content)
                self.label_desc_content.setStyleSheet(
                        "font-size: 17px;"
                        "color: #C2C2C2;"
                )
                self.label_desc_content.setFixedWidth(self.frame_desc_content.width())
                self.label_desc_content.setText(str(i[0]))
                self.label_desc_content.setAlignment(QtCore.Qt.AlignCenter)

                #######################################################################

                self.check_box_frame    = QFrame()
                self.check_box_frame.setStyleSheet("border: 0;")

                self.check_box          = QCheckBox(str(i[1]), self.check_box_frame)
                
                self.check_box.setStyleSheet("color: transparent;margin-top: 18px;margin-left: 19px;")
                self.check_box.setChecked(Qt.Unchecked)

                self.horizontal_layout.addWidget(self.frame_id_content)
                self.horizontal_layout.addWidget(self.frame_desc_content)
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