from flask import Flask, request, redirect, url_for, render_template, send_from_directory
import os

app = Flask(__name__)

# Define the required user agent for the secret page
required_user_agent = 'James Bond'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/secret')
def secret():
    user_agent = request.headers.get('User-Agent')

    # Get the query parameter 'year'
    year = request.args.get('year')

    # Check if the user agent matches the required one
    if user_agent != required_user_agent:
        return redirect(url_for('error', message='My name is Bond,James Bond'))

    # Check the year value (as a string comparison)
    if year == '2016':
        return render_template('secret.html')  # Correct year value
    elif year is not None:
        return 'lmao what u doing'  # Any other value of year
    else:
        return render_template('error.html', message="Let's go back to our roots.")

@app.route('/error')
def error():
    message = request.args.get('message', 'Access denied.')
    return f'Error: {message}'

@app.route('/robots.txt')
def robots():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'robots.txt')


def home():
    return render_template('index.html')

@app.route('/secret')
def secret():
    user_agent = request.headers.get('User-Agent')
    
    # Get the query parameter 'year'
    year = request.args.get('year')
    
    # Check if the user agent matches the required one
    if user_agent != required_user_agent:
        return redirect(url_for('error', message='Cant access this site.'))

    # Check the year value (as a string comparison)
    if year == '2016':
        return render_template('secret.html')  # Correct year value
    elif year is not None:
        return 'lmao what u doing'  # Any other value of year
    else:
        return render_template('error.html', message="Let's go back to our roots.")

@app.route('/error')
def error():
    message = request.args.get('message', 'Access denied.')
    return f'Error: {message}'

@app.route('/robots.txt')
def robots():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'robots.txt')

if __name__ == '__main__':
    app.run(debug=True)
