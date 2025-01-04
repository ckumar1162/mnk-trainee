import tkinter as tk
from tkinter import messagebox
import pandas as pd


def load_data():
    try:
        return pd.read_csv("users.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["unique_id", "name", "address", "designation"])
        df.to_csv("users.csv", index=False)
        return df


df = load_data()


def add_user():
    user_name = entry_name.get()
    user_address = entry_address.get()
    user_designation = entry_designation.get()
    unique_id = len(df) + 1

    if user_name not in df["name"].values:
        df.loc[len(df)] = [unique_id, user_name, user_address, user_designation]
        df.to_csv("users.csv", index=False)
        messagebox.showinfo("Success", "User added successfully!")
    else:
        messagebox.showerror("Error", "The username already exists.")


def view_user():
    try:
        user_id = int(entry_user_id.get())
        user_data = df[df["unique_id"] == user_id]
        if not user_data.empty:
            user_info = user_data[["name", "address", "designation"]].to_string(index=False)
            messagebox.showinfo("User Details", user_info)
        else:
            messagebox.showerror("Error", "User ID not found.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid User ID.")


def filter_users():
    name_filter = entry_filter_name.get().lower()
    address_filter = entry_filter_address.get().lower()
    designation_filter = entry_filter_designation.get().lower()

    filtered_df = df[
        df["name"].str.contains(name_filter, case=False) &
        df["address"].str.contains(address_filter, case=False) &
        df["designation"].str.contains(designation_filter, case=False)
        ]

    if not filtered_df.empty:
        users_list = filtered_df[["unique_id", "name", "address", "designation"]].to_string(index=False)
        messagebox.showinfo("Filtered Users", users_list)
    else:
        messagebox.showinfo("Info", "No users match the filter.")


def delete_user():
    try:
        user_id = int(entry_user_id.get())
        user_index = df[df["unique_id"] == user_id]
        if not user_index.empty:
            confirm = messagebox.askyesno("Confirmation", f"Do you want to delete user {user_index['name'].values[0]}?")
            if confirm:
                df.drop(user_index.index, inplace=True)
                df.to_csv("users.csv", index=False)
                messagebox.showinfo("Success", "User deleted successfully!")
        else:
            messagebox.showerror("Error", "User ID not found.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid User ID.")


window = tk.Tk()
window.title("User Management System")
window.config(padx=50, pady=50)

label_name = tk.Label(window, text="Name:")
label_name.grid(row=0, column=0)
entry_name = tk.Entry(window)
entry_name.grid(row=0, column=1)

label_address = tk.Label(window, text="Address:")
label_address.grid(row=1, column=0)
entry_address = tk.Entry(window)
entry_address.grid(row=1, column=1)

label_designation = tk.Label(window, text="Designation:")
label_designation.grid(row=2, column=0)
entry_designation = tk.Entry(window)
entry_designation.grid(row=2, column=1)

label_user_id = tk.Label(window, text="User ID:")
label_user_id.grid(row=3, column=0)
entry_user_id = tk.Entry(window)
entry_user_id.grid(row=3, column=1)

label_filter_name = tk.Label(window, text="Filter by Name:")
label_filter_name.grid(row=4, column=0)
entry_filter_name = tk.Entry(window)
entry_filter_name.grid(row=4, column=1)

label_filter_address = tk.Label(window, text="Filter by Address:")
label_filter_address.grid(row=5, column=0)
entry_filter_address = tk.Entry(window)
entry_filter_address.grid(row=5, column=1)

label_filter_designation = tk.Label(window, text="Filter by Designation:")
label_filter_designation.grid(row=6, column=0)
entry_filter_designation = tk.Entry(window)
entry_filter_designation.grid(row=6, column=1)

btn_add_user = tk.Button(window, text="Add User", command=add_user)
btn_add_user.grid(row=7, column=0)

btn_view_user = tk.Button(window, text="View User", command=view_user)
btn_view_user.grid(row=7, column=1)

btn_filter_users = tk.Button(window, text="Filter Users", command=filter_users)
btn_filter_users.grid(row=8, column=0)

btn_delete_user = tk.Button(window, text="Delete User", command=delete_user)
btn_delete_user.grid(row=8, column=1)

result_label = tk.Label(window, text="", fg="green")
result_label.grid(row=9, column=0, columnspan=2)

window.mainloop()