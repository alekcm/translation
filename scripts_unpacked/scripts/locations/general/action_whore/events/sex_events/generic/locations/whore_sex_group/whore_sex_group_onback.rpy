label whore_street_sex_group_onback_start_picker:
    "I head over to the bed, lay down and spread my legs."
    show sb_onback look_up happy relaxed with dissolve
    pc "Someone want to join?"
    jump expression WeightedChoice([
    ("whore_street_sex_group_onback_vag", 100),
    ("whore_street_sex_group_onback_anal", If(player.check_anal_agree(), 50, 0)),
    ])

label whore_street_sex_group_onback_picker:
    jump expression WeightedChoice([
    ("whore_street_sex_group_onback_vag", If(not ("vag" in player.sex_holes or "ass" in player.sex_holes) and player.sex_man_amount, 300, 0)),
    ("whore_street_sex_group_onback_vag_cont_sexonly", If(any(x in ["vag", "ass"] for x in player.sex_holes) and not any(x in ["lhand", "rhand", "mouth"] for x in player.sex_holes) , 150, 0)),
    ("whore_street_sex_group_onback_vag_cum_picker", If("vag" in player.sex_holes, 50, 0)),
    
    ("whore_street_sex_group_onback_anal", If(not ("vag" in player.sex_holes or "ass" in player.sex_holes) and player.sex_man_amount and player.check_anal_agree(), 300, 0)),
    ("whore_street_sex_group_onback_anal_cum_picker", If("ass" in player.sex_holes, 50, 0)),

    ("whore_street_sex_group_onback_facefuck", If(not "mouth" in player.sex_holes and player.sex_man_amount and not player.gagged, If(any(x in ["lhand", "rhand"] for x in player.sex_holes), 25, 100), 0)),
    ("whore_street_sex_group_onback_facefuck_continue", If("mouth" in player.sex_holes, 75, 0)),
    ("whore_street_sex_group_onback_facefuck_cum", If("mouth" in player.sex_holes, 50, 0)),

    ("whore_street_sex_group_onback_leftman_mast", If(not "lhand"in player.sex_holes and player.sex_man_amount, If("mouth" in player.sex_holes, 25, 100), 0)),
    ("whore_street_sex_group_onback_leftman_mast_cum", If("lhand" in player.sex_holes, 50, 0)),

    ("whore_street_sex_group_onback_rightman_mast", If(not "rhand" in player.sex_holes and player.sex_man_amount, If("mouth" in player.sex_holes, 25, 100), 0)),
    ("whore_street_sex_group_onback_rightman_mast_cum", If("rhand" in player.sex_holes, 50, 0)),

    
    ("whore_street_sex_group_onback_mating_switch", If(not any(x in ["lhand", "rhand", "mouth"] for x in player.sex_holes) and any(x in ["ass", "vag"] for x in player.sex_holes), 50, 0)),
    ("whore_street_sex_group_onback_hj_bukkake_switch", If(any(x in ["lhand", "rhand"] for x in player.sex_holes) and not any(x in ["ass", "vag", "mouth"] for x in player.sex_holes), 150, 0)), 

    ("whore_street_sex_group_watch_robin_picker", If(whore_street_sex_group_can_watch_robin(), 15, 0)),

    ("whore_street_sex_group_reset", If(player.sex_holes == [] and player.sex_man_amount, 1000, 0)),
    ])

label whore_street_sex_group_onback_vag:
    $ add_to_list(player.sex_holes, "vag")
    show sb_onback missionary with dissolve
    "[rlist.having_sex_tease_vag]"
    "[rlist.having_sex_penetrate_vag_slow]"
    show sb_onback happy
    $ player.sex_vag(tempname, quest_temp)
    $ player.face_excited()
    "[rlist.having_sex_action_onback]"
    "[rlist.having_sex_action_onback]"
    tempname.name "[rlist.having_sex_man_dirtytalk]"
    pc "[rlist.having_sex_yes]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_onback_vag_cont_sexonly:
    show sb_onbed sex with dissolve
    "[rlist.having_sex_action_onback]"
    "[rlist.having_sex_action_onback]"
    hide sb_onbed with dissolve
    jump whore_street_sex_group_picker

