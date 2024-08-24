import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from trielogic import Trie
from sourcewords import wordsource
import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


# Class for interface
class interface(tk.Tk):
     # Initializes window
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Typemaster")
        self.geometry('1920x1080')
        logging.debug(f"Creating title:{self.title}, Windowsiz: {self.geometry}")
        self.trie = Trie()
        self.word_source = wordsource()
        self.add_background()
        self.addwidgets()
        self.populatetrie(self.word_source.listofwords())
        logging.debug(f"Creating background: {self.add_background} and widgets: {self.addwidgets}")
        

     # Adds widgets to GUI
    def addwidgets(self):
        
         # Frame for entry box
        self.entryframe = tk.Frame(self, bg='black', width= 300, height=29, relief= RAISED)
        self.entryframe.place(x= 600, y= 200)
        self.entryframe.winfo_width()
        self.entryframe.winfo_height()
        logging.debug(f"Creating entry frame with properties: {self.entryframe.winfo_width}, {self.entryframe.winfo_height}")
         # Records User input
        self.User_input= tk.StringVar()
       
         
         # Entry box 
        self.entrybox = tk.Entry(self.entryframe, textvariable= self.User_input, bg='white')
        self.entrybox.place(x = 2, y =2, height= 25, width = 296, in_= self.entryframe)
        self.entrybox.winfo_width()
        self.entrybox.winfo_height()
        self.entrybox.bind('<Any-KeyPress>', self.typepress)
        logging.debug(f"Creating entry box with properties: {self.entrybox.winfo_height}, {self.entrybox.winfo_width}")

         # Drop down menu
        
        
       
     # Handles Event for Key press
    def typepress(self, *args):
         # Retrieves user input and cleans it
        user_input_raw = self.User_input.get()
        user_input_cleaned = user_input_raw.casefold()
         # Receives clean user input and sends to auto complete method
        self.input_received = user_input_cleaned
        self.auto_complete(self.input_received)
     
     # Handles auto complete logic
    def auto_complete(self, word_to_automate):        
        word_to_automate = self.input_received
        suggestions = self.trie.startswith(word_to_automate)
        try: 
      
            if suggestions:
                self.optionsmenu = tk.Listbox(self)
                self.optionsmenu.delete(0, tk.END)
                self.optionsmenu.place(x=600, y=229)
                for suggestion in suggestions:
                    self.optionsmenu.insert(tk.END, suggestion)
                
            else:
                logging.debug(f"No suggestions for: {word_to_automate}")
            self.optionsmenu.place_forget()
        except TypeError as e:
            logging.debug(f"Type error: {e}")

    def populatetrie(self, words):
        self.word_source.listofwords()
         # Inserts words from wordsource to trie structure
        for words in self.word_source.listofwords():
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