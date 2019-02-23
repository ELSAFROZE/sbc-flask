from flask import Flask

app=Flask(__name__)

@app.route("/")
def india():
    return "<h1> i love india hi !!!! <h1>"

@app.route("/home")
def homey():
    return "im from kottayam"   

@app.route("/contact")
def contct():
    return"this is my contact :)"

if(__name__=="__main__"):
    app.run(debug = True)