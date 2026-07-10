

label robin_sex_picker:
    "Temp label for offering sex with robin."
    "Not written yet."
    jump robin_talk_end
label robin_bus_picker:
    "Temp label for going on a bus ride with robin."
    "Not written yet."
    jump robin_talk_end

label robin_talk_picker:
    if not "robin_meet_chain" in robin.dict:
        $ robin.dict["robin_meet_chain"] = 0
    if not "robin_talk_bus_chain" in robin.dict:
        $ robin.dict["robin_talk_bus_chain"] = 0
    if not "robin_talk_pub_chain" in robin.dict:
        $ robin.dict["robin_talk_pub_chain"] = 0
    if not "robin_talk_soccersex_chain" in robin.dict:
        $ robin.dict["robin_talk_soccersex_chain"] = 0
    if not "robin_talk_sexgossip_chain" in robin.dict:
        $ robin.dict["robin_talk_sexgossip_chain"] = 0
    if not "robin_talk_sexobject_chain" in robin.dict:
        $ robin.dict["robin_talk_sexobject_chain"] = 0
    if not "robin_talk_scav_chain" in robin.dict:
        $ robin.dict["robin_talk_scav_chain"] = 0
    if not "robin_talk_sexobject_last_outing" in robin.dict:
        $ robin.dict["robin_talk_sexobject_last_outing"] = 0
    if not "robin_talk_lesbian_times" in robin.dict:
        $ robin.dict["robin_talk_lesbian_times"] = 0
    if not "robin_talk_oskarsexrent_chain" in robin.dict:
        $ robin.dict["robin_talk_oskarsexrent_chain"] = 0
    if not "robin_talk_oskarsexseen_chain" in robin.dict:
        $ robin.dict["robin_talk_oskarsexseen_chain"] = 0
    if not "robin_naked_talk" in robin.dict:
        $ robin.dict["robin_naked_talk"] = 0

    if t.time_from_to(00.00, 06.00) and loc(loc_bedroom_robin):
        pcm "I should let her sleep."
        jump travel
    if oskar_here():


        pc "Dirty slut!"
        robin.name "Shoo!"
        jump travel
    elif "common_passout" in robin.list and loc(loc_common):
        if robin.love >= 100:
            pcm "Someone has been drinking too much..."
            menu:
                "Wake her and shoo her to bed":
                    pc "[robin.name]! Get to bed."
                    if numgen(0,5):
                        $ dialouge = renpy.random.choice([
                        "Ugh... Go away!",
                        "Ugh Abfoe Unng Asaa.",
                        "...",
                        "Noooo..."
                        ])
                        robin.name "[dialouge]"
                        pc "Ugh. She's too drunk..."
                        jump travel
                    else:
                        robin.name "Ugh! Huh?"
                        show robin worried at right1 with dissolve
                        robin.name "Uhhhh..."
                        $ remove_from_list(robin.list, "common_passout")
                        hide robin with dissolve
                        jump travel
                "Leave her be":
                    pcm "Eh, I'll leave her to sleep."
                    jump travel
        pcm "Looks like someone drank a bit much..."
        jump travel

    show robin at right1 with dissolve

    jump expression WeightedChoice([
    ("robin_talk_meet_intro_" + str(robin.dict["robin_meet_chain"]), If(renpy.has_label("robin_talk_meet_intro_" + str(robin.dict["robin_meet_chain"])) and dis(dis_home), 1000, 0)),
    
    ("robin_talk_naked_first", If(c.exposed and not "naked_talk" in robin.list and not tab_top in "swim", 5000, 0)),

    ("robin_talk_bus_" + str(robin.dict["robin_talk_bus_chain"]), If(renpy.has_label("robin_talk_bus_" + str(robin.dict["robin_talk_bus_chain"])) and (robin.dict["robin_talk_pub_chain"] > 0 and (robin.love >= (robin.dict["robin_talk_pub_chain"] * 10) or robin.love >= 100)) and t.day > 4 and (t.day >= (robin.dict["robin_talk_bus_chain"] * 2) or t.day > 25), 100, 0)),

    ("robin_talk_pub_chain_" + str(robin.dict["robin_talk_pub_chain"]), If(pub_waitress.timesworked and renpy.has_label("robin_talk_pub_chain_" + str(robin.dict["robin_talk_pub_chain"])) and robin.love >= 10 and (robin.love >= (robin.dict["robin_talk_pub_chain"] * 10) or robin.love >= 100) and pub_waitress.timesworked >= (robin.dict["robin_talk_pub_chain"] * 3), 100, 0)),
    
    ("robin_talk_soccerboys_ask", If(t.day in irange(4, 10) and not "soccerboys_ask_know" in robin.list, 100, 0)),
    ("robin_talk_soccerboys_tell", If(t.day > 10 and "soccerboys_ask_know" in robin.list and not "soccerboys_ask_tell" in robin.list, 100, 0)),
    
    ("robin_talk_soccersex_chain_" + str(robin.dict["robin_talk_soccersex_chain"]), If(renpy.has_label("robin_talk_soccersex_chain_" + str(robin.dict["robin_talk_soccersex_chain"])) and ("soccerboys_knows_pc_sex" in robin.list or (player.has_perk([perk_slut, perk_sucu, perk_freeuse, perk_exhibitionist, perk_broken]) and any([drake.sex, nate.sex, dan.sex]) and robin.love > 60)), 100, 0)),
    ("robin_talk_soccersextold", If("soccerboys_told_sex" in robin.list and not "soccerboys_can_sex" in robin.list, 100, 0)),

    ("robin_talk_beachvball_ask", If(t.day in irange(4, 10) and not "beachvball_ask_know" in robin.list, 100, 0)),
    ("robin_talk_beachvball_tell", If(t.day > 10 and "beachvball_ask_know" in robin.list and not "beachvball_ask_tell" in robin.list, 100, 0)),
    
    ("robin_talk_sexgossip_chain_" + str(robin.dict["robin_talk_sexgossip_chain"]), If(renpy.has_label("robin_talk_sexgossip_chain_" + str(robin.dict["robin_talk_sexgossip_chain"])) and robin.love >= 100 and "pc_knows_likes_watching" in robin.list, 100, 0)),
    
    ("robin_talk_sexobject_chain_" + str(robin.dict["robin_talk_sexobject_chain"]), If(renpy.has_label("robin_talk_sexobject_chain_" + str(robin.dict["robin_talk_sexobject_chain"])) and robin.love >= 100 and "pc_knows_likes_watching" in robin.list and "pc_know_want_sexstories" in robin.list and player.has_perk([perk_bimbo, perk_whore, perk_slut, perk_sucu]), 100, 0)),
    ("robin_talk_sexobject_bought_intro", If(inv.qty(item_robin_package) and dis(dis_home) and t.timeofday == "night", 300, 0)),
    ("robin_talk_sexobject_bought_aftermath", If(robin.dict["robin_talk_sexobject_last_outing"] and (t.day + 1) > robin.dict["robin_talk_sexobject_last_outing"] and not robin.isslut, 300, 0)),
    

    ("robin_talk_scav_intro", If(quest_scav.active and not robin.dict["robin_talk_scav_chain"], 300, 0)),
    ("robin_talk_scav_return", If(quest_scav.active and robin.dict["robin_talk_scav_chain"] > (t.day + 2) and not "is_scavver" in robin.list, 300, 0)),

    ("robin_talk_pregnant_discover", If(robin.days_pregnant > (global_pregnancy_length * 0.3) and not "seen_pregnant_" + str(robin.preg) in robin.list, 5000, 0)),

    ("quest_mira_missing_robin_mira_ask", If(log.interactive("mira_missing_01") and not "asked_about_mira" in robin.list and dis(dis_school), 5000, 0)),

    
    ("robin_talk_oskarsexrent_chain_" + str(robin.dict["robin_talk_oskarsexrent_chain"]), If(renpy.has_label("robin_talk_oskarsexrent_chain_" + str(robin.dict["robin_talk_oskarsexrent_chain"])) and (robin.love >= 50 or robin.isslut) and "rent_sex_offer_day" in oskar.dict and oskar.dict["rent_sex_offer_day"] > 0 and t.day >= (oskar.dict["rent_sex_offer_day"] + 4) and not oskar.dead, 100, 0)),
    ("robin_talk_oskarsexseen_chain_" + str(robin.dict["robin_talk_oskarsexseen_chain"]), If(renpy.has_label("robin_talk_oskarsexseen_chain_" + str(robin.dict["robin_talk_oskarsexseen_chain"])) and ("oskar_sex_seen" in robin.list or "oskar_sex_watched" in robin.list) and not oskar.dead, 100, 0)),
    ("robin_talk_oskar_dead_know", If(oskar.days_dead >= 10 and "dead_poisoned" in oskar.list and not "oskar_dead_know" in robin.list, 500, 0)),

    ("robin_talk_bitching_aftermath", If("done_bitching" in robin.list, 5000, 0)),
    
    ("robin_talk_nudevball_tell", If(not "nudebeachvball_ask_know" in robin.list and "nude_vball" in loc_beach_hangout.list and robin.love >= 90, 100, 0)),
    ("robin_talk_nudevball_tell_pc", If(not "nudebeachvball_ask_know" in robin.list and not "nude_vball" in loc_beach_hangout.list and robin.love >= 90 and t.day > 30 and (robin.isslut or "pc_know_want_bussex" in robin.list or "pc_knows_likes_watching" in robin.list), 100, 0)),

    ("robin_talk_subject", 20),     
    ])



