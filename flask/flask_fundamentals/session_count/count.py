from flask import Flask, request, render_template, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'root'
 
@app.route("/")
def count():
    if 'count' in session:
        session['count'] = session.get('count') + 1
    else:
         session['count'] = 0
    return render_template('index.html', count = session['count'])

@app.route('/reset')
def reset():
    session.pop('count', None)
    session['count'] = 0
    return redirect('/')

@app.route('/add')
def addTwo():
    if 'count' in session:
        session['count'] = session.get('count')+1
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)