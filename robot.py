from sr.robot3 import *

robot = Robot()

def drive(power, time):                                         #Normal function 
    robot.motor_board.motors[0].power = power
    robot.motor_board.motors[1].power = power
    robot.sleep(time)                                           #The power makes the motor spin, the robot.sleep is how long it spins for in seconds, if there isnt a robot.sleep after it, it will run forever
    robot.motor_board.motors[0].power = 0                       #This stops the robot moving
    robot.motor_board.motors[1].power = 0


def turn(direction):                                            #Add another time parameter after direction so def turn(direction, time) for more control, i didnt do it cus im lazy once again.
    spinpower = 0.35                                            #Change this value for the speed in which the turning goes at
    n_spinpower = -spinpower
    runtime = 1.5                                               #change this for how long you want the turning to run for

    if direction == "left":
        robot.motor_board.motors[0].power = spinpower           #turning n stuff 
        robot.motor_board.motors[1].power = -n_spinpower        #Haven't quite got the 90 degrees set up due to me being a lazy ass you guys can do it lol
        robot.sleep(runtime)
        robot.motor_board.motors[0].power = 0
        robot.motor_board.motors[1].power = 0
        robot.sleep(2)                                          #literally only here so the robot doesn't blow up or smthn 
    
    
    if direction == "right":
        robot.motor_board.motors[1].power = spinpower
        robot.motor_board.motors[0].power = n_spinpower
        robot.sleep(runtime)
        robot.motor_board.motors[0].power = 0
        robot.motor_board.motors[1].power = 0
        robot.sleep(2)



while True:
    turn("right")
    robot.sleep(2)
    drive(-0.3, 2)                                              #wiring polarity is messed up and i cba to fix it so just wack a - sign if u need to make it go forwards
    turn("left")
    robot.sleep(2)

    
    