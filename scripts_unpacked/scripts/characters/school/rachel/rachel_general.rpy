init python:

    def rachel_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        text_desc = ""
        
        if not rachel.has_met or not rachel.active:
            cur_location = None
        elif "no_location" in rachel.list or "streaking" in rachel.list: 
            cur_location = None 
        
        elif school_dance_waiting_party():
            cur_location = loc_revel_backstreet
        elif school_dance_at_party():
            if "party_sex" in rachel.list:
                cur_location = loc_party_bedroom1
            elif "left_party" in rachel.list:
                cur_location = loc_revel_backstreet
            elif "dancing" in rachel.list:
                cur_location = loc_party_stage
            elif rachel.hour_number in (1,2):
                cur_location = loc_party_main
            elif rachel.hour_number in (3,4):
                cur_location = loc_party_kitchen
            elif rachel.hour_number in (5,6):
                cur_location = loc_party_terrace
            elif rachel.hour_number in (7,8):
                cur_location = loc_party_stage
            else:
                cur_location = loc_party_hall
        
        
        elif "exhib_wait_outside" in rachel.list and t.hour in (20,21,22,23): 
            cur_location = loc_school
        elif t.wkday in weekdays and t.hour == 12: 
            cur_location = loc_school_cafe
        elif t.wkday in weekdays and loc_school_toilet_girls.has_gloryhole and t.hour in (9, 13) and "using_gloryhole" in rachel.list: 
            cur_location = loc_school_toilet_girls_stall
        elif t.wkday in weekdays and loc_school_toilet_girls.has_gloryhole and t.hour in (9, 10, 11): 
            cur_location = loc_school_toilet_girls 
        
        elif "can_bitch" in rachel.list and t.hour in (20,21,22,23,0,1,2) and rachel.noon_number <= 3 and not rachel.showing:
            cur_location = dis_park
            text_desc = "Bitching at the park."
        
        elif "nude_vball" in rachel.list and people_nude_beach_vball_canplay() and rachel.noon_number > 6: 
            cur_location = loc_beach_gym
        elif "soccerboys_hangout" in rachel.list and t.hour in (20,21,22,23,0,1):
            cur_location = loc_school_field_back
        elif "exhib_inside_academy" in rachel.list and t.hour in (20,21,22,23,0,1,2,3): 
            cur_location = loc_school_gym
        elif all(["soccerboys_hangout" in rachel.list, "can_bitch" in rachel.list, "nude_vball" in loc_beach_hangout.list]) and t.hour in (17,18,19):
            
            cur_location = loc_school_field_back
        
        elif school_dance_trope_present() or (t.wkday in weekdays and t.hour in (12,13,14,15,16,17,18,19)): 
            cur_location = loc_school_gym
        
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where, text_desc)

label rachel_talk_meet_dance:
    show svet happy at right1 with dissolve
    svet.name "Joining us [name]?"
    pc "Yeah, getting a bit of a workout."
    svet.name "Great, this is [rachel.name], we usually dance together."
    show rachel happy at right2 with dissolve
    rachel.name "Ah someone new. Glad you are here. We have so muh fun!"
    pc "Hi, [name]."
    rachel.name "Lets dance [name]!"
    hide svet
    hide rachel
    with dissolve
    return

label rachel_talk_meet_academy:
    show rachel happy at right1 with dissolve
    rachel.name "Ah! You're new right?"
    pc "Yeah, not been here long."
    rachel.name "Nice to meet you! I'm [rachel.name]."
    pc "[name]."
    rachel.name "See ya!"
    hide rachel
    with dissolve
    jump travel

label rachel_talk_end:
    $ relax(20, rachel)
    $ dialouge = renpy.random.choice([
    "I hang out talking and joking about random stuff.",
    "I hang out for a while chatting and joking around about random topics.",
    "We hang out chatting and laughing about whatever comes up.",
    "We chat and have a bit of a laugh about random stuff."
    ])
    "[dialouge]"
    hide rachel with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
