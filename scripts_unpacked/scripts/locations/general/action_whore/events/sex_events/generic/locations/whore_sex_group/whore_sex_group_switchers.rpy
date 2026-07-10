label whore_street_sex_group_onback_hj_bukkake_switch:
    if not player.gagged and ("lhand" in player.sex_holes or "rhand" in player.sex_holes):
        if "lhand" in player.sex_holes:
            $ remove_from_list(player.sex_holes, "lhand")
            $ add_to_list(player.sex_holes, "mouth")
            $ npc_race_switch()
        else:
            $ remove_from_list(player.sex_holes, "rhand")
            $ add_to_list(player.sex_holes, "mouth")
            $ npc_race_switch(npc_race, npc_race3)
        "Without anyone taking me from behind, I take the guy I am wanking off into my mouth."
        $ renpy.scene()
        show sb_blowjob 1h poke
        with dissolve
        show sb_blowjob suck
    elif "lhand" in player.sex_holes or "rhand" in player.sex_holes:
        $ renpy.scene()

        if "lhand" in player.sex_holes and "rhand" in player.sex_holes:
            show sb_blowjob man_left man_right
            with dissolve
        elif "lhand" in player.sex_holes:
            show sb_blowjob man_left
            with dissolve
        else:
            show sb_blowjob man_right
            with dissolve

        "Without anyone taking me from behind, I use my hands to wank the guys off."
    else:
        $ renpy.scene()
        show sb_blowjob
        with dissolve
        "With no one left, I relax a bit and wait for someone else."
    jump whore_street_sex_group_picker

label whore_street_sex_group_onfours_hj_bukkake_switch:
    if not player.gagged and ("lhand" in player.sex_holes or "rhand" in player.sex_holes):
        if "lhand" in player.sex_holes:
            $ remove_from_list(player.sex_holes, "lhand")
            $ add_to_list(player.sex_holes, "mouth")
            $ npc_race_switch()
        else:
            $ remove_from_list(player.sex_holes, "rhand")
            $ add_to_list(player.sex_holes, "mouth")
            $ npc_race_switch(npc_race, npc_race3)
        "Without anyone taking me from behind, I take the guy I am wanking off into my mouth."
        $ renpy.scene()
        show sb_blowjob 1h poke
        with dissolve
        show sb_blowjob suck
    elif "lhand" in player.sex_holes or "rhand" in player.sex_holes:
        $ renpy.scene()

        if "lhand" in player.sex_holes and "rhand" in player.sex_holes:
            show sb_blowjob man_left man_right
            with dissolve
        elif "lhand" in player.sex_holes:
            show sb_blowjob man_left
            with dissolve
        else:
            show sb_blowjob man_right
            with dissolve

        "Without anyone taking me from behind, I use my hands to wank the guys off."
    else:
        $ renpy.scene()
        show sb_blowjob
        with dissolve
        "With no one left, I relax a bit and wait for someone else."
    jump whore_street_sex_group_picker

label whore_street_sex_group_buk_fours_switch:
    "I feel a guy coming up behind me and put his hands between my legs."
    $ renpy.scene()
    if "lhand" in player.sex_holes and "rhand" in player.sex_holes:
        show sb_onfours grope man_front man_side
    elif "rhand" in player.sex_holes:
        show sb_onfours grope man_front
    elif "lhand" in player.sex_holes:
        show sb_onfours grope man_side
    else:
        show sb_onfours grope
    with dissolve
    tempname.name "[rlist.having_sex_man_dirtytalk]"
    pc "[rlist.having_sex_mmm]"
    "I wiggle my bum some more, inviting him to do something a bit deeper."
    show sb_onfours noman with dissolve
    jump expression WeightedChoice([
    ("whore_street_sex_group_onfours_vag", 100),
    ("whore_street_sex_group_onfours_anal", If(not player.has_perk(perk_buttplug), 100, 0)),
    ])

label whore_street_sex_group_buk_back_switch:


    if "lhand" in player.sex_holes and "rhand" in player.sex_holes:
        "Without anyone pressing on top of me, I adjust myself better to wank the guys off."
        $ renpy.scene()
        show sb_onback man_left r_penis l_penis man_right
    elif "lhand" in player.sex_holes or "rhand" in player.sex_holes:
        if "lhand" in player.sex_holes:
            $ remove_from_list(player.sex_holes, "lhand")
            $ add_to_list(player.sex_holes, "mouth")
            $ npc_race_switch()
        else:
            $ remove_from_list(player.sex_holes, "rhand")
            $ add_to_list(player.sex_holes, "mouth")
            $ npc_race_switch(npc_race, npc_race3)
        "Without anyone taking me from behind, I take the guy I am wanking off into my mouth."
        $ renpy.scene()
        show sb_blowjob 1h poke
        with dissolve
        show sb_blowjob suck
    else:
        $ renpy.scene()
        show sb_blowjob
        with dissolve
        "With no one left, I relax a bit and wait for someone else."
    jump whore_street_sex_group_picker

