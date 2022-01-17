from app import app
from app.controller import CategoriesController
from app.controller import ProducsController
from flask import request

@app.route('/')
def hallo():
    return 'Hello Yusup Setiawan'

@app.route('/categories', methods=['GET'])
def categories():
        return CategoriesController.index()

@app.route('/categories/<id>', methods=['GET'])
def categoriesDetail(id):
    return CategoriesController.detail(id)

@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'GET':
        return ProducsController.index()
    else:
        return ProducsController.post()

@app.route('/products/<id>', methods=['GET', 'PUT', 'DELETE'])
def productsDetail(id):
    if request.method == 'GET':
        return ProducsController.detail(id)
    elif request.method == 'PUT':
        return ProducsController.put(id)
    elif request.method == 'DELETE':
        return ProducsController.delete(id)