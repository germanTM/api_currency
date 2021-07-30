from flask import Flask
from app import blueprint

app = Flask(__name__)

app.register_blueprint(blueprint)
app.app_context().push()

app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
    
