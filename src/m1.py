"""
The  Python Capstone Project -- Talk to Me!

CSSE 120 - Introduction to Software Development (Robotics).
Winter term, 2013-2014.
Team members: Jeremiah Goist, Brooke Brown and Sarah Walker.

The primary author of this module is: Sarah Walker
"""
# Done: Put the names of ALL team members in the above where indicated.
#       Put YOUR NAME in the above where indicated.


# ALL the imports
import m0
import m2
import m3
import tkinter
from tkinter import ttk
import new_create
import time
import math


def main():
    """
    Tests functions in this module.
    Intended to be used internally by the primary author of this module.
    """
    # Imports data container from m0
    dc = m0.DataContainer()

    # Creates window
    root = tkinter.Tk()

    # Creates frame for printing
    frame0 = ttk.Frame(root)
    frame0.grid(row=0, column=2)

    # Creates label to print on
    label = ttk.Label(frame0, text=dc.label_text)
    label.grid(ipadx=100, ipady=50)

    # Creates frame number 1
    frame = my_connect_frame(root, dc, label)
    frame.grid(row=0)

    # Creates frame number 1.5
    frame1 = ttk.Frame(root)
    frame1.grid(row=1)

    # Creates button
    button2 = ttk.Button(frame1, text='Action')
    button2.grid(row=1, column=0)

    # Creates drop down menu
    frame_options = ("Select a Frame", 'CREATE Basic Autonomous', 'CREATE Advanced IR', 'CREATE Line Follow', 'CREATE Waypoints', "CREATE BIO's")
    selected_frame = tkinter.StringVar()
    selected_frame.set(frame_options[0])
    frame_selection = ttk.OptionMenu(frame1, selected_frame, *frame_options)
    frame_selection.grid(row=0, column=0)

    # Creates button
    button3 = ttk.Button(frame1, text='Action')
    button3.grid(row=1, column=1)

    # Creates second drop down menu
    frame1_options = ("Select a Frame", 'DESTROY Basic Autonomous', 'DESTROY Advanced IR', 'DESTROY Line Follow', 'DESTROY Waypoints', "DESTROY BIO's")
    selected_frame1 = tkinter.StringVar()
    selected_frame1.set(frame1_options[0])
    frame1_selection = ttk.OptionMenu(frame1, selected_frame1, *frame1_options)
    frame1_selection.grid(row=0, column=1)

    # When buttons are pushed
    button2['command'] = lambda: select_frame(root, dc, selected_frame, label)
    button3['command'] = lambda: delete_frame(root, dc, selected_frame1)

    # Runs main loop
    root.mainloop()

def select_frame(root, dc, select, label):

    # Gets value from drop down menu
    selected_frame = select.get()

    if selected_frame == "CREATE BIO's":
        # Creates frame number 2
        frame9 = BIO_frame(root, dc)
        frame9.grid(row=0, column=1)
        dc.frame_list[5] = frame9
        return frame9

    # Depending on input from drop down menu, displays selected frame
    if selected_frame == 'CREATE Basic Autonomous':
        # Creates frame number 2
        frame2 = basic_auto_frame(root, dc, label)
        frame2.grid(row=0, column=1)
        dc.frame_list[0] = frame2
        return frame2

    if selected_frame == 'CREATE Advanced IR':
        # Creates frame number 3
        frame3 = advanced_frame(root, dc, label)
        frame3.grid(row=0, column=2)
        dc.frame_list[1] = frame3
        return frame3

    if selected_frame == 'CREATE Line Follow':
        # Creates frame number 4
        frame4 = line_follow_frame(root, dc)
        frame4.grid(row=1, column=1)
        dc.frame_list[2] = frame4
        return frame4

    if selected_frame == 'CREATE Waypoints':
        # Creates frame number 5
        frame5 = waypoints_frame(root, dc)
        frame5.grid(row=1, column=2)
        dc.frame_list[3] = frame5
        return frame5

