from flask import Flask, render_template, request

app = Flask(__name__)

# Sample menu data
menu = [
    {"name": "Chicken Parmesan", "price": 15.99},
    {"name": "Veggie Wrap", "price": 12.99},
    {"name": "Meatball Sub", "price": 14.99},
    {"name": "Greek Salad", "price": 10.99}
]

# Homepage
@app.route("/")
def index():
    return render_template("index.html", menu=menu)

# Order form
@app.route("/order", methods=["GET", "POST"])
def order():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        order_items = request.form.getlist("order_items")
        print(f"Order received from {name}: {order_items}")
        return "Order received! Thank you for your business."
    return render_template("order.html", menu=menu)

if __name__ == "__main__":
    app.run(debug=True)
