from app.models import products
from app.models.categories import Categories
from app.models.products import Products


from app import response, app, db
from flask import request

def index():
    try:
        categories = Categories.query.all()
        data = formatarray(categories)
        return response.success(data, "success")
    except Exception as e:
        print(e)
        return response(), 500
            
def formatarray(datas):
    array = []

    for i in datas:
        array.append(singleObject(i))

    return array

def singleObject(data):
    data = {
        'id' : data.id,
        'name' : data.name
    }

    return data


def detail(id):
    try:
        categories = Categories.query.filter_by(id=id).first()
        products = Products.query.filter(Products.category == id)


        if not categories:
            return response.badRequest([], 'Tidak ada data dosen')

        dataproducts = formatProducts(products)

        data = singleDetailProducts(categories, dataproducts)

        return response.success(data, "success")
    except Exception as e:
        print(e)
        return response(), 500

def singleDetailProducts(categories, products):
    data = {
        'id' : categories.id,
        'name' : categories.name,
        'products' : products
    }

    return data


def singleProducts(products):
    data = {
        'id' : products.id,
        'kode' : products.kode,
        'name' : products.name,
        'harga' : products.harga
    }

    return data

def formatProducts(data):
    array = []
    for i in data:
        array.append(singleProducts(i))
    return array


