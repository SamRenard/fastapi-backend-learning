from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Optional


@dataclass
class Book:
    book_id: str
    title: str
    author: str
    is_available: bool = True


@dataclass
class Member:
    member_id: str
    name: str


@dataclass
class Loan:
    book: Book
    member: Member
    due_date: datetime
    loan_date: datetime = field(default_factory=datetime.now)


def borrow_book(book: Book, member: Member, days: int) -> Optional[Loan]:
    """
    Processes a book borrowing transaction for a library system.

    Args:
        book (Book): The book object to be borrowed.
        member (Member): The library member borrowing the book.
        days (int): The number of days the book is loaned for.

    Returns:
        Optional[Loan]: A Loan object if the transaction is successful, None otherwise.
    """
    if not book.is_available:
        print(f"Error: The book '{book.title}' is currently unavailable.")
        return None

    # Update book availability status
    book.is_available = False

    # Calculate the exact due date based on the current time
    due_date = datetime.now() + timedelta(days=days)

    # Generate and return the loan record
    loan = Loan(book=book, member=member, due_date=due_date)
    print(f"Success: '{book.title}' has been loaned to {member.name} until {due_date.strftime('%Y-%m-%d')}.")

    return loan


# --- Example Usage ---
if __name__ == "__main__":
    book1 = Book(book_id="B001", title="Artificial Intelligence: A Modern Approach", author="Stuart Russell")
    member1 = Member(member_id="M001", name="Ali Aliyev")

    # Borrowing the book for 14 days
    active_loan = borrow_book(book=book1, member=member1, days=14)

    # Attempting to borrow the same book again to test the error logic
    failed_loan = borrow_book(book=book1, member=member1, days=7)