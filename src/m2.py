"""
The  Python Capstone Project -- Talk to Me!

CSSE 120 - Introduction to Software Development (Robotics).
Winter term, 2013-2014.
Team members: Jeremiah Goist, Sarah Walker, Brooke Brown (all of them).

The primary author of this module is: Jeremiah Goist
"""
# DONE: Put the names of ALL team members in the above where indicated.
#       Put YOUR NAME in the above where indicated.

import m0
import m1
import m3
import m4

import tkinter
from tkinter import ttk

import time
import new_create
import math
import random

class Music():

    def __init__(self):

        self.Fmajor = [53, 55, 57, 58, 60, 62, 64, 65, 67, 69,
                       70, 72, 74, 76, 77, 79, 81, 82, 84, 86,
                       88, 89, 91, 93, 94, 96, 98, 100, 101, 128]

        self.Cmajor = [48, 50, 52, 53, 55, 57, 59, 60, 62, 64,
                       65, 67, 69, 71, 72, 74, 76, 77, 79, 81,
                       83, 84, 86, 88, 89, 91, 93, 95, 96, 98,
                       100, 101, 103, 105, 107, 108, 128]

        self.Gmajor = [43, 45, 47, 48, 50, 52, 54, 55, 57, 59,
                       60, 62, 64, 66, 67, 69, 71, 72, 74, 76,
                       78, 79, 81, 83, 84, 86, 88, 90, 91, 93,
                       95, 96, 98, 100, 102, 103, 128]

        self.Dmajor = [50, 52, 54, 55, 57, 59, 61, 62, 64,
                       66, 67, 69, 71, 73, 74, 76, 78, 79, 81,
                       83, 85, 86, 88, 90, 91, 93, 95, 97, 98,
                       100, 102, 103, 105, 107, 109, 110, 128]

        self.Amajor = [45, 47, 49, 50, 52, 54, 56, 57, 59, 61,
                       62, 64, 66, 68, 69, 71, 73, 74, 76, 78,
                       80, 81, 83, 85, 86, 88, 90, 92, 93, 95,
                       97, 98, 100, 102, 104, 105, 128]

        self.Emajor = [40, 42, 44, 45, 47, 49, 51, 52, 54, 56,
                       57, 59, 61, 63, 64, 66, 68, 69, 71, 73,
                       75, 76, 78, 80, 81, 83, 85, 87, 88, 90,
                       92, 93, 95, 97, 99, 100, 128]

        self.Bmajor = [47, 49, 51, 52, 54, 56, 58, 59, 61, 63,
                       64, 66, 68, 70, 71, 73, 75, 76, 78, 80,
                       82, 83, 85, 87, 88, 90, 92, 94, 95, 97,
                       99, 100, 102, 104, 106, 107, 128]

        self.GFlatmajor = [42, 44, 46, 47, 49, 51, 53, 54, 56, 58,
                           59, 61, 63, 65, 66, 68, 70, 71, 73, 75,
                           77, 78, 80, 82, 83, 85, 87, 89, 90, 92,
                           94, 95, 97, 99, 101, 102, 128]

        self.Dflatmajor = [37, 39, 41, 42, 44, 46, 48, 49, 51, 53,
                           54, 56, 58, 60, 61, 63, 65, 66, 68, 70,
                           72, 73, 75, 77, 78, 80, 82, 84, 85, 87,
                           89, 90, 92, 94, 96, 97, 128]

        self.Aflatmajor = [44, 46, 48, 49, 51, 53, 55, 56, 58, 60,
                           61, 63, 65, 67, 68, 70, 72, 73, 75, 77,
                           79, 80, 82, 84, 85, 87, 89, 91, 92, 94,
                           96, 97, 99, 101, 103, 104, 128]

        self.Eflatmajor = [39, 41, 43, 44, 46, 48, 50, 51, 53, 55,
                           56, 58, 60, 62, 63, 65, 67, 68, 70, 72,
                           74, 75, 77, 79, 80, 82, 84, 86, 87, 89,
                           91, 92, 94, 96, 98, 99, 128]

        self.Bflatmajor = [46, 48, 50, 51, 53, 55, 57, 58, 60, 62,
                           63, 65, 67, 69, 70, 72, 74, 75, 77, 79,
                           81, 82, 84, 86, 87, 89, 91, 93, 94, 96,
                           98, 99, 101, 103, 105, 106, 128]

        self.known_songs = {"Select a Song":[],
                            "Imperial March":[(55, 16), (0, 16), (55, 32), (55, 24),
                                             (51, 16), (58, 8), (55, 24), (51, 16),
                                             (58, 4), (55, 24), (0, 16), (62, 32),
                                             (62, 24), (62, 24), (63, 16), (58, 4),
                                             (54, 32), (51, 16), (58, 8), (55, 32),
                                             (0, 32), (67, 32), (55, 16), (55, 8),
                                             (67, 24), (66, 16), (65, 4), (64, 8),
                                             (63, 8), (64, 16), (0, 16), (56, 16),
                                             (61, 32), (60, 16), (59, 4), (58, 8),
                                             (57, 8), (58, 16), (0, 16), (51, 16),
                                             (54, 16), (0, 16), (51, 16), (54, 8),
                                             (58, 24), (55, 16), (58, 4), (62, 48),
                                             (0, 16), (67, 32), (55, 16), (55, 8), (67, 24),
                                             (66, 16), (65, 4), (64, 8), (63, 8), (64, 16),
                                             (0, 16), (56, 16), (61, 24), (60, 16), (59, 4),
                                             (58, 8), (57, 8), (58, 16), (0, 16), (51, 16),
                                             (54, 16), (0, 16), (51, 16), (58, 4), (55, 24),
                                             (51, 16), (58, 4), (55, 24), (0, 32)],
                            "Zelda Theme":[(70, 64), (0, 16), (65, 16), (65, 16), (70, 16),
                                           (68, 8), (66, 8), (68, 64), (70, 64), (0, 16),
                                           (66, 16), (66, 16), (70, 16), (69, 8), (67, 8),
                                           (69, 64), (53, 16), (53, 8), (46, 8), (53, 16),
                                           (53, 8), (46, 8), (53, 16), (53, 8), (46, 8),
                                           (53, 8), (46, 8), (53, 8), (46, 8), (53, 16),
                                           (53, 8), (46, 8), (53, 16), (53, 8), (46, 8),
                                           (53, 16), (53, 8), (46, 8), (53, 8), (46, 8),
                                           (53, 8), (46, 8), (70, 32), (65, 32), (0, 16),
                                           (70, 16), (70, 8), (72, 8), (74, 8), (87, 8),
                                           (89, 32), (58, 8), (60, 8), (62, 8), (63, 8),
                                           (65, 16), (39, 8), (32, 8), (39, 8), (32, 8),
                                           (39, 8), (32, 8), (70, 32), (65, 32), (0, 16),
                                           (70, 16), (70, 8), (72, 8), (74, 8), (87, 8),
                                           (89, 32), (58, 8), (60, 8), (62, 8), (63, 8),
                                           (65, 16), (48, 8), (41, 8), (48, 8), (41, 8),
                                           (48, 8), (41, 8), (70, 32), (65, 24), (70, 16),
                                           (70, 8), (72, 8), (74, 8), (75, 8), (77, 32),
                                           (70, 8), (72, 8), (74, 8), (75, 8), (77, 16),
                                           (77, 16), (77, 8), (78, 8), (80, 16), (82, 64),
                                           (0, 16), (82, 16), (82, 8), (80, 8), (78, 16),
                                           (80, 16), (78, 16), (77, 64)],
                            "Tetris":[(59, 16), (64, 16), (71, 16), (67, 8), (67, 8), (69, 8),
                                      (66, 16), (67, 16), (64, 8), (64, 8), (66, 8), (63, 16),
                                      (64, 16), (59, 8), (59, 8), (63, 8), (59, 16), (59, 16),
                                      (63, 8), (63, 8), (59, 8), (52, 16), (59, 16), (63, 16),
                                      (59, 16), (52, 16), (63, 16), (59, 16), (59, 16), (64, 16),
                                      (71, 16), (67, 8), (67, 8), (69, 8), (66, 16), (67, 16),
                                      (64, 8), (64, 8), (66, 8), (63, 16), (64, 16), (59, 8), (59, 8),
                                      (63, 8), (59, 16), (59, 16), (63, 8), (63, 8), (59, 8),
                                      (52, 16), (59, 16), (63, 16), (59, 16), (52, 16), (63, 16),
                                      (63, 16), (64, 96), (59, 32), (62, 16), (62, 8), (62, 8),
                                      (66, 16), (62, 16), (62, 16), (62, 8), (62, 8), (66, 16),
                                      (62, 16), (62, 96), (66, 32), (67, 16), (67, 8), (67, 8),
                                      (69, 16), (66, 16), (67, 16), (67, 8), (67, 8), (66, 16), (66, 16),
                                      (62, 96), (69, 32), (69, 16), (69, 8), (69, 8), (74, 16), (74, 16),
                                      (76, 16), (74, 16), (74, 16), (73, 16), (74, 16), (74, 8), (74, 8),
                                      (74, 8), (74, 16), (73, 16), (73, 8), (73, 8), (73, 8), (73, 16),
                                      (72, 16), (72, 8), (72, 8), (72, 8), (69, 16), (66, 16), (67, 16),
                                      (69, 16), (62, 16), (69, 16), (67, 16), (64, 16), (67, 32), (64, 8),
                                      (69, 8), (67, 16), (64, 16), (69, 16), (67, 16), (64, 16), (67, 32),
                                      (69, 8), (69, 8), (67, 16), (66, 16), (62, 128)]}

        self.list_of_keys = (self.Fmajor, self.Cmajor, self.Gmajor, self.Dmajor,
                             self.Amajor, self.Emajor, self.Bmajor, self.GFlatmajor,
                             self.Dflatmajor, self.Aflatmajor, self.Eflatmajor, self.Bflatmajor)

    def get_key(self, key_select):

        return self.list_of_keys[key_select]

