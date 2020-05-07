from flask import  Flask,escape
app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
@app.route('/<username>')
def profile(username):
    return '<h1>Hello {}!</h1>'.format(escape(username))

if __name__ == '__main__':
    app.run(debug=True,port=8090)