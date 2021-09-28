from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 4
robotArm.grab()
for a in range (1,3):
    robotArm.moveRight()
robotArm.drop()
for b in range(1,3):
    robotArm.moveLeft()
robotArm.grab()
for c in range(1,3):
    robotArm.moveRight()
robotArm.drop()
for d in range(1,3):
    robotArm.moveLeft()
robotArm.grab()
for e in range(1,3):
    robotArm.moveRight()
robotArm.drop()
for f in range(1,3): 
    robotArm.moveLeft()
robotArm.grab()
for g in range(1,3):
    robotArm.moveRight()
robotArm.drop()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()