from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<num>')
def checkerboard(num):
    return render_template('indexc.html',num = int(num))

if __name__ == '__main__':
    app.run(debug=True)