from flask import Flask
app = Flask(__name__)



@app.route('/')
@app.route('/index')
def index():
    return 'Main landing page for the App'





if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=9000)

