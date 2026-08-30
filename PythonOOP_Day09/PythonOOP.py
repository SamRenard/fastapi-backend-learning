from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    """
    Abstract Base Class (ABC) representing a generic payment processor.
    This class demonstrates abstraction by defining a blueprint for all payment types.
    """

    @abstractmethod
    def process_payment(self, amount: float) -> None:
        """
        Process a payment for a given amount.
        Must be overridden by all subclasses.

        Args:
            amount (float): The payment amount to be processed.
        """
        pass


class StripeProcessor(PaymentProcessor):
    """
    Stripe implementation of the PaymentProcessor.
    """

    def process_payment(self, amount: float) -> None:
        """
        Process payment using the Stripe gateway.
        """
        print(f"[SUCCESS] Stripe payment method called. Amount processed: ${amount:.2f}")


class PayPalProcessor(PaymentProcessor):
    """
    PayPal implementation of the PaymentProcessor.
    """

    def process_payment(self, amount: float) -> None:
        """
        Process payment using the PayPal gateway.
        """
        print(f"[SUCCESS] PayPal payment method called. Amount processed: ${amount:.2f}")


# The main execution block
if __name__ == "__main__":
    print("--- Initiating Payment Processing System ---")

    # Demonstrating Polymorphism:
    # A single interface (process_payment) is used for different data types (Stripe, PayPal)
    processors: list[PaymentProcessor] = [
        StripeProcessor(),
        PayPalProcessor()
    ]

    payment_amount = 100.00

    for processor in processors:
        processor.process_payment(payment_amount)

    print("--- All payments processed successfully ---")
