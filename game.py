import tkinter as tk
import random
import time
import pygame 

class Game:
    def __init__(self, root, width=20, height=10, obstacle_density=0.1):
        self.width = width
        self.height = height
        self.obstacle_density = obstacle_density
        self.player_x = width // 2
        self.score = 0
        self.game_over = False
        self.obstacles = []
        self.root = root  
        self.generate_obstacles()

    def generate_obstacles(self):
        for _ in range(self.width):
            if random.random() < self.obstacle_density:
                self.obstacles.append((random.randint(0, self.width - 1), random.randint(0, self.height - 1)))
        if not self.game_over:
            self.root.after(1000, self.generate_obstacles)  
    def move_player(self, direction):
        if self.game_over:
            return
        if direction == "left":
            self.player_x = max(0, self.player_x - 1)
        elif direction == "right":
            self.player_x = min(self.width - 1, self.player_x + 1)
        self.check_collision()

    def check_collision(self):
        for obstacle in self.obstacles:
            if obstacle[0] == self.player_x and obstacle[1] == self.height - 1:
                self.game_over = True
                break

    def move_obstacles(self):
        new_obstacles = []
        for obstacle in self.obstacles:
            x, y = obstacle
            if y < self.height - 1:
                new_obstacles.append((x, y + 1))
                if x == self.player_x and y + 1 == self.height - 1:
                    self.game_over = True
            else:
                self.score += 1
        self.obstacles = new_obstacles

class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = Game(self)  
        self.canvas = tk.Canvas(self, width=self.game.width * 20, height=self.game.height * 20, bg="white")
        self.canvas.pack()
        self.bind("<KeyPress-Left>", lambda event: self.game.move_player("left"))
        self.bind("<KeyPress-Right>", lambda event: self.game.move_player("right"))
        self.bind("<Return>", lambda event: self.game.move_player("right"))
        self.draw()

    def draw(self):
        self.canvas.delete("all")
        for obstacle in self.game.obstacles:
            x, y = obstacle
            self.canvas.create_rectangle(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill="black")
        self.canvas.create_oval(self.game.player_x * 20, (self.game.height - 1) * 20,
                                (self.game.player_x + 1) * 20, self.game.height * 20, fill="red")
        self.canvas.create_text(50, 10, text=f"Score: {self.game.score}", anchor=tk.NW)
        self.after(100, self.update_game)

    def update_game(self):
        if not self.game.game_over:
            self.game.move_obstacles()
            self.draw()
        else:
            self.canvas.create_text(self.game.width * 10, self.game.height * 10, text="Game Over!", fill="red", font=("Helvetica", 24), anchor=tk.CENTER)

def main():
    gui = GUI()
    gui.mainloop()

if __name__ == "__main__":
    main()
    main()
