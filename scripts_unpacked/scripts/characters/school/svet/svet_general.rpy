init python:

    def svet_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        
        if not svet.has_met or not svet.active:
            cur_location = None
        elif "no_location" in svet.list: 
            cur_location = None 
        
        elif t.wkday in weekdays and t.hour == 12:
            cur_location = loc_school_cafe
        elif school_dance_trope_present() or t.hour in school_hours: 
            cur_location = loc_school_gym
        
        elif school_dance_waiting_party():
            cur_location = loc_revel_backstreet
        elif school_dance_at_party():
            if "party_sex" in svet.list:
                cur_location = loc_party_bedroom1
            elif "left_party" in svet.list:
                cur_location = loc_revel_backstreet
            elif "dancing" in svet.list:
                cur_location = loc_party_stage
            elif svet.hour_number in (1,2):
                cur_location = loc_party_main
            elif svet.hour_number in (3,4):
                cur_location = loc_party_kitchen
            elif svet.hour_number in (5,6):
                cur_location = loc_party_terrace
            elif svet.hour_number in (7,8):
                cur_location = loc_party_stage
            else:
                cur_location = loc_party_hall
        
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where)

    def svetlana_here(location=None, where=False, class_loc=False):
        return svet_here(location, where, class_loc)

label dance_talk_picker:

    jump expression WeightedChoice([

    ("svet_rachel_talk_test", 100),
    ("dani_anabel_talk_picker", 100),

    ])

label svet_talk_picker:






    show svet at right1 with dissolve

    jump expression WeightedChoice([

    ("svet_talk_subject", 20), 

    ])

label svet_talk_end:
    $ relax(20, svet)
    $ dialouge = renpy.random.choice([
    "I hang out talking and joking about random stuff.",
    "I hang out for a while chatting and joking around about random topics.",
    "We hang out chatting and laughing about whatever comes up.",
    "We chat and have a bit of a laugh about random stuff."
    ])
    "[dialouge]"
    hide svet with dissolve
    jump travel

label svet_rachel_talk_test:
    show svet at right1
    show rachel at right2
    with dissolve
    svet.name "Testing testing i am here"
    rachel.name "So am I"
    hide svet
    hide rachel
    with dissolve
    jump travel
    jump rachel_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
