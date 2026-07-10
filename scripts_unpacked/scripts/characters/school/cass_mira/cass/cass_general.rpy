init python:

    def cass_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        
        if not cass.has_met or not cass.isactive:
            cur_location = None
        
        elif "broken" in cass.list and "cass_knows" in quest_whore.list: 
            if t.time_from_to(17.00, 04.00):
                if cass.hour_number in (0,1,2):
                    cur_location = loc_highway
                elif cass.hour_number  in (3,4,5):
                    cur_location = loc_motel
                elif cass.hour_number  in (6,7,8):
                    cur_location = loc_truckstop
                else:
                    cur_location = loc_highway_slum
            else:
                cur_location = None
        
        elif "broken" in cass.list: 
            cur_location = None
        
        elif log.interactive("mira_missing_07") and t.hour in (20,21,22,23): 
            cur_location = loc_revel_backstreet
        
        
        elif t.wkday in weekdays and t.time_from_to(07.30, 07.59): 
            cur_location = loc_school
        
        elif t.wkday in weekdays and t.hour == 12: 
            cur_location = loc_school_cafe
        elif t.wkday in weekdays and t.hour in irange(8, 13): 
            cur_location = loc_school_classroom
        elif t.wkday in weekdays and t.hour in (14,15): 
            cur_location = loc_school
        
        elif cass.iswhore and t.time_from_to(18.00, 02.00) and not "hospitalised" in mira.list:
            if cass.hour_number in (0,1,2):
                cur_location = loc_highway
            elif cass.hour_number  in (3,4,5):
                cur_location = loc_motel
            elif cass.hour_number  in (6,7,8):
                cur_location = loc_truckstop
            else:
                cur_location = loc_highway_slum
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where)

    def cassidy_here(location=None, where=False, class_loc=False):
        return cass_here(location, where, class_loc)

label cass_talk_subject:


    if not "cass_poison_talk" in cass.dict:
        $ cass.dict["cass_poison_talk"] = 0
    if not "cass_bully_talk" in cass.dict:
        $ cass.dict["cass_bully_talk"] = 0
    if not "cass_soccerboys_talk" in cass.dict:
        $ cass.dict["cass_soccerboys_talk"] = 0


    if "broken" in cass.list:
        jump cass_talk_broken_tombola
    elif mira.dead and not "broken" in cass.list:
        jump quest_mira_missing_dead_tellcass
    elif log.interactive("mira_missing_02"):
        jump quest_mira_missing_return_to_cass
    elif log.interactive("mira_missing_03"):
        if t.day > quest_mira_missing.dict["told_cass_mira_whore_date"]:
            jump quest_mira_missing_cass_whore_idea
        else:
            pcm "I should give her time to process what I told her."
            jump travel
    elif t.hour == 14 and log.interactive("mira_missing_04"):
        jump quest_mira_missing_go_highway_first_prompt
    elif log.interactive("mira_missing_06"):
        jump quest_mira_missing_cass_only_whores
    elif log.interactive("mira_missing_08") and cass.inv.qty(item_mira_intel):
        jump quest_mira_missing_intel_cass
    elif log.interactive("mira_missing_09") and not "told_cass_all_intel" in quest_mira_missing.list:
        jump quest_mira_missing_intel_complete
    elif log.interactive("mira_missing_10"):
        jump quest_mira_missing_cass_conv
    elif log.completed("Find Mira") and not "visited_hospital" in mira.list and loc(loc_school) and "rescue_date" in mira.dict and t.day >= (mira.dict["rescue_date"] + 1):
        jump quest_mira_missing_cass_visit




    show cass at right1 with dissolve
    jump expression WeightedChoice([

    ("cass_talk_general_tombola", 20),

    
    ("cass_talk_bully_poison_" + str(cass.dict["cass_poison_talk"]), If(renpy.has_label("cass_talk_bully_poison_" + str(cass.dict["cass_poison_talk"])) and not shane.dead and "cass_poison" in shane.list, 200, 0)),
    
    
    ("cass_talk_soccerboys_meet_" + str(cass.dict["cass_soccerboys_talk"]), If(renpy.has_label("cass_talk_soccerboys_meet_" + str(cass.dict["cass_soccerboys_talk"])) and all([drake.has_met, nate.has_met, dan.has_met]), 200, 0)),

    
    ("cass_talk_pregnant_discover", If(cass.showing and not "seen_pregnant_" + str(cass.preg) in cass.list, 5000, 0)),
    ])

label cass_talk_test:
    cass.name "Testing testing i am here"
    cass.name "test test am i wearing the right clothes?"
    jump cass_talk_end

