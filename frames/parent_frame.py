#!/usr/bin/python3

import tkinter as tk
from abc import ABC, abstractmethod
from tkinter import messagebox

class AbstractCourseFrame(tk.Frame, ABC):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    @abstractmethod
    def create_widgets(self):
        pass

    def show_course_info(self, avg, grade):
        message = f"Average: {avg}\nGrade: {grade}"
        messagebox.showinfo("Course Info", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = AbstractCourseFrame(master=root)
    app.mainloop()