def main():
    """
    Tests functions in this module.
    Intended to be used internally by the primary author of this module.
    """
    print('Testing functions in module m2:\n')

    root = tkinter.Tk()

    dc = m0.DataContainer()

    frame1 = basic_teleop_frame(root, dc)
    frame1.grid(row=1, column=0)

    root.mainloop()

def basic_teleop_frame(root, data_container):
    """
    Constructs and returns a Frame that contains this module's widgets.
    Also sets up callbacks for this module's widgets.
    """

    # Creates frame for buttons
    frame = ttk.Frame(root, padding=10, relief="raised")

    # Creates Time Spent Label
    label = ttk.Label(frame, text=str(data_container.Hours()[2]))
    label.grid(row=0, column=1)

    # Creates a button to move wallE forward
    forward = ttk.Button(frame, text="Move Forward")
    forward.grid(row=1, column=1)

    # Creates a button to move wallE backward
    backward = ttk.Button(frame, text="Move Backward")
    backward.grid(row=3, column=1)

    # Creates a button to rotate wallE left
    left = ttk.Button(frame, text="Rotate Left")
    left.grid(row=2, column=0)

    # Creates a button to rotate wallE right
    right = ttk.Button(frame, text="Rotate Right")
    right.grid(row=2, column=2)

    # Creates a button to stop wallE
    stop = ttk.Button(frame, text="Stop WallE")
    stop.grid(row=2, column=1)

    # Creates button to increase speed
    speed_up = ttk.Button(frame, text="Increase speed")
    speed_up.grid(row=3, column=0)

    # Creates button to decrease speed
    speed_down = ttk.Button(frame, text="Decrease speed")
    speed_down.grid(row=3, column=2)

    # Creates a button to increase angular speed
    speed_left = ttk.Button(frame, text="Increase angular speed")
    speed_left.grid(row=1, column=0)

    # Creates a button to decrease angular speed
    speed_right = ttk.Button(frame, text="Decrease angular speed")
    speed_right.grid(row=1, column=2)

    start_IR = ttk.Button(frame, text="Lead robot(s) w/ IR")
    start_IR.grid(row=4, column=0)

    follow_IR = ttk.Button(frame, text="Follow the Leader")
    follow_IR.grid(row=4, column=2)

    forward['command'] = lambda : move_forward(data_container, 0)
    backward['command'] = lambda : move_backward(data_container, 0)
    left['command'] = lambda: rotate_left(0, data_container)
    right['command'] = lambda: rotate_right(0, data_container)
    stop['command'] = lambda: stop_robot(data_container)

    speed_up['command'] = lambda: increase_speed(data_container)
    speed_down['command'] = lambda: decrease_speed(data_container)
    speed_left['command'] = lambda: increase_angle_per_second(data_container)
    speed_right[  'command'] = lambda: decrease_angle_per_second(data_container)

    start_IR['command'] = lambda: lead_IR_signal(data_container)
    follow_IR['command'] = lambda: follow_IR_signal(data_container, frame)

    return frame

