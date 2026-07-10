label park_local_nap:
    pc "I am exausted. Maybe I can have a quick nap on the bench"
    menu:
        pc "I am exausted. Maybe I can have a quick nap on the bench"
        "Have a quick nap.":

            if t.hour in light:

                show screen blackout_screen with dissolve
                $ time_sleep_rough()
                $ rand_choice = WeightedChoice([
                ("sleep_rough_wake_vcommon", 800),
                ("sleep_rough_wake_common", 300),
                ("sleep_rough_wake_normal", 50),
                ("sleep_rough_wake_rare", 5),
                ("sleep_rough_wake_vrare", 1)
                ])
                jump expression rand_choice
            else:
                show screen blackout_screen with dissolve
                $ time_sleep_rough()
                $ rand_choice = WeightedChoice([
                ("sleep_rough_wake_vcommon", 400),
                ("sleep_rough_wake_common", 150),
                ("sleep_rough_wake_normal", 20),
                ("sleep_rough_wake_rare", 5),
                ("sleep_rough_wake_vrare", 1)
                ])
                jump expression rand_choice
        "Not now.":

            pc "Not now, I should probably go home and rest anyway."
            jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
