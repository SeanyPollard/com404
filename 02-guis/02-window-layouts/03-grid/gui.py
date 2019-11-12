from tkinter import *

class Gui(Tk):
    #initialise window
    def __init__(self):
        super().__init__()

        #set window attributes
        self.title("Newsletter")
        self.configure(bg="light grey")

        self.add_back_canvas()
        self.add_main_canvas()
        self.add_heading_label()
        self.add_text_label()
        self.add_entry_label()
        self.add_entry_box()
        self.add_sub_button()

    def add_back_canvas(self):
        self.back_canvas = Canvas()
        self.back_canvas.grid(column=0, row=0, columnspan=20, rowspan=15)

        self.back_canvas.configure(bg="light grey")
    
    def add_main_canvas(self):
        self.main_canvas = Canvas()
        self.main_canvas.grid(column=2, row=2, columnspan=16, rowspan=11)

        self.main_canvas.configure(bg="black")

    def add_heading_label(self):
        #create an object of the component stored in an attribute
        self.heading_label = Label()
        self.heading_label.grid(column=2, row=2, columnspan=16, rowspan=1)

        #set the attributes of the component using the attribute
        self.heading_label.configure(font="Arial 16",
                                        text="RECEIVE OUR NEWSLETTER",
                                        bg="#eee")
        #assign any event handlers to the component

    def add_text_label(self):
        self.text_label = Label()
        self.text_label.grid(column=2, row=4, columnspan=16, rowspan=1)

        self.text_label.configure(text="Please enter your email below to receive our newsletter.")

    def add_entry_label(self):
        self.text_label = Label()
        self.text_label.grid(column=2, row=6, columnspan=4, rowspan=1)

        self.text_label.configure(text="Entry:")

    def add_entry_box(self):
        self.entry_box = Entry()
        self.entry_box.grid(column=6, row=6, columnspan=10, rowspan=1)

        #self.entry_box.configure(width=40)

    def add_sub_button(self):
        self.sub_button = Button()
        self.sub_button.grid(column=2, row=8, columnspan=16, rowspan=1)

        self.sub_button.configure(text="Subscribe",
                                    bg="light pink")
    #handle events
    