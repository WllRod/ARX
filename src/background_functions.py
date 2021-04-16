from src.DB_Connect.SQL import SQL_Funcionario, Funcoes, Obras, FolhaDePonto, Clientes_DB, Despesas_DB, Relatorios_DB
from src.Layouts.list_funcs import Func_Window
from src.Layouts.messageBox import return_message
from src.Layouts.loading import SpecialDialog
import threading
import queue
from datetime import datetime
import time
from PDF.Despesas import main_relat_despesas
from PDF.Folha_Ponto import main_relat_folha_ponto
from PDF.Folha_Ponto_Simples import main_relat_folha_ponto_simples
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread, QTimer, QSize
from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QDialog,
    QApplication,
    QPushButton,
    QGridLayout,
    QProgressBar,
    QLabel,
    QWidget, 
    QMessageBox,
    QMainWindow
    
)
from PyQt5.QtGui import *
import numpy as np
from functools import partial
import requests


class Handler(QObject):
    progress    = pyqtSignal(int)
    finished    = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self._isRunning = True
        self._success   = False
    
    @pyqtSlot()
    def task1(self):
      
        self.progress.emit(0)
            #time.sleep(2)
        
        
    
    @pyqtSlot()
    def task2(self, func_1=None):
        #func()
        
        #self.progress.emit(2)
        if(func_1 != None):
            func_1()
        else:
            time.sleep(10)
        #time.sleep(10)
        #func_2()
        self.finished.emit(1)
    
    @pyqtSlot(int)
    def task3(self, func):
        func()
        self.finished.emit(0)
        

    def stop(self):
        self._isRunning = False

class ErrorMessage(object):
    def __init__(self, text):
        super().__init__()

        self.message = QMessageBox()
        self.message.setIcon(QMessageBox.Critical)
        self.message.setText(text)
        self.message.setWindowTitle("Error")
        
