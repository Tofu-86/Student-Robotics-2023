from sr.robot3 import *
robot = Robot()

ny_servo_board = robot.servo_board

#Servo definitions
RotationalArm1 = robot.servo_board.servos[0]
RotationalArm2 = robot.servo_board.servos[1]
GrapplerArm1 = robot.servo_board.servos[2]
GrapplerArm2 = robot.servo_board.servos[3]


#Position to start arams in
def DefaultArmPosition():
    DefaultPos = 0
    RotationalArm1.position = DefaultPos
    RotationalArm2.position = DefaultPos
    GrapplerArm1.position = DefaultPos
    GrapplerArm2.position = DefaultPos

#Should only be used to test if the servos actually work lol.
def TestFunctionArm():
    DefaultArmPosition()
    RotationalArm1.position = 1
    RotationalArm2.position = -1
    GrapplerArm1.position = 1
    GrapplerArm2.position = -1
    
    robot.sleep(3000)

    RotationalArm1.position = -1
    RotationalArm2.position = 1
    GrapplerArm1.position = -1
    GrapplerArm2.position = 1
    
#Rotational arms lifting  box
def RotationalArmLiftPosition():
    LiftPos = 1
    RotationalArm1.position = LiftPos
    RotationalArm2.position = -LiftPos

    arm.position = pos

#main code ran here  for arms
def ArmLift():
    robot.sleep(1000)
    DefaultArmPosition()
    RotationalArm1.position = 0.2
    RotationalArm2.position = -0.2
    robot.sleep(1000)           #dk if this is 1 second or 1000 seconds.
    GrapplerArm1.position = 0.2
    GrapplerArm2.position = -0.2
    robot.sleep(500)
    RotationalArmLiftPosition()
    
def ArmPlace():
    robot.sleep(1000)
    RotationalArm1.position = 0.8
    RotationalArm2.position = -0.8
    robot.sleep(500)
    GrapplerArm1.position = -0.1
    GrapplerArm2.position = 0.1