# You can remove 'pass' when you start writing the class.
# Read README.md for exactly what each class must do.

# Exercise 1
class BusCard:
    def __init__(self,owner):
        self.owner = owner
        self.balance = 0
        self.trips = 0
    def top_up(self,amount):
        if amount<1:
            return False
        else:
            self.balance += amount
            return True

    def pay(self,fare):
        if self.balance>=fare:
            self.balance = self.balance - fare
            self.trips += 1
            return True
        else:
            return False

# Exercise 2
class Student:
    def __init__(self,name):
        self.name  =name
        self.grades = []
    def add_grade(self,score):
        if 0<=score<=100:
            self.grades.append(score)
            return True
        else:
            return False
    def average(self):
        total = 0
        for i in range(len(self.grades)):
            total += self.grades[i]
        return  total/len(self.grades)

    def highest(self):
        highest = self.grades[0]
        for i in range(len(self.grades)):
            if highest < self.grades[i]:
                highest = self.grades[i]
        return highest
# Exercise 3
class Song:
    pass


class Playlist:
    pass