def adv_auto_frame(root, data_container):

    frame = ttk.Frame(root, padding=10, relief='raised')

    # Creates Time Spent Label
    label = ttk.Label(frame, text=str(data_container.Hours()[5]))
    label.grid()

    distance_label = ttk.Label(frame, text='Enter a distance (cm)')
    distance_label.grid()
    entry_distance = ttk.Entry(frame, width=8)
    entry_distance.grid()

    direction_label = ttk.Label(frame, text='Enter angular speed (degrees/second)')
    direction_label.grid()
    entry_direction = ttk.Entry(frame, width=8)
    entry_direction.grid()

    speed_label = ttk.Label(frame, text='Enter a speed (cm/second)')
    speed_label.grid()
    entry_speed = ttk.Entry(frame, width=8)
    entry_speed.grid()

    move_button = ttk.Button(frame, text='Move Advanced Auto! (w/ time calculation)')
    move_button.grid()

    dist_move_button = ttk.Button(frame, text='Move Advanced Auto! (w/ distance sensor)')
    dist_move_button.grid()

    wait_move_button = ttk.Button(frame, text='Move Advanced Auto! (w/ create function)')
    wait_move_button.grid()

    arclength_move_button = ttk.Button(frame, text='Move ADV Auto! (Arclength)')
    arclength_move_button.grid()

    move_button['command'] = lambda: auto_move(data_container,
                                               entry_distance,
                                               entry_direction,
                                               entry_speed)

    dist_move_button['command'] = lambda: auto_move_sensor(data_container,
                                                           entry_distance,
                                                           entry_direction,
                                                           entry_speed)

    wait_move_button['command'] = lambda: auto_move_function(data_container,
                                                             entry_distance,
                                                             entry_direction,
                                                             entry_speed)

    arclength_move_button['command'] = lambda: auto_move_arclength(data_container,
                                                                   entry_distance,
                                                                   entry_direction,
                                                                   entry_speed)

    return frame

