from flask import Flask

app=Flask(__name__)

@app.route("/")
def india():
    return "i love india !!!!"
@app.route("/home")
def homey():
    return "im from kottayam"   
@app.route("/contact")
def contct():
    return"this is my contact :)"

if(__name__=="__main__"):
    app.run()