from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("PAssport Checker")
        
        # add components
        self.__add_heading_label()
        self.__add_q1_label()
        self.__add_q1_yes_checkbutton()
        self.__add_q1_no_checkbutton()
        self.__add_q2_label()
        self.__add_q2_yes_checkbutton()
        self.__add_q2_no_checkbutton()
        self.__add_q3_label()
        self.__add_q3_yes_checkbutton()
        self.__add_q3_no_checkbutton()
        self.__add_check_button()
        
    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(column=0,row=0,columnspan=4)

        self.heading_label.configure(text="Passport Checker",
                                        font="Arial 16")
        
    def __add_q1_label(self):
        self.q1_label = Label()
        self.q1_label.grid(column=0,row=1,sticky=W,columnspan=4)

        self.q1_label.configure(text="1. Photo matches face?")

    def __add_q1_yes_checkbutton(self):
        self.q1_yes_checkbutton = Checkbutton()
        self.q1_yes_checkbutton.grid(column=2,row=2)

        self.q1_yes_val = IntVar()
        self.q1_yes_checkbutton.configure(text="Yes",variable=self.q1_yes_val)

    def __add_q1_no_checkbutton(self):
        self.q1_no_checkbutton = Checkbutton()
        self.q1_no_checkbutton.grid(column=3,row=2)

        self.q1_no_val = IntVar()
        self.q1_no_checkbutton.configure(text="No",variable=self.q1_no_val)
    
    def __add_q2_label(self):
        self.q2_label = Label()
        self.q2_label.grid(column=0,row=3,sticky=W,columnspan=4)

        self.q2_label.configure(text="2. Passport has at least 6 months validity?")
    
    def __add_q2_yes_checkbutton(self):
        self.q2_yes_checkbutton = Checkbutton()
        self.q2_yes_checkbutton.grid(column=2,row=4)

        self.q2_yes_val = IntVar()
        self.q2_yes_checkbutton.configure(text="Yes",variable=self.q2_yes_val)

    def __add_q2_no_checkbutton(self):
        self.q2_no_checkbutton = Checkbutton()
        self.q2_no_checkbutton.grid(column=3,row=4)

        self.q2_no_val = IntVar()
        self.q2_no_checkbutton.configure(text="No",variable=self.q2_no_val) 

    def __add_q3_label(self):
        self.q3_label = Label()
        self.q3_label.grid(column=0,row=5,sticky=W,columnspan=4)

        self.q3_label.configure(text="3. Visa, if required, is valid?")

    def __add_q3_yes_checkbutton(self):
        self.q3_yes_checkbutton = Checkbutton()
        self.q3_yes_checkbutton.grid(column=2,row=6)

        self.q3_yes_val = IntVar()
        self.q3_yes_checkbutton.configure(text="Yes",variable=self.q3_yes_val)

    def __add_q3_no_checkbutton(self):
        self.q3_no_checkbutton = Checkbutton()
        self.q3_no_checkbutton.grid(column=3,row=6)

        self.q3_no_val = IntVar()
        self.q3_no_checkbutton.configure(text="No",variable=self.q3_no_val)

    def __add_check_button(self):
        self.check_button = Button()
        self.check_button.grid(column=0,row=7,columnspan=4)

        self.check_button.configure(text="Check")

        self.check_button.bind("<ButtonRelease-1>", self.__check_button_clicked)

    
    def __check_button_clicked(self, event):
        if self.q1_yes_val.get() == 1 and self.q2_yes_val.get() == 1 and self.q3_yes_val.get() == 1:
            messagebox.showinfo("Passed!","You have passed the passport checks!")
        else:
            messagebox.showerror("Failed!", "You have failed the passport checks!")