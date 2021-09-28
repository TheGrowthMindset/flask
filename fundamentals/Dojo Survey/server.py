from flask import Flask, render_template, session, redirect,request

app = Flask(__name__)

import secrets 
secret_key = secrets.token_hex(16)
app.config['SECRET_KEY'] = secret_key

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process',methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/success')

@app.route('/result', methods=['GET'])
def success():
    return render_template('success.html')
    
if __name__=="__main__":
    app.run(debug=True)