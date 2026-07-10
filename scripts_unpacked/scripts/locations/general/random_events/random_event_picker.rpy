init python:
    def random_event_late_trigger():
        if t.timeofday == "night" and not (loc_cur in dis_home.locs or loc_cur == loc_stairwell) and player.check_nowill(notif=False, block_face=True, block_broken=True) and loc_cur.outside:
            return True
        else:
            return False

    def danger_weight():
        global danger_content
        
        if not danger_content: 
            
            
            
            return 0
        
        if not danger_delay(): 
            return 0
        elif npc_any_here() or npc_any_here(loc_from):
            return 0
        elif loc_cur.population >= 2:
            weight = 0
            for i in player.perk_list:
                if i.victim:
                    weight += 10
                elif i.not_victim:
                    weight -= 10
            return int(weight)
        elif dis_cur.danger > 0 or dis([dis_walk]):
            weight = dis_cur.danger + (player.allure / 16) + (player.drunk / 2)
            if loc_cur.population == 0:
                weight += (weight * 1.2)
            if t.hour in irange(1,4):
                weight += (weight * 1.5)
            if not loc_cur.outside:
                weight = weight / 4
            
            victim_amount = weight * 0.5
            for i in player.perk_list:
                if i.victim:
                    weight += victim_amount
                elif i.not_victim:
                    weight -= victim_amount
            return int(weight)
        else:
            return 0

    def danger_gen(amount, override=0):
        if not danger_content:
            return False
        
        weight = danger_weight()
        if override > danger_weight():
            weight = override
        return weightgen(weight, amount)

    def danger_delay():
        
        global danger_content
        
        if not danger_content:
            return False
        elif not danger_day_limit:
            return True
        elif t.day <= 10: 
            return False
        elif t.day < 40 and weightgen(100, ((t.day - 10) * 3)): 
            return False
        else:
            return True

    def allure_weight():
        if player.looks_dirty():
            return 0
        elif player.perverted or c.exposed:
            allure_cap = 0
        elif player.slutty:
            allure_cap = 200
        else:
            allure_cap = 400
        if player.allure <= allure_cap:
            return 0
        else:
            return (player.allure - allure_cap) / 2

    def stupid_weight():
        if t.day < 10:
            
            return 0
        amount = 0
        if player.has_perk(perk_deadinside):
            amount = amount + 20
        if player.int < 20:
            amount = amount + (10 - (player.int / 2))
        if player.has_perk([perk_blackout, perk_wasted]):
            amount = amount + 10
        if player.has_perk(perk_despondent):
            amount = amount + 10
        return amount

    def mira_can_discover_highway():
        
        if loc([loc_highway, loc_motel, loc_truckstop, loc_highway_slum]) and t.time_from_to(18.00, 02.00) and not "pc_knows_whore" in mira.list and not "kidnapped" in mira.list and not mira.dead:
            return True
        else:
            return False

default random_event_picker_time = 0
default random_event_picker_location = ""
default random_event_picker_explanation_devnote = False

label random_event_picker_tombola:

    if log.interactive("quest_homeless_start_01") or log.interactive("quest_homeless_start_02"):

        jump random_event_picker_homeless_start_tombola

    elif dis_cur == dis_school and not loc_cur == loc_school:
        jump random_event_picker_school_tombola

    elif dis(dis_home) or dis(dis_home_area):

        jump random_event_picker_home_tombola

    elif dis(dis_pub):
        jump travel

    elif dis(dis_haven):
        if log.interactive("mq_05_b"):

            if haven_search_complete():
                jump haven_searched
            jump travel_dis
        $ haven_progress_triggers()
        jump random_event_picker_haven_tombola

    elif dis(dis_partyhouse) and t.hour in (21,22,23,0,1,2,3,4):
        jump random_event_picker_dance_party_tombola

    elif loc_cur.home_location:

        jump random_event_picker_home_location_tombola

    elif loc_cur.events and loc_cur.population:
        jump random_event_picker_generic_tombola
    else:
        jump travel_dis

