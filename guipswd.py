import tkinter as tk
from tkinter import messagebox

class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Password Manager")
        self.root.geometry("400x400")
        self.passwords = {}

        # Labels and Entry fields
        tk.Label(root, text="Website:").pack()
        self.website_entry = tk.Entry(root, width=40)
        self.website_entry.pack()

        tk.Label(root, text="Username/Email:").pack()
        self.username_entry = tk.Entry(root, width=40)
        self.username_entry.pack()

        tk.Label(root, text="Password:").pack()
        self.password_entry = tk.Entry(root, width=40, show='*')
        self.password_entry.pack()

        # Buttons
        tk.Button(root, text="Save Password ✅", command=self.save_password).pack(pady=5)
        tk.Button(root, text="View Saved Passwords 🔍", command=self.view_passwords).pack(pady=5)

        # Listbox for displaying saved passwords
        self.output_box = tk.Listbox(root, width=50)
        self.output_box.pack(pady=10, fill="both", expand=True)

    def save_password(self):
        website = self.website_entry.get().strip()
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if website and username and password:
            self.passwords[website] = {"username": username, "password": password}
            messagebox.showinfo("Success", f"✅ Password for {website} saved!")
            self.website_entry.delete(0, tk.END)
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "⚠️ Please fill all fields.")

    def view_passwords(self):
        self.output_box.delete(0, tk.END)
        if not self.passwords:
            self.output_box.insert(tk.END, "📭 No passwords saved.")
        else:
            for site, creds in self.passwords.items():
                entry = f"🌐 {site} | 👤 {creds['username']} | 🔑 {creds['password']}"
                self.output_box.insert(tk.END, entry)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()