def delete_frame(root, dc, select):

    # Gets value form drop down box
    selected_frame = select.get()

    # Destroys selected frame from drop down box
    if selected_frame == 'DESTROY Basic Autonomous':
        dc.frame = dc.frame_list[0]
        dc.frame.destroy()
        return dc.frame

    if selected_frame == "DETROY BIO's":
        dc.frame = dc.frame_list[5]
        dc.frame.destroy()
        return dc.frame

    if selected_frame == 'DESTROY Advanced IR':
        dc.frame = dc.frame_list[1]
        dc.frame.destroy()
        return dc.frame

    if selected_frame == 'DESTROY Line Follow':
        dc.frame = dc.frame_list[2]
        dc.frame.destroy()
        return dc.frame

    if selected_frame == 'DESTROY Waypoints':
        dc.frame = dc.frame_list[3]
        dc.frame.destroy()
        return dc.frame

def BIO_frame(root, dc):

    frame = ttk.Frame(root, padding=10, relief='raised')

    # creates label for hours
    label = ttk.Label(frame, text=str(dc.Hours()[21]))
    label.grid()

    Sarah_button = ttk.Button(frame, text="Display Sarah's Bio")
    Sarah_button.grid()

    Sarah_button['command'] = lambda: diplay_BIO(dc, 'Sarah')

    Jeremiah_button = ttk.Button(frame, text="Display Jeremiah's Bio")
    Jeremiah_button.grid()

    Jeremiah_button['command'] = lambda: diplay_BIO(dc, 'Jeremiah')

    WIW_button = ttk.Button(frame, text="Display Robot's Bio")
    WIW_button.grid()

    WIW_button['command'] = lambda: diplay_BIO(dc, 'WIW')

    Brooke_button = ttk.Button(frame, text="Display Brooke's Bio")
    Brooke_button.grid()

    Brooke_button['command'] = lambda: diplay_BIO(dc, 'Brooke')

    return frame

def diplay_BIO(dc, Name):

    root = tkinter.Tk()

    frame = ttk.Frame(root)
    frame.grid()

    if Name == 'Sarah':

        f = open('Sarah', 'r')
        BIO = f.read()
        f.close()

    elif Name == 'Jeremiah':

        f = open('Jeremiah', 'r')
        BIO = f.read()
        f.close()

    elif Name == 'WIW':

        f = open('WIW', 'r')
        BIO = f.read()
        f.close()

    else:

        f = open('Brooke', 'r')
        BIO = f.read()
        f.close()

    label = ttk.Label(frame, text=BIO)
    label.grid()

    button = ttk.Button(frame, text='Close Window')
    button.grid()

    button['command'] = lambda: close_window(root)

def my_connect_frame(root, data_container, label):
    """
    Constructs and returns a Frame that contains this module's widgets.
    Also sets up callbacks for this module's widgets.
    """

    # Creates frame
    frame = ttk.Frame(root, padding=10, relief='raised')

    # Creates connect and disconnect buttons
    connect_button = ttk.Button(frame, text='Connect It')
    connect_button.grid()
    disconnect_button = ttk.Button(frame, text='Disconnect It')
    disconnect_button.grid()

    # Choose your port
    port_label = ttk.Label(frame, text="Enter a port")
    port_label.grid()
    entry_port = ttk.Entry(frame, width=8)
    entry_port.grid()

    # Creates stop button
    stop_button = ttk.Button(frame, text="STOP WallE (and stuff)!")
    stop_button.grid()

    # When you push button, calls function
    connect_button['command'] = lambda: actual_connect(data_container, entry_port, label)
    disconnect_button['command'] = lambda: disconnect_robot(data_container, label)

    # Stops robot when pushed
    stop_button['command'] = lambda: stop_robot(data_container)

    return frame

