# https://jiayi.space/post/shi-yong-flask-socketiojin-xing-websockettong-xin
# 2019/09/08

from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit
from config import DevelopmentConfig

app = Flask(__name__)

app.config.from_object(DevelopmentConfig)

socketio = SocketIO(app)


@socketio.on('message')
def handle_message(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)


@socketio.on('connect')
def handle_connect():
    emit('push', {'data': 'OK'})


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app)
