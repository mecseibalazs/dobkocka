kocka = 0

def on_forever():
    global kocka
    if input.is_gesture(Gesture.SHAKE):
        kocka = randint(1, 6)
    if kocka == 1:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
    if kocka == 2:
        basic.show_leds("""
            . . . . .
                        . . . # .
                        . . . . .
                        . # . . .
                        . . . . .
        """)
    if kocka == 3:
        basic.show_leds("""
            . . . . .
                        . . . # .
                        . . # . .
                        . # . . .
                        . . . . .
        """)
    if kocka == 4:
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . . . .
                        . # . # .
                        . . . . .
        """)
    if kocka == 5:
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . # . .
                        . # . # .
                        . . . . .
        """)
    if kocka == 6:
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . # . # .
                        . # . # .
                        . . . . .
        """)
basic.forever(on_forever)
