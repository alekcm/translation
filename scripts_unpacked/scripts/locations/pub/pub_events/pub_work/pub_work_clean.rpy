label pub_waitress_work_cleaner:
    jump expression WeightedChoice([
    ("action_clean_event_pub_busy_1", If (pub_waitress.workcycle, 100, 0)),
    ("action_clean_event_pub_busy_2", If (pub_waitress.workcycle, 100, 0)),
    ("action_clean_event_pub_busy_3", If (pub_waitress.workcycle, 100, 0)),
    ("action_clean_event_pub_busy_4", If (pub_waitress.workcycle, 100, 0)),
    ("action_clean_event_pub_quiet_1", 50),
    ("action_clean_event_pub_quiet_2", 50),
    ])

label action_clean_event_pub_busy_1:
    "There are no drinks at the bar so I head to the tables to clean up the mess."
    show sb_table with dissolve
    "[rlist.clean_area_dialogue]"
    patron "Cheers [rlist.name_cute]."
    pcm "No problem"
    jump action_clean_event_pub_end

label action_clean_event_pub_busy_2:
    pcm "No drinks to give away so might as well clean up."
    show sb_table with dissolve
    "[rlist.clean_area_dialogue]"
    "I head around to the tables and clear away the empty glasses."
    jump action_clean_event_pub_end

label action_clean_event_pub_busy_3:
    pcm "The mess around here is just piling up. Suppose I best do something about it."
    show sb_table with dissolve
    "[rlist.clean_area_dialogue]"
    patron "Ah thanks [rlist.name_cute]. Getting hard to drink without knocking something over."
    pc "Enjoy yourselves."
    jump action_clean_event_pub_end

label action_clean_event_pub_busy_4:
    pcm "No drinks at the bar..."
    show sb_table with dissolve
    "[rlist.clean_area_dialogue]"
    pc "Don't mind me lads."
    patron "Cheers [rlist.name_cute]."
    jump action_clean_event_pub_end

label action_clean_event_pub_quiet_1:
    $ show_cleaning_image()
    "[rlist.clean_area_dialogue]"
    "I clean up all the junk around the pub, mop up spills and clear away glasses."
    jump action_clean_event_pub_end

label action_clean_event_pub_quiet_2:
    $ show_cleaning_image()
    "[rlist.clean_area_dialogue]"
    pcm "Got to watch my fingers from broken glass..."
    "I wipe all the spillage from the tables onto the floor then start giving the floor a mop."
    jump action_clean_event_pub_end

label action_clean_event_pub_quiet_3:
    $ show_cleaning_image()
    "[rlist.clean_area_dialogue]"
    "I clear away all the empty glasses and bring them over to the bar to be washed."
    jump action_clean_event_pub_end

label action_clean_event_pub_end:
    if pub_waitress.workcycle and c.outfit == 6:
        jump pub_waitress_work_cycle1
    else:
        jump action_clean_event_picker

label pub_waitress_work_clean_harass:
    jump expression WeightedChoice([
    ("pub_waitress_work_clean_harass_1", 100),
    
    
    
    
    
    ])

label pub_waitress_work_clean_harass_1:
    show sb_table bentover sex shock back with hpunch
    pc "Ah!"
    patron "Sorry [rlist.name_cute]"
    $ player.grope(hands=False)
    pc "Oi!"
    show sb_table noman with dissolve
    pc "..."
    show sb_table stand with dissolve
    jump pub_waitress_work_cycleend
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
