import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'lu.. kontol!'

os.system("python3 -m rams")