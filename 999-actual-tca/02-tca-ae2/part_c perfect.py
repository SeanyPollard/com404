from tkinter import *
from tkinter import messagebox
import time

class Gui(Tk):

    # Window
    def __init__(self):
        super().__init__()

        # Resources
        self.santa_image = PhotoImage(file="/Users/seanypollard/Documents/Uni/Programming/com404/999-actual-tca/02-tca-ae2/santa.gif")
        self.unknown_image = PhotoImage(file="/Users/seanypollard/Documents/Uni/Programming/com404/999-actual-tca/02-tca-ae2/unknown.gif")
        self.reindeer_image = PhotoImage(file="/Users/seanypollard/Documents/Uni/Programming/com404/999-actual-tca/02-tca-ae2/reindeer.gif")
        self.snowman_image = PhotoImage(file="/Users/seanypollard/Documents/Uni/Programming/com404/999-actual-tca/02-tca-ae2/snowman.gif")
        self.elf_image = PhotoImage(file="/Users/seanypollard/Documents/Uni/Programming/com404/999-actual-tca/02-tca-ae2/elf.gif")

        # Variables
        self.animation = FALSE
        self.reverse = FALSE

        self.animation_x_pos = 20
        self.animation_y_pos = 20
        self.animation_x_change = 1
        self.animation_y_change = 0

        # Attributes
        self.title("Letter to Santa")
        self.configure(background="#f66",
                        padx=15, pady=15,
                        width=400)
        self.minsize(400,0)
        self.columnconfigure(0, weight=1)
    
        # Components
        self.__add_global_frame()
        self.__add_heading_label()
        self.__add_name_label()
        self.__add_name_entry()
        self.__add_santa_image_label()
        self.__add_letter_text()
        self.__add_sender_image_label()
        self.__add_post_button()
        self.__add_animation_button()
        self.__add_reverse_button()
        self.__add_animation_frame()
        self.__add_animation_image_label()

        # Timer
        self.tick()

    # Global Frame
    def __add_global_frame(self):
        self.global_frame = Frame()
        self.global_frame.grid(row=0, column=0, sticky=N+E+S+W)
        self.global_frame.configure(background="#f33",
                                    padx=5, pady=5)
        self.global_frame.columnconfigure(1, weight=1)

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
        self.name_entry.grid(row=1, column=1, sticky=E+W)
        self.name_entry.bind("<KeyRelease>", self.__name_entry_keyed)

    # Santa Image Label
    def __add_santa_image_label(self):
        self.santa_image_label = Label(self.global_frame)
        self.santa_image_label.grid(row=2, column=0)
        self.santa_image_label.configure(background="#f33",
                                            image=self.santa_image)
    
    # Letter Text
    def __add_letter_text(self):
        self.letter_text = Text(self.global_frame)
        self.letter_text.grid(row=2, column=1, sticky=E+W)
        self.letter_text.configure(width=30, height=5)

    # Sender Image Label
    def __add_sender_image_label(self):
        self.sender_image_label = Label(self.global_frame)
        self.sender_image_label.grid(row=3, column=0, columnspan=2, pady=(0,5))
        self.sender_image_label.configure(image=self.unknown_image)

    # Post Button
    def __add_post_button(self):
        self.post_button = Button(self.global_frame)
        self.post_button.grid(row=4, column=0, columnspan=2, sticky=E+W)
        self.post_button.configure(background="#ff0",
                                    text="Post Letter")
        self.post_button.bind("<ButtonRelease-1>", self.__post_button_clicked)

    # Animation Button
    def __add_animation_button(self):
        self.animation_button = Button(self.global_frame)
        self.animation_button.grid(row=5, column=0, columnspan=2, sticky=E+W)
        self.animation_button.configure(background="#0ff",
                                        text="Start Animation")
        self.animation_button.bind("<ButtonRelease-1>", self.__animation_button_clicked)

    # Reverse Button
    def __add_reverse_button(self):
        self.reverse_button = Button(self.global_frame)
        self.reverse_button.grid(row=6, column=0, columnspan=2, pady=(0,5), sticky=E+W)
        self.reverse_button.configure(background="#0ff",
                                        text="Reverse")
        self.reverse_button.bind("<ButtonRelease-1>", self.__reverse_button_clicked)

    def __add_animation_frame(self):
        self.animation_frame = Frame()
        self.animation_frame.grid(row=7, column=0, columnspan=2, sticky=N+S+E+W)
        self.animation_frame.configure(height=200)

    def __add_animation_image_label(self):
        self.animation_image_label = Label(self.animation_frame)
        self.animation_image_label.place(x=self.animation_x_pos,
                                            y=self.animation_y_pos)
        self.animation_image_label.configure(image=self.unknown_image)
    
    # Events
    def __post_button_clicked(self, event):
        if self.name_entry.get() == "":
            messagebox.showerror("Error!", "Please enter a name")
        elif self.name_entry.get() == "Snowy":
            messagebox.showinfo("Sent!", "Your letter has been sent! The snowman is falling!")
        elif self.name_entry.get() == "Elfie":
            messagebox.showinfo("Sent!", "Your letter has been sent! The elf is on its way!")
        elif self.name_entry.get() == "Rudolph":
            messagebox.showinfo("Sent!", "Your letter has been sent! The reindeer is shining its nose")
        else: 
            messagebox.showinfo("Sent!", "Your letter has been sent!")

    def __name_entry_keyed(self, event):
        if self.name_entry.get() == "Snowy":
            self.sender_image_label.configure(image=self.snowman_image)
            self.animation_image_label.configure(image=self.snowman_image)
        elif self.name_entry.get() == "Elfie":
            self.sender_image_label.configure(image=self.elf_image)
            self.animation_image_label.configure(image=self.elf_image)
        elif self.name_entry.get() == "Rudolph":
            self.sender_image_label.configure(image=self.reindeer_image)
            self.animation_image_label.configure(image=self.reindeer_image)
        else:
            self.sender_image_label.configure(image=self.unknown_image)
            self.animation_image_label.configure(image=self.unknown_image)

    def __animation_button_clicked(self, event):
        if self.animation == FALSE:
            self.animation = TRUE
            self.animation_button.configure(text="Stop Animation")
        else:
            self.animation = FALSE
            self.animation_button.configure(text="Start Animation")

    def __reverse_button_clicked(self, event):
        if self.reverse == FALSE:
            self.reverse = TRUE
        else:
            self.reverse = FALSE

    def tick(self):
        if self.animation == TRUE:
            if self.reverse == FALSE:
                self.animation_x_pos += self.animation_x_change
                self.animation_y_pos += self.animation_y_change
                self.animation_image_label.place(x=self.animation_x_pos,
                                                    y=self.animation_y_pos)

                if self.animation_x_pos == (self.animation_frame.winfo_width()-self.animation_image_label.winfo_width()-20) and self.animation_y_pos == 20:
                    self.animation_x_change = 0
                    self.animation_y_change = 1
                if self.animation_x_pos == (self.animation_frame.winfo_width()-self.animation_image_label.winfo_width()-20) and self.animation_y_pos == (self.animation_frame.winfo_height()-self.animation_image_label.winfo_height()-20):
                    self.animation_x_change = -1
                    self.animation_y_change = 0
                if self.animation_x_pos == 20 and self.animation_y_pos == (self.animation_frame.winfo_height()-self.animation_image_label.winfo_height()-20):
                    self.animation_x_change = 0
                    self.animation_y_change = -1
                if self.animation_x_pos == 20 and self.animation_y_pos ==20:
                    self.animation_x_change = 1
                    self.animation_y_change = 0
            else:
                self.animation_x_pos -= self.animation_x_change
                self.animation_y_pos -= self.animation_y_change
                self.animation_image_label.place(x=self.animation_x_pos,
                                                    y=self.animation_y_pos)

                if self.animation_x_pos == (self.animation_frame.winfo_width()-self.animation_image_label.winfo_width()-20) and self.animation_y_pos == 20:
                    self.animation_x_change = 1
                    self.animation_y_change = 0
                if self.animation_x_pos == (self.animation_frame.winfo_width()-self.animation_image_label.winfo_width()-20) and self.animation_y_pos == (self.animation_frame.winfo_height()-self.animation_image_label.winfo_height()-20):
                    self.animation_x_change = 0
                    self.animation_y_change = 1
                if self.animation_x_pos == 20 and self.animation_y_pos == (self.animation_frame.winfo_height()-self.animation_image_label.winfo_height()-20):
                    self.animation_x_change = -1
                    self.animation_y_change = 0
                if self.animation_x_pos == 20 and self.animation_y_pos ==20:
                    self.animation_x_change = 0
                    self.animation_y_change = -1

        self.after(10, self.tick)

gui = Gui()    
gui.mainloop() 