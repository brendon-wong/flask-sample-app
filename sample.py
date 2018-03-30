from flask import (
    # Import the Flask class; an instance of this class will be this Flask app
    Flask,
    # url_for builds a URL from the name of a view function
    url_for,
    # render_template looks in the root directory for a folder called templates
    # with HTML templates inside by default
    render_template,
    # The request object contains data the client sends to the server
    # Its attributes include form, files, and cookies (for security, use session for cookies)
    request,
    # Use this function to redirect users to another endpoint
    redirect,
    # Use this function to abort a request with an error code
    abort,
    # The session object uses cookies to store user specific information
    # which persists through multiple requests
    session
    )


# We create an instance of the Flask class which is this WSGI application
# The first argument is the name of this app's module or package
# so Flask knows where to look for templates, files, etc
# (a module is a file containing Python definitions and statements)
# (a package is a directory of Python module(s) with a special file called __init__.py inside)
app = Flask(__name__)

# This decorator, generated from a method of "app" (which is an instance of "Flask"),
# associates the path '/hello' with the hello_world function, which is now a view function
@app.route('/hello')
def hello_world():
    return 'Hello World!'

# <string:post_name> represents a variable section of the URL
# In addition to string there is also int, float, path, and uuid for variable URL sections
@app.route('/post/<string:post_name>')
# The posts function receives the variable URL section as a keyword argument
def posts(post_name):
    return 'Post: {}'.format(post_name.title())

# This is the home page of the app
@app.route('/')
def index():
    # render_template takes in the name of a template and variables for template engine to use
    # Jinja2 replaces placeholders with actual values during rendering
    # Inside templates you also have access to the request, session and g1 objects
    # as well as the get_flashed_messages() function
    name = 'Visitor'
    # Here we pass in a template name and the name variable for the HTML template to use
    # Edit the name variable to display an alternative greeting
    return render_template('/index.html', name=name)


# User sessions
# This section demonstrates various ways to display text and HTML to website
# visitors without using templates which is simpler but generally not best practice

# Must set secret key to use sessions; the secret key makes it so
# users can read but cannot modify this app's cookies without the key
app.secret_key = "Do not use insecure passwords in production"

# An HTTP GET request represents the browser requesting data from a web server
# All view functions accept GET requests by default
# This function also accepts POST requests, representing the browser sending
# data to a web server, which is a username in this case
@app.route('/login', methods = ['GET', 'POST'])
def login():
    # This block of code only executes if the user submits a POST request
    if request.method == "POST":
        # The user's username is logged in a cookie
        # The session cookie can be viewed in a browser's cookie settings area
        session['username'] = request.form['username']
        # User is redirected to the dashboard
        return redirect(url_for('dashboard'))
    # This block of code only executes if the user submits a GET request to view the /login page
    return """
        <h1>Sign in</h1>
        <form method="post">
            <input type=text name=username placeholder="Enter a username"
            required style="width: 200px; height: 25px;">
            <br><br>
            <input type=submit value=Login style="width: 75px; height: 25px;">
        </form>
    """

@app.route('/dashboard')
def dashboard():
    # This block of code checks if there the username is stored in a cookie,
    # and thus only executes if the user has "logged in"
    if 'username' in session:
        return "Welcome {}!".format(session['username']) + " Press " + \
                '<a href="logout">log out</a>' + " to sign out."
    # This return statement only executes if the user has not registered
    return 'This is a private area for logged in users only, go to the ' \
            + '<a href="login">log in</a>' + ' page to sign in.'

@app.route('/logout')
def logout():
    # The username is deleted from the cookie
    session.pop('username', None)
    return redirect(url_for('dashboard'))
