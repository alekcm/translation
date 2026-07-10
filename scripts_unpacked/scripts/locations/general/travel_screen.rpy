label travel:
    if force_return:
        $ force_return = False
        return
    $ arrival_travel()
    call screen travel_screen 

label travel_arrival:
    if force_return:
        $ force_return = False
        return
    $ arrival()
    $ arrival_character_speech_popup()
    call screen travel_screen 

label travel_dis:
    if force_return:
        $ force_return = False
        return
    $ arrival_travel()
    $ arrival_character_speech_popup()
    call screen travel_screen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
