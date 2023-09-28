import tkinter as tk #Specific tool to use UI options
#Louis Copeland
#Ability to add password(s)
def add_password():
    password = entry.get()
    if password:
        passwords.append(password)
        entry.delete(0, tk.END) #Ends/ Kills the text process

#Ability to review all stored passwords in the log
def show_passwords():
    password_list.delete(0, tk.END)
    password_list.insert(tk.END, *passwords)

#Ability to save stored passwords to a .txt file
def save_passwords():
    with open("passwords.txt", "w") as file:
        file.write("\n".join(passwords)) #Creates the .txt file to store passwords

#This is the list that stores the passwords
passwords = []
window = tk.Tk() #Main UI window
window.title("password Storage")

#Text box to enter passwords into
entry = tk.Entry(window, width=40)
add_button = tk.Button(window, text="Add password", command=add_password) #Add a button which allows a user to add passwords
show_button = tk.Button(window, text="Show passwords", command=show_passwords) #Add a button which allows user to see password list
save_button = tk.Button(window, text="Save passwords", command=save_passwords) #Add a button which saves all previously entered passwords to a .txt file
password_list = tk.Listbox(window, width=45) #When "show passwords" button is pressed a list of saved passwords will show

#Interface layout packing options
entry.pack(pady=10)
add_button.pack()
show_button.pack()
save_button.pack()
password_list.pack(pady=10)

#TKinter UI main loop
window.mainloop()
