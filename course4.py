#!/usr/bin/python3

import tkinter as tk
from tkinter import messagebox

class Course4:
    def __init__(self):
        self.Q1 = 0.0
        self.Q2 = 0.0
        self.Pt = 0.0
        self.Final = 0.0
        self.MARK = 0.0
        self.MARK1 = 0.0
        self.MARK2 = 0.0
        self.MARK3 = 0.0
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
            self.MARK = self.Q1 * 10
            self.AVG = self.MARK
        elif num_params == 1:
            self.MARK = self.Q1 * 10
            self.MARK1 = self.Q2 * 10
            self.AVG = (self.MARK + self.MARK1) / 2
        elif num_params == 2:
            self.MARK = self.Q1 * 10
            self.MARK1 = self.Q2 * 10
            self.MARK2 = (self.Pt / 40) * 100
            self.AVG = (self.MARK + self.MARK1 + self.MARK2) / 3
        elif num_params == 3:
            self.MARK = self.Q1 * 10
            self.MARK1 = self.Q2 * 10
            self.MARK2 = (self.Pt / 40) * 100
            self.MARK3 = (self.Final / 40) * 100
            self.AVG = (self.MARK + self.MARK1 + self.MARK2 + self.MARK3) / 4

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

        message1 = (
            f"Quiz1: {self.Q1}\n"
            f"Quiz2: {self.Q2}\n"
            f"Mid term: {self.Pt}\n"
            f"Project: {self.Final}\n"
            f"AVG: {self.AVG}"
        )
        messagebox.showinfo("Course Marks", message1)
