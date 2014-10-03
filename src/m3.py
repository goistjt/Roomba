"""
The  Python Capstone Project -- Talk to Me!

CSSE 120 - Introduction to Software Development (Robotics).
Winter term, 2013-2014.
Team members: Brooke Brown, Jeremiah Goist, and Sarah Walker.

The primary author of this module is: Brooke Brown
"""
# TODO: Put the names of ALL team members in the above where indicated.
#       Put YOUR NAME in the above where indicated.

import m0
import m1
import m2
import m4

import tkinter
from tkinter import ttk

import time
import new_create


class PID(object):
    """ Simple PID control.
    """
    def __init__(self):
        # initialze gains
        self.Kp = 0
        self.Kd = 0
        self.Ki = 0

        self.Initialize()

    def SetKp(self, P):
        """ Set proportional gain. """
        self.Kp = float(P)

    def SetKi(self, I):
        """ Set integral gain. """
        self.Ki = float(I)

    def SetKd(self, D):
        """ Set derivative gain. """
        self.Kd = float(D)

    def SetPrevErr(self, preverr):
        """ Set previous error value. """
        self.previous_error = preverr

    def Initialize(self):
        # initialize delta t variables
        self.currtm = time.time()
        self.prevtm = self.currtm

        self.prev_err = 0

        # term result variables
        self.Cp = 0
        self.Ci = 0
        self.Cd = 0


    def GenOut(self, error):
        """ Performs a PID computation and returns a control value based on
            the elapsed time (dt) and the error signal from a summing junction
            (the error parameter).
        """
        self.currtm = time.time()  # get t
        dt = self.currtm - self.prevtm  # get delta t
        de = error - self.prev_err  # get delta error

        self.Cp = self.Kp * error  # proportional term
        self.Ci += error * dt  # integral term

        self.Cd = 0
        if dt > 0:  # no div by zero
            self.Cd = de / dt  # derivative term

        self.prevtm = self.currtm  # save t for next pass
        self.prev_err = error  # save t-1 error

        # sum the terms and return the result
        return self.Cp + (self.Ki * self.Ci) + (self.Kd * self.Cd)

def main():
    print('Testing functions in module m3:\n')

    root = tkinter.Tk()
    dc = m0.DataContainer()
    pid = PID()

    label = ttk.Label(root, text=dc.label_text)
    label.grid(row=0, column=0, ipadx=150, ipady=50)

    frame = basic_auto_frame(root, dc)
    frame.grid()

    frame2 = adv_teleop_frame(root, dc)
    frame2.grid()

    frame3 = basic_chat_frame(root, dc)
    frame3.grid()

    frame4 = adv_line_following_frame(root, dc, pid, label)
    frame4.grid()

    frame5 = leap_frame(root, dc)
    frame5.grid()

    root.mainloop()



# Leap Motion Stuff

def leap_frame(root, data_container):
    frame = ttk.Frame(root, padding=10, relief='raised')

    # Creates Time Spent Label
    label = ttk.Label(frame, text=str(data_container.Hours()[22]))
    label.grid()

    leap_button = ttk.Button(frame, text='Start Leap Control!')
    leap_button.grid()

    leap_button['command'] = lambda: leap_function(frame, data_container)

    return frame

def leap_function(frame, data_container):
    print('Moving with Leap Motion!')
    counter = 0
    while True:
        frame.update()
        leap_file = open('../../Z_ProjectLeapMotion/src/leap' + str(counter), 'r')
        motion = leap_file.read()
        parts1 = motion.split(' ')
        parts2 = []
        for k in range(len(parts1)):
            parts2 += parts1[k].split(',')
        leap_file.close()
        counter += 1
        time.sleep(1.25)
        num_of_fingers = int(parts2[11])
        print('Fingers:', num_of_fingers)
        if data_container.robot_check:
            data_container.robot.stop()
            data_container.robot_check = False
        elif num_of_fingers == 0:
            go_straight(data_container)
        elif num_of_fingers == 1:
            forward(data_container, 30)
        elif num_of_fingers == 2:
            forward(data_container, -30)
        elif num_of_fingers == 3:
            backward(data_container, 30)
        elif num_of_fingers == 4:
            backward(data_container, -30)
        elif num_of_fingers == 5 or num_of_fingers == 6:
            data_container.robot_check = True

