# TCP-Chat-Room
A real-time chat application built using Flask and socket programming, enabling users to communicate instantly in a shared chatroom. It features a simple, responsive interface with support for multiple concurrent clients or users and WebSocket-based real-time updates.

## Features

- Real-time messaging with WebSocket integration.
- Join and leave notifications for users.
- Simple, responsive user interface for seamless communication.

## Prerequisites 

- Python 3.7 or higher
- pip for installing dependencies

## Setup and Installation 

To download the repository:

`git clone https://github.com/gandhidhruv2003/TCP-Chat-Room.git`

Create a virtual environment (optional but recommended):

\``python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows``

Then you need to install the basic dependencies to run the project on your system:

`cd TCP-Chat-Room
pip install -r requirements.txt`

Run the application:

`python run.py`

Open your browser and navigate to:

`http://127.0.0.1:5000/`

## Usage

- Open the app in your browser.
- Enter a username to join the chatroom.
- Start chatting with other connected users in real time.

## Technologies Used
- Backend: Flask, Flask-SocketIO
- Frontend: HTML, CSS, JavaScript
- WebSocket Server: Flask-SocketIO with Eventlet
