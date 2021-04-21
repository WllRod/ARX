import mysql.connector
import json
from os import getcwd, path
from collections import namedtuple
import base64
from src.Password_Hash.hash import check_password, get_hashed_password
from os import path
import ctypes
import queue
import random, string
from datetime import datetime
import time
#from Password_Hash.hash import check_password, get_hashed_password

def error_box(text):
    result = ctypes.windll.user32.MessageBoxW(0, text, "ERROR", 0x10)

class DB():
    def __init__(self):

        try:
            
            arq         = open('config.json', 'r')
            json_data   = json.load(arq)
            arq.close()

            self.cnxn   = mysql.connector.connect(
                host=json_data['Connector']['Server'],
                user=json_data['Connector']['User'],
                password=json_data['Connector']['Password'],
                database=json_data['Connector']['Database'],
                port=json_data['Connector']['Port'],
                connect_timeout=10000
            ) 

            self.cursor = self.cnxn.cursor(buffered=True)
        except Exception as e:
            error_box(str(e))
            raise Exception(e)
    
    def __del__(self):
        
        self.cnxn.close()
        
    def set_data(self, query):
        try:
            self.cursor.execute(query)
            self.cnxn.commit()
        except(AttributeError, mysql.connector.errors.OperationalError):
            arq         = open('config.json', 'r')
            json_data   = json.load(arq)
            arq.close()

            self.cnxn   = mysql.connector.connect(
                host=json_data['Connector']['Server'],
                user=json_data['Connector']['User'],
                password=json_data['Connector']['Password'],
                database=json_data['Connector']['Database'],
                port=json_data['Connector']['Port'],
                connect_timeout=10000
            ) 

            self.cursor = self.cnxn.cursor(buffered=True)
            self.cursor.execute(query)
            self.cnxn.commit()

        
    
    def get_data(self, query):
        try:
            self.cursor.execute(query)
            q   = self.cursor.fetchall()
            
            if(q == [] or q == None):

                return False
            else:
                return q
        except(AttributeError, mysql.connector.errors.OperationalError):
            arq         = open('config.json', 'r')
            json_data   = json.load(arq)
            arq.close()

            self.cnxn   = mysql.connector.connect(
                host=json_data['Connector']['Server'],
                user=json_data['Connector']['User'],
                password=json_data['Connector']['Password'],
                database=json_data['Connector']['Database'],
                port=json_data['Connector']['Port'],
                connect_timeout=10000
            ) 

            self.cursor = self.cnxn.cursor(buffered=True)
            self.cursor.execute(query)
            q   = self.cursor.fetchall()
            if(q == []):
                return False
            else:
                return q
class DB_Login():
    def __init__(self):
        self.db     = DB()
        
    def login(self, username, password, q):
        self.authorized = False
        query   = """SELECT ID AS "ID" FROM USERS WHERE USERNAME='{}'""".format(username)
        execute = self.db.get_data(query)

        if(execute == False):
            q.put(False)
        else:
            query   = """SELECT PASSW AS "P" FROM USERS WHERE ID='{}'""".format(execute[0][0])
            execute = self.db.get_data(query)
            
            if(check_password(password, execute[0][0])):
                query   = """SELECT PERMISSION FROM USERS WHERE ID='{}'""".format(execute[0][0])
                '''return True'''
                q.put(True)
            else:
                q.put(False)
    
    def return_perm(self, user):
        query   = """
        SELECT PERMISSION FROM USERS WHERE USERNAME='{}'
        """.format(user)

        try:
            return self.db.get_data(query)
        except Exception as e:
            error_box(str(e))
    def return_all_users(self, q=None):
        data_tuple  = namedtuple('Dados', 'ID USER NAME PERMISSION')
        array       = []
        query       =   """
                    SELECT  ID AS "ID", 
                            USERNAME AS "USER", 
                            NAME AS "NAME", 
                            PERMISSION AS "PERM" 
                    FROM USERS
                        """

        for data in self.db.get_data(query):
            s   = data_tuple(data[0], data[1], data[2], data[3])
            array.append(s)
        if(q == None):
            return array

        else:
            q.put(array)
    
    def close(self):
        self.db.cursor.close()
        self.db.cnxn.close()

