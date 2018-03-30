# Flask Sample App

Flask-sample-app is a fully operational one file Flask app complete with many explanatory code comments. This app was created to provide a sample of the power and simplicity of the Flask framework. The ample code comments are so that anyone can look at the code and immediately understand what is going on without prior experience with Flask or even web development.

This app and its supporting documentation is based on "A Minimal Application" from the Quickstart section of the official Flask documentation. The latest version of the documentation can be found [here](http://flask.pocoo.org/docs/latest/).

The following instructions are for MacOS. See the Flask documentation on
"Installation" to learn how to run the app on different operating systems.

## To set up the application:
1. Create a folder for this app or `git clone` this repository
2. If using Python 3, create a new virtual environment with `python3 -m venv venv`
3. Activate the virtual environment with `. venv/bin/activate` (Deactivate the virtual environment by entering `deactivate` in the terminal)
4. Install Flask with `pip install Flask`

## To run the application:
1. Activate the virtual environment with `. venv/bin/activate`
2. Tell the terminal the application to work with by exporting the FLASK_APP environment variable with `export FLASK_APP=sample.py`
3. Run the app with `flask run`
4. View the app in a web browser at http://localhost:5000

## Notes
1. Enable debug mode with `export FLASK_DEBUG=1` before running the server; this will display code changes in the browser immediately when changes to a file are saved without having to relaunch the Flask app
2. The Flask server can be made externally visible with `flask run --host=0.0.0.0`
