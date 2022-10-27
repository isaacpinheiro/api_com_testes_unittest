#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, request
from src.model.pessoa import Pessoa

pessoa_controller = Blueprint('pessoa_controller', __name__)
pessoa = Pessoa()

@pessoa_controller.route('/', methods=['GET'])
def find():
    return jsonify(pessoa.find())

@pessoa_controller.route('/<_id>', methods=['GET'])
def find_one(_id):
    return jsonify(pessoa.find_one(_id))

@pessoa_controller.route('/', methods=['POST'])
def insert():
    obj = request.json
    _id = pessoa.insert(obj)
    return {'msg': 'success', 'id': _id}

@pessoa_controller.route('/', methods=['PUT'])
def update():
    obj = request.json
    pessoa.update(obj)
    return {'msg': 'success'}

@pessoa_controller.route('/<_id>', methods=['DELETE'])
def delete(_id):
    pessoa.delete(_id)
    return {'msg': 'success'}

