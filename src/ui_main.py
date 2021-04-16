from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QThread, QTimer, QDate, QTime)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QPixmap)
from PyQt5.QtWidgets import *
from PyQt5 import sip, QtCore
import sys
import threading
from DB_Connect.SQL import DB_Alter, DB_Login, SQL_Funcionario, Funcoes
from Layouts.frame import Frame
from Layouts.list_users import Window
from Layouts.Confirmation import Confirmation_Screen
from Layouts.Frame_Box import FrameBox
from Layouts.Buttons import CRUD_Buttons
from Layouts.Func import Window_Add_Func, Edit_Func
from Layouts.list_funcs import Func_Window
from Layouts.list_cargos import Cargos_List
from Layouts.list_clientes import Clientes_List
from background_functions import (
    Functions, 
    Cargos, 
    Obras_Functions, 
    Folha_Ponto_Function, 
    ErrorMessage,
    Clientes,
    Despesas,
    Relatorios
    )
from Layouts.cargos_dialog import Add_Cargo, Edit_Cargo
from Layouts.atribFuncScreen import Atrib_Func_Window, Atrib_Func_Screen
from Layouts.obras_dialog import Add_Obra
from Layouts.Folha_Ponto_Params import Folha_Params
from Layouts.list_folhas import Folhas_Window
#from Layouts.loading_screen import main_loading
import queue
from datetime import datetime
from FOLHA_PONTO import QTable
from Layouts.list_folha import Window_Folha
from Layouts.form_cliente import Window_Add_Cliente
from Layouts.form_despesa import Window_Form_Despesa
from Layouts.list_despesas import Despesas_List
from Layouts.form_relatorios import Window_Form_Relatorio

class SplashScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.splashScreen   = QSplashScreen()
        self.splashScreen.show()

        QTimer.singleShot(5000, self.splashScreen.close)
        
