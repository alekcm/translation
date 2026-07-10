label random_event_picker_school_tombola:
    if rachel_exhib_stripping_events_trigger():
        jump expression "rachel_talk_exhib_inside_talk_" + str(rachel.dict["rachel_exhib_inside_talk"])
    elif not school_open_hours():
        jump random_event_picker_school_night_tombola
    elif loc(loc_school_toilet_boys):
        jump random_event_school_boys_toilet
    elif loc(loc_school_locker_boys):
        "Can't actually enter here yourself right now. but I am adding this for the future."
        jump travel
    elif loc([loc_school_pool, loc_school_locker_girls, loc_school_toilet_girls, loc_school_locker_old, loc_school_field_back, loc_school_library, loc_school_sewroom, loc_school_chem, loc_school_darkroom]):

        jump travel
    else:

        $ rand_choice = WeightedChoice([
        ("random_event_school_normal", 300),
        ("random_event_school_desire", player.check_horny(extreme=True)), 
        ("random_event_school_allure", player.allure),
        ("random_event_school_highconf", If (player.confidence > 40, player.confidence, 0)),
        ("random_event_school_lowconf", If (player.confidence < 30, 100 - player.confidence, 0)),
        
        ("random_event_school_fitness", If (player.fitness >= 40 and not player.pregnancy > 0, player.fitness, 0)),
        ("random_event_school_fat", If (player.isfat or player.pregnancy == 1, 100, 0)),
        ("random_event_school_lowmood", If (player.mood < 30, 100, 0)),
        
        ("random_event_school_weather", If (outside, 50, 0)),
        
        ("random_event_school_rushhour", If (t.hour in rushhour, 25, 0)),
        ("random_event_school_hungry", If (player.hunger < 20, 300, 0)),
        ("random_event_school_dirty", If (player.hygiene < 20, 500, 0)),
        ("random_event_school_drunk", If (player.drunk > 60, player.drunk * 5, 0)),
        ("random_event_school_pregnant", If (player.pregnant > 1, 200, 0)),
        ("random_event_school_cum", If (player.cum_visible, 400, 0)),
        ("random_event_school_whore", If (player.iswhore, 50, 0)),
        ("random_event_school_slut", If (player.isslut, 50, 0)),
        ("random_event_school_broken", If (player.isbroken, 50, 0)),
        ("random_event_generic_exhib", If(player.covering, 2000, 0)),

        
        ("random_event_school_photo", If (school_photo_shoots_done > 2, 50, 0)),
        
        ("school_photo_intro_return", If (log.completed("Promotional material") and not quest_photo.active and t.day >= quest_photo_intro.workedtoday+3, 1000, 0)),

        
        ("school_field_soccer_hangout_bully_ask_remove_where", If (school_soccer_bully_vanish() and not school_soccer_quest_bully_remove["vanished_field"] and loc_cur == loc_school_field, 50000, 0)),
        
        ("random_event_school_bully", If (school_bully_can_bully() and not (school_bully_quest_bully_cass_target or school_bully_quest_bully_soccer_boys_remove), (100 - player.confidence) * 5, 0)),
        ("school_bully_cass_event_tombola", If (t.wkday in weekdays and school_bully_can_bully() and school_bully_quest_bully_cass_target and not cass.dead, If(inv.qty(item_beer_poison) >= 4, 1000, 100), 0)),
        ("school_bully_removed_event_tombola", If ((school_bully_quest_bully_soccer_boys_remove and t.day - school_soccer_quest_bully_remove["vanished_date"] <= 15) or ("took_poison" in shane.dict and t.day - shane.dict["took_poison"] >= 15 and shane.dead), 30, 0)),
        ("school_bully_removed_event_chain_" + str(school_soccer_quest_bully_vanished_stage), If (school_soccer_quest_bully_vanished_checker(), 500, 0)),
        ("school_bully_poisoned_event_tombola", If ("took_poison" in shane.dict and t.day - shane.dict["took_poison"] >= 6 and not shane.dead, 300, 0)),

        
        ("dani_postdance_company_conv_followup", If (dani.active and "dance_went_alone_followup" in dani.conversation_topics and school_people_present() and school_dance_quest_show_count == 9,1000,0)),

        
        ("dance_party_academy_meetup_start", If (any([rachel_here(loc_school_gym), dani_here(loc_school_gym), svet_here(loc_school_gym)]) and loc(loc_school_gym) and log.interactive("quest_dancevip_03"), 50000, 0)),

        
        ("dani_freakout_event_tell_troupe_picker", If (any([rachel_here(loc_school_gym), dani_here(loc_school_gym), svet_here(loc_school_gym)]) and loc(loc_school_gym) and dani.dead and not "dead_told_troupe" in dani.list, 50000, 0)),
        ("dani_freakout_event_tell_troupe_ana_alone", If (dis(dis_school) and anabel_here(dis_school) and dani.dead and "dead_told_troupe" in dani.list and not "dead_anabel_knows" in dani.list, 300, 0)),

        
        
        ("quest_mira_missing_cass_approach", If (not mira.dead and "kidnap_date" in mira.dict and ((t.day + 5) >= (mira.dict["kidnap_date"] + 5)) and not quest_mira_missing.active, 1000, 0)),
        ("quest_mira_missing_pc_knows", If (not mira.dead and log.interactive("mira_missing_01") and ("met_mira" in quest_whore.list or "pc_knows_whore" in mira.list), 1000, 0)),
        ("quest_mira_missing_dan_approach", If (not mira.dead and "asked_about_mira" in dan.list and not "told_about_mira" in dan.list, 1000, 0)),
        ("quest_mira_missing_cass_whore_idea", If (not mira.dead and log.interactive("mira_missing_03") and "told_cass_mira_whore_date" in quest_mira_missing.dict and (t.day - quest_mira_missing.dict["told_cass_mira_whore_date"]) >= 1, 1000, 0)),

        
        ("rachel_exhib_game_mason_investigate", If ("rachel_talk_exhib_games_chain" in rachel.dict and rachel.dict["rachel_talk_exhib_games_chain"] >= 5 and not "mason_investigate" in mason.list and t.hour in irange(9,16) and loc([loc_school_hallway, loc_school_gym, loc_school_field]), 5000,0)),
        
        ("random_event_nudevball_mason_catch_park_convo", If(loc(loc_school_gym) and t.hour in irange(9,18) and "mason_caught_parknude" in mason.list and not "mason_caught_parknude_convo" in mason.list, 500, 0)),


        
        ("dani_talk_meet_academy", If (not dani.has_met and t.day > 4 and not loc_cur.outside and cass.has_met, 50,0)),
        ("rachel_talk_meet_academy", If (not rachel.has_met and t.day > 4 and not loc_cur.outside and cass.has_met, 50,0)),
        
        ("random_event_none", 1000),

        ])

    if rand_choice == "random_event_none":

        jump travel
    elif not renpy.has_label(rand_choice):

        jump travel
    else:


        $ random_event_picker_time = t._minutes
        jump expression rand_choice

