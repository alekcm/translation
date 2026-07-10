












































label code_example:
    jump expression WeightedChoice([
    ("exhib_events_1_0", can_trigger_events(0)),
    ("exhib_events_2_0", can_trigger_events(0)),
    ("exhib_events_3_0", can_trigger_events(0)),
    ("exhib_events_4_0", can_trigger_events(0)),
    ("exhib_events_5_0", can_trigger_events(0)),

    ("exhib_events_1_1", can_trigger_events(1)),
    ("exhib_events_2_1", can_trigger_events(1)),
    ("exhib_events_3_1", can_trigger_events(1)),
    ("exhib_events_4_1", can_trigger_events(1)),
    ("exhib_events_5_1", can_trigger_events(1)),

    ("exhib_events_1_2", can_trigger_events(2)),
    ("exhib_events_2_2", can_trigger_events(2)),
    ("exhib_events_3_2", can_trigger_events(2)),
    ("exhib_events_4_2", can_trigger_events(2)),
    ("exhib_events_5_2", can_trigger_events(2)),

    ("exhib_events_1_3", can_trigger_events(3)),
    ("exhib_events_2_3", can_trigger_events(3)),
    ("exhib_events_3_3", can_trigger_events(3)),
    ("exhib_events_4_3", can_trigger_events(3)),
    ("exhib_events_5_3", can_trigger_events(3)),

    ("exhib_events_1_4", can_trigger_events(4)),
    ("exhib_events_2_4", can_trigger_events(4)),
    ("exhib_events_3_4", can_trigger_events(4)),
    ("exhib_events_4_4", can_trigger_events(4)),
    ("exhib_events_5_4", can_trigger_events(4)),
    ])


default menuset = set()

label menu_test:
    menu menu_test1:
        set menuset
        "Where should I go?"
        "Go to class.":


            jump go_to_class
        "Go to the bar.":

            jump go_to_bar
        "Go to jail.":

            jump go_to_jail

label chapter_1_after_places:

    "Wow, that was one heck of a Tuesday."

label go_to_class:
    "Go to class and return"
    jump menu_test

label go_to_bar:
    "Go to bar and return"
    jump menu_test

label go_to_jail:
    "Go to jail and return"
    jump menu_test
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
