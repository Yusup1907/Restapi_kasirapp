from app.models import products
from app.models.categories import Categories
from app.models.products import Products


from app import response, app, db
from flask import request

def index():
    try:
        products = Products.query.all()
        data = formatarray(products)
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
        'kode' : data.kode,
        'name' : data.name,
        'harga' : data.harga,
        'category' : data.category
    }

    return data


def detail(id):
    try:
        products = Products.query.filter_by(id=id).first()


        categories = Categories.query.filter(Categories == id)

        if not products:
            return response.badRequest([], 'Tidak ada data products')

        datacategories = formatCategories(categories)

        data = singleDetailCategories(products, datacategories)

        return response.success(data, "success")
    except Exception as e:
        print(e)
        return response(), 500

def singleDetailCategories(products, categories):
    data = {
        'id' : products.id,
        'kode' : products.kode,
        'name' : products.name,
        'harga' : products.harga,
        'categories' : categories
    }

    return data


def singleCategories(categories):
    data = {
        'id' : categories.id,
        'name' : categories.name
    }

    return data

def formatCategories(data):
    array = []
    for i in data:
        array.append(singleCategories(i))
    return array


def post():
    try:
        kode = request.form.get('kode')
        name = request.form.get('name')
        harga = request.form.get('harga')
        category = request.form.get('category')

        products = Products(kode=kode, name=name, harga=harga, category=category)
        db.session.add(products)
        db.session.commit()

        return response.success('', 'Sukses Menambahkan Data')
    except Exception as e:
        print(e)
        return response(), 500

def put(id):
    try:
        kode = request.form.get('kode')
        name = request.form.get('name')
        harga = request.form.get('harga')
        category = request.form.get('category')

        input = [
            {
                'kode': kode,
                'name': name,
                'harga': harga,
                'category': category
            }
        ]

        products = Products.query.filter_by(id=id).first()

        products.kode = kode,
        products.name = name,
        products.harga = harga,
        products.category = category

        db.session.commit()

        return response.success('', 'Sukses Mengubah Data')
    except Exception as e:
        print(e)
        return response(), 500


def delete(id):
    try:
        products = Products.query.filter_by(id=id).first()
        if not products:
            return response.badRequest([], 'Tidak ada data products')

        db.session.delete(products)
        db.session.commit()

        return response.success('', 'Sukses Menghapus Data')
    except Exception as e:
        print(e)
        return response(), 500

