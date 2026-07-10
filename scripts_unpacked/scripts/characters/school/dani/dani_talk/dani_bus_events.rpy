label dani_bus_goto_school_event_picker:
    $ dialouge = renpy.random.choice([
    "We squeeze on the bus and manage to find somewhere to stand.",
    "We get on the bus and look for some space to stand.",
    "We work our way through the crowd and find somewhere to stand.",
    "We make our way through the bus and find somewhere to stand."
    ])
    "[dialouge]"

    call expression WeightedChoice([
    ("dani_bus_event_1", 100),

    ]) from _call_expression_26
    jump dani_goto_school_arrive

label dani_bus_event_1:
    $ dialouge = renpy.random.choice([
    "We stand there talking and joking about random stuff.",
    "We wait for our stop while chatting and joking around about random topics.",
    "We stand there talking and laughing about whatever comes up.",
    "We chat and have a bit of a laugh about random stuff."
    ])
    "[dialouge]"
    return

label dani_goto_school_arrive:
    if pc_lost_clothes():
        "I manage to grab back the clothes that the perverts took from me."
        pcm "Quickly before I need to get off..."
        $ pc_dress()
    $ relax(10, dani)
    pc "Our stop is here. Come on, let's go."
    if not renpy.showing("dani"):
        $ renpy.scene()
        show dani at right6
        with dissolve
    dani.name "Yup."
    $ walk(loc_busstop_school)
    $ walk(loc_school)
    dani.name "See you in there."
    hide dani with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