class Ui_MainWindow(QMainWindow):

    def __init__(self, users, funcs, cargos, obras, folha, folhas_list, clientes_list, despesas_list):
        super().__init__()
        try:
            self.cont_folha     = 0
            self.cont_folha_del = 0
            self.funcs  = funcs
            self.counter    = 0
            self.cargos = cargos
            self.users  = users
            self.obras  = obras
            self.type   = ""
            self.folha  = folha
            self.lista_de_folhas    = folhas_list
            self.clientes_list      = clientes_list
            self.despesas_list      = despesas_list
            #self.folha_list_obras = folha_list
            self.Lista_De_Folhas    = Folhas_Window(self.lista_de_folhas)
            if(self.funcs != False):
                self.func_box   = Func_Window(self.funcs)
            else:
                self.func_box   = QLabel("")
            self.users_list = Window(users)

            if(self.cargos != False):
                
                self.cargos_list    = Cargos_List(self.cargos)
            else:
                self.cargos_list    = QLabel("")
            self.folha_list         = Window_Folha(self.folha)
            self.obras_list         = self.folha_list
            self.clientes_screen    = Clientes_List(self.clientes_list) 
            self.cargos_funcoes = Cargos()
            self.despesas_screen_list   = Despesas_List(self.despesas_list)
            self.background = "background-color: rgb(45, 45, 45);"
            #self.loading    = LoadignScreen()       
            self.resize(1000, 500)
            self.setMinimumSize(QSize(1000, 500))
            self.setStyleSheet(self.background)
            self.users          = users
            self.function       = Functions()
            self.crud_buttons   = CRUD_Buttons()
            self.crud_buttons_2 = CRUD_Buttons()
            self.crud_buttons_3 = CRUD_Buttons()
            self.crud_buttons_4 = CRUD_Buttons()
            self.crud_buttons_5 = CRUD_Buttons()
            self.crud_buttons_6 = CRUD_Buttons()
            self.crud_buttons_7 = CRUD_Buttons()
            self.crud_buttons_teste = CRUD_Buttons()
            self.sql    = DB_Alter()
            self.return_user    = DB_Login()
            self.sql_func       = SQL_Funcionario()
            
            #self.users_list = Window(users)
            self.centralwidget = QWidget()
            self.centralwidget.setObjectName(u"centralwidget")
            self.verticalLayout = QVBoxLayout(self.centralwidget)
            self.verticalLayout.setSpacing(0)
            self.verticalLayout.setObjectName(u"verticalLayout")
            self.verticalLayout.setContentsMargins(0, 0, 0, 0)
            self.Top_Bar = QFrame(self.centralwidget)
            self.Top_Bar.setObjectName(u"Top_Bar")
            self.Top_Bar.setMaximumSize(QSize(16777215, 40))
            self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
            self.Top_Bar.setFrameShape(QFrame.NoFrame)
            self.Top_Bar.setFrameShadow(QFrame.Raised)
            self.horizontalLayout = QHBoxLayout(self.Top_Bar)
            self.horizontalLayout.setSpacing(0)
            self.horizontalLayout.setObjectName(u"horizontalLayout")
            self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.frame_toggle = QFrame(self.Top_Bar)
            self.frame_toggle.setObjectName(u"frame_toggle")
            self.frame_toggle.setMaximumSize(QSize(150, 40))
            self.frame_toggle.setStyleSheet(u"background-color: rgb(85, 170, 255);")
            self.frame_toggle.setFrameShape(QFrame.StyledPanel)
            self.frame_toggle.setFrameShadow(QFrame.Raised)
            self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
            self.verticalLayout_2.setSpacing(0)
            self.verticalLayout_2.setObjectName(u"verticalLayout_2")
            self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
            self.Btn_Toggle = QPushButton(self.frame_toggle)
            self.Btn_Toggle.setMinimumSize(QSize(150, 40))
            self.Btn_Toggle.setObjectName(u"Btn_Toggle")
            sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
            self.Btn_Toggle.setSizePolicy(sizePolicy)
            self.Btn_Toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
    "border: 0px solid;")
            self.setWindowIcon(QIcon("assets\\ico.ico"))
            self.verticalLayout_2.addWidget(self.Btn_Toggle)


            self.horizontalLayout.addWidget(self.frame_toggle)

            self.frame_top = QFrame(self.Top_Bar)
            self.frame_top.setObjectName(u"frame_top")
            self.frame_top.setFrameShape(QFrame.StyledPanel)
            self.frame_top.setFrameShadow(QFrame.Raised)

            self.horizontalLayout.addWidget(self.frame_top)


            self.verticalLayout.addWidget(self.Top_Bar)
            
            self.Content = QFrame(self.centralwidget)
            self.Content.setObjectName(u"Content")
            self.Content.setFrameShape(QFrame.NoFrame)
            self.Content.setFrameShadow(QFrame.Raised)
            self.horizontalLayout_2 = QHBoxLayout(self.Content)
            self.horizontalLayout_2.setSpacing(0)
            self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
            self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
            self.frame_left_menu = QFrame(self.Content)
            self.frame_left_menu.setObjectName(u"frame_left_menu")
            self.frame_left_menu.setMinimumSize(QSize(0, 0))
            self.frame_left_menu.setMaximumSize(QSize(0, 16777215))
            self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
            self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
            self.frame_left_menu.setFrameShadow(QFrame.Raised)
            self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
            self.verticalLayout_3.setObjectName(u"verticalLayout_3")
            self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
            self.frame_top_menus = QFrame(self.frame_left_menu)
            self.frame_top_menus.setObjectName(u"frame_top_menus")
            self.frame_top_menus.setFrameShape(QFrame.NoFrame)
            self.frame_top_menus.setFrameShadow(QFrame.Raised)
            self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
            self.verticalLayout_4.setSpacing(0)
            self.verticalLayout_4.setObjectName(u"verticalLayout_4")
            self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
            self.btn_page_home = QPushButton(self.frame_top_menus)
            

            self.btn_page_home.setObjectName(u"btn_page_home")
            self.btn_page_home.setMinimumSize(QSize(0, 40))
            self.btn_page_home.setStyleSheet(u"QPushButton {\n"
    "	color: rgb(255, 255, 255);\n"
    "	background-color: rgb(35, 35, 35);\n"
    "	border: 0px solid;\n"
    "}\n"
    "QPushButton:hover {\n"
    "	background-color: rgb(85, 170, 255);\n"
    "}")
            self.btn_page_home.clicked.connect(self.home_screen)
            
            self.verticalLayout_4.addWidget(self.btn_page_home)
            self.btn_page_1 = QPushButton(self.frame_top_menus)
            self.btn_page_1.clicked.connect(self.btn_page_1_onClick)
            self.btn_page_1.setObjectName(u"btn_page_1")
            self.btn_page_1.setMinimumSize(QSize(0, 40))
            self.btn_page_1.setStyleSheet(u"QPushButton {\n"
    "	color: rgb(255, 255, 255);\n"
    "	background-color: rgb(35, 35, 35);\n"
    "	border: 0px solid;\n"
    "}\n"
    "QPushButton:hover {\n"
    "	background-color: rgb(85, 170, 255);\n"
    "}")
            
            self.verticalLayout_4.addWidget(self.btn_page_1)
            
            self.btn_page_2 = QPushButton(self.frame_top_menus)
            self.btn_page_2.clicked.connect(self.btn_page_2_func)
            self.btn_page_2.setObjectName(u"btn_page_2")
            self.btn_page_2.setMinimumSize(QSize(0, 40))
            self.btn_page_2.setStyleSheet(u"QPushButton {\n"
    "	color: rgb(255, 255, 255);\n"
    "	background-color: rgb(35, 35, 35);\n"
    "	border: 0px solid;\n"
    "}\n"
    "QPushButton:hover {\n"
    "	background-color: rgb(85, 170, 255);\n"
    "}")

            self.verticalLayout_4.addWidget(self.btn_page_2)

            self.btn_page_3 = QPushButton(self.frame_top_menus)
            self.btn_page_3.setObjectName(u"btn_page_3")
            self.btn_page_3.setCheckable(True)
            self.btn_page_3.clicked.connect(self.btn_page_3_onClick)
            self.btn_page_3.setMinimumSize(QSize(0, 40))
            self.btn_page_3.setStyleSheet(u"QPushButton {\n"
    "	color: rgb(255, 255, 255);\n"
    "	background-color: rgb(35, 35, 35);\n"
    "	border: 0px solid;\n"
    "}\n"
    "QPushButton:hover {\n"
    "	background-color: rgb(85, 170, 255);\n"
    "}")
            
            self.verticalLayout_4.addWidget(self.btn_page_3)

            self.btn_page_clientes = QPushButton(self.frame_top_menus)
            self.btn_page_clientes.setObjectName(u"btn_page_despesas")
            self.btn_page_clientes.setCheckable(True)
            self.btn_page_clientes.clicked.connect(self.despesas_onClick)
            self.btn_page_clientes.setMinimumSize(QSize(0, 40))
            self.btn_page_clientes.setStyleSheet(u"QPushButton {\n"
    "	color: rgb(255, 255, 255);\n"
    "	background-color: rgb(35, 35, 35);\n"
    "	border: 0px solid;\n"
    "}\n"
    "QPushButton:hover {\n"
    "	background-color: rgb(85, 170, 255);\n"
    "}")
            
            self.verticalLayout_4.addWidget(self.btn_page_clientes)

            self.btn_page_4 = QPushButton(self.frame_top_menus)
            self.btn_page_4.setObjectName(u"btn_page_4")
            self.btn_page_4.setCheckable(True)
            self.btn_page_4.clicked.connect(self.btn_page_4_onClick)
            self.btn_page_4.setMinimumSize(QSize(0, 40))
            self.btn_page_4.setStyleSheet(u"QPushButton {\n"
    "	color: rgb(255, 255, 255);\n"
    "	background-color: rgb(35, 35, 35);\n"
    "	border: 0px solid;\n"
    "}\n"
    "QPushButton:hover {\n"
    "	background-color: rgb(85, 170, 255);\n"
    "}")
            
            self.verticalLayout_4.addWidget(self.btn_page_4)

            self.btn_page_folha_ponto = QPushButton(self.frame_top_menus)
            self.btn_page_folha_ponto.setObjectName(u"btn_page_folha_ponto")
            self.btn_page_folha_ponto.setCheckable(True)
            self.btn_page_folha_ponto.clicked.connect(self.btn_page_folha_ponto_onClick)
            self.btn_page_folha_ponto.setMinimumSize(QSize(0, 40))
            self.btn_page_folha_ponto.setStyleSheet(u"QPushButton {\n"
    "	color: rgb(255, 255, 255);\n"
    "	background-color: rgb(35, 35, 35);\n"
    "	border: 0px solid;\n"
    "}\n"
    "QPushButton:hover {\n"
    "	background-color: rgb(85, 170, 255);\n"
    "}")
            
            self.verticalLayout_4.addWidget(self.btn_page_folha_ponto)

            

            self.btn_page_despesas = QPushButton(self.frame_top_menus)
            self.btn_page_despesas.setObjectName(u"btn_page_despesas")
            self.btn_page_despesas.setCheckable(True)
            self.btn_page_despesas.clicked.connect(self.onClick_despesas)
            self.btn_page_despesas.setMinimumSize(QSize(0, 40))
            self.btn_page_despesas.setStyleSheet(u"QPushButton {\n"
    "	color: rgb(255, 255, 255);\n"
    "	background-color: rgb(35, 35, 35);\n"
    "	border: 0px solid;\n"
    "}\n"
    "QPushButton:hover {\n"
    "	background-color: rgb(85, 170, 255);\n"
    "}")
            
            self.verticalLayout_4.addWidget(self.btn_page_despesas)

            ##########################################################################
            self.btn_page_relatorios = QPushButton(self.frame_top_menus)
            self.btn_page_relatorios.setObjectName(u"btn_page_relatorios")
            self.btn_page_relatorios.setCheckable(True)
            self.btn_page_relatorios.clicked.connect(self.onClick_page_relatorio)
            self.btn_page_relatorios.setMinimumSize(QSize(0, 40))
            self.btn_page_relatorios.setStyleSheet(u"QPushButton {\n"
    "	color: rgb(255, 255, 255);\n"
    "	background-color: rgb(35, 35, 35);\n"
    "	border: 0px solid;\n"
    "}\n"
    "QPushButton:hover {\n"
    "	background-color: rgb(85, 170, 255);\n"
    "}")
            
            self.verticalLayout_4.addWidget(self.btn_page_relatorios)


            self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


            self.horizontalLayout_2.addWidget(self.frame_left_menu)

            self.frame_pages = QFrame(self.Content)
            self.frame_pages.setObjectName(u"frame_pages")
            self.frame_pages.setFrameShape(QFrame.StyledPanel)
            self.frame_pages.setFrameShadow(QFrame.Raised)
            self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
            self.verticalLayout_5.setObjectName(u"verticalLayout_5")
            self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_5.setSpacing(0)
            self.frame_top_menu    = QFrame(self.frame_pages)
            self.frame_top_menu.setStyleSheet("background-color: rgb(40, 40, 40);")
            self.frame_top_menu.setMinimumSize(QSize(16777215, 60))
            self.verticalLayout_5.addWidget(self.frame_top_menu)
            
            self.horizontalLayout_12  = QHBoxLayout(self.frame_top_menu)
            self.horizontalLayout_12.setSpacing(0)
            self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
            
            self.stackedWidget = QStackedWidget(self.frame_pages)

            
            

            self.stackedWidget.setObjectName(u"stackedWidget")

            self.page_home = QWidget()
            self.page_home.setObjectName(u"page_home")
            
            self.frame_top         = QFrame(self.page_home)
            
            self.verticalLayout_home = QVBoxLayout(self.page_home)
            self.verticalLayout_home.setObjectName(u"verticalLayout_7")
            self.verticalLayout_home.setSpacing(0)
            self.verticalLayout_home.setContentsMargins(0, 0, 0, 0)

            self.label_logo = QLabel()
            self.label_logo.setStyleSheet("border-bottom: 1px solid; border-color: white;")
            self.label_logo.setMinimumSize(500, 500)
            w   = self.label_logo.width()
            h   = self.label_logo.height()
            self.pixmap     = QPixmap("assets\\logo.png")
            self.label_logo.setPixmap(self.pixmap.scaled(w, h, QtCore.Qt.KeepAspectRatio))
            
            
            self.verticalLayout_home.addWidget(self.label_logo, alignment=QtCore.Qt.AlignCenter)
            arq     = open('Version', 'r')
            version = arq.read()
            arq.close()
            self.label_version  = QLabel("Ver.: %s" % version)
            self.label_version.setStyleSheet("color: white;font-size: 17px;")
            self.verticalLayout_home.addWidget(self.label_version, alignment=QtCore.Qt.AlignCenter)
                
            font = QFont()
            font.setPointSize(40)
            
            

            self.stackedWidget.addWidget(self.page_home)

            self.page_1 = QWidget()
            self.page_1.setObjectName(u"page_1")
            self.frame_top         = QFrame(self.page_1)
            
            self.verticalLayout_7 = QVBoxLayout(self.page_1)
            self.verticalLayout_7.setObjectName(u"verticalLayout_7")
            self.verticalLayout_7.setSpacing(0)
            self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
            self.crud_buttons_2.add_user_btn.setText("Criar Cargo")
            self.crud_buttons_2.add_user_btn.clicked.connect(self.add_cargo_onClick)
            self.crud_buttons_2.edit_user_btn.setText("Editar Cargo")
            self.crud_buttons_2.edit_user_btn.clicked.connect(self.update_cargo)
            self.crud_buttons_2.del_user_btn.setText("Excluir Cargo")
            self.crud_buttons_2.del_user_btn.clicked.connect(self.exclude_cargo)
            
            self.horizontalLayout_12.addWidget(self.crud_buttons_2.add_user_btn)
            self.horizontalLayout_12.addWidget(self.crud_buttons_2.edit_user_btn)
            self.horizontalLayout_12.addWidget(self.crud_buttons_2.del_user_btn)

            

            self.verticalLayout_7.addWidget(self.cargos_list)

            
            
                
            font = QFont()
            font.setPointSize(40)
            
            

            self.stackedWidget.addWidget(self.page_1)

            ################################################################################################
            self.page_2 = QWidget()
            self.page_2.setObjectName(u"page_2")
            self.verticalLayout_6 = QVBoxLayout(self.page_2)
            self.verticalLayout_6.setObjectName(u"verticalLayout_6")
            self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_6.setSpacing(0)
            self.add_func   = self.crud_buttons.add_user_btn
            self.add_func.setText("Criar Func.")
            #self.crud_buttons.add_user_btn.setText("Criar Func.")
            self.add_func.clicked.connect(self.add_funcionario)
            self.crud_buttons.edit_user_btn.setText("Editar Func.")
            self.crud_buttons.edit_user_btn.clicked.connect(self.edit_funcionario)
            self.crud_buttons.del_user_btn.setText("Excluir Func.")
            self.crud_buttons.del_user_btn.clicked.connect(self.exclude_funcionario)
            self.horizontalLayout_12.addWidget(self.crud_buttons.add_user_btn)
            self.horizontalLayout_12.addWidget(self.crud_buttons.edit_user_btn)
            self.horizontalLayout_12.addWidget(self.crud_buttons.del_user_btn)
            
            self.verticalLayout_6.addWidget(self.func_box)
            self.stackedWidget.addWidget(self.page_2)

            ##################################################################################################
            self.page_3 = QWidget()
            self.page_3.setObjectName(u"page_1")
            self.frame_top         = QFrame(self.page_3)
            
            self.verticalLayout_8 = QVBoxLayout(self.page_3)
            self.verticalLayout_8.setObjectName(u"verticalLayout_7")
            self.verticalLayout_8.setSpacing(0)
            self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_8.addWidget(self.users_list)
            #self.verticalLayout_8.addWidget(self.users_list)
            

            self.add_user_btn = QPushButton()
            self.add_user_btn.hide()
            self.add_user_btn.setStyleSheet("margin-top: 5%; border-radius: 2px;background: rgb(85, 170, 255)")

            self.add_user_btn.setMaximumSize(QSize(100, 50))
            self.add_user_btn.clicked.connect(self.cadastro_de_usuario)
            self.add_user_btn.setText("Criar Usuário")
            self.add_user_btn.setCursor(QCursor(Qt.PointingHandCursor))

                #self.frame_icon_include_btn  = QFrame(self.add_user_btn)
            self.add_user_btn.setIcon(QIcon("assets\\add.png"))
            self.add_user_btn.setIconSize(QSize(25, 50))
            
            self.horizontalLayout_12.addWidget(self.add_user_btn)

            #######################################################################################################

            self.edit_user_btn = QPushButton()
            self.edit_user_btn.hide()
            self.edit_user_btn.setStyleSheet("margin-top: 5%; border-radius: 2px;background: rgb(85, 170, 255)")

            self.edit_user_btn.setMaximumSize(QSize(100, 50))
            self.edit_user_btn.clicked.connect(self.edit_user)
            self.edit_user_btn.setText("Editar Usuário")
            self.edit_user_btn.setCursor(QCursor(Qt.PointingHandCursor))

                #self.frame_icon_include_btn  = QFrame(self.edit_user_btn)
            self.edit_user_btn.setIcon(QIcon("assets\\edit.png"))
            self.edit_user_btn.setIconSize(QSize(25, 50))
            
            self.horizontalLayout_12.addWidget(self.edit_user_btn)

            #######################################################################################################

            self.del_user_btn = QPushButton()
            self.del_user_btn.hide()
            self.del_user_btn.setStyleSheet("margin-top: 5%; border-radius: 2px; background: #D22121;")

            self.del_user_btn.setMaximumSize(QSize(100, 50))
            self.del_user_btn.clicked.connect(self.del_user)
            self.del_user_btn.setText("Deletar Usuário")
            self.del_user_btn.setCursor(QCursor(Qt.PointingHandCursor))

                #self.frame_icon_include_btn  = QFrame(self.del_user_btn)
            self.del_user_btn.setIcon(QIcon("assets\\delete.png"))
            self.del_user_btn.setIconSize(QSize(25, 50))
            
            self.horizontalLayout_12.addWidget(self.del_user_btn)
            
            self.stackedWidget.addWidget(self.page_3)

            self.page_4 = QWidget()
            self.page_4.setObjectName(u"page_4")
            self.frame_top         = QFrame(self.page_4)
            
            self.crud_buttons_3.add_user_btn.setText("Adicionar Obra")
            self.crud_buttons_3.add_user_btn.clicked.connect(self.atrib_func)
            self.crud_buttons_3.edit_user_btn.setText("Editar Obra")
            self.crud_buttons_3.edit_user_btn.clicked.connect(self.edit_obra)
            self.crud_buttons_3.del_user_btn.setText("Excluir Obra")
            self.crud_buttons_3.del_user_btn.clicked.connect(self.del_obra)
            self.verticalLayout_page_4 = QVBoxLayout(self.page_4)
            self.verticalLayout_page_4.setObjectName(u"verticalLayout_7")
            self.verticalLayout_page_4.setSpacing(0)
            self.verticalLayout_page_4.setContentsMargins(0, 0, 0, 0)

            self.horizontalLayout_12.addWidget(self.crud_buttons_3.add_user_btn)
            self.horizontalLayout_12.addWidget(self.crud_buttons_3.edit_user_btn)
            self.horizontalLayout_12.addWidget(self.crud_buttons_3.del_user_btn)

            self.crud_buttons_teste.add_user_btn.setText("Salvar")
            self.horizontalLayout_12.addWidget(self.crud_buttons_teste.add_user_btn)
        
            self.crud_buttons_teste.add_user_btn.hide()
            
            self.verticalLayout_page_4.addWidget(self.folha_list)

            
            
                
            font = QFont()
            font.setPointSize(40)
            
            

            self.stackedWidget.addWidget(self.page_4)

            

            self.page_folha_ponto = QWidget()
            self.page_folha_ponto.setObjectName(u"page_folha_ponto")
            self.frame_top         = QFrame(self.page_folha_ponto)
            
            self.verticalLayout_page_folha_ponto = QVBoxLayout(self.page_folha_ponto)
            self.verticalLayout_page_folha_ponto.setObjectName(u"verticalLayout_7")
            self.verticalLayout_page_folha_ponto.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_page_folha_ponto.setSpacing(0)
            self.horizontalLayout_12.addWidget(self.crud_buttons_4.add_user_btn)
            self.horizontalLayout_12.addWidget(self.crud_buttons_4.edit_user_btn)
            self.horizontalLayout_12.addWidget(self.crud_buttons_4.del_user_btn)
            
            #self.verticalLayout_page_folha_ponto.addWidget(self.folha_list)
            
            
            #self.verticalLayout_page_folha_ponto.addWidget(Folha_Params().centralWidget)

            font = QFont()
            font.setPointSize(40)
            
            
            self.crud_buttons_5.add_user_btn.setText("Criar Folha")
            self.crud_buttons_5.edit_user_btn.setText("Editar Folha")
            self.crud_buttons_5.del_user_btn.setText("Excluir Folha")

            self.horizontalLayout_12.addWidget(self.crud_buttons_5.add_user_btn)
            self.horizontalLayout_12.addWidget(self.crud_buttons_5.edit_user_btn)
            self.horizontalLayout_12.addWidget(self.crud_buttons_5.del_user_btn)
            self.stackedWidget.addWidget(self.page_folha_ponto)

            self.verticalLayout_5.addWidget(self.stackedWidget)

            self.page_clientes = QWidget()
            self.page_clientes.setObjectName(u"page_5")
            self.frame_top         = QFrame(self.page_clientes)
            
            
            self.verticalLayout_page_5 = QVBoxLayout(self.page_clientes)
            self.verticalLayout_page_5.setObjectName(u"verticalLayout_7")
            self.verticalLayout_page_5.setSpacing(0)
            self.verticalLayout_page_5.setContentsMargins(0, 0, 0, 0)
            

            self.crud_buttons_6.add_user_btn.setText("Cad. Cliente")
            self.crud_buttons_6.add_user_btn.clicked.connect(self.add_cliente)
            self.crud_buttons_6.edit_user_btn.setText("Editar Cliente")
            self.crud_buttons_6.edit_user_btn.clicked.connect(self.edit_cliente)
            self.crud_buttons_6.del_user_btn.setText("Deletar Cliente")
            self.crud_buttons_6.del_user_btn.clicked.connect(self.delete_cliente)

            self.horizontalLayout_12.addWidget(self.crud_buttons_6.add_user_btn)
            self.horizontalLayout_12.addWidget(self.crud_buttons_6.edit_user_btn)
            self.horizontalLayout_12.addWidget(self.crud_buttons_6.del_user_btn)
            self.verticalLayout_page_5.addWidget(self.clientes_screen)

            self.stackedWidget.addWidget(self.page_clientes)

            self.page_despesas = QWidget()
            self.page_despesas.setObjectName(u"page_5")
            self.frame_top         = QFrame(self.page_despesas)
            
            
            self.verticalLayout_page_despesas = QVBoxLayout(self.page_despesas)
            self.verticalLayout_page_despesas.setObjectName(u"verticalLayout_7")
            self.verticalLayout_page_despesas.setSpacing(0)
            self.verticalLayout_page_despesas.setContentsMargins(0, 0, 0, 0)
            
            self.verticalLayout_page_despesas.addWidget(self.despesas_screen_list)
            self.crud_buttons_7.add_user_btn.setText("Adicionar Título")
            self.crud_buttons_7.add_user_btn.clicked.connect(self.add_despesa)
            self.crud_buttons_7.edit_user_btn.setText("Editar Título")
            self.crud_buttons_7.edit_user_btn.clicked.connect(self.edit_despesa)
            self.crud_buttons_7.del_user_btn.setText("Deletar Título")
            self.crud_buttons_7.del_user_btn.clicked.connect(self.del_despesa)

            self.horizontalLayout_12.addWidget(self.crud_buttons_7.add_user_btn)
            self.horizontalLayout_12.addWidget(self.crud_buttons_7.edit_user_btn)
            self.horizontalLayout_12.addWidget(self.crud_buttons_7.del_user_btn)
            #self.verticalLayout_page_despesas.addWidget(self.clientes_screen)

            self.stackedWidget.addWidget(self.page_despesas)
            #self.verticalLayout_page_5.addWidget(self.folha_list)

            
            

            


            self.horizontalLayout_2.addWidget(self.frame_pages)


            self.verticalLayout.addWidget(self.Content)

            self.setCentralWidget(self.centralwidget)

            self.retranslateUi(self)

            self.stackedWidget.setCurrentIndex(0)
            self.sql                = DB_Alter()

            QMetaObject.connectSlotsByName(self)
            #self.loading.close()
        except Exception as e:
            ErrorMessage(str(e)).message.exec_()

    def change_buttons_color(self):
        self.btn_page_home.setStyleSheet(u"QPushButton {\n"
        "	color: rgb(255, 255, 255);\n"
        "	background-color: rgb(35, 35, 35);\n"
        "	border: 0px solid;\n"
        "}\n"
        "QPushButton:hover {\n"
        "	background-color: rgb(85, 170, 255);\n"
        "}")

        self.btn_page_1.setStyleSheet(u"QPushButton {\n"
            "	color: rgb(255, 255, 255);\n"
            "	background-color: rgb(35, 35, 35);\n"
            "	border: 0px solid;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "}")

        self.btn_page_2.setStyleSheet(u"QPushButton {\n"
            "	color: rgb(255, 255, 255);\n"
            "	background-color: rgb(35, 35, 35);\n"
            "	border: 0px solid;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "}")

        self.btn_page_3.setStyleSheet(u"QPushButton {\n"
            "	color: rgb(255, 255, 255);\n"
            "	background-color: rgb(35, 35, 35);\n"
            "	border: 0px solid;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "}")

        self.btn_page_4.setStyleSheet(u"QPushButton {\n"
            "	color: rgb(255, 255, 255);\n"
            "	background-color: rgb(35, 35, 35);\n"
            "	border: 0px solid;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "}")

        self.btn_page_folha_ponto.setStyleSheet(u"QPushButton {\n"
            "	color: rgb(255, 255, 255);\n"
            "	background-color: rgb(35, 35, 35);\n"
            "	border: 0px solid;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "}")

        self.btn_page_clientes.setStyleSheet(u"QPushButton {\n"
            "	color: rgb(255, 255, 255);\n"
            "	background-color: rgb(35, 35, 35);\n"
            "	border: 0px solid;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "}")

        self.btn_page_despesas.setStyleSheet(u"QPushButton {\n"
            "	color: rgb(255, 255, 255);\n"
            "	background-color: rgb(35, 35, 35);\n"
            "	border: 0px solid;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "}")

        self.btn_page_relatorios.setStyleSheet(u"QPushButton {\n"
            "	color: rgb(255, 255, 255);\n"
            "	background-color: rgb(35, 35, 35);\n"
            "	border: 0px solid;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "}")

    def home_screen(self):
        self.change_buttons_color()
        self.btn_page_home.setStyleSheet(u"QPushButton {\n"
    "	color: rgb(255, 255, 255);\n"
    "	background-color: rgb(85, 170, 255);\n"
    "	border: 0px solid;\n"
    "}\n"
    "QPushButton:hover {\n"
    "	background-color: rgb(85, 170, 255);\n"
    "}")
        self.add_user_btn.hide()
        self.edit_user_btn.hide()
        self.del_user_btn.hide()
        self.crud_buttons_teste.add_user_btn.hide()
        self.crud_buttons.add_user_btn.hide()
        self.crud_buttons.edit_user_btn.hide()
        self.crud_buttons.del_user_btn.hide()

        self.crud_buttons_2.add_user_btn.hide()
        self.crud_buttons_2.edit_user_btn.hide()
        self.crud_buttons_2.del_user_btn.hide()

        self.crud_buttons_3.add_user_btn.hide()
        self.crud_buttons_3.edit_user_btn.hide()
        self.crud_buttons_3.del_user_btn.hide()

        self.crud_buttons_4.add_user_btn.hide()
        self.crud_buttons_4.edit_user_btn.hide()
        self.crud_buttons_4.del_user_btn.hide()

        self.crud_buttons_5.add_user_btn.hide()
        self.crud_buttons_5.edit_user_btn.hide()
        self.crud_buttons_5.del_user_btn.hide()
        
        self.crud_buttons_6.add_user_btn.hide()
        self.crud_buttons_6.edit_user_btn.hide()
        self.crud_buttons_6.del_user_btn.hide()

        self.crud_buttons_7.add_user_btn.hide()
        self.crud_buttons_7.edit_user_btn.hide()
        self.crud_buttons_7.del_user_btn.hide()

    def cadastro_de_usuario(self):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
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
        self.input_user.setStyleSheet("background-color: white; margin-left: 12px; margin-top: 10px;border-radius: 2px;")
        self.input_user.setMinimumSize(QSize(230, 38))
        self.input_user.textChanged.connect(self.handle_user)
        self.frame_input_2  = QFrame(self.frame_2_cadastro_fFrame)
        self.input_name     = QLineEdit(self.frame_input_2)
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
        self.sub_button.setText("Salvar")
        
        self.sub_button.setStyleSheet("""
        background-color: rgb(201, 198, 177);
        margin-left: 80%;
        font-size: 17px;
        
        """)
        self.sub_button.clicked.connect(self.click)
        self.sub_button.setMinimumSize(QSize(360, 30))
        self.sub_button.setCursor(Qt.PointingHandCursor)
        
        QApplication.restoreOverrideCursor()
        self.dlg.exec_()
    
    def handle_user(self, text):
        self.user   = text
    
    def handle_name(self, text):
        self.name   = text
    
    def handle_password(self, text):
        self.password   = text
    
    def click(self):
        q   = queue.Queue()
        t1  = threading.Thread(target=self.sql.add_user, args=(self.user, self.name, self.password, self.comboBox.currentIndex(), q, ))
        t3  = threading.Thread(target=self.close())
        t3.start()
        
        t1.start()
        t1.join()
        t3.join()
        for i in reversed(range(self.verticalLayout_8.count())):
                self.verticalLayout_8.itemAt(i).widget().setParent(None)
        self.users_list = Window(q.get())
        self.verticalLayout_8.addWidget(self.users_list)
        self.verticalLayout_8.update()
        
        self.sql                = DB_Alter()
        
    def close(self):
        self.dlg.close()

    def btn_page_3_onClick(self):

        self.change_buttons_color()
        self.btn_page_3.setStyleSheet(u"QPushButton {\n"
    "	color: rgb(255, 255, 255);\n"
    "	background-color: rgb(85, 170, 255);\n"
    "	border: 0px solid;\n"
    "}\n"
    "QPushButton:hover {\n"
    "	background-color: rgb(85, 170, 255);\n"
    "}")
        self.add_user_btn.show()
        self.edit_user_btn.show()
        self.del_user_btn.show()
        self.crud_buttons_teste.add_user_btn.hide()
        self.crud_buttons.add_user_btn.hide()
        self.crud_buttons.edit_user_btn.hide()
        self.crud_buttons.del_user_btn.hide()

        self.crud_buttons_3.add_user_btn.hide()
        self.crud_buttons_3.edit_user_btn.hide()
        self.crud_buttons_3.del_user_btn.hide()

        self.crud_buttons_2.add_user_btn.hide()
        self.crud_buttons_2.edit_user_btn.hide()
        self.crud_buttons_2.del_user_btn.hide()

        self.crud_buttons_5.add_user_btn.hide()
        self.crud_buttons_5.edit_user_btn.hide()
        self.crud_buttons_5.del_user_btn.hide()

        self.crud_buttons_4.add_user_btn.hide()
        self.crud_buttons_4.edit_user_btn.hide()
        self.crud_buttons_4.del_user_btn.hide()

        self.crud_buttons_6.add_user_btn.hide()
        self.crud_buttons_6.edit_user_btn.hide()
        self.crud_buttons_6.del_user_btn.hide()

        self.crud_buttons_7.add_user_btn.hide()
        self.crud_buttons_7.edit_user_btn.hide()
        self.crud_buttons_7.del_user_btn.hide()
        #self.verticalLayout_8.addWidget(Window(self.users))

    def add_funcionario(self):

        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.add_func   = Window_Add_Func()
        
        self.funcoes    = Funcoes()
        self.sql        = SQL_Funcionario()
        
        
    
        self.add_func.name_input.textChanged.connect(self.function.handle_name)
        self.add_func.cpf_input.textChanged.connect(self.function.handle_cpf)
        self.add_func.RG_input.textChanged.connect(self.function.handle_rg)
        self.add_func.salario_input.textChanged.connect(self.function.handle_salario_hora)
        self.add_func.Data_nascimento_input.dateChanged.connect(self.function.handle_data_nascimento)

        funcoes = self.funcoes.return_funcoes()
        if(funcoes == False):
            message = QMessageBox()
            message.setIcon(QMessageBox.Critical)
            message.setText("É necessário cadastrar um cargo primeiro!")
            message.setWindowTitle("ERROR")
            QApplication.restoreOverrideCursor()
            message.exec_()
            self.crud_buttons_3.add_user_btn.setChecked(False)
            self.crud_buttons.add_user_btn.setChecked(False)
            self.crud_buttons_2.add_user_btn.click()
        else:
            
            for x in self.funcoes.return_funcoes():
                self.add_func.funcao_input.addItem(x[0])
            
            
            self.function.handle_funcao(self.add_func.funcao_input.currentText(), self.funcoes.return_funcoes())
            self.add_func.funcao_input.currentTextChanged.connect(lambda: self.function.handle_funcao(
                self.add_func.funcao_input.currentText(),
                self.funcoes.return_funcoes()
            ))
            
                
            self.add_func.Email_input.textChanged.connect(self.function.handle_email)
            self.add_func.Telefone_input.textChanged.connect(self.function.handle_telefone)
            self.add_func.Horas_Trab_Dia_input.timeChanged.connect(self.function.handle_horas_trabalhadas)
            self.add_func.sub_button.clicked.connect(lambda: self.function.add_user_(self.add_func.dlg, self.refresh))
            QApplication.restoreOverrideCursor()
            self.add_func.dlg.exec_()

            #self.refresh()
    
    def edit_funcionario(self):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.funcoes    = Funcoes()
        self.sql_func       = SQL_Funcionario()
        c   = Confirmation_Screen()
        if(len(self.func_box.check_box_func()) == 0):
            
            QApplication.restoreOverrideCursor()
            c.show_confirmation(
                """Nenhum funcionário selecionado para edição!""",
                onlyText=True
            )
        elif(len(self.func_box.check_box_func()) > 1):
            QApplication.restoreOverrideCursor()
            c.show_confirmation(
                """Só é permitida a edição de um funcionário!""",
                onlyText=True
            )
        else:

            user_data   = self.sql_func.return_users_data(self.func_box.check_box_func()[0])
            
            self.function   = Functions(self.func_box.check_box_func()[0])
            cargos  = self.funcoes.return_funcoes()
            edit_func   = Edit_Func(user_data)
            for x in cargos:
                if(x[1] == user_data[0][9]):
                    edit_func.dialog.funcao_input.addItem(str(x[0]))
            
            for x in cargos:
                if(x[1] == user_data[0][9]):
                    pass
                else:
                    edit_func.dialog.funcao_input.addItem(str(x[0]))
            
            edit_func.dialog.name_input.setText(user_data[0][1])
            edit_func.dialog.name_input.textChanged.connect(self.function.handle_name)
            edit_func.dialog.cpf_input.setText(user_data[0][2])
            edit_func.dialog.cpf_input.textChanged.connect(self.function.handle_cpf)
            edit_func.dialog.RG_input.setText(user_data[0][3])
            edit_func.dialog.RG_input.textChanged.connect(self.function.handle_rg)
            
            #edit_func.dialog.salario_input.setText(user_data[0][4])
            edit_func.dialog.salario_input.textChanged.connect(self.function.handle_salario_hora)

            try:
                data    = datetime.strptime(str(user_data[0][5]), "%Y-%m-%d %H:%M:%S")
                qdate   = QDate(int(data.strftime("%Y")), int(data.strftime("%m")), int(data.strftime("%d")))
                edit_func.dialog.Data_nascimento_input.setDate(qdate)
            except Exception as e:
                pass
            edit_func.dialog.Data_nascimento_input.dateChanged.connect(self.function.handle_data_nascimento)

            
            self.function.handle_funcao(edit_func.dialog.funcao_input.currentText(), self.funcoes.return_funcoes())
            edit_func.dialog.funcao_input.currentTextChanged.connect(lambda: self.function.handle_funcao(
                edit_func.dialog.funcao_input.currentText(),
                self.funcoes.return_funcoes()
            ))
            
            
            edit_func.dialog.Email_input.setText(user_data[0][6])
            edit_func.dialog.Email_input.textChanged.connect(self.function.handle_email)
            edit_func.dialog.Telefone_input.setText(user_data[0][7])
            edit_func.dialog.Telefone_input.textChanged.connect(self.function.handle_telefone)
            try:
                time    = datetime.strptime(str(user_data[0][8]), "%H:%M:%S")
                qtime   = QTime(int(time.strftime("%H")), int(time.strftime("%M")), int(time.strftime("%S")))
                edit_func.dialog.Horas_Trab_Dia_input.setTime(qtime)
            except Exception as e:
                pass
            edit_func.dialog.Horas_Trab_Dia_input.timeChanged.connect(self.function.handle_horas_trabalhadas)
            edit_func.dialog.sub_button.clicked.connect(lambda: self.function.edit_funcionario(edit_func.dialog.dlg, self.refresh))
            QApplication.restoreOverrideCursor()
            edit_func.dialog.dlg.exec_()
        
    
    def exclude_funcionario(self):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.functions  = Functions()
        c   = Confirmation_Screen()
        reg_selecionados    = len(self.func_box.check_box_func())

        if(reg_selecionados == 0):
            QApplication.restoreOverrideCursor()
            c.show_confirmation(
                """Nenhum funcionário selecionado para exclusão""",
                onlyText=True
            )
        else:
            
            c.confirm_btn.clicked.connect(lambda: self.functions.exclude_func(
                c.dialog,
                self.func_box.check_box_func(),
                self.refresh
            ))
            QApplication.restoreOverrideCursor()
            c.show_confirmation(
                """Deseja excluir %s registros de Funcionários?""" % reg_selecionados,
                btn=True
            )
            

    def refresh(self):
        #threading.Thread(target=main_loading()).start()
        self.func_box   = Func_Window(SQL_Funcionario().return_all_funcs())
        for x in reversed(range(self.verticalLayout_6.count())):
            self.verticalLayout_6.itemAt(x).widget().setParent(None)
        self.verticalLayout_6.addWidget(self.func_box)
        self.verticalLayout_6.update()
        

    def btn_page_2_func(self):
        self.change_buttons_color()
        self.btn_page_2.setStyleSheet(u"QPushButton {\n"
    "	color: rgb(255, 255, 255);\n"
    "	background-color: rgb(85, 170, 255);\n"
    "	border: 0px solid;\n"
    "}\n"
    "QPushButton:hover {\n"
    "	background-color: rgb(85, 170, 255);\n"
    "}")
        #dialog  = QDialog()
        ##LoadignScreen(dialog)
        #dialog.show()
        self.add_user_btn.hide()
        self.edit_user_btn.hide()
        self.del_user_btn.hide()

        self.crud_buttons_3.add_user_btn.hide()
        self.crud_buttons_3.edit_user_btn.hide()
        self.crud_buttons_3.del_user_btn.hide()
        self.crud_buttons_teste.add_user_btn.hide()
        self.crud_buttons.add_user_btn.show()
        self.crud_buttons.edit_user_btn.show()
        self.crud_buttons.del_user_btn.show()

        self.crud_buttons_2.add_user_btn.hide()
        self.crud_buttons_2.edit_user_btn.hide()
        self.crud_buttons_2.del_user_btn.hide()

        self.crud_buttons_5.add_user_btn.hide()
        self.crud_buttons_5.edit_user_btn.hide()
        self.crud_buttons_5.del_user_btn.hide()

        self.crud_buttons_6.add_user_btn.hide()
        self.crud_buttons_6.edit_user_btn.hide()
        self.crud_buttons_6.del_user_btn.hide()

        self.crud_buttons_7.add_user_btn.hide()
        self.crud_buttons_7.edit_user_btn.hide()
        self.crud_buttons_7.del_user_btn.hide()

        #self.loading.dialog.show()
        #self.hide()
        #self.verticalLayout_6_widget()
        #self.loading.stopAnimation()
        #self.showMaximized()
        #self.loading.close()
        #self.verticalLayout_6.addWidget(Func_Window(SQL_Funcionario().return_all_funcs()))

    def verticalLayout_6_widget(self):
        self.verticalLayout_6.addWidget(Func_Window(self.funcs))
    
    def del_user(self):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        c   = Confirmation_Screen()
        reg_selecionados    = len(self.users_list.check_box_func())

        if(reg_selecionados == 0):
            QApplication.restoreOverrideCursor()
            c.show_confirmation(
                """Nenhum usuário selecionado para exclusão""",
                onlyText=True
            )
        else:
            QApplication.restoreOverrideCursor()
            c.show_confirmation(
                "Deseja excluir %s registros de usuários?" % reg_selecionados, 
                list=self.users_list.check_box_func(),
                user=True,
                refresh_1=self.refresh_users_screen
            )

    def edit_user(self):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        c   = Confirmation_Screen()
        if(len(self.users_list.check_box_func()) == 0):
            QApplication.restoreOverrideCursor()
            c.show_confirmation("Nenhum usuário selecionado!", onlyText=True)
        elif(len(self.users_list.check_box_func()) > 1):
            QApplication.restoreOverrideCursor()
            c.show_confirmation("Para edição, só é possível a seleção de um usuário!", onlyText=True)
        else:
            QApplication.restoreOverrideCursor()
            id  = self.users_list.check_box_func()[0]
            self.sql                = DB_Alter()
            user_data   = self.sql.user_data(id)
            
            FrameBox().frame_box(user_data[0], user_data[1], user_data[2], id, self.refresh_users_screen)
 
    def btn_page_1_onClick(self):
        self.change_buttons_color()
        self.btn_page_1.setStyleSheet(u"QPushButton {\n"
    "	color: rgb(255, 255, 255);\n"
    "	background-color: rgb(85, 170, 255);\n"
    "	border: 0px solid;\n"
    "}\n"
    "QPushButton:hover {\n"
    "	background-color: rgb(85, 170, 255);\n"
    "}")
        self.add_user_btn.hide()
        self.edit_user_btn.hide()
        self.del_user_btn.hide()

        self.crud_buttons.add_user_btn.hide()
        self.crud_buttons_teste.add_user_btn.hide()
        self.crud_buttons.edit_user_btn.hide()
        self.crud_buttons.del_user_btn.hide()

        self.crud_buttons_3.add_user_btn.hide()
        self.crud_buttons_3.edit_user_btn.hide()
        self.crud_buttons_3.del_user_btn.hide()
        self.crud_buttons_2.add_user_btn.show()
        self.crud_buttons_2.edit_user_btn.show()
        self.crud_buttons_2.del_user_btn.show()

        self.crud_buttons_5.add_user_btn.hide()
        self.crud_buttons_5.edit_user_btn.hide()
        self.crud_buttons_5.del_user_btn.hide()

        self.crud_buttons_6.add_user_btn.hide()
        self.crud_buttons_6.edit_user_btn.hide()
        self.crud_buttons_6.del_user_btn.hide()

        self.crud_buttons_7.add_user_btn.hide()
        self.crud_buttons_7.edit_user_btn.hide()
        self.crud_buttons_7.del_user_btn.hide()

    def add_cargo_onClick(self):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.add_cargo  = Add_Cargo()
        self.add_cargo.name_input.textChanged.connect(self.cargos_funcoes.handle_descricao)
        
        self.add_cargo.sub_button.clicked.connect(lambda: self.cargos_funcoes.cargo_submit(self.add_cargo.dlg, self.refresh_cargos_screen, self.refresh, self.hide_self_screen))
        QApplication.restoreOverrideCursor()
        self.add_cargo.dlg.exec_()
    
    def hide_self_screen(self):
        self.hide()
        #self.refresh_cargos_screen() 
        #self.refresh()
                
    def exclude_cargo(self):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        c   = Confirmation_Screen()
        self.funcao         = Cargos()
        reg_selecionados    = len(self.cargos_list.check_box_func())

        if(reg_selecionados == 0):
            QApplication.restoreOverrideCursor()
            c.show_confirmation(
                """Nenhum cargo selecionado para exclusão""",
                onlyText=True
            )
        else:
            QApplication.restoreOverrideCursor()
            c.confirm_btn.clicked.connect(lambda: self.funcao.del_cargos(
                c.dialog,
                self.cargos_list.check_box_func(),
                self.refresh_cargos_screen,
                self.refresh

            ))
            c.show_confirmation(
                "Deseja excluir %s registros de cargos?" % reg_selecionados, 
                btn=True
            )

    def update_cargo(self):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        c   = Confirmation_Screen()
        if(len(self.cargos_list.check_box_func()) > 1):
            QApplication.restoreOverrideCursor()
            c.show_confirmation(
                """Só é possivel a seleção para edição de apenas um cargo por vez!""",
                onlyText=True
            )
        elif(len(self.cargos_list.check_box_func()) == 0):
            QApplication.restoreOverrideCursor()
            c.show_confirmation(
                """Nenhum cargo selecionado para edição!""",
                onlyText=True
            )
        else:
            
            self.cargos_funcoes = Cargos(id=str(self.cargos_list.check_box_func()[0]))
            edit_cargo_dialog   = Edit_Cargo(Funcoes().return_funcao_data(str(self.cargos_list.check_box_func()[0])))
            edit_cargo_dialog.dialog.name_input.textChanged.connect(self.cargos_funcoes.handle_descricao)
            edit_cargo_dialog.dialog.sub_button.clicked.connect(lambda: self.cargos_funcoes.edit_cargo(edit_cargo_dialog.dialog.dlg, self.refresh_cargos_screen, self.refresh))
            
            #self.edit_cargo_dialog.dialog.sub_button.clicked.connect(lambda: self.cargos_funcoes.edit_cargo(self.dialog.dlg))
            QApplication.restoreOverrideCursor()
            edit_cargo_dialog.dialog.dlg.exec_()
            
    def refresh_cargos_screen(self):
        
        self.cargos_funcoes = Cargos()
        self.refresh_list   = self.cargos_funcoes.refresh_list()
        
        self.cargos_list    = Cargos_List(self.refresh_list)
        for x in reversed(range(self.verticalLayout_7.count())):
            self.verticalLayout_7.itemAt(x).widget().setParent(None)
        
        self.verticalLayout_7.addWidget(self.cargos_list)
        self.verticalLayout_7.update()
        

    def refresh_users_screen(self):

        self.users_list = Window(DB_Login().return_all_users())
        for x in reversed(range(self.verticalLayout_8.count())):
            self.verticalLayout_8.itemAt(x).widget().setParent(None)
        self.verticalLayout_8.addWidget(self.users_list)
        self.verticalLayout_8.update()

    def btn_page_4_onClick(self):

        self.change_buttons_color()
        self.btn_page_4.setStyleSheet(u"QPushButton {\n"
    "	color: rgb(255, 255, 255);\n"
    "	background-color: rgb(85, 170, 255);\n"
    "	border: 0px solid;\n"
    "}\n"
    "QPushButton:hover {\n"
    "	background-color: rgb(85, 170, 255);\n"
    "}")
        self.add_user_btn.hide()
        self.edit_user_btn.hide()
        self.del_user_btn.hide()
         
        self.crud_buttons_3.add_user_btn.show()
        self.crud_buttons_3.edit_user_btn.show()
        self.crud_buttons_3.del_user_btn.show()
        
        self.crud_buttons_6.add_user_btn.hide()
        self.crud_buttons_6.edit_user_btn.hide()
        self.crud_buttons_6.del_user_btn.hide()

        self.add_user_btn.hide()
        self.edit_user_btn.hide()
        self.del_user_btn.hide()

        self.crud_buttons.add_user_btn.hide()
        self.crud_buttons_teste.add_user_btn.hide()
        self.crud_buttons.edit_user_btn.hide()
        self.crud_buttons.del_user_btn.hide()

        self.crud_buttons_2.add_user_btn.hide()
        self.crud_buttons_2.edit_user_btn.hide()
        self.crud_buttons_2.del_user_btn.hide()

        self.crud_buttons_5.add_user_btn.hide()
        self.crud_buttons_5.edit_user_btn.hide()
        self.crud_buttons_5.del_user_btn.hide()

        self.crud_buttons_7.add_user_btn.hide()
        self.crud_buttons_7.edit_user_btn.hide()
        self.crud_buttons_7.del_user_btn.hide()

    def atrib_func(self):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.add_obra    = Add_Obra()
        self.type       = "obra"
        self.clientes_functions = Clientes()
        clientes    = self.clientes_functions.refresh()
        if(clientes == False):
            message = QMessageBox()
            message.setIcon(QMessageBox.Critical)
            message.setText("É necessário cadastrar um cliente primeiro!")
            message.setWindowTitle("ERROR")
            QApplication.restoreOverrideCursor()
            message.exec_()
            self.crud_buttons_3.add_user_btn.setChecked(False)
            self.crud_buttons_6.add_user_btn.click()
        else:
            for x in self.clientes_functions.refresh():
                texto = "{} - {}".format(x[1], x[2])
                self.add_obra.input_cliente.addItem(texto)
            self.functions  = Obras_Functions()
            self.add_obra_screen = Atrib_Func_Screen()
            if(self.add_obra_screen.return_data == False):
                pass
            else:
                self.add_obra.verticalLayout_frame_5.addWidget(self.add_obra_screen)
                self.add_obra.dlg.show()
                self.add_obra.name_input.textChanged.connect(self.functions.handle_descricao)
                self.add_obra.input_data.dateChanged.connect(self.functions.handle_data)
                self.add_obra.sub_button.clicked.connect(lambda: self.functions.add_obra(self.add_obra_screen.check_box_func(), self.add_obra.dlg, self.refresh_folha_screen, self.add_obra.input_cliente.currentText()))
                QApplication.restoreOverrideCursor()
                self.add_obra.dlg.exec_()
                #self.refresh_folha_screen()
                self.crud_buttons_5.add_user_btn.hide()
                self.crud_buttons_5.edit_user_btn.hide()
                self.crud_buttons_5.del_user_btn.hide()
        
    def edit_obra(self):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        obra_selected   = self.folha_list.check_box_func()
        c   = Confirmation_Screen()

        if(len(obra_selected) == 0 or len(obra_selected) > 1):
            QApplication.restoreOverrideCursor()
            c.show_confirmation(
                "Só é permitida a edição de uma obra por vez!",
                onlyText=True
            )
        else:
            QApplication.restoreOverrideCursor()
            self.add_obra   = Add_Obra()
            self.add_obra.dlg.setWindowTitle("Edição de Obra")
            
            self.functions          = Obras_Functions()
            self.add_obra_screen    = Atrib_Func_Screen(edited=True, id_obra=obra_selected[0])
            self.clientes_functions = Clientes()
            for x in self.clientes_functions.refresh():
                texto = "{} - {}".format(x[1], x[2])
                self.add_obra.input_cliente.addItem(texto)
            
            selected_func           = self.add_obra_screen.check_box_func()
            db_response             = self.functions.return_obra_data(obra_selected[0])
            if(db_response[0][2] == None):
                pass
            else:
                data    = datetime.strptime(str(db_response[0][2]), "%Y-%m-%d %H:%M:%S")
                qdate   = QDate(int(data.strftime("%Y")), int(data.strftime("%m")), int(data.strftime("%d")))
                self.add_obra.input_data.setDate(qdate)
                self.add_obra.data = data
            
            self.add_obra.input_data.dateChanged.connect(self.functions.handle_data)
            self.add_obra.verticalLayout_frame_5.addWidget(self.add_obra_screen)
            self.add_obra.dlg.show()
            self.add_obra.name_input.textChanged.connect(self.functions.handle_descricao)
            self.add_obra.name_input.setText(
                self.add_obra_screen.descricao[0][0]
            )
            self.functions.edited(db_response)
            self.add_obra.sub_button.clicked.connect(lambda: self.functions.edit_obra(
                self.add_obra_screen.check_box_func(), 
                self.add_obra_screen.funcs,
                self.add_obra.dlg,
                self.refresh_folha_screen,
                obra_selected[0],
                self.refresh_folha_screen,
                self.add_obra.input_cliente.currentText()
            ))
            QApplication.restoreOverrideCursor()
            self.add_obra.dlg.exec_()
            self.crud_buttons_5.add_user_btn.hide()
            self.crud_buttons_5.edit_user_btn.hide()
            self.crud_buttons_5.del_user_btn.hide()

    
    def del_obra(self):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.functions  = Obras_Functions()
        
        c               = Confirmation_Screen()

        selected_id     = self.folha_list.check_box_func()

        if(len(selected_id) == 0):
            QApplication.restoreOverrideCursor()
            c.show_confirmation(
                """Nenhuma obra selecionada para exclusão!""",
                True
            )
        else:
            
            c.confirm_btn.clicked.connect(lambda: self.functions.del_obra(selected_id, c.dialog, self.refresh_folha_screen))
            QApplication.restoreOverrideCursor()
            c.show_confirmation(
                """Deseja excluir %s registros de Obras?""" % len(selected_id),
                btn=True
            )
            
        

    def btn_page_folha_ponto_onClick(self):
        
        self.change_buttons_color()
        self.btn_page_folha_ponto.setStyleSheet(u"QPushButton {\n"
    "	color: rgb(255, 255, 255);\n"
    "	background-color: rgb(85, 170, 255);\n"
    "	border: 0px solid;\n"
    "}\n"
    "QPushButton:hover {\n"
    "	background-color: rgb(85, 170, 255);\n"
    "}")
        self.add_user_btn.hide()
        self.edit_user_btn.hide()
        self.del_user_btn.hide()

        self.crud_buttons.add_user_btn.hide()
        self.crud_buttons.edit_user_btn.hide()
        try:
            self.crud_buttons_teste.add_user_btn.hide()
        except Exception as e:
            pass
        self.crud_buttons.del_user_btn.hide()

        self.crud_buttons_2.add_user_btn.hide()
        self.crud_buttons_2.edit_user_btn.hide()
        self.crud_buttons_2.del_user_btn.hide()

        self.crud_buttons_3.add_user_btn.hide()
        self.crud_buttons_3.edit_user_btn.hide()
        self.crud_buttons_3.del_user_btn.hide()

        self.crud_buttons_4.add_user_btn.hide()
        self.crud_buttons_4.edit_user_btn.hide()
        self.crud_buttons_4.del_user_btn.hide()

        self.crud_buttons_5.add_user_btn.show()
        self.crud_buttons_5.add_user_btn.clicked.connect(self.create_folha)
        self.crud_buttons_5.edit_user_btn.show()
        self.crud_buttons_5.edit_user_btn.clicked.connect(self.edit_folha)
        self.crud_buttons_5.del_user_btn.show()
        self.crud_buttons_5.del_user_btn.clicked.connect(self.delete_folha)

        self.crud_buttons_6.add_user_btn.hide()
        self.crud_buttons_6.edit_user_btn.hide()
        self.crud_buttons_6.del_user_btn.hide()

        self.crud_buttons_7.add_user_btn.hide()
        self.crud_buttons_7.edit_user_btn.hide()
        self.crud_buttons_7.del_user_btn.hide()

        
        self.refresh_folha_screen()
        self.cont_folha = 0
        self.crud_buttons_5.add_user_btn.show()
        self.crud_buttons_5.add_user_btn.clicked.connect(self.create_folha)
        self.crud_buttons_5.edit_user_btn.show()
        self.crud_buttons_5.edit_user_btn.clicked.connect(self.edit_folha)
        self.crud_buttons_5.del_user_btn.show()
        self.crud_buttons_5.del_user_btn.clicked.connect(self.delete_folha)
        
        
    def create_folha(self):
        
        if(self.cont_folha == 0):
            self.cont_folha += 1
            QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
            self.obras  = Obras_Functions().refresh()
            self.folha_ponto    = Folha_Params()
            self.folha_ponto.data_Inicial_input.dateChanged.connect(self.data_inicial)
            self.folha_ponto.Data_final_input.dateChanged.connect(self.data_final)
            if(self.obras == False):
                QApplication.restoreOverrideCursor()
                self.btn_page_4.click()
                ErrorMessage("Nenhuma obra cadastrada, cadastre uma obra para poder criar uma folha de ponto!").message.exec_()
                    
            else:
                for x in self.obras:
                    self.folha_ponto.obra_input.addItem(x[1])

                self.folha_ponto.sub_button.clicked.connect(lambda: self.ponto_folha_submit(self.folha_ponto.dialog))
                QApplication.restoreOverrideCursor()
                
                self.folha_ponto.dialog.exec_()
                QApplication.restoreOverrideCursor()
                self.crud_buttons_5.add_user_btn.setChecked(False)
                
        
            
    def adc_folha_ponto(self):
        pass
    
    def data_inicial(self, text):
        self.data_inicial_folha = datetime.strptime(str(text.day())+"-"+str(text.month())+"-"+str(text.year()), "%d-%m-%Y")

    def data_final(self, text):
        self.data_final_folha = datetime.strptime(str(text.day())+"-"+str(text.month())+"-"+str(text.year()), "%d-%m-%Y")

    def ponto_folha_submit(self, screen):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.obras  = Obras_Functions().refresh()
        
        self.crud_buttons_5.add_user_btn.setChecked(False)
        #QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        if(self.verticalLayout_page_folha_ponto.count() > 0):
            for x in range(self.verticalLayout_page_folha_ponto.count()):
                self.verticalLayout_page_folha_ponto.itemAt(x).widget().setParent(None)

        self.functions = Folha_Ponto_Function()
        self.obra_escolhida = self.obras[self.folha_ponto.obra_input.currentIndex()][0]
        if(self.folha_ponto.check_box.isChecked()):
            screen.close()
            QApplication.restoreOverrideCursor()
            self.table  = QTable(
                self.data_inicial_folha.strftime("%d-%m-%Y"), 
                self.data_final_folha.strftime("%d-%m-%Y"),
                self.functions.return_func_obra(
                    self.obra_escolhida, 
                    True,
                    self.data_inicial_folha.strftime("%Y%m%d"), 
                    self.data_final_folha.strftime("%Y%m%d")
                ),
                True
            )
        else:
            QApplication.restoreOverrideCursor()
            screen.close()
            self.table  = QTable(
                self.data_inicial_folha.strftime("%d-%m-%Y"), 
                self.data_final_folha.strftime("%d-%m-%Y"),
                self.functions.return_func_obra(self.obra_escolhida)
            )

            message = QMessageBox()
            message.setWindowTitle("ARX Sistemas")

            self.type   = "folha"
            self.crud_buttons_5.add_user_btn.hide()
            self.crud_buttons_5.edit_user_btn.hide()
            self.crud_buttons_5.del_user_btn.hide()
            
            self.crud_buttons_teste.add_user_btn.show()
            
            self.crud_buttons_teste.add_user_btn.clicked.connect(lambda: self.functions.add_values(self.table.array, message))
        
        self.verticalLayout_page_folha_ponto.addWidget(self.table.dialog)
        
        
        self.verticalLayout_page_folha_ponto.update()
        #QApplication.restoreOverrideCursor()

    def delete_folha(self):
        if(self.cont_folha_del == 0):
            self.cont_folha_del += 1
            try:
                QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
                self.functions  = Folha_Ponto_Function()
                
                c               = Confirmation_Screen()

                selected_id     = self.Lista_De_Folha.check_box_func()
                if(len(selected_id) == 0):
                    QApplication.restoreOverrideCursor()
                    c.show_confirmation(
                        """Nenhuma obra selecionada para exclusão!""",
                        True
                    )
                else:
                    
                    c.confirm_btn.clicked.connect(lambda: self.functions.del_folha(selected_id, c.dialog, self.refresh_folha_screen))
                    QApplication.restoreOverrideCursor()
                    c.show_confirmation(
                        """Deseja excluir %s registros de Obras?""" % len(selected_id),
                        btn=True
                    )
            except Exception as e:
                QApplication.restoreOverrideCursor()
                message = QMessageBox()
                message.setIcon(QMessageBox.Critical)
                message.setWindowTitle("ERROR")
                message.setText("CRIE UMA FOLHA DE PONTO")
                message.exec_()
                self.crud_buttons_5.add_user_btn.click()
    
    def edit_folha(self):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        if(self.verticalLayout_page_folha_ponto.count() > 0):
            for x in range(self.verticalLayout_page_folha_ponto.count()):
                self.verticalLayout_page_folha_ponto.itemAt(x).widget().setParent(None)

        self.functions = Folha_Ponto_Function()
        try:
            self.obra_escolhida = self.Lista_De_Folha.check_box_func()
            
            data    = self.functions.return_data(self.obra_escolhida[0])
            
            data_inicial    = datetime.strptime(str(data[0][0]), "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y")
            data_final    = datetime.strptime(str(data[0][1]), "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y")

            self.table  = QTable(
                    data_inicial, 
                    data_final,
                    self.functions.return_func_obra(self.obra_escolhida[0])
                )

            message = QMessageBox()
            message.setWindowTitle("ARX Sistemas")
            self.crud_buttons_5.add_user_btn.hide()
            self.crud_buttons_5.edit_user_btn.hide()
            self.crud_buttons_5.del_user_btn.hide()
            
            self.crud_buttons_teste.add_user_btn.show()
            
            self.crud_buttons_teste.add_user_btn.clicked.connect(self.add_values)
            QApplication.restoreOverrideCursor()
            self.verticalLayout_page_folha_ponto.addWidget(self.table.dialog)
            
            
            self.verticalLayout_page_folha_ponto.update()
        except Exception as e:
            QApplication.restoreOverrideCursor()
            message = QMessageBox()
            message.setIcon(QMessageBox.Critical)
            message.setWindowTitle("ERROR")
            message.setText("CRIE UMA FOLHA DE PONTO")
            message.exec_()
            self.crud_buttons_5.add_user_btn.click()


        
    def add_values(self):
        if(self.counter == 0):
            self.counter += 1
            res = list({v['Funcionario']:v for v in self.table.array}.values())
            #res = list(set((key, val) for dic in self.table.array for key, val in dic.items()))
            
            #print(res)
            self.functions.add_values(res, self.table)
        else:
            self.counter -= 1

    def refresh_folha_screen(self, typeFunc=None):
        self.folha_refresh  = Folha_Ponto_Function()
        self.folha_list     = Window_Folha(self.folha_refresh.refresh())
        self.Lista_De_Folha = Folhas_Window(self.folha_refresh.refresh_2())
        self.cont_folha     = 0
        self.cont_folha_del = 0
        
        if(self.type == "obra"):
            self.crud_buttons_5.add_user_btn.hide()
            self.crud_buttons_5.edit_user_btn.hide()
            self.crud_buttons_5.del_user_btn.hide()
        elif(self.type == "folha"):
            self.crud_buttons_5.add_user_btn.show()
            self.crud_buttons_5.edit_user_btn.show()
            self.crud_buttons_5.del_user_btn.show()

        self.crud_buttons_teste.add_user_btn.hide()
        
        for x in range(self.verticalLayout_page_folha_ponto.count()):
            self.verticalLayout_page_folha_ponto.itemAt(x).widget().setParent(None)
        self.verticalLayout_page_folha_ponto.addWidget(self.Lista_De_Folha)
        self.verticalLayout_page_folha_ponto.update()

        for x in range(self.verticalLayout_page_4.count()):
            self.verticalLayout_page_4.itemAt(x).widget().setParent(None)
        self.verticalLayout_page_4.addWidget(self.folha_list)
        self.verticalLayout_page_4.update()

    def despesas_onClick(self):

        self.change_buttons_color()
        self.btn_page_clientes.setStyleSheet(u"QPushButton {\n"
    "	color: rgb(255, 255, 255);\n"
    "	background-color: rgb(85, 170, 255);\n"
    "	border: 0px solid;\n"
    "}\n"
    "QPushButton:hover {\n"
    "	background-color: rgb(85, 170, 255);\n"
    "}")
        self.add_user_btn.hide()
        self.edit_user_btn.hide()
        self.del_user_btn.hide()

        self.crud_buttons.add_user_btn.hide()
        self.crud_buttons.edit_user_btn.hide()
        self.crud_buttons.del_user_btn.hide()
        self.crud_buttons_teste.add_user_btn.hide()

        self.crud_buttons_2.add_user_btn.hide()
        self.crud_buttons_2.edit_user_btn.hide()
        self.crud_buttons_2.del_user_btn.hide()

        self.crud_buttons_3.add_user_btn.hide()
        self.crud_buttons_3.edit_user_btn.hide()
        self.crud_buttons_3.del_user_btn.hide()

        self.crud_buttons_4.add_user_btn.hide()
        self.crud_buttons_4.edit_user_btn.hide()
        self.crud_buttons_4.del_user_btn.hide()

        self.crud_buttons_5.add_user_btn.hide()
        self.crud_buttons_5.edit_user_btn.hide()
        self.crud_buttons_5.del_user_btn.hide()

        self.crud_buttons_6.add_user_btn.show()
        self.crud_buttons_6.edit_user_btn.show()
        self.crud_buttons_6.del_user_btn.show()

        self.crud_buttons_7.add_user_btn.hide()
        self.crud_buttons_7.edit_user_btn.hide()
        self.crud_buttons_7.del_user_btn.hide()

    def add_cliente(self):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.add_cliente    = Window_Add_Cliente()
        self.clientes_functions = Clientes()
        inputs_array    = [
            self.add_cliente.nome_input,
            self.add_cliente.endereco_input,
        ]
        self.add_cliente.nome_input.textChanged.connect(
            self.clientes_functions.handle_nome
        )
        self.clientes_functions.inputs(inputs_array)
        self.add_cliente.cnpj_input.textChanged.connect(
            self.clientes_functions.handle_cnpj
        )
        self.add_cliente.telefoneInput.textChanged.connect(
            self.clientes_functions.handle_telefone
        )
        
        self.add_cliente.email_input.textChanged.connect(
            self.clientes_functions.handle_email
        )
        self.add_cliente.endereco_input.textChanged.connect(
            self.clientes_functions.handle_endereco
        )
        self.add_cliente.sub_button.clicked.connect(
            lambda:
            self.clientes_functions.onClick_add_cliente(
                self.refresh_cliente_screen,
                self.add_cliente.dlg
            )
            
        )
        QApplication.restoreOverrideCursor()
        self.add_cliente.dlg.exec_()

    def edit_cliente(self):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        c   = Confirmation_Screen()
        selected_cliente    = self.clientes_screen.check_box_func()
        self.clientes_functions = Clientes()
        if(len(selected_cliente) == 0):
            QApplication.restoreOverrideCursor()
            c.show_confirmation(
                """Nenhuma obra selecionada para exclusão!""",
                True
            )
        elif(len(selected_cliente) > 1):
            QApplication.restoreOverrideCursor()
            c.show_confirmation(
                """Só é permitida a edição de um cliente!""",
                True
            )
        else:
            self.add_cliente    = Window_Add_Cliente()
            self.clientes_functions = Clientes()
            db_response = self.clientes_functions.return_client_data(selected_cliente[0])
            
            inputs_array    = [
                self.add_cliente.nome_input,
                self.add_cliente.endereco_input,
            ]
            self.add_cliente.nome_input.setReadOnly(True)
            self.clientes_functions.inputs(inputs_array)
            self.add_cliente.cnpj_input.setText(db_response[0][1])
            self.add_cliente.nome_input.setText(db_response[0][2])
            self.add_cliente.cnpj_input.textChanged.connect(
                self.clientes_functions.handle_cnpj
            )
            self.add_cliente.telefoneInput.setText(db_response[0][4])
            self.add_cliente.telefoneInput.textChanged.connect(
                self.clientes_functions.handle_telefone
            )
            
            self.add_cliente.email_input.setText(db_response[0][3])
            self.add_cliente.email_input.textChanged.connect(
                self.clientes_functions.handle_email
            )

            self.add_cliente.endereco_input.setText(db_response[0][5])
            self.add_cliente.endereco_input.textChanged.connect(
                self.clientes_functions.handle_endereco
            )
            self.add_cliente.sub_button.clicked.connect(
                lambda:
                self.clientes_functions.onClick_edit_client(
                    self.add_cliente.dlg,
                    self.refresh_cliente_screen
                )
                
            )
            QApplication.restoreOverrideCursor()
            self.add_cliente.dlg.exec_()

    def delete_cliente(self):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        c   = Confirmation_Screen()
        selected_cliente    = self.clientes_screen.check_box_func()
        self.clientes_functions = Clientes()
        if(len(selected_cliente) == 0):
            QApplication.restoreOverrideCursor()
            c.show_confirmation(
                """Nenhuma obra selecionada para exclusão!""",
                True
            )
        else:
            
            c.confirm_btn.clicked.connect(lambda: self.clientes_functions.onClick_del_cliente(
                selected_cliente,
                c.dialog,
                self.refresh_cliente_screen
            ))
            QApplication.restoreOverrideCursor()
            c.show_confirmation(
                """Deseja excluir %s registros de Obras?""" % len(selected_cliente),
                btn=True
            )
           
            #self.refresh_cliente_screen()
    
    def refresh_cliente_screen(self):
        self.clientes_functions = Clientes()
        self.clientes_screen        = Clientes_List(self.clientes_functions.refresh())
        for x in range(self.verticalLayout_page_5.count()):
            self.verticalLayout_page_5.itemAt(x).widget().setParent(None)
        self.verticalLayout_page_5.addWidget(self.clientes_screen)
        self.verticalLayout_page_5.update()

    def onClick_despesas(self):

        self.change_buttons_color()
        self.btn_page_despesas.setStyleSheet(u"QPushButton {\n"
    "	color: rgb(255, 255, 255);\n"
    "	background-color: rgb(85, 170, 255);\n"
    "	border: 0px solid;\n"
    "}\n"
    "QPushButton:hover {\n"
    "	background-color: rgb(85, 170, 255);\n"
    "}")
        self.add_user_btn.hide()
        self.edit_user_btn.hide()
        self.del_user_btn.hide()

        self.crud_buttons.add_user_btn.hide()
        self.crud_buttons.edit_user_btn.hide()
        self.crud_buttons.del_user_btn.hide()
        self.crud_buttons_teste.add_user_btn.hide()

        self.crud_buttons_2.add_user_btn.hide()
        self.crud_buttons_2.edit_user_btn.hide()
        self.crud_buttons_2.del_user_btn.hide()

        self.crud_buttons_3.add_user_btn.hide()
        self.crud_buttons_3.edit_user_btn.hide()
        self.crud_buttons_3.del_user_btn.hide()

        self.crud_buttons_4.add_user_btn.hide()
        self.crud_buttons_4.edit_user_btn.hide()
        self.crud_buttons_4.del_user_btn.hide()

        self.crud_buttons_5.add_user_btn.hide()
        self.crud_buttons_5.edit_user_btn.hide()
        self.crud_buttons_5.del_user_btn.hide()

        self.crud_buttons_6.add_user_btn.hide()
        self.crud_buttons_6.edit_user_btn.hide()
        self.crud_buttons_6.del_user_btn.hide()

        self.crud_buttons_7.add_user_btn.show()
        self.crud_buttons_7.edit_user_btn.show()
        self.crud_buttons_7.del_user_btn.show()
    
    def add_despesa(self):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.despesa_screen =   Window_Form_Despesa()
        self.function       =   Despesas()
        self.despesa_screen.num_titulo_input.textChanged.connect(self.function.handle_num_titulo)
        self.despesa_screen.descricao_input.textChanged.connect(self.function.handle_descricao)
        self.despesa_screen.fornecedor_input.textChanged.connect(self.function.handle_fornecedor)
        self.despesa_screen.valor_input.textChanged.connect(self.function.handle_valor)
        
        self.despesa_screen.observacao_input.textChanged.connect(self.function.handle_observacao)
        self.despesa_screen.input_data.dateChanged.connect(self.function.handle_data)
        self.despesa_screen.vincular_obra_check_box.clicked.connect(self.check_box_despesa)
        self.despesa_screen.sub_button.clicked.connect(
            lambda:
            self.function.onClick_add_despesa(
                self.folha_list.check_box_func(),
                self.despesa_screen.dlg,
                self.refresh_despesa_screen
            )
        )
        QApplication.restoreOverrideCursor()
        self.despesa_screen.dlg.exec_()
    
    def check_box_despesa(self):
        
        if(self.folha == False):
           
            message = QMessageBox()
            message.setIcon(QMessageBox.Critical)
            message.setText("É necessário cadastrar uma obra primeiro!")
            message.setWindowTitle("ERROR")
            QApplication.restoreOverrideCursor()
            message.exec_()
        else:

            if(self.despesa_screen.vincular_obra_check_box.isChecked()):
                self.despesa_screen.dlg.setMinimumHeight(500)
                self.despesa_screen.verticalLayout_obras.addWidget(self.obras_list)
                
            else:
                for x in range(self.despesa_screen.verticalLayout_obras.count()):
                    self.despesa_screen.verticalLayout_obras.itemAt(x).widget().setParent(None)
                self.despesa_screen.dlg.setMinimumHeight(350)
                self.despesa_screen.dlg.setMaximumHeight(350)
    
    def del_despesa(self):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        c   = Confirmation_Screen()
        selected_despesa    = self.despesas_screen_list.check_box_func()
        if(selected_despesa == None):
            message = QMessageBox()
            message.setIcon(QMessageBox.Critical)
            message.setText("É necessário cadastrar uma despesa primeiro!")
            message.setWindowTitle("ERROR")
            QApplication.restoreOverrideCursor()
            message.exec_()
        else:
            self.despesas_functions = Despesas()
            if(len(selected_despesa) == 0):
                QApplication.restoreOverrideCursor()
                c.show_confirmation(
                    """Nenhum título selecionado para exclusão!""",
                    True
                )
            else:
                c.confirm_btn.clicked.connect(lambda: self.despesas_functions.onClick_del_despesa(
                    selected_despesa,
                    c.dialog,
                    self.refresh_despesa_screen
                ))
                QApplication.restoreOverrideCursor()
                c.show_confirmation(
                    """Deseja excluir %s registros de Obras?""" % len(selected_despesa),
                    btn=True
                )
                
    def edit_despesa(self):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        c   = Confirmation_Screen()
        selected_despesa    = self.despesas_screen_list.check_box_func()
        #self.despesas_functions = Despesas()
        if(len(selected_despesa) == 0):
            QApplication.restoreOverrideCursor()
            c.show_confirmation(
                """Nenhum título selecionado para exclusão!""",
                True
            )
        elif(len(selected_despesa) > 1):
            QApplication.restoreOverrideCursor()
            c.show_confirmation(
                """Só é permitida a edição de uma despesa!""",
                True
            )
        else:
            self.function       =   Despesas()
            db_response         = self.function.return_despesa_data(selected_despesa)
            self.despesa_screen =   Window_Form_Despesa()

            self.despesa_screen.num_titulo_input.setText(db_response[0][7])
            self.despesa_screen.num_titulo_input.textChanged.connect(self.function.handle_num_titulo)
            self.despesa_screen.descricao_input.setText(db_response[0][1])
            self.despesa_screen.descricao_input.textChanged.connect(self.function.handle_descricao)
            self.despesa_screen.fornecedor_input.setText(db_response[0][2])
            self.despesa_screen.fornecedor_input.textChanged.connect(self.function.handle_fornecedor)
            self.despesa_screen.valor_input.setText(str(db_response[0][3]))
            self.despesa_screen.valor_input.textChanged.connect(self.function.handle_valor)
            self.despesa_screen.observacao_input.setText(db_response[0][6])
            self.despesa_screen.observacao_input.textChanged.connect(self.function.handle_observacao)
            try:
                data    = datetime.strptime(str(db_response[0][5]), "%Y-%m-%d %H:%M:%S")
                date    = QDate(int(data.strftime("%Y")), int(data.strftime("%m")), int(data.strftime("%d")))
                self.despesa_screen.input_data.setDate(date)
            except Exception as e:
                pass
            self.despesa_screen.input_data.dateChanged.connect(self.function.handle_data)
            self.despesa_screen.vincular_obra_check_box.hide()
            self.despesa_screen.vincular_obra_label.hide()
            self.despesa_screen.sub_button.clicked.connect(
                lambda:
                self.function.onClick_edit_despesa(
                    self.despesa_screen.dlg,
                    self.refresh_despesa_screen
                )
            )
            QApplication.restoreOverrideCursor()
            self.despesa_screen.dlg.exec_()
            

    def refresh_despesa_screen(self):
        self.despesas_functions     = Despesas()
        self.despesas_screen_list   = Despesas_List(self.despesas_functions.refresh())

        for x in range(self.verticalLayout_page_despesas.count()):
            self.verticalLayout_page_despesas.itemAt(x).widget().setParent(None)
        self.verticalLayout_page_despesas.addWidget(self.despesas_screen_list)
        self.verticalLayout_page_despesas.update()

    def onClick_page_relatorio(self):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.change_buttons_color()
        self.btn_page_relatorios.setStyleSheet(u"QPushButton {\n"
        "	color: rgb(255, 255, 255);\n"
        "	background-color: rgb(85, 170, 255);\n"
        "	border: 0px solid;\n"
        "}\n"
        "QPushButton:hover {\n"
        "	background-color: rgb(85, 170, 255);\n"
        "}")

        self.screen_relatorio  = Window_Form_Relatorio()
        self.relatorios_functions   = Relatorios()
        self.screen_relatorio.num_titulo_input.dateChanged.connect(self.relatorios_functions.handle_data_inicial)
        self.screen_relatorio.descricao_input.dateChanged.connect(self.relatorios_functions.handle_data_final)
        self.screen_relatorio.sub_button.clicked.connect(self.openfile_screen)
        QApplication.restoreOverrideCursor()
        self.screen_relatorio.dlg.exec_()

    def openfile_screen(self):
        dialog = QFileDialog()
        dialog.setFilter(dialog.filter() | QtCore.QDir.Hidden)
        dialog.setDefaultSuffix('pdf')
        dialog.setAcceptMode(QFileDialog.AcceptSave)
        dialog.setNameFilters(['PDF (*.pdf)'])
        if dialog.exec_() == QDialog.Accepted:
            self.relatorios_functions.onClick_submit_relatorio(dialog.selectedFiles(), self.screen_relatorio.fornecedor_input.currentIndex())
        else:
            pass

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ARX Sistemas", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.btn_page_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_page_1.setText(QCoreApplication.translate("MainWindow", u"Cargos", None))
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", u"Funcionário", None))
        self.btn_page_3.setText(QCoreApplication.translate("MainWindow", u"Usuário", None))
        self.btn_page_4.setText(QCoreApplication.translate("MainWindow", u"Obras", None))
        self.btn_page_folha_ponto.setText(QCoreApplication.translate("MainWindow", u"Folha de Ponto", None))
        self.btn_page_clientes.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.btn_page_despesas.setText(QCoreApplication.translate("MainWindow", u"Despesas", None))
        self.btn_page_relatorios.setText(QCoreApplication.translate("MainWindow", u"Relatórios", None))
       