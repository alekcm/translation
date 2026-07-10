label action_flyer_start:
    if loc(loc_market):
        if not "market_start" in quest_flyers.list:
            $ add_to_list(quest_flyers.list, "market_start")
            call market_flyer_firsttime from _call_market_flyer_firsttime

        $ quest_flyers.reward = 10
        $ quest_flyers.missionvar1 = "market"

    elif loc(loc_market_stall_milk):
        if not "milkmaid_outfit" in quest_flyers.list:
            $ add_to_list(quest_flyers.list, "milkmaid_outfit")
            call market_stall_milkstand_flyer_firsttime from _call_market_stall_milkstand_flyer_firsttime

        $ outfit_hucow()
        $ pc_dress_event("work", loc_mall_changingroom, force_dress=True)
        $ quest_flyers.reward = 10
        if player.showing:
            $ quest_flyers.reward += 10
        if player.lactating:
            $ quest_flyers.reward += 5
        $ quest_flyers.missionvar1 = "milkmaid"

    elif loc(loc_shop_funwear):

        if not "funwear_outfit" in quest_flyers.list:
            $ add_to_list(quest_flyers.list, "funwear_outfit")
            call funwear_shop_flyer_firsttime from _call_funwear_shop_flyer_firsttime
        else:
            $ outfit_funwear()
            $ pc_dress_event("work", loc_mall_changingroom, force_dress=True)

        $ quest_flyers.reward = 10
        if c.slutty:
            $ quest_flyers.reward += 5
        if c.cansee_breasts:
            $ quest_flyers.reward += 5
        if c.cansee_vagina:
            $ quest_flyers.reward += 10
        $ quest_flyers.missionvar1 = "funwear"

    elif loc(loc_motel_lobby):
        if not "motel_start" in quest_flyers.list:
            $ add_to_list(quest_flyers.list, "motel_start")
            call motel_receptionist_talk_flyerstart from _call_motel_receptionist_talk_flyerstart

        $ quest_flyers.reward = 15
        $ quest_flyers.missionvar1 = "motel"

    elif loc(loc_boardwalk):
        if not "sandy_start" in quest_flyers.list:
            $ add_to_list(quest_flyers.list, "sandy_start")
            call boardwalk_bikini_kiosk_flyers_first from _call_boardwalk_bikini_kiosk_flyers_first

        if not "swim" in tab_top:
            if (swim.inappropriate_check() and swim2.inappropriate_check()):
                hide sandy
                $ walk(loc_beach_locker_girls)
                $ walk(loc_beach_locker_girls_stall)
                pcm "Hmm, I don't really have a proper bikini to wear."
                call screen wardrobe_screen(shop_return=True)
                if (swim.inappropriate_check() and swim2.inappropriate_check()):
                    pcm "Maybe I should buy something off of [sandy.name]."
                    jump travel
            $ pc_dress_event("swim", [loc_beach_locker_girls, loc_beach_locker_girls_stall], loc_beach_locker_girls)

        $ quest_flyers.reward = 10
        if c.exposed:
            $ quest_flyers.reward += 10
        elif c.slutty:
            $ quest_flyers.reward += 5
        $ quest_flyers.missionvar1 = "sandy"
    $ quest_flyers.workcycle = 0


    $ quest_temp = quest_flyers
    jump action_flyer_event_picker

label action_flyer_event_picker:
    if not quest_flyers.workcycle or not flyer_locations:
        $ flyer_locations_picker()
    if renpy.count_displayables_in_layer("master"):
        $ renpy.scene()
        with dissolve
    $ player.reset_sex_status(True)
    $ player.face_normal()
    if pub_waitress.workcycle and dis(dis_pub):
        jump pub_waitress_work_picker
    if quest_flyers.workcycle >= 4:

        jump action_flyer_event_done_change
    else:

        $ player.flyer()
        $ walk(renpy.random.choice(flyer_locations))
        $ quest_flyers.workcycle += 1
        $ flyer_area()
        jump action_flyer_event_picker_tombola

