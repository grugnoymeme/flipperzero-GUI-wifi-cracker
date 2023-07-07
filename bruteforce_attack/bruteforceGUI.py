import tkinter as tk
from tkinter import filedialog
import subprocess
import os
import string
import itertools
import webbrowser

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PCAP Files", "*.pcap *.cap *.pcapng")])
    if file_path:
        if file_path.endswith((".pcap", ".cap", ".pcapng")):
            file_entry.delete(0, tk.END)
            file_entry.insert(0, file_path)
            grab_button.config(state=tk.NORMAL)
        else:
            tk.messagebox.showerror("Format Error", "Invalid file format. Please select a .pcap, .cap, or .pcapng file.")


def execute_script():
    input_file = file_entry.get()
    hc22000_file = "wpa_crack.hc22000"
    subprocess.run(["hcxpcapngtool", "-o", hc22000_file, input_file])
    
    charset = string.printable  # Define the character set to be used
    
    for password_length in range(1, 11):
        for password in itertools.product(charset, repeat=password_length):
            password = ''.join(password)
            result = subprocess.run(["hashcat", "-m", "22000", hc22000_file, password], capture_output=True)
            if "Cracked" in result.stdout.decode():
                output_text.config(state=tk.NORMAL)
                output_text.delete("1.0", tk.END)
                output_text.insert(tk.END, f"Password found: {password}\n")
                output_text.config(state=tk.DISABLED)
                os.remove(hc22000_file)
                return
    
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "Password not found.\n")
    output_text.config(state=tk.DISABLED)
    os.remove(hc22000_file)

def open_github(event):
    webbrowser.open_new_tab("https://github.com/grugnoymeme")

def open_email(event):
    webbrowser.open_new_tab("mailto:47lecoste@tuta.io?subject=WPA/WPA2 WiFi Grabber")

root = tk.Tk()
root.title("WPA/WPA2 Crack Tool GUI")
root.geometry("500x650")
root.configure(bg="black")

title_label = tk.Label(root, text="Select .pcap file:", bg="black", fg="white", font=("Arial", 40))
title_label.place(relx=0.5, rely=0.13, anchor=tk.CENTER)

select_button = tk.Button(root, text="Select input file", command=select_file, width=10, height=1, font=("Arial", 15))
select_button.place(relx=0.5, rely=0.27, anchor=tk.CENTER)

file_entry = tk.Entry(root, width=40)
file_entry.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

grab_button = tk.Button(root, text="GRAB", state=tk.DISABLED, command=execute_script, width=15, height=2, font=("Arial", 25, "bold"))
grab_button.place(relx=0.5, rely=0.53, anchor=tk.CENTER)

output_text = tk.Text(root, width=50, height=8, state=tk.DISABLED)
output_text.place(relx=0.5, rely=0.80, anchor=tk.CENTER)

output_margin = tk.Frame(root, bg="black", width=500, height=25)
output_margin.place(relx=0.5, rely=0.94, anchor=tk.CENTER)

copyright_label = tk.Label(root, text="© 2023 • 47lecoste : ", bg="black", fg="white", font=("Arial", 10))
copyright_label.place(relx=0.43, rely=0.92, anchor=tk.CENTER)

github_label = tk.Label(root, text="GitHub", bg="black", fg="white", font=("Arial", 10, "underline"))
github_label.place(relx=0.56, rely=0.92, anchor=tk.CENTER)
github_label.bind("<Button-1>", open_github)

email_label = tk.Label(root, text="eMail", bg="black", fg="white", font=("Arial", 10, "underline"))
email_label.place(relx=0.63, rely=0.92, anchor=tk.CENTER)
email_label.bind("<Button-1>", open_email)
root.mainloop()