label whore_street_sex_group_onback_anal:
    $ add_to_list(player.sex_holes, "ass")
    show sb_onback missionary with dissolve
    $ player.sex_anal(tempname, quest_temp)
    "[rlist.having_sex_penetrate_ass_slow]"
    tempname.name "Ahhhhhh so warm."
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_action_ass]"
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_action_ass]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_onback_vag_cum_picker:
    $ player.sex_cum_location_offer(
    difficulty=5, choice_inside="Keep going!", choice_pullout="Not inside.",
    cum_want="whore_street_sex_group_onback_vag_cum_want", 
    cum_notwant="whore_street_sex_group_onback_vag_cum_notwant", 
    cum_pullout="whore_street_sex_group_onback_cum_pullout", 
    )

label whore_street_sex_group_onback_vag_cum_want:
    $ remove_from_list(player.sex_holes, "vag")

    if renpy.showing("sb_onback missionary") and (player.has_perk(perk_preg_want) and not numgen(0,3)) and not player.beingraped and not any(x in ["mouth", "lhand", "rhand"] for x in player.sex_holes):

        pc "[rlist.having_sex_pc_cum_inside_vag_want_dialogue]"
        show sb_onback lock
        "I wrap my legs around him, making sure he cannot escape and gives me what I want."
        pc "[rlist.having_sex_yes]"
        tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"
        $ player.sex_cum(tempname, "inside", quest_temp)
        "[rlist.having_sex_cumming_inside_vag_want_action]"
        pc "[rlist.having_sex_came_inside_vag_want]"
        show sb_onback relaxed happy with dissolve
        jump whore_street_sex_group_picker
    else:
        pc "[rlist.having_sex_pc_cum_inside_vag_want_dialogue]"
        pc "[rlist.having_sex_yes]"
        tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"
        $ player.sex_cum(tempname, "inside", quest_temp)
        "[rlist.having_sex_cumming_inside_vag_want_action]"
        pc "[rlist.having_sex_came_inside_vag_want]"

    show sb_onback no_sex with dissolve
    $ npc_race_picker_1()
    jump whore_street_sex_group_picker

label whore_street_sex_group_onback_vag_cum_notwant:
    $ remove_from_list(player.sex_holes, "vag")

    pc "[rlist.having_sex_pc_cum_pullout_ask_front]"
    tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"
    $ player.sex_cum(tempname, "inside", quest_temp)
    "[rlist.having_sex_cumming_inside_vag_notwant_action]"
    tempname.name "Ahh yes."
    pc "[rlist.having_sex_came_inside_vag_notwant_reaction]"
    pc "*Sigh*"
    show sb_onback no_sex with dissolve
    $ npc_race_picker_1()
    jump whore_street_sex_group_picker

label whore_street_sex_group_onback_cum_pullout:
    $ remove_from_list(player.sex_holes, ["vag", "ass"])
    pc "[rlist.having_sex_pc_cum_pullout_ask]"
    tempname.name "[rlist.having_sex_cumming_pullout_man_dialogue]"
    $ player.sex_cum(tempname, "belly", quest_temp)
    "[rlist.having_sex_cumming_pullout_action]"
    tempname.name "Ahh yes!"
    pc "[rlist.having_sex_cumming_pullout_reaction]"
    show sb_onback no_sex with dissolve
    $ npc_race_picker_1()
    jump whore_street_sex_group_picker

label whore_street_sex_group_onback_ass_cum:
    $ remove_from_list(player.sex_holes, "ass")
    pc "[rlist.having_sex_yes]"
    tempname.name "[rlist.having_sex_man_cum_inside_ass_dialogue]"
    $ player.sex_cum(tempname, "anal", quest_temp)
    "[rlist.having_sex_cumming_inside_ass_want_action]"
    tempname.name "Ahh yes."
    pc "[rlist.having_sex_came_inside_ass_want]"
    show sb_onback no_sex with dissolve
    $ npc_race_picker_1()
    jump whore_street_sex_group_picker