label robin_talk_end:
    $ relax(20, robin)
    $ dialouge = renpy.random.choice([
    "I hang out talking and joking about random stuff.",
    "I hang out for a while chatting and joking around about random topics.",
    "We hang out chatting and laughing about whatever comes up.",
    "We chat and have a bit of a laugh about random stuff."
    ])
    "[dialouge]"
    if t.hour == 9 and t.wkday in weekdays and loc(dis_home.locs):
        robin.name "I'm heading off to school now? You coming?"
        menu:
            "Yeah, let's go":
                jump robin_goto_school
            "No, you go ahead":

                robin.name "Ok, cya."
    elif loc(loc_bedroom_robin) and oskar_here():
        show oskar at left4 with dissolve
        oskar.name "[robin.name]. Let's have a chat."
        robin.name "Err, okay. See you in a bit [name]."
        pc "Sure."
        hide oskar
        hide robin
        $ walk(loc_common)
        pcm "..."
        jump travel
    hide robin with dissolve
    jump travel

label robin_goto_school:
    if not "school" in tab_top:
        pc "Let me change first."
        $ pc_dress_event("school", loc_bedroom, loc_stairwell)
        pc "Let's go."
    $ walk(loc_stairwell, trans=False)
    show robin at left1 with dissolve
    $ walk(loc_busstop_residential)
    robin.name "Here it comes."
    hide robin with dissolve
    $ walk(loc_bus_interior, trans=False)
    show robin at right6 with dissolve
    jump robin_bus_goto_school_event_picker

