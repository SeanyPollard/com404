from tkinter import *

class Gui(Tk):
    #initialise window
    def __init__(self):
        super().__init__()

        #set window attributes
        self.title("Newsletter")
        self.configure(bg="light grey",
                        height=200,
                        width=400)

        self.add_main_frame()
        self.add_heading_label()
        self.add_text_label()
        self.add_email_frame()
        self.add_entry_label()
        self.add_entry_box()
        self.add_sub_button()

    def add_main_frame(self):
        self.main_frame = Frame()
        self.main_frame.pack()

        self.main_frame.configure(bg="light grey")
        
    def add_heading_label(self):
        #create an object of the component stored in an attribute
        self.heading_label = Label(self.main_frame)
        self.heading_label.pack()

        #set the attributes of the component using the attribute
        self.heading_label.configure(font="Arial 16",
                                        text="RECEIVE OUR NEWSLETTER",
                                        width=28,
                                        bg="#eee")
        #assign any event handlers to the component

    def add_text_label(self):
        self.text_label = Label(self.main_frame)
        self.text_label.pack()

        self.text_label.configure(text="Please enter your email below to receive our newsletter.")

    def add_email_frame(self):
        self.email_frame = Frame(self.main_frame)
        self.email_frame.pack()

    def add_entry_label(self):
        self.text_label = Label(self.email_frame)
        self.text_label.pack(side=LEFT)

        self.text_label.configure(text="Entry:")

    def add_entry_box(self):
        self.entry_box = Entry(self.email_frame)
        self.entry_box.pack(side=RIGHT)

        self.entry_box.configure(width=40)

    def add_sub_button(self):
        self.sub_button = Button(self.main_frame)
        self.sub_button.pack()

        self.sub_button.configure(width=40,
                                    text="Subscribe",
                                    bg="light pink")
    #handle events
    