from flask import Flask, render_template, redirect, request, session
import random
import datetime
app = Flask(__name__)
app.secret_key = 'root'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    return render_template('index.html', gold = session['gold'])

@app.route('/process_money', methods = ['POST'])
def process():
    if request.form['building'] == 'cave':
        session['gold'] = session['gold'] + random.randint(5,10)
    if request.form['building'] == 'farm':
        session['gold'] = session['gold'] + random.randint(10,20)
    if request.form['building'] == 'house':
        session['gold'] = session['gold'] + random.randint(2,5)
    if request.form['building'] == 'casino':
        session['gold'] = session['gold'] + random.randint(-50,50)
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)