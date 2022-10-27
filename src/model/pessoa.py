#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.config.mysql import db

class Pessoa:

    def find(self):

        conn = db.connect()
        cursor = conn.cursor()

        sql = 'select * from pessoa;'
        cursor.execute(sql)
        results = cursor.fetchall()
        pessoas = []

        cursor.close()
        conn.close()

        for res in results:

            pessoa = {
                'id': res[0],
                'nome': res[1],
                'cpf': res[2]
            }

            pessoas.append(pessoa)

        return pessoas

    def find_one(self, _id):

        conn = db.connect()
        cursor = conn.cursor()

        sql = 'select * from pessoa where id = %s;'
        cursor.execute(sql, _id)
        results = cursor.fetchall()
        pessoa = None

        cursor.close()
        conn.close()

        if len(results) > 0:

            res = results[0]

            pessoa = {
                'id': res[0],
                'nome': res[1],
                'cpf': res[2]
            }

        return pessoa

    def insert(self, obj):

        conn = db.connect()
        cursor = conn.cursor()

        sql = 'insert into pessoa(nome, cpf) values(%s, %s);'
        cursor.execute(sql, (obj['nome'], obj['cpf']))
        conn.commit()
        _id = cursor.lastrowid

        cursor.close()
        conn.close()

        return _id

    def update(self, obj):

        conn = db.connect()
        cursor = conn.cursor()

        sql = 'update pessoa set nome = %s, cpf = %s where id = %s;'
        cursor.execute(sql, (obj['nome'], obj['cpf'], obj['id']))
        conn.commit()

        cursor.close()
        conn.close()

    def delete(self, _id):

        conn = db.connect()
        cursor = conn.cursor()

        sql = 'delete from pessoa where id = %s;'
        cursor.execute(sql, _id)
        conn.commit()

        cursor.close()
        conn.close()

