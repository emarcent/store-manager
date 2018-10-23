from flask import Flask
from api.views import app, add_products,view_products,create_sale_record,view_sales,get_product,get_sale
if __name__ =="__main__":
    app.run(debug=True)
