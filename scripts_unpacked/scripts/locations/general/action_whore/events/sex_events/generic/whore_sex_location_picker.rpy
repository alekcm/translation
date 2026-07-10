label whore_street_customer_pick_location:
    $ player.face_happy()
    $ male_npc_create()
    $ renpy.scene()
    show male_generic at right1
    with dissolve
    "[rlist.whore_start_see_customer]"
    pc "[rlist.whore_start_see_customer_speak]"
    $ player.set_whore_price(0)

    if numgen(0, 2):
        call whore_street_customer_convince_picker from _call_whore_street_customer_convince_picker

    tempname.name "[rlist.whore_start_see_customer_speak_reply]"



    $ pc_dress()


    tempname.name "How does £[player.soldprice] sound?"

    if whore_experiance_weight():
        call whore_street_customer_whatsex from _call_whore_street_customer_whatsex
    jump whore_street_customer_pick_location_tombola

label whore_street_customer_pick_location_tombola:

    jump expression WeightedChoice([
    
    

    
    
    ("whore_street_customer_pick_location_isolate",1),

    
    ("whore_street_customer_pick_location_home", If(dis(dis_residential) and not emile_here(dis_home.locs) and not loc_kitchen.locked, 1000, 0)),
    ("whore_street_customer_pick_location_park_toilets", If (dis(dis_park), 1000, 0)),
    ("whore_street_customer_pick_location_flat", If(dis(dis_residential), 1000, 0)),

    
    ("whore_street_customer_pick_location_school_toilets", If (dis(dis_school) and loc_school_hallway.open(), 1000, 0)),
    ("whore_street_customer_pick_location_school_lockers", If (dis(dis_school) and loc_school_hallway.open(), 1000, 0)),
    ("whore_street_customer_pick_location_school_lockers_old", If (dis(dis_school) and loc_school_hallway.open() and not loc_school_locker_old.locked, 1000, 0)),
    
    
    ("whore_street_customer_pick_location_pub_toilets", If (dis(dis_pub), 1000, 0)),
    ("whore_street_customer_pick_location_pub_backroom", If (dis(dis_pub) and pub_waitress.timesworked, 1000, 0)),
    ("whore_street_customer_pick_location_flat", If(dis(dis_revel) and not (dis(dis_pub) or dis(dis_partyhouse)), 1000, 0)),
    ("whore_street_customer_pick_location_partyhouse_bedroom", If (dis(dis_partyhouse), 1000, 0)),
   
    
    ("whore_street_customer_pick_location_jaylee_trailer", If (dis(dis_junkyard) and loc_junk_trailer.open() and not (jaylee_here(loc_junk_1) or jaylee_here(loc_junk_trailer) or jaylee_here(loc_junk_trailer_bathroom)), 1000, 0)),
    
    
    ("whore_street_customer_pick_location_motel", If(dis(dis_truckstop), 1000, 0)),
    ("whore_street_customer_pick_location_trucktrailer", If (dis(dis_truckstop), 300, 0)),
    ("whore_street_customer_pick_location_slumhome", If (dis(dis_truckstop) and loc_highway_slum_home.unlocked, 5000, 0)),

    ])

label whore_street_customer_pick_location_isolate:
    pc "[rlist.whore_start_location_somewhere_else]"
    tempname.name "[rlist.whore_start_location_somewhere_follow]"
    $ quest_mira_intel_trigger()
    $ walk(loc_cur.isolate_loc)
    jump whore_sex_start

label whore_street_customer_pick_location_flat:
    tempname.name "Let's have some fun at my place."
    pc "Sounds good."
    $ walk(dis_cur.hub)
    $ quest_mira_intel_trigger()
    $ walk(random([loc_flat1, loc_flat2, loc_flat3, loc_flat4, loc_flat5]))
    tempname.name "Here we go."
    jump whore_sex_start





label whore_street_customer_pick_location_home:
    pc "We can head back to my room if you want."
    tempname.name "[rlist.whore_start_location_somewhere_follow]"
    $ walk(loc_stairwell)

    $ walk(loc_bedroom)
    jump whore_sex_start

