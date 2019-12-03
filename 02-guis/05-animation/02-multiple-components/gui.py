from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.great_ball_image = PhotoImage(file="/Users/seanypollard/Documents/Uni/Programming/com404/02-guis/05-animation/02-multiple-components/img/Great-Ball.gif")
        self.poke_ball_image = PhotoImage(file="/Users/seanypollard/Documents/Uni/Programming/com404/02-guis/05-animation/02-multiple-components/img/PokeBall.gif")
        self.ultra_ball_image = PhotoImage(file="/Users/seanypollard/Documents/Uni/Programming/com404/02-guis/05-animation/02-multiple-components/img/Ultra-Ball.gif")
        
        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.great_ball_x_pos = 225
        self.great_ball_y_pos = 1
        self.great_ball_x_change = -1
        self.great_ball_y_change = 1

        self.poke_ball_x_pos = 380
        self.poke_ball_y_pos = 230
        self.poke_ball_x_change = 1
        self.poke_ball_y_change = 1

        self.ultra_ball_x_pos = 140
        self.ultra_ball_y_pos = 360
        self.ultra_ball_x_change = 1
        self.ultra_ball_y_change = -1

        
        # add components
        self.add_poke_ball_image_label()
        self.add_great_ball_image_label()
        self.add_ultra_ball_image_label()
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):
        if self.poke_ball_x_pos == 0 or self.poke_ball_x_pos == 450:
            self.poke_ball_x_change *= -1
        if self.poke_ball_y_pos == 0 or self.poke_ball_y_pos == 450:
            self.poke_ball_y_change *= -1
        self.poke_ball_x_pos += self.poke_ball_x_change
        self.poke_ball_y_pos += self.poke_ball_y_change
        self.poke_ball_image_label.place(x=self.poke_ball_x_pos, 
                                        y=self.poke_ball_y_pos)

        if self.great_ball_x_pos == 0 or self.great_ball_x_pos == 450:
            self.great_ball_x_change *= -1
        if self.great_ball_y_pos == 0 or self.great_ball_y_pos == 450:
            self.great_ball_y_change *= -1
        self.great_ball_x_pos += self.great_ball_x_change
        self.great_ball_y_pos += self.great_ball_y_change
        self.great_ball_image_label.place(x=self.great_ball_x_pos, 
                                        y=self.great_ball_y_pos)

        if self.ultra_ball_x_pos == 0 or self.ultra_ball_x_pos == 450:
            self.ultra_ball_x_change *= -1
        if self.ultra_ball_y_pos == 0 or self.ultra_ball_y_pos == 450:
            self.ultra_ball_y_change *= -1
        self.ultra_ball_x_pos += self.ultra_ball_x_change
        self.ultra_ball_y_pos += self.ultra_ball_y_change
        self.ultra_ball_image_label.place(x=self.ultra_ball_x_pos, 
                                        y=self.ultra_ball_y_pos)


        self.after(10, self.tick)

    # the ball images
    def add_poke_ball_image_label(self):
        self.poke_ball_image_label = Label()
        self.poke_ball_image_label.place(x=self.poke_ball_x_pos,
                                            y=self.poke_ball_y_pos)
        self.poke_ball_image_label.configure(image=self.poke_ball_image)

    def add_great_ball_image_label(self):
        self.great_ball_image_label = Label()
        self.great_ball_image_label.place(x=self.great_ball_x_pos,
                                            y=self.great_ball_y_pos)
        self.great_ball_image_label.configure(image=self.great_ball_image)

    def add_ultra_ball_image_label(self):
        self.ultra_ball_image_label = Label()
        self.ultra_ball_image_label.place(x=self.ultra_ball_x_pos,
                                            y=self.ultra_ball_y_pos)
        self.ultra_ball_image_label.configure(image=self.ultra_ball_image)
     
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 