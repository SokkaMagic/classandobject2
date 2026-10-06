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
    pass

# Exercise 3
class Song:
    pass


class Playlist:
    pass
