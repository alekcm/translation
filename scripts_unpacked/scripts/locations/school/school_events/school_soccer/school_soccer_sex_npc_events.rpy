init python:
    def school_soccer_npc_sex_end():
        for i in [robin, dan, nate, drake]:
            remove_from_list(i.list, "soccer_sex_robin")

    def school_soccer_npc_sex_boy_who():
        for i in [dan, nate, drake]:
            if "soccer_sex_robin" in i.list:
                return i
        else: 
            return nate    

    def school_soccer_npc_nosex_boy_who():
        who_list = [dan, nate, drake]
        for i in who_list:
            if "soccer_sex_robin" in i.list or "soccer_sex_rachel" in i.list:
                who_list.remove(i)
        return random(who_list)

    def school_soccer_npc_sex_robin_pick():
        if robin_here(loc_school_field_back) and not "soccer_sex_robin" in robin.list and "soccerboys_can_sex" in robin.list and not numgen(0,10):
            boy_list = []
            for i in (drake, nate, dan):
                if not "soccer_sex_rachel" in i.list:
                    boy_list.append(i)
            add_to_list(robin.list, "soccer_sex_robin")
            add_to_list(random(boy_list).list, "soccer_sex_robin")
        elif "soccer_sex_robin" in robin.list and not numgen(0,3):
            robin.have_sex(school_soccer_npc_sex_robin_boy_who())
            school_soccer_npc_sex_robin_end()

    def school_soccer_npc_sex_robin_end():
        for i in [robin, dan, nate, drake]:
            remove_from_list(i.list, "soccer_sex_robin")

    def school_soccer_npc_sex_robin_boy_who():
        for i in [dan, nate, drake]:
            if "soccer_sex_robin" in i.list:
                return i
        else: 
            return nate 

    def school_soccer_npc_sex_rachel_pick():
        if rachel_here(loc_school_field_back) and not "soccer_sex_rachel" in rachel.list and "soccer_free_use" in rachel.list and not numgen(0,10):
            boy_list = []
            for i in (drake, nate, dan):
                if not "soccer_sex_rachel" in i.list:
                    boy_list.append(i)
            add_to_list(rachel.list, "soccer_sex_rachel")
            add_to_list(random(boy_list).list, "soccer_sex_rachel")
        elif "soccer_sex_rachel" in rachel.list and not numgen(0,3):
            rachel.have_sex(school_soccer_npc_sex_rachel_boy_who())
            school_soccer_npc_sex_rachel_end()

    def school_soccer_npc_sex_rachel_end():
        for i in [rachel, dan, nate, drake]:
            remove_from_list(i.list, "soccer_sex_rachel")

    def school_soccer_npc_sex_rachel_boy_who():
        for i in [dan, nate, drake]:
            if "soccer_sex_rachel" in i.list:
                return i
        else: 
            return nate 

label school_field_soccer_sex_robin_spy:
    $ player.face_shy()
    $ tempname = school_soccer_npc_sex_robin_boy_who()
    $ npc_race_picker(tempname)
    if not robin_here():
        pcm "Hmm, that dirty [robin.name] sneaked off with [tempname.name]..."
        pcm "I should make sure she is ok. ♥"
        $ walk(robin_here(class_loc=True))
    else:
        pcm "[robin.name] looks like she is having fun..."
    $ robin.have_sex(tempname)
    if t.minute > 30:
        jump school_field_soccer_sex_robin_spy_blow
    else:
        jump school_field_soccer_sex_robin_spy_sex

label school_field_soccer_sex_robin_spy_blow:
    $ tempname = school_soccer_npc_sex_robin_boy_who()
    $ dialogue = WeightedChoice([
    ("Ah, you perverted bitch sucking him off.", 1),
    ("Finally giving that slut what she has been asking for?", 1),
    ("Ooh? What have we here?", 1),
    ("Oh? Sucking off another pervert?", 1),
    ])
    pc "[dialogue]"
    show robin_blowjob with dissolve
    $ dialogue = WeightedChoice([
    ("That's right " + tempname.setname + ". Shove it down her throat.", 1),
    ("Mmmm, gonna swallow up all his cum?", 1),
    ("She has been asking for this for a long time hasn't she?", 1),
    ("Make sure to give her something tasty.", 1),
    ])
    pc "[dialogue]"
    jump school_field_soccer_sex_robin_spy_sex_start

