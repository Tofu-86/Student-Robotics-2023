import cv2
from sr.robot3 import *
import math
robot = Robot()
#my_motor_board = robot.motor_board


RotationalArm1 = robot.servo_board.servos[0]
RotationalArm2 = robot.servo_board.servos[1]
GrapplerArm1 = robot.servo_board.servos[2]
GrapplerArm2 = robot.servo_board.servos[3]

def grappleBox():
    robot.sleep(2)
    GrapplerArm1.position = 0.4
    GrapplerArm2.position = -0.4
    RotationalArm1.position = -1
    RotationalArm2.position = 1
    robot.sleep(0.4)
    RotationalArm1.position = 1
    RotationalArm2.position = -1

def placeBox():
    robot.sleep(2)
    RotationalArm1.position = -0.35
    RotationalArm2.position = 0.35
    robot.sleep(0.4)
    GrapplerArm1.position = 1
    GrapplerArm2.position = -1
    
def drive(power, time):                                         #Normal function 
    robot.motor_board.motors[0].power = power
    robot.motor_board.motors[1].power = power
    robot.sleep(time)                                           #The power makes the motor spin, the robot.sleep is how long it spins for in seconds, if there isnt a robot.sleep after it, it will run forever
    robot.motor_board.motors[0].power = 0                       #This stops the robot moving
    robot.motor_board.motors[1].power = 0


def scanHome():
    pass
    #Camera scans for the spaceship marker to place the box  back into. 
    #robot spins slowly to find where our ship is.
    #attempt to add collision detection, so if theres something infront of the robot, it wont run directly into it.
    #then robot travels home
    placeBox() # once parallel to spaceship, it will place

def scanBox():
    #scan for the boxes
    #travel to box
    #once parallel
    grappleBox()
    scanHome()

def homeCheck():
    pass
    #check if the spaceship is in the correct place  by comparing the markers around the arena to the marker on the spaceship (compare distance.)
    #at the start , either pre program the correct distance ro work it out when the robot is in the arena.

def stealShip():
    pass
    #in the name innit.
    #probably run this at the start too. 



def runtime():
    scanBox()
    homeCheck()
    runtime()
    
    
stealShip()
runtime()



# loop = True
# while loop:
#     robot.sleep(2)
#     GrapplerArm1.position = 0.4
#     GrapplerArm2.position = -0.4
#     RotationalArm1.position = -1
#     RotationalArm2.position = 1
#     robot.sleep(0.4)
#     RotationalArm1.position = 1
#     RotationalArm2.position = -1
#     robot.sleep(5)
#     RotationalArm1.position = -1
#     RotationalArm2.position = 1
#     robot.sleep(0.4)
#     GrapplerArm1.position = 1
#     GrapplerArm2.position = -1




# def take_pic():
#     robot.camera.save(robot.usbkey / "view19.jpg")
#     markers = robot.camera.see()
#     for marker in markers:
#         print(f"The marker has id {marker.id}")
#         print(f"The marker is {marker.position.distance} mm from the cam") #distance from camera and center of marker
#         print(f"The horizontal angle is {marker.position.horizontal_angle} radians") 
#         print(f"The vertical angle is {marker.position.vertical_angle} radians")
#         print(f"Yaw:{marker.orientation.yaw}")
#         print(f"Pitch:{marker.orientation.pitch}")
#         print(f"Roll{marker.orientation.roll}")

# take_pic()