import socket
import json

class Controller:
    def __init__(self, host="127.0.0.1", port=5000):
        self.host = host
        self.port = port

    def _send_command(self, command_dict):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.host, self.port))
            sock.send(json.dumps(command_dict).encode())

    def set_color(self, index, color):
        """
        index: int
        color: tuple or list (R, G, B)
        """
        command = {
            "command": "set_light",
            "index": index,
            "color": list(color)
        }
        self._send_command(command)

if __name__ == "__main__":
    controller = Controller()
    for i in range(100):
        if i % 2 == 0:
            controller.set_color(i, (0, 0, 0))
        else:
            controller.set_color(i, (255, 255, 255))