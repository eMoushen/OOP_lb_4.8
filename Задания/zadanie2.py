#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk


class TextListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Список")

        # Создаем текстовое поле
        self.text_entry = tk.Entry(
            root, font=("Arial", 12), borderwidth=2, relief="groove"
        )
        self.text_entry.pack(pady=10, padx=20, fill=tk.X)
        self.text_entry.bind("<Return>", self.add)

        # Создаем список
        self.text_listbox = tk.Listbox(
            root,
            font=("Arial", 12),
            selectbackground="#add8e6",
            borderwidth=2,
            relief="groove",
        )
        self.text_listbox.pack(expand=True, fill=tk.BOTH, padx=20)
        self.text_listbox.bind("<Double-Button-1>", self.copy_text)

    def add(self, event):
        text = self.text_entry.get()
        if text:
            self.text_listbox.insert(tk.END, text)
            self.text_entry.delete(0, tk.END)

    def copy_text(self, event):
        selected_index = self.text_listbox.curselection()
        if selected_index:
            selected_text = self.text_listbox.get(selected_index)
            self.text_entry.delete(0, tk.END)
            self.text_entry.insert(0, selected_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = TextListApp(root)
    root.mainloop()
