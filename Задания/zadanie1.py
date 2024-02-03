#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import tkinter as tk


class ShoppingList:
    def __init__(self, root):
        self.root = root
        self.root.title("Магазин одежды")

        self.available_items_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
        self.available_items_listbox.pack(side=tk.LEFT, padx=10)

        self.shopping_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
        self.shopping_listbox.pack(side=tk.RIGHT, padx=10)

        # Наполняем первый список одеждой
        available_items = ["Футболка", "Джинсы", "Куртка", "Платье", "Обувь", "Шапка", "Перчатки", "Носки", "Очки"]
        for item in available_items:
            self.available_items_listbox.insert(tk.END, item)

        self.add_button = tk.Button(
            root, text=">>>", command=self.move_to_shopping
        )
        self.add_button.pack(side=tk.LEFT, pady=10, padx=5)

        self.remove_button = tk.Button(
            root, text="<<<", command=self.move_from_shopping
        )
        self.remove_button.pack(side=tk.LEFT, pady=10, padx=5)

    def move_to_shopping(self):
        selected_items = self.available_items_listbox.curselection()
        for index in selected_items[
            ::-1
        ]:  # Перебираем в обратном порядке, чтобы удаление не нарушало индексы
            item = self.available_items_listbox.get(index)
            self.shopping_listbox.insert(tk.END, item)
            self.available_items_listbox.delete(index)

    def move_from_shopping(self):
        selected_items = self.shopping_listbox.curselection()
        for index in selected_items[::-1]:
            item = self.shopping_listbox.get(index)
            self.available_items_listbox.insert(tk.END, item)
            self.shopping_listbox.delete(index)


if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingList(root)
    root.mainloop()
