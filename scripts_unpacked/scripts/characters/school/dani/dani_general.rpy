init python:
    def dani_not_hanging_with_anabel():
        
        
        if "being_alone" in dani.list:
            return True
        else:
            return False

    def dani_alone_academy_day_picker():
        amount = dani_yan_value() / 10
        if log.interactive("quest_dancevip_04") and not "freakout_blocked" in dani.list:
            
            add_to_list(dani.list, "being_alone")
        
        if numgen(0,10) <= amount:
            add_to_list(dani.list, "being_alone")
        else:
            remove_from_list(dani.list, "being_alone")

    def dani_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        text_desc = ""
        
        if not dani.has_met or not dani.isactive:
            cur_location = None
        elif "no_location" in dani.list: 
            cur_location = None
        
        
        
        elif school_dance_waiting_party():
            cur_location = loc_revel_backstreet
        elif school_dance_at_party():
            if "party_sex" in dani.list:
                cur_location = loc_party_bedroom3
            elif "left_party" in dani.list:
                cur_location = loc_revel_backstreet
            elif "dancing" in dani.list:
                cur_location = loc_party_stage
            elif dani.hour_number in (1,2):
                cur_location = loc_party_main
            elif dani.hour_number in (3,4):
                cur_location = loc_party_kitchen
            elif dani.hour_number in (5,6):
                cur_location = loc_party_terrace
            elif dani.hour_number in (7,8):
                cur_location = loc_party_stage
            else:
                cur_location = loc_party_hall
        
        
        
        elif dani_not_hanging_with_anabel() and t.wkday in weekdays and t.time_from_to(07.30, 07.59): 
            cur_location = loc_bus_interior
        elif dani_not_hanging_with_anabel() and  school_dance_trope_present(): 
            cur_location = loc_school_gym
        elif dani_not_hanging_with_anabel() and  t.wkday in weekdays and t.hour in (8, 9, 10, 11, 12, 13): 
            cur_location = loc_school_hallway_2f
        elif dani_not_hanging_with_anabel() and  t.wkday in weekdays and t.time_from_to(17.00, 17.30): 
            cur_location = loc_bus_interior
        elif dani_not_hanging_with_anabel() and  t.wkday in weekdays and t.hour in (8,9,10,11,12,13,14,15,16):
            text_desc = "Somewhere around the Academy."
        
        
        elif t.wkday in weekdays and t.time_from_to(07.00, 07.29): 
            cur_location = loc_bus_interior
        elif t.wkday in weekdays and t.time_from_to(07.30, 07.59): 
            cur_location = loc_school
        elif school_dance_trope_present(): 
            cur_location = loc_school_gym
        elif t.wkday in weekdays and t.hour in (8, 9, 10, 11, 12, 13): 
            cur_location = loc_school_cafe
        elif t.wkday in weekdays and t.hour == 17: 
            cur_location = loc_school
        elif t.wkday in weekdays and t.time_from_to(18.00, 18.30): 
            cur_location = loc_bus_interior
        elif t.wkday in weekdays and t.hour in (8,9,10,11,12,13,14,15,16):
            text_desc = "Somewhere around the Academy."
        
        
        
        
        
        elif "working_pub" in dani.list and t.time_from_to(20.30, 20.59) and t.wkday in ["Wednesday", "Thursday", "Friday", "Saturday"]:
            
            cur_location = loc_bus_interior
        elif "working_pub" in dani.list and t.time_from_to(3.00, 3.30) and t.wkday in ["Thursday", "Friday", "Saturday", "Sunday"]:
            
            cur_location = loc_bus_interior
        elif "working_pub" in dani.list and ((t.hour in (21,22,23,0,1,2) and t.wkday in ["Thursday", "Friday", "Saturday"]) or (t.wkday == "Sunday" and t.hour in (0,1,2)) or (t.wkday == "Wednesday" and t.hour in (21,22,23))):
            cur_location = loc_pub
        
        
        elif (t.wkday in weekdays and t.hour in (18,19,20,21)) or (t.wkday in weekend and t.hour in (10,11,12,13,14,15,18,19,20,21)):
            cur_location = loc_stairwell
        
        
        
        else:
            cur_location = loc_bedroom_dani
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where, text_desc) 

    def danielle_here(location=None, where=False, class_loc=False):
        return dani_here(location, where, class_loc) 


