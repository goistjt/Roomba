"""
The  Python Capstone Project -- Talk to Me!

This module runs the ENTIRE program.
Your instructor will run THIS MODULE to test your code.

CSSE 120 - Introduction to Software Development (Robotics).
Winter term, 2013-2014.
Team members: Jeremiah Goist, Brooke Brown, Sarah Walker.

The primary author of this module is:  ENTIRE TEAM.
"""
# TODO: Put the names of ALL team members in the above where indicated.

import m1
import m2
import m3
import m4

import tkinter
from tkinter import ttk  # @UnusedImport
import time


class DataContainer(object):
    """ A container for the data shared across the application. """

    # Initializes inputs
    def __init__(self, robot=None, speed=10,
                 distance=10, angle=10, current_angle=0,
                 angle_per_second=30, seconds=1, darkness=0,
                 robot_check=False, song=[],
                 frame=None,
                 frame2=None,
                 frame_list=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 label_text='Text will display here',
                 label=None,
                 click_x=[],
                 click_y=[],
                 x_coordinates=[],
                 y_coordinates=[],
                 IR_heard=None):

        """ Initializes instance variables (fields). """
        # TODO: ADD     self.FOO = BLAH     HERE AS NEEDED.

        self.robot = robot
        self.speed = speed
        self.distance = distance
        self.angle = angle
        self.current_angle = current_angle
        self.angle_per_second = angle_per_second
        self.seconds = seconds
        self.darkness = darkness
        self.robot_check = robot_check
        self.song = song
        self.song_list = m2.Music()
        self.frame = frame
        self.frame2 = frame2
        self.frame_list = frame_list
        self.label_text = label_text
        self.label = label
        self.x_coordinates = x_coordinates
        self.y_coordinates = y_coordinates
        self.click_x = click_x
        self.click_y = click_y
        self.IR_heard = IR_heard

    def Hours(self):
        hours_file = open('Hours Per Person Per Sprint', 'r')
        hours = hours_file.read()
        hours_file.close()
        individual = hours.split('\n')
        return individual


def main():
    """ Runs the MAIN PROGRAM. """
    print('Integration Testing of the MAIN PROGRAM:\n')
    time.sleep(0.1)  # Allows print to complete before showing window

    # Creates root window
    root = tkinter.Tk()

    # Shortens data_container to dc
    dc = DataContainer()
    pid = m3.PID()

    label = ttk.Label(root, text=dc.label_text)
    label.grid(row=0, column=1, ipadx=100)

    # Creates connect frame from m1
    frame = m1.my_connect_frame(root, dc, label)
    frame.grid(row=0, column=0)

    # Creates frame number 1.5 used for drop down menu and buttons
    frame1 = ttk.Frame(root)
    frame1.grid(row=1, column=0)

    # Creates button
    button2 = ttk.Button(frame1, text='Action')
    button2.grid(row=1, column=0)

    # Creates drop down menu
    frame_options = ("Select a Frame",
                     'CREATE Autonomous',
                     'CREATE Wait for Event',
                     'CREATE Tele-Op',
                     'CREATE Line Follow',
                     'CREATE Waypoints',
                     'CREATE IR',
                     'CREATE Random Composer',
                     'CREATE Leap Motion',
                     "CREATE BIO's")

    selected_frame = tkinter.StringVar()
    selected_frame.set(frame_options[0])
    frame_selection = ttk.OptionMenu(frame1, selected_frame, *frame_options)
    frame_selection.grid(row=0, column=0)

    # Creates button second button
    button3 = ttk.Button(frame1, text='Action')
    button3.grid(row=1, column=1)

    # Creates second drop down menu
    frame1_options = ("Select a Frame",
                     'DESTROY Autonomous',
                     'DESTROY Wait for Event',
                     'DESTROY Tele-Op',
                     'DESTROY Line Follow',
                     'DESTROY Waypoints',
                     'DESTROY IR',
                     'DESTROY Random Composer',
                     'DESTROY Leap Motion',
                     "DESTROY BIO's")

    selected_frame1 = tkinter.StringVar()
    selected_frame1.set(frame1_options[0])
    frame1_selection = ttk.OptionMenu(frame1, selected_frame1, *frame1_options)
    frame1_selection.grid(row=0, column=1)

    # When button is pushed
    button2['command'] = lambda: select_frame(root, dc, selected_frame, pid, label)
    button3['command'] = lambda: delete_frame(root, dc, selected_frame1)

    # Runs main loop, allowing stuff to happen...
    root.mainloop()

