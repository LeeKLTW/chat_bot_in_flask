# encoding: utf-8
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRETE_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)
