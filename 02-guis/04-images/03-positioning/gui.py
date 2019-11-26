from tkinter import *

class Gui(Tk):
    
    def __init__(self):
        super().__init__()

        # load resources
        self.road_map_image = PhotoImage(file="/Users/seanypollard/Documents/com404/02-guis/04-images/03-positioning/img/road_map.gif")
        self.bus_image = PhotoImage(file="/Users/seanypollard/Documents/com404/02-guis/04-images/03-positioning/img/bus.gif")
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.add_heading_label()
        self.add_driving_frame()
        self.add_road_map_image_label()
        self.add_bus_image_label()

    def add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0,column=0)
        self.heading_label.configure(font="Arial 20",
                                        text="Bus Journey")
        
    def add_driving_frame(self):
        self.driving_frame = Frame()
        self.driving_frame.grid(row=1, column=0)
        self.driving_frame.configure(width=500, height=293)
    
    def add_road_map_image_label(self):
        self.road_map_image_label = Label(self.driving_frame)
        self.road_map_image_label.place(x=0, y=0)
        self.road_map_image_label.configure(image=self.road_map_image)

        self.road_map_image_label.bind("<B1-Motion>", self.__clicky_move)

    def add_bus_image_label(self):
        self.bus_image_label = Label(self.driving_frame)
        self.bus_image_label.place(x=10, y=10)
        self.bus_image_label.configure(image=self.bus_image)

    def __clicky_move(self, event):
        self.bus_image_label.place(x=event.x, y=event.y)
    