class Functions():
    def __init__(self, id=None):
        self.sql    = SQL_Funcionario()
        
        self.name       = ""
        self.cpf        = ""
        self.rg         = ""
        self.salario    = ""
        
        self.data       = datetime.strptime(str("01-01-2000"), "%d-%m-%Y")
        self.email      = ""
        self.telefone   = ""
       
        self.horas_trabalhadas  = ""
        self.funcao             = ""
        if(id != None):

            
            self.user_data  = self.sql.return_users_data(id)
            self.id   = self.user_data[0][0]
            self.name   = self.user_data[0][1]
            self.cpf    = self.user_data[0][2]
            self.rg     = self.user_data[0][3]
            self.salario    = self.user_data[0][4]
            data            = datetime.strptime(str(self.user_data[0][5]), "%Y-%m-%d")
            self.data       = data.strftime("%Y%m%d")
            self.email      = self.user_data[0][6]
            self.telefone   = self.user_data[0][7]
            horas_trab      = datetime.strptime(str(self.user_data[0][8]), "%H:%M:%S")
            self.horas_trabalhadas  = horas_trab.strftime("%H:%M:%S")
            self.funcao             = self.user_data[0][9]
        
        self.handler    = None
        self.handler_thread = QThread()
        self.result = None
        self.actual_func    = None
        self.finish_func    = None

    def run_test(self):
        self.handler    = Handler()
        self.handler.moveToThread(self.handler_thread)
        self.handler.progress.connect(self.progress)
        self.handler.finished.connect(self.finisher)
        
        
    
    def progress(self, result):

        if(result == 0):
            wrapper = partial(self.handler.task2, self.actual_func)
            QTimer.singleShot(0, wrapper)
       
        
        self.dialog = SpecialDialog()
        self.dialog.show()
       
        result  = self.dialog.variable
        #
    
    def finisher(self, result):
        
        self.result = result
        #self.update_changes()
        #self.refresh_screen()
        
        
        self.handler.stop()
        self.handler_thread.quit()
        self.handler_thread.wait()
        if(self.finish_func == None):
            pass
        else:
            self.finish_func()
        self.dialog.close()
        QApplication.restoreOverrideCursor()

    def handle_name(self, text):
        self.name   = text
    
    def handle_cpf(self, text):
        self.cpf    = text

    def handle_rg(self, text):
        self.rg     = text
    
    def handle_salario_hora(self, text):
        self.salario    = text
    
    def handle_data_nascimento(self, text):
        self.data       = datetime.strptime(str(text.year())+str(text.month())+str(text.day()), "%Y%m%d")
    
    def handle_email(self, text):
        self.email      = text
    
    def handle_funcao(self, text, dataTuple):
        for x in dataTuple:
            if(text == x[0]):
               self.funcao  = x[1]

    def handle_telefone(self, text):
        self.telefone   = text
    
    def handle_horas_trabalhadas(self, text):
        self.hours      =   str(text.hour())+":"+str(text.minute())
        self.time       = datetime.strptime(self.hours, "%H:%M")     
        self.horas_trabalhadas  = self.time.strftime("%H:%M")

    def add_widget(self, layout, widget, frame):
        self.layout = QVBoxLayout(frame)
        self.layout.addWidget(Func_Window(widget))
        self.dialog.close()

    def new_func(self):
        
        if(self.data == ""):
            self.data   = ""
        else:
            self.data   = self.data.strftime("%Y%m%d")
        self.q   = queue.Queue()
        add = self.sql.add_func(
            self.name, 
            self.rg, 
            self.cpf, 
            self.salario, 
            self.data, 
            self.email, 
            self.telefone, 
            self.horas_trabalhadas,
            self.funcao,
            self.q)
        self.refresh    = False
        
        if(add != False):
            return add
        
    def add_user_(self, screen, refresh_screen):
        
        screen.close()
        if(self.name == ""):
            ErrorMessage("Campo 'Nome' é obrigatório!").message.exec_()
            
        else:
            self.refresh_screen = refresh_screen
            self.actual_func    = self.new_func
            self.finish_func    = self.refresh_screen

            self.run_test()
            self.handler_thread.started.connect(self.handler.task1)
                    
            self.handler_thread.start()
        

    def edit_funcionario(self, screen, refresh_screen):
        
        screen.close()
        self.refresh_screen = refresh_screen
        self.actual_func    = self.onClick_Edit_Funcionario
        self.finish_func    = self.refresh_screen

        self.run_test()
        self.handler_thread.started.connect(self.handler.task1)
                
        self.handler_thread.start()
    
    def exclude_func(self, dialog, list, refresh_screen):
        self.list           = list
        self.refresh_screen = refresh_screen
        dialog.close()
        self.actual_func    = self.onClick_exclude_func
        self.finish_func    = self.refresh_screen
        
        self.run_test()
        self.handler_thread.started.connect(self.handler.task1)
        self.handler_thread.start()

    def onClick_exclude_func(self):
        for x in self.list:
            self.sql.exclude_func(str(x))
        
    def onClick_Edit_Funcionario(self):
        self.edit   = self.sql.update_funcionario(
            ID=self.id,
            name=self.name,
            cpf=self.cpf, 
            rg=self.rg,
            salario=self.salario,
            data=self.data,
            email=self.email,
            telefone=self.telefone,
            horas=self.horas_trabalhadas,
            funcao=self.funcao
        )
        
        
