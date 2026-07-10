label whore_street_sex_group_bukkake_start_picker:
    "I get down on my knees and watch the guy as he wanks his cock, getting it hard."
    jump expression WeightedChoice([
    ("whore_street_sex_group_bukkake_mouth", If(not player.gagged, 100, 0)),
    ("whore_street_sex_group_bukkake_leftman", 100),
    ("whore_street_sex_group_bukkake_rightman", 100),
    ])

label whore_street_sex_group_bukkake_picker:
    jump expression WeightedChoice([
    ("whore_street_sex_group_bukkake_mouth", If(not "mouth" in player.sex_holes and player.sex_man_amount and not player.gagged, 200, 0)),
    ("whore_street_sex_group_bukkake_mouth_cum", If("mouth" in player.sex_holes, 50, 0)),

    ("whore_street_sex_group_bukkake_leftman", If(not "rhand" in player.sex_holes and player.sex_man_amount, 100, 0)),
    ("whore_street_sex_group_bukkake_leftman_cum", If("rhand" in player.sex_holes, 50, 0)),

    ("whore_street_sex_group_bukkake_rightman", If(not "lhand" in player.sex_holes and player.sex_man_amount, 100, 0)),
    ("whore_street_sex_group_bukkake_rightman_cum", If("lhand" in player.sex_holes, 50, 0)),

    ("whore_street_sex_group_blow_assup_switch", If("mouth" in player.sex_holes and not ("lhand" in player.sex_holes or "rhand" in player.sex_holes) and player.sex_man_amount, 100, 0)),
    
    ("whore_street_sex_group_buk_fours_switch", If(not any(x in ["vag", "ass", "mouth"] for x in player.sex_holes) and player.sex_man_amount, 100, 0)),

    ("whore_street_sex_group_watch_robin_picker", If(whore_street_sex_group_can_watch_robin(), 15, 0)),

    ("whore_street_sex_group_reset", If(player.sex_holes == [] and player.sex_man_amount, 10000, 0)),
    ])

label whore_street_sex_group_bukkake_mouth:
    $ add_to_list(player.sex_holes, "mouth")
    jump expression WeightedChoice([
    ("whore_street_sex_group_bukkake_mouth_suck", 100),
    ("whore_street_sex_group_bukkake_mouth_slap", 50),
    ("whore_street_sex_group_bukkake_mouth_shove", 50),
    ])

label whore_street_sex_group_bukkake_mouth_suck:
    show sb_blowjob poke down smile with dissolve
    pc "[rlist.foreplay_nice_cock]"
    show sb_blowjob 2h swallow up with dissolve
    show sb_blowjob suck with dissolve
    $ player.sex_oral(tempname, quest_temp)
    "[rlist.blowjob_start_suck]"
    tempname.name "[rlist.having_sex_man_yes]"
    "[rlist.blowjob_start_suck_reaction]"
    $ if_showing("sb_blowjob", "up", "sb_spitroast", "up", "sb_layblow", "forward")
    pc "[rlist.blowjob_muffle]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_bukkake_mouth_slap:
    show sb_blowjob face shock with hpunch
    "Without warning, I am slapped in the face by the guy's cock."
    pc "Oi."
    show sb_blowjob 2h poke down frown with dissolve
    show sb_blowjob swallow up with dissolve
    show sb_blowjob suck with dissolve
    $ player.sex_oral(tempname, quest_temp)
    "[rlist.blowjob_start_suck]"
    tempname.name "[rlist.having_sex_man_yes]"
    "[rlist.blowjob_start_suck_reaction]"
    $ if_showing("sb_blowjob", "up", "sb_spitroast", "up", "sb_layblow", "forward")
    pc "[rlist.blowjob_muffle]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_bukkake_mouth_shove:
    show sb_blowjob poke down frown with hpunch
    "Without warning, I am poked in the face by a cock."
    show sb_blowjob 2h suck with hpunch
    $ player.sex_oral(tempname, quest_temp)
    pc "Mmmmf!"
    "[rlist.blowjob_start_suck]"
    tempname.name "[rlist.having_sex_man_yes]"
    "[rlist.blowjob_start_suck_reaction]"
    $ if_showing("sb_blowjob", "up", "sb_spitroast", "up", "sb_layblow", "forward")
    pc "[rlist.blowjob_muffle]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_bukkake_mouth_cum:
    $ remove_from_list(player.sex_holes, "mouth")
    show sb_blowjob down suck 2h with dissolve
    tempname.name "[rlist.having_sex_man_keep_going]"
    "[rlist.blowjob_cum_close]"
    tempname.name "[rlist.having_sex_man_close_dialogue]"
    show sb_blowjob angry closed with dissolve
    tempname.name "[rlist.blowjob_cum_mouth_man_dialogue]"
    $ player.sex_cum(tempname, "mouth", quest_temp)

    "[rlist.blowjob_cum_mouth]"
    tempname.name "[rlist.having_sex_man_yes]"
    pc "[rlist.blowjob_muffle]"
    show sb_blowjob 0h poke up happy ub with dissolve
    show sb_blowjob laugh with dissolve
    pc "[rlist.blowjob_cum_mouth_swallow_reaction]"
    tempname.name "[rlist.blowjob_cum_mouth_swallow_reaction_man]"

    show sb_blowjob noman with dissolve
    jump whore_street_sex_group_picker



label whore_street_sex_group_bukkake_leftman:
    $ add_to_list(player.sex_holes, "rhand")
    show sb_blowjob man_left with dissolve
    "A guy comes up to me and starts wanking, so I take his cock in my hand to help him out."
    if not renpy.showing("sb_blowjob 0h"):
        show sb_blowjob 0h with dissolve
    $ player.sex_hand(tempname, quest_temp)
    pc "[rlist.handjob_touch_cock]"
    "[rlist.handjob_wank_cock]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_bukkake_leftman_cum:
    $ remove_from_list(player.sex_holes, "rhand")
    "Someone seems like they are close, so i start wanking them off fast."
    pc "[rlist.handjob_wank_pc_say_man_close]"
    tempname.name "[rlist.handjob_wank_man_say_enjoy]"
    $ player.sex_cum(tempname, "face", quest_temp)
    "[rlist.handjob_man_cum_action_face]"
    pc "[rlist.handjob_pc_cum_reaction]"
    show sb_blowjob noman_left with dissolve
    jump whore_street_sex_group_picker

label whore_street_sex_group_bukkake_rightman:
    $ add_to_list(player.sex_holes, "lhand")

    show sb_blowjob man_right with dissolve
    "One guy walks up to me while wanking and starts poking his cock in my face."
    if not renpy.showing("sb_blowjob 0h"):
        show sb_blowjob 0h with dissolve
    $ player.sex_hand(tempname, quest_temp)
    pc "[rlist.handjob_touch_cock]"
    "[rlist.handjob_wank_cock]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_bukkake_rightman_cum:
    $ remove_from_list(player.sex_holes, "lhand")
    pc "Ready to cum are you?"
    pc "[rlist.handjob_wank_pc_say_man_close]"
    tempname.name "[rlist.handjob_wank_man_say_enjoy]"
    $ player.sex_cum(tempname, "face", quest_temp)
    "[rlist.handjob_man_cum_action_face]"
    pc "[rlist.handjob_pc_cum_reaction]"
    show sb_blowjob noman_right with dissolve
    jump whore_street_sex_group_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
