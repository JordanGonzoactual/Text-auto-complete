import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from trielogic import Trie
from sourcewords import wordsource



# Class for interface
class interface(tk.Tk):
     # Initializes window
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Typemaster")
        self.geometry('1920x1080')
        self.trie = Trie()
        self.words = wordsource()
        self.add_background()
        self.addwidgets()
        

     # Adds widgets to GUI
    def addwidgets(self):
        
         # Frame for entry box
        self.entryframe = tk.Frame(self, bg='black', width= 300, height=29, relief= RAISED)
        self.entryframe.place(x= 600, y= 200)
        self.entryframe.winfo_width()
        self.entryframe.winfo_height()
         
         # Records User input
        self.User_input= tk.StringVar()
       
         
         # Entry box 
        self.entrybox = tk.Entry(self.entryframe, textvariable= self.User_input, bg='white')
        self.entrybox.place(x = 2, y =2, height= 25, width = 296, in_= self.entryframe)
        self.entrybox.bind('<Any-KeyPress>', self.typepress)

         # Drop down menu
       
     # Handles Event for Key press
    def typepress(self):
         # Retrieves user input and cleans it
        user_input_raw = self.User_input.get()
        user_input_cleaned = user_input_raw.casefold()
         # Receives clean user input and sends to auto complete method
        self.input_received = user_input_cleaned
        self.auto_complete(self.input_received)
     
     # Handles auto complete logic
    def auto_complete(self, word_to_automate):
        word_to_automate = self.input_received
        self.trie.startswith(self, prefix = word_to_automate)
         # for suggesstions
        for suggestion in self.trie.startswith():
            self.optionsmenu.insert(tk.END, suggestion)
         # Handles list box if suggestion
        if suggestion:
            self.optionsmenu = tk.Listbox(self)
            self.optionsmenu.place(x= 600, y=229)
         # Handles suggestion if no suggestion
        elif not suggestion:
            self.optionsmenu.place_forget()
    
    def populatetrie(self, words):
        self.words()
         # Inserts words from wordsource to trie structure
        for words in self.words:
            self.trie.insertchar(words)
            


        
        
    
            






   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
     # Sets background for interface
    def add_background(self):
        self.bgimage = 'H:/Python/Textauto/Images/City.jpg'
        self.image = Image.open(self.bgimage)
        self.bg = ImageTk.PhotoImage(self.image)
        self.bglabel = tk.Label(self, image= self.bg)
        self.bglabel.place(x=0, y=0)
        


















 # Main Loop
if __name__ == "__main__":
    display = interface()
    display.mainloop()