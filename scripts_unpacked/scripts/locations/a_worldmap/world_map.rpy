label map_screen_unknown_busstop:
    pcm "I have no idea where the bus stop is. I need to look around the area first."
    jump travel

label map_screen:
    if log.interactive("quest_homeless_start_01") or log.interactive("quest_homeless_start_02"):

        if log.interactive("quest_homeless_start_01"):
            pcm "I need to look around here first and see if I can see [emile.name]."
        else:
            pcm "I need to find somewhere to stay first before I explore more of the city."
        jump travel

    if loc_cur.home_location or loc_cur.name.endswith("shower") or loc_cur.name.endswith("bathroom") or dis(dis_home):

        call leave_house_checks_call from _call_leave_house_checks_call_1
    elif dis(dis_lake) and ("swim" in tab_top or "temp" in tab_top or "work" in tab_top):
        pcm "I should change before getting the bus."
        $ pc_dress_event(If(t.timeofday == "day", "daily", "party"), loc_beach_locker_girls)
    elif "temp" in tab_top and c.nude:
        pcm "I should dress up before getting on the bus."
        if check_if_isolated() or loc_cur.inside:
            $ pc_dress_slow(If(t.timeofday == "day", "daily", "party"))
        else:
            $ pc_dress_event(If(t.timeofday == "day", "daily", "party"), where=loc_cur.isolate_loc, where2=loc_cur)
    elif c.inappropriate and not perk_exhib_total_value() > 200:
        pcm "I really should dress properly before getting on the bus..."
    $ travel_walk(loc_cur.district.busstop, 8)
    menu:
        "Travel to the residential area" if not (dis(dis_residential) or dis_residential.locked):
            $ want_loc = loc_residential
        "Travel to the lake" if not (dis(dis_lake) or dis_lake.locked):
            $ want_loc = loc_lake
        "Travel to the academy" if not (dis(dis_school) or dis_school.locked):
            $ want_loc = loc_school
        "Travel to Revel street" if not (dis(dis_revel) or dis_revel.locked):
            $ want_loc = loc_revel
        "Travel to the checkpoint" if not (dis(dis_checkpoint) or dis_checkpoint.locked):
            $ want_loc = loc_checkpoint
        "Travel to the truck stop area" if not (dis(dis_truckstop) or dis_truckstop.locked):
            $ want_loc = loc_truckstop
        "Never mind":
            jump travel
    jump bus_travel

label bus_travel_end:
    if event_end_interrupt_label:
        jump expression event_end_interrupt_label

    $ relax(25)
    if pc_lost_clothes():
        if not numgen(0,5):
            pcm "Fuck, what did these cunts do with my clothes?"
            pcm "Ugh. Shit."
            if c.nude:
                pcm "Pay no attention to the naked idiot getting off the bus."
            elif c.cansee_breasts:
                pcm "Pay no attention to the girl with her tits out."
            elif c.cansee_ass:
                pcm "Pay no attention to the bare arsed girl."
            else:
                pcm "Pretend nothing is wrong. Don't look at me..."
        else:
            "I manage to grab back the clothes that the perverts took from me."
            pcm "Quickly before I need to get off..."
            $ pc_dress()
    $ player.face_normal()
    if t.hour in rushhour:
        $ dialouge = renpy.random.choice([
        "My stop is coming up so I shove my way to the exit so I can get off.",
        "I push my way to the exit so I don't miss my stop.",
        "I squeeze my way through the crowd to the bus doors and prepare to get off.",
        ])
        "[dialouge]"
        with vpunch
        $ dialouge = renpy.random.choice([
        "Coming through.",
        "Excuse me.",
        "Move!",
        "Sorry, let me past.",
        "Sorry, sorry.",
        "Ugn!",
        ])
        pc "[dialouge]"
    elif t.hour in workhours:
        $ dialouge = renpy.random.choice([
        "My stop is coming up so I make my way to the exit so I can get off.",
        "I work my way to the exit so I don't miss my stop.",
        "I squeeze my way through the crowd to the bus doors and prepare to get off.",
        ])
        "[dialouge]"
        $ dialouge = renpy.random.choice([
        "Coming through.",
        "Excuse me.",
        "Move!",
        "Sorry, let me past.",
        "Sorry, sorry.",
        "Ugn!",
        ])
        pc "[dialouge]"
    else:
        $ dialouge = renpy.random.choice([
        "My stop is here so I head to the doors.",
        "This is my stop so I head to the exit.",
        "I see my stop so I go to the exit.",
        ])
        "[dialouge]"

    if player.drunk > 100:
        if numgen(0,1000) < player.drunk:
            $ walk(renpy.random.choice(busstops))
            pause 0.3
            $ walk(loc_cur.district.hub)
            if not loc_cur == want_loc:
                $ player.face_worried()
                pcm "..."
                pcm "Errr..."
                pcm "This isn't my stop..."
                pcm "Fuck!"
                jump travel_arrival


    $ walk(want_loc.district.busstop, trans=False)

    $ renpy.scene()
    with dissolve
    pause 0.3
    $ walk(want_loc)
    jump travel_arrival
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