label whore_street_customer_pick_location_park_toilets:
    pc "We can go to the park toilets."
    tempname.name "[rlist.whore_start_location_somewhere_follow]"
    $ walk(loc_park_toilet)
    $ walk(loc_park_toilet_girls)
    jump whore_sex_start





label whore_street_customer_pick_location_school_toilets:
    pc "The toilets should be quiet enough."
    tempname.name "[rlist.whore_start_location_somewhere_follow]"
    $ walk(loc_school_toilet_girls)
    $ walk(loc_school_toilet_girls_stall)
    jump whore_sex_start

label whore_street_customer_pick_location_school_lockers:
    pc "The changing rooms should be quiet enough."
    tempname.name "[rlist.whore_start_location_somewhere_follow]"
    $ walk(loc_school_locker_girls)
    jump whore_sex_start

label whore_street_customer_pick_location_school_lockers_old:
    pc "I know somewhere quiet. Let's go."
    tempname.name "[rlist.whore_start_location_somewhere_follow]"
    $ walk(loc_school_locker_old)
    jump whore_sex_start





label whore_street_customer_pick_location_pub_toilets:
    pc "The toilets should be quiet enough."
    tempname.name "[rlist.whore_start_location_somewhere_follow]"
    $ renpy.scene()
    $ walk(loc_pub_toilet_girls)
    $ walk(loc_pub_toilet_girls_stall)
    jump whore_sex_start

label whore_street_customer_pick_location_pub_backroom:
    pc "Let's head through to the back."
    tempname.name "[rlist.whore_start_location_somewhere_follow]"
    $ renpy.scene()
    $ walk(loc_pub_changingroom)
    jump whore_sex_start

label whore_street_customer_pick_location_partyhouse_bedroom:
    pc "Should be an empty room somewhere."
    tempname.name "[rlist.whore_start_location_somewhere_follow]"
    $ renpy.scene()
    $ walk(random([loc_party_bedroom1, loc_party_bedroom2, loc_party_bedroom3, loc_party_bedroom4]))
    if all(["party_sex" in dani.list, "party_sex" in rachel.list, "party_sex" in svet.list]) and numgen():
        jump random_event_picker_dance_party_general_sex_bedroom_inturrupt_svet_threesome
    elif all(["party_sex" in dani.list, "party_sex" in rachel.list, "party_sex" in anabel.list]) and numgen():
        jump random_event_picker_dance_party_general_sex_bedroom_inturrupt_anabel_threesome
    elif any(["party_sex" in dani.list, "party_sex" in rachel.list, "party_sex" in anabel.list, "party_sex" in svet.list]) and not numgen(0,5):
        jump expression "random_event_picker_dance_party_general_sex_bedroom_inturrupt_" + dance_pick_who_having_sex()
    elif any(["party_sex" in dani.list, "party_sex" in rachel.list]) and not numgen(0,3):
        jump random_event_picker_dance_party_general_sex_bedroom_inturrupt_dani_rachel
    jump whore_sex_start





label whore_street_customer_pick_location_jaylee_trailer:
    pcm "Hopefully [jaylee.name] won't mind if I use her trailer."
    pc "I know a quiet place. Let's go."
    $ walk(loc_junk_trailer)
    jump whore_sex_start





label whore_street_customer_pick_location_motel:
    tempname.name "Let's have some fun at my motel room."
    pc "Sounds good."
    $ walk(loc_motel)
    $ quest_mira_intel_trigger()
    $ walk(loc_motel_room2)
    tempname.name "Here we go."
    jump whore_sex_start

label whore_street_customer_pick_location_trucktrailer:
    tempname.name "Let's have some fun in my trailer."
    pc "Sounds good."
    $ walk(loc_truckstop)
    $ quest_mira_intel_trigger()
    $ walk(random([loc_lorry, loc_lorry_1, loc_lorry_2]))
    tempname.name "Here we go."
    jump whore_sex_start

label whore_street_customer_pick_location_slumhome:
    pc "I have a place round here, we can go there."
    tempname.name "Lead the way."
    $ walk(loc_highway_slum_street)
    $ quest_mira_intel_trigger()
    $ walk(loc_highway_slum_home)
    pc "Here we go."
    jump whore_sex_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