class DB_Alter():
    def __init__(self):
        self.db = DB()

    def delete_user(self, id, ):
        query   = """DELETE FROM USERS WHERE ID='{}'""".format(id)
        self.db.set_data(query)
        

        return True
    
    def add_user(self, user, name, passw, perm, q):
        verify_query    = """
        SELECT 
            USERNAME AS "USER",
            NAME     AS "NAME"
        FROM USERS
            WHERE USERNAME='{}' OR NAME='{}'
        """.format(user, name)

        response    = self.db.set_data(verify_query)
        if(response == None):
            query   = """
            INSERT INTO USERS(
                USERNAME, 
                NAME, 
                PASSW, 
                PERMISSION
            )VALUES (
                '{}',
                '{}',
                '{}',
                 {}
            ) 
            """.format(
                user,
                name,
                get_hashed_password(passw),
                perm
            )
            self.db.set_data(query)
            
            q.put(DB_Login().return_all_users())
        else:
            if(response[0][0] == user):
                return "Já existe um cadastro com este usuário!"
            elif(response[0][1] == name):
                return "Já existe um cadastro com este nome!"
    def user_data(self, id):
        query   = """
        SELECT 
            USERNAME AS "USER",
            NAME     AS "NAME",
            PASSW    AS "PASSWORD",
            PERMISSION AS "PERM"
        FROM USERS WHERE ID='{}'
        """.format(id)

        return self.db.get_data(query)[0]

    def update(self, id, user, name, password, perm, hash):

        if(hash):
            password    = get_hashed_password(password)
        query = """UPDATE USERS SET 
                            USERNAME='{}',
                            NAME='{}',
                            PASSW='{}',
                            PERMISSION='{}'
                    WHERE ID='{}'""".format(
                        user,
                        name,
                        password,
                        perm,
                        id
                    )
        
        self.db.set_data(query)
        return True

    def close(self):
        self.db.cursor.close()
        self.db.cnxn.close()

class SQL_Funcionario():
    def __init__(self):
        self.db = DB()
    
    def return_all_funcs(self, q=None):

        try:
            data_tuple  = namedtuple('Data', 'ID NOME CPF RG')
            array       = []
            query   = """
            SELECT 
                ID AS "ID",
                NOME AS "NOME",
                CPF AS "CPF", 
                RG AS "RG"
            FROM FUNCIONARIOS
            """
            
            if(q == None):
                execute = self.db.get_data(query)
               
                return execute
            else:
                execute = self.db.get_data(query)
              
                q.put(execute)
        except Exception as e:
            error_box(str(e))

    def add_func(self, nome, rg, cpf, salario_hora, data_nascimento, email, telefone, horas_trab, funcao, q=None):
        try:
            query   = """
            INSERT INTO FUNCIONARIOS(NOME, RG, CPF, SALARIO_HORA, DATA_NASCIMENTO, EMAIL, TELEFONE, HORAS_TRAB, FUNCAO)
            VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')
            """.format(
                nome,
                rg,
                cpf,
                salario_hora,
                data_nascimento,
                email,
                telefone,
                horas_trab,
                funcao
            )
            
            if(self.db.set_data(query)):
                q.put(self.return_all_funcs())
            else:
                return False
        except Exception as e:
            error_box(str(e))

    def exclude_func(self, id):

        try:
            query   = """
            DELETE FROM FUNCIONARIOS WHERE ID='{}'
            """.format(id)

            self.db.set_data(query)
            return True
        except Exception as e:
            error_box(str(e))

    def return_users_data(self, id):
       
        query   = """
            SELECT 
                F.ID, 
                F.NOME, 
                F.CPF,
                F.RG,
                F.SALARIO_HORA,
                F.DATA_NASCIMENTO,
                F.EMAIL,
                F.TELEFONE,
                F.HORAS_TRAB,
                F.FUNCAO,
                C.DESCRICAO
            FROM FUNCIONARIOS F JOIN CARGOS C ON C.ID = F.FUNCAO
            WHERE F.ID='{}'
        """.format(id)

        return self.db.get_data(query)
    
    def update_funcionario(self, ID, name, cpf, rg, salario, data, email, telefone, horas, funcao):

        try:
            query   = """
            UPDATE FUNCIONARIOS SET NOME='{}',
                    CPF='{}',
                    RG='{}',
                    SALARIO_HORA='{}',
                    DATA_NASCIMENTO='{}',
                    EMAIL='{}',
                    TELEFONE='{}',
                    HORAS_TRAB='{}',
                    FUNCAO='{}'
                WHERE ID='{}'
            """.format(
                name,
                cpf,
                rg, 
                salario,
                data,
                email,
                telefone,
                horas,
                funcao, 
                ID
            )
            self.db.set_data(query)
            return True
        except Exception as e:
            error_str(str(e))
    
    def funcs_atribuidos(self, id_obra):
        query   = """
        SELECT ID_FUNC FROM OBRAS WHERE UNIQUE_KEY='{}'
        """.format(
            id_obra
        )

        query_2 = """
        SELECT DESCRICAO FROM OBRAS WHERE UNIQUE_KEY='{}'
        """.format(
            id_obra
        )

        dataTuple   = {
            "Funcionarios"  : self.db.get_data(query),
            "Descricao_Obra": self.db.get_data(query_2) 
        }

        try:
            return dataTuple 
        except Exception as e:
            error_box(str(e))

