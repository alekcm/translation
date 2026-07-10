label random_event_generic_exhib:
    $ exhib_stat_changes()

    $ rand_choice = WeightedChoice([
    
    
    ("random_event_generic_exhib_general", If(perk_exhib_total_value() < 200, 30, 0)),

    
    ("random_event_generic_exhib_0", If(c.exposed, perk_exhib_weight(0), 0)),
    ("random_event_generic_exhib_1", If(c.exposed, perk_exhib_weight(1), 0)),
    ("random_event_generic_exhib_2", If(c.exposed, perk_exhib_weight(2), 0)),
    ("random_event_generic_exhib_3", If(c.exposed, perk_exhib_weight(3), 0)),
    ("random_event_generic_exhib_4", If(c.exposed, perk_exhib_weight(4), 0)),
    ("random_event_generic_exhib_5", If(c.exposed, perk_exhib_weight(5), 0)),
    ("random_event_generic_exhib_6", If(c.exposed, perk_exhib_weight(6), 0)),
    
    
    ("random_event_generic_exhib_cover", If(player.covering, 100, 0)),

    
    ("random_event_generic_exhib_academy", If(c.exposed and dis(dis_school) and not loc_cur.outside and loc_cur.population == 2, 200, 0)),
    ("random_event_generic_exhib_park", If(c.exposed and dis(dis_park) and t.timeofday == "night", 100, 0)),
    ("random_event_generic_exhib_highway", If(c.exposed and dis(dis_truckstop) and loc_cur.outside, 100, 0)),
    ("random_event_generic_exhib_pub", If(c.exposed and loc(loc_pub), 100, 0)),
    ("random_event_generic_exhib_hospital", If(c.exposed and loc(loc_hospital_lobby), 100, 0)),
    ("random_event_generic_exhib_junk", If(c.exposed and dis(dis_junkyard) and jaylee.love > 30, 100, 0)),


    
    ("random_event_chain_exhib_" + str(perk_exhibitionist.dict["exhib_event_trigger"]), If(renpy.has_label("random_event_chain_exhib_" + str(perk_exhibitionist.dict["exhib_event_trigger"])) and perk_exhibitionist.dict["exhib_counter"] >= 20 and perk_exhibitionist.dict["exhib_counter"] >= perk_exhibitionist.dict["exhib_event_trigger"] * 30 and loc_cur.population >= 2, 1000, 0)),
    
    
    ("random_event_generic_danger", danger_weight()),
    ("random_event_generic_drunkblackout", If (player.check_drunk(5, notif=False), player.drunk, 0)),
    
    ("random_event_none", 1000), 
    ])

    if rand_choice == "random_event_none":

        jump travel_dis
    elif not renpy.has_label(rand_choice):

        jump travel_dis
    else:
        $ random_event_picker_time = t._minutes
        jump expression rand_choice





label random_event_generic_exhib_miscloc_find_clothes:
    pcm "I can't go out there looking like this. I need to find something to cover up with."
    jump travel

label random_event_generic_exhib_miscloc_people:
    pcm "I am too exposed and there might be people out there..."
    pcm "Fuck..."
    $ walk(loc_want)
    jump travel



label random_event_generic_exhib_general:

    jump expression WeightedChoice([
    ("random_event_generic_exhib_general_1", If(loc_cur.population == 2, 100, 0)),
    ("random_event_generic_exhib_general_2", If(loc_cur.population == 2, 100, 0)),
    ("random_event_generic_exhib_general_3", If(dis(dis_home), 100, 0)),
    ])

label random_event_generic_exhib_perk:

    jump expression WeightedChoice([
    ("random_event_generic_exhib_perk_1", If(loc_cur.population == 2 and c.pants and c.skirt, 100, 0)),
    ("random_event_generic_exhib_perk_2", If(loc_cur.population == 2 and c.bra, 100, 0)),
    ("random_event_generic_exhib_perk_3", If(loc_cur.population == 2 and c.top and not (c.bra and c.coat and c.bsuit), 100, 0)),
    ("random_event_generic_exhib_perk_4", If(loc_cur.population == 2 and c.skirt and c.bottom, 100, 0)),
    ("random_event_generic_exhib_perk_5", If(t.timeofday == "night" and loc_cur.outside and not c.exposed, 20, 0)),
    ])

