from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
   return 'home'

@app.route('/info/<name>')
def foo(name):
   return render_template('index.html', userName = name)

if __name__ == '__main__':
   app.run(debug = True,host = '0.0.0.0',port = 4444)