label random_event_picker_generic_tombola:
    $ rand_choice = WeightedChoice([
    ("random_event_generic_normal", 300),
    ("give_birth", If (player.pregnant == 2, 10000, 0)),
    ("random_event_generic_tired", If (player.tired < 20, 200, 0)),
    ("world_tired_trigger", If (player.tired < 4, 700, 0)),
    ("random_event_generic_desire", player.check_horny()), 
    ("random_event_generic_desiremax", player.check_horny(extreme=True)),
    ("random_event_generic_desirenocontrol", player.check_horny(very_extreme=True)),
    ("random_event_generic_allure", allure_weight()),
    ("random_event_generic_allure_flirt_start_normal", If(loc_cur.outside and loc_cur.population >= 2, allure_weight(), 0)),
    ("random_event_generic_whore_approach_normal", If(player.has_perk([perk_slutty, perk_pervert]) and loc_cur.outside and loc_cur.population >= 2, allure_weight(), 0)),    
    
    ("random_event_generic_highconf", If (player.confidence > 40, player.confidence, 0)),
    ("random_event_generic_lowconf", If (player.check_nowill(False, True), 100 - player.confidence, 0)),
    ("random_event_generic_int", If (player.int > 50, player.int, 0)),
    ("random_event_generic_fitness", If (player.fitness >= 40, player.fitness, 0)),
    ("random_event_generic_fat", If (player.isfat or player.pregnancy == 1, 100, 0)),
    ("random_event_generic_lowmood", If (player.has_perk(perk_despondent), 500, 0)),
    ("random_event_generic_highmood", If (player.mood > 60, 100, 0)),
    ("random_event_generic_weather", If (outside, 50, 0)),
    ("random_event_generic_night", If (t.hour in dark, 200, 0)),
    ("random_event_generic_rushhour", If (t.hour in rushhour, 25, 0)),
    ("random_event_generic_hungry", If (player.hunger < 20, 300, 0)),
    ("random_event_generic_dirty", If (player.hygiene < 20, 500, 0)),
    ("random_event_generic_drunk", If (player.drunk > 60, player.drunk * 2, 0)),
    ("random_event_generic_drunkblackout", If (player.check_drunk(5, notif=False), player.drunk, 0)),
    ("random_event_generic_pregnant", If (player.pregnant and player.days_pregnant > (global_pregnancy_length * 0.1), 50, 0)),
    ("random_event_generic_inseminated", If (player.has_perk(perk_inseminated) and not player.preg_knows, 50, 0)),
    ("random_event_generic_lactation", If (player.has_perk(perk_lactating), 50, 0)),
    ("random_event_generic_cum", If (player.cum_visible_check(), 400, 0)),
    ("random_event_generic_danger", danger_weight()),
    ("random_event_generic_latenight", If (random_event_late_trigger(), 500, 0)),
    ("random_event_generic_malestart", If(player.has_perk(perk_male), (-player.body_conf), 0)),
    ("random_event_generic_exhib_perk", perk_exhib_weight(6)),
    ("random_event_generic_badchoices", stupid_weight()),
    ("random_event_generic_comments", 50),

    
    ("random_event_misc_hucow_1", trigger_hucow()),

    
    ("scav_discover_remind_park_event", If(scav_discover_remind_park(), 100, 0)),
    ("scav_discover_remind_junk_event", If(scav_discover_remind_junk(), 100, 0)),
    ("scav_discover_remind_beach_event", If(scav_discover_remind_beach(), 100, 0)),

    
    ("loc_walk_rails_discover", If(scav_discover_walk_junk_slum() and t.day >= 14, (t.day * 2), 0)),
    ("loc_walk_park_forest_discover", If(scav_discover_walk_park_academy() and t.day >= 14, (t.day * 2), 0)),
    ("loc_walk_park_lake_discover", If(scav_discover_walk_park_lake() and t.day >= 14, (t.day * 2), 0)),
    
    
    ("random_event_generic_park_wolf_1", If(not quest_wolfgang.active and dis(dis_park), 100, 0)),
    ("random_event_generic_park_wolf_2", If(not quest_wolfgang.active and dis(dis_park), 100, 0)),
    ("random_event_generic_park_wolf_3", If(quest_wolfgang.active and dis(dis_park), 100, 0)),
    ("random_event_generic_park_wolf_4", If(quest_wolfgang.active and dis(dis_park), 100, 0)),

    
    ("random_event_generic_exhib_cover", If(player.covering and not dis(dis_beach), 500, 0)),
    ("random_event_generic_exhib", If(c.inappropriate and not dis(dis_beach), 2000, 0)),

    
    ("random_event_nudevball_mason_catch_park", If((wolfgang_play_location() or dis(dis_beach)) and not "nude_vball" in loc_beach_hangout.list and not "mason_caught_parknude" in mason.list and mason.has_met and "beach_vball_asked" in loc_beach_gym.list and not t.timeofday == "day", 100, 0)),
    ("random_event_nudevball_mason_catch_park_again", If((wolfgang_play_location() or dis(dis_beach)) and not "nude_vball" in loc_beach_hangout.list and not "mason_caught_parknude_again" in mason.list and "mason_caught_parknude_convo" in mason.list and not t.timeofday == "day", 100, 0)),

    
    ("random_event_generic_addict_joy", If(player.has_perk(perk_joy_addict) and not player.has_perk(perk_joy), 150, 0)),
    ("random_event_generic_addict_alcohol", If(player.has_perk(perk_alcoholic) and not player.drunk, 150, 0)),
    ("random_event_generic_addict_cigs", If(player.has_perk(perk_smoker) and item_cigs.last_used, 150, 0)),
    
    

    
    ("robin_talk_sexobject_market_thoughts", If (not "sexobject_clothes_market_thoughts" in robin.list and loc(loc_market) and log.interactive("quest_robinslut_01"), 5000, 0)),
    ("robin_talk_sexobject_funwear_thoughts", If (not "sexobject_clothes_funwear_thoughts" in robin.list and loc(loc_revel_backstreet) and log.interactive("quest_robinslut_01"), 5000, 0)),
    
    
    ("jaylee_meet_0", If (jaylee.isactive and loc_cur in dis_junkyard.locs and t.hour in workhours and jaylee.spoke_to_hours_ago and not jaylee.dict["jaylee_meet_events"], 1000, 0)),
    ("jaylee_meet_picker", If (jaylee.isactive and loc_cur in dis_junkyard.locs and t.hour in workhours and jaylee.spoke_to_hours_ago > 0 and jaylee.dict["jaylee_meet_events"] and ashon.inv.value_junk() > 10, 500, 0)),
    
    
    ("lake_dealer_meet", If(loc_cur in dis_beach.locs and not lake_dealer.has_met, 80, 0)),
    
    
    
    ("random_event_generic_rent", If(rent_total_owed() and not loc_kitchen.locked, 50, 0)),
    ("oskar_talk_pay_rent_kickout", If(rent_weeks_skipped() >= 5 and not loc_kitchen.locked and loc_cur.population == 1 and loc_cur.outside, 500, 0)),
    ("random_event_generic_newhome", If(loc_kitchen.locked and loc_highway_slum_home.locked, 50, 0)),

    
    ("mira_whore_discover", If(mira_can_discover_highway(), 5, 0)),
    ("quest_mira_missing_dead_discover", If(loc(loc_beach_hangout) and "kidnapped" in mira.list and not "rescued" in mira.list and (t.day - mira.dict["kidnap_date"]) >= 28 and mira.alive and t.hour in workhours, 50000, 0)),
    ("quest_mira_missing_pc_knows", If (log.interactive("mira_missing_01") and any("met_whore_mira" in item for item in mira.list), 1000, 0)),
    ("quest_mira_missing_dead_assume", If("kidnapped" in mira.list and not "rescued" in mira.list and (t.day - mira.dict["kidnap_date"]) >= 40 and mira.alive and t.hour in workhours, 1000, 0)),

    
    ("rachel_talk_exhib_inside_notalk_0", If("exhib_inside_academy" in rachel.list and "rachel_exhib_inside_talk" in rachel.dict and t.day >= (rachel.dict["rachel_exhib_try"] + 2) and rachel.dict["rachel_exhib_inside_talk"] == 0 and "exhib_inside_academy" in rachel.list and not "show_stripping" in rachel.list, 500, 0)),
    ("rachel_talk_exhib_inside_notalk_1", If("exhib_inside_academy" in rachel.list and "rachel_exhib_inside_talk" in rachel.dict and t.day >= (rachel.dict["rachel_exhib_try"] + 2) and rachel.dict["rachel_exhib_inside_talk"] == 1 and "exhib_inside_academy" in rachel.list and not "show_stripping" in rachel.list, 500, 0)),
    ("rachel_talk_exhib_inside_notalk_2", If("exhib_inside_academy" in rachel.list and "rachel_exhib_inside_talk" in rachel.dict and t.day >= (rachel.dict["rachel_exhib_try"] + 2) and rachel.dict["rachel_exhib_inside_talk"] == 2 and "exhib_inside_academy" in rachel.list and not "show_stripping" in rachel.list, 500, 0)),
    ("rachel_talk_exhib_inside_notalk_3", If("exhib_inside_academy" in rachel.list and "rachel_exhib_inside_talk" in rachel.dict and t.day >= (rachel.dict["rachel_exhib_try"] + 2) and rachel.dict["rachel_exhib_inside_talk"] == 3 and "exhib_inside_academy" in rachel.list and not "show_stripping" in rachel.list, 500, 0)),

    
    
    
    ("random_event_generic_malestart_remove", If(player.has_perk(perk_male) and not player.body_conf, 1000, 0)),
    
    ("random_event_perk_bimbo", If(perk_bimbo_qualify_checker(), 300, 0)),
    ("random_event_perk_commando", If(perk_commando_qualify_checker(), 300, 0)), 
    ("random_event_commando_underwear", If(player.has_perk(perk_commando) and (c.pants and not(c.thong or c.pantsless)), 100, 0)), 
    ("random_event_perk_loose_commando", If(perk_commando_loose_checker(), 300, 0)), 
    ("broodmother_sudden_lactation", If(not player.has_perk(perk_lactating) and player.has_perk(perk_broodmother), 10, 0)), 
    
    ("pregnancy_want_or_not_choice_first", If(not player.preg_knows and not "asked_preg_want" in player.list and t.day > 3 and not player.preg_amount and not player.vvirgin, 30, 0)), 
    ("pregnancy_want_or_not_choice_repeat", If(not player.preg_knows and not "asked_preg_want" in player.list and t.day > 3 and not player.cycle_conditions["stage"] in ("mens", "no_cycle") and player.preg_amount, 200, 0)), 

    
    
    ("start_homeless_meet_sister", If(log.interactive("quest_homeless_start_03") and loc_cur.outside and loc_cur.population >= 2 and t.timeofday == "day" and t.day > 25, (t.day * 2), 0)), 
    

    ("random_event_none", 1000), 
    ])

    if rand_choice == "random_event_none":

        jump travel_dis
    elif not renpy.has_label(rand_choice):

        jump travel_dis
    else:
        $ random_event_picker_time = t._minutes
        jump expression rand_choice


