from tkinter import *
from tkinter import messagebox

class Gui(Tk):

    # Window
    def __init__(self):
        super().__init__()

        # Resources
        self.santa_image = PhotoImage(file="/Users/seanypollard/Documents/Uni/Programming/com404/999-actual-tca/02-tca-ae2/santa.gif")

        # Attributes
        self.title("Letter to Santa")
        self.configure(background="#f66",
                        padx=15, pady=15,
                        width=400)
    
        # Components
        self.__add_global_frame()
        self.__add_heading_label()
        self.__add_name_label()
        self.__add_name_entry()
        self.__add_santa_image_label()
        self.__add_letter_text()
        self.__add_post_button()

    # Global Frame
    def __add_global_frame(self):
        self.global_frame = Frame()
        self.global_frame.pack()
        self.global_frame.configure(background="#f33",
                                    padx=5, pady=5)

    # Heading Label
    def __add_heading_label(self):
        self.heading_label = Label(self.global_frame)
        self.heading_label.grid(row=0, column=0, columnspan=2, padx=5)
        self.heading_label.configure(background="#f33", foreground="#fff",
                                        font="Arial 18", text="Write to Santa!")

    # Name Label
    def __add_name_label(self):
        self.name_label = Label(self.global_frame)
        self.name_label.grid(row=1, column=0, pady=5)
        self.name_label.configure(background="#f33", foreground="#fff",
                                    font="Arial 12", text="Your name:")

    # Name Entry
    def __add_name_entry(self):
        self.name_entry = Entry(self.global_frame)
        self.name_entry.grid(row=1, column=1)

    # Santa Image Label
    def __add_santa_image_label(self):
        self.santa_image_label = Label(self.global_frame)
        self.santa_image_label.grid(row=2, column=0)
        self.santa_image_label.configure(background="#f33",
                                            image=self.santa_image)
    
    # Letter Text
    def __add_letter_text(self):
        self.letter_text = Text(self.global_frame)
        self.letter_text.grid(row=2, column=1)
        self.letter_text.configure(width=30, height=5)

    # Post Button
    def __add_post_button(self):
        self.post_button = Button(self.global_frame)
        self.post_button.grid(row=3, column=0, columnspan=2)
        self.post_button.configure(background="#ff0",
                                    text="Post Letter")
        self.post_button.bind("<ButtonRelease-1>", self.__post_button_clicked)
    
    def __post_button_clicked(self, event):
        messagebox.showinfo("Sent!", "Your letter has been sent!")

gui = Gui()    
gui.mainloop() 