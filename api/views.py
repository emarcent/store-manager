from flask import Flask,jsonify,request
from .models import Product,Sale_record
from .utilities import errors


app = Flask(__name__)

products = []
sales_record = []

@app.route("/products", methods = ["POST"])
def add_products():
    data = request.get_json()
    if errors(data):
        return jsonify({
            "message": "these fields can't be empty"
        }), 400
    name = data.get("name")
    quantity = data.get("quantity")
    unit_price = data.get("unit_price")
    id_number = data.get("id_number")

        
    product = Product(name,quantity,unit_price,id_number)
    products.append(product)
    return jsonify({
        "message": "product added"
    }), 201


@app.route("/products",methods = ["GET"])
def view_products():
    if len(products) == 0:
        return jsonify({
           "message": "products not found"
        }), 200
    all_products = [prod.name for prod in products]
    return jsonify(all_products), 200


@app.route("/products",methods = ["POST"])   
def create_sale_record():
    data = request.get_json()
    date = data.get("date")
    name = data.get("name")
    quantity = data.get("quantity")
    unit_price = data.get("unit_price")
    id_number = data.get("id_number") 

    if date is False or name is False or quantity is False or unit_price is False or id_number is False:
        return jsonify({
             "message": "fields can't be left empty"
        }), 400
    sale_record = sale_record(date,name,quantity,unit_price,id_number)
    sales_record.append(dict(sale_record))
    return jsonify({
         "message":"sale record added"
    }), 201


@app.route("/products",methods = ["GET"] )
def view_sales():
    if len(sales_record)==0:
        return jsonify({
            "message": "sale doesn't exist"
        }), 404
    return jsonify({
        "sale": sales_record
    }), 200


@app.route("/products",methods = ["GET"])
def get_product(product_id):
    for product in products:
        if product["product_id"] == product_id:
            return jsonify(product)
    return jsonify({
            "message": "product not found"
    }), 404


@app.route('/api/v1/sales/<int:sale_id>', methods=["GET"])
def get_sale(sale_id):
    for sale in Sale_record:
        if sale["sale_id"] == sale_id:
            return jsonify(sale)
    return jsonify({
        "message": "Sale order not found"
    }), 404
        

