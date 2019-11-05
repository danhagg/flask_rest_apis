# python -m venv venv

# import class Flask from package Flask (F)
from flask import Flask

# create the object app from Flask class
# __name__ gives each file unqiue name
app = Flask(__name__)

# endpoint or request that flask is to understand
# / tends to represent homepage 
@app.route('/')
# Decorators have to act on method (name here does not matter)
def home():
    # has to return a response back to the browser
    return 'Hello, World'

# port is area of computer for app to receive information
app.run(port=5000)

# Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)