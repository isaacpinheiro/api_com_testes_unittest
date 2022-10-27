#!/usr/bin/python
# -*- coding: utf-8 -*-

from flaskext.mysql import MySQL

db_info = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'api_com_testes'
}

db = MySQL()

