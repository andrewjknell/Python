from flask import Flask, request, render_template, redirect, session
import random
app = Flask(__name__, static_url_path='/static')
app.secret_key = 'root'

@app.route('/')
def game():
    if 'rand' not in session.keys():
        session['rand'] = random.randint(1,10)
        
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def result():
    pick = request.form['guess']
    if int(pick) > session['rand']:
        session['result'] = 'pick lower!'
        session['color'] = 'red'
    if int(pick) < session['rand']:
        session['result'] = 'pick higher!'
        session['color'] = 'red'
    if int(pick) == session['rand']:
        session['result'] = 'You Win!'
        session['color'] = 'green'
    return redirect('/')

@app.route('/reset')
def logout():
    session.clear()
    return redirect('/')
if __name__=='__main__':
    app.run(debug=True)