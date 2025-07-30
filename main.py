def on_gesture_shake():
    integer = (randint(1,6))
    basic.show_number(integer)
    pause(400)
    if integer == 1: 
        basic.show_arrow(ArrowNames.NORTH)
    elif integer == 2:
        basic.show_arrow(ArrowNames.SOUTH)
    elif integer == 3:
        basic.show_arrow(ArrowNames.EAST)
    elif integer == 4:
        basic.show_arrow(ArrowNames.WEST)
    elif integer == 5:
        basic.show_arrow(ArrowNames.SOUTH_WEST)
    elif integer == 6:
        basic.show_arrow(ArrowNames.NORTH_EAST)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

