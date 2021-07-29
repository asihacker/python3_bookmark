#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 17:48
# @Author  : AsiHacker
# @File    : demo.txt.txt.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from flask import Flask, jsonify, abort, request

app = Flask(__name__)
books = [
    {
        'id': 1,
        'title': u'论语',
        'auther': u'孔子',
        'price': 18
    },
    {
        'id': 2,
        'title': u'道德经',
        'auther': u'老子',
        'price': 15
    }
]


@app.route('/bookstore/api/v1/books', methods=['GET'])
def get_tasks():
    return jsonify({'books': books})


@app.route('/bookstore/api/v1/books/<int:id>', methods=['GET'])
def get_task(id):
    for book in books:
        if book['id'] == id:
            return jsonify({'book': book})
    abort(404)


@app.route('/bookstore/api/v1/books/', methods=['POST'])
def create_task():
    if not request.form or not 'title' in request.form:
        abort(400)
    book = {
        'id': books[-1]['id'] + 1,
        'title': request.form['title'],
        'auther': request.form['auther'],
        'price': request.form['price'],
    }
    books.append(book)
    return jsonify({'book': book}), 201


@app.route('/bookstore/api/v1/books/<int:id>', methods=['PUT'])
def update_book(id):
    for book in books:
        if book['id'] == id:
            book["title"] = request.form['title']
            book["auther"] = request.form['auther']
            book["price"] = request.form['price']
        return jsonify({'books': books})
    abort(400)


@app.route('/bookstore/api/v1/books/<int:id>', methods=['DELETE'])
def delete_task(id):
    for book in books:
        if book['id'] == id:
            books.remove(book)
            return jsonify({'result': True})
    abort(404)

    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)
