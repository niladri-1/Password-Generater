import string, secrets, pyperclip
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


root = Tk()
root.geometry('400x330')  # width x hight
root.iconbitmap('icon.ico')
root.title('  Password Genarater')
root.resizable(0,0)


a=[]
switch_value = True

def generate_password(length=25, symbols=True, uppercase = True):
    combination = string.ascii_lowercase + string.digits
    if symbols:
        combination += string.punctuation
    if uppercase:
        combination += string.ascii_uppercase
    combination_lenth = len(combination)
    new_password = ""
    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_lenth)]
        
    a.append(new_password)
    print(new_password)
    result_label.config(text=new_password)
    
    with open("records.txt","w") as f:
        for i in a:
            f.write(f"{i} \n")


def copy():
    c = pyperclip.copy(a[len(a)-1])
    messagebox.showinfo('Passwoed Genarater','Password Copied!')
    print("Copied!")
    
    
def toggle():
    global switch_value
    if switch_value == True:
        switch.config(image=light, bg='#26242f', activebackground="#26262f")
        h1_lavel.config(fg="white", bg="#26262f")
        h2_lavel.config(fg="white", bg="#26262f")
        result_label.config(fg="white", bg="#26262f")
        f1.config(bg="white")

        # Change the window to dark theme
        root.config(bg="#26242f")
        switch_value = False

        
    else:
        switch.config(image=dark, bg="white", activebackground="white")
        h1_lavel.config(fg="#000080", bg="white")
        h2_lavel.config(fg="#000080", bg="white")
        result_label.config(fg="#000080", bg="white")
        f1.config(bg="black")


        # Chenges the window to light theme
        root.config(bg="white")
        switch_value = True
        


light = Image.open('Light.png')
resized_light = light.resize((30,30))
light = ImageTk.PhotoImage(resized_light)


dark = Image.open('dark.png')
resized_dark = dark.resize((30,30))
dark = ImageTk.PhotoImage(resized_dark)



# Switch to Dark & Light Mode
switch = Button(root, image=dark, bd=0, command=toggle, cursor="hand2")
switch.place(x=350, y=10)

# Heading 1
h1_lavel = Label(root, text="Wellcome")
h1_lavel.config(font=("verdana 15 bold"), fg="#000080")
h1_lavel.place(x=140, y=2)

# Heading 2
h2_lavel = Label(root, text="Password Generater")
h2_lavel.config(font=("verdana 16"), fg="#000080")
h2_lavel.place(x=90, y=40)

# Button to generate Password by generate_password() class
btn_lavel = Button(root, text='Click to Generate!')
btn_lavel.config(font=('verdana 10'), fg='#000080', bg='#EEEE40',  cursor="hand2", command=generate_password)
btn_lavel.place(x=130, y=85)

# Get new password by clicking "Click to Generate!"
result_label = Label(root, text="Click the above button to get password", cursor="pirate")
result_label.config(font=("verdana 11"), fg="#000080")
result_label.pack(pady=140)

f1=Frame(root, width=300, height=2, bg='black')
f1.place(x=50, y=170)

# Button to copy the generated password  
btn2_lavel= Button(root, text="Copy to Clipbord!")
btn2_lavel.config(font=("verdana 10"), fg="#000080", bg="#EEEE40", cursor="hand2", command=copy)
btn2_lavel.place(x=130, y=190)

# Footer
footer_lavel = Label(root, text="Thank You!")
footer_lavel.config(font=('verdana 10'), fg='white', bg='green')
footer_lavel.pack(side=BOTTOM, fill=X)

       
root.mainloop()