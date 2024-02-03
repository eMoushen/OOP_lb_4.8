#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from tkinter import *


class MovingCircleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Перемещение круга")

        self.canvas = Canvas(root, width=300, height=200, bg="white")
        self.canvas.pack()

        self.circle = self.canvas.create_oval(
            50, 50, 70, 70,
            fill="blue", outline="black"
        )

        self.target_coords = (0, 0)  # Initialize target_coords

        self.canvas.bind("<Button-1>", self.on_click)

    def move_towards_target(self):
        current_coords = self.canvas.coords(self.circle)
        target_x, target_y = self.target_coords

        distance_x = target_x - current_coords[0]
        distance_y = target_y - current_coords[1]

        slope = distance_y / distance_x if distance_x != 0 else 0

        # Определяем шаг перемещения по x и y
        step_x = 1 if distance_x > 0 else -1
        step_y = int(slope * step_x)

        # Перемещаем кружок
        self.canvas.move(self.circle, step_x, step_y)

        if (
            self.canvas.coords(self.circle)[0] != target_x
            or self.canvas.coords(self.circle)[1] != target_y
        ):
            self.root.after(10, self.move_towards_target)

    def on_click(self, event):
        self.target_coords = (event.x, event.y)
        self.move_towards_target()


if __name__ == "__main__":
    root = Tk()
    app = MovingCircleApp(root)
    root.mainloop()
