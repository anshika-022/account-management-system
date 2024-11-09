import tkinter as tk
from tkinter import messagebox

# Define the Account class
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        if amount > self.balance:
            return f"Insufficient funds. Your balance is: Rs {self.get_balance()}"
        self.balance -= amount
        return f"Rs {amount} was debited.\nTotal balance is: Rs {self.get_balance()}"

    def credit(self, amount):
        self.balance += amount
        return f"Rs {amount} was credited.\nTotal balance is: Rs {self.get_balance()}"

    def get_balance(self):
        return self.balance

# Initialize the GUI window
def create_account():
    try:
        bal = float(balance_entry.get())
        acc_no = int(acc_no_entry.get())
        global acc1
        acc1 = Account(bal, acc_no)
        messagebox.showinfo("Success", "Account created successfully!")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid account details.")

def perform_debit():
    try:
        amount = float(amount_entry.get())
        message = acc1.debit(amount)
        result_label.config(text=message)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")
    except NameError:
        messagebox.showerror("Error", "Please create an account first.")

def perform_credit():
    try:
        amount = float(amount_entry.get())
        message = acc1.credit(amount)
        result_label.config(text=message)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")
    except NameError:
        messagebox.showerror("Error", "Please create an account first.")

# Creating the UI
window = tk.Tk()
window.title("Bank Account Manager")
window.geometry("400x400")

# Account details
tk.Label(window, text="Account Number:").pack(pady=5)
acc_no_entry = tk.Entry(window)
acc_no_entry.pack(pady=5)

tk.Label(window, text="Initial Balance:").pack(pady=5)
balance_entry = tk.Entry(window)
balance_entry.pack(pady=5)

tk.Button(window, text="Create Account", command=create_account).pack(pady=10)

# Transaction section
tk.Label(window, text="Enter Amount:").pack(pady=5)
amount_entry = tk.Entry(window)
amount_entry.pack(pady=5)

tk.Button(window, text="Debit", command=perform_debit).pack(pady=5)
tk.Button(window, text="Credit", command=perform_credit).pack(pady=5)

# Result
result_label = tk.Label(window, text="")
result_label.pack(pady=20)

# Run the application
window.mainloop()
