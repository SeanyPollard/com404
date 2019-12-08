from tkinter import *

class Gui(Tk):

    # Window
    def __init__(self):
        super().__init__()

        # Window attributes
        self.title("Newsletter")
        self.configure(background="#eee",
                        padx=10, pady=10)

        # Add components
        self.__add_main_frame()
        self.__add_heading_label()
        self.__add_instructional_label()
        self.__add_email_label()
        self.__add_email_entry()
        # self.__add_subscribe_button()

    # Components
    def __add_main_frame(self):
        self.main_frame = Frame()
        self.main_frame.pack()

    def __add_heading_label(self):
        self.heading_label = Label(self.main_frame)
        self.heading_label.grid(column=0, row=0, columnspan=3)
        self.heading_label.configure(text="RECEIVE OUR NEWSLETTER",
                                        font="Arial 14",
                                        pady=10)
                        
    def __add_instructional_label(self):
        self.instructional_label = Label(self.main_frame)
        self.instructional_label.grid(column=0, row=1, columnspan=3, sticky=W)
        self.instructional_label.configure(text="Please enter your email below to receive our newsletter.",
                                            padx=10, pady=10)

    def __add_email_label(self):
        self.email_label = Label(self.main_frame)
        self.email_label.grid(column=0, row=2)
        self.email_label.configure(text="Email:",
                                    padx=10)

    def __add_email_entry(self):
        self.email_entry = Entry(self.main_frame)
        self.email_entry.grid(column=1, row=2)
        self.email_entry.configure(borderwidth=2,
                                    foreground="#f00",
                                    width=30)
    
gui = Gui()    
gui.mainloop() 





