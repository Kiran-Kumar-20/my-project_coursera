from flask import Flask, jsonify, request

app = Flask(__name__)

# Example in-memory storage
products = []

@app.route('/products', methods=['GET'])
def list_products():
    name = request.args.get('name')
    if name:
        filtered = [p for p in products if p['name'] == name]
        return jsonify(filtered), 200
    return jsonify(products), 200

@app.route('/products', methods=['POST'])
def create_product():
    product = request.json
    product['id'] = len(products) + 1
    products.append(product)
    return jsonify(product), 201

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    product.update(request.json)
    return jsonify(product), 200

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    products = [p for p in products if p['id'] != product_id]
    return '', 204