label action_flyer_event_picker_tombola:

    $ player.face_happy()
    pc "[rlist.flyering_area_dialogue]"

    jump expression WeightedChoice([
    
    
    ("action_flyer_event_general_1", 100),
    ("action_flyer_event_general_2", 100),
    ("action_flyer_event_general_3", 100),
    ("action_flyer_event_general_4", 100),
    ("action_flyer_event_general_5", 100),
    ("action_flyer_event_general_6", 100),
    
    
    

    
    ("action_flyer_event_milk_1", If(quest_flyers.missionvar1 == "milkmaid", 100, 0)),
    ("action_flyer_event_milk_2", If(quest_flyers.missionvar1 == "milkmaid", 100, 0)),
    ("action_flyer_event_milk_3", If(quest_flyers.missionvar1 == "milkmaid", 100, 0)),

    
    ("action_flyer_event_motel_1", If(quest_flyers.missionvar1 == "motel", 100, 0)),
    ("action_flyer_event_motel_2", If(quest_flyers.missionvar1 == "motel", 100, 0)),
    ("action_flyer_event_motel_3", If(quest_flyers.missionvar1 == "motel" and player.allure > 200, 10, 0)),
    ("action_flyer_event_motel_4", If(quest_flyers.missionvar1 == "motel", 100, 0)),
    ("action_flyer_event_motel_5", If(quest_flyers.missionvar1 == "motel", 100, 0)),
    ("action_flyer_event_motel_6", If(quest_flyers.missionvar1 == "motel", 100, 0)),
    ("action_flyer_event_motel_7", If(quest_flyers.missionvar1 == "motel", 100, 0)),
    ("action_flyer_event_motel_8", If(quest_flyers.missionvar1 == "motel", 100, 0)),

    
    ("action_flyer_event_unique_meet_mira", If(mira_can_discover_highway(), 1, 0)),

    ])

label action_flyer_event_testing_1:
    "This is a test event. Locations might be a bit weird right now."
    pc "I am handing out flyers. yay."
    "And now it ends."
    jump action_flyer_event_picker

label action_flyer_event_done_change:
    $ quest_flyers.work()
    $ player.add_money(quest_flyers.reward)

    if player.looks_dirty():
        pcm "I need to clean up before handing out anything more."

    elif quest_flyers.missionvar1 == "sandy" and not sandy_here(loc_boardwalk):
        pcm "Her kiosk is closed now so I'd better call it a day."
    elif quest_flyers.missionvar1 == "market" and not t.hour in workhours:
        pcm "The market is closed so I had better call it a day."
    elif quest_flyers.missionvar1 == "milkmaid" and not hucow_here(loc_market_stall_milk):
        pcm "The milk stall is closed so I had better call it a day."
    elif quest_flyers.missionvar1 == "funwear" and loc_shop_funwear.closed():
        pcm "The shop is closing so I should call it a day."
    elif not player.tired < 20:
        pcm "Should I keep handing out flyers?"
        menu:
            "Keep handing out flyers":
                jump action_flyer_event_picker
            "Not now":
                pcm "Think I'll call it a day."
    else:
        pcm "I'm pretty tired. I think I'll call it a day"


    if quest_flyers.missionvar1 == "market":
        $ walk(loc_market)
        pc "That's me for now."
        $ player.hands_reset()
        "I hand back the fliers and go about my day."

    elif quest_flyers.missionvar1 == "funwear":
        $ walk(loc_revel_backstreet)
        $ walk(loc_shop_funwear, trans=False)
        show fun_girl at right1 with dissolve
        pc "That's me for now."
        $ player.left_hand = ""
        fun_girl.name "Okay."
        hide fun_girl with dissolve
        $ pc_dress_event("party", loc_mall_changingroom, loc_shop_funwear)

    elif quest_flyers.missionvar1 == "milkmaid":
        $ walk(loc_market_stall_milk, trans=False)
        show hucow at right1 with dissolve
        pc "That's me for now."
        $ player.left_hand = ""
        hucow.name "Mooo!"
        hide hucow with dissolve
        $ pc_dress_event("daily", loc_mall_changingroom, loc_market_stall_milk)

    elif quest_flyers.missionvar1 == "motel":
        $ walk(loc_motel_lobby, trans=False)
        show motel_recep at right1 with dissolve
        pc "That's me for now."
        $ player.left_hand = ""
        motel_recep.name "Okay."
        hide motel_recep with dissolve

    if quest_flyers.missionvar1 == "sandy":
        $ walk(loc_boardwalk)
        show sandy at right1 with dissolve
        pc "That's me for now."
        $ player.left_hand = ""
        sandy.name "Thanks [name]."
    else:
        $ player.left_hand = ""
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
