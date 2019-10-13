from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    strawberry = request.form['strawberry']
    raspberry = request.form['raspberry']
    apple = request.form['apple']
    first = request.form['first']
    last = request.form['last']
    id = request.form['id']
    count = int(apple) + int(raspberry) + int(strawberry)
    return render_template("checkout.html", r_apple = apple, r_strawberry = strawberry, r_raspberry = raspberry, first = first, last = last, id_num = id, count = count)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    