label cass_talk_end:
    show cass neutral
    if mira_here():
        jump cass_mira_talk_end
    $ relax(20, cass)
    $ dialouge = renpy.random.choice([
    "I hang out talking and joking about random stuff.",
    "I hang out for a while chatting and joking around about random topics.",
    "We hang out chatting and laughing about whatever comes up.",
    "We chat and have a bit of a laugh about random stuff."
    ])
    "[dialouge]"
    hide cass with dissolve
    jump travel

label cass_gift_picker:
    show cass at right1 with dissolve
    $ temp_var_1 = True
    cass.name "Have something for me?"

    $ temp_var_1 = [item_beer, item_map_pill, item_abort_pill, item_joy, item_pepperspray]
    if cass.iswhore:
        $ add_to_list(temp_var_1, [item_lebo, item_wakeup])
    if school_bully_quest_bully_cass_target and shane.alive and not "gave_poison" in cass.list:
        $ add_to_list(temp_var_1, [item_poison])
    call screen inventory_gift_choice(temp_var_1)

    $ temp_var_1 = True

    if buy_inv.qty(item_beer):
        if cass.inv.qty(item_beer) >= 3:
            cass.name "Think I am okay on the beer [name]."
            $ temp_var_1 = False
        else:
            cass.name "Thanks [name]!"

    elif buy_inv.qty(item_map_pill):
        if cass.is_pregnant:
            $ temp_var_1 = False
            robin.name "I think it's a bit late for these [name]."
            if not cass.showing:
                pc "Oh? I didn't know. You don't look it."
                cass.name "..."
        elif (cass.iswhore and cass.inv.qty(item_map_pill) >= 5) or (not cass.iswhore and cass.inv.qty(item_map_pill) >= 3):
            if cass.iswhore:
                cass.name "I managed to keep a few I got from the whores, so I think I am okay for now."
            else:
                cass.name "I think I have enough of these [name]. You are better keeping them."
            $ temp_var_1 = False
        else:
            if cass.iswhore:
                cass.name "These really come in handy when working the highway. Thanks [name]."
            else:
                cass.name "Thanks [name]. These are hard to come by"

    elif buy_inv.qty(item_abort_pill):
        if cass.is_pregnant and cass.pregnant_who.abort:
            cass.name "Oh thank you [name]!"
            if cass.showing:
                pc "Yeah, seeing the belly I thought I would offer."
        elif cass.is_pregnant:
            cass.name "Thanks [name]. But I think I will keep this one"
            pc "Oh? Really? Okay then."
            $ temp_var_1 = False
        elif cass.inv.qty(item_map_pill) >= 2:
            cass.name "I already have some of these [name]. I think you should keep them."
            $ temp_var_1 = False
        else:
            if cass.iswhore:
                cass.name "These really come in handy when working the highway. Thanks [name]."
            else:
                cass.name "Thanks [name]. These are hard to come by"

    elif buy_inv.qty(item_joy):
        if cass.inv.qty(item_joy) >= 3:
            cass.name "I think I have enough of these [name]. You are better keeping them."
            $ temp_var_1 = False
        else:
            cass.name "Oooh, that will keep me happy when things go to shit. Thanks [name]!"

    elif buy_inv.qty(item_lebo):
        if cass.inv.qty(item_lebo) >= 3:
            cass.name "I think I have enough of these [name]. You are better keeping them."
            $ temp_var_1 = False
        else:
            pc "This might make hanging around the highway easier for you."
            cass.name "It does... Thanks [name]."

    elif buy_inv.qty(item_wakeup):
        if cass.inv.qty(item_wakeup) >= 3:
            cass.name "I think I have enough of these [name]. You are better keeping them."
            $ temp_var_1 = False
        else:
            pc "This might make hanging around the highway easier for you."
            cass.name "It does... Thanks [name]."

    elif buy_inv.qty(item_poison):
        $ add_to_list(cass.list, "gave_poison")
        show cass worried
        cass.name "Errm... What is this?"
        pc "It's something that will make those two arseholes go away."
        cass.name "It really what I think it is?"
        pc "Mix with some beer or something and let them have it."
        cass.name "Are you really suggesting what I think you are?"
        pc "..."
        cass.name "You are?"
        pc "Do you think anyone will care?"
        cass.name "But... you are talking about murder!"
        pc "I am talking about getting rid of a huge problem."
        cass.name "[name]! This is too much!"
        pc "Then don't. But keep this anyway."
        cass.name "..."
        $ cass.add_love(5000)
    else:

        show cass worried
        cass.name "Ah... Okay."
    if temp_var_1:
        $ cass._love += (inv_value(buy_inv) / 4)
        $ inv_transfer(buy_inv, cass.inv)
    else:
        $ inv_transfer(buy_inv, inv)

    show cass happy
    jump cass_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
