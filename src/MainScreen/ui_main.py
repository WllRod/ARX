from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

from MainScreen.SQL_Connect import Connector

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.sql    = Connector()
        self.centralwidget = QWidget(MainWindow)
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
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid;")

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
        self.btn_page_1 = QPushButton(self.frame_top_menus)
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
        self.frame_top_menu_1   = QFrame(self.frame_top_menu)
        self.frame_top_menu_2   = QFrame(self.frame_top_menu)
        self.frame_top_menu_3   = QFrame(self.frame_top_menu)
        self.frame_top_menu_4   = QFrame(self.frame_top_menu)

        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_menu)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_4.addWidget(self.frame_top_menu_1)
        self.horizontalLayout_4.addWidget(self.frame_top_menu_2)
        self.horizontalLayout_4.addWidget(self.frame_top_menu_3)
        self.horizontalLayout_4.addWidget(self.frame_top_menu_4)
        self.stackedWidget = QStackedWidget(self.frame_pages)

        self.include_button_1 = QPushButton(self.frame_top_menu_2)
        self.include_button_1.setStyleSheet("margin-top: 5%; border-radius: 2px;background: rgb(85, 170, 255)")
        
        self.include_button_1.setMinimumSize(QSize(100, 50))
        self.include_button_1.clicked.connect(self.teste)
        self.include_button_1.setText("Criar Usuário")
        self.include_button_1.setCursor(QCursor(Qt.PointingHandCursor))

        #self.frame_icon_include_btn  = QFrame(self.include_button_1)
        '''self.frame_icon_include_btn.setStyleSheet("background: red;")'''
        self.include_button_1.setIcon(QIcon("assets\\add.png"))
        self.include_button_1.setIconSize(QSize(25, 50))
        '''self.frame_text_include_btn = QFrame(self.include_button_1)
        self.frame_text_include_btn.setStyleSheet("background: yellow;")
        self.frame_text_include_btn.setMinimumSize(QSize(70, 10))

        self.horizontalLayout_5 = QHBoxLayout(self.include_button_1)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.addWidget(self.frame_text_include_btn)
        self.horizontalLayout_5.addWidget(self.frame_icon_include_btn)'''

        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_7 = QVBoxLayout(self.page_1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        
        for users in self.sql.return_all_users():
            self.frame_content  = QFrame(self.page_1)
            self.frame_content.setMaximumSize(QSize(900, 100))
            self.horizontalLayout_3 = QHBoxLayout(self.frame_content)
            self.frame_id   = QFrame(self.frame_content)
            self.frame_user = QFrame(self.frame_content)
            
            self.label_id   = QLabel(self.frame_id)
            self.label_id.setStyleSheet("border: 1px solid;")
            self.label_users    = QLabel(self.frame_user)
            self.label_users.setStyleSheet("border: 1px solid;")

            self.label_id.setText(str(users.ID))
            self.label_users.setText(users.User)
            self.horizontalLayout_3.addWidget(self.label_id)
            self.horizontalLayout_3.addWidget(self.label_users)
            self.verticalLayout_7.addWidget(self.frame_content)
            
        font = QFont()
        font.setPointSize(40)
        
        

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: #FFF;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #FFF;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)

    def teste(self):
        self.dlg = QDialog()
        self.dlg.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.dlg.setWindowTitle("Cadastro de Usuário")
        self.dlg.setStyleSheet(u"background-color: rgb(201, 198, 177); ")
        
        self.dlg.setMinimumSize(QSize(500, 500))
        self.dlg_frame  = QFrame(self.dlg)
        self.dlg_frame.setStyleSheet("background: rgb(40, 40, 40)")

        self.horizontalLayout_5 = QHBoxLayout(self.dlg)
        self.horizontalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.addWidget(self.dlg_frame)

        
        self.dlg.exec_()
    
    def close(self):
        self.dlg.close()
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.btn_page_1.setText(QCoreApplication.translate("MainWindow", u"Pag. 1", None))
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", u"Pag. 2", None))
        self.btn_page_3.setText(QCoreApplication.translate("MainWindow", u"Pag. 3", None))
        #self.label_1.setText(QCoreApplication.translate("MainWindow", u"Página 1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Página 2", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Página 3", None))
    # retranslateUi