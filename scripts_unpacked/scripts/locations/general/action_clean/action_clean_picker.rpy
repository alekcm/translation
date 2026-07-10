label action_clean_start:
    if loc(loc_stairwell) and not "apron" in quest_rent.list:
        jump oskar_clean_event_apron_give
    elif dis(dis_pub) and wardrobe.qty(item_outfit_6) and pub_waitress.timesworked:
        $ NullAction()
    elif "maid" in quest_rent.list and not wardrobe.qty(item_outfit_20) and dis(dis_home_area):
        pcm "[oskar.name] wanted me to wear something better than the overalls."
        jump travel
    elif loc(loc_motel):
        if not "cleaned_first" in loc_motel_lobby.list:
            jump motel_cleaner_first
        elif not wardrobe.qty(item_outfit_20):
            pcm "I need to buy a maid dress before I can clean here."
            jump travel
    elif not (wardrobe.qty(item_outfit_20) or wardrobe.qty(item_outfit_19)):
        pcm "I don't have anything to change into and don't want to ruin my own clothes."
        jump travel

    $ clean_locations_picker()
    $ quest_cleaner.workcycle = 0
    $ quest_rent.workcycle = 0


    $ quest_temp = quest_cleaner
    $ dialogue = WeightedChoice([
    ("Right then...", 1),
    ("Best get to work.", 1),
    ("Rent's not going to pay it's self.", If(loc_cur == loc_stairwell, 1, 0)),
    ("Better get to it.", 1),
    ])
    pcm "[dialogue]"
    $ loc_cur.clean_last = t.minutes_total

    if dis(dis_home_area):
        if wardrobe.qty(item_outfit_20) and (not wardrobe.qty(item_outfit_19) or "maid" in quest_rent.list or player.isslut or player.iswhore or player.confidence > 40):
            $ maid_outfit_set()
        else:
            $ cleaner_outfit()

        if loc_office_ll.open():
            if oskar_here(loc_office_ll):
                $ walk(loc_office_ll)
                pc "I'm going to change and do some cleaning."
                oskar.name "Okay."
                $ pc_dress_event("work", loc_office_ll_back)
                if not "maid" in quest_rent.list and (quest_rent.timesworked >= 8 or c.outfit == 20):
                    jump oskar_clean_event_maid_give
            else:
                $ pc_dress_event("work", loc_office_ll_back)
        else:
            $ pc_dress_event("work", loc_bedroom)
    elif dis(dis_pub):
        if not pub_waitress.timesworked:
            $ cleaner_outfit()
        else:
            $ pub_outfit()
        $ walk(loc_pub_changingroom)
        $ pc_striptease()
        pause 0.5  
        $ pc_dress_event("work", loc_pub_changingroom, loc_pub_changingroom)
    elif dis(dis_motel):
        $ maid_outfit_set()
        $ pc_dress_event("work", loc_motel_room, loc_motel)

    $ clean_locations_picker()
    jump action_clean_event_picker


label action_clean_event_picker:
    if not quest_cleaner.workcycle:
        $ clean_locations_picker()
    if renpy.count_displayables_in_layer("master"):
        $ renpy.scene()
        with dissolve
    $ player.reset_sex_status(True)
    $ player.face_normal()
    if pub_waitress.workcycle and dis(dis_pub):
        jump pub_waitress_work_picker
    if quest_cleaner.workcycle >= 4:
        if item_picker(False):
            pcm "Looks like I managed to find some junk."

        jump action_clean_event_done_change
    else:

        $ walk(renpy.random.choice(clean_locations))


        $ quest_cleaner.workcycle += 1
        if dis(dis_home_area) or dis(dis_home):
            $ quest_rent.workcycle += 1
        $ clean_area()
        jump action_clean_event_picker_tombola