class Cargos():
    def __init__(self, id=None):
        self.db = Funcoes()
        
        self.handler    = None
        self.handler_thread = QThread()
        self.result = None
        self.descricao  = ""
        #self.run_test()

        if(id != None):
            self.cargo_data = self.db.return_funcao_data(str(id))
            self.id         = self.cargo_data[0][0]
            self.descricao  = self.cargo_data[0][1]

    def run_test(self):
        self.handler    = Handler()
        self.handler.moveToThread(self.handler_thread)
        self.handler.progress.connect(self.progress)
        self.handler.finished.connect(self.finisher)
        
        
    
    def progress(self, result):

        if(result == 0):
            wrapper = partial(self.handler.task2, self.insert_data)
            QTimer.singleShot(0, wrapper)
        if(result   == 1):
            wrapper = partial(self.handler.task3, self.refresh_screen)
            QTimer.singleShot(0, wrapper)
        
        self.dialog = SpecialDialog()
        self.dialog.show()
       
        result  = self.dialog.variable
        #
    
    def finisher(self, result):
        
        
        
        self.result = result
        #self.update_changes()
        #self.refresh_screen()
        
        
        self.handler.stop()
        self.handler_thread.quit()
        self.handler_thread.wait()
        self.refresh_screen()
        self.dialog.close()
        QApplication.restoreOverrideCursor()

    def handle_descricao(self, text):
        self.descricao  = text

    def insert_data(self):
        self.db.add_funcao(self.descricao)
        self.screen.close()
        #time.sleep(5)
    
    def refresh_screen(self):
        
        self.refresh_func_screen()
        
        self.refresh_cargo_screen()

        #self.refresh_cargo_screen()
    def cargo_submit(self, screen, refresh_cargo_screen, refresh_func_screen, hide_screen):
        
        self.screen = screen
        self.refresh_cargo_screen   = refresh_cargo_screen
        self.hide_screen    = hide_screen
        
        self.refresh_func_screen    = refresh_func_screen
        self.run_test()
        self.handler_thread.started.connect(self.handler.task1)
             
        self.handler_thread.start()
        
        return True

    def edit_cargo(self, screen, refresh_cargo_screen, refresh_func_screen):
        self.db.edit_cargo(self.id, self.descricao)
        refresh_cargo_screen()
        refresh_func_screen()
        screen.close()
        return True
    
    def del_cargos(self, dialog, list, screen, screen_2):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        dialog.close()
        for x in list:
            self.db.del_cargo(x)
        screen()
        screen_2()
        QApplication.restoreOverrideCursor()
    
    def refresh_list(self):
        return self.db.return_funcoes()
        return True

class Obras_Functions():

    def __init__(self):
        self.db = Obras()
        self.descricao  = ""
        self.data       = "NULL"
        self.handler    = None
        self.handler_thread = QThread()
        self.result = None
        self.actual_func    = None
        self.finish_func    = None

    def run_test(self):
        self.handler    = Handler()
        self.handler.moveToThread(self.handler_thread)
        self.handler.progress.connect(self.progress)
        self.handler.finished.connect(self.finisher)
        
        
    
    def progress(self, result):

        if(result == 0):
            wrapper = partial(self.handler.task2, self.actual_func)
            QTimer.singleShot(0, wrapper)
       
        
        self.dialog = SpecialDialog()
        self.dialog.show()
       
        result  = self.dialog.variable
        #
    
    def finisher(self, result):
        
        self.result = result
        #self.update_changes()
        #self.refresh_screen()
        
        
        self.handler.stop()
        self.handler_thread.quit()
        self.handler_thread.wait()
        if(self.finish_func == None):
            pass
        else:
            self.finish_func()
        self.dialog.close()
        QApplication.restoreOverrideCursor()
        
    def handle_descricao(self, text):
        self.descricao  = text

    def handle_data(self, data):
        self.data     = datetime.strptime(str(data.year())+str(data.month())+str(data.day()), "%Y%m%d")

    def return_obra_data(self, id):
        return self.db.return_obra_data(id)

    def add_obra(self, list, screen, refresh_screen, cliente_selected):
        self.list   = list
        screen.close()
        if(self.list    == []):
            ErrorMessage("É necessário vincular ao menos um funcionário!").message.exec_()
        elif(self.descricao == ""):
            ErrorMessage("O campo 'Descrição' é obrigatório!").message.exec_()
        else:
            self.refresh_screen = refresh_screen
            self.cliente_selected   = cliente_selected

            self.actual_func    = self.onClick_add_obra
            self.finish_func    = self.refresh_screen

            self.run_test()
            self.handler_thread.started.connect(self.handler.task1)
                        
            self.handler_thread.start()

    def onClick_add_obra(self):
        
        (cnpj, nome) = self.cliente_selected.split(" - ")
        self.db.add_obras(self.list, self.descricao, self.data, cnpj)
            
        return True

    def del_obra(self, list, dialog, refresh_screen):
        dialog.close()
        self.list   = list
        self.refresh_screen = refresh_screen
        self.actual_func    = self.onClick_del_obra
        self.finish_func    = self.refresh_screen

        self.run_test()
        self.handler_thread.started.connect(self.handler.task1)
                
        self.handler_thread.start()
        
    
    def onClick_del_obra(self):
        self.db.del_obra(self.list)
            
    
    def edited(self, data):
        self.descricao  = data[0][0]
        self.data       = data[0][2]

    def edit_obra(self, checked_list, funcs, dialog, refresh_screen, id_obra, folha_screen, cliente):
        
        self.checked_list   = checked_list
        self.funcs          = funcs
        dialog.close()
        self.refresh_screen = refresh_screen
        self.id_obra    = id_obra
        self.folha_screen   = folha_screen
        self.cliente    = cliente

        self.actual_func    = self.onClick_edit_obra
        self.finish_func    = self.refresh_screen

        self.run_test()
        self.handler_thread.started.connect(self.handler.task1)
                
        self.handler_thread.start()
        self.folha_screen()
    def onClick_edit_obra(self):

        (cnpj, nome) = self.cliente.split(" - ")

        for x in self.checked_list:
            if(str(x).find("del") < 0):
                id  = str(x)
                self.db.add_func_obra(self.id_obra, id)

        for x in self.checked_list:
            if(str(x).find("del") >= 0):
                id  = str(x).split("del")
                self.db.del_func_obra(self.id_obra, id[0])
                
        self.db.update_obras(self.descricao, self.data, cnpj, self.id_obra)
        #refresh_screen()
        
        #dialog.close()

    def update_obra(self, cliente, data):
        (cnpj, nome) = cliente.split(" - ")
        self.descricao  = data[0]
        
    def refresh(self):
        return self.db.return_obras_list()

