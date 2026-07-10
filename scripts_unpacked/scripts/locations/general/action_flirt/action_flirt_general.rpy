init python:
    def flirt_guy_weight():
        base = 100
        if not t.timeofday == "night":
            base = base * 3
        if weather_var in (3,4):
            base = base * 2
        
        
        return weightgen(player.allure, int(base))

label action_flirt_test:
    "I do some flirting."
    jump whore_street_customer_pick_location

label flirt_street_checker:
    if loc(loc_motel_pinkroom):
        pcm "Why would I do that here?"
        jump travel
    elif player.cum_visible or player.looks_dirty():
        pcm "I'm kinda nasty. I doubt anyone will want to have fun."
        jump travel
    elif dis_cur == dis_haven:
        pcm "Yeah, I'm not doing that around here."
        jump travel
    elif dis(dis_walk):
        pcm "There is no one here, I should find somewhere better."
        jump travel
    elif loc_cur in dis_home.locs:
        pcm "Need to actually go out to do that."
        jump travel
    jump flirt_street_start


label flirt_street_start:
    $ tempname = renpy.random.choice([streetguy,streetman,streetpervert])
    $ quest_temp = None
    if not loc_cur.population >= 1:
        pcm "I should go somewhere better."
        $ travel_whore_location()
    $ show_whore_image()
    "[rlist.flirt_start_available]"
    $ working(10)
    if flirt_guy_weight():
        jump flirt_street_customer_pick_location
    else:
        call whore_street_no_customer_tombola from _call_whore_street_no_customer_tombola_3
    pcm "[rlist.flirt_start_waiting]"
    $ show_whore_image()
    "[rlist.flirt_start_available]"
    $ working(10)
    if whore_customer_weight():
        jump flirt_street_customer_pick_location
    else:
        call whore_street_no_customer_tombola from _call_whore_street_no_customer_tombola_4

    pcm "[rlist.flirt_start_waiting]"
    $ show_whore_image()
    "[rlist.flirt_start_available]"
    $ working(10)
    if whore_customer_weight():
        jump flirt_street_customer_pick_location
    else:
        call whore_street_no_customer_tombola from _call_whore_street_no_customer_tombola_5

    pcm "[rlist.flirt_start_waiting]"
    $ renpy.scene()
    with dissolve
    jump travel

label flirt_street_customer_pick_location:
    $ player.face_happy()
    $ male_npc_create()
    $ renpy.scene()
    show male_generic at right1
    with dissolve
    "[rlist.flirt_guy_start]"
    pc "[rlist.flirt_guy_pc_cont]."
    $ relax(3)
    tempname.name "[rlist.flirt_guy_man_cont]"
    $ relax(3)
    "[rlist.flirt_guy_wrapup]"
    pc "[rlist.flirt_guy_wrapup_pc]"
    jump whore_street_customer_pick_location_tombola
    tempname.name "[rlist.flirt_guy_wrapup_man]"
    jump whore_street_customer_pick_location_tombola
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