def basic_auto_frame(root, data_container, label):

    # Creates frame
    frame = ttk.Frame(root, padding=10, relief="raised")

    # Creates Time Spent Label
    label = ttk.Label(frame, text=str(data_container.Hours()[4]))
    label.grid()

    # Distance entry box
    distance_label = ttk.Label(frame, text="Enter a distance")
    distance_label.grid()
    entry_distance = ttk.Entry(frame, width=8)
    entry_distance.grid()

    # Direction entry box
    angle_label = ttk.Label(frame, text="Enter a direction in degrees")
    angle_label.grid()
    entry_angle = ttk.Entry(frame, width=8)
    entry_angle.grid()

    # Angular speed entry box
    angle_speed_label = ttk.Label(frame, text="Enter a rotation speed (Degrees/second)")
    angle_speed_label.grid()
    entry_angle_speed = ttk.Entry(frame, width=8)
    entry_angle_speed.grid()

    # Speed entry box
    speed_label = ttk.Label(frame, text="Enter a speed")
    speed_label.grid()
    entry_speed = ttk.Entry(frame, width=8)
    entry_speed.grid()

    # Auto move button
    basic_auto_move = ttk.Button(frame, text="Move autonomously (basic)")
    basic_auto_move.grid()

    # Moves when pushed
    basic_auto_move['command'] = lambda: basic_move_autonomous(data_container,
                                                               entry_distance,
                                                               entry_angle,
                                                               entry_angle_speed,
                                                               entry_speed, label)

    return frame

def actual_connect(data_container, port_number, label):

    # Creates port number thingy
    port = port_number.get()

    if port != 'sim':
        port = int(port)

    # Connects to robot
    wallE = new_create.Create(port)
    data_container.robot = wallE

    data_container.label_text = 'Connected to WallE!'
    label['text'] = data_container.label_text

def disconnect_robot(data_container, label):

    # Disconnects from robot
    data_container.robot.shutdown()

    data_container.label_text = 'Disconnected from WallE!'
    label['text'] = data_container.label_text

    # Resets initial values for data container
    data_container.robot = None
    data_container.speed = 10
    data_container.distance = 10
    data_container.angle = 10
    data_container.current_angle = 0
    data_container.angle_per_second = 0
    data_container.seconds = 1
    data_container.darkness = 0
    data_container.robot_check = False

def stop_robot(data_container):

    # Emergency robot stop
    data_container.robot.stop()
    data_container.robot_check = True

def basic_move_autonomous(data_container, distance, direction, degrees_per_second, speed, label):

    # Gets values from entry boxes
    data_container.distance = float(distance.get())
    data_container.angle = float(direction.get())
    data_container.angle_per_second = float(degrees_per_second.get())
    data_container.speed = float(speed.get())

    data_container.label_text = 'Moving!'
    label['text'] = data_container.label_text

    if data_container.angle != 0 and data_container.angle_per_second != 0:

        # Corrects direction if negative
        if data_container.angle < 0:
            data_container.angle_per_second *= -1

        # Moves robot angularly if requested
        data_container.robot.go(0, data_container.angle_per_second)
        time.sleep(abs(data_container.angle / data_container.angle_per_second))

    # Moves robot linearly
    data_container.robot.go(data_container.speed, 0)
    time.sleep(abs(data_container.distance / data_container.speed))

    data_container.label_text = 'WallE has finished moving!'
    label['text'] = data_container.label_text

    # Stops robot
    data_container.robot.stop()

def advanced_frame(root, data_container, label):

    # Creates frame
    frame = ttk.Frame(root, padding=10, relief="raised")

    # Creates Time Spent Label
    label = ttk.Label(frame, text=str(data_container.Hours()[10]))
    label.grid()

    # Linear speed entry box
    speed_label = ttk.Label(frame, text="Enter a linear speed")
    speed_label.grid()
    entry_speed = ttk.Entry(frame, width=8)
    entry_speed.grid()

    # angular speed entry box
    angle_label = ttk.Label(frame, text="Enter a angular speed")
    angle_label.grid()
    entry_angle = ttk.Entry(frame, width=8)
    entry_angle.grid()

    # IR entry box
    IR_label = ttk.Label(frame, text="Enter an IR signal number (0 to 254)")
    IR_label.grid()
    entry_IR = ttk.Entry(frame, width=8)
    entry_IR.grid()

    # Move button
    move_button = ttk.Button(frame, text='Move until signal recieved')
    move_button.grid()

    # IR signal button
    signal_button = ttk.Button(frame, text='Send Signal')
    signal_button.grid()

    # When you push the move button...
    move_button['command'] = lambda: wait_for_IR_signal(data_container,
                                                       entry_speed,
                                                       entry_angle,
                                                       frame, entry_IR,
                                                       signal_button, label)

    return frame

