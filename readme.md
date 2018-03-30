# A Minimal Application

This is "A Minimal Application" from the official Flask documentations
Instructions are for Mac, see the Flask documentation for Windows instructions

To set up the application:
1. Create a folder for this app
2. If using Python 3, create a new virtual environment with "python3 -m venv venv"
3. Activate the virtual environment with ". venv/bin/activate"
4. Install Flask with "pip install Flask"
(Deactivate virtual environment by entering "deactivate" in the terminal)

To run the application:
1. Activate the virtual environment with ". venv/bin/activate"
2. Tell the terminal the application to work with by exporting the FLASK_APP environment variable with export FLASK_APP=insert_name_of_app_here.py, "export FLASK_APP=minimal.py" in this case
3. Run the app with "flask run"
4. App is available at localhost:5000

Notes
1. Enable debug mode with "export FLASK_DEBUG=1" before running the server; this will display code changes in the browser immediately without having to relaunch the Flask app
2. The Flask server can be made externally visible with "flask run --host=0.0.0.0"
