#!/usr/bin/python3

class StudentExpectationsSystem:
    def course_name(self):
        raise NotImplementedError
    def assessments(self):
        raise NotImplementedError

class Course1(StudentExpecationsSystem):
    def __init__(self, c_name):
        self.C_name = c_name
        self.MARK = 0.0
        self.MARK1 = 0.0
        self.MARK2 = 0.0
        self.MARK3 = 0.0
        self.MARK4 = 0.0
        self.AVG = 0.0
        self.report = ""
        self.X = ""

    def course_name(self):
        return self.C_name

    def F(self, Q1, Assignemnt, Pt=None, Final=None):
        self.MARK = Q1 * 10
        self.MARK1 = Assignment * 5
        self.MARK2 = Q2 * 10
        if Pt is not None:
            self.MARK3 = (Pt / 30) * 100
        else:
            self.MARK4 = 0.0

        # Calculate AVG based on the number of provided arguments
        num_args = 3
        if Pt is not None:
            num_args += 1
        if Final is not None:
            num_args += 1

        self.AVG = (self.MARK + self.MARK1 + self.MARK2 + self.MARK3 + self.MARK4) / num_args
        return self.AVG

    def Assessment(self):
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
        elif self.AVG < 50:
            self.X = "F"
