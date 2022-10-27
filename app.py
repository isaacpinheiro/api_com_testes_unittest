#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from src.config.mysql import db_info, db
from src.controller.pessoa_controller import pessoa_controller

def create_app(db_config):

    app = Flask(__name__)

    app.config['MYSQL_DATABASE_USER'] = db_config.get('user')
    app.config['MYSQL_DATABASE_PASSWORD'] = db_config.get('password')
    app.config['MYSQL_DATABASE_DB'] = db_config.get('database')
    app.config['MYSQL_DATABASE_HOST'] = db_config.get('host')
    db.init_app(app)

    app.register_blueprint(pessoa_controller, url_prefix='/api/pessoa')

    return app

app = create_app(db_info)

@app.route('/api')
def index():
    return 'API com Testes'

if __name__ == '__main__':
    app.run()

