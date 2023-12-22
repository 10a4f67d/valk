const express = require('express');
const http = require('http');
const socketIO = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = socketIO(server);

const PORT = process.env.PORT || 8000;

app.use(express.static('public'));

console.clear();

console.log('██╗      ██████╗  ██████╗ █████╗ ██╗     ██╗  ██╗ ██████╗ ███████╗████████╗');
console.log('██║     ██╔═══██╗██╔════╝██╔══██╗██║     ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝');
console.log('██║     ██║   ██║██║     ███████║██║     ███████║██║   ██║███████╗   ██║   ');
console.log('██║     ██║   ██║██║     ██╔══██║██║     ██╔══██║██║   ██║╚════██║   ██║   ');
console.log('███████╗╚██████╔╝╚██████╗██║  ██║███████╗██║  ██║╚██████╔╝███████║   ██║   ');
console.log('╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ');

io.on('connection', (socket) => {
  console.log(`User connected: ${socket.id}`);

  socket.on('disconnect', () => {
    console.log(`User disconnected: ${socket.id}`);
  });

  socket.on('chatMessage', (message) => {
    console.log(`Received message from ${socket.id}: ${message}`);
    io.emit('chatMessage', message);
  });
});

server.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});