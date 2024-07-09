#!/usr/bin/python3

from tkinter import font
import tkinter as tk
from parent_frame import AbstractCourseFrame

class CourseFrame1(AbstractCourseFrame):
    def create_widgets(self):
        # Define a custom font
        custom_font = font.Font(family="Helvetica", size=20, weight="bold")

        # Create the label with the custom font
        label = tk.Label(self, text="Student Expectation System", anchor='n', font=custom_font)
        label.grid(row=0, column=0, columnspan=2, padx=170, pady=20)

        # Label and Entry for "Student Name"
        label2 = tk.Label(self, text="Student Name")
        label2.grid(row=0, column=0, padx=(30, 10), pady=(50, 5), sticky='w')

        entry_student_name = tk.Entry(self, width=20)
        entry_student_name.grid(row=1, column=0, padx=(20, 10), pady=(0, 20), sticky='w')

        # Label and Entry for "Number of assessments"
        label3 = tk.Label(self, text="Number of assessments")
        label3.grid(row=0, column=3, padx=(30, 10), pady=(50, 5), sticky='w')

        entry_assessment = tk.Entry(self, width=20)
        entry_assessment.grid(row=1, column=3, padx=(20, 10), pady=(0, 20), sticky='w')

if __name__ == "__main__":
    root = tk.Tk()
    app = CourseFrame1(master=root)  # Instantiate CourseFrame1
    app.mainloop()