class Funcoes():
    def __init__(self):
        self.db = DB()

    def return_funcoes(self, q=None):
        try:
            query   = """SELECT DESCRICAO AS "DESCRICAO", ID AS "ID" FROM CARGOS"""
            
            if(q == None):
                return self.db.get_data(query)
            else:
                q.put(self.db.get_data(query))
        except Exception as e:
            error_box(str(e))
    
    def return_funcao_data(self, id):
        try:
            query   = """
            SELECT 
                ID AS "ID",
                DESCRICAO AS "DESCRICAO"
            FROM CARGOS WHERE ID='{}'
            """.format(str(id))

            return self.db.get_data(query)
        except Exception as e:
            error_box(str(e))

    def add_funcao(self, descricao, screen_1=None, screen_2=None, screen_3=None):

        try:
            query   = """
            INSERT INTO CARGOS (DESCRICAO) VALUES ('{}')
            """.format(descricao)
            self.db.set_data(query)
            
            return True
        except Exception as e:
            error_box(str(e))

    def del_cargo(self, id):

        try:
            query   = """
            DELETE FROM CARGOS WHERE ID='{}'
            """.format(id)

            self.db.set_data(query)
            
            return True
        except Exception as e:
            error_box(str(e))

    def edit_cargo(self, id, descricao):

        try:
            query   = """
            UPDATE CARGOS SET DESCRICAO='{}' WHERE ID='{}'
            """.format(descricao, id)

            self.db.set_data(query)
            return True
        except Exception as e:
            error_box(str(e))

