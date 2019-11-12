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

        self.add_canvas()
        self.add_heading_label()
        self.add_text_label()
        self.add_entry_label()
        self.add_entry_box()
        self.add_sub_button()

    def add_canvas(self):
        self.main_canvas = Canvas()
        self.main_canvas.place(x=20, y=20)

        self.main_canvas.configure(height=160,
                                    width=360)

    def add_heading_label(self):
        #create an object of the component stored in an attribute
        self.heading_label = Label()
        self.heading_label.place(x=30, y=30)

        #set the attributes of the component using the attribute
        self.heading_label.configure(font="Arial 16",
                                        text="RECEIVE OUR NEWSLETTER",
                                        width=28,
                                        bg="#eee")
        #assign any event handlers to the component

    def add_text_label(self):
        self.text_label = Label()
        self.text_label.place(x=50,y=80)

        self.text_label.configure(text="Please enter your email below to receive our newsletter.")

    def add_entry_label(self):
        self.text_label = Label()
        self.text_label.place(x=50,y=120)

        self.text_label.configure(text="Entry:")

    def add_entry_box(self):
        self.entry_box = Entry()
        self.entry_box.place(x=100,y=120)

        self.entry_box.configure(width=40)

    def add_sub_button(self):
        self.sub_button = Button()
        self.sub_button.place(x=50, y=150)

        self.sub_button.configure(width=40,
                                    text="Subscribe",
                                    bg="light pink")
    #handle events
    