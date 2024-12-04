from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "a3f5b81d6c9f2c3e1f4e9b3c2d4a6f7g"  

    from .routes import main
    app.register_blueprint(main)

    from .sockets import socketio  # Import socket handlers
    socketio.init_app(app)

    return app
