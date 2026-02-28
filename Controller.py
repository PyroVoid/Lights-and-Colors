import socket
import json

command = {
    "command": "set_light",
    "index": 0,
    "color": [0, 0, 0]
}

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 5000))
sock.send(json.dumps(command).encode())
sock.close()