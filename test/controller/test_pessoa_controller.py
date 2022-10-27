#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import requests as req
import json

class TestPessoaController(unittest.TestCase):

    URL = 'http://localhost:5000/api/pessoa'

    obj1 = {
        'nome': 'Isaac',
        'cpf': '111.111.111/11'
    }

    obj2 = {
        'nome': 'Lucas',
        'cpf': '222.222.222/22'
    }

    obj3 = {
        'id': 1,
        'nome': 'Isaac',
        'cpf': '111.111.111/11'
    }

    obj4 = {
        'id': 2,
        'nome': 'Lucas',
        'cpf': '222.222.222/22'
    }

    obj5 = {
        'id': 1,
        'nome': 'Isaac',
        'cpf': '123.456.789/10'
    }

    def test_01_insert(self):

        res = req.request('POST', self.URL, json=self.obj1)
        res = json.loads(res.text)

        self.assertEqual(res, {'msg': 'success', 'id': 1})

    def test_02_find_one(self):

        res = req.request('GET', self.URL + '/1')
        res = json.loads(res.text)

        self.assertEqual(res, self.obj3)

    def test_03_find(self):

        res = req.request('POST', self.URL, json=self.obj2)
        res = json.loads(res.text)

        self.assertEqual(res, {'msg': 'success', 'id': 2})

        res = req.request('GET', self.URL)
        res = json.loads(res.text)

        self.assertEqual(res[1], self.obj4)

    def test_04_update(self):

        res = req.request('PUT', self.URL, json=self.obj5)
        res = json.loads(res.text)

        self.assertEqual(res, {'msg': 'success'})

        res = req.request('GET', self.URL + '/1')
        res = json.loads(res.text)

        self.assertEqual(res, self.obj5)

    def test_05_delete(self):

        res = req.request('DELETE', self.URL + '/1')
        res = json.loads(res.text)

        self.assertEqual(res, {'msg': 'success'})

        res = req.request('GET', self.URL)
        res = json.loads(res.text)

        self.assertEqual(len(res), 1)

