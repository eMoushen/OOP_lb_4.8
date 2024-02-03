#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk


class DrawingPicture:
    def __init__(self, root):
        self.root = root
        self.root.title("Домик в поле")

        self.canvas = tk.Canvas(root, width=550, height=400, bg="white")
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        # Рисуем траву
        self.draw_grass()

        # Рисуем домик
        self.draw_house()

        # Рисуем солнце
        self.draw_sun()

    def draw_grass(self):
        for x in range(0, 550, 10):
            if 100 < x < 500:
                self.canvas.create_line(
                    x, 290, x + 5, 310,
                    fill="green", smooth=tk.TRUE
                )

    def draw_house(self):
        self.canvas.create_rectangle(250, 200, 350, 300, fill="brown", outline="black")
        self.canvas.create_polygon(250, 200, 300, 150, 350, 200, fill="brown", outline="black")

        for x in range(250, 351, 10):
            if 100 < x < 500:
                self.canvas.create_line(
                    x, 290, x + 5, 310,
                    fill="green", smooth=tk.TRUE
                )

    def draw_sun(self):
        self.canvas.create_oval(400, 50, 450, 100, fill="orange", outline="orange")


if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingPicture(root)
    root.mainloop()
