from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def survery_result():
    print(request.form)
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comments = request.form['comments']
    return render_template('results.html', return_comments=comments, return_name = name, return_loc=location, return_lang = language)

if __name__=="__main__":
    app.run(debug=True)