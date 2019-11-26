from tkinter import *

class Gui(Tk):
    
    def __init__(self):
        super().__init__()

        # load resources
        self.tick_icon = PhotoImage(file="/Users/seanypollard/Documents/com404/02-guis/04-images/04-hiding-and-showing/img/tick.gif")
        self.cross_icon = PhotoImage(file="/Users/seanypollard/Documents/com404/02-guis/04-images/04-hiding-and-showing/img/cross.gif")
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.add_heading_label()
        self.add_name_label()
        self.add_name_entry()
        self.add_name_check()
        self.add_passport_label()
        self.add_passport_entry()
        self.add_passport_check()
        self.add_nights_label()
        self.add_nights_entry()
        self.add_nights_check()
        self.add_check_in_button()

    def add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0,column=0,columnspan=5)
        self.heading_label.configure(font="Arial 20",
                                        text="Hotel Check In")
        
    def add_name_label(self):
        self.name_label = Label()
        self.name_label.grid(row=1,column=2,columnspan=2, sticky=W)
        self.name_label.configure(font="Arial 14",
                                    text="Name:")
    
