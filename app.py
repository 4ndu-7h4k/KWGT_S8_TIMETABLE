from urllib import request
from flask import Flask,request
from s8_timetable import main
app = Flask(__name__)
@app.route('/')
def index():
    return main(request)
if __name__ == "__main__":
    app.run(debug=True)