class Folha_Ponto_Function():
    def __init__(self):
        self.db = FolhaDePonto()

        self.handler    = None
        self.handler_thread = QThread()
        self.result = None
        self.actual_func    = None
        self.finish_func    = None

    def run_test(self):
        self.handler    = Handler()
        self.handler.moveToThread(self.handler_thread)
        self.handler.progress.connect(self.progress)
        self.handler.finished.connect(self.finisher)
        
        
    
    def progress(self, result):

        if(result == 0):
            wrapper = partial(self.handler.task2, self.actual_func)
            QTimer.singleShot(0, wrapper)
       
        
        self.dialog = SpecialDialog()
        self.dialog.show()
       
        result  = self.dialog.variable
        #
    
    def finisher(self, result):
        
        self.result = result
        #self.update_changes()
        #self.refresh_screen()
        
        
        self.handler.stop()
        self.handler_thread.quit()
        self.handler_thread.wait()
        if(self.finish_func == None):
            pass
        else:
            self.finish_func()
        self.dialog.close()
        QApplication.restoreOverrideCursor()

    def return_func_obra(self, id, folha_existente=None, data_inicial=None, data_final=None):
        if(folha_existente != None):
            return self.db.return_func_obra(id, True, data_inicial, data_final)
        else:
            return self.db.return_func_obra(id)
    
    def refresh(self):
        return self.db.return_folha()

    def refresh_2(self):
        return self.db.lists()
    
    def add_values(self, array, table):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        result  = {}
        array_temp  = []
        
        
        if(len(array) == 0):
            
            ErrorMessage("Nenhuma informação preenchida!").message.exec_()
            
        else:
            for x in array:
                total_dia   = float(x['Valor_Dia']) + float(x['Hora_Extra']) + float(x['Bonificacao'])
                self.db.verification(str(x['ID']), str(x['ID_Obra_Func']), str(x['Data']))
                insert_values   = self.db.add_folha_values(
                    str(x['ID']),
                    str(x['Data']),
                    str(x['Situacao']),
                    x['Hora_Extra_Hora'],
                    total_dia,
                    str(x['ID_Obra_Func']),
                    float(x['Bonificacao']),
                    float(x['Hora_Extra']),
                    float(x['Valor_Dia'])
                )
        #array.clear()
        QApplication.restoreOverrideCursor()

    def onClick_add_values(self):
        pass
        #message.setText("Dados gravados com sucesso!")
        #message.show()
        
    
    def del_folha(self, list, dialog, refresh_screen):
        dialog.close()
        self.list   = list
        self.refresh_screen = refresh_screen

        self.actual_func    = self.onClick_del_folha
        self.finish_func    = self.refresh_screen

        self.run_test()
        self.handler_thread.started.connect(self.handler.task1)
                
        self.handler_thread.start()
        
    def onClick_del_folha(self):
        
        self.db.delete_folha(self.list)

    def return_data(self, id):
        return self.db.return_data(id)