label whore_street_sex_group_bukkake_mouth_facefuck_switch:
    "The guy pushes his cock deep in my mouth and pushes me onto the bed."
    $ renpy.scene()
    show sb_facefuck deep
    with dissolve
    tempname.name "[rlist.having_sex_man_yes]"
    "[rlist.blowjob_start_suck_reaction]"
    pc "[rlist.blowjob_muffle]"
    $ renpy.scene()
    show sb_onback facefuck_deep
    with dissolve
    show sb_onback facefuck with dissolve
    jump whore_street_sex_group_picker

label whore_street_sex_group_standing_dp_switch:
    "A guy comes in front of me, so I lift my leg up to give him access"
    $ renpy.scene()
    show sb_dpstand banal
    with dissolve
    jump whore_street_sex_group_standing_dp_vag

label whore_street_sex_group_dp_onback_switch:
    "The guy presses me forward and shoves me on the bed, cock still inside me."
    $ renpy.scene()
    show sb_onback missionary look_down ooh
    with dissolve
    "[rlist.having_sex_action_onback]"
    "[rlist.having_sex_action_onback]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_dp_doggy_switch:
    "The guy pushes my back and bends me over, still fucking me in the ass as he does."
    $ renpy.scene()
    show sb_doggy1 anal shock with dissolve
    with dissolve
    "[rlist.having_sex_action]"
    "[rlist.having_sex_action]"
    show sb_doggy1 ag
    jump whore_street_sex_group_picker

label whore_street_sex_group_3p_cow_spit_switch:
    "With the guy I am sitting on done, I lift my ass up so he can shuffle away."
    $ temp_var_1 = ""
    if "ass" in player.sex_holes and "mouth" in player.sex_holes:
        $ temp_var_1 = "anal blow"
    elif "mouth" in player.sex_holes:
        $ temp_var_1 = "blow"
    elif "ass" in player.sex_holes:
        $ temp_var_1 = "anal"
    $ renpy.scene()
    $ renpy.show("sb_doggy1 " + temp_var_1)
    with dissolve
    jump whore_street_sex_group_picker

label whore_street_sex_group_lay_doggy_switch:
    $ renpy.scene()
    if "vag" in player.sex_holes:
        show sb_doggy1 vag
    elif "ass" in player.sex_holes:
        show sb_doggy1 anal
    else:
        show sb_doggy1
    with dissolve
    "With the guy I was sucking done, I lift my body up and let him get out the way."
    jump whore_street_sex_group_picker

label whore_street_sex_group_stand_doggy_switch:
    "The guy is pawing away at me and starts pushing me onto the floor."
    $ renpy.scene()
    if "vag" in player.sex_holes:
        show sb_doggy1 vag
    else:
        show sb_doggy1 anal
    with dissolve
    jump whore_street_sex_group_picker

label whore_street_sex_group_pronesex_switch:
    "The guy behind me is fucking me harder and pressing down on my ass."
    $ renpy.scene()
    $ renpy.show(renpy.random.choice(["sb_onbelly lay_sex back happy", "sb_onbelly sex grope back happy"]))
    with vpunch
    pc "Having fun back there?"
    if "vag" in player.sex_holes:
        jump whore_street_sex_group_pronesex_vag_cum_picker
    else:
        jump whore_street_sex_group_pronesex_anal_cum_picker

label whore_street_sex_group_blow_assup_switch:
    "I feel a guy pressing me from behind, so I relax and let him position me."
    $ renpy.scene()
    show sb_layblow
    with dissolve
    show sb_layblow sex with dissolve
    "He gets behind me and starts touching me, and I can feel him wanking off a bit."
    show sb_layblow blow with dissolve
    "But I just carry on sucking the guy in front of me and let the guy behind do what he wants."
    jump expression WeightedChoice([
    ("whore_street_sex_group_spitroast_layblow_vag", 100),
    ("whore_street_sex_group_spitroast_layblow_anal", 50),
    ])

label whore_street_sex_group_standing_switch:
    "The guy starts pulling me up into a standing position and I try to get to my feet."
    $ renpy.scene()
    with dissolve
    pc "This would be easier if you would stop fucking me while you pick me up."
    show sb_standbehind happy with dissolve
    jump whore_street_sex_group_standing_cont

label whore_street_sex_group_onback_mating_switch:
    "With my hands free, I use them to lift and spread my legs, giving the guy fucking me better access."
    $ renpy.scene()
    if "vag" in player.sex_holes:
        show sb_matingpress oh down vag
    else:
        show sb_matingpress oh down anal
    with dissolve
    "[rlist.having_sex_action_onback]"
    "[rlist.having_sex_action_onback]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_mating_onback_switch:
    "I get a bit tired in this position, so relax back a little."
    $ renpy.scene()
    show sb_onback missionary look_down ah
    "[rlist.having_sex_action_onback]"
    "[rlist.having_sex_action_onback]"
    jump whore_street_sex_group_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