label dani_talk_init:




    if not "stairwell_talk" in dani.dict:
        $ dani.dict["stairwell_talk"] = 0


    if not "pub_askjob_talk" in dani.dict:
        $ dani.dict["pub_askjob_talk"] = 0
    if not "pub_started_working" in dani.dict:
        $ dani.dict["pub_started_working"] = 0
    if not "pub_gotjob_talk" in dani.dict:
        $ dani.dict["pub_gotjob_talk"] = 0


    if not "talk_workingpub_chain" in dani.dict:
        $ dani.dict["talk_workingpub_chain"] = 0
    if not "talk_whoringpub_chain" in dani.dict:
        $ dani.dict["talk_whoringpub_chain"] = 0
    if not "talk_gloryholepub_chain" in dani.dict:
        $ dani.dict["talk_gloryholepub_chain"] = 0


    if not "oskar_sex_talk" in dani.dict:
        $ dani.dict["oskar_sex_talk"] = 0
    if not "oskar_missing_talk" in dani.dict:
        $ dani.dict["oskar_missing_talk"] = 0


    if not "dani_talk_anabel_chain" in dani.dict:
        $ dani.dict["dani_talk_anabel_chain"] = 0
    if not "dani_talk_upstairs_chain" in dani.dict:
        $ dani.dict["dani_talk_upstairs_chain"] = 0


    if not "dani_post_vip_chain" in dani.dict:
        $ dani.dict["dani_post_vip_chain"] = 0
    if not "dani_post_vip_anabel_reconcile_chain" in dani.dict:
        $ dani.dict["dani_post_vip_anabel_reconcile_chain"] = 0


    if not "dani_drinking_wine_day" in dani.dict:
        $ dani.dict["dani_drinking_wine_day"] = 0
    if not "dani_drinking_wine_counter" in dani.dict:
        $ dani.dict["dani_drinking_wine_counter"] = 0
    if not "dani_times_slept_over" in dani.dict:
        $ dani.dict["dani_times_slept_over"] = 0

    return