label whore_street_sex_group_onback_anal_cum_picker:

    jump expression WeightedChoice([
    ("whore_street_sex_group_onback_ass_cum", 100),
    ("whore_street_sex_group_onback_cum_pullout", 75),
    ])



label whore_street_sex_group_onback_facefuck:
    $ add_to_list(player.sex_holes, "mouth")
    "One of the guys clumbs on the bed, straddles my face and puts his cock in my mouth."
    show sb_onback facefuck with dissolve
    $ player.sex_oral(tempname, quest_temp)
    tempname.name "[rlist.having_sex_man_yes]"
    "[rlist.blowjob_start_suck_reaction]"
    show sb_onback blow with dissolve
    pc "[rlist.blowjob_muffle]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_onback_facefuck_continue:
    $ npc_race_switch()
    show sb_facefuck blow with dissolve
    pc "[rlist.blowjob_muffle]"
    show sb_facefuck deep closed with hpunch
    "The guy shoves his cock deep in my mouth and starts to fuck my face."
    "He pays little attention to if I am enjoying it and keeps going deep in my mouth."
    show sb_facefuck blow squint with dissolve
    "Eventually he eases up and I can breathe again."
    hide sb_facefuck with dissolve
    $ npc_race_switch()
    jump whore_street_sex_group_picker

label whore_street_sex_group_onback_facefuck_cum:
    $ remove_from_list(player.sex_holes, "mouth")
    tempname.name "[rlist.having_sex_man_close_dialogue]"
    show sb_onback facefuck_deep with dissolve
    tempname.name "[rlist.blowjob_cum_mouth_man_dialogue]"
    $ player.sex_cum(tempname, "mouth", quest_temp)
    "[rlist.blowjob_cum_mouth]"
    tempname.name "[rlist.having_sex_man_yes]"
    pc "[rlist.blowjob_muffle]"
    show sb_onback facefuck with dissolve
    show sb_onback no_facefuck with dissolve
    pc "[rlist.blowjob_cum_mouth_swallow_reaction]"
    tempname.name "[rlist.blowjob_cum_mouth_swallow_reaction_man]"
    jump whore_street_sex_group_picker



label whore_street_sex_group_onback_leftman_mast:
    $ add_to_list(player.sex_holes, "lhand")
    show sb_onback man_left with dissolve
    $ player.sex_hand(tempname, quest_temp)
    "One of the guys comes up and starts touching my tits while wanking off."
    show sb_onback l_penis with dissolve
    "I grab hold of his cock and start stroking him so he can use his hands to touch me."
    jump whore_street_sex_group_picker

label whore_street_sex_group_onback_leftman_mast_cum:
    $ remove_from_list(player.sex_holes, "lhand")
    $ player.sex_cum(tempname, "belly", quest_temp)
    "I don't even realise what's going on until I feel my hand getting wet and sticky. And before I know it, warm liquid is spraying on my belly."
    pc "[rlist.handjob_man_cum]"
    tempname.name "[rlist.handjob_wank_man_say_enjoy]"
    show sb_onback no_man_left with dissolve
    jump whore_street_sex_group_picker

label whore_street_sex_group_onback_rightman_mast:
    $ add_to_list(player.sex_holes, "rhand")
    show sb_onback man_right with dissolve
    "One of the guys comes up to me while wanking."
    $ player.sex_hand(tempname, quest_temp)
    show sb_onback r_penis with dissolve
    "I take his cock in my hand and help him out. Rubbing up and down his shaft, leaving his hands free to touch my body."
    jump whore_street_sex_group_picker

label whore_street_sex_group_onback_rightman_mast_cum:
    $ remove_from_list(player.sex_holes, "rhand")
    $ player.sex_cum(tempname, "chest", quest_temp)
    "I feel his cock start to get slick, then start pumping his cum all over my tits."
    pc "[rlist.handjob_man_cum]"
    tempname.name "[rlist.handjob_man_cum_yes_dialogue]"
    show sb_onback no_man_right with dissolve
    jump whore_street_sex_group_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
