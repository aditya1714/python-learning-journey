'''Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways'''

from random import randint
n = int(input("Enter Your Train Numeber : "))

class Train:

    def __init__(self, n):
        self.n = n

    def book(self, fro, to):
        print(f"Ticket is booked in Train no : {self.n} from {fro} to {to}successfully.")

    def getstatus(self):
        print(f"Train no : {self.n} is running on time.")

    def getfare(self, fro, to ):
        print(f"Ticket fare for Train no : {self.n} from {fro} to {to} is {randint(120, 340)}")

t = Train(n)
t.book("Patna", "Delhi")
t.getstatus()
t.getfare("Patna", "Delhi")