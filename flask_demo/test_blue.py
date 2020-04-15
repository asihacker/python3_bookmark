#!/usr/bin/python
# coding=utf-8
from flask import blueprints, request, jsonify

index_page = blueprints.Blueprint('index_page', __name__)


@index_page.route('/my')
def index():
    return 'asihacker3'


@index_page.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    a = {'f': f'{f}'}
    print(type(jsonify(a)), jsonify(a))
    return jsonify(a)
