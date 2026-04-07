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