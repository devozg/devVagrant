from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "<h1> Hello, world! I'm a minimal Flask app hosted with Apache + mod_wsgi V3 </h1>"
 
if __name__ == "__main__":
    app.run()

