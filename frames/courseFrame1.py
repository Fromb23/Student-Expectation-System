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
        label.grid(row=0, column=0, columnspan=2, padx=100, pady=10)

        # Label and Entry for "Student Name"
        label2 = tk.Label(self, text="Student Name")
        label2.grid(row=0, column=0, padx=(30, 10), pady=(50, 5), sticky='w')

        entry_student_name = tk.Entry(self, width=20)
        entry_student_name.grid(row=1, column=0, padx=(20, 10), pady=(0, 20), sticky='w')

        # Label and Entry for "Number of assessments"
        label3 = tk.Label(self, text="Number of assessments")
        label3.grid(row=0, column=2, padx=(30, 10), pady=(50, 5), sticky='w')

        entry_assessment = tk.Entry(self, width=20)
        entry_assessment.grid(row=1, column=2, padx=(20, 10), pady=(0, 20), sticky='w')

        # Course Codes
        label4 = tk.Label(self, text="Choose one of the following code courses:")
        label4.grid(row=2, column=1, sticky='nsew')

        label5 = tk.Label(self, text="111 Introduction to computer networks")
        label5.grid(row=3, column=1, sticky='nsew')

        label6 = tk.Label(self, text='112 Object-oriented programming')
        label6.grid(row=4, column=1, sticky='nsew', padx=(0, 35))

        label7 = tk.Label(self, text='113 Web design & programming')
        label7.grid(row=5, column=1, padx=(0, 45), sticky='nsew')

        label8 = tk.Label(self, text='114 Introduction to operating stystem')
        label8.grid(row=6, column=1, padx=(0, 16), sticky='nsew')

        label9 = tk.Label(self, text='Course Code')
        label9.grid(row=7, column=1, pady=(20, 0), sticky='nsew')

        # Entry for course code
        entry_course_code = tk.Entry(self, width=5)
        entry_course_code.grid(row=8, column=1, sticky='nsew')
        
        # Show Course Assessments
        button = tk.Button(self, text='Show Course Assessments', borderwidth=0, bg='#6e605f')
        button.grid(row=9, column=1, sticky='nsew', pady=(10, 0))

        # Assessment marks
        label10 = tk.Label(self, text='Assessment Marks')
        label10.grid(row=10, column=0, sticky='w', padx=(20, 10), pady=(0, 20))

        entry_1 = tk.Entry(self, width=20)
        entry_1.grid(row=11, column=0, sticky='w', padx=(20, 10), pady=(0, 20))

        entry_2 = tk.Entry(self, width=20)
        entry_2.grid(row=12, column=0, sticky='w', padx=(20, 10), pady=(0, 20))

        entry_3 = tk.Entry(self, width=20)
        entry_3.grid(row=13, column=0, sticky='w', padx=(20, 10), pady=(0, 20))

        entry_4 = tk.Entry(self, width=20)
        entry_4.grid(row=14, column=0, sticky='w', padx=(20, 10), pady=(0, 20))


        entry_5 = tk.Entry(self, width=20)
        entry_5.grid(row=11, column=1, sticky='nwes', rowspan=4, columnspan=2, padx=40)

        # Level of Student
        student_level = tk.Button(self, text='Level of student', borderwidth=0, bg="#e35502")
        student_level.grid(row=15, column=1, sticky='nswe', pady=(10, 0))

if __name__ == "__main__":
    root = tk.Tk()
    app = CourseFrame1(master=root)  # Instantiate CourseFrame1
    app.mainloop()
