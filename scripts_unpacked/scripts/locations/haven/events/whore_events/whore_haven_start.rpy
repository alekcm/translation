label dis_haven_whore_lowmood:
    pcm "Ugh. Really want a pick me up. Wonder if I can get anything off some of the guys round here..."
    jump dis_haven_whore

label dis_haven_whore:
    if player.cum_visible or not player.allure:
        pcm "No one is going to pay for me while I am like this. I need to shower first."
        jump travel
    if haven_time_empty():
        pcm "This place is a graveyard right now. I would just be wasting my time. Better off trying to scavenge around."
        jump travel
    elif haven_time_safe() and loc_cur == [loc_haven_bed, loc_haven_bedroom]:
        pcm "The girls are all around the bedroom so probably a bad time to go there. I'll head to the lounge."
        $ walk(loc_haven_lounge)
    elif not loc_cur.can_whore:
        pcm "Should head to somewhere a bit better."
        $ travel_whore_location()
    jump dis_haven_whore_start

label dis_haven_whore_start:
    show haven_wait at right2 with dissolve
    "I stand around making myself look available."
    $ working(20)
    if weightgen(player.allure, 1000):
        jump dis_haven_whore_customer
    else:
        call random_event_picker_haven_tombola_call from _call_random_event_picker_haven_tombola_call_5
        if not rand_choice == "random_event_none":
            $ renpy.scene()
            with dissolve
            jump expression rand_choice
    pcm "Hmmm, no one?"
    "I hang around some more hoping to attract someone."
    $ working(20)
    if weightgen(player.allure, 1000):
        jump dis_haven_whore_customer
    else:
        call random_event_picker_haven_tombola_call from _call_random_event_picker_haven_tombola_call_6
        if not rand_choice == "random_event_none":
            $ renpy.scene()
            with dissolve
            jump expression rand_choice
    pcm "C'mon. I don't want to be standing here all day..."
    $ working(20)
    if weightgen(player.allure, 1000):
        jump dis_haven_whore_customer
    else:
        call random_event_picker_haven_tombola_call from _call_random_event_picker_haven_tombola_call_7
        if not rand_choice == "random_event_none":
            $ renpy.scene()
            with dissolve
            jump expression rand_choice
    pcm "Ugh. No one at all?"
    hide haven_wait with dissolve
    jump travel

label dis_haven_whore_customer:
    $ dialouge = renpy.random.choice([
    "Looking for someone whore?",
    "Hey whore. Looking for a fucking?",
    "I'll have a go with ya girlie.",
    "Oh, let's have some fun."
    ])
    hav "[dialouge]"
    pc "Pay first."
    $ dialouge = renpy.random.choice([
    "Here ya go.",
    "This what I got.",
    "That all I have.",
    ])
    hav "[dialouge]"
    pc "It will do."
    hide haven_wait with dissolve
    jump haven_sex_repeatable_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
