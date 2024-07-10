#!/usr/bin/python3

from tkinter import font, Text
import tkinter as tk
from parent_frame import AbstractCourseFrame

class CourseFrame1(AbstractCourseFrame):
    def create_widgets(self):
        # Define a custom font
        custom_font = font.Font(family="Helvetica", size=20, weight="bold")

        # Create the label with the custom font
        label = tk.Label(self, text="Student Expectation System", anchor='n', font=custom_font)
        label.grid(row=0, column=0, columnspan=2, padx=120, pady=10)

        # Label and Entry for "Student Name"
        label2 = tk.Label(self, text="Student Name")
        label2.grid(row=0, column=0, padx=(30, 10), pady=(50, 5), sticky='w')

        self.entry_student_name = tk.Entry(self, width=20)
        self.entry_student_name.grid(row=1, column=0, padx=(20, 10), pady=(0, 20), sticky='w')

        # Label and Entry for "Number of assessments"
        label3 = tk.Label(self, text="Number of assessments")
        label3.grid(row=0, column=2, padx=(30, 10), pady=(50, 5), sticky='w')

        self.entry_assessment = tk.Entry(self, width=20)
        self.entry_assessment.grid(row=1, column=2, padx=(20, 10), pady=(0, 20), sticky='w')

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
        self.entry_course_code = tk.Entry(self, width=5)
        self.entry_course_code.grid(row=8, column=1, sticky='nsew')
        
        # Button to show Course Assessments
        button = tk.Button(self, text='Show Course Assessments', borderwidth=0, bg='#6e605f', command=self.show_course_assessments)
        button.grid(row=9, column=1, sticky='nsew', pady=(10, 0))

        # Entry to display number of assessments
        self.assessment_display = Text(self, width=20, state='disable', height=10)
        self.assessment_display.grid(row=16, column=1, pady=(10, 0), padx=20)

        # Label to display course syllabus
        self.syllabus_label = tk.Label(self, text="", font=("Helvetica", 14))
        self.syllabus_label.grid(row=17, column=1, sticky='nsew', padx=20)

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


        self.entry_5 = Text(self, width=20, height=10)
        self.entry_5.grid(row=11, column=1, sticky='nwes', rowspan=4, columnspan=2, padx=40)

        # Level of Student
        self.student_level = tk.Button(self, text='Level of student', borderwidth=0, bg="#e35502")
        self.student_level.grid(row=15, column=1, sticky='nswe', pady=(10, 0))

    def show_course_assessments(self):
        # Retrieve input values
        student_name = self.entry_student_name.get()
        number_of_assessments = self.entry_assessment.get()
        course_code = self.entry_course_code.get()

        # Display number of assessments in the Text widget
        self.assessment_display.config(state='normal')
        self.assessment_display.delete('1.0', tk.END)
        self.assessment_display.insert('1.0', number_of_assessments)
        self.assessment_display.config(state='disable')

        # Process the inputs (e.g., look up the course code in a database)
        # For simplicity, let's assume we get the syllabus based on the course code
        course_syllabus = self.get_syllabus_for_course(course_code)

        # Display the syllabus in the label
        syllabus_text = f"Student: {student_name}\nAssessments: {number_of_assessments}\nCourse Code: {course_code}\nSyllabus: {course_syllabus}"
        self.syllabus_label.config(text=syllabus_text)

        # Update entry_5 with multiple entries
        self.entry_5.config(state='normal')
        self.entry_5.delete('1.0', tk.END)
        # Insert multiple lines
        self.entry_5.insert(tk.END, f"Student Name: {student_name}\n")
        self.entry_5.insert(tk.END, f"Assessments: {number_of_assessments}\n")
        self.entry_5.insert(tk.END, f"Course Code: {course_code}\n")
        self.entry_5.insert(tk.END, f"Syllabus: {course_syllabus}\n")
        self.entry_5.config(state='disable')

    def get_syllabus_for_course(self, course_code):
        # Simulate a database lookup for the course syllabus
        # In a real application, replace this with actual database queries
        syllabi = {
            "111": "Introduction to Computer Networks, Midterm, Final Exam",
            "112": "Object-Oriented Programming, Midterm, Final Project",
            "113": "Web Design & Programming, Midterm, Final Project",
            "114": "Introduction to Operating Systems, Midterm, Final Exam"
        }
        return syllabi.get(course_code, "Course syllabus not found")


if __name__ == "__main__":
    root = tk.Tk()
    app = CourseFrame1(master=root)  # Instantiate CourseFrame1
    app.mainloop()
