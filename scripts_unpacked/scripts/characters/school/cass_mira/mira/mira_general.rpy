init python:

    def mira_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        text_desc = ""
        
        if not mira.has_met or not mira.isactive:
            cur_location = None
        
        elif "hospitalised" in mira.list:
            cur_location = loc_hospital_ward
        elif "whore_having_sex" in mira.list:
            text_desc = "I think she is off with a customer."
        
        
        elif t.wkday in weekdays and t.time_from_to(07.30, 07.59): 
            cur_location = loc_school
        
        elif t.wkday in weekdays and t.hour == 12: 
            cur_location = loc_school_cafe
        elif t.wkday in weekdays and t.hour in irange(8, 13): 
            cur_location = loc_school_classroom
        elif t.wkday in weekdays and t.hour in (14,15): 
            cur_location = loc_school
        
        
        elif (t.wkday in weekdays and t.hour in (16,17, 18, 19) or t.wkday in weekend and t.hour in (13, 14, 15, 16,17, 18, 19)) and school_soccer_hangingout() and "rescued" in mira.list and not "hospitalised" in mira.list and "soccer_hangout" in mira.list:
            cur_location = loc_school_field_back
        elif (t.wkday in weekdays and t.hour in (16,17, 18, 19) or t.wkday in weekend and t.hour in (13, 14, 15, 16,17, 18, 19)) and school_soccer_playing() and "rescued" in mira.list and not "hospitalised" in mira.list and "soccer_hangout" in mira.list:
            cur_location = loc_school_field
        
        elif t.time_from_to(18.00, 02.00) and "pc_knows_whore" in mira.list: 
            
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
        return npc_here_check(location, cur_location, where, text_desc) 

label mira_whore_discover:

    $ add_to_list(mira.list, "pc_knows_whore")
    if not mira.has_met:

        $ add_to_list(mira.list, "met_before_academy")
        $ player.face_shock()
        show mira whore worried at right6 with hpunch
        pc "Ah! Sorry."
        mira.name "It's fine, I was looking somewhere else."
        $ mira.meet()
        show mira neutral at left1 with dissolve

        if quest_whore.active and quest_whore.sold > 5:
            $ player.face_worried()
            pc "Oh? Okay."
            mira.name "Have to make sure everyone stays safe."
            pc "Yeah, these weirdos can get out of hand."
        elif quest_whore.active:
            $ player.face_worried()
            pc "Err..."
            pc "Oh?"
            pc "Err... Watching them have sex?"
            $ player.face_neutral()
            pc "Ah, they told me about this when I asked around."
            mira.name "Yeah, have to make sure everyone keeps safe."
            pc "Yeah..."
        else:
            $ player.face_worried()
            pc "Err..."
            pc "Oh?"
            pc "Err... Watching them have sex?"
            pc "Okay..."
            mira.name "Making sure she is okay and not dragged off somewhere."
            pc "Ah, okay..."
            pc "Makes sense..."

        show mira at right5 with dissolve
        mira.name "Not seen you about before. You new?"
        if quest_homeless_start.active:
            pc "Yeah, stumbled into town recently. Still getting used to things."
        else:
            pc "Yeah, sort of. Arrived in town a while ago but spent most of that time in hospital."
            pc "Back on my feet now and figuring things out."
        mira.name "Well, nice to meet you. I'm [mira.wname]."

        if quest_whore.active and quest_whore.sold > 5:
            $ player.face_happy()
            pc "[wname]."
        elif quest_whore.active:
            pc "Ah, err, I guess I am [wname]."
        else:
            pc "[name], nice to meet you."
            mira.name "[name]? So you don't work here?"
            pc "Err, looking for work. But this job, no. Not yet anyway..."
            mira.name "Yeah, no one really chooses this work."
            pc "I bet."
        mira.name "Well, she is done so I will gt back to work."
        pc "Be safe."
        hide mira with dissolve
        jump travel


    pcm "Wait... That's [mira.name]!"
    if player.has_perk(perk_whore):
        $ add_to_list(mira.list, "met_whore_mira_as_whore")
        pcm "Well, money has to come from somewhere. Didn't expect someone like her to be whoring here though."
        show mira worried at right1
        pc "Hey [mira.name]."
        mira.name "[name]! Errr, what are you doing here?"
        pc "Same as you probably."
        show mira neutral
        mira.name "What? Really?"
        pc "Got to make money somehow."
        mira.name "Yeah..."
        mira.name "Err... [name]. Don't tell [cass.nname]."
        pc "Of course not."
        mira.name "Thanks."
        hide mira with dissolve
    else:
        $ add_to_list(mira.list, "met_whore_mira")
        $ player.face_worried()
        pcm "What the fuck. She is dressed like a whore."
        pcm "And hanging out in a place where whores hang out..."
        pcm "Shit..."
        pcm "Err. Fuck."
        pcm "What do I do? Fuck fuck!"
        pcm "..."
        pcm "Shit she saw me!"
        show mira worried at right1 with dissolve
        mira.name "[name]!"
        pc "Err. Hi?"
        mira.name "Hi..."
        pc "Fancy meeting you round here. Gotta go!"
        mira.name "Wait."
        pc "Err, yeah?"
        mira.name "Don't tell [cass.nname]."
        pc "Yeah."
        hide mira with dissolve
        pcm "Well, that was unexpected."
        pcm "Wish I hadn't seen. This is going to be a bit awkward."
    jump travel

