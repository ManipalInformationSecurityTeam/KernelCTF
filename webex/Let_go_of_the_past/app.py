from flask import Flask, request, make_response, redirect, url_for, render_template

app = Flask(__name__)

# Dummy admin credentials
admin_username = "admin"
admin_password = "password"

@app.route('/')
def index():
    user_cookie = request.cookies.get('user')
    admin_cookie = request.cookies.get('very_very_very_tasty_cookiedHJ5IHNjcmlwdGluZw')
    
    if admin_cookie:
        return render_template('index.html', message="Welcome, Admin! wtfCTF{c00k13_yuM_c00kie_t45tY}")
    elif user_cookie:
        return render_template('index.html', message=f"Hello, {user_cookie}!")  # Greet the logged-in user
    return render_template('index.html', message="Hello, Guest!", show_login=True)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Admin login
        if username == admin_username and password == admin_password:
            response = make_response(redirect(url_for('index')))
            response.set_cookie('very_very_very_tasty_cookiedHJ5IHNjcmlwdGluZw', 'yay')  # Admin cookie
            return response
        
        # Regular user login (any username that isn't admin)
        elif username:
            response = make_response(redirect(url_for('index')))
            response.set_cookie('user', username)  # User cookie
            return response
    
    # Show the login form for both GET and failed POST
    return render_template('login.html')

@app.route('/delete_data', methods=['POST'])
def delete_data():
    if request.cookies.get('very_very_very_tasty_cookiedHJ5IHNjcmlwdGluZw'):
        # Simulate deleting data
        return render_template('index.html', message="Data deleted!")
    return render_template('index.html', message="Unauthorized", status=403)

@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('index')))
    response.delete_cookie('user')
    response.delete_cookie('very_very_very_tasty_cookiedHJ5IHNjcmlwdGluZw')
    return response

if __name__ == '__main__':
    app.run(debug=True)
