from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

imageDir = "img/"

fruitsList = [
    {"name": "Strawberry", "image": "strawberry.png"},
    {"name": "Raspberry", "image": "raspberry.png"},
    {"name": "Blackberry", "image": "blackberry.png"},
    {"name": "Apple", "image": "apple.png"}
]

@app.errorhandler(404)
def not_found(e):
    return "<p>¡Lo siento! No hay respuesta. Inténtalo otra vez</p>"

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", fruits = fruitsList)

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)

    dt = datetime.now()

    total = int(request.form["Strawberry"]) + int(request.form["Raspberry"]) + int(request.form["Blackberry"]) + int(request.form["Apple"])
    
    newOrder = {
        "date": f"{dt.strftime('%B %drd %Y %H:%M:%S %p')}",
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "student_id": request.form["student_id"],
        "fruits": [
            {"name": "Strawberry", "quantity": int(request.form["Strawberry"])},
            {"name": "Raspberry", "quantity": int(request.form["Raspberry"])},
            {"name": "Blackberry", "quantity": int(request.form["Blackberry"])},
            {"name": "Apple", "quantity": int(request.form["Apple"])}
        ],
        "total": total
    }

    print(f"Cobrando a {request.form['first_name']} {request.form['last_name']} por {total} frutas")

    return render_template("checkout.html", order = newOrder)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html", dir = imageDir, fruits = fruitsList)

if __name__ == "__main__":
    app.run( debug = True )