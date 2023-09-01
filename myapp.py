from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login authentication
        # For example, check username and password
        username = request.form['username']
        password = request.form['password']

        if username == 'saani' and password == 'eff!1':
            # Redirect to the home page
            return redirect('/')
        elif username == "josh" and password == "de21":
             return redirect('/')
        elif username == "prince" and password == "sleep":
            return redirect('/')          
        else:
            # Handle unsuccessful login
            return "Invalid credentials"

    return render_template('base.html')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

