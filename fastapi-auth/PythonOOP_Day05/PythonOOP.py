class BankAccount:
    """
    A simple Bank Account class to manage deposits, withdrawals, and balance inquiries.
    """

    def __init__(self, account_number: str, bank_name: str, account_type: str, initial_balance: float = 0.0) -> None:
        self.account_number = account_number
        self.bank_name = bank_name
        self.account_type = account_type
        self.balance = initial_balance

    def deposit(self, amount: float) -> float:
        """
        Deposits a positive amount into the bank account.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        """
        Withdraws a positive amount from the bank account if sufficient funds exist.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Withdrawal amount cannot be greater than the current balance.")

        self.balance -= amount
        return self.balance

    def get_balance(self) -> float:
        """
        Returns the current account balance.
        """
        return self.balance


# --- Usage Example ---
if __name__ == "__main__":
    # Creating a new bank account instance
    account = BankAccount(
        account_number="US123456789",
        bank_name="Kapital Bank",
        account_type="Deposit",
        initial_balance=100.0
    )

    print(f"Initial balance: {account.get_balance():.2f} USD")

    # We add money
    account.deposit(100.0)
    print(f"Balance after 100.00 USD deposit: {account.get_balance():.2f} USD")

    # Withdraw money
    account.withdraw(30.0)
    print(f"Balance after 30.00 USD withdrawal: {account.get_balance():.2f} USD")
