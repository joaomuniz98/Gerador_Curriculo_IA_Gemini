
from flask import Flask , request , jsonify , Blueprint
from flask_cors import CORS
from controller import controller 

app = Flask(__name__)
CORS(app) 

# Registrando o controlador na aplicação
app.register_blueprint(controller)


if __name__ == '__main__':
    app.run(debug=True)