class Obras():
    def __init__(self):
        self.db = DB()
        self.fp = FolhaDePonto()

    def return_obra_data(self, id):
        try:
            query   = """
            SELECT * FROM OBRAS WHERE UNIQUE_KEY='{}'
            GROUP BY UNIQUE_KEY
            """.format(id)
            return self.db.get_data(query)
        except Exception as e:
            error_box(str(e))

    def add_obras(self, funcList, descricao, date, cnpj):

        try:
            key = ''.join(random.SystemRandom().choice(string.digits) for _ in range(5))


            for data in funcList:
                query   = """
                INSERT INTO OBRAS (DESCRICAO, ID_FUNC, DATA_CONCLUSÃO, UNIQUE_KEY, ID_CLIENTE) SELECT '{}', F.ID, '{}', '{}', C.ID FROM FUNCIONARIOS F JOIN CLIENTES C WHERE F.ID='{}' AND C.CNPJ='{}'
                """.format(descricao, date, key,  data, cnpj )
                
                self.db.set_data(query)
            #self.fp.add_obra(key)
            return True
        except Exception as e:
            error_box(str(e))

    def update_obras(self, desc, data, cnpj, id_obra):
        try:
            query   = """
            UPDATE OBRAS O JOIN CLIENTES C  SET O.ID_CLIENTE=C.ID, O.DATA_CONCLUSÃO='{}', O.DESCRICAO='{}' WHERE C.CNPJ='{}' AND O.UNIQUE_KEY='{}'
            """.format(data, desc, cnpj, id_obra)
            self.db.set_data(query)
            return True
        except Exception as e:
            error_box(str(e))
    def return_obras_list(self, q=None):

        try:
            query   = """
            SELECT UNIQUE_KEY AS "KEY", DESCRICAO AS "DESCRICAO" FROM OBRAS
            GROUP BY DESCRICAO
            ORDER BY ID DESC
            """

            if(q == None):
                teste   = self.db.get_data(query)
                return teste
            else:
                q.put(self.db.get_data(query))
        except Exception as e:
            error_box(str(e))
    
    def del_obra(self, listID):

        try:
            for x in listID:
                query   = """
                DELETE FROM OBRAS WHERE UNIQUE_KEY='{}'
                """.format(x)

                self.db.set_data(query)
            return True
        except Exception as e:
            error_box(str(e))
        
    def del_func_obra(self, id_obra, id_func):

        query   = """
        SELECT O.ID, FP.ID_OBRA FROM OBRAS O JOIN FOLHA_PONTO FP ON FP.OBRA_UNIQUE_KEY = O.UNIQUE_KEY
        WHERE O.UNIQUE_KEY='{}'
        """.format(id_obra)

        if(self.db.get_data(query) == False):
            query_1 = """
            DELETE FROM OBRAS WHERE UNIQUE_KEY='{}' AND ID_FUNC='{}'
            """.format(id_obra, id_func)

            query_2 = """SELECT 'PASS'"""
        else:
            query_1   = """
            DELETE T1 FROM FOLHA_PONTO T1 JOIN OBRAS T2 ON T1.OBRA_UNIQUE_KEY = T2.UNIQUE_KEY AND T1.ID_OBRA = T2.ID
            WHERE T2.UNIQUE_KEY='{}' AND T2.ID_FUNC='{}'
            """.format(
                id_obra,
                id_func
            )

            query_2   = """
            DELETE FROM OBRAS WHERE UNIQUE_KEY='{}' AND ID_FUNC='{}'
            """.format(
                id_obra,
                id_func
            )

        try:
           
            self.db.set_data(query_1)
            self.db.set_data(query_2)
            return True
        except Exception as e:
            error_box(str(e))
    
    def add_func_obra(self, id_obra, id_func):

        query   = """
        INSERT INTO OBRAS (DESCRICAO, ID_FUNC, UNIQUE_KEY) 
            SELECT DESCRICAO, '{}', UNIQUE_KEY FROM OBRAS 
        WHERE UNIQUE_KEY='{}' AND NOT EXISTS (
            SELECT ID_FUNC FROM OBRAS WHERE ID_FUNC='{}'
        )
            GROUP BY UNIQUE_KEY
        """.format(id_func, id_obra, id_func)
        print(query)

        try:
            self.db.set_data(query)
            return True
        except Exception as e:
            error_box(str(e))

