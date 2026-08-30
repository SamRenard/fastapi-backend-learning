# Day 9: Advanced OOP in Python - Abstraction & Polymorphism

This repository contains my daily practice for Day 9 of the Python OOP challenge. The primary focus of this project is to implement **Abstract Base Classes (ABC)** and demonstrate **Polymorphism** in a real-world scenario.

## 🚀 Project Overview

In this project, I simulated a payment processing system. Instead of writing separate, unrelated classes for different payment gateways, I used **Abstraction** to create a strict blueprint (`PaymentProcessor`) that enforces consistency across all payment methods.

### Key Concepts Demonstrated:
*   **Abstract Base Classes (ABC):** Using the `abc` module to create the `PaymentProcessor` interface.
*   **Encapsulation & Blueprinting:** Enforcing the `process_payment` method on all child classes using the `@abstractmethod` decorator.
*   **Polymorphism:** Iterating through a list of different processor objects (`StripeProcessor`, `PayPalProcessor`) and calling the identical `.process_payment()` method on each, yielding different behaviors.
*   **Clean Code Practices:** Applied type hinting (`-> None`, `amount: float`) and comprehensive docstrings for better readability and maintainability.

## 🛠️ How to Run

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Run the Python script:
   ```bash
   python PythonOOP.py