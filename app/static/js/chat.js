const socket = io();

const messages = document.getElementById('messages');
const input = document.getElementById('message-input');
const sendButton = document.getElementById('send-button');

const username = prompt('Enter your username:');
socket.emit('join', { username });

sendButton.addEventListener('click', () => {
    const msg = input.value;
    if (msg) {
        socket.emit('message', { username, msg });
        input.value = '';
    }
});

socket.on('message', (data) => {
    const msgElement = document.createElement('div');
    msgElement.textContent = data.msg;
    messages.appendChild(msgElement);
});