class FolhaDePonto():
    def __init__(self):
        self.db = DB()

    def return_data(self, id):
        try:
            query   = """
            SELECT MIN(DATA), MAX(DATA) FROM FOLHA_PONTO WHERE OBRA_UNIQUE_KEY='{}'
            """.format(id)

            return self.db.get_data(query)
        except Exception as e:
            error_box(str(e))
            
    def verification(self, id_obra, id_func, data):
        try:
            query   = """
            SELECT * FROM FOLHA_PONTO WHERE DATA='{}' AND OBRA_UNIQUE_KEY='{}' AND ID_OBRA='{}'
            """.format(data, id_obra, id_func)
            q   = self.db.get_data(query)
            if(q == False):
                pass
            else:
                query_2 = """
                DELETE FROM FOLHA_PONTO WHERE DATA='{}' AND OBRA_UNIQUE_KEY='{}' AND ID_OBRA='{}'
                """.format(data, id_obra, id_func)
                self.db.set_data(query_2)
            return True
        except Exception as e:
            error_box(str(e))

    def lists(self, q=None):
        query   = """
        SELECT FP.OBRA_UNIQUE_KEY AS "ID", O.DESCRICAO AS "DESC",  MIN(FP.DATA), MAX(FP.DATA)

        FROM FOLHA_PONTO FP JOIN OBRAS O ON O.UNIQUE_KEY = FP.OBRA_UNIQUE_KEY

        GROUP BY FP.OBRA_UNIQUE_KEY
        """
        try:
            if(q == None):
                return self.db.get_data(query)
            else:
                q.put(self.db.get_data(query))
        except Exception as e:
            error_box(str(e))
    def return_folha(self, q=None):

        try:
            array   = []
            query   = """
            SELECT O.UNIQUE_KEY AS "ID", O.DESCRICAO AS "DESCRICAO", O.DATA_CONCLUSÃO AS "DATA" FROM OBRAS O
            GROUP BY O.UNIQUE_KEY, O.DESCRICAO, O.DATA_CONCLUSÃO
            """.format(id)
            dataTuple   = namedtuple('Data', 'ID DESCRICAO DATA')
            get_data    = self.db.get_data(query)
            if(get_data == [] or get_data == False):
                s   = dataTuple(None, None, None)
            else:
                for x in self.db.get_data(query):
                    s   = dataTuple(x[0], x[1], x[2])
                    array.append(s)
            if(q == None):
                return array
            else:
                q.put(array)
        except Exception as e:
            error_box(str(e))

    def return_func_obra(self, id, folha_existente=None, data_inicial=None, data_final=None):

        try:
            query   = """
            SELECT F.NOME, F.SALARIO_HORA, F.HORAS_TRAB, O.UNIQUE_KEY, O.ID FROM FUNCIONARIOS F JOIN OBRAS O 
                ON O.ID_FUNC = F.ID
            WHERE O.UNIQUE_KEY='{}'
            """.format(id)
            
            query_func = """
            SELECT F.NOME, FP.DATA, FP.SITUACAO, FP.HORA_EXTRA, FP.BONIFICACAO FROM FOLHA_PONTO FP JOIN OBRAS O ON FP.ID_OBRA = O.ID JOIN FUNCIONARIOS F ON O.ID_FUNC = F.ID WHERE FP.OBRA_UNIQUE_KEY='{}'
            """ .format(id)

            if(folha_existente != None):
                query_func += " AND FP.DATA>='{}' AND FP.DATA<='{}'".format(data_inicial, data_final)
                
            query2 = """
            SELECT F.NOME, F.SALARIO_HORA, F.HORAS_TRAB, FP.`DATA`, O.UNIQUE_KEY, O.ID, O.DESCRICAO, FP.SITUACAO FROM FUNCIONARIOS F JOIN OBRAS O 
                ON O.ID_FUNC = F.ID
                JOIN FOLHA_PONTO FP
                ON FP.OBRA_UNIQUE_KEY = O.UNIQUE_KEY
                AND FP.ID_OBRA = O.ID
            """

            array = []
            response = self.db.get_data(query_func)
            tupleTeste = namedtuple('DADOS', 'FUNC DATA SITUACAO HORA_EXTRA BONIFICACAO')
            if(response == False):
                pass
            else:
                for x in response:
                    s = tupleTeste(x[0], datetime.strptime(str(x[1]), "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y"), x[2], x[3], x[4])
                    array.append(s)



            return (self.db.get_data(query), self.db.get_data(query2), array)

        except Exception as e:
            error_box(str(e))
    
    def add_obra(self, id):

        try:
            query   = """
            INSERT INTO FOLHA_PONTO (ID_OBRA, OBRA_UNIQUE_KEY) SELECT ID, UNIQUE_KEY FROM OBRAS WHERE UNIQUE_KEY='{}'
            """.format(id)

            self.db.set_data(query)
            return True
        except Exception as e:
            error_box(str(e))
    
    def add_folha_values(self, id_obra, data, situacao, hora_extra, valor_total, id_obra_func, bonificacao, valor_hora_extra, valor_dia):
        try:
            query   = """
            INSERT INTO FOLHA_PONTO 
                (
                    DATA, 
                    SITUACAO, 
                    HORA_EXTRA, 
                    VALOR_TOTAL, 
                    OBRA_UNIQUE_KEY, 
                    ID_OBRA, 
                    BONIFICACAO, 
                    VALOR_HORA_EXTRA, 
                    VALOR_DIA
                )
            SELECT 
                '{}', 
                '{}', 
                '{}', 
                '{}', 
                UNIQUE_KEY, 
                ID, 
                '{}', 
                '{}', 
                '{}' 
            FROM OBRAS WHERE UNIQUE_KEY='{}' AND ID='{}'
            """.format(
                data, 
                situacao, 
                hora_extra, 
                valor_total, 
                bonificacao, 
                valor_hora_extra,
                valor_dia,
                id_obra, 
                id_obra_func
            )
            
            self.db.set_data(query)
            return True

        except Exception as e:
            error_box(str(e))    

    def update_folha_value(self, situacao, id_obra, obra_unique_key):

        try:
            query   = """
            UPDATE FOLHA_PONTO SET 
                SITUACAO='{}',
                VALOR_DIA=VALOR_DIA / 2,
                VALOR_TOTAL=VALOR_DIA+VALOR_HORA_EXTRA+BONIFICACAO
            WHERE ID_OBRA='{}' AND OBRA_UNIQUE_KEY='{}'
            """.format(
                situacao,
                id_obra,
                obra_unique_key
            )
            self.db.set_data(query)
            return True
        except Exception as e:
            error_box(str(e))

    def delete_folha(self, idList):

        try:
            for x in idList:
                query   = """
                DELETE FROM FOLHA_PONTO WHERE OBRA_UNIQUE_KEY='{}'
                """.format(x)
                self.db.set_data(query)
            return True
        except Exception as e:
            error_box(str(e))

