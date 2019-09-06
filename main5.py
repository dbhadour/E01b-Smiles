#!/usr/bin/env python3

import utils, open_color, arcade

utils.check_version((3,7))

SCREEN_WIDTH = 800 # we are initializing variables from lines 7 through 9
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Smiley Face Example"

class Faces(arcade.Window):       # making a class here
    """ Our custom Window Class"""

    def __init__(self):        #defining a function here where self is a keyword which would bind the attributes with the given arguments 
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Show the mouse cursor
        self.set_mouse_visible(True) #this means we are alllowing the mouse to be visible

        self.x = SCREEN_WIDTH / 2 # this would mean that the smiley would at the middle of the screen by default
        self.y = SCREEN_HEIGHT / 2

        arcade.set_background_color(open_color.white)

    def on_draw(self):    # this is another function which actually draws the smiley
        """ Draw the face """
        arcade.start_render()
        face_x,face_y = (self.x,self.y)  # the use of self here indicates that the smiley would go wherever the mouse would go
        smile_x,smile_y = (face_x + 0,face_y - 10) # these are the coordinates of smiley and all its parts
        eye1_x,eye1_y = (face_x - 30,face_y + 20) 
        eye2_x,eye2_y = (face_x + 30,face_y + 20)
        catch1_x,catch1_y = (face_x - 25,face_y + 25) 
        catch2_x,catch2_y = (face_x + 35,face_y + 25) 

        arcade.draw_circle_filled(face_x, face_y, 100, open_color.yellow_3)  #lines 37-43 draws the smiiley also giving its parts specific colors to make it look like a smiley
        arcade.draw_circle_outline(face_x, face_y, 100, open_color.black,4)
        arcade.draw_ellipse_filled(eye1_x,eye1_y,15,25,open_color.black)
        arcade.draw_ellipse_filled(eye2_x,eye2_y,15,25,open_color.black)
        arcade.draw_circle_filled(catch1_x,catch1_y,3,open_color.gray_2)
        arcade.draw_circle_filled(catch2_x,catch2_y,3,open_color.gray_2)
        arcade.draw_arc_outline(smile_x,smile_y,60,50,open_color.black,190,350,4)


    def on_mouse_motion(self, x, y, dx, dy): # helps sets x and y ( of smiley's ) to the x and y value of the mouse so that the smiley goes whereever the mouse goes
        """ Handle Mouse Motion """
        self.x = x
        self.y = y



window = Faces()
arcade.run()