label dani_talk_picker:

    call dani_talk_init from _call_dani_talk_init

    if loc(loc_bedroom_dani) and t.hour in (23,0,1,2,3,4,5):

        pcm "She is sleeping, I should leave her alone."
        jump travel

    if loc(loc_bedroom_dani):
        show dani at right5 with dissolve
    else:
        show dani at right1 with dissolve

    jump expression WeightedChoice([

    ("dani_talk_subject", 20),

    
    ("dani_stairwell_talk_" + str(dani.dict["stairwell_talk"]), If(renpy.has_label("dani_stairwell_talk_" + str(dani.dict["stairwell_talk"])) and dani_here(loc_stairwell), 500, 0)),
    
    
    ("dani_talk_pregnant_discover", If(dani.showing and not "seen_pregnant_" + str(dani.preg) in dani.list, 5000, 0)),

    
    ("pub_askjob_talk_trigger", If(pub_waitress.timesworked >= 8 and not "asked_pub_work" in dani.list and dani.love >= 30, 500, 0)),
    
    ("pub_askjob_talk_" + str(dani.dict["pub_askjob_talk"]), If(renpy.has_label("pub_askjob_talk_" + str(dani.dict["pub_askjob_talk"])) and "asked_pub_work" in dani.list and dani.love >= 30, 500, 0)),
    ("dani_gotjob_talk_" + str(dani.dict["pub_gotjob_talk"]), If(renpy.has_label("dani_gotjob_talk_" + str(dani.dict["pub_gotjob_talk"])) and "willwork_pub" in dani.list and (dani.dict["pub_started_working"] - 2) <= t.day, 500, 0)),
    
    
    ("dani_talk_workingpub_chain_" + str(dani.dict["talk_workingpub_chain"]), If(renpy.has_label("dani_talk_workingpub_chain_" + str(dani.dict["talk_workingpub_chain"])) and (dani.dict["pub_started_working"] - 4) <= t.day and "pub_first_talk" in dani.list, 500, 0)),
    ("dani_talk_whoreingpub_chain_" + str(dani.dict["talk_whoringpub_chain"]), If(renpy.has_label("dani_talk_whoreingpub_chain_" + str(dani.dict["talk_whoringpub_chain"])) and not renpy.has_label("dani_talk_workingpub_chain_" + str(dani.dict["talk_workingpub_chain"])) and pubpatron.name in dani.sex_who, 500, 0)),
    ("dani_talk_gloryholepub_chain_" + str(dani.dict["talk_gloryholepub_chain"]), If(renpy.has_label("dani_talk_gloryholepub_chain_" + str(dani.dict["talk_gloryholepub_chain"])) and not renpy.has_label("dani_talk_whoreingpub_chain_" + str(dani.dict["talk_whoringpub_chain"])) and ghman.name in dani.sex_who, 500, 0)),

    
    ("oskar_sex_talk_" + str(dani.dict["oskar_sex_talk"]), If(renpy.has_label("oskar_sex_talk_" + str(dani.dict["oskar_sex_talk"])) and dani.love >= 50 and loc(loc_stairwell), 500, 0)),
    ("oskar_sex_force_talk", If(not "forced_oskar_talk" in dani.conversation_topics and oskar.rape, 5000, 0)),
    ("oskar_sex_kickedout_talk", If(not "kickedout_oskar_talk" in dani.conversation_topics and loc_kitchen.locked, 5000, 0)),
    ("dani_talk_oskar_dead_" + str(dani.dict["oskar_missing_talk"]), If(renpy.has_label("dani_talk_oskar_dead_" + str(dani.dict["oskar_missing_talk"])) and dani.love >= 50 and oskar.days_dead in irange(3,9) and "dead_poisoned" in oskar.list, 500, 0)),
    ("dani_talk_oskar_dead_know", If(dani.love >= 50 and oskar.days_dead >= 10 and "dead_poisoned" in oskar.list and not "oskar_dead_know" in dani.list, 500, 0)),
    
    
    ("dani_talk_anabel_chain_" + str(dani.dict["dani_talk_anabel_chain"]), If(renpy.has_label("dani_talk_anabel_chain_" + str(dani.dict["dani_talk_anabel_chain"])) and dani.love >= 20, 500, 0)),
    ("dani_talk_upstairs_" + str(dani.dict["dani_talk_upstairs_chain"]), If(renpy.has_label("dani_talk_upstairs_" + str(dani.dict["dani_talk_upstairs_chain"])) and not renpy.has_label("dani_talk_anabel_chain_" + str(dani.dict["dani_talk_anabel_chain"])) and loc(loc_school_hallway_2f) and not quest_dancevip.active, 2000, 0)),


    
    ("dani_postdance_company_conv_chat", If("dance_went_alone" in dani.conversation_topics and school_dance_quest_show_count == 9 and dis(dis_school), 500, 0)),
    ("dani_postdance_company_conv_chat_alone", If("dance_went_alone" in dani.conversation_topics and school_dance_quest_show_count == 9 and not dis(dis_school), 500, 0)),
    ("dani_postdance_company_conv_followup", If ("dance_went_alone_followup" in dani.conversation_topics and school_dance_quest_show_count == 9 and (loc_cur.population == 0 or not dis(dis_school)) ,500,0)),
    
    
    
    ("dani_talk_postvip_goodend_chain_" + str(dani.dict["dani_post_vip_chain"]), If(renpy.has_label("dani_talk_postvip_goodend_chain_" + str(dani.dict["dani_post_vip_chain"])) and log.interactive("quest_dancevip_04") and not ("bad_end" in anabel.list or anabel.hate), 500, 0)), 

    
    
    
    ("dani_talk_postvip_anabel_reconcile_chain_" + str(dani.dict["dani_post_vip_anabel_reconcile_chain"]), If(renpy.has_label("dani_talk_postvip_anabel_reconcile_chain_" + str(dani.dict["dani_post_vip_anabel_reconcile_chain"])) and log.interactive("quest_dancevip_04") and not ("bad_end" in anabel.list or anabel.hate) and "dance_vip_post_dani_conv_date" in anabel.dict and anabel.dict["dance_vip_post_dani_conv_date"] > 0 and t.day >= (anabel.dict["dance_vip_post_dani_conv_date"] + 2), 500, 0)), 

    
    ("dani_talk_postvip_badend_chain_" + str(dani.dict["dani_post_vip_chain"]), If(renpy.has_label("dani_talk_postvip_badend_chain_" + str(dani.dict["dani_post_vip_chain"])) and log.interactive("quest_dancevip_04") and ("bad_end" in anabel.list or anabel.hate), 500, 0)), 

    
    ("dani_drinking_wine_event_trigger", If (loc([loc_bedroom_dani, loc_stairwell]) and not quest_daniwine.active and not loc_bedroom_dani.locked, 500, 0)),
    ("dani_drinking_wine_event_trigger_repeat", If (quest_daniwine.active and not log.interactive("quest_daniwine_02") and dani.dict["dani_drinking_wine_counter"] and (dani_yan_value() >= 50 or dani_drinkwine_subject_can_trigger_unique()),200,0)),
    
    ])

label dani_talk_test:
    dani.name "Hello. Talk talk"
    pc "Hi!"
    jump dani_talk_end

