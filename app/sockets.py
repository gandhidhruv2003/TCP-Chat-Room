from flask_socketio import SocketIO, emit, join_room, leave_room
from . import socketio

clients = {}

@socketio.on("join")
def handle_join(data):
    username = data["username"]
    room = "chatroom"
    join_room(room)
    clients[username] = room
    emit("message", {"msg": f"{username} has joined the chat!"}, room=room)

@socketio.on("message")
def handle_message(data):
    room = clients.get(data["username"], "chatroom")
    emit("message", {"msg": f"{data['username']}: {data['msg']}"}, room=room)

@socketio.on("disconnect")
def handle_disconnect():
    username = None
    for user, room in clients.items():
        if room == "chatroom": 
            username = user
            leave_room(room)
            emit("message", {"msg": f"{username} has left the chat!"}, room=room)
            break
    if username:
        del clients[username]
