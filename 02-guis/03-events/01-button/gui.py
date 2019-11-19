from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Tickets")
        
        # add components
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_tickets_entry()
        self.__add_buy_button()
        
    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(column=0,row=0)

        self.heading_label.configure(text="Entrance Ticket",
                                        font="Arial 16")
        
    def __add_instruction_label(self):
        self.instruction_label = Label()
        self.instruction_label.grid(column=0,row=1,sticky=W)

        self.instruction_label.configure(text="How many tickets are needed?")
        
    def __add_tickets_entry(self):
        self.tickets_entry = Entry()
        self.tickets_entry.grid(column=0,row=2)
        
    def __add_buy_button(self):
        self.buy_button = Button()
        self.buy_button.grid(column=0,row=3)

        self.buy_button.configure(text="Buy")

        self.buy_button.bind("<ButtonRelease-1>", self.__buy_button_clicked)

    
    def __buy_button_clicked(self, event):
        purchased_tickets = int(self.tickets_entry.get())
        if purchased_tickets == 1:
            messagebox.showinfo("Purchased!", "You have purchased 1 ticket!")
        elif purchased_tickets > 1:
            messagebox.showinfo("Purchased!", "You have purchased " + str(purchased_tickets) + " tickets!")
        else:
            messagebox.showinfo("Error!", "You have entered an invalid number of tickets!")