from djitellopy import Tello

from time import sleep

tello = Tello()

tello.connect()

tello.takeoff()

tello.move_up(181)

tello.move_forward(152)
sleep(1)

tello.rotate_counter_clockwise(90)

tello.move_forward(183)
sleep(1)

tello.rotate_clockwise(90)

tello.move_down(91)

tello.move_forward(91)
sleep(1)

tello.rotate_clockwise(90)

tello.move_up(30)

tello.move_forward(91)
sleep(1)

tello.rotate_counter_clockwise(90)

tello.move_forward(183)

tello.land()
