'''
from abc import ABC, abstractmethod

class PaymentGetway(ABC):
        @abstractmethod
        def pay(self,amount):
         pass


        @abstractmethod
        def refund(self,amount):
         pass

class CreditCardPayment(PaymentGetway):
        def __init__(self,card_num,Holder_name):
                self.card_num=card_num
                self.Holder_name=Holder_name

        def pay(self,amount):
                print(f"Processing Credit Card payment of Rs.{amount} for{self.Holder_name}")

        def refund(self,amount):
                print(f"Rufunding ${amount} back to Credit Card ****{self.card_num}")

class PayPalPayment(PaymentGetway):
        def __init__(self,email):
                self.email= email

        def pay(self,amount):
                print(f"Processing PayPal payment of Rs.{amount} via account: {self.email}")
        def refund(self,amount):
                print(f"Refunding Rs.{amount} from PayPal account: {self.email}")

if __name__ =="__main__":
        print("--- Testing Credit Card Payment ---")
        cc__payment=CreditCardPayment("123456789","Suhag")
        cc__payment.pay(150.00)
        cc__payment.refund(50.00)
        print("\n-- Testing PayPal Payment ---")
        paypal_payment= PayPalPayment("yunishgurung@gmail.com")
        paypal_payment.pay(50.00)

        paypal_payment.refund(20.00)

        
n=10
try:
        res=n/0
except ZeroDivisionError:
        print("cant'be divided by zero")
print("can't be divided by zero")


def divided(a,b):
        try:
                return a/b
        except ZeroDivisionError as e:
                print("Logging Division by zero attempted.")
                raise

        try:
                result=divided(10,0)

        except ZeroDivisionError:
                print("Handled again in outer block")
                result=None  

import method

result = method.add(5, 3)
print(result)
from method import subtract
result = subtract(10, 4)
print(result)   

import method as mo
result = mo.add(7, 2)
print(result)

def divide(a,b):
    try:
        return a / b
    except (ZeroDivisionError, TypeError) as e:
        print(f"Error occurred: {e}")
        raise

try:
    divide(10, 0)
except ZeroDivisionError:
    print("Handled: Cannot divide by zero.\n")

try:
    divide(10, "a")
except TypeError:
    print("Handled: Invalid type for division.")

class MyCustomError(Exception):
    """Custom exception for my application."""
    pass

def check_age(age):
    if age < 0:
        raise MyCustomError("Age cannot be negative.")
    elif age < 18:
        raise MyCustomError("Age must be at least 18.")
    else:
        print(f"Age {age} is valid.")
try:
    check_age(-5)       
except MyCustomError as e:
    print(f"Custom Error: {e}")

class MyConnection:
    def __enter__(self):
        print("Opening connection...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing connection...")


with MyConnection() as conn:
    print("Using connection.")

s="Hello, World!"
print(s[6:12:1])
print(s[::-1])

for i in range(5):
    print(f"start only{i}",i)

a={1,2,3,4}
b={3,4,5,6}
print(a|b)
print(a&b)
print(a-b)
print(a^b)
a.add(10)
print(a)
a.remove(3)
print(a)
a.discard(8)
print(a)

faculty = {
 "Course_name":{"BCS":["BCA", "CSIT", "BIT"]  },
 "year":{1,2,3,4}
}

students = {
    "name": {"Suhag", "Nirajan"},
    "course": ["Python", "Java", "C++"],
    "principal": ["Mr. Sharma", "Mrs. Singh"]
}

print(students["name"])
print(students["course"][1])
print(students.get("principal"))
faculty.update(students)
print(faculty)
print(students)

square=[i**2 for i in range(1,11)]
print("Square of numbers from 1 to 11:", square)
numbers = [1, 2, 3, 4, 5]
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers from the list:", even_numbers)
labels=["even" if n%2==0 else "odd" for n in range(1,11)]
print("Labels for numbers from 1 to 10:", labels)   

a=str(input("Enter any string:"))
txt=a.split()
print(txt)
'''
txt="I love playing sports,I can play football and basketball"
print(txt.rpartition("and"))

title="Hello,My name is Suhag"
print(title.title())

swap="Hello,My name is Yunish"
print(swap.swapcase())