def wait_for_IR_signal(data_container, speed, angle_per_second, frame, IR, signal_button, label):

    # Calls robot
    wallE = data_container.robot

    # IR signals can be between 0 and 254
    number = int(IR.get())

    # Starts the robot moving
    wallE.go(float(speed.get()), float(angle_per_second.get()))

    # Checks IR sensor
    while True:

        # Sends signal when button pushed
        signal_button['command'] = lambda: send_IR(data_container, number)

        # Continuously checks for IR number, if gets correct one, breaks loop
        number_heard = wallE.getSensor('IR_BYTE')
        if number_heard == number:
            break
        if stop_if_stuck(data_container):
            data_container.robot.stop()
            break
        if data_container.robot_check:
            break
        frame.update()
        time.sleep(.05)

    # Returns data container to original state
    data_container.robot_check = False

    # Stops robot
    wallE.stop()

    # Stops sending the signal
    wallE.stopIR()

    # Double check it worked correctly
    statement = ['Number WallE heard:', number_heard]
    data_container.label_text = str(statement)
    label['text'] = data_container.label_text

def stop_if_stuck(data_container):
    if (data_container.robot.getSensor('BUMPS_AND_WHEEL_DROPS')[0] or
        data_container.robot.getSensor('BUMPS_AND_WHEEL_DROPS')[1] or
        data_container.robot.getSensor('BUMPS_AND_WHEEL_DROPS')[2] or
        data_container.robot.getSensor('BUMPS_AND_WHEEL_DROPS')[3] or
        data_container.robot.getSensor('BUMPS_AND_WHEEL_DROPS')[4] or
        data_container.robot.getSensor('OVERCURRENTS')[0] or
        data_container.robot.getSensor('OVERCURRENTS')[1]):

        return True

def send_IR(data_container, number):

    # Starts sending IR on button push
    data_container.robot.startIR(number)

def line_follow_frame(root, data_container):

    # Creates frame
    frame = ttk.Frame(root, relief='raised')

    # Creates Time Spent Label
    label = ttk.Label(frame, text=str(data_container.Hours()[13]))
    label.grid()

    # Creates button to start line following
    button = ttk.Button(frame, text='Line Follow!')
    button.grid()

    # Label for enrty box and entry box
    darkness_label = ttk.Label(frame, text="Enter the darkness on black line (about 200 for real, 600 for sim)")
    darkness_label.grid()
    entry_darkness = ttk.Entry(frame, width=8)
    entry_darkness.grid()

    # Label for entry box and entry box
    constant_label = ttk.Label(frame, text="Enter the proportional constant (about 0.005 for real and .002 for sim)")
    constant_label.grid()
    entry_constant = ttk.Entry(frame, width=8)
    entry_constant.grid()

    # When you push button, does stuff...
    button['command'] = lambda: line_following(data_container, frame, entry_darkness, entry_constant)

    return frame

def line_following(data_container, frame, entry_darkness, entry_constant):

    # Creates robot
    wallE = data_container.robot

    desired = float(entry_darkness.get())

    # Initializes variables
    error_1 = 0
    error_2 = 0
    Kp = float(entry_constant.get())

    # Checks if on line and adjusts speed
    while True:

        # Update frame
        frame.update()

        # Gets sensor values
        actual_1 = wallE.getSensor('CLIFF_FRONT_RIGHT_SIGNAL')
        actual_2 = wallE.getSensor('CLIFF_FRONT_LEFT_SIGNAL')

        print('right', actual_1, 'left', actual_2)

        # Calculates error
        error_1 = actual_1 - desired
        error_2 = actual_2 - desired

        # Calculates right wheel speed
        v1 = error_1 * Kp
        right_speed = (2 + abs(v1))

        # Calculates left wheel speed
        v2 = error_2 * Kp
        left_speed = (2 + abs(v2))

        # Moves robot
        wallE.driveDirect(left_speed, right_speed)

        # Small sleep to avoid overflow
        time.sleep(.01)

        # Stop command
        if data_container.robot_check:
            break

    # Stops robot
    wallE.stop()

    # Resets data container values so can run multiple times
    data_container.robot_check = False

