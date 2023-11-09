# Step 1: Import necessary libraries
from flask import Flask, jsonify
import pandas as pd

# Step 2: Read CSV Files
customers_df = pd.read_csv('customers_data.csv')
products_df = pd.read_csv('products_data.csv')
sales_df = pd.read_csv('sales_data.csv')
stores_df = pd.read_csv('stores_data.csv')

# Step 3: Initialize Flask App
app = Flask(__name__)

# Step 4: Define Endpoints
@app.route('/customers')
def get_customers():
    return jsonify(customers_df.to_dict(orient='records'))

@app.route('/products')
def get_products():
    return jsonify(products_df.to_dict(orient='records'))

@app.route('/sales')
def get_sales():
    return jsonify(sales_df.to_dict(orient='records'))

@app.route('/stores')
def get_stores():
    return jsonify(stores_df.to_dict(orient='records'))

# Step 5: Run the App
if __name__ == '__main__':
    app.run()