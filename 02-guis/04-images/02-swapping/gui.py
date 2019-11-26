from tkinter import *

class Gui(Tk):
    
    def __init__(self):
        super().__init__()

        # load resources
        self.cactus_image = PhotoImage(file="/Users/seanypollard/Documents/com404/02-guis/04-images/02-swapping/img/cactus.gif")
        self.cactus_name_image = PhotoImage(file="/Users/seanypollard/Documents/com404/02-guis/04-images/02-swapping/img/cactus2.gif")
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.add_heading_label()
        self.add_cactus_image_label()
        self.add_flip_button()

    def add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0,column=0)
        self.heading_label.configure(font="Arial 20",
                                        text="Cactus Leaves")
        
    def add_cactus_image_label(self):
        self.cactus_image_label = Label()
        self.cactus_image_label.grid(row=1, column=0)
        self.cactus_image_label.configure(image=self.cactus_image,
                                                height=528,
                                                width=918)

    def add_flip_button(self):
        self.flip_button = Button()
        self.flip_button.grid(row=2, column=0)
        self.flip_button.configure(font="Arial 16",
                                    text="Flip!")

        self.flip_button.bind("<ButtonRelease-1>", self.__flip_button_left_clicked)
        self.flip_button.bind("<ButtonRelease-2>", self.__flip_button_right_clicked)

    def __flip_button_left_clicked(self, event):
        self.cactus_image_label.configure(image=self.cactus_image)

    def __flip_button_right_clicked(self, event):
        self.cactus_image_label.configure(image=self.cactus_name_image)
    
