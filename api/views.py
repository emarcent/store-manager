from flask import Flask,jsonify,request
from models import Product

app = Flask(__name__)

products = []

@app.route("/products", methods = ["POST"])
def add_products():
    data = request.get_json()
    name = data.get("name")
    quantity = data.get("quantity")
    unit_price = data.get("unit_price")

    if name is False or quantity is False or unit_price is False:
        return jsonify({
            "message": "these fields can't be empty"
        }), 400
    product = Product(name,quantity,unit_price)
    products.append(dict(product))
    return jsonify({
        "message": "product added"
    }), 201


@app.route("/products",methods = ["GET"])
def view_products():
    if len(products) == 0:
        return jsonify({
           "message": "product doesn't exit"
        }), 404
    return jsonify({
        'product': products
    }), 200    
