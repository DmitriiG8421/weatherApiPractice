from flask import Flask
app = Flask(__name__) #creates the Flask website app
@app.route("/") #decorator
def home():
    return """
    <h1>My First Flask Website</h1>
    <h2> This is my first Flask Website </h2>
    <h3> Hello World! </h3>
    <h4> This is awesome </h4>
    <p>Hello students!</p>
    """
app.run(debug=True)