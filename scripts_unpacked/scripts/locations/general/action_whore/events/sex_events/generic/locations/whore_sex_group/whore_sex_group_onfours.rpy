label whore_street_sex_group_onfours_start_picker:
    show sb_onfours with dissolve
    "I get down on the floor and wiggle my ass at the guys."
    jump expression WeightedChoice([
    ("whore_street_sex_group_onfours_vag", 100),
    ("whore_street_sex_group_onfours_anal", If(player.check_anal_agree(), 50, 0)),
    ])

label whore_street_sex_group_onfours_picker:
    jump expression WeightedChoice([
    ("whore_street_sex_group_onfours_vag", If(not any(x in ["vag", "ass"] for x in player.sex_holes) and player.sex_man_amount, 100, 0)),
    ("whore_street_sex_group_onfours_vag_cont", If("vag" in player.sex_holes, 100, 0)),
    ("whore_street_sex_group_onfours_vag_cum_picker", If("vag" in player.sex_holes, 50, 0)),
    
    ("whore_street_sex_group_onfours_anal", If(not any(x in ["vag", "ass"] for x in player.sex_holes) and player.sex_man_amount and player.check_anal_agree(), 100, 0)),
    ("whore_street_sex_group_onfours_anal_cont", If("ass" in player.sex_holes, 100, 0)),
    ("whore_street_sex_group_onfours_anal_cum_picker", If("ass" in player.sex_holes, 50, 0)),

    ("whore_street_sex_group_onfours_leftman", If(not "rhand" in player.sex_holes and player.sex_man_amount, 100, 0)),
    ("whore_street_sex_group_onfours_leftman_cum", If("rhand" in player.sex_holes, 50, 0)),

    ("whore_street_sex_group_onfours_rightman", If(not "lhand" in player.sex_holes and player.sex_man_amount, 100, 0)),
    ("whore_street_sex_group_onfours_rightman_cum", If("lhand" in player.sex_holes, 50, 0)),

    ("whore_street_sex_group_onfours_wank_cont", If(any(x in ["lhand", "rhand"] for x in player.sex_holes), 50, 0)),

    ("whore_street_sex_group_onfours_hj_bukkake_switch", If(any(x in ["lhand", "rhand"] for x in player.sex_holes) and not any(x in ["ass", "vag"] for x in player.sex_holes), 100, 0)),
    
    ("whore_street_sex_group_spank", If(any(x in ["ass", "vag"] for x in player.sex_holes), 25, 0)),
    ("whore_street_sex_group_sexytalk", If(any(x in ["ass", "vag", "mouth"] for x in player.sex_holes), 25, 0)),
    ("whore_street_sex_group_beat", If(any(x in ["ass", "vag", "mouth"] for x in player.sex_holes) and player.beingraped, 25, 0)),
    ("whore_street_sex_group_plug_remove", If(acc.anus and player.sex_man_amount > 3, 25, 0)),
    
    ("whore_street_sex_group_watch_robin_picker", If(whore_street_sex_group_can_watch_robin(), 15, 0)),

    ("whore_street_sex_group_reset", If(player.sex_holes == [] and player.sex_man_amount, 1000, 0)),
    ])


label whore_street_sex_group_onfours_vag:
    $ add_to_list(player.sex_holes, "vag")
    show sb_onfours poke with dissolve
    "[rlist.having_sex_tease_vag]"
    "[rlist.having_sex_penetrate_vag_slow]"
    show sb_onfours vag with dissolve
    $ player.sex_vag(tempname, quest_temp)
    $ player.face_excited()
    "[rlist.having_sex_action]"
    tempname.name "[rlist.having_sex_man_dirtytalk]"
    pc "[rlist.having_sex_yes]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_onfours_vag_cont:
    tempname.name "[rlist.having_sex_man_dirtytalk]"
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_enjoy]"
    $ player.face_orgasm()
    pc "[rlist.having_sex_yes]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_onfours_anal:
    $ add_to_list(player.sex_holes, "ass")
    show sb_onfours poke with dissolve
    "[rlist.having_sex_vag_to_ass_switch]"
    "[rlist.having_sex_penetrate_ass_slow]"
    show sb_onfours ass with dissolve
    $ player.sex_anal(tempname, quest_temp)
    $ player.face_excited()
    tempname.name "Ahhhhhh so warm."
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_action_ass]"
    pc "[rlist.having_sex_yes]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_onfours_anal_cont:
    jump whore_street_sex_group_onfours_vag_cont