class Clientes_DB():
    def __init__(self):
        self.db = DB()
    
    def add_cliente(self, cnpj, nome, email, telefone, endereco):
        query   = """
        INSERT INTO CLIENTES(CNPJ, NOME, EMAIL, TELEFONE, ENDERECO)
        VALUES ('{}', '{}', '{}', '{}', '{}')
        """.format(
            cnpj,
            nome,
            email,
            telefone,
            endereco
        )

        try:
            self.db.set_data(query)
            return True
        except Exception as e:
            error_box(str(e))

    def return_clientes(self, q=None):
        query   = """
        SELECT ID, CNPJ, NOME FROM CLIENTES
        """

        try:
            if(q == None):
                return self.db.get_data(query)
            else:
                q.put(self.db.get_data(query))
            
        except Exception as e:
            error_box(str(e))

    def delete_cliente(self, list):
        try:
            for x in list:
                query   = """
                DELETE FROM CLIENTES WHERE ID='{}'
                """ .format(x)
                self.db.set_data(query)
        except Exception as e:
            error_box(str(e))

    def return_cliente_data(self, id):
        try:
            query   = """
            SELECT * FROM CLIENTES WHERE ID='{}'
            """ .format(id)
            return self.db.get_data(query)
        except Exception as e:
            error_box(str(e))
    
    def update_cliente(self, id, cnpj, nome, email, telefone, endereco):
        try:
            query   = """
            UPDATE
                CLIENTES
            SET
                CNPJ='{}',
                NOME='{}',
                EMAIL='{}',
                TELEFONE='{}',
                ENDERECO='{}'
            WHERE
                ID='{}'
            """.format(
                cnpj,
                nome,
                email,
                telefone,
                endereco,
                id
            )

            self.db.set_data(query)
            return True
        except Exception as e:
            error_box(str(e))

