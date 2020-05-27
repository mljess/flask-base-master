## models.py
from banco import bd


class Presenca:
    def __init__(self, email, presenca, resposta, comentarios):
        self.email = email
        self.presenca = presenca
        self.resposta = resposta
        self.comentarios = comentarios


    def gravar(self):
        sql = '''insert into presencas (email, presenca, resposta, comentarios) values (?, ?, ?, ?)'''
        primeiro_interrogacao = self.email
        segundo_interrogacao = self.presenca
        terceiro_interrogacao = self.resposta
        quarto_interrogacao = self.comentarios
        bd().execute(sql, [primeiro_interrogacao, segundo_interrogacao, terceiro_interrogacao, quarto_interrogacao])
        bd().commit()

 
    @staticmethod
    def recupera_todas():
        ## Usamos o objeto retornado por bd() para realizar comandos sql
        sql = '''select email, presenca, resposta, comentarios from presencas order by id desc'''
        cur = bd().execute(sql)
        ## Montamos dicionário dicionários com os resultados da consulta para passar para a view
        presencas = []
        for email, presenca, resposta, comentarios in cur.fetchall(): # fetchall() gera uma lista com os resultados:
            presente = Presenca(email, presenca, resposta, comentarios)
            presencas.append(presente)
        
        return presencas