def basic_waypoint_frame(root, data_container):

    # Creates Frame
    frame = ttk.Frame(root, padding=10, relief="raised")

    # Creates Time Spent Label
    label = ttk.Label(frame, text=str(data_container.Hours()[11]))
    label.grid()

    # Creates X coord entry box
    x_label = ttk.Label(frame, text="Enter list of x-coordinates")
    x_label.grid()
    x_coordinate = ttk.Entry(frame, width=8)
    x_coordinate.grid()

    # Creates Y coord entry box
    y_label = ttk.Label(frame, text="Enter list of y-coordinates")
    y_label.grid()
    y_coordinate = ttk.Entry(frame, width=8)
    y_coordinate.grid()

    # Creates speed entry box
    speed_label = ttk.Label(frame, text="Enter a speed (cm/s)")
    speed_label.grid()
    entry_speed = ttk.Entry(frame, width=8)
    entry_speed.grid()

    # Creates angular speed entry box
    angle_speed_label = ttk.Label(frame, text="Enter an angular speed(degrees/s)")
    angle_speed_label.grid()
    entry_angular_speed = ttk.Entry(frame, width=8)
    entry_angular_speed.grid()

    # Creates two movement buttons
    move_short = ttk.Button(frame, text="Move shortest path to each point")
    move_short.grid()

    move_short['command'] = lambda: move_direct_path(data_container,
                                                     x_coordinate,
                                                     y_coordinate,
                                                     entry_speed,
                                                     entry_angular_speed)

    return frame

