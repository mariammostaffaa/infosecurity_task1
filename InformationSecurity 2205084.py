import tkinter as tk
from tkinter import ttk
import itertools
import string

USER_PASSWORDS = {
    "user1": "mariam",  
    "user2": "2205084",  
    "user3": "hello", 
    "user4": "qwpdpdn",  
    "user5": "20j2$md@#$@" 
}

DICTIONARY = ["password", "123456", "qwerty", "abcde", "letmein", "admin", "welcome","mariam","2205084"]

def dictionary_attack(username):
    correct_password = USER_PASSWORDS.get(username, "")
    for password in DICTIONARY:
        if password == correct_password:
            return True, password
    return False, None

def brute_force_attack(username):
    correct_password = USER_PASSWORDS.get(username, "")
    chars = string.ascii_letters  
    length = 5  
    
    for attempt in itertools.product(chars, repeat=length):
        attempt = ''.join(attempt)
        if attempt == correct_password:
            return True, attempt
    return False, None

def on_submit():
    username = username_var.get()
    attack_method = attack_var.get()
    result_text.set(" Searching for password... ")
    root.update()
    
    if attack_method == "Dictionary Attack":
        success, password = dictionary_attack(username)
    else:
        success, password = brute_force_attack(username)
    
    if success:
        result_text.set(f"✨ Password found: {password} ✨")
    else:
        result_text.set("💔 Password not found 💔")

root = tk.Tk()
root.title("Password Cracker ")
root.geometry("450x400")
root.configure(bg="#FFD1DC")  

style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#FFD1DC")
style.configure("TLabel", background="#FFD1DC", foreground="#FF69B4", font=("Arial", 12))
style.configure("TButton", background="#FF69B4", foreground="white", font=("Arial", 12, "bold"), padding=10)
style.configure("TCombobox", fieldbackground="#FFFFFF", foreground="#FF69B4", font=("Arial", 12))
style.configure("TRadiobutton", background="#FFD1DC", foreground="#FF69B4", font=("Arial", 12))

frame = ttk.Frame(root, padding="20")
frame.pack(pady=20)

title_label = ttk.Label(frame, text=" Mariam Mostafa Amin - 2205084 ", font=("Arial", 16, "bold"), background="#FFD1DC", foreground="#FF69B4")
title_label.pack(pady=10)

username_label = ttk.Label(frame, text="Enter Username:")
username_label.pack()
username_var = tk.StringVar()
username_entry = ttk.Entry(frame, textvariable=username_var, width=20)
username_entry.pack(pady=5)

attack_var = tk.StringVar(value="Dictionary Attack")
dictionary_radio = ttk.Radiobutton(frame, text="💖 Dictionary Attack 💖", variable=attack_var, value="Dictionary Attack")
brute_force_radio = ttk.Radiobutton(frame, text="🌸 Brute Force Attack 🌸", variable=attack_var, value="Brute Force Attack")
dictionary_radio.pack()
brute_force_radio.pack()

submit_button = ttk.Button(frame, text="✨ Crack Password ✨", command=on_submit)
submit_button.pack(pady=10)

result_text = tk.StringVar()
result_text.set("💗 Result will appear here... 💗")
result_label = ttk.Label(frame, textvariable=result_text)
result_label.pack(pady=10)

root.mainloop()