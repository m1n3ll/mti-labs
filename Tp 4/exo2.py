class PaymentProcessor:
    def process_payment(self, amount, method):
        if method == "credit_card":
            # Process credit card
            pass
        elif method == "paypal":
            # Process PayPal
            pass
        elif method == "bitcoin":
            # Process Bitcoin
            pass

 # Violate the Open/Closed Principle : Open for extension, closed for modification

from abc import ABC, abstractmethod

class PaymentMethod:
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        pass

class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        pass 

class BitCoinPayment(PaymentMethod):
    def pay(self, amount):
        pass

class PaymentProcessor:
    def process_payment(self, amount, payment_method : PaymentMethod):
        payment_method.pay(amount)


