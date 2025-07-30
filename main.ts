input.onGesture(Gesture.Shake, function on_gesture_shake() {
    let integer = randint(1, 6)
    basic.showNumber(integer)
    pause(400)
    if (integer == 1) {
        basic.showArrow(ArrowNames.North)
    } else if (integer == 2) {
        basic.showArrow(ArrowNames.South)
    } else if (integer == 3) {
        basic.showArrow(ArrowNames.East)
    } else if (integer == 4) {
        basic.showArrow(ArrowNames.West)
    } else if (integer == 5) {
        basic.showArrow(ArrowNames.SouthWest)
    } else if (integer == 6) {
        basic.showArrow(ArrowNames.NorthEast)
    }
    
})
