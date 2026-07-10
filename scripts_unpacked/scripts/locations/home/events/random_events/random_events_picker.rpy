label random_event_picker_home_tombola:
    if not "dead_rent_reminder" in oskar.dict:
        $ oskar.dict["dead_rent_reminder"] = 0
    if not "dead_rent_reminder_date" in oskar.dict:
        $ oskar.dict["dead_rent_reminder_date"] = 0

    $ rand_choice = WeightedChoice([
    
    
    
    ("random_event_home_robin_meet_firsttime", If (not robin.has_met and t.day > 1 and t.timeofday == "day" and loc([loc_kitchen, loc_hallway, loc_common]), 100, 0)), 
    
    ("robin_talk_sexobject_bedroom_thoughts", If (log.interactive("quest_robinslut_01") and not "sexobject_clothes_bedroom_thoughts" in robin.list and loc(loc_bedroom), 100, 0)), 
    
    
    
    ("oskar_talk_meet_house", If (not oskar.has_met and t.day in (7,8,9,10,11,12,13) and t.timeofday == "day" and loc([loc_kitchen, loc_hallway, loc_common]), 100, 0)), 
    
    ("oskar_talk_pay_rent_home", If (t.wkday == "Sunday" and t.hour in irange(8,18) and loc([loc_kitchen, loc_hallway, loc_common]) and rent_total_owed() and not "asked_rent" in oskar.list and not oskar.dead and not rent_weeks_skipped() >= 4, 100, 0)),
    
    ("oskar_talk_pay_rent_punish", If (t.hour in irange(7,21) and loc([loc_kitchen, loc_hallway, loc_common, loc_stairwell, loc_bedroom, loc_office_ll]) and rent_weeks_skipped() >= 4 and not (oskar.dead or loc_kitchen.locked), 100, 0)),
    
    ("oskar_talk_pay_rent_oskardead_" + str(oskar.dict["dead_rent_reminder"]), If (renpy.has_label("oskar_talk_pay_rent_oskardead_" + str(oskar.dict["dead_rent_reminder"])) and not oskar.dict["dead_rent_reminder_date"] == t.day and t.wkday == "Sunday" and t.hour in irange(8,18) and dis(dis_home_area) and oskar.dead and not loc_kitchen.locked, 100, 0)),
    ("oskar_talk_poison_dead_picker", If (oskar.dead and oskar.days_dead <= 10 and "dead_poisoned" in oskar.list and loc(loc_stairwell) and not numgen(0,5), 1, 0)), 

    
    ("oskar_sex_home_init", If (rent_total_owed() and oskar.can_sex and oskar_here(loc_office_ll) and loc([loc_kitchen, loc_hallway, loc_common, loc_stairwell]) and (oskar.lust > 50 or (t.day - oskar.last_spoke_to) > 1) and not loc_kitchen.locked and not "oskar_sex" in robin.list, 100, 0)),
    
    
    
    ("main_quest_03_fixer_home", If (main_quest_03.active == 1 and main_quest_03.stage == 2 and loc(loc_bedroom), 100, 0)),
    
    
    
    ("dani_freakout_event_courtyard_arrive", If(loc(loc_stairwell) and loc_from == loc_residential and dani_here([loc_bedroom_dani, loc_stairwell]) and oskar_here(dis_home_area) and dani_yan_value() >= 100 and log.interactive("quest_dancevip_04") and not "freakout_blocked" in dani.list, 100, 0)),

    
    
    ("bathroom_enter_occupied", If (loc(loc_bathroom) and any([robin_here(), emile_here()]), 100, 0)),





    ("random_event_none", 1), 
    ])

    if rand_choice == "random_event_none":

        jump travel_dis
    elif not renpy.has_label(rand_choice):

        jump travel_dis
    else:
        $ random_event_picker_time = t._minutes
        jump expression rand_choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
