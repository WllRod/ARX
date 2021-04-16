from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

from DB_Connect.SQL import DB_Alter, SQL_Funcionario, Funcoes
import threading

class Confirmation_Screen(object):

    def __init__(self):
        super().__init__()

        self.confirm_btn = QPushButton()
        self.dialog = QDialog()
    def show_confirmation(self, texto, onlyText=None, list=None, refresh_1=None, func=None, user=None, cargo=None, btn=None, refresh_2=None):
        
        self.list           = list
        self.refresh_1      = refresh_1
        self.refresh_2      = refresh_2
        self.user           = user
        self.func           = func
        self.cargo          = cargo
        self.verticalLayout = QVBoxLayout(self.dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label  = QLabel()
        self.label.setFixedSize(QSize(498, 50))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("""
        margin-left: 8px; 
        margin-top: 10px;
        font-size: 17px;
        color: #D6D6D6;
        border: 0;""")
        self.label.setText(texto)
        self.frame  = QFrame()
        self.horizontalLayout   = QHBoxLayout(self.frame)
        
        
        ###################CONFIRM BUTTON######################

        
        
        self.confirm_btn.setStyleSheet("margin-top: 5%; margin-left: 2px; border-radius: 2px;background: rgb(85, 170, 255); border: 0;")

        self.confirm_btn.setMaximumSize(QSize(100, 50))
        if(btn == None):
            self.confirm_btn.clicked.connect(self.confirm_onClick)
        self.confirm_btn.setText("Confirmar")
        self.confirm_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.confirm_btn.setIcon(QIcon("assets\\confirm.png"))
        self.confirm_btn.setIconSize(QSize(25, 50))
        
        ###################CLOSE BUTTON#########################
        self.close_btn = QPushButton()
        
        self.close_btn.setStyleSheet("margin-top: 5%; margin-left: 2px; border-radius: 2px;background: #D22121; border: 0;")

        self.close_btn.setMaximumSize(QSize(100, 50))
        self.close_btn.clicked.connect(self.close_btn_click)
        self.close_btn.setText("Fechar")
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.close_btn.setIcon(QIcon("assets\\close.png"))
        self.close_btn.setIconSize(QSize(25, 50))
        #########################################################

            #self.frame_icon_include_btn  = QFrame(self.close_btn)
        

        if(onlyText):
            self.horizontalLayout.addWidget(self.close_btn)
        else:
            self.horizontalLayout.addWidget(self.confirm_btn)
            self.horizontalLayout.addWidget(self.close_btn)
        
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame)
        self.dialog.setMaximumSize(QSize(500, 200))
        self.dialog.setMinimumSize(QSize(500, 200))
        self.dialog.setWindowFlag(Qt.FramelessWindowHint)
        self.dialog.setStyleSheet(u"background: rgb(40, 40, 40); border: 1px solid; border-color: red;")
        
        self.dialog.exec_()
        
        return True
    def close_btn_click(self):
        self.dialog.close()
    
    def confirm_onClick(self):
        self.sql_user       = DB_Alter()
        self.sql_func       = SQL_Funcionario()
        self.sql_cargo      = Funcoes()  
        self.sql    = DB_Alter()
        if(self.func != None):
           

            for x in self.list:
                self.sql_func.exclude_func(str(x))
            
        elif(self.user != None):

            for x in self.list:
                self.sql_user.delete_user(str(x))
        
        elif(self.cargo != None):
            for x in self.list:
                self.sql_cargo.del_cargo(str(x))
        if(self.refresh_1 != None):
            self.refresh_1()
        if(self.refresh_2 != None):
            self.refresh_2()
        if(self.refresh_1 != None and self.refresh_2 != None):
            self.refresh_1()
            self.refresh_2()
        self.dialog.close()

