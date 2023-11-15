from tkinter import*
import random
import pyperclip
import string

window = Tk() #creates our window object
window.geometry("720x720") #sets the size of the window
window.title("Password Generator") #sets title of window
n = StringVar() # creates object of class StringVar
password = StringVar()
n.set("") #default length is 0


def generate():

    # creates 4 lists which each contain a specific type of required character
    upperlist = list(string.ascii_uppercase)
    lowerlist = list(string.ascii_lowercase)
    diglist = list(string.digits)
    speccharlist = list("!-$%&'()*+,./:;<=>?_[]^`{|}~")
   
    allcharlist = upperlist + lowerlist + diglist + speccharlist  #list of all possible characters 
    
    #creates a password of length 4 which has all the required charaters
    genpass= ''.join(random.choice(upperlist)+random.choice(lowerlist)+random.choice(diglist)+random.choice(speccharlist ))  
    
    # loop is used to add the rest of the characters in order to create a password with n characters
    i = 4
    j = int(float(n.get()))
    for k in range(i,j):
        genpass = ''.join(genpass+random.choice(allcharlist))
        
    
    # characters of generated password is then shuffled in order another layer of randomness
    genpasslist=list(genpass)  
    random.shuffle(genpasslist)
    genpassfinal=''.join(genpasslist)
    global password
    # final generated password is set to password object
    password.set(genpassfinal)

def copypass():
    global password
    copythis = password.get()
    pyperclip.copy(copythis)
    
# adds text labels to window
Label(window, text = "Secure Password Generator", font="TimesNewRoman 20 bold").pack()
Label(window, text = "Please enter desired password length", font="TimesNewRoman 15").pack(pady=20)
Label(window, text = "Must be of length 4 or greater", pady=20, font="TimesNewRoman 14").pack()

Entry(window, textvariable=n).pack(pady=25) # creates box for user input of password length
Button(window, text="Generate Password", command=generate).pack(pady=10) # creates button, when pushed generates the password
Entry(window, textvariable=password).pack(pady=25) # creates box that shows generated password
Button(window, text="Copy Password", command=copypass).pack(pady=10) # creates button, when pushed copies password to clipboard

window.mainloop()
