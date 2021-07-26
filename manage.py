from flask import Flask
from app import blueprint

app = Flask(__name__)

app.register_blueprint(blueprint)
app.app_context().push()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
    
