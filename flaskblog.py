from flask import Flask, escape, request
import json

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello():
    blog = {
        'name': '1',
        'name2': '12' 
    }
    return json.dumps(blog)

if __name__ == '__main__':
    app.run(debug=True)