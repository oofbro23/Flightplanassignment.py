from djitellopy import Tello

from time import sleep


kp.init()
tello = Tello()
tello.connect
print(tello.get_battery())

tello.takeoff()

# 32in = 82cm

tello.move_up(101)

tello.move(152)
sleep(1)

tello.rotate_counter_clockwise(90)

tello.move_forward(183)
sleep(1)

tello.rotate_clockwise(90)

tello.move_down(91)

tello.move_forward(91)
sleep(1)

tello.rotate_clockwise(90)

tello.move_forward(91)
sleep(1)

tello.rotate_clockwise(90)

tello.move_up(30)

tello.move_forward(183)

tello.move_down(183)