def go_straight(data_container):
    data_container.robot.go(15, 0)

def forward(data_container, angle):
    m2.move_forward(data_container, angle)

def backward(data_container, angle):
    m2.move_backward(data_container, angle)

def basic_auto_frame(root, data_container):
    """
    Constructs and returns a Frame that contains this module's widgets.
    Also sets up callbacks for this module's widgets.
    """
    frame = ttk.Frame(root, padding=10, relief='raised')

    # Creates Time Spent Label
    label = ttk.Label(frame, text=str(data_container.Hours()[6]))
    label.grid()

# Basic: WIW can move autonomously, by going until an event occurs.
    label = ttk.Label(frame, text='Enter a speed in the box')
    label.grid()
    entry = ttk.Entry(frame, width=8)
    entry.grid()

    label2 = ttk.Label(frame, text='Enter a darkness in the box')
    label2.grid()
    entry2 = ttk.Entry(frame, width=8)
    entry2.grid()

    auto_bump_button = ttk.Button(frame, text='Go Until Bumped!')
    auto_bump_button.grid()

    auto_bump_button['command'] = lambda: autonomous_bump(frame, data_container, entry)

    auto_dark_button = ttk.Button(frame, text='Go Until Dark!')
    auto_dark_button.grid()

    auto_dark_button['command'] = lambda: autonomous_darkness(frame, data_container,
                                                              entry, entry2)

    return frame


# Basic Autonomous movement until wallE is bumped

def autonomous_bump(frame, data_container, entry_speed):
    print('Autonomous Movement Until Bumped!')
    bumps_sensors = new_create.Sensors.bumps_and_wheel_drops

    data_container.speed = float(entry_speed.get())
    if data_container.speed < 0:
        data_container.speed = 0

    data_container.robot.go(data_container.speed, 0)
    while True:
        sensor_values = data_container.robot.getSensor(bumps_sensors)
        left_bumper_state = sensor_values[3]
        right_bumper_state = sensor_values[4]
        if left_bumper_state == 1 or right_bumper_state == 1:
            data_container.robot.stop()
            break
        frame.update()
        time.sleep(0.05)

def autonomous_darkness(frame, data_container, entry_speed, entry_darkness):
    print('Autonomous Movement Until Dark!')
    darkness_sensor = new_create.Sensors.cliff_front_left_signal

    speed = entry_speed.get()
    darkness_level = entry_darkness.get()

    data_container.robot.go(int(speed), 0)
    while True:
        darkness = data_container.robot.getSensor(darkness_sensor)
        if darkness <= int(darkness_level):
            data_container.robot.stop()
            break
        frame.update()
        time.sleep(0.05)

def adv_teleop_frame(root, data_container):
    frame = ttk.Frame(root, padding=10, relief='raised')

    # Creates Time Spent Label
    label = ttk.Label(frame, text=str(data_container.Hours()[3]))
    label.grid()

    tele_button = ttk.Button(frame, text='Tele-Operated With Keys!')
    tele_button.grid()

    tele_button['command'] = lambda: tele_move(frame, data_container)

    return frame


# Teleoperation Advanced

def tele_move(frame, data_container):
    print('Tele-operated movement with keys!')

    # Arrow Key Control!
    frame.bind_all('<Up>', lambda event: m2.move_forward(data_container,
                                                data_container.angle_per_second))
    frame.bind_all('<Left>', lambda event: m2.move_backward(data_container,
                                                data_container.angle_per_second))
    frame.bind_all('<Right>', lambda event: m2.move_forward(data_container,
                                                data_container.angle_per_second))
    frame.bind_all('<Down>', lambda event: m2.move_backward(data_container,
                                                - data_container.angle_per_second))

    # Adding ability to change speed and angle with keys.
    frame.bind_all('<d>', lambda event: m2.increase_angle_per_second(data_container))
    frame.bind_all('<a>', lambda event: m2.decrease_angle_per_second(data_container))
    frame.bind_all('<w>', lambda event: m2.increase_speed(data_container))
    frame.bind_all('<s>', lambda event: m2.decrease_speed(data_container))
    frame.bind_all('<Shift_R>', lambda event: m2.stop_robot(data_container))