label action_clean_event_picker_tombola:

    jump expression WeightedChoice([
    
    
    ("action_clean_event_general_1", 50),

    ("action_clean_event_public_1", If(loc_cur.population == 2, 100, 0)),
    ("action_clean_event_public_2", If(loc_cur.population == 2, 100, 0)),  
    ("action_clean_event_public_3", If(loc_cur.population == 2, 100, 0)),
    ("action_clean_event_public_4", If(loc_cur.population == 2, 100, 0)),
    ("action_clean_event_public_5", If(loc_cur.population == 2, 100, 0)),

    ("action_clean_event_secluded_1", If(loc_cur.population == 1 or loc_cur.mens_room, danger_weight() / 2, 0)),
    ("action_clean_event_secluded_2", If(loc_cur.population == 1 or loc_cur.mens_room, danger_weight() / 2, 0)),
    

    
    ("action_clean_event_toilet_1", If("toilet" in loc_cur.name, 100, 0)),
    ("action_clean_event_toilet_2", If("toilet" in loc_cur.name, 100, 0)),
    ("action_clean_event_bathroom_1", If("toilet" in loc_cur.name or "bathroom" in loc_cur.name, 100, 0)),

    
    ("action_clean_event_bedroom_1", If(loc(loc_bedroom), 100, 0)),

    
    ("action_clean_event_pub_quiet_1", If(loc(loc_pub), 100, 0)),
    ("action_clean_event_pub_quiet_2", If(loc(loc_pub), 100, 0)),
    ("action_clean_event_pub_quiet_3", If(loc(loc_pub), 100, 0)),

    
    ("action_clean_event_robin_1", If(loc(loc_bedroom_robin) and robin_here(), 100, 0)),
    ("action_clean_event_robin_2", If(loc(loc_bedroom_robin) and robin_here(), 100, 0)),
    ("action_clean_event_robin_3", If(robin_here(), 100, 0)),

    
    ("action_clean_event_oskar_1", If(oskar_here() and not oskar.naughty, 100, 0)),
    ("action_clean_event_oskar_2", If(oskar_here() and oskar.sex and c.skirt, 100, 0)),

    
    ("action_clean_event_motel_1", If(loc([loc_motel_room, loc_motel_room2]), 100, 0)),
    ("action_clean_event_motel_2", If(loc([loc_motel_room, loc_motel_room2]), 100, 0)),
    ("action_clean_event_motel_3", If(loc([loc_motel_room, loc_motel_room2]), 100, 0)),
    ("action_clean_event_motel_4", If(mira_can_discover_highway(), 1, 0)),
    ("action_clean_event_secluded_1", If(loc([loc_motel_room, loc_motel_room2]), 100, 0)),
    ("action_clean_event_secluded_2", If(loc([loc_motel_room, loc_motel_room2]), 100, 0)),
    ("action_clean_event_motel_flyeroffer", If(loc(loc_motel_lobby) and not "motel_offer" in quest_flyers.list, 1000, 0)),
    ])

label action_clean_event_done_change:
    $ quest_cleaner.reward = 20
    if c.outfit in (6, 20):
        $ quest_cleaner.reward = 30
    $ quest_cleaner.work()

    if dis(dis_home_area) or dis(dis_home):
        $ quest_rent.work()
    if dis(dis_home_area) or dis(dis_home):
        if loc_office_ll.open():
            $ walk(loc_office_ll)
            if oskar_here():
                pc "That's me done [oskar.name]. I'll go change."
                $ dialouge =  WeightedChoice([
                ("Right.", 10),
                ("Okay.", 10),
                ("Mmm.", 10),
                ("Right. I'll put it towards your rent.", If(rent_total_owed(), 100, 0)),
                ("Okay. You are paid up so here you go.", If(not rent_total_owed(), 100, 0)),
                ])
                oskar.name "[dialouge]"

            $ pc_dress_event("daily", loc_office_ll_back, loc_office_ll)
            if loc_office_ll.closed():
                $ walk(loc_stairwell)
        else:
            $ pc_dress_event("daily", loc_bedroom, loc_bedroom)

        $ rent_workoff(quest_cleaner.reward)

    elif dis(dis_pub):
        $ player.add_money(quest_cleaner.reward)
        if not pub_waitress.can_work() and loc_pub.open():
            pcm "Should I keep cleaning?"
            menu:
                "Clean up some more":
                    jump action_clean_event_picker
                "Not now":
                    $ NullAction()
        elif pub_waitress.can_work() and pub_waitress.timesworked:
            $ walk(loc_pub_changingroom)
            pcm "Should I work a pub shift now that I am done cleaning?"
            menu:
                "Work a pub shift":
                    jump pub_waitress_picker
                "Not now":
                    $ NullAction()
        $ pc_dress_event("daily", loc_pub_changingroom, loc_pub_changingroom)
        if not pub_waitress.timesworked:
            $ walk(loc_pub)

    elif dis(dis_motel):
        $ player.add_money(quest_cleaner.reward)
        if not player.tired < 20:
            pcm "Should I keep cleaning?"
            menu:
                "Clean up some more":
                    jump action_clean_event_picker
                "Not now":
                    $ NullAction()

        $ pc_dress_event("daily", loc_motel_room, loc_motel)
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
