
label hallway_screen:

    call screen travel_screen

label hallway_arrival:
    $ walk(False, "hallway", 1)
    $ loc_home = True

    $ arrival()

    jump hallway_screen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
