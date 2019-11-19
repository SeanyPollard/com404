from tkinter import *

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Song Maker")
        
        # add components
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_lyric_frame()
        self.__add_lyrics_entry()
        self.__add_submit_button()
        self.__add_display_label()
        self.__add_display_listbox()
        
    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(column=0,row=0)

        self.heading_label.configure(text="Song Maker",
                                        font="Arial 16")
        
    def __add_instruction_label(self):
        self.instruction_label = Label()
        self.instruction_label.grid(column=0,row=1,sticky=W)

        self.instruction_label.configure(text="Lyric to add:")

    def __add_lyric_frame(self):
        self.lyric_frame = Frame()
        self.lyric_frame.grid(column=0,row=2)
        
    def __add_lyrics_entry(self):
        self.lyrics_entry = Entry(self.lyric_frame)
        self.lyrics_entry.pack(side=LEFT)
        
    def __add_submit_button(self):
        self.submit_button = Button(self.lyric_frame)
        self.submit_button.pack(side=RIGHT)

        self.submit_button.configure(text="Add")

        self.submit_button.bind("<ButtonRelease-1>", self.__submit_button_clicked)

    def __add_display_label(self):
        self.display_label = Label()
        self.display_label.grid(column=0,row=3,sticky=W)

        self.display_label.configure(text="Lyrics:")

    def __add_display_listbox(self):
        self.display_listbox = Listbox()
        self.display_listbox.grid(column=0,row=4)

        self.display_listbox.configure(height=4)


    def __submit_button_clicked(self, event):
        self.display_listbox.insert(END, self.lyrics_entry.get())