label school_field_soccer_sex_robin_spy_sex:
    $ tempname = school_soccer_npc_sex_robin_boy_who()
    $ dialogue = WeightedChoice([
    ("Ah, you perverted bitch letting him fuck you like that.", 1),
    ("Finally giving that slut what she has been asking for?", 1),
    ("Ooh? What have we here?", 1),
    ("Oh? Some perverts are fucking each other?", 1),
    ])
    pc "[dialogue]"
    $ renpy.show(random(["robin_againstwall", "robin_doggy"]))
    $ dialogue = WeightedChoice([
    ("That's right " + tempname.setname + ". Fuck her like the slut she is.", 1),
    ("Mmmm, gonna take his cum in you?", 1),
    ("She has been asking for this for a long time hasn't she?", 1),
    ("Make sure to give her something good inside.", 1),
    ])
    pc "[dialogue]"
    jump school_field_soccer_sex_robin_spy_sex_start

label school_field_soccer_sex_robin_spy_sex_pc_strip:
    $ pc_striptease()
    if numgen():
        show sb_pose_showbreasts happy at rightover with dissolve
        pc "[rlist.foreplay_like_boobs_ask]"
    else:
        show sb_pose_lookback happy at rightover with dissolve
        pc "[rlist.foreplay_like_ass_ask]"
    return

label school_field_soccer_sex_robin_spy_sex_start:
    if not c.nude:
        pc "Want something fun to look at while you are fucking her?"
        call school_field_soccer_sex_robin_spy_sex_pc_strip from _call_school_field_soccer_sex_robin_spy_sex_pc_strip
    pc "Mmmmm..."
    hide sb_pose_showbreasts
    hide sb_pose_lookback
    $ renpy.show(random(["sb_mast_stand", "sb_pose_upvag"]), [rightover])
    with dissolve
    $ player.masturbate(True)
    $ if_showing("sb_pose_upvag", "mast")
    pc "Mmm. Keep giving that slut your cock."
    jump expression WeightedChoice([
    ("school_field_soccer_sex_robin_spy_sex_leave", If(player.desire <= 50, 5000, 0)),
    ("school_field_soccer_sex_robin_spy_sex_mast", 100),
    ("school_field_soccer_sex_robin_spy_sex_switch", 100),
    ])

label school_field_soccer_sex_robin_spy_sex_leave:
    pc "Oh? Giving [tempname.name] a good time?"
    pc "Slut!"
    $ walk(loc_school_field_back)
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_sex_robin_spy_sex_mast:
    pc "Keep going [tempname.name]!"
    pc "She kicks your ass at football, so now you can show her who is the boss."
    robin.name "[name]!"
    pc "Shush! Take his cock."
    pc "These boys have been wanting to put their dick in you since you met them."
    pc "Had to be me to convince you to let them."
    $ player.masturbate_cum()
    pcm "Fuck yes! Yes! Haaaa..."
    pcm "..."
    $ player.masturbate_end()
    $ renpy.scene()
    with dissolve
    pc "Ha, I'll leave you to it you dirty girl."
    $ pc_dress_slow()
    $ walk(loc_school_field_back)
    pcm "Hehe."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_sex_robin_spy_sex_switch:
    pc "Keep going [tempname.name]!"
    pc "She kicks your ass at football, so now you can show her who is the boss."
    robin.name "[name]!"
    pc "Shush! Take his cock."
    hide robin_againstwall
    hide robin_doggy
    hide robin_blowjob
    with dissolve
    $ add_to_list(robin.list, "no_location")
    pc "These boys have been wanting to put their dick in you since you met them."
    $ quest_temp = None
    $ event_end_interrupt_label = "school_field_soccer_sex_robin_spy_sex_end"
    $ player.face_shock()
    $ player.masturbate_end()
    $ renpy.scene()
    if numgen():
        $ renpy.show(renpy.random.choice(["sb_onfours poke", "sb_doggy1 poke", "sb_doggy2 pokevaghold"]))
        with hpunch
        pc "Ah!"
        robin.name "Haha, slut!"
        robin.name "You get fucked."
        jump whore_street_sex_floor_vag_picker
    else:
        $ renpy.show(renpy.random.choice(["sb_againstwall2 pokeasshand wink worried", "sb_againstwall3 poke wink", "sb_table bentover happy mast"]))
        with hpunch
        pc "Ah!"
        robin.name "Haha, slut!"
        robin.name "You get fucked."
        jump whore_street_sex_standing_vag_picker

label school_field_soccer_sex_robin_spy_sex_end:
    $ renpy.scene()
    show robin happy nude at right1
    with dissolve
    pc "Ugh. Was supposed to be you getting fucked."
    robin.name "Ha, your own fault for being a pervert and wanting to watch."
    pc "Ugh..."
    $ pc_dress_slow()
    $ remove_from_list(robin.list, "no_location")
    $ school_soccer_npc_sex_robin_end()
    hide robin with dissolve
    $ walk(loc_school_field_back)
    jump school_field_soccer_hangout_conv_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
