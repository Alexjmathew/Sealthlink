from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/products')
def products():
    return render_template('products.html')

if __name__ == '__main__':
    # For local development only
    app.run(host='0.0.0.0', port=5000, debug=False)