label mira_talk_subject:


    if not "whore_discover_talk" in mira.dict:
        $ mira.dict["whore_discover_talk"] = 0
    if not "whore_whore_talk" in mira.dict:
        $ mira.dict["whore_whore_talk"] = 0
    if not "whore_slut_talk" in mira.dict:
        $ mira.dict["whore_slut_talk"] = 0
    if not "whore_pre_aca_talk" in mira.dict:
        $ mira.dict["whore_pre_aca_talk"] = 0



    if not cass.has_met:
        pcm "Err, pretty sure that's who I think it is. [mira.wname] I think she said..."
        pcm "Better not speak to her here..."
        $ add_to_list(mira.list, "saw_at_academy")
        jump travel
    show mira at right1 with dissolve

    jump expression WeightedChoice([

    ("mira_talk_general_tombola", 20),

    
    ("mira_whore_discover_talk_" + str(mira.dict["whore_discover_talk"]), If(renpy.has_label("mira_whore_discover_talk_" + str(mira.dict["whore_discover_talk"])) and not "kidnapped" in mira.list and not cass_here() and dis(dis_truckstop) and not "met_before_academy" in mira.list, 500, 0)),
    ("mira_whore_pc_whore_" + str(mira.dict["whore_whore_talk"]), If(renpy.has_label("mira_whore_pc_whore_" + str(mira.dict["whore_whore_talk"])) and not "kidnapped" in mira.list and not cass_here() and dis(dis_truckstop) and player.has_perk(perk_whore), 100, 0)),
    ("mira_whore_pre_academy_" + str(mira.dict["whore_pre_aca_talk"]), If(renpy.has_label("mira_whore_pre_academy_" + str(mira.dict["whore_pre_aca_talk"])) and not "kidnapped" in mira.list and not cass_here() and "met_before_academy" in mira.list, 500, 0)),

    
    ("mira_talk_general_whore_slut_" + str(mira.dict["whore_slut_talk"]), If(renpy.has_label("mira_talk_general_whore_slut_" + str(mira.dict["whore_slut_talk"])) and not "kidnapped" in mira.list and not cass_here() and dis(dis_truckstop) and player.has_perk([perk_slut, perk_sucu, perk_bimbo]) and not player.has_perk(perk_whore), 100, 0)),

    ])

label mira_talk_end:
    if cass_here():
        jump cass_mira_talk_end
    $ relax(20, mira)
    $ dialouge = renpy.random.choice([
    "I hang out talking and joking about random stuff.",
    "I hang out for a while chatting and joking around about random topics.",
    "We hang out chatting and laughing about whatever comes up.",
    "We chat and have a bit of a laugh about random stuff."
    ])
    "[dialouge]"
    hide mira with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