label whore_street_sex_group_onfours_vag_cum_picker:
    $ player.sex_cum_location_offer(
    difficulty=5, choice_inside="Keep going!", choice_pullout="Not inside.",
    cum_want="whore_street_sex_group_onfours_vag_cum_want", 
    cum_notwant="whore_street_sex_group_onfours_vag_cum_notwant", 
    cum_pullout="whore_street_sex_group_onfours_cum_pullout", 
    )

label whore_street_sex_group_onfours_vag_cum_want:
    $ remove_from_list(player.sex_holes, "vag")
    pc "[rlist.having_sex_yes]"
    tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"
    $ player.sex_cum(tempname, "inside", quest_temp)
    "[rlist.having_sex_cumming_inside_vag_want_action]"
    pc "[rlist.having_sex_yes]"
    pc "[rlist.having_sex_came_inside_vag_want]"
    show sb_onfours noman with dissolve
    $ npc_race_picker_1()
    jump whore_street_sex_group_picker

label whore_street_sex_group_onfours_vag_cum_notwant:
    $ remove_from_list(player.sex_holes, "vag")
    pc "[rlist.having_sex_yes]"
    tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"
    $ player.sex_cum(tempname, "inside", quest_temp)
    "[rlist.having_sex_cumming_inside_vag_notwant_action]"
    pc "[rlist.having_sex_yes]"
    pc "[rlist.having_sex_came_inside_vag_want]"
    show sb_onfours noman with dissolve
    $ npc_race_picker_1()
    jump whore_street_sex_group_picker

label whore_street_sex_group_onfours_ass_cum:
    $ remove_from_list(player.sex_holes, "ass")
    pc "[rlist.having_sex_yes]"
    tempname.name "[rlist.having_sex_man_cum_inside_ass_dialogue]"
    $ player.sex_cum(tempname, "anal", quest_temp)
    "[rlist.having_sex_cumming_inside_ass_want_action]"
    tempname.name "Ahh yes."
    pc "[rlist.having_sex_came_inside_ass_want]"
    show sb_onfours noman with dissolve
    $ npc_race_picker_1()
    jump whore_street_sex_group_picker

label whore_street_sex_group_onfours_cum_pullout:
    $ remove_from_list(player.sex_holes, ["vag", "ass"])
    tempname.name "[rlist.having_sex_cumming_pullout_man_dialogue]"
    show sb_onfours poke with dissolve
    $ player.sex_cum(tempname, "ass", quest_temp)
    "[rlist.having_sex_cumming_pullout_action]"
    tempname.name "Ahh yes!"
    pc "[rlist.having_sex_cumming_pullout_reaction]"
    show sb_onfours noman with dissolve
    $ npc_race_picker_1()
    jump whore_street_sex_group_picker

label whore_street_sex_group_onfours_anal_cum_picker:

    jump expression WeightedChoice([
    ("whore_street_sex_group_onfours_ass_cum", 100),
    ("whore_street_sex_group_onfours_cum_pullout", 75),
    ])




label whore_street_sex_group_onfours_leftman:
    $ add_to_list(player.sex_holes, "rhand")
    show sb_onfours man_front with dissolve
    $ player.sex_hand(tempname, quest_temp)
    "One of the guys gets in front of me while wanking. Now and then he reaches out to grope me or hit me with his cock."
    pc "[rlist.dirtytalk_guywank_pc]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_onfours_leftman_cum:
    $ remove_from_list(player.sex_holes, "rhand")
    $ player.sex_cum(tempname, "face", quest_temp)
    "[rlist.wanking_man_cum_action_face]"
    pc "[rlist.wanking_man_cum_action_face_reaction]"
    show sb_onfours noman_front with dissolve
    jump whore_street_sex_group_picker

label whore_street_sex_group_onfours_rightman:
    $ add_to_list(player.sex_holes, "lhand")
    show sb_onfours man_side with dissolve
    "One of the guys comes up and starts wanking while touching me."
    pc "[rlist.dirtytalk_guywank_pc]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_onfours_rightman_cum:
    $ remove_from_list(player.sex_holes, "lhand")
    tempname.name "[rlist.having_sex_man_dirtytalk]"
    $ player.sex_cum(tempname, "ass", quest_temp)
    "The guy wanking starts to cum all over me. He is too far away to aim properly so I end up feeling it all over my back."
    show sb_onfours noman_side with dissolve
    jump whore_street_sex_group_picker

label whore_street_sex_group_onfours_wank_cont:
    "The guys in front of me are furiously wanking off while looking at me. I can't touch or suck them so I decide to tease them a bit."
    pc "[rlist.dirtytalk_guywank_pc]"
    jump whore_street_sex_group_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
