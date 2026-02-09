import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import mysql.connector


def get_conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="expenses_db"
    )


def add_expense():
    date = date_entry.get()
    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Enter a valid amount!")
        return
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO expenses (date, amount) VALUES (%s, %s)", (date, amount)
    )

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Expense added!")
    amount_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Simple Expanse Tracker.")
root.geometry("300x200")

tk.Label(root, text="Date").pack()
date_entry = DateEntry(root)
date_entry.pack()

tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Button(root, text="Add Expense", command=add_expense).pack(pady=10)


root.mainloop()
