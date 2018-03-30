from flask import (
    # import the Flask class to create app
    Flask,
    # url_for uses the format url_for("name_of_view_function") to build a URL
    url_for,
    # render_template looks in top-level templates folder for templates by default
    render_template,
    # the request object contains data the client sends to the server
    # its attributes include form, files, and cookies (for security, use session for cookies)
    request,
    # use this function to redirect users to another endpoint
    redirect,
    # use this function to abort a request with an error code
    abort,
    # the session object stores user specific info that persists with multiple requests
    session
    )


# We create an instance of the Flask class which is this WSGI application.
# the first argument is the name of this app's module
# (a module is a file containing Python definitions and statements) or package
# so Flask knows where to look for templates, files, etc
app = Flask(__name__)

# this decorator, from a method of our app (a Flask instance), associates the
# path '/' with the hello_world function, which is now a view function for the path
@app.route('/hello')
def hello_world():
    return 'Hello World!'

# path accepts strings, including slashes
@app.route('/post/<path:post_name>')
# the posts function receives the post_name part of path:post_name as a keyword argument
def posts(post_name):
    return 'Post: {}'.format(post_name.title())

@app.route('/')
def index():
    # render_template takes in name of template and variables for template engine
    # Jinja2 replaces placeholders with actual values during rendering
    # Inside templates you also have access to the request, session and g1 objects
    # as well as the get_flashed_messages() function
    name = 'User'
    return render_template('/index.html', name=name)

# User sessions

# Must set secret key to use sessions; the secret key makes it so
# users can read but cannot modify cookies without the key
app.secret_key = "Do not use insecure passwords in production"

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return "Welcome {}!".format(session['username']) + " Press " + \
                '<a href="logout">log out</a>' + " to sign out."
    return 'This is a private area for logged in users only, go to the ' \
            + '<a href="login">log in</a>' + ' page to sign in.'

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        session['username'] = request.form['username']
        return redirect(url_for('dashboard'))
    return """
        <h1>Sign in</h1>
        <form method="post">
            <input type=text name=username placeholder="Enter a username"
            required style="width: 200px; height: 25px;">
            <br><br>
            <input type=submit value=Login style="width: 75px; height: 25px;">
        </form>
    """

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('dashboard'))