label random_event_generic_exhib_0:

    $ player.face_worried()
    jump expression WeightedChoice([
    ("random_event_generic_exhib_0_1", If(loc_cur.population == 2, 100, 0)),
    ("random_event_generic_exhib_0_2", If(loc_cur.population == 2, 100, 0)),
    ("random_event_generic_exhib_0_3", If(loc_cur.population == 1, 100, 0)),
    ("random_event_generic_exhib_0_4", If(loc_cur.population == 2 and t.hour in irange(17,22) and not t.timeofday == "night", 100, 0)),
    ("random_event_generic_exhib_0_5", If(loc_cur.population == 2, 100, 0)),
    ("random_event_generic_exhib_0_6", If(loc_cur.population == 2, 100, 0)),
    ])

label random_event_generic_exhib_1:

    $ player.face_worried()
    jump expression WeightedChoice([
    ("random_event_generic_exhib_1_1", If(loc_cur.population == 2, 100, 0)),
    ("random_event_generic_exhib_1_2", If(loc_cur.population == 2, 100, 0)),
    ("random_event_generic_exhib_1_3", If(loc_cur.population == 1, 100, 0)),
    ("random_event_generic_exhib_1_4", If(loc_cur.population == 2 and t.hour in irange(17,22) and not t.timeofday == "night", 100, 0)),
    ])

label random_event_generic_exhib_2:

    $ player.face_worried()
    jump expression WeightedChoice([
    ("random_event_generic_exhib_2_1", If(loc_cur.population == 2, 100, 0)),
    ("random_event_generic_exhib_2_2", If(loc_cur.population == 2, 100, 0)),
    ("random_event_generic_exhib_2_3", If(loc_cur.population == 1, 100, 0)),
    ("random_event_generic_exhib_2_4", If(loc_cur.population == 2 and t.hour in irange(17,22) and not t.timeofday == "night", 100, 0)),
    ])

label random_event_generic_exhib_3:

    $ player.face_shy()
    jump expression WeightedChoice([
    ("random_event_generic_exhib_3_1", If(loc_cur.population == 2, 100, 0)),
    ("random_event_generic_exhib_3_2", If(t.timeofday == "night" and loc_cur.outside, 100, 0)),
    ("random_event_generic_exhib_3_3", If(t.timeofday == "night" and loc_cur.outside, 100, 0)),
    ("random_event_generic_exhib_3_4", If(loc_cur.population == 2 and t.hour in irange(17,22) and not t.timeofday == "night", 100, 0)),
    ])

label random_event_generic_exhib_4:

    $ player.face_neutral()
    jump expression WeightedChoice([
    ("random_event_generic_exhib_4_1", If(loc_cur.population == 2 and t.timeofday == "day", 100, 0)),
    ("random_event_generic_exhib_4_2", If(loc_cur.population == 2, 100, 0)),
    ("random_event_generic_exhib_4_3", If(loc_cur.population == 1, 100, 0)),
    ("random_event_generic_exhib_4_4", If(loc_cur.population == 2 and t.hour in irange(17,22) and not t.timeofday == "night", 100, 0)),
    ])

label random_event_generic_exhib_5:

    $ player.face_happy()
    jump expression WeightedChoice([
    ("random_event_generic_exhib_5_1", If(loc_cur.population == 2, 100, 0)),
    ("random_event_generic_exhib_5_2", If(loc_cur.population == 2, 100, 0)),
    ("random_event_generic_exhib_5_3", If(loc_cur.population == 1, 100, 0)),
    ("random_event_generic_exhib_5_4", If(loc_cur.population == 2 and t.hour in irange(17,22) and not t.timeofday == "night", 100, 0)),
    ])

label random_event_generic_exhib_6:

    $ player.face_happy()
    jump expression WeightedChoice([
    ("random_event_generic_exhib_5_1", If(loc_cur.population == 2, 100, 0)),
    ("random_event_generic_exhib_5_2", If(loc_cur.population == 2, 100, 0)),
    ("random_event_generic_exhib_5_3", If(loc_cur.population == 1, 100, 0)),
    ("random_event_generic_exhib_5_4", If(loc_cur.population == 2 and t.hour in irange(17,22) and not t.timeofday == "night", 100, 0)),
    ])
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