def open_grid(dc):

    # Creates new window for choosing points
    root = tkinter.Tk()

    # Creates frame for choosing points
    frame = ttk.Frame(root)
    frame.grid(row=1)

    # Make a tkinter.Canvas on a Frame.
    # Note that Canvas is a tkinter (NOT a ttk) class.
    canvas = tkinter.Canvas(frame, background='lightgray')
    canvas.grid()

    # Make callbacks for mouse events.
    canvas.bind('<Button-1>', lambda event: left_mouse_click(event, dc))

    # Creates frame for label
    frame1 = ttk.Frame(root)
    frame1.grid(row=0)

    # Creates label
    label = ttk.Label(frame1, text='Pick points by clicking on locations...')
    label.grid()

    # Creates frame for button
    frame2 = ttk.Frame(root)
    frame2.grid(row=2)

    # Creates button
    button = ttk.Button(frame2, text='Close Window')
    button.grid()

    # Closes window when button is pushed
    button['command'] = lambda: close_window(root)

    # Runs everything
    root.mainloop()

def left_mouse_click(event, dc):

    # Creates grey canvas for clicking on
    canvas = event.widget
    canvas.create_oval(event.x - 10, event.y - 10,
                       event.x + 10, event.y + 10,
                       fill='purple', width=3)

    # Stores clicks in data container list
    dc.click_x.append(event.x)
    dc.click_y.append(event.y)

    # Double check it worked
    print(event.x, event.y)

def close_window(root):

    # Closes point graph choosing window
    root.destroy()

def waypoints_frame(root, data_container):

    # Creates Frame
    frame = ttk.Frame(root, padding=10, relief="raised")

    # Creates Time Spent Label
    label = ttk.Label(frame, text=str(data_container.Hours()[18]))
    label.grid()

    # Creates button to choose points
    button3 = ttk.Button(frame, text='Open grid to pick points!')
    button3.grid(row=1)

    # Opens new window on click
    button3['command'] = lambda: open_grid(data_container)

    # Creates X coord entry box
    x_label = ttk.Label(frame, text="Enter list of x-coordinates")
    x_label.grid(row=2)
    x_coordinate = ttk.Entry(frame, width=8)
    x_coordinate.grid(row=3)

    # Creates Y coord entry box
    y_label = ttk.Label(frame, text="Enter list of y-coordinates")
    y_label.grid(row=4)
    y_coordinate = ttk.Entry(frame, width=8)
    y_coordinate.grid(row=5)

    # Creates speed entry box
    speed_label = ttk.Label(frame, text="Enter a speed (cm/s)")
    speed_label.grid(row=6)
    entry_speed = ttk.Entry(frame, width=8)
    entry_speed.grid(row=7)

    # Creates angular speed entry box
    angle_speed_label = ttk.Label(frame, text="Enter an angular speed(degrees/s)")
    angle_speed_label.grid(row=8)
    entry_angular_speed = ttk.Entry(frame, width=8)
    entry_angular_speed.grid(row=9)

    # Creates button to start moving
    button = ttk.Button(frame, text='Start Moving (Advanced)!')
    button.grid(row=3, column=1)

    # Moves selected points
    button['command'] = lambda: waypoints_advanced(frame,
                                                   data_container,
                                                   x_coordinate,
                                                   y_coordinate,
                                                   entry_speed,
                                                   entry_angular_speed)

    # Creates button to start moving
    button4 = ttk.Button(frame, text='Start Moving Clicked Points!')
    button4.grid(row=1, column=1)

    # Moves clicked points
    button4['command'] = lambda: waypoints_clicked_points(frame, data_container)

    # Creates button to start moving
    button2 = ttk.Button(frame, text='Retrace Movements!')
    button2.grid(row=5, column=1)

    # Retraces points when pushed
    button2['command'] = lambda: waypoints_retrace(frame, data_container)

    return frame

