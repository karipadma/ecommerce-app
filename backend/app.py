from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/api')
def home():

    return jsonify({
        "status":"healthy",
        "service":"ecommerce-backend"
    })

@app.route('/api/products')
def products():

    return jsonify([
        {
            "id":1,
            "name":"Laptop",
            "price":50000
        },
        {
            "id":2,
            "name":"Phone",
            "price":25000
        }
    ])

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)
