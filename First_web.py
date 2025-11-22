from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return'''<h1> Hello world! My first Flask app<h1>
    <p><a href="/about">Go to about page</p>'''

@app.route('/about')
def about():
    return'''<h1><marquee> About this site </marquee></h1
    <p> this is my first website built with powerful Flask frameworks</p>
    <P><a href="/home">Go back to home page</p>'''

if __name__ == '__main__' :
   app.run(debug=True)