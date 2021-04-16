import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent, QTimer)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QMovie)
from PyQt5.QtWidgets import *
import threading
import queue
# GUI FILE
from ui_main import Ui_MainWindow
from DB_Connect.SQL import DB_Login, SQL_Funcionario, Funcoes, Obras, FolhaDePonto, Clientes_DB, Despesas_DB
# IMPORT FUNCTIONS
from ui_functions import *

class render_data():
    def __init__(self):
        done            = False
        self.db         = DB_Login()
        self.perm       = 0
        self.db_users   = SQL_Funcionario()
        self.db_cargos  = Funcoes()
        self.db_obras   = Obras()
        self.db_folha   = FolhaDePonto()
        self.db_cliente = Clientes_DB()
        self.db_despesa = Despesas_DB()
    
    def start(self):
        teste   = [
            self.db.return_all_users,
            self.db_users.return_all_funcs,
            self.db_cargos.return_funcoes,
            self.db_obras.return_obras_list,
            self.db_folha.return_folha
        ]

        #self.loading    = LoadignScreen()

        #t1  = threading.Thread(target=self.loading.dialog.show())
        #t1.start()

        threads = []

        self.q   = queue.Queue()

        self.q2  = queue.Queue()

        self.q3  = queue.Queue()

        self.q4  = queue.Queue()

        self.q5  = queue.Queue()

        self.q6  = queue.Queue()

        self.q7 = queue.Queue()

        self.q8 = queue.Queue()

        self.teste2 = [
            self.q,
            self.q2,
            self.q3,
            self.q4,
            self.q5,
            
        ]

        for x in range(len(teste)):
            t   = threading.Thread(target=teste[x], args=(self.teste2[x], ))
            t.start()
            threads.append(t)
        for x in threads:
            x.join()

        
        self.db_folha.lists(self.q6)
        self.teste2.append(self.q6)

        self.db_cliente.return_clientes(self.q7)
        self.teste2.append(self.q7)

        self.db_despesa.return_data(self.q8)
        self.teste2.append(self.q8)
        
    def hide_screen(self, perm):
        self.ui  = MainWindow(self.teste2, perm)
        self.ui.ui.hide()
    
    def start_screen(self):
        
        self.ui.ui.showMaximized()

class MainWindow(QMainWindow):
    def __init__(self, list, perm):
        QMainWindow.__init__(self)
        self.perm   = perm
        done    = True
        
        if(done):

            #QTimer.singleShot(5000, self.loading.dialog.close)
            self.ui = Ui_MainWindow(
                list[0].get(), 
                list[1].get(),
                list[2].get(),
                list[3].get(),
                list[4].get(),
                list[5].get(),
                list[6].get(),
                list[7].get()
            )
            
            if(self.perm == 0 or self.perm == 1):
                pass
            elif(self.perm == 2):
                
                self.ui.btn_page_3.hide()

                self.ui.btn_page_4.hide()

                self.ui.btn_page_relatorios.hide()

                self.ui.btn_page_folha_ponto.hide()

            #self.ui.setupUi(self)
            
                ## TOGGLE/BURGUER MENU
                ########################################################################
            self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))
            self.ui.Btn_Toggle.click()

                ## PAGES
                ########################################################################
                #HOME
            self.ui.btn_page_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_home))
                # PAGE 1
            
            self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
                

                # PAGE 2
            self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))

                # PAGE 3
            self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

            self.ui.btn_page_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))

            self.ui.btn_page_folha_ponto.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_folha_ponto))

            self.ui.btn_page_clientes.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_clientes))

            self.ui.btn_page_despesas.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_despesas))

                ## SHOW ==> MAIN WINDOW
                ########################################################################
            self.setMinimumSize(QSize(1050, 600))
            #QTimer.singleShot(5000, self.ui.showMaximized)
            
            #self.ui.showMaximized()
        
        ## ==> END ##

def main_teste(list):

    #print('TESTE')
    app = QApplication(sys.argv)
    window  = MainWindow(list)
    #window.ui.showMaximized()
    sys.exit(app.exec_())

#main_teste()
#main_teste()
'''if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())'''