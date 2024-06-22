from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response
import jwt


MAX_TOKEN_AGE_S = 10

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

# Simple in-memory data store for demo.
users = {}


def generate_token(data):
    token = jwt.encode(data, app.config['SECRET_KEY'], algorithm='HS256')

    return token


def verify_token(token):
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms='HS256')
    except:
        data = None

    return data


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if username in users:
        return jsonify({'message': 'User already exists.'}), 400

    users[username] = password
    return jsonify({'message': 'User successfully registered.'}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if password == users[username]:
        token = generate_token({'username': username})
        return jsonify({'token': token}), 200
    else:
        return jsonify({'message': 'Invalid credentials.'}), 401


@app.route('/protected', methods=['GET'])
def protected():
    token = request.args.get('token')

    if not token:
        return jsonify({'message': 'Missing token.'}), 401

    data = verify_token(token)

    if data is None:
        return jsonify({'message': 'Invalid or expired token.'}), 401

    return jsonify({'message': 'Protected data accessed successfully!'}), 200
