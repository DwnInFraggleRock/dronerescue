from djitellopy import Tello
from time import sleep

# all cm in code is rounded down


tello = Tello()
tello.connect()

tello.takeoff()
# takeoff is 81cm

tello.move_up(101)
# now at 60 feet on 10:1 scale
sleep(2)
# Line to due east
tello.move_forward(152)
sleep(2)
# fly forward for 5 feet
tello.send_rc_control(0, 0, 0, -50)
sleep(3.46)
# rotate to north
# First leg done

tello.move_forward(182)
sleep(2)
# move forward for 6 feet

tello.send_rc_control(0, 0, 0, 50)
sleep(3.46)
# turn 90 degrees to face east
# second leg done

tello.move_down(91)
sleep(2)
# move down to 3 ft
tello.move_forward(91)
sleep(2)
# move forward 3 feet
tello.send_rc_control(0, 0, 0, 50)
sleep(3.46)
# rotate left
# third leg done

tello.move_up(30)
# move up a foot to 4 feet total height
sleep(2)
tello.move_forward(91)
sleep(2)
# move forward 3 feet
tello.send_rc_control(0, 0, 0, -50)
sleep(3.46)
# rotate 90 degrees to east
# forth leg done

tello.move_forward(182)
# move forward for 6 feet
tello.land()
sleep(2)
# drone delivered 
