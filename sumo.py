from zumo_2040_robot import robot
import time

motors = robot.Motors()
proximity_sensors = robot.ProximitySensors()
button_a = robot.ButtonA()
display = robot.Display()
buzzer = robot.Buzzer()

display.fill(0)
display.text("Press A", 0, 0)
display.show()
buzzer.play("o5c32>c32")

while not button_a.check():
    pass

display.fill(0)
display.text("Go!!!", 0, 0)
display.show()

buzzer.play("c4r4c4r4")
buzzer.play_in_background("g2")

while True:
    proximity_sensors.read()

    left = proximity_sensors.counts[0]
    front = proximity_sensors.counts[1]
    right = proximity_sensors.counts[2]
    
    display.fill(0)
    display.text(str(list(left)), 0, 0)
    display.text(str(list(front)), 0, 10)
    display.text(str(list(right)), 0, 20)
    display.show()
    
    if sum(front) > 2:
        motors.set_speeds(3000, 3000)
    elif sum(left) > 1:
        motors.set_speeds(-3000, 3000)
    elif sum(right) > 1:
        motors.set_speeds(3000, -3000)
    else:
        motors.off()