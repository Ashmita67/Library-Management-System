import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import mysql.connector
from tabulate import tabulate

# --- MySQL connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # ← put your password here
    database="library"
)
mycursor = mydb.cursor()

# --- main window setup
root = tk.Tk()
root.title("Library Management System")
root.geometry("900x600")

# --- Function to switch to the Library System Page
def start_system():
    # Remove welcome screen and show system page
    welcome_frame.pack_forget()
    system_frame.pack(fill="both", expand=True)

# --- Function to show book records
def show_book():
    mycursor.execute("SELECT * FROM book")
    rows = mycursor.fetchall()
    result = tabulate(rows, headers=["Book_id", "Title", "Author", "Publisher", "Pages", "Price", "Edition", "Copies"], tablefmt="github")
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, result)

# --- Function to show member records
def show_member():
    mycursor.execute("SELECT * FROM member")
    rows = mycursor.fetchall()
    result = tabulate(rows, headers=["Member_id", "Name", "Class", "Address", "Mobile", "Email"], tablefmt="github")
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, result)

# --- Function to show transactions
def show_transactions():
    mycursor.execute("SELECT * FROM transactions")
    rows = mycursor.fetchall()
    result = tabulate(rows, headers=["Trans_id", "Book_id", "Member_id", "Date of Issue", "Date of Return"], tablefmt="github")
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, result)

# --- Function to add book record
def add_book():
    def save_book():
        sql = "INSERT INTO book (Title, Author, Publisher, Pages, Price, Edition, Copies) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (title_entry.get(), author_entry.get(), publisher_entry.get(), int(pages_entry.get()), float(price_entry.get()), int(edition_entry.get()), int(copies_entry.get()))
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Success", "Book added successfully!")
        add_window.destroy()

    add_window = tk.Toplevel(root)
    add_window.title("Add Book")
    add_window.geometry("400x400")
    
    tk.Label(add_window, text="Title:").pack()
    title_entry = tk.Entry(add_window)
    title_entry.pack()

    tk.Label(add_window, text="Author:").pack()
    author_entry = tk.Entry(add_window)
    author_entry.pack()

    tk.Label(add_window, text="Publisher:").pack()
    publisher_entry = tk.Entry(add_window)
    publisher_entry.pack()

    tk.Label(add_window, text="Pages:").pack()
    pages_entry = tk.Entry(add_window)
    pages_entry.pack()

    tk.Label(add_window, text="Price:").pack()
    price_entry = tk.Entry(add_window)
    price_entry.pack()

    tk.Label(add_window, text="Edition:").pack()
    edition_entry = tk.Entry(add_window)
    edition_entry.pack()

    tk.Label(add_window, text="Copies:").pack()
    copies_entry = tk.Entry(add_window)
    copies_entry.pack()

    tk.Button(add_window, text="Save Book", command=save_book).pack(pady=10)

# --- create the "Welcome" frame (this will show when the app opens)
welcome_frame = tk.Frame(root)
welcome_frame.pack(fill="both", expand=True)

tk.Label(welcome_frame, text="Welcome to the Library Management System", font=("Arial", 24)).pack(pady=50)
tk.Button(welcome_frame, text="Start", width=20, height=2, font=("Arial", 14), command=start_system).pack()

# --- create the system frame (hidden initially)
system_frame = tk.Frame(root)
system_frame.pack_forget()

# --- create the sidebar navigation in the system frame
sidebar = tk.Frame(system_frame, width=200, bg="lightgray", height=600, relief="sunken", borderwidth=2)
sidebar.pack(side="left", fill="y")

menu_buttons = [
    ("Add Book Record", add_book),
    ("Display Book Records", show_book),
    ("Display Member Records", show_member),
    ("Display Transactions", show_transactions),
    ("Exit", root.quit)
]

for label, command in menu_buttons:
    tk.Button(sidebar, text=label, width=20, anchor="w", command=command).pack(pady=10)

# --- create the output text area
output_text = tk.Text(system_frame, wrap="none", width=100, height=20)
output_text.pack(pady=20)

# --- start the Tkinter event loop
root.mainloop()