def select_frame(root, dc, select, pid, label):

    # Gets value from drop down menu
    selected_frame = select.get()

    # Displays frame depending on value from menu
    if selected_frame == "CREATE BIO's":
        frame14 = m1.BIO_frame(root, dc)
        frame14.grid(row=9)
        dc.frame_list[13] = frame14
        return frame14

    if selected_frame == "CREATE Autonomous":
        frame1 = m1.basic_auto_frame(root, dc, label)
        frame1.grid(row=2, column=0)
        dc.frame_list[0] = frame1
        frame6 = m2.adv_auto_frame(root, dc)
        frame6.grid(row=2, column=1)
        dc.frame_list[5] = frame6
        return frame1, frame6

    elif selected_frame == "CREATE Wait for Event":
        frame2 = m1.advanced_frame(root, dc, label)
        frame2.grid(row=3, column=1)
        dc.frame_list[1] = frame2
        frame10 = m3.basic_auto_frame(root, dc)
        frame10.grid(row=3, column=0)
        dc.frame_list[9] = frame10
        return frame2, frame10

    elif selected_frame == "CREATE Line Follow":
        frame3 = m1.line_follow_frame(root, dc)
        frame3.grid(row=4, column=0)
        dc.frame_list[2] = frame3
        frame3point5 = m3.adv_line_following_frame(root, dc, pid, label)
        frame3point5.grid(row=4, column=1)
        dc.frame_list[12] = frame3point5
        return frame3, frame3point5

    elif selected_frame == "CREATE Tele-Op":
        frame5 = m2.basic_teleop_frame(root, dc)
        frame5.grid(row=5, column=0)
        dc.frame_list[4] = frame5
        frame11 = m3.adv_teleop_frame(root, dc)
        frame11.grid(row=5, column=1)
        dc.frame_list[10] = frame11
        return frame5, frame11,

    elif selected_frame == "CREATE Leap Motion":
        frame13 = m3.leap_frame(root, dc)
        frame13.grid(row=5, column=0)
        dc.frame_list[14] = frame13
        return frame13

    elif selected_frame == "CREATE Waypoints":
        frame7 = m2.basic_waypoint_frame(root, dc)
        frame7.grid(row=6, column=0)
        dc.frame_list[6] = frame7
        frame4 = m1.waypoints_frame(root, dc)
        frame4.grid(row=6, column=1)
        dc.frame_list[3] = frame4
        return frame7, frame4

    elif selected_frame == "CREATE Random Composer":
        frame8 = m2.random_composer(root, dc)
        frame8.grid(row=7, column=0)
        dc.frame_list[7] = frame8
        return frame8

    elif selected_frame == "CREATE IR":
        frame12 = m3.basic_chat_frame(root, dc)
        frame12.grid(row=8, column=0)
        dc.frame_list[11] = frame12
        frame9 = m2.adv_IR_chat(root, dc)
        frame9.grid(row=8, column=1)
        dc.frame_list[8] = frame9
        return frame12, frame9

def delete_frame(root, dc, select):

    # Gets value from second drop down menu
    selected_frame = select.get()

    # Destroys selected function depending on drop down menu
    if selected_frame == "DESTROY Wait for Event":
        dc.frame = dc.frame_list[1]
        dc.frame.destroy()
        dc.frame2 = dc.frame_list[9]
        dc.frame2.destroy()
        return dc.frame, dc.frame2

    elif selected_frame == "DESTROY Leap Motion":
        dc.frame = dc.frame_list[14]
        dc.frame.destroy()
        return dc.frame

    elif selected_frame == "DESTROY BIO's":
        dc.frame = dc.frame_list[13]
        dc.frame.destroy()
        return dc.frame

    elif selected_frame == "DESTROY Line Follow":
        dc.frame = dc.frame_list[2]
        dc.frame.destroy()
        dc.frame2 = dc.frame_list[12]
        dc.frame2.destroy()
        return dc.frame, dc.frame2

    elif selected_frame == "DESTROY Tele-Op":
        dc.frame = dc.frame_list[4]
        dc.frame.destroy()
        dc.frame2 = dc.frame_list[10]
        dc.frame2.destroy()
        return dc.frame, dc.frame2

    elif selected_frame == "DESTROY Autonomous":
        dc.frame = dc.frame_list[5]
        dc.frame.destroy()
        dc.frame2 = dc.frame_list[0]
        dc.frame2.destroy()
        return dc.frame, dc.frame2

    elif selected_frame == "DESTROY Waypoints":
        dc.frame = dc.frame_list[6]
        dc.frame.destroy()
        dc.frame2 = dc.frame_list[3]
        dc.frame2.destroy()
        return dc.frame, dc.frame2

    elif selected_frame == "DESTROY Random Composer":
        dc.frame = dc.frame_list[7]
        dc.frame.destroy()
        return dc.frame

    elif selected_frame == "DESTROY IR":
        dc.frame = dc.frame_list[8]
        dc.frame.destroy()
        dc.frame2 = dc.frame_list[11]
        dc.frame2.destroy()
        return dc.frame, dc.frame2

    # TODO: TEAM-PROGRAM this module so that it runs your entire
    #       practice program, incorporating parts from m1 .. m4.

#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()
