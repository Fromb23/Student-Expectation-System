#!/usr/bin/python3

import tkinter as tk
from tkinter import messagebox

class Course2:
    def __init__(self):
        self.Q1 = 0.0
        self.Q2 = 0.0
        self.Pt = 0.0
        self.Final = 0.0
        self.AVG = 0.0
        self.X = ""

    def F(self, Q1, Q2=None, Pt=None, Final=None):
        self.Q1 = Q1
        self.Q2 = Q2 if Q2 is not None else 0.0
        self.Pt = Pt if Pt is not None else 0.0
        self.Final = Final if Final is not None else 0.0

        # Calculate AVG based on the number of provided parameters
        num_params = sum(1 for param in [Q2, Pt, Final] if param is not None)

        if num_params == 0:
            self.AVG = self.Q1 * 10
        elif num_params == 1:
            self.AVG = (self.Q1 * 10 + self.Q2 * 10) / 2
        elif num_params == 2:
            self.AVG = (self.Q1 * 10 + self.Q2 * 10 + (self.Pt / 40) * 100) / 3
        elif num_params == 3:
            self.AVG = (self.Q1 * 10 + self.Q2 * 10 + (self.Pt / 40) * 100 + (self.Final / 40) * 100) / 4

        return self.AVG

    def Course_name(self):
        messagebox.showinfo("Course Info", f"Average: {self.AVG}")

    def Assessments(self):
        if self.AVG >= 90:
            self.X = "A"
        elif self.AVG >= 80:
            self.X = "B"
        elif self.AVG >= 70:
            self.X = "C"
        elif self.AVG >= 60:
            self.X = "D"
        elif self.AVG >= 50:
            self.X = "E"
        else:
            self.X = "F"

        messagebox.showinfo("Course Marks", f"AVG: {self.AVG}\nGrade: {self.X}")

