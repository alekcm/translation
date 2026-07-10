define work_fliers_var_clothing = False
define work_fliers_var_market = False
define work_fliers_var_fliers = False


define work_fliers_events_counter = 0
define work_fliers_naughty_counter = 0



label work_fliers:
    "You start walking around the streets handing out fliers to everone you see."


    jump work_fliers_end



label work_fliers_end:
    "Before you know it, an hour has passed."
    $ t.hour = 1
    if work_fliers_events_counter == 0:
        $ face = 1
        pc "That was easy, almost nothing happened."
    elif work_fliers_events_counter <= 3:
        pc "Okay looks like I'm done."
    else:
        $ face = 4
        pc "Uff, finally done..."

    if work_fliers_var_clothing == True:
        "You return to Teen Spirit and get back to your normal duties."
        $ work_fliers_var_clothing = False
        $ work_clothing_events_counter += 3
        $ face = 0
        jump work_clothing_weights


    elif work_fliers_var_market == True:
        "You return to the market stall and return to your normal duties."
        $ work_fliers_var_market = False

        $ face = 0


    elif work_fliers_var_fliers == True:
        "You give your leftover fliers to [flier]."
        $ work_fliers_var_fliers = False
        $ face = 0
        jump commercial_area_mall_screen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