# WallE can chat with another robot via IR.

def basic_chat_frame(root, data_container):
    frame = ttk.Frame(root, padding=10, relief='raised')

    # Creates Time Spent Label
    label = ttk.Label(frame, text=str(data_container.Hours()[12]))
    label.grid()

    IR_label = ttk.Label(frame, text="Enter a list of IR signal numbers (0 to 253)")
    IR_label.grid()
    entry_IR = ttk.Entry(frame, width=8)
    entry_IR.grid()

    signal_button = ttk.Button(frame, text='Chat')
    signal_button.grid()

    send_button = ttk.Button(frame, text='Send Signal')
    send_button.grid()

    listen_button = ttk.Button(frame, text='Listen for Signal')
    listen_button.grid()

    stop_button = ttk.Button(frame, text='Stop Signal')
    stop_button.grid()

    signal_button['command'] = lambda: chat_via_IR(frame, data_container, entry_IR)
    send_button['command'] = lambda: send_signal(data_container, entry_IR)
    listen_button['command'] = lambda: listen_for_signal(frame, data_container)
    stop_button['command'] = lambda: stop_signal(data_container)

    return frame

def chat_via_IR(frame, data_container, IR):
    # Calls robot
    wallE = data_container.robot

    # IR signals can be between 0 and 254
    list_of_numbers = IR.get()
    numbers = list_of_numbers.split(' ')

    # Starts sending IR on button push
    for k in range(len(numbers)):
        if wallE.getSensor('IR_BYTE') == 255:
            send_signal_handshake(frame, wallE, int(numbers[k]))
            listen_for_signal_handshake(data_container, frame, int(numbers[k]))
        elif wallE.getSensor('IR_BYTE') != 255:
            if k == len(numbers) - 1:
                listen_for_signal_handshake_last(data_container, frame, int(numbers[k]))
            else:
                listen_for_signal_handshake(data_container, frame, int(numbers[k]))
            send_signal_handshake(frame, wallE, int(numbers[k]))
        time.sleep(0.1)

def send_signal_handshake(frame, wallE, IR):
    wallE.startIR(IR)
    while True:
        frame.update()
        if wallE.getSensor('IR_BYTE') == 254:
            wallE.stopIR()
            break


def listen_for_signal_handshake(data_container, frame, IR_sent):
    data_container.robot_check = False
    while True:
        heard = data_container.robot.getSensor('IR_BYTE')
        frame.update()
        if heard != IR_sent and heard != data_container.IR_heard and heard != 255 and heard != 254:
            print('Number wallE Heard:', heard)
            data_container.robot.startIR(254)
            time.sleep(0.75)
            data_container.robot.stopIR()
            data_container.IR_heard = heard
            break
        if data_container.robot_check:
            break
    return data_container.IR_heard

def listen_for_signal_handshake_last(data_container, frame, IR_sent):
    data_container.robot_check = False
    while True:
        heard = data_container.robot.getSensor('IR_BYTE')
        frame.update()
        if heard != IR_sent and heard != 255 and heard != 254:
            print('Number wallE Heard:', heard)
            data_container.robot.startIR(254)
            time.sleep(3.0)
            data_container.robot.stopIR()
            break
        if data_container.robot_check:
            break


def send_signal(data_container, IR):
    wallE = data_container.robot
    signal = IR.get()

    wallE.startIR(int(signal))

def listen_for_signal(frame, data_container):
    wallE = data_container.robot

    while True:
        heard = wallE.getSensor('IR_BYTE')
        frame.update()
        if heard != 255:
            print('Number WallE Heard:', heard)
            break

def stop_signal(data_container):
    data_container.robot.stopIR()


# wallE can follow a line using PID and other controls