def waypoints_advanced(frame, dc, x, y, speed, angular_speed):

    dc.current_angle = 0

    # Gets x and y-coordinates form enrty box
    list_x = (x.get())
    list_y = (y.get())

    # Turns x and y-coordinates into a list
    x_coords = list_x.split()
    y_coords = list_y.split()

    # Gets speed and angular speed from entry box
    dc.speed = float(speed.get())
    dc.angle_per_second = float(angular_speed.get())

    # Calculates change needed to move in x and y directions
    dx = float(x_coords[0])
    dy = float(y_coords[0])

    # Updates lists
    dc.x_coordinates.insert(0, dx)
    dc.y_coordinates.insert(0, dy)

    # Calculates angle needed to move and then moves
    angle = m2.calculate_rotation(dx, dy, dc)
    m2.turn_to_direction(dc, angle)

    # Moves the given x and y distances
    m2.travel_distance(dx, dy, dc)

    # Small sleep
    time.sleep(.5)

    # Repeates for list of coordinates
    for k in range(1, len(x_coords)):

        dx = float(x_coords[k]) - float(x_coords[k - 1])
        dy = float(y_coords[k]) - float(y_coords[k - 1])

        # Updates lists
        dc.x_coordinates.insert(0, dx)
        dc.y_coordinates.insert(0, dy)

        # Turns to angle
        angle = m2.calculate_rotation(dx, dy, dc)
        m2.turn_to_direction(dc, angle)

        # Moves displacement
        m2.travel_distance(dx, dy, dc)

        # Small sleep
        time.sleep(.5)

def waypoints_clicked_points(frame, dc):

    dc.current_angle = 0

    # Gets speed and angular speed from entry box
    dc.speed = 30
    dc.angle_per_second = 60

    x = float(dc.click_x[0])
    y = float(dc.click_y[0])

    dx = calc_x(x, dc)
    dy = calc_y(y, dc)

    # Updates lists
    dc.x_coordinates.insert(0, dx)
    dc.y_coordinates.insert(0, dy)

    # Calculates angle needed to move and then moves
    angle = m2.calculate_rotation(dx, dy, dc)
    m2.turn_to_direction(dc, angle)

    # Moves the given x and y distances
    m2.travel_distance(dx, dy, dc)

    time.sleep(.5)

    # Repeates for list of coordinates
    for k in range(1, len(dc.click_x) + 1):

        # Gets dx and dy from lists in data container
        dx = float(calc_x(dc.click_x[k], dc) - calc_x(dc.click_x[k + 1], dc))
        dy = float(calc_y(dc.click_y[k], dc) - calc_y(dc.click_y[k + 1], dc))

        # Updates lists
        dc.x_coordinates.insert(0, dx)
        dc.y_coordinates.insert(0, dy)

        # Calculates and moves to angle
        angle = m2.calculate_rotation(dx, dy, dc)
        m2.turn_to_direction(dc, angle)

        # Linear movement
        m2.travel_distance(dx, dy, dc)

        # Don't wanna flood robot
        time.sleep(.5)

    # Resets data container values
    dc.click_x = []
    dc.click_y = []

def calc_x(x, dc):

    # Puts grid points into cartesian coodinate system
    if x != 250:
        dx = (x - 250) * (1 / 3)
    else:
        dx = 0
    return dx

def calc_y(y, dc):

    # Puts grid points into cartesian coordinate system
    if y < 150:
        dy = y * (1 / 3)
    elif y > 150:
        dy = (150 - y) * (1 / 3)
    else:
        dy = 0
    return dy

def waypoints_retrace(frame, dc):

    dc.speed = 30
    dc.angle_per_second = 60

    # Gets first point
    dx = -dc.x_coordinates[0]
    dy = -dc.y_coordinates[0]

    # Calculates angle needed to move and then moves
    angle = m2.calculate_rotation(dx, dy, dc)
    m2.turn_to_direction(dc, angle)

    # Moves the given x and y distances
    m2.travel_distance(dx, dy, dc)

    time.sleep(.5)

    # Repeates for rest of list of coordinates
    for k in range(1, len(dc.x_coordinates)):

        dx = -float(dc.x_coordinates[k])
        dy = -float(dc.y_coordinates[k])

        angle = m2.calculate_rotation(dx, dy, dc)
        m2.turn_to_direction(dc, angle)

        m2.travel_distance(dx, dy, dc)

        time.sleep(.5)

    # Clears list of coordinates
    dc.x_coordinates = []
    dc.y_coordinates = []


#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