label random_event_picker_school_night_tombola:

    $ rand_choice = WeightedChoice([
    ("rachel_exhib_game_mason_catchnude", If ("rachel_talk_exhib_games_chain" in rachel.dict and rachel.dict["rachel_talk_exhib_games_chain"] >= 5 and "mason_investigate" in mason.list and not "mason_caughtnude" in mason.list and t.hour in (21,22,23,0,1,2,3) and c.nude and not rachel_here() and loc([loc_school_hallway, loc_school_gym, loc_school_hallway_2f]), 1000,0)),
    ("rachel_exhib_game_mason_joinnude", If ("rachel_talk_exhib_games_chain" in rachel.dict and rachel.dict["rachel_talk_exhib_games_chain"] >= 5 and "mason_investigate" in mason.list and "mason_caughtnude" in mason.list and t.hour in (21,22,23,0,1,2,3) and c.nude and not rachel_here() and not "nude_vball" in loc_beach_hangout.list and loc([loc_school_hallway, loc_school_gym, loc_school_hallway_2f]), 1000,0)),

    ("random_event_none", 1000),

    ])

    if rand_choice == "random_event_none":

        jump travel
    elif not renpy.has_label(rand_choice):

        jump travel
    else:
        $ random_event_picker_time = t._minutes
        jump expression rand_choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
