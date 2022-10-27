#!/usr/bin/python
# -*- coding: utf-8 -*-

from app import create_app
from test.config.mysql import db_info
import pymysql

def preparing_db():

    db = pymysql.connect(
        db_info.get('host'),
        db_info.get('user'),
        db_info.get('password'),
        db_info.get('database')
    )

    cursor = db.cursor()

    sql = 'drop table if exists pessoa;'
    sql = sql + 'create table pessoa(id serial, '
    sql = sql + 'nome varchar(255) not null, '
    sql = sql + 'cpf varchar(255) not null, primary key(id));'

    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

app = create_app(db_info)

@app.route('/api')
def index():
    return 'API com Testes - Ambiente de Teste'

if __name__ == '__main__':
    preparing_db()
    app.run()

