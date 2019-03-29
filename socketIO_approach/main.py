# encoding: utf-8
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRETE_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)


@app.route('/')
def session():
    return render_template('session.html')

def messageRecieved(methods=['GET','POST']):
    print('Message recieved!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET','POST']):
    print('Recieved event:'+str(json))
    socketio.emit('My response', json ,callback=messageRecieved)

if __name__ == '__main__':
    socketio.run(app,debug=True)
