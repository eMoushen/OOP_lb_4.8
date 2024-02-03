#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk


class ResizableTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Изменяемый текст")

        # Создаем текстовые поля
        self.width_entry = tk.Entry(root, font=("Arial", 12))
        self.width_entry.pack(pady=5)

        self.height_entry = tk.Entry(root, font=("Arial", 12))
        self.height_entry.pack(pady=5)

        # Создаем многострочное текстовое поле
        self.text_widget = tk.Text(
            root, wrap=tk.WORD, font=("Arial", 12), bg="lightgrey"
        )
        self.text_widget.pack(expand=True, fill=tk.BOTH, padx=10, pady=5)

        # Привязываем события к фокусу
        self.text_widget.bind("<FocusIn>", self.focus_in)
        self.text_widget.bind("<FocusOut>", self.focus_out)

        # Привязываем событие к клавише Enter
        self.root.bind("<Return>", self.resize)

        # Создаем кнопку для изменения размера
        self.resize_button = tk.Button(root, text="Изменить", command=self.resize)
        self.resize_button.pack(pady=10)

    def focus_in(self, event):
        self.text_widget.config(bg="white")

    def focus_out(self, event):
        self.text_widget.config(bg="lightgrey")

    def resize(self, event=None):
        try:
            width = int(self.width_entry.get())
            height = int(self.height_entry.get())
            self.text_widget.config(width=width, height=height)
        except ValueError:
            pass


if __name__ == "__main__":
    root = tk.Tk()
    app = ResizableTextApp(root)
    root.mainloop()