label random_event_generic_normal:
    jump travel
label random_event_generic_desire:
    jump travel
label random_event_generic_desiremax:
    jump travel
label random_event_generic_whore:
    jump travel
label random_event_generic_slut:
    jump travel
label random_event_generic_highconf:
    jump travel
label random_event_generic_lowconf:
    jump travel
label random_event_generic_int:
    jump travel
label random_event_generic_fitness:
    jump travel
label random_event_generic_fat:
    jump travel

label random_event_generic_lowmood:
    if inv.qty(item_joy) and player.has_perk(perk_joy_addict):
        call item_joy_action from _call_item_joy_action_1
    elif inv.qty(item_beer):
        call item_beer_action from _call_item_beer_action
    elif inv.qty(item_joy):
        call item_joy_action from _call_item_joy_action_4
    else:
        pcm "Ugh, I feel so shitty. Is there nothing to cheer me up?"
    jump travel

label random_event_generic_highmood:
    jump travel
label random_event_generic_weather:
    if weather_var == 0 and not t.timeofday == "night":
        pcm "Glad the weather is nice."
    elif weather_var == 1 and not t.timeofday == "night":
        pcm "Such a gloomy day..."
    elif weather_var == 3:
        pcm "Damn rain."
    elif weather_var == 4:
        pcm "Fuck I am freezing in this snow."
    jump travel
label random_event_generic_night:
    jump travel
label random_event_generic_rushhour:
    jump travel
label random_event_generic_hungry:
    jump travel




label random_event_generic_cum:
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