label dani_talk_meet_dance:
    show dani happy at right1 with dissolve
    dani.name "Hey, new here?"
    pc "Yeah."
    dani.name "[dani.nname], nice to meet you. This is [anabel.name]."
    show anabel at right2 with dissolve
    anabel.name "Hi."
    pc "[name]. You doing dance?"
    dani.name "Yeah, here most days."
    pc "Okay, looks like I'll be seeing you round."
    dani.name "Yup."
    hide dani
    hide anabel
    with dissolve
    return

label dani_talk_meet_academy:
    show dani happy at right1 with dissolve
    dani.name "Ah hey, I've seen you around. New here right?"
    pc "Yeah."
    dani.name "[dani.nname], nice to meet you. This is [anabel.name]."
    show anabel at right2 with dissolve
    anabel.name "Hi."
    pc "[name]."
    dani.name "Looks like we will be seeing you around."
    pc "Yeah, seems so."
    hide dani
    hide anabel
    with dissolve
    jump travel


label dani_talk_end:
    $ relax(20, dani)
    show dani neutral
    if not numgen(0,10):
        $ dani_yan_remove(1)
    $ dialouge = renpy.random.choice([
    "I hang out talking and joking about random stuff.",
    "I hang out for a while chatting and joking around about random topics.",
    "We hang out chatting and laughing about whatever comes up.",
    "We chat and have a bit of a laugh about random stuff."
    ])
    "[dialouge]"
    if not loc(loc_bedroom_dani) and dani_here(loc_bedroom_dani):
        if loc_bedroom_dani.locked:
            dani.name "I'm going to head home. See you later [name]."
            pc "Cya."
        else:
            dani.name "I'm going to head home. Come join if you want."
            pc "Okay."
    elif loc(loc_bedroom_dani) and not dani_here(loc_bedroom_dani):
        if t.hour == 7 and t.wkday in weekdays:
            dani.name "I'm going to head off to the academy. You going to come with?"
            menu:
                "Yeah, let's go":
                    jump dani_goto_school
                "No, you go ahead":

                    dani.name "Ok, I'm heading off."
        elif dani_here(loc_stairwell):
            dani.name "I'm going outside for some fresh air."
            pc "Okay."
            hide dani
            $ walk(loc_stairwell)
            jump travel
        elif not dani_here(loc_stairwell) or dani_here(loc_bedroom_dani):
            dani.name "I'm going to head out for a bit [name]."
            pc "Okay. See ya."
            hide dani
            $ walk(loc_stairwell)
            jump travel
    elif loc(loc_stairwell) and not dani_here(loc_stairwell):
        if dani_here(loc_bus_interior) and t.hour == 20:
            dani.name "I'm heading to the pub for a shift."
            pc "Okay, have fun."
            hide dani with dissolve
            jump travel

    elif loc(loc_bedroom_dani) and dani_here(loc_bedroom_dani):
        if t.hour == 23:
            if not "can_sleep" in loc_bedroom_dani.list:
                dani.name "I'm going to go to bed now [name]."
                pc "Okay. Goodnight."
                hide dani
                $ walk(loc_stairwell)
                jump travel
            else:
                dani.name "I am heading to bed [name]. You can sleep over if you want."

    hide dani with dissolve
    jump travel

label dani_goto_school:
    if not "school" in tab_top:
        pc "Let me change first."
        $ pc_dress_event("school", say="Ready.")
    $ walk(loc_stairwell, trans=False)
    show dani at left1 with dissolve
    $ walk(loc_busstop_residential)
    dani.name "I can see the bus."
    hide dani with dissolve
    $ walk(loc_bus_interior, trans=False)
    show dani at right6 with dissolve
    jump dani_bus_goto_school_event_picker

label dani_bedroom_checks:
    if dani.dead:
        $ walk(loc_bedroom_dani, arrival=True)
    elif dani.hate:
        $ player.face_angry()
        pcm "No way and I going in that bitches place."
        jump travel
    elif not "can_sleep" in loc_bedroom_dani.list and t.hour in (23,0, 1,2,3,4,5,6,7) and dani_here(loc_bedroom_dani):
        pcm "She is probably sleeping. I should leave her alone."
        jump travel
    elif not "can_sleep" in loc_bedroom_dani.list and not dani_here(loc_bedroom_dani):
        if dani_here(loc_stairwell):
            pcm "[dani.nname] is just over there. I shouldn't just walk in her place."
        else:
            pcm "Looks like it's locked. [dani.nname] must be out."
            if dani_here(loc_pub):
                pcm "Pretty sure she is working at the pub."
        jump travel
    else:
        $ walk(loc_bedroom_dani, arrival=True)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
