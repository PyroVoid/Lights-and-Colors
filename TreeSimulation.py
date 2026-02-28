import pygame
import random
import socket
import threading
import json
import queue

class Tree:
    IMAGE = pygame.image.load("tree.webp")
    SCREEN_WIDTH = 616
    SCREEN_HEIGHT = 924
    TREE_TL = (160, 300)
    TREE_BR = (470, 770)
    LIGHTS = 100
    LIGHT_RADIUS = 5

    def __init__(self):
        self.light_colors = []
        self.light_coords = []
        self.command_queue = queue.Queue()

        for _ in range(Tree.LIGHTS):
            x = random.randint(Tree.TREE_TL[0], Tree.TREE_BR[0])
            y = random.randint(Tree.TREE_TL[1], Tree.TREE_BR[1])
            self.light_coords.append((x, y))
            self.light_colors.append(
                (random.randint(0,255),
                 random.randint(0,255),
                 random.randint(0,255))
            )

    def apply_command(self, cmd):
        if cmd["command"] == "set_light":
            index = cmd["index"]
            color = tuple(cmd["color"])
            if 0 <= index < Tree.LIGHTS:
                self.light_colors[index] = color

    def process_commands(self):
        while not self.command_queue.empty():
            cmd = self.command_queue.get()
            self.apply_command(cmd)

    def update(self, screen):
        self.process_commands()

        screen.fill((0, 0, 0))
        screen.blit(Tree.IMAGE, (0, 0))

        for i in range(Tree.LIGHTS):
            pygame.draw.circle(screen, self.light_colors[i], self.light_coords[i], Tree.LIGHT_RADIUS)

        pygame.display.flip()


def tcp_listener(tree, host="127.0.0.1", port=5000):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    while True:
        conn, _ = server.accept()
        data = conn.recv(1024).decode()
        if data:
            try:
                cmd = json.loads(data)
                tree.command_queue.put(cmd)
            except json.JSONDecodeError:
                pass
        conn.close()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((Tree.SCREEN_WIDTH, Tree.SCREEN_HEIGHT))
    tree = Tree()

    # Start TCP listener thread
    threading.Thread(target=tcp_listener, args=(tree,), daemon=True).start()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        tree.update(screen)

    pygame.quit()