def adv_line_following_frame(root, data_container, pid, print_label):
    # Creates frame
    frame = ttk.Frame(root, padding=10, relief='raised')

    # Creates Time Spent Labels
    label = ttk.Label(frame, text=str(data_container.Hours()[19]))
    label.grid()

    label = ttk.Label(frame, text=str(data_container.Hours()[20]))
    label.grid()

    # Creates button to start line following
    button = ttk.Button(frame, text='Advanced Line Follow!')
    button.grid()

    wall_button = ttk.Button(frame, text='Follow that damn wall')
    wall_button.grid()

    darkness_label = ttk.Label(frame, text="Enter the darkness on black line (about 800 for real, 600 for sim)")
    darkness_label.grid()
    entry_darkness = ttk.Entry(frame, width=8)
    entry_darkness.grid()

    wall_label = ttk.Label(frame, text="Enter the wall sensor value (about 130)")
    wall_label.grid()
    entry_wall = ttk.Entry(frame, width=8)
    entry_wall.grid()

    p_label = ttk.Label(frame, text="Enter the proportional constant (about 0.02 for line, .1 for wall & .002 for sim)")
    p_label.grid()
    entry_p = ttk.Entry(frame, width=8)
    entry_p.grid()


    i_label = ttk.Label(frame, text="Enter the integral constant (about 0.00001 for line, .0005 for wall & .00025 for sim)")
    i_label.grid()
    entry_i = ttk.Entry(frame, width=8)
    entry_i.grid()


    d_label = ttk.Label(frame, text="Enter the derivative constant (about 0.00001 for line, .0005 for wall & .0005 for sim)")
    d_label.grid()
    entry_d = ttk.Entry(frame, width=8)
    entry_d.grid()

    # Button commands
    button['command'] = lambda: line_following(data_container, pid, frame, entry_darkness,
                                               entry_p, entry_i, entry_d, print_label)
    wall_button['command'] = lambda: wall_following(data_container, pid, frame, entry_wall, entry_p, entry_i, entry_d, print_label)

    return frame

def line_following(data_container, pid, frame, darkness, P, I, D, print_label):
    wallE = data_container.robot

    desired = float(darkness.get())

    pid.SetKp(P.get())
    pid.SetKi(I.get())
    pid.SetKd(D.get())

    # Checks if on line and adjusts speed
    while True:
        frame.update()

        # Gets sensor values
        actual_fr = wallE.getSensor('CLIFF_FRONT_RIGHT_SIGNAL')
        actual_fl = wallE.getSensor('CLIFF_FRONT_LEFT_SIGNAL')

        print('front right', actual_fr, 'front left', actual_fl)

        data_container.label_text = ('front right', actual_fr, 'front left', actual_fl)
        print_label['text'] = data_container.label_text


        # Calculates error
        error1 = actual_fr - desired
        error2 = actual_fl - desired

        # Calculates right wheel speed
        right_speed = 5 + pid.GenOut(error1)


        # Calculates left wheel speed
        left_speed = 5 + pid.GenOut(error2)

        wallE.driveDirect(left_speed, right_speed)

        # Small sleep to avoid overflow
        time.sleep(.01)

        # Stop command
        if data_container.robot_check:
            break

    wallE.stop()

    data_container.robot_check = False

def wall_following(data_container, pid, frame, wall_strength, P, I, D, print_label):
    wallE = data_container.robot

    desired = float(wall_strength.get())

    pid.SetKp(P.get())
    pid.SetKi(I.get())
    pid.SetKd(D.get())

    # Checks if on line and adjusts speed
    while True:
        frame.update()

        # Gets sensor values
        actual_wall = wallE.getSensor('WALL_SIGNAL')

        print('Wall', actual_wall)

        data_container.label_text = ('Wall', actual_wall)
        print_label['text'] = data_container.label_text

        if actual_wall == None:
            actual_wall = 150
        # Calculates error
        error1 = actual_wall - desired

        # Calculates right wheel speed
        right_speed = 10 + pid.GenOut(error1)

        # Calculates left wheel speed
        left_speed = 10 + pid.GenOut(-error1)

        wallE.driveDirect(left_speed, right_speed)

        # Small sleep to avoid overflow
        time.sleep(.01)

        # Stop command
        if data_container.robot_check:
            break
        if data_container.robot.getSensor('BUMPS_AND_WHEEL_DROPS')[4] or data_container.robot.getSensor('BUMPS_AND_WHEEL_DROPS')[3]:
            data_container.robot.go(0, 30)
            data_container.robot.waitAngle(10)

    wallE.stop()

    data_container.robot_check = False

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------

if __name__ == '__main__':
    main()