class Clientes():
    def __init__(self):
        self.handler    = None
        self.handler_thread = QThread()
        self.result = None
        self.text   = ""
        self.cnpj   = ""
        self.nome   = ""
        self.email  = ""
        self.endereco   = ""
        self.telefone   = ""
        self.db     = Clientes_DB()
        self.actual_func    = None
        self.finish_func    = None
        #self.run_test()

    def refresh(self):
        return self.db.return_clientes()

    def run_test(self):
        self.handler    = Handler()
        self.handler.moveToThread(self.handler_thread)
        self.handler.progress.connect(self.progress)
        self.handler.finished.connect(self.finisher)
        
        
    
    def progress(self, result):

        if(result == 0):
            wrapper = partial(self.handler.task2, self.actual_func)
            QTimer.singleShot(0, wrapper)
       
        
        self.dialog = SpecialDialog()
        self.dialog.show()
       
        result  = self.dialog.variable
        #
    
    def finisher(self, result):
        
        
        self.result = result
        #self.update_changes()
        #self.refresh_screen()
        
        
        self.handler.stop()
        self.handler_thread.quit()
        self.handler_thread.wait()
        if(self.finish_func == None):
            pass
        else:
            self.finish_func()
        self.dialog.close()
        QApplication.restoreOverrideCursor()
    
    def handle_nome(self, nome):
        self.nome   = nome

    def handle_cnpj(self, cnpj):
        if(len(cnpj) == 14):
            self.cnpj  = cnpj
            self.actual_func    = self.cnpj_api
            self.run_test()
            self.handler_thread.started.connect(self.handler.task1)
                
            self.handler_thread.start()
        else:
            self.cnpj   = cnpj

    def handle_telefone(self, telefone):
        self.telefone   = telefone

    def handle_email(self, email):
        self.email      = email
    
    def handle_endereco(self, endereco):
        self.endereco   = endereco

    def cnpj_api(self):
        try:
            resp    = requests.get('https://www.receitaws.com.br/v1/cnpj/'+self.cnpj)
            if resp.status_code != 200:
                raise ApiError('GET /tasks/ {}'.format(resp.status_code))
            
            #resp        = resp.json()
            json_data       = resp.json()
            self.endereco   = json_data['logradouro']+","+json_data['numero']+","+json_data['bairro']+" - "+json_data['municipio']+" - "+json_data['cep']
            self.nome       = json_data['nome'] 
            self.input[0].setText(self.nome)
            self.input[1].setText(self.endereco)
        except Exception as e:
            pass

    def onClick_add_cliente(self, refresh_screen, dialog):
        dialog.close()
        if(self.cnpj == ""):
            ErrorMessage("Campo 'CNPJ' é obrigatório!").message.exec_()
        else:
            self.actual_func    = self.add_cliente
            self.finish_func    = refresh_screen
            self.run_test()
            self.handler_thread.started.connect(self.handler.task1)
                
            self.handler_thread.start()

    def add_cliente(self):

        self.db.add_cliente(
            self.cnpj,
            self.nome,
            self.email,
            self.telefone,
            self.endereco
        )
        
        
    def inputs(self, list):
        self.input  = list

    def onClick_del_cliente(self, list, dialog, screen_refresh):
        self.list   = list
        self.screen = dialog
        self.finish_func = screen_refresh
        dialog.close()
        self.actual_func    = self.teste
        self.run_test()
        self.handler_thread.started.connect(self.handler.task1)
                
        self.handler_thread.start()

    def teste(self):
        self.db.delete_cliente(self.list)
        #self.screen_refresh()
        #self.screen.close()
    
    def return_client_data(self, id):
        db_response     =  self.db.return_cliente_data(id)
        self.id         = db_response[0][0]
        self.cnpj       = db_response[0][1]
        self.nome       = db_response[0][2]
        self.email      = db_response[0][3]
        self.telefone   = db_response[0][4]
        self.endereco   = db_response[0][5]
        return db_response
    
    def onClick_edit_client(self, dialog, refresh_screen):
        dialog.close()
        self.actual_func    = self.update_client
        self.finish_func    = refresh_screen
        self.run_test()
        self.handler_thread.started.connect(self.handler.task1)
                
        self.handler_thread.start()
    
    def update_client(self):
        self.db.update_cliente(
            self.id,
            self.cnpj,
            self.nome,
            self.email,
            self.telefone,
            self.endereco
        )

