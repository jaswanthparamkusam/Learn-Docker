from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', products=get_sample_products())

@app.route('/purchase/<int:product_id>')
def purchase(product_id):
    product = get_product_by_id(product_id)
    if product:
        # In a real application, you would handle the purchase logic here
        return f"You have purchased {product['name']} for ${product['price']}!"
    else:
        return "Product not found"

def get_sample_products():
    return [
        {'id': 1, 'name': 'Robot Model A', 'price': 499.99},
        {'id': 2, 'name': 'Robot Model B', 'price': 699.99},
        {'id': 3, 'name': 'Robot Model C', 'price': 899.99},
    ]

def get_product_by_id(product_id):
    products = get_sample_products()
    return next((product for product in products if product['id'] == product_id), None)

if __name__ == '__main__':
    app.run(debug=True)
