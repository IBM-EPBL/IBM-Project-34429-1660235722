import numpy as np
import pickle
import inputScript
from flask import Flask, render_template, request
app = Flask(__name__)

model = pickle.load(open('phishing_website.pkl','rb'))

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/predict")
def predict():
    return render_template("final.html")

@app.route("/y_predict", methods = ['GET', 'POST'])
def y_predict():
    geturl = request.form['url']
    check_prediction = inputScript.main(geturl)
    prediction = model.predict(check_prediction)
    print(prediction)
    output = prediction[0]
    if(output==1):
        pred ='Your are safe!! This is a Legitimate Website.'
    else:
        pred = 'You are on the wrong site. Be cautions!'
    return render_template('final.html',url_path = geturl,url = pred) 



if __name__ == '__main__':
   app.run(debug = True)
