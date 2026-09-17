'''Create an abstract class PaymentGateway with abstract methods pay() and refund(). Implement two subclasses: CreditCardPayment and PayPalPayment. Demonstrate calling their methods.'''

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
        cc__payment=CreditCardPayment("123456789","Yunish")
        cc__payment.pay(150.00)
        cc__payment.refund(50.00)
        print("\n-- Testing PayPal Payment ---")
        paypal_payment= PayPalPayment("yunishgurung@gmail.com")
        paypal_payment.pay(50.00)
        paypal_payment.refund(20.00)