label robin_goto_school_arrive:
    if pc_lost_clothes():
        "I manage to grab back the clothes that the perverts took from me."
        pcm "Quickly before I need to get off..."
        $ pc_dress()
    $ relax(10, robin)
    pc "Our stop is here. Come on, let's go."
    if not renpy.showing("robin"):
        $ renpy.scene()
        show robin at right6
        with dissolve
    robin.name "Yup."
    $ walk(loc_busstop_school)
    $ walk(loc_school)
    robin.name "See you in there."
    hide robin with dissolve
    jump travel

label robin_goto_home:
    if dis(dis_school):
        if tab_top == ["temp_outfit", "swim", "home", "work"] or c.nude:
            pc "I'll dress up first."
            $ pc_dress_event("party", loc_school_locker_old, loc_school)
        else:
            $ walk(loc_school, trans=False)
        show robin at left1 with dissolve
        $ walk(loc_busstop_school)
    elif dis(dis_lake):
        if any(clothes in ["temp_outfit", "swim", "home", "work"] for clothes in tab_top) or c.nude:
            pc "I'll dress up first."
            $ pc_dress_event("party", loc_beach_locker_girls, loc_lake)
        else:
            $ walk(loc_lake, trans=False)
        show robin at left1 with dissolve
        $ walk(loc_busstop_lake)
    elif dis(dis_pub):
        if any(clothes in ["temp_outfit", "swim", "home", "work"] for clothes in tab_top) or c.nude:
            pc "I'll dress up first."
            $ pc_dress_event("party", loc_pub_changingroom, loc_revel)
        else:
            $ walk(loc_revel, trans=False)
        show robin at left1 with dissolve
        $ walk(loc_busstop_revel)
    elif dis(dis_motel):
        if any(clothes in ["temp_outfit", "swim", "home", "work"] for clothes in tab_top) or c.nude:
            pc "I'll dress up first."
            $ pc_dress_event("party", loc_cur, loc_motel)
        else:
            $ walk(loc_motel, trans=False)
        show robin at left1 with dissolve
        $ walk(loc_busstop_truckstop)

    robin.name "Here it comes."
    hide robin with dissolve
    $ walk(loc_bus_interior, trans=False)
    show robin at right6 with dissolve
    jump robin_bus_goto_home_event_picker

label robin_goto_home_arrive:
    if pc_lost_clothes():
        "I manage to grab back the clothes that the perverts took from me."
        pcm "Quickly before I need to get off..."
        $ pc_dress()
    $ relax(10, robin)
    pc "Our stop is here. Come on, let's go."
    if not renpy.showing("robin"):
        $ renpy.scene()
        show robin at right6
        with dissolve
    robin.name "Yup."
    $ walk(loc_busstop_residential)
    $ walk(loc_stairwell)
    robin.name "See you in there."
    hide robin with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
