# Python OOP Basics - Library Management System

A streamlined, object-oriented Library Management System built with Python. This mini-project from Day 10 of my OOP journey demonstrates core Object-Oriented Programming principles, utilizing modern Python features for clean and maintainable code.

## 🚀 Features

* **Dataclasses Integration:** Uses Python's `@dataclass` decorator to efficiently manage `Book`, `Member`, and `Loan` models.
* **Static Typing:** Fully integrated `type hints` (`typing` module) to ensure type safety.
* **Robust Logic:** Simple yet effective transaction logic that prevents borrowing unavailable books and dynamically calculates due dates.

## 🛠️ Technologies Used

* **Language:** Python 3.9+
* **Core Modules:** `dataclasses`, `datetime`, `typing`

## 💻 Quick Start

Clone the repository:
```bash
git clone [https://github.com/SamRenard/python-oop-basics.git](https://github.com/SamRenard/python-oop-basics.git)

🏗️ Code Structure
 * Book: Represents a book entity tracking its availability.
 * Member: Represents a library member.
 * Loan: Represents the transaction record, calculating loan and due dates automatically.
 * borrow_book(): Core business logic handling the checkout process.