class Despesas():
    def __init__(self):
        self.handler    = None
        self.handler_thread = QThread()
        self.result = None
        self.text   = ""
        self.actual_func    = None
        self.finish_func    = None
        self.num_titulo     = ""
        self.descricao      = ""
        self.fornecedor     = ""
        self.valor          = ""
        self.observacao     = ""
        self.data           = ""
        self.db             = Despesas_DB()

    def run_test(self):
        self.handler    = Handler()
        self.handler.moveToThread(self.handler_thread)
        self.handler.progress.connect(self.progress)
        self.handler.finished.connect(self.finisher)
        
        
    
    def progress(self, result):

        if(result == 0):
            wrapper = partial(self.handler.task2, self.actual_func)
            QTimer.singleShot(0, wrapper)
       
        
        self.dialog = SpecialDialog()
        self.dialog.show()
       
        result  = self.dialog.variable
        #
    
    def finisher(self, result):
        
        self.result = result
        #self.update_changes()
        #self.refresh_screen()
        
        
        self.handler.stop()
        self.handler_thread.quit()
        self.handler_thread.wait()
        if(self.finish_func == None):
            pass
        else:
            self.finish_func()
        self.dialog.close()
        QApplication.restoreOverrideCursor()
    
    def refresh(self):
        return self.db.return_data()

    def handle_num_titulo(self, num_titulo):
        self.num_titulo = num_titulo
    
    def handle_descricao(self, descricao):
        self.descricao  = descricao
    
    def handle_fornecedor(self, fornecedor):
        self.fornecedor = fornecedor

    def handle_valor(self, valor):
        self.valor   = valor
    
    def handle_observacao(self, observacao):
        self.observacao = observacao
    
    def handle_data(self, data):
        self.data       = datetime.strptime(str(data.year())+str(data.month())+str(data.day()), "%Y%m%d")

    
    def onClick_add_despesa(self, id, dialog, screen):
        dialog.close()
        if(self.num_titulo == ""):
            
            ErrorMessage("Campo 'Num. Título' é obrigatório!").message.exec_()
            
        elif(self.valor == ""):
            
            ErrorMessage("Campo 'Valor' é obrigatório!").message.exec_()
            
        else:
            self.id             = id
            self.actual_func    = self.add_despesa
            self.finish_func    = screen
            self.run_test()
            self.handler_thread.started.connect(self.handler.task1)
            self.handler_thread.start()

    def add_despesa(self):
        self.db.add_despesa(
            self.id,
            self.num_titulo,
            self.descricao,
            self.fornecedor,
            self.valor,
            self.observacao,
            self.data
        )
    
    def onClick_del_despesa(self, list, dialog, refresh):
        self.list   = list
        dialog.close()
        self.actual_func    = self.del_despesa
        self.finish_func    = refresh
        self.run_test()
        self.handler_thread.started.connect(self.handler.task1)
        self.handler_thread.start()
    
    def del_despesa(self):
        self.db.del_despesa(self.list)

    def return_despesa_data(self, id):
        db_response     =  self.db.return_despesa_data(id[0])
        
        self.id         = db_response[0][0]
        self.descricao  = db_response[0][1]
        self.fornecedor = db_response[0][2]
        self.valor      = db_response[0][3]
        self.data       = db_response[0][5]
        self.observacao = db_response[0][6]
        self.num_titulo = db_response[0][7]
        return db_response
    
    def onClick_edit_despesa(self, dialog, refresh):
        dialog.close()
        self.actual_func    = self.edit_despesa
        self.finish_func    = refresh
        self.run_test()
        self.handler_thread.started.connect(self.handler.task1)
        self.handler_thread.start()

    def edit_despesa(self):
        self.db.update_despesa(
            self.id,
            self.descricao,
            self.fornecedor,
            self.valor,
            self.data,
            self.observacao,
            self.num_titulo
        )

