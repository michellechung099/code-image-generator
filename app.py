from flask import Flask 

app = Flask(__name__)

# first parameter: alls code() when you visit root URL 
# methods parameter: restricts which request methods the view allows
@app.route("/", methods=["GET"])

# view function that you prepend with app.route() decorators
# entry point of the web app 
def code():

    pass 
