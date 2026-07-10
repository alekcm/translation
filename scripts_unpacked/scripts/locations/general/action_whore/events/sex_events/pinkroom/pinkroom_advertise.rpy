label pinkroom_advertise_start:
    if player.tired <= 10:
        pcm "I am way too tired. I'll end up passing out and something bad will happen."
        jump travel
    $ npc_race_picker()
    $ tempname = pinkroom_man
    $ tempname2 = pinkroom_man2
    $ tempname3 = pinkroom_man3
    $ quest_temp = quest_whore
    $ player.soldprice = item_pinkticket.value
    if not "advertised" in loc_motel_pinkroom.list:
        jump pinkroom_advertise_firsttime
    $ pc_striptease()
    $ pc_set_temp_outfit()
    jump pinkroom_advertise_cycle

label pinkroom_advertise_cycle:
    $ show_pinkroom_image()
    "[rlist.whore_start_available]"
    $ working(10)
    if whore_customer_weight():
        jump pinkroom_customer_tombola
    else:
        call pinkroom_no_customer_tombola from _call_pinkroom_no_customer_tombola

    pcm "[rlist.whore_start_waiting]"
    $ show_pinkroom_image()
    "[rlist.whore_start_available]"
    $ working(10)
    if whore_customer_weight():
        jump pinkroom_customer_tombola
    else:
        call pinkroom_no_customer_tombola from _call_pinkroom_no_customer_tombola_1

    pcm "[rlist.whore_start_waiting]"
    $ show_pinkroom_image()
    "[rlist.whore_start_available]"
    $ working(10)
    if whore_customer_weight():
        jump pinkroom_customer_tombola
    else:
        call pinkroom_no_customer_tombola from _call_pinkroom_no_customer_tombola_2

    pcm "[rlist.whore_start_waiting]"
    $ renpy.scene()
    with dissolve
    jump travel



label pinkroom_no_customer_tombola:
    call expression WeightedChoice([
  
    ("pinkroom_no_customer_event_test", 300),
    ("pinkroom_no_customer_event_test", If (player.pregnant == 2, 10000, 0)),

    ]) from _call_expression_18
    return

label pinkroom_no_customer_event_test:
    $ dialouge = renpy.random.choice([
    "I try to attract the eye of a few guys, but no one knocks.",
    "People pass and some pay attention to me, but no one comes to the door.",
    "Despite me showing off at the window, no one decides to come to my door."
    ])
    "[dialouge]"
    return


label pinkroom_customer_tombola:
    "A customer knocks on the door and I head over to let him in."
    $ male_npc_create_all()
    $ renpy.scene()
    show male_generic at right1
    with dissolve
    jump expression WeightedChoice([
    ("pinkroom_customer_standard_tombola", 100),
    ("pinkroom_customer_group_tombola", If(loc_motel_pinkroom.dict["sex_groups"], 30, 0)),
    ("pinkroom_customer_extreme_tombola", If(loc_motel_pinkroom.dict["sex_extreme"], 10, 0)),
    ])

label pinkroom_customer_standard_tombola:
    jump expression WeightedChoice([

    
    ("pinkroom_customer_event_vanilla", 100),
    ("pinkroom_customer_event_anal", 100),
    ("pinkroom_customer_event_vag", 200),

    ("pinkroom_customer_event_dance", 100),
    ("pinkroom_customer_event_drugdeal", 20),
    
    ("pinkroom_customer_event_showersex", 100),
    ("pinkroom_customer_event_creampie", 100),
    ])

label pinkroom_customer_group_tombola:
    jump expression WeightedChoice([

    
    ("pinkroom_customer_event_gangbang", 100),
    
    ("pinkroom_customer_event_maid", If(any([wardrobe.qty(item_outfit_6), wardrobe.qty(item_outfit_18), wardrobe.qty(item_outfit_20)]), 100, 0)),
    ("pinkroom_customer_event_dance_group", 100),
    ])

label pinkroom_customer_extreme_tombola:
    jump expression WeightedChoice([
    
    ("pinkroom_customer_event_rough", 100),
    ("pinkroom_customer_event_beating", 100),
    
    ("pinkroom_customer_event_tattoo", 100),
    ("pinkroom_customer_event_tied", 100),
    ("pinkroom_customer_event_upsidedown", 100),
    ("pinkroom_customer_event_spanking", If(bruise.ass < 0.3, 100, 0)),
    
    ("pinkroom_customer_event_forced", If(danger_content, 100, 0)),
    ])


label pinkroom_customer_event_vanilla:
    pc "[rlist.pinkroom_welcome_single]"
    tempname.name "[rlist.pinkroom_welcome_guyask_vanilla]"
    $ inv.take(item_pinkticket)
    jump whore_bed_sex_start

label pinkroom_customer_event_anal:
    pc "[rlist.pinkroom_welcome_single]"
    tempname.name "[rlist.pinkroom_welcome_guyask_anal]"
    $ inv.take(item_pinkticket)
    $ player.soldrequest = "anal"
    jump whore_bed_sex_start

label pinkroom_customer_event_vag:
    pc "[rlist.pinkroom_welcome_single]"
    tempname.name "[rlist.pinkroom_welcome_guyask_vag]"
    $ inv.take(item_pinkticket)
    $ player.soldrequest = "vag"
    jump whore_bed_sex_start

label pinkroom_customer_event_creampie:
    pc "[rlist.pinkroom_welcome_single]"
    tempname.name "[rlist.pinkroom_welcome_guyask_creampie]"
    $ inv.take(item_pinkticket)
    $ player.soldrequest = "creampie"
    jump whore_bed_sex_start

label pinkroom_customer_event_rough:
    pc "[rlist.pinkroom_welcome_single]"
    tempname.name "Hey darling, I want to take you rough."
    $ player.soldrequest = "rough"
    $ inv.take(item_pinkticket, 2)
    jump whore_street_sex_floor
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