class Relatorios():
    def __init__(self):
        self.handler    = None
        self.handler_thread = QThread()
        self.result = None
        self.text   = ""
        self.actual_func    = None
        self.finish_func    = None
        self.data_inicial   = ""
        self.data_final     = ""
        self.db             = Relatorios_DB()

    def run_test(self):
        self.handler    = Handler()
        self.handler.moveToThread(self.handler_thread)
        self.handler.progress.connect(self.progress)
        self.handler.finished.connect(self.finisher)
        
        
    
    def progress(self, result):

        if(result == 0):
            wrapper = partial(self.handler.task2, self.actual_func)
            QTimer.singleShot(0, wrapper)
       
        
        self.dialog = SpecialDialog()
        self.dialog.show()
       
        result  = self.dialog.variable
        #
    
    def finisher(self, result):
        
        self.result = result
        #self.update_changes()
        #self.refresh_screen()
        
        
        self.handler.stop()
        self.handler_thread.quit()
        self.handler_thread.wait()
        if(self.finish_func == None):
            pass
        else:
            self.finish_func()
        self.dialog.close()
        QApplication.restoreOverrideCursor()
    
    def handle_data_inicial(self, data):
        self.data_inicial   = datetime.strptime(str(data.year())+str(data.month())+str(data.day()), "%Y%m%d")

    def handle_data_final(self, data):
        self.data_final     = datetime.strptime(str(data.year())+str(data.month())+str(data.day()), "%Y%m%d")

    def onClick_submit_relatorio(self, save_path, relatorio):
        self.save_path  = save_path
        self.relatorio  = relatorio

        self.generate_relatorio()
    def teste(self):
        ErrorMessage('TESTE').message.exec_()
    def generate_relatorio(self):
        
        if(self.relatorio == 1):
            db_response = self.db.despesas(self.data_inicial, self.data_final)
            if(db_response == False):
                #self.finish_func    = self.teste()
                ErrorMessage("CADASTRE UMA DESPESA!").message.exec_()
            else:
                main_relat_despesas(db_response, self.save_path[0])
        elif(self.relatorio == 0):
            db_response = self.db.relat_folha_Ponto_simples(self.data_inicial, self.data_final)
            if(db_response == False):
                ErrorMessage("CADASTRE UMA FOLHA DE PONTO!").message.exec_()
            else:
                main_relat_folha_ponto_simples(db_response, self.save_path[0])
        elif(self.relatorio == 2):
            db_response = self.db.folha_ponto_relat(self.data_inicial, self.data_final)
            if(db_response == False):
                ErrorMessage("CADASTRE UMA FOLHA DE PONTO!").message.exec_()
            else:
                main_relat_folha_ponto(db_response, self.save_path[0])
    
