from tkinter import *
import tkinter as tk
from tkinter import messagebox

class BinarySearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary Search Visualization")

        self.values_list = []
        self.mid = None
        self.comparison_canvases = []  # To store references to the comparison canvases

        self.create_widgets()

    def create_widgets(self):
        self.root.configure(bg="lightgray")  # Set the background color of the root window

        input_label = tk.Label(self.root, text="Enter comma-separated values:")
        input_label.pack(pady=10)

        self.input_entry = tk.Entry(self.root)
        self.input_entry.pack(pady=5)

        submit_button = tk.Button(self.root, text="Submit", command=self.store_values)
        submit_button.pack(pady=5)

        self.canvas = tk.Canvas(self.root, width=600, height=100, bg="white")
        self.canvas.pack(pady=10)

        search_label = tk.Label(self.root, text="Enter target value to search:")
        search_label.pack()

        self.target_entry = tk.Entry(self.root)
        self.target_entry.pack()

        search_button = tk.Button(self.root, text="Search", command=self.perform_binary_search)
        search_button.pack(pady=5)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def store_values(self):
        input_text = self.input_entry.get()
        self.values_list = list(map(int, input_text.split(',')))
        self.values_list.sort()

        self.update_canvas()

    def update_canvas(self):
        self.canvas.delete("all")
        for i, value in enumerate(self.values_list):
            x = 50 + i * 40
            self.canvas.create_rectangle(x - 20, 50, x + 20, 100, outline="black", fill="lightblue")
            self.canvas.create_text(x, 75, text=str(value), font=("Helvetica", 10), anchor="center")
        if self.mid is not None:
            x = 50 + self.mid * 40
            self.canvas.create_rectangle(x - 20, 50, x + 20, 100, outline="black", fill="yellow")

    def show_comparison(self, low, high):
        comparison_canvas = tk.Canvas(self.root, width=600, height=100, bg="white")
        comparison_canvas.pack(pady=10)
        self.comparison_canvases.append(comparison_canvas)  # Store reference to the current canvas

        for i, value in enumerate(self.values_list):
            x = 50 + i * 40
            fill_color = "lightblue"
            if low <= i <= high:
                fill_color = "orange"
            comparison_canvas.create_rectangle(x - 20, 50, x + 20, 100, outline="black", fill=fill_color)
            comparison_canvas.create_text(x, 75, text=str(value), font=("Helvetica", 10), anchor="center")

    def perform_binary_search(self):
        target = self.target_entry.get()
        try:
            target = int(target)
        except ValueError:
            messagebox.showerror("Error", "Target must be an integer.")
            return

        self.clear_comparison_canvases()  # Clear previous comparison canvases

        low, high = 0, len(self.values_list) - 1
        self.mid = None

        while low <= high:
            self.mid = (low + high) // 2
            self.update_canvas()
            self.show_comparison(low, high)
            self.root.update()
            self.root.after(1000)

            if self.values_list[self.mid] == target:
                self.result_label.config(text=f"Target {target} found at index {self.mid}.")
                return
            elif self.values_list[self.mid] < target:
                low = self.mid + 1
            else:
                high = self.mid - 1

        self.result_label.config(text=f"Target {target} not found.")

    def clear_comparison_canvases(self):
        for canvas in self.comparison_canvases:
            canvas.destroy()
        self.comparison_canvases = []

if __name__ == "__main__":
    root = tk.Tk()
    app = BinarySearchApp(root)
    root.mainloop()
