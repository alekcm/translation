label random_event_picker_haven_tombola:


    call random_event_picker_haven_tombola_call from _call_random_event_picker_haven_tombola_call_2

    if rand_choice == "random_event_none" or not renpy.has_label(rand_choice) or (t._minutes < random_event_picker_time + 5):
        jump travel
    else:
        $ random_event_picker_time = t._minutes
        $ renpy.scene()
        jump expression rand_choice


label random_event_picker_haven_tombola_call:
    $ rand_choice = WeightedChoice([
    ("random_event_haven_normal_1", haven_random_event_room_weight()),
    ("random_event_haven_normal_2", haven_random_event_room_weight()),
    ("random_event_haven_normal_3", haven_random_event_room_weight()),
    ("random_event_haven_normal_4", haven_random_event_room_weight()),
    ("random_event_haven_normal_5", haven_random_event_room_weight()),
    ("random_event_haven_normal_6", haven_random_event_room_weight()),
    ("random_event_haven_normal_7", haven_random_event_room_weight()),
    ("random_event_haven_normal_8", haven_random_event_room_weight()),
    ("random_event_haven_normal_9", haven_random_event_room_weight()),
    ("random_event_haven_normal_10", haven_random_event_room_weight()),
    ("random_event_haven_normal_11", haven_random_event_room_weight()),
    ("random_event_haven_normal_12", haven_random_event_room_weight()),
    ("random_event_haven_normal_13", haven_random_event_room_weight()),
    ("random_event_haven_normal_14", haven_random_event_room_weight()),

    ("random_event_haven_drunk_1", If (player.drunk > 70, haven_random_event_room_weight(),0)),
    ("random_event_haven_drunk_2", If (player.drunk > 70, haven_random_event_room_weight(),0)),
    ("random_event_haven_drunk_3", If (player.drunk > 70, haven_random_event_room_weight(),0)),
    ("random_event_haven_drunk_4", If (player.drunk > 70, haven_random_event_room_weight(),0)),
    ("random_event_haven_drunk_5", If (player.drunk > 70, haven_random_event_room_weight(),0)),
    ("random_event_haven_drunk_6", If (player.drunk > 70, haven_random_event_room_weight(),0)),
    ("random_event_haven_drunk_7", If (player.drunk > 70, player.drunk,0)),
    ("random_event_haven_drunk_8", If (player.drunk > 70, player.drunk,0)),
    ("random_event_haven_drunk_9", If (player.drunk > 70, player.drunk,0)),

    ("random_event_haven_sex_1", haven_random_event_room_weight() / 3),
    ("random_event_haven_sex_2", haven_random_event_room_weight() / 3),
    ("random_event_haven_sex_3", haven_random_event_room_weight() / 3),
    ("random_event_haven_sex_4", haven_random_event_room_weight() / 3),

    ("haven_utilities_join_1", haven_random_event_room_weight(util=True) / 2),
    ("haven_utilities_join_2", haven_random_event_room_weight(util=True) / 2),
    ("haven_utilities_join_3", haven_random_event_room_weight(util=True) / 2),
    ("haven_utilities_join_4", haven_random_event_room_weight(util=True) / 3),
    ("haven_utilities_join_5", haven_random_event_room_weight(util=True) / 5),

    ("random_event_haven_shower_1", haven_random_event_room_weight(shower=True)),
    ("random_event_haven_shower_2", haven_random_event_room_weight(shower=True)),
    ("random_event_haven_shower_3", haven_random_event_room_weight(shower=True)),
    ("random_event_haven_shower_4", haven_random_event_room_weight(shower=True)),
    ("random_event_haven_shower_5", haven_random_event_room_weight(shower=True)),
    ("random_event_haven_shower_6", haven_random_event_room_weight(shower=True)),
    ("random_event_haven_shower_7", If (player.drunk > 60, haven_random_event_room_weight(shower=True),0)),
    ("random_event_haven_shower_8", If (player.drunk > 60, haven_random_event_room_weight(shower=True),0)),
    ("random_event_haven_shower_9", haven_random_event_room_weight(shower=True)),
    ("random_event_haven_shower_10", haven_random_event_room_weight(shower=True)),
    ("random_event_haven_shower_11", haven_random_event_room_weight(shower=True)),
    ("random_event_haven_shower_12", haven_random_event_room_weight(shower=True)),

    ("random_event_haven_force_1", haven_random_event_room_weight() / 10),


    ("random_event_haven_desire_1", player.check_horny()),
    ("random_event_haven_desire_2", player.check_horny()),
    ("random_event_haven_desire_3", player.check_horny()),
    ("random_event_haven_desire_4", player.check_horny()),
    ("random_event_haven_desire_5", If (player.check_horny() and havenpeeper.has_met, player.check_horny(), 0)),

    ("random_event_haven_hygiene_1", If (player.hygiene < 20, 200, 0)),
    ("random_event_haven_hygiene_2", If (player.hygiene < 20, 200, 0)),
    ("random_event_haven_hygiene_3", If (player.hygiene < 20, 200, 0)),

    ("random_event_haven_harass_1", If (not haven_time_safe() or haven_time_empty(), 50, 0)),
    ("random_event_haven_harass_2", If (not haven_time_safe() or haven_time_empty(), 50, 0)),
    ("random_event_haven_harass_3", If (not haven_time_safe() or haven_time_empty(), 50, 0)),
    ("random_event_haven_harass_4", If (not haven_time_safe() or haven_time_empty(), 50, 0)),


    ("haven_bed_whore_offer", If ((writing.forehead or writing.face) and loc_cur in (loc_haven_bed, loc_haven_bedroom) and not haven_time_safe() or haven_time_empty(), 100, 0)),
    ("haven_bed_whore_offer", If (not loc_cur in (loc_haven_utilities, loc_haven_shower_stall) and not haven_time_safe() or haven_time_empty(), 10, 0)),

    ("haven_tired_trigger", If (player.tired < 5, 10000,0)),

    ("haven_brewmaster_drink_lowmood", If (player.mood < 20 and inv.qty(item_brew) and not player.drinking, 10000,0)),
    ("haven_brewmaster_picker", If (player.mood < 10 and not inv.qty(item_brew) and not player.drinking, 10000,0)),
    ("dis_haven_whore_lowmood", If (player.mood < 10 and not inv.qty(item_brew) and player.iswhore and not haven_time_empty() and not player.drinking, 10000,0)),

    ("haven_drunk_trigger", If (player.drunk > 100, player.drunk, 0)),

    ("haven_pregnant_ending_start", If (player.pregnancy and player.pregnant, 50000, 0)),
    
    ("random_event_none", haven_random_event_noevent_weight()),

    ])


    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
