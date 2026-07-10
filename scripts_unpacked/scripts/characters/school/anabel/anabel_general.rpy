init python:

    def anabel_not_hanging_with_dani():
        
        
        if "being_alone" in anabel.list:
            return True
        else:
            return False

    def anabel_alone_academy_day_picker(count=False):
        
        if log.interactive("quest_dancevip_04") and not "reconciled" in dani.list:
            amount = 20
        
        amount = 1
        if log.interactive("quest_dancevip_04") and not "freakout_blocked" in dani.list:
            
            amount += 100
        elif "freakout_blocked" in dani.list:
            amount -= 100
        
        if dani.showing:
            amount += 1
        if "working_pub" in dani.list:
            amount += 1
        if pubpatron in dani.sex_who_class:
            amount += 1
        if ghman in dani.sex_who_class:
            amount += 1
        if school_dance_quest_show_count >= 5:
            amount += 1
        if school_dance_quest_show_count >= 9:
            amount += 2
        if partyman in dani.sex_who_class:
            amount += 2
        if log.interactive("quest_dancevip_04"):
            amount += 4
        
        
        if count:
            
            
            return amount
        
        if numgen(0,10) <= amount:
            
            add_to_list(anabel.list, "being_alone")
        else:
            remove_from_list(anabel.list, "being_alone")

    def anabel_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        
        if not anabel.has_met or not anabel.active:
            cur_location = None
        elif "no_location" in anabel.list: 
            cur_location = None 
        elif "bad_end" in anabel.list:
            cur_location = None 
        
        elif anabel.hate:
            if t.wkday in weekdays and t.hour in (8, 9, 10, 11, 12,13,14,15,16,17):
                if not dani_here(loc_school_cafe):
                    cur_location = loc_school_cafe
                elif not dani_here(loc_school):
                    cur_location = loc_school
                else:
                    cur_location = loc_school_classroom
        
        
        
        
        elif school_dance_trope_present() and anabel.hate: 
            cur_location = loc_school_classroom
        elif school_dance_trope_present() and dani.dead and "dead_anabel_knows" in dani.list: 
            cur_location = loc_school_classroom
        
        elif anabel_not_hanging_with_dani() and t.wkday in weekdays and t.time_from_to(07.30, 07.59): 
            cur_location = loc_school
        elif anabel_not_hanging_with_dani() and school_dance_trope_present(): 
            cur_location = loc_school_gym
        elif anabel_not_hanging_with_dani() and t.wkday in weekdays and t.hour in (8, 9, 10, 11, 12,13,14): 
            cur_location = loc_school_classroom
        elif anabel_not_hanging_with_dani() and t.wkday in weekdays and t.hour == 17: 
            cur_location = loc_school_classroom
        
        
        elif t.wkday in weekdays and t.time_from_to(07.30, 07.59): 
            cur_location = loc_school
        elif school_dance_trope_present(): 
            cur_location = loc_school_gym
        elif t.wkday in weekdays and t.hour in (8, 9, 10, 11, 12,13,14): 
            cur_location = loc_school_cafe
        elif t.wkday in weekdays and t.hour == 17: 
            cur_location = loc_school
        
        
        elif school_dance_waiting_party() and not "dance_event_refuse" in anabel.list:
            cur_location = loc_revel_backstreet
        elif school_dance_at_party() and not "dance_event_refuse" in anabel.list:
            if "party_sex" in anabel.list:
                cur_location = loc_party_bedroom4
            elif "left_party" in anabel.list:
                cur_location = loc_revel_backstreet
            elif "dancing" in anabel.list:
                cur_location = loc_party_stage
            elif anabel.hour_number in (1,2):
                cur_location = loc_party_main
            elif anabel.hour_number in (3,4):
                cur_location = loc_party_kitchen
            elif anabel.hour_number in (5,6):
                cur_location = loc_party_terrace
            elif anabel.hour_number in (7,8):
                cur_location = loc_party_stage
            else:
                cur_location = loc_party_hall
        
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where)

label anabel_talk_picker:


    if not "dani_split" in anabel.dict:
        $ anabel.dict["dani_split"] = 0
    if not "dani_struggle" in anabel.dict:
        $ anabel.dict["dani_struggle"] = 0

    if not "dance_vip_post" in anabel.dict:
        $ anabel.dict["dance_vip_post"] = 0
    if not "dance_vip_post_dani_conv_date" in anabel.dict:
        $ anabel.dict["dance_vip_post_dani_conv_date"] = 0
    if not "anabel_post_vip_dani_reconcile_chain" in anabel.dict:
        $ anabel.dict["anabel_post_vip_dani_reconcile_chain"] = 0



    show anabel at right1 with dissolve

    jump expression WeightedChoice([

    ("anabel_talk_subject", 100),



    
    ("anabel_talk_dani_split_" + str(anabel.dict["dani_split"]), If(renpy.has_label("anabel_talk_dani_split_" + str(anabel.dict["dani_split"])) and anabel_alone_academy_day_picker(True) >= 4 and anabel.love > 40 and not quest_dancevip.active, 5000, 0)),
    ("anabel_talk_dani_struggle_" + str(anabel.dict["dani_struggle"]), If(renpy.has_label("anabel_talk_dani_struggle_" + str(anabel.dict["dani_struggle"])) and anabel_alone_academy_day_picker(True) >= 4 and anabel.love > 40 and not renpy.has_label("anabel_talk_dani_split_" + str(anabel.dict["dani_split"])) and dani_yan_value() >= 50, 5000, 0)),

    
    ("anabel_talk_post_vip_" + str(anabel.dict["dance_vip_post"]), If(renpy.has_label("anabel_talk_post_vip_" + str(anabel.dict["dance_vip_post"])) and anabel_not_hanging_with_dani() and log.interactive("quest_dancevip_04") and "dani_post_vip_talk" in anabel.list, 5000, 0)),

    ("anabel_talk_postvip_dani_reconcile_chain_" + str(anabel.dict["anabel_post_vip_dani_reconcile_chain"]), If(renpy.has_label("anabel_talk_postvip_dani_reconcile_chain_" + str(anabel.dict["anabel_post_vip_dani_reconcile_chain"])) and log.interactive("quest_dancevip_04") and not ("bad_end" in anabel.list or anabel.hate) and "dance_vip_post_dani_conv_date" in anabel.dict and anabel.dict["dance_vip_post_dani_conv_date"] > 0 and t.day >= (anabel.dict["dance_vip_post_dani_conv_date"] + 2), 5000, 0)),

    ])

label anabel_talk_test:
    anabel.name "Talking to me alone?"
    anabel.name "I'm not even sure if there is anywhere I am alone yet."
    pc "Later maybe."
    jump anabel_talk_end

label anabel_talk_end:
    show anabel neutral
    $ relax(20, anabel)
    $ dialouge = renpy.random.choice([
    "I hang out talking and joking about random stuff.",
    "I hang out for a while chatting and joking around about random topics.",
    "We hang out chatting and laughing about whatever comes up.",
    "We chat and have a bit of a laugh about random stuff."
    ])
    "[dialouge]"
    hide anabel
    with dissolve
    jump travel

label anabel_talk_reject_talking:
    $ add_to_list(anabel.list, "blocked_talking")
    show anabel angry at right1 with dissolve
    anabel.name "Don't talk to me."
    $ player.face_worried()
    pc "I thought..."
    anabel.name "Stop! Not after what you did!"
    hide anabel with dissolve
    pcm "..."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
