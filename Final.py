import tkinter as tk #Import tkinter

#Create the Gui
root = tk.Tk()
root.title ("Francisco's Phone Book")
root.geometry ("600x600")

# creates listbox to hold the contacts
contactsList = tk.Listbox(root) #defines the contactsList as a Listbox
contact = {} #contact holds the contact info that is input



# function for the add contact button
def add():
   name = nameInput.get() # defines name as the input the user inputs for name
   num= numInput.get() # defines num as the input the user inputs for Number
   address = addressInput.get() # defines address as the input the user inputs for address
   email = emailInput.get("1.0", "end-1c") # defines email as the input the user inputs for email


   contactsList.insert(tk.END, name)
   contact[name] = {"number": num, "email": email, "address": address}


   nameInput.delete(0, tk.END)
   numInput.delete(0, tk.END)
   addressInput.delete(0, tk.END)
   emailInput.delete("1.0", tk.END)

#function for the see contact button
def seeContact():
   name = contactsList.get(contactsList.curselection())
   num = contact[name]["number"]
   address = contact[name]["address"]
   email = contact[name]["email"]


   nameInput.insert(0, name)
   numInput.insert(0, num)
   addressInput.insert(0, address)
   emailInput.insert("1.0", email)

# function for when the user wants to use the delete a contact button
def deleteContact():
   name = contactsList.get(contactsList.curselection())
   contactsList.delete(tk.ANCHOR)
   contact.pop(name)

# function for exit button
def exit():
   root.destroy()

# creates the function for the help button click which Calls for the show_help_popup function when
def help():
   show_help_popup()

# creates teh other GUI window which is a pop up if the user needs help
def show_help_popup():
   popup = tk.Toplevel(root) #defines popup as the popup youn get when you click help
   popup.title("Help")
   popup.geometry("400x400".format(root.winfo_screenwidth() // 2 - 100, root.winfo_screenheight() // 2 - 100))


   message = tk.Label(popup, text="If you need help please refer to the manuel in the .zip",)
   message.pack(fill=tk.BOTH, expand=True)

# Creates the input boxes for the user to input the contacts
nameInput = tk.Entry(root)
numInput = tk.Entry(root)
addressInput = tk.Entry(root)
emailInput = tk.Text(root, height=2, width=26)

#Places the grid boxes from above
nameInput.grid(row=0, column=1)
numInput.grid(row=1, column=1)
addressInput.grid(row=2, column=1,)
emailInput.grid(row=3, column=1, rowspan=2)


# all buttons are made and named and placed
addBut = tk.Button(root, text="Add", command=add).place (x=50, y=180) #addbutton is the button for add contact
seeBut = tk.Button(root, text="See Contact Info", command=seeContact).place (x=90, y=180) #seeBut is the button to see your contact
delBut = tk.Button(root, text="Delete Contact Info", command=deleteContact).place (x=200, y=180)#delBut is the delete contact button
exitBut= tk.Button(root, text="Exit Program", foreground="red", command=exit).place (x=500, y=550) #exitBut is the button to Exit the program
helpBut = tk.Button(root, text="Help", background="orange", foreground="gold", command=help).place (x=10, y=550) #helpBut is the help button


# Labels are named
name_label = tk.Label(root, text="Name")
num_label = tk.Label(root, text="Number")
address_label = tk.Label(root, text="Address")
email_label = tk.Label(root, text="Email")

#Labels are put next to the input boxes
name_label.grid(row=0, column=0, sticky="W")
num_label.grid(row=1, column=0, sticky="W")
address_label.grid(row=2, column=0, sticky="W")
email_label.grid(row=3, column=0, sticky="W")


# Contact List is placed and colored
contactsList.place(x=20, y=300)
contactsList.configure(background="cornsilk2", foreground="gray44", width=40)




root.mainloop()