class Despesas_DB():
    def __init__(self):
        self.db = DB()

    def add_despesa(self, idList, numTitulo, descricao, fornecedor, valor, observacao, data):
        try:
            if(len(idList) >= 1):
                for x in range(len(idList)):
                    query   = """
                    INSERT INTO DESPESAS(
                        NUMERO,
                        DESCRICAO,
                        FORNECEDOR,
                        VALOR,
                        OBSERVACAO,
                        DATA_BAIXA,
                        ID_OBRA
                    ) VALUES (
                        '{}',
                        '{}',
                        '{}',
                        '{}',
                        '{}',
                        '{}',
                        '{}'
                    )
                    """.format(
                        numTitulo,
                        descricao,
                        fornecedor,
                        valor,
                        observacao,
                        data,
                        idList[x]
                    )
                    self.db.set_data(query)
            else:
                query = """
                INSERT INTO DESPESAS(
                    NUMERO,
                    DESCRICAO,
                    FORNECEDOR,
                    VALOR,
                    OBSERVACAO,
                    DATA_BAIXA
                ) VALUES(
                    '{}',
                    '{}',
                    '{}',
                    '{}',
                    '{}',
                    '{}'
                )
                """.format(
                    numTitulo,
                    descricao,
                    fornecedor,
                    valor,
                    observacao,
                    data,
                )
                self.db.set_data(query)
            return True
        except Exception as e:
            error_box(str(e))
    
    def return_data(self, q=None):
        query   = """
        SELECT D.ID, D.NUMERO, D.DESCRICAO, D.VALOR, O.DESCRICAO, D.DATA_BAIXA FROM DESPESAS D LEFT JOIN OBRAS O ON O.UNIQUE_KEY = D.ID_OBRA
        GROUP BY D.ID
        """

        try:
            if(q == None):
                return self.db.get_data(query)
            else:
                q.put(self.db.get_data(query))
        except Exception as e:
            error_box(str(e))

    def del_despesa(self, idList):
        try:
            for x in idList:
                query   = """
                DELETE FROM DESPESAS WHERE ID='{}'
                """.format(x)
                self.db.set_data(query)
            return True
        except Exception as e:
            error_box(str(e))

    def return_despesa_data(self, id):
        try:
            query   = """
            SELECT * FROM DESPESAS WHERE ID='{}'
            """.format(id)
            return self.db.get_data(query)
        except Exception as e:
            error_box(str(e))

    def update_despesa(self, id, descricao, fornecedor, valor, data, observacao, num_titulo):
        try:
            query   = """
            UPDATE 
                DESPESAS 
            SET 
                NUMERO='{}',
                DESCRICAO='{}',
                FORNECEDOR='{}',
                VALOR='{}',
                OBSERVACAO='{}',
                DATA_BAIXA='{}'
            WHERE
                ID='{}'
            """.format(
                num_titulo,
                descricao,
                fornecedor,
                valor,
                observacao,
                data,
                id
            )
            self.db.set_data(query)

            return True
        except Exception as e:
            error_box(str(e))

class Relatorios_DB():
    def __init__(self):
        self.db = DB()

    def despesas(self, data_inicial, data_final):
        query   = """
        SELECT DISTINCT
            D.NUMERO, 
            D.DESCRICAO, 
            D.FORNECEDOR, 
            D.VALOR, 
            CASE WHEN D.ID_OBRA IS NULL THEN "SEM OBRAS VINCULADAS" ELSE O.DESCRICAO END "OBRA",
            D.DATA_BAIXA 
        FROM 
	        DESPESAS D 
        JOIN 
	        OBRAS O  
        WHERE 
	        D.DATA_BAIXA >='{}' AND D.DATA_BAIXA <= '{}'
	     
        """.format(data_inicial, data_final)
        
        return self.db.get_data(query)
    
    def folha_ponto_relat(self, data_inicial, data_final):
        query   = """
        SELECT
            F.NOME,
            FP.DATA,
            FP.SITUACAO,
            FP.VALOR_DIA,
            FP.HORA_EXTRA,
            FP.VALOR_HORA_EXTRA,
            FP.BONIFICACAO
        FROM
	        FOLHA_PONTO FP
        JOIN
	        OBRAS O
        ON
	        FP.OBRA_UNIQUE_KEY = O.UNIQUE_KEY
	
        JOIN
	        FUNCIONARIOS F
        ON
	        F.ID	= O.ID_FUNC
        WHERE
            FP.DATA>='{}' AND
            FP.DATA<='{}'
        """.format(data_inicial, data_final)

        try:
            return self.db.get_data(query)
        except Exception as e:
            error_box(str(e))
    
    def relat_folha_Ponto_simples(self, data_inicial, data_final):
        query   = """
        SELECT 
            F.NOME,
            MIN(FP.DATA),
            MAX(FP.DATA),
            COUNT(CASE WHEN FP.SITUACAO = "00:00:00" THEN 1 ELSE NULL END) AS "FALTAS",
            MAX(FP.VALOR_DIA),
            FP.HORA_EXTRA,
            FP.VALOR_HORA_EXTRA,
            FP.BONIFICACAO,
            SUM(FP.VALOR_TOTAL)
        FROM 
 	        FOLHA_PONTO FP 
        JOIN 
	        OBRAS O 
        ON 
	        O.ID = FP.ID_OBRA
        JOIN 
	        FUNCIONARIOS F
        ON
	        F.ID = O.ID_FUNC
        WHERE FP.DATA>='{}'  AND FP.DATA<='{}'
        GROUP BY FP.ID_OBRA
        """.format(data_inicial, data_final)

        try:
            return self.db.get_data(query)
        except Exception as e:
            error_box(str(e))
    