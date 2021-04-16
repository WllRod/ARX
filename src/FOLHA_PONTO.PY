from dateutil.relativedelta import *
from datetime import datetime, date
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
import sys
from PyQt5 import sip, QtCore
from DB_Connect.SQL import DB
from datetime import datetime, timedelta
import locale
from decimal import Decimal

class QTable(QWidget):
    def __init__(self, dataInicial, dataFinal, funcList, read_only=None, bool_value=None, edited=None):
        
        super(QTable, self).__init__()
        #self.array.clear()
        self.dataInicial    = dataInicial
        self.dataFinal      = dataFinal
        self.db = DB()
        self.bonificacao    = None
        self.edited         = edited
        self.hora_extra     = None
        self.testeC_ont         = 0
        self.testeC_ont_2   = 0
        self.data           = None
        self.situacao       = None
        self.array_clear    = [
            self.bonificacao,
            self.hora_extra, 
            self.data,       
            self.situacao   
        ]
        self.array                  = []
        
        self.update_array_values    = []
        self.db_response    = funcList[0]
        self.db_response_2  = funcList[1]
        self.db_response_3  = funcList[2]
        
        self.array_bidimensional = [
            self.db_response_3
        ]
        
        self.dialog = QWidget()
        #self.dialog.setStyleSheet("background: rgb(201, 198, 177);")
        self.tableWidget    = QTableWidget(self.dialog)
        
        self.verticalLayout = QVBoxLayout(self.tableWidget)
        self.tableWidget.setStyleSheet("background: 7A7A7A")
        self.tableWidget.setMinimumSize(QSize(1000, 500))
        if(read_only):
            self.read_only()
        else:
            self.nova_folha()
        self.error_message  = QMessageBox()
        self.error_message.setIcon(QMessageBox.Critical)
        self.error_message.setWindowTitle("ERROR")
        self.close_message_1    = False
        self.mp                 = None
        #self.button.clicked.connect(self.button_teste)
        #self.dialog.showMaximized()
        #self.dialog.exec_()

    def return_dict(self, funcionario, dataSemana, situacao, hora_extra, bonificacao, array):
        
        if((situacao and hora_extra and bonificacao) != "" or situacao.upper() == "F"):
            if(situacao.upper() == "OK"):
                for x in self.db_response:
                    if(str(x[0]) == funcionario):
                        data    = x[2]
                        to_time = datetime.strptime(str(data), "%H:%M:%S")
                        horaExtra   = datetime.strptime(str(hora_extra), "%H:%M")
                        (hE, mE) = horaExtra.strftime("%H:%M").split(":")
                        self.valor_hora_extra   = (int(hE) * float(x[1])) + ((int(mE) / 60) * float(x[1]))
                        (h, m, s) = to_time.strftime("%H:%M:%S").split(":")
                        self.valor_dia   = (int(h) * float(x[1])) + ((int(m) / 60) * float(x[1]))
                        self.id_obra    = x[3]
                        self.id_obra_func   = x[4]
            
            elif(situacao == None):
                pass
            elif(situacao.upper() == "F"):
                for x in self.db_response:
                    if(str(x[0]) == funcionario):
                        data    = x[2]
                        to_time = datetime.strptime(str("00:00:00"), "%H:%M:%S")
                        horaExtra   = datetime.strptime(str("00:00"), "%H:%M")
                        (hE, mE) = horaExtra.strftime("%H:%M").split(":")
                        self.valor_hora_extra   = float(0.00)
                        (h, m, s) = to_time.strftime("%H:%M:%S").split(":")
                        bonificacao = float(0.00)
                        self.valor_dia   = float(0.00)
                        self.id_obra    = x[3]
                        self.id_obra_func   = x[4]
            elif(situacao.upper() == "MP"):
                for x in self.db_response:
                    if(str(x[0]) == funcionario):
                        data                    = x[2]
                        to_time                 = datetime.strptime(str(data), "%H:%M:%S")
                        horaExtra               = datetime.strptime(str(hora_extra), "%H:%M")
                        (hE, mE)                = horaExtra.strftime("%H:%M").split(":")
                        self.valor_hora_extra   = (int(hE) * float(x[1])) + ((int(mE) / 60) * float(x[1]))
                        (h, m, s)               = to_time.strftime("%H:%M:%S").split(":")
                        self.valor_dia          = (int(h) * float(x[1])) + ((int(m) / 60) * float(x[1]))
                        self.valor_dia          = self.valor_dia / 2
                        self.valor_hora_extra   = self.valor_hora_extra / 2
                        self.id_obra            = x[3]
                        self.id_obra_func       = x[4]
                        meio_periodo            = ''.join(str(str(int(h) / 2)+":"+str(int(m) / 2)+":"+str(int(s) / 2))).replace(".0", "")
                        #to_time                 = datetime.strptime(str(meio_periodo), "%H:%M:%S")
                        a_time                  = to_time - datetime(1900, 1, 1)
                        seconds                 = a_time.total_seconds() / 2
                        to_time                 = datetime.strptime(str(timedelta(seconds=seconds)), "%H:%M:%S")
                        

            
            self.tupleData   = {
                "ID": self.id_obra,
                "ID_Obra_Func": self.id_obra_func,
                "Funcionario": funcionario,
                "Data": datetime.strptime(dataSemana, "%d-%m-%Y").strftime("%Y-%m-%d"),
                "Valor_Dia": self.valor_dia,
                "Situacao": to_time.strftime("%H:%M:%S"),
                "Hora_Extra": self.valor_hora_extra,
                "Hora_Extra_Hora": horaExtra.strftime("%H:%M"),
                "Bonificacao": bonificacao
            }

            if(self.tupleData['Situacao'] == ''):
                pass
            else:
                '''if(len(self.array) == self.tableWidget.rowCount() - 1):
                    self.array.clear()'''
                
                self.array.append(self.tupleData)
                #self.tupleData.clear()
                
                #print(self.array)
                #return self.tupleData
            
    def verification(self, func_id=None):
        cont = 0
        for x in self.db_response_2:
            if(str(x[0]) == func_id):
                cont += 1
                
           
    def nova_folha(self):
        dataInicial = self.dataInicial
        dataFinal   = self.dataFinal

        dataInicial_to_date = datetime.strptime(dataInicial, "%d-%m-%Y")
        dataFinal_to_date   = datetime.strptime(dataFinal, "%d-%m-%Y")


        difference = ((abs(dataInicial_to_date - dataFinal_to_date).days))

        self.tableWidget.setRowCount(len(self.db_response) + 1)
        self.tableWidget.setColumnCount((difference+1) * 3 + 1)
        self.tableWidget.setItem(0, 0, QTableWidgetItem(str("")))


        primeiro=1
        razao = 3
        n = difference + 1

        ultimo = primeiro + (n-1)*razao
        ultimo = ultimo + 1
        
        
        for var in range(primeiro, ultimo, razao):
            data = dataFinal_to_date - relativedelta(days=difference)
            difference -= 1
            self.tableWidget.setItem(0, var, QTableWidgetItem(data.strftime("%d-%m-%Y")))
            self.tableWidget.item(0, var).setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(0, var+1, QTableWidgetItem(str("Horas Extras")))
            self.tableWidget.item(0, var+1).setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(0, var+2, QTableWidgetItem(str("Bonificações")))
            self.tableWidget.item(0, var+2).setFlags(QtCore.Qt.ItemIsEnabled)
        
        for x in range(1, self.tableWidget.rowCount()):
            for var in range(primeiro, ultimo, razao): 
                self.tableWidget.setItem(x, var+1, QTableWidgetItem(str("0:00")))
                self.tableWidget.setItem(x, var+2, QTableWidgetItem(str("0.00")))
            
        cont = 1
        
        for data in self.db_response:
            self.tableWidget.setItem(cont, 0, QTableWidgetItem(str(data[0])))
            self.tableWidget.item(cont, 0).setFlags(QtCore.Qt.ItemIsEnabled)
            cont += 1

        for x in range(1, self.tableWidget.rowCount()):
            func_name   = self.tableWidget.item(x, 0).text()
            for b in self.db_response_3:
                if(b.BONIFICACAO == None):
                    bonificacao = "Sem bonificações!"
                else:
                    bonificacao = float(b.BONIFICACAO)
                if(b.FUNC == func_name):
                    for c in range(1, self.tableWidget.columnCount()):
                        data    = self.tableWidget.item(0, c).text()
                        if(data == b.DATA):
                            self.tableWidget.setItem(x, c, QTableWidgetItem(str(b.SITUACAO)))
                            self.tableWidget.setItem(x, c+1, QTableWidgetItem(str(b.HORA_EXTRA)))
                            self.tableWidget.setItem(x, c+2, QTableWidgetItem(str(bonificacao)))
                        
        self.tableWidget.cellChanged.connect(self.teste)

    def read_only(self):

        cont = 1
        temp_array = []
        for data in self.db_response_3:
            temp_array.append(data.FUNC)
        
        func_name = list(set(temp_array))
        dataInicial = self.dataInicial
        dataFinal   = self.dataFinal

        dataInicial_to_date = datetime.strptime(dataInicial, "%d-%m-%Y")
        dataFinal_to_date   = datetime.strptime(dataFinal, "%d-%m-%Y")


        difference = ((abs(dataInicial_to_date - dataFinal_to_date).days))

        self.tableWidget.setRowCount(len(func_name) + 1)
        self.tableWidget.setColumnCount((difference+1) * 3 + 1)
        self.tableWidget.setItem(0, 0, QTableWidgetItem(str("")))


        primeiro=1
        razao = 3
        n = difference + 1

        ultimo = primeiro + (n-1)*razao
        ultimo = ultimo + 1
        
        for x in range(1, self.tableWidget.rowCount()):
            for b in range(1, self.tableWidget.columnCount()):
                self.tableWidget.setItem(x, b, QTableWidgetItem(str("-")))
        for var in range(primeiro, ultimo, razao):
            data = dataFinal_to_date - relativedelta(days=difference)
            difference -= 1
            self.tableWidget.setItem(0, var, QTableWidgetItem(data.strftime("%d-%m-%Y")))
            
            self.tableWidget.setItem(0, var+1, QTableWidgetItem(str("Horas Extras")))
            self.tableWidget.setItem(0, var+2, QTableWidgetItem(str("Bonificações")))

        cont = 1
        for funcs in func_name:
            self.tableWidget.setItem(cont, 0, QTableWidgetItem(str(funcs)))
            cont += 1

        linha = 1
        for x in range(1, self.tableWidget.rowCount()):
            func_name   = self.tableWidget.item(x, 0).text()
            for b in self.db_response_3:
                if(b.BONIFICACAO == None):
                    bonificacao = "Sem bonificações!"
                else:
                    bonificacao = float(b.BONIFICACAO)
                if(b.FUNC == func_name):
                    for c in range(1, self.tableWidget.columnCount()):
                        data    = self.tableWidget.item(0, c).text()
                        if(data == b.DATA):
                            self.tableWidget.setItem(x, c, QTableWidgetItem(str(b.SITUACAO)))
                            self.tableWidget.setItem(x, c+1, QTableWidgetItem(str(b.HORA_EXTRA)))
                            self.tableWidget.setItem(x, c+2, QTableWidgetItem(str(bonificacao)))
                        


    def teste(self):
        currentRow  = self.tableWidget.currentRow()
        currentColumn  = self.tableWidget.currentColumn()
        column_name = self.tableWidget.item(0, currentColumn).text()
        
        
        self.funcionario    = self.tableWidget.item(currentRow, 0).text()

        if(column_name == "Bonificações"):
            self.bonificacao =  self.tableWidget.item(currentRow, currentColumn).text()
            try:
                float(self.bonificacao)
            except Exception as e:

                if(self.bonificacao == ""):
                    pass
                else:

                    texto   = """SÍNTAXE "{}" INCORRETA!\nÉ necessário digitar um valor monetário, exemplo: 100.00.""".format(
                        self.bonificacao
                    )
                    self.error_message.setText(texto)
                    result  = self.error_message.exec_()
                    self.bonificacao    = ""
                    self.tableWidget.setItem(currentRow, currentColumn, QTableWidgetItem(str("")))
            self.data    =      self.data
            self.situacao    =  self.situacao
            self.hora_extra  =  self.hora_extra
    
        elif(column_name == "Horas Extras"):
            self.hora_extra  =  self.tableWidget.item(currentRow, currentColumn).text()
            try:
                datetime.strptime(str(self.hora_extra), "%H:%M")
            except Exception as e:
                if(self.hora_extra == ""):
                    pass
                else:
                    texto   = """SÍNTAXE "{}" INCORRETA\nÉ necessário digitar um valor no formato H:M, exemplo: 2:30""".format(
                        self.hora_extra
                    )
                    self.error_message.setText(texto)
                    result  = self.error_message.exec_()
                    self.tableWidget.setItem(currentRow, currentColumn, QTableWidgetItem(str("")))
                    self.hora_extra = ""
            self.data    =      self.data
            self.situacao    =  self.situacao
            self.bonificacao =  self.bonificacao

        elif(column_name.find("-") >= 0):
            self.data    =      datetime.strptime(self.tableWidget.item(0, currentColumn).text(), "%d-%m-%Y").strftime("%d-%m-%Y")
            self.situacao    =  self.tableWidget.item(currentRow, currentColumn).text()

            cont2   = 0
            if(self.situacao.upper() == "OK" or self.situacao.upper() == "F" or self.situacao.upper() == "MP"):
                indices = []
                cont = 0
                
                
                if(self.db_response_2 == False or self.edited == True):
                    pass
                else:
                    for row in self.db_response_2:
                        self.data_func  = datetime.strptime(str(row[3]), "%Y-%m-%d %H:%M:%S")
                        if(self.data == self.data_func.strftime("%d-%m-%Y") and self.funcionario == row[0]):
                            indices.append(cont)
                            #print('AQUI ROW', " - ", row)
                        cont += 1

                    self.message_box            = QMessageBox()
                    self.message_box.setIcon(QMessageBox.Information)
                    self.message_box.setWindowTitle("Warning!")
                    self.message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                    
                    if(self.edited == True):
                        pass
                    else:
                        if(len(indices) == 1):
                            
                            texto   = """O funcionario "{}" ja se encontra vinculado na seguinte obra:\n"{}" """.format(
                                self.funcionario,
                                self.db_response_2[indices[0]][6]
                            )

                            texto   += """\nDeseja alterar os dados dessas obras para meio período?"""
                            self.message_box.setText(texto)
                            if(self.testeC_ont == 0):
                                result = self.message_box.exec_()
                                if(result == self.message_box.Yes):
                            
                                    self.close_message_1 = True
                                    self.testeC_ont += 1
                                    self.tableWidget.setItem(currentRow, currentColumn, QTableWidgetItem(str("MP")))
                                
                                elif(result == self.message_box.No):
                                    self.testeC_ont += 1
                                    
                            else:
                                self.testeC_ont -= 1
                            
                        elif(len(indices) > 1):

                            cont = 0
                            texto = """O funcionario "{}" ja se encontra vinculado as seguintes obras:\n""".format(
                                        self.funcionario
                                    )
                            for x in indices:
                                texto += """\n{}\n""".format(
                                    self.db_response_2[x][6]
                                )
                                
                            texto   += """Será feito o lançamento como "OK", preencha as horas extras trabalhadas!"""
                            self.message_box.setText(texto)
                            if(self.testeC_ont_2 == 0):
                                result = self.message_box.exec_()

                                if(result == self.message_box.Yes):
                                    self.testeC_ont_2 += 1
                                    self.tableWidget.setItem(currentRow, currentColumn, QTableWidgetItem(str("OK")))
                                    indices.clear()
                                    close_message = True
                                    
                                elif(result == self.message_box.No):
                                    self.testeC_ont_2 += 1
                                   
                            else:
                                self.testeC_ont_2 -= 1

            elif(self.situacao == ""):
                pass
            else:
                texto = """FORMATO INVÁLIDO\nAs síntaxes corretas são:\nOK  -> Expediente normal\nMP  -> Meio expediente\nF   -> Falta"""
                
                self.error_message.setText(texto)
                self.error_message.setWindowTitle("Erro de síntaxe!")
                error_result  = self.error_message.exec_()
                self.tableWidget.setItem(currentRow, currentColumn, QTableWidgetItem(str("")))
                
                                    
            
            if(self.situacao.upper() == "F"):
                self.bonificacao =  None
                self.hora_extra  =  None
                
            else:
                self.bonificacao =  None
                self.hora_extra  =  None

        if(self.bonificacao == None):

            self.bonificacao    = "0.00"
        
        if(self.hora_extra == None):
            self.hora_extra     = "0:00"

        if((self.data) != None):
            
            self.dictData = self.return_dict(
            self.funcionario,
            self.data,
            self.situacao,
            self.hora_extra,
            self.bonificacao,
            self.array
            )

            #print(self.dictData)
    
'''app = QApplication(sys.argv)
window  = QTable()'''
