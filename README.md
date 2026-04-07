# Grocery-Billing-System_Devansh_202501100700062_ECE-B
CaseStudy-3

PROBLEM STATEMENT:
Design and implement a Smart Payment Processing System using Object-Oriented Programming concepts in Python. The system should allow a user to make payments using different payment methods such as Credit Card, UPI, PayPal, and Digital Wallet. Each payment method must follow a common interface but implement different business logic for computing the final payable amount.
Create an abstract base class named Payment that stores the user name and declares an abstract method pay(amount) which must be implemented by all child classes. The base class should also contain a concrete method generate_receipt() that prints the user name, original amount, and final amount paid after processing.
Implement the following payment types by inheriting from the Payment class:

1) CreditCardPayment: Apply a 2% gateway fee on the transaction amount and then apply 18% GST on the gateway fee. The final amount should be computed by adding the original amount, gateway fee, and GST.
2) UPIPayment: Provide a cashback of ₹50 if the payment amount is greater than 1000. Otherwise, no cashback is applied. The final payable amount should be calculated after subtracting cashback.
3) PayPalPayment: Apply a 3% international transaction fee and an additional fixed currency conversion fee of ₹20. These charges should be added to the original amount to compute the final payment.
4) WalletPayment: This payment method should maintain a wallet balance. If the payment amount exceeds the available balance, the transaction should fail. Otherwise, deduct the amount from the wallet and update the remaining balance.

Create a function process_payment(payment, amount) that accepts any payment object and calls its pay() method. This function should demonstrate runtime polymorphism, where the same function behaves differently depending on the payment type object passed.
Finally, create objects of all payment classes and process multiple transactions to demonstrate abstraction, inheritance, and polymorphism working together in a real-world payment processing system.


CODE:

from abc import ABC, abstractmethod

# Abstract Base Class
class Payment(ABC):
    def __init__(self, user_name):
        self.user_name = user_name
        self.final_amount = 0

    @abstractmethod
    def pay(self, amount):
        pass

    def generate_receipt(self, original_amount):
        print("----- Payment Receipt -----")
        print(f"User: {self.user_name}")
        print(f"Original Amount: ₹{original_amount}")
        print(f"Final Amount Paid: ₹{self.final_amount}")
        print("---------------------------\n")


# Credit Card Payment
class CreditCardPayment(Payment):
    def pay(self, amount):
        gateway_fee = 0.02 * amount
        gst = 0.18 * gateway_fee
        self.final_amount = amount + gateway_fee + gst
        self.generate_receipt(amount)


# UPI Payment
class UPIPayment(Payment):
    def pay(self, amount):
        cashback = 50 if amount > 1000 else 0
        self.final_amount = amount - cashback
        self.generate_receipt(amount)


# PayPal Payment
class PayPalPayment(Payment):
    def pay(self, amount):
        intl_fee = 0.03 * amount
        conversion_fee = 20
        self.final_amount = amount + intl_fee + conversion_fee
        self.generate_receipt(amount)


# Wallet Payment
class WalletPayment(Payment):
    def __init__(self, user_name, balance):
        super().__init__(user_name)
        self.balance = balance

    def pay(self, amount):
        if amount > self.balance:
            print(f"Transaction Failed! Insufficient balance in {self.user_name}'s wallet.")
        else:
            self.balance -= amount
            self.final_amount = amount
            self.generate_receipt(amount)
            print(f"Remaining Wallet Balance: ₹{self.balance}\n")


# Polymorphic function
def process_payment(payment, amount):
    payment.pay(amount)


# Demonstration
if __name__ == "__main__":
    # Create payment objects
    cc_payment = CreditCardPayment("Devansh")
    upi_payment = UPIPayment("Devansh")
    paypal_payment = PayPalPayment("Devansh")
    wallet_payment = WalletPayment("Devansh", balance=1500)

    # Process transactions
    process_payment(cc_payment, 1000)       # Credit Card
    process_payment(upi_payment, 1200)      # UPI
    process_payment(paypal_payment, 800)    # PayPal
    process_payment(wallet_payment, 1000)   # Wallet (success)
    process_payment(wallet_payment, 600)    # Wallet (fail due to insufficient balance)

OUTPUT:

----- Payment Receipt -----
User: Devansh
Original Amount: ₹1000
Final Amount Paid: ₹1023.6
---------------------------

----- Payment Receipt -----
User: Devansh
Original Amount: ₹1200
Final Amount Paid: ₹1150
---------------------------

----- Payment Receipt -----
User: Devansh
Original Amount: ₹800
Final Amount Paid: ₹844.0
---------------------------

----- Payment Receipt -----
User: Devansh
Original Amount: ₹1000
Final Amount Paid: ₹1000
---------------------------

Remaining Wallet Balance: ₹500

Transaction Failed! Insufficient balance in Devansh's wallet.


