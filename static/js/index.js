$(document).ready(function () {

    // var socket = io.connect('http://127.0.0.1:5000');
    var socket = io();
    var messages = $('#messages');
    var myMessage = $('#myMessage');
    var send = $('#send');

    socket.on('connect', function() {
        socket.send('Tony is coming');
    });

    // Server Push
    socket.on('response', function(data) {
        messages.append('<li>' + data + '</li>');
    });

    // Client push to Server
    socket.on('message', function(data) {
        messages.append('<li>' + data + '</li>');
    });

    send.on('click', function() {
        sendingMessage();
    });

    $('input[type=text]').on('keydown', function(evt) {
        if (evt.key == 'Enter') {
            evt.preventDefault();
            sendingMessage();
        }
    })

    var sendingMessage = function() {
        let sending = myMessage.val();
        socket.send(sending);
        myMessage.val('');
        myMessage.focus();
    }

    myMessage.focus();
});