def move_forward(data_container, angle):
    data_container.robot.go(abs(data_container.speed), angle)

def move_backward(data_container, angle):
    data_container.robot.go(-abs(data_container.speed), angle)

def rotate_left(speed, data_container):
    data_container.robot.go(speed, abs(data_container.angle_per_second))

def rotate_right(speed, data_container):
    data_container.robot.go(speed, -abs(data_container.angle_per_second))

def increase_speed(data_container):
    data_container.speed += 5
    if data_container.speed < 0:
        data_container.speed = 0
    elif data_container.speed > 50:
        data_container.speed = 50
    print(data_container.speed)

def decrease_speed(data_container):
    data_container.speed -= 5
    if data_container.speed < 0:
        data_container.speed = 0
    elif data_container.speed > 50:
        data_container.speed = 50
    print(data_container.speed)

def increase_angle_per_second(data_container):
    data_container.angle_per_second += 10
    if data_container.angle_per_second < 0:
        data_container.angle_per_second = 0
    elif data_container.angle_per_second > 200:
        data_container.angle_per_second = 200
    print(data_container.angle_per_second)

def decrease_angle_per_second(data_container):
    data_container.angle_per_second -= 10
    if data_container.angle_per_second < 0:
        data_container.angle_per_second = 0
    elif data_container.angle_per_second > 200:
        data_container.angle_per_second = 200
    print(data_container.angle_per_second)

def stop_robot(data_container):
    data_container.robot.stop()

def auto_move(data_container, distance, direction, speed):
    data_container.distance = float(distance.get())
    data_container.angle_per_second = float(direction.get())
    data_container.speed = float(speed.get())

    data_container.robot.go(data_container.speed, data_container.angle_per_second)
    time.sleep(abs(data_container.distance / data_container.speed))
    data_container.robot.stop()

def auto_move_sensor(data_container, distance, direction, speed):
    data_container.distance = float(distance.get())
    data_container.angle_per_second = float(direction.get())
    data_container.speed = float(speed.get())

    data_container.robot.go(data_container.speed, data_container.angle_per_second)

    total_distance = 0
    while total_distance / 10 <= data_container.distance:
        total_distance += abs(data_container.robot.getSensor('DISTANCE'))

    data_container.robot.stop()

def auto_move_function(data_container, distance, direction, speed):
    data_container.distance = float(distance.get())
    data_container.angle_per_second = float(direction.get())
    data_container.speed = float(speed.get())

    data_container.robot.go(data_container.speed, data_container.angle_per_second)
    data_container.robot.waitDistance(data_container.distance)
    data_container.robot.stop()

def auto_move_arclength(data_container, distance, direction, speed):
    rotation_angle = float(direction.get()) - 90
    turn_to_direction(data_container, rotation_angle)

    arc_length = ((math.pi) * float(distance.get())) / 2
    data_container.robot.drive(int(speed.get()) * 10, float(distance.get()) * 5, turnDir='CCW')
    data_container.robot.waitDistance(arc_length)
    data_container.robot.stop()

def move_direct_path(data_container, x_coordinates, y_coordinates, speed, angular_speed):

    sequence_of_x = (x_coordinates.get())
    sequence_of_y = (y_coordinates.get())

    x_coords = sequence_of_x.split()
    y_coords = sequence_of_y.split()

    print(x_coords)
    print(y_coords)

    data_container.speed = float(speed.get())
    data_container.angle_per_second = float(angular_speed.get())

    dx = float(x_coords[0])
    dy = float(y_coords[0])

    rotation_angle = calculate_rotation(dx, dy, data_container)
    turn_to_direction(data_container, rotation_angle)

    travel_distance(dx, dy, data_container)

    time.sleep(.5)

    for k in range(1, len(x_coords)):

        dx = float(x_coords[k]) - float(x_coords[k - 1])
        dy = float(y_coords[k]) - float(y_coords[k - 1])

        rotation_angle = calculate_rotation(dx, dy, data_container)
        turn_to_direction(data_container, rotation_angle)

        travel_distance(dx, dy, data_container)

        time.sleep(.5)

    data_container.current_angle = 0

def calculate_rotation(dx, dy, data_container):

    if dx == 0:
        if dy > 0:
            goal_angle = 90
        elif dy < 0:
            goal_angle = 270
        else:
            goal_angle = data_container.current_angle
    else:
        goal_angle = math.degrees(math.atan2(dy, dx))

    delta_angle = goal_angle - data_container.current_angle

    if delta_angle > 180:
        delta_angle = delta_angle - 360

    return delta_angle

def turn_to_direction(data_container, rotation_angle):

    if rotation_angle > 0:
        data_container.robot.go(0, data_container.angle_per_second)
    elif rotation_angle < 0:
        data_container.robot.go(0, -data_container.angle_per_second)
    data_container.robot.waitAngle(rotation_angle)
    data_container.robot.stop()
    data_container.current_angle += rotation_angle

def travel_distance(dx, dy, data_container):

    distance = math.sqrt(dx ** 2 + dy ** 2)

    data_container.robot.go(data_container.speed, 0)
    data_container.robot.waitDistance(distance)
    data_container.robot.stop()

def random_composer(root, data_container):

    frame = ttk.Frame(root, padding=10, relief="raised")

    # Creates Time Spent Label
    label = ttk.Label(frame, text=str(data_container.Hours()[23]))
    label.grid()

    compose_button = ttk.Button(frame, text="Compose a Song")
    compose_button.grid()

    play_composed_button = ttk.Button(frame, text="Play Composed Song")
    play_composed_button.grid()

    song_options = ("Select a Song", "Imperial March", "Zelda Theme", "Tetris")
    selected_song = tkinter.StringVar()
    selected_song.set(song_options[0])
    song_selection = ttk.OptionMenu(frame, selected_song, *song_options)
    song_selection.grid()

    play_button = ttk.Button(frame, text="Play Song")
    play_button.grid()

    compose_button['command'] = lambda: compose_song(data_container)
    play_composed_button['command'] = lambda: play_composition(data_container, frame)
    play_button['command'] = lambda: play_song(data_container, frame, selected_song.get())

    return frame

def compose_song(data_container):

    sequence_of_notes = []

    # Note lengths from .25s to 2s
    possible_lengths = [16, 32, 48, 64, 80, 96, 112, 128]

    key_to_play = data_container.song_list.get_key(random.randrange(len(data_container.song_list.list_of_keys)))

    t = 0
    while True:
        # Forces songs to be at least 16 notes long
        if t < 16:
            length = possible_lengths[random.randrange(len(possible_lengths) - 1)]
            pitch = key_to_play[random.randrange(len(key_to_play) - 1)]
            note = (pitch, length)
            sequence_of_notes += [note]
            t += 1
        else:
            length = possible_lengths[random.randrange(len(possible_lengths))]
            pitch = key_to_play[random.randrange(len(key_to_play))]
            note = (pitch, length)
            sequence_of_notes += [note]
            t += 1
        # End composition on rest
        if pitch == 128:
            break

    print(sequence_of_notes)
    data_container.song = sequence_of_notes

def play_composition(data_container, frame):

    data_container.robot_check = False
    for k in range(len(data_container.song)):
        # Plays song note by note and flashes LEDs with each note
        data_container.robot.playNote(data_container.song[k][0], data_container.song[k][1])
        data_container.robot.setLEDs(random.randrange(255), random.randrange(255),
                                     random.randrange(1), random.randrange(1))
        while True:
            # Makes sure note is not playing before playing new note
            is_playing = data_container.robot.getSensor('SONG_PLAYING')
            frame.update()
            if not is_playing:
                break
            if data_container.robot_check:
                break
        if data_container.robot_check:
            break

def play_song(data_container, frame, known_song):

    data_container.robot_check = False
    song = data_container.song_list.known_songs.get(known_song)
    for k in range(len(song)):
        # Plays song note by note and flashes LEDs with each note
        data_container.robot.playNote(song[k][0], song[k][1])
        data_container.robot.setLEDs(random.randrange(255), random.randrange(255),
                                     random.randrange(1), random.randrange(1))
        while True:
            # Makes sure note is not playing before playing new note
            is_playing = data_container.robot.getSensor('SONG_PLAYING')
            frame.update()
            if not is_playing:
                break
            if data_container.robot_check:
                break
        if data_container.robot_check:
            break

def adv_IR_chat(root, data_container):

    frame = ttk.Frame(root, padding=10, relief="raised")

    # Creates Time Spent Label
    label = ttk.Label(frame, text=str(data_container.Hours()[14]))
    label.grid()

    IR_label = ttk.Label(frame, text="Enter a phrase to send")
    IR_label.grid()
    entry_IR = ttk.Entry(frame, width=8)
    entry_IR.grid()

    send_button = ttk.Button(frame, text="Send Encrypted Signal")
    send_button.grid()

    listen_button = ttk.Button(frame, text="Decrypt Heard Signal")
    listen_button.grid()

    send_button['command'] = lambda: send_signal(data_container, entry_IR, frame)
    listen_button['command'] = lambda: listen_for_signal(data_container, frame)

    return frame

def send_signal(data_container, entry_IR, frame):

    CAESAR_SLIDE = 3

    signal = entry_IR.get()
    new_signal = ''

    for k in range(len(signal)):

        new_signal += encrypt(signal[k], CAESAR_SLIDE)

    for j in range(len(new_signal)):
        m3.send_signal_handshake(frame, data_container.robot, ord(new_signal[j]))
        time.sleep(.5)

def listen_for_signal(data_container, frame):

    data_container.robot_check = False

    CAESAR_SLIDE = 3

    decrypted_signal = ''

    while True:
        if data_container.robot_check:
            break
        decrypted_signal += decrypt(m3.listen_for_signal_handshake(data_container, frame,
                                                                   255), CAESAR_SLIDE)
    foo = list(decrypted_signal)
    foo.remove(foo[len(foo) - 1])
    d_sig = ''
    for k in range(len(foo)):
        d_sig += foo[k]

    print(d_sig)

def encrypt(character, key):
    original = ord(character)
    encrypted = chr(original - key)

    return encrypted

def decrypt(character, key):
    original = character
    decrypted = chr(original + key)

    return decrypted

def lead_IR_signal(data_container):
    data_container.robot_check = False
    data_container.robot.startIR(23)
    if data_container.robot_check:
        data_container.robot.stopIR()

def follow_IR_signal(data_container, frame):
    while True:
        frame.update()
        if data_container.robot.getSensor('IR_BYTE') == 23:
            data_container.robot.go(20, 0)
        elif data_container.robot.getSensor('IR_BYTE') != 23:
            data_container.robot.go(0, 45)
        if data_container.robot_check:
            data_container.robot.stop()
            break
        time.sleep(.1)


#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------

if __name__ == '__main__':
    main()
