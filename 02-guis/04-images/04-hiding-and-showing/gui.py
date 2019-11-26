from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    
    def __init__(self):
        super().__init__()

        # load resources
        self.tick_icon = PhotoImage(file="/Users/seanypollard/Documents/Uni/Programming/com404/02-guis/04-images/04-hiding-and-showing/img/tick.gif")
        self.cross_icon = PhotoImage(file="/Users/seanypollard/Documents/Uni/Programming/com404/02-guis/04-images/04-hiding-and-showing/img/cross.gif")
        
        # set window attributes
        self.title("Gui")
        
        # set vars
        self.name_bool = FALSE
        self.passport_bool = FALSE
        self.nights_bool = FALSE

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

    # window components
    def add_heading_label(self):
        # create
        self.heading_label = Label()
        # position
        self.heading_label.grid(row=0,column=0,columnspan=5)
        # customise
        self.heading_label.configure(font="Arial 20",
                                        text="Hotel Check In")
        
    # name components
    def add_name_label(self):
        # create
        self.name_label = Label()
        # position
        self.name_label.grid(row=1,column=0,columnspan=2, sticky=W)
        # customise
        self.name_label.configure(font="Arial 14",
                                    text="Name:")
    
    def add_name_entry(self):
        # create
        self.name_entry = Entry()
        # position
        self.name_entry.grid(row=1,column=2,columnspan=2)
        # customise
        self.name_entry.configure(width=30)
        # methods
        self.name_entry.bind("<FocusOut>", self.__name_entry_focus_out)

    def add_name_check(self):
        # create
        self.name_check = Label()
        # position
        self.name_check.grid(row=1, column=4)
        # customise
        self.name_check.configure(image=self.cross_icon,
                                    width=50,
                                    height=50)

    # passport components
    def add_passport_label(self):
        # create
        self.passport_label = Label()
        # position
        self.passport_label.grid(row=2,column=0,columnspan=2, sticky=W)
        # customise
        self.passport_label.configure(font="Arial 14",
                                    text="Passport Number:")
    
    def add_passport_entry(self):
        # create
        self.passport_entry = Entry()
        # position
        self.passport_entry.grid(row=2,column=2,columnspan=2)
        # customise
        self.passport_entry.configure(width=30)
        # methods
        self.passport_entry.bind("<FocusOut>", self.__passport_entry_focus_out)

    def add_passport_check(self):
        # create
        self.passport_check = Label()
        # position
        self.passport_check.grid(row=2, column=4)
        # customise
        self.passport_check.configure(image=self.cross_icon,
                                        width=50,
                                        height=50)

    # nights components
    def add_nights_label(self):
        # create
        self.nights_label = Label()
        # position
        self.nights_label.grid(row=3,column=0,columnspan=2, sticky=W)
        # customise
        self.nights_label.configure(font="Arial 14",
                                    text="No. of Nights:")
    
    def add_nights_entry(self):
        # create
        self.nights_entry = Entry()
        # position
        self.nights_entry.grid(row=3,column=2,columnspan=2)
        # customise
        self.nights_entry.configure(width=30)
        # methods
        self.nights_entry.bind("<FocusOut>", self.__nights_entry_focus_out)

    def add_nights_check(self):
        # create
        self.nights_check = Label()
        # position
        self.nights_check.grid(row=3, column=4)
        # customise
        self.nights_check.configure(image=self.cross_icon,
                                    width=50,
                                    height=50)   

    def add_check_in_button(self):
        # create
        self.check_in_button = Button()
        # position
        self.check_in_button.grid(row=4, column=0, columnspan=5)
        # customise
        self.check_in_button.configure(text="Check In")
        # methods
        self.check_in_button.bind("<ButtonRelease-1>", self.__check_in_button_clicked)

    def __name_entry_focus_out(self, event):
        if self.name_entry.get() != "":
            self.name_bool = TRUE
            self.name_check.configure(image=self.tick_icon)
        else:
            self.name_bool = FALSE
            self.name_check.configure(image=self.cross_icon)
    
    def __passport_entry_focus_out(self, event):
        if len(self.passport_entry.get()) == 9:
            self.passport_bool = TRUE
            self.passport_check.configure(image=self.tick_icon)
        else:
            self.passport_bool = FALSE
            self.passport_check.configure(image=self.cross_icon)

    def __nights_entry_focus_out(self, event):
        if int(self.nights_entry.get()) > 0 or int(self.nights_entry.get()) < 365:
            self.nights_bool = TRUE
            self.nights_check.configure(image=self.tick_icon)
        else:
            self.nights_bool = FALSE
            self.nights_check.configure(image=self.cross_icon)

    def __check_in_button_clicked(self, event):
        error_desc = ""
        if self.name_bool and self.passport_bool and self.nights_bool:
            messagebox.showinfo("Passed!", "You have passed the check!")
        else:
            if not self.name_bool:
                error_desc += "Name cannot be blank\n"
            if not self.passport_bool:
                error_desc += "Passport number must be 9 digits\n"
            if not self.nights_bool:
                error_desc += "Numbers of nights must be greater than 0 and less than 365"
            messagebox.showerror("Failed!", error_desc)



