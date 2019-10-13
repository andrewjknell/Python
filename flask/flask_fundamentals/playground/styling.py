from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play/<times>/<color>')
def blocks(times,color):
    return render_template("indexbox.html", times = int(times), color = color)

if __name__ == "__main__":
    app.run(debug=True)