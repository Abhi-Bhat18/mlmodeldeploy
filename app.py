
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/predict',methods = ["POST"])
def playlist():
    if request.method == "POST":
        song = request.form['song']
    return render_template('song.html',s = song)
if __name__ == "__main__":
    app.run(debug=True)