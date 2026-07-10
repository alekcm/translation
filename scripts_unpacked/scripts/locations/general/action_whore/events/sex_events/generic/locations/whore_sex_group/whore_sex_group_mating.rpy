label whore_street_sex_group_matingpress_start_picker:
    "I head over to the bed, lay down and spread my legs."
    show sb_matingpress oh with dissolve
    pc "Someone want to join?"
    jump expression WeightedChoice([
    ("whore_street_sex_group_matingpress_vag", 100),
    ("whore_street_sex_group_matingpress_anal", If(player.check_anal_agree(), 50, 0)),
    ])

label whore_street_sex_group_matingpress_picker:
    jump expression WeightedChoice([
    ("whore_street_sex_group_matingpress_vag", If(not ("vag" in player.sex_holes or "ass" in player.sex_holes) and player.sex_man_amount, 300, 0)),
    ("whore_street_sex_group_matingpress_vag_cont_sexonly", If(any(x in ["vag", "ass"] for x in player.sex_holes) and not any(x in ["lhand", "rhand", "mouth"] for x in player.sex_holes) , 150, 0)),
    ("whore_street_sex_group_matingpress_vag_cum_picker", If("vag" in player.sex_holes, 50, 0)),
    
    ("whore_street_sex_group_matingpress_anal", If(not ("vag" in player.sex_holes or "ass" in player.sex_holes) and player.sex_man_amount and player.check_anal_agree(), 300, 0)),
    ("whore_street_sex_group_matingpress_anal_cum_picker", If("ass" in player.sex_holes, 50, 0)),

    ("whore_street_sex_group_mating_onback_switch", If("ass" in player.sex_holes or "vag" in player.sex_holes and not any("robin" in holes for holes in player.sex_holes), 50, 0)),

    ("whore_street_sex_group_robin_matingpress_facesit_lick", If(not ("vag" in player.sex_holes or "ass" in player.sex_holes) and player.sex_man_amount and "robin_facesit" in player.sex_holes and player.cum_locations["cum_vagin"] > 5, player.cum_locations["cum_vagin"] * 30, 0)),
    ("whore_street_sex_group_robin_matingpress_facesit_sexoffer", If(not ("vag" in player.sex_holes or "ass" in player.sex_holes) and player.sex_man_amount and "robin_facesit" in player.sex_holes, 500, 0)),
    ("whore_street_sex_group_robin_matingpress_facesit", If(robin_here() and not "robin_facesit" in player.sex_holes, 40, 0)),
    ("whore_street_sex_group_watch_robin_picker", If(whore_street_sex_group_can_watch_robin(), 15, 0)),

    ("whore_street_sex_group_reset", If(player.sex_holes == [] and player.sex_man_amount, 100, 0)),
    ])

label whore_street_sex_group_matingpress_vag:
    $ add_to_list(player.sex_holes, "vag")
    show sb_matingpress down poke with dissolve
    "[rlist.having_sex_tease_vag]"
    "[rlist.having_sex_penetrate_vag_slow]"
    show sb_matingpress happy vag
    $ player.sex_vag(tempname, quest_temp)
    $ player.face_excited()
    "[rlist.having_sex_action_onback]"
    "[rlist.having_sex_action_onback]"
    tempname.name "[rlist.having_sex_man_dirtytalk]"
    pc "[rlist.having_sex_yes]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_matingpress_vag_cont_sexonly:
    show sb_matingpress up
    "[rlist.having_sex_action_onback]"
    "[rlist.having_sex_action_onback]"
    show sb_matingpress down
    jump whore_street_sex_group_picker

label whore_street_sex_group_matingpress_anal:
    $ add_to_list(player.sex_holes, "ass")
    show sb_matingpress down poke with dissolve
    $ player.sex_anal(tempname, quest_temp)
    show sb_matingpress down anal oh with dissolve
    "[rlist.having_sex_penetrate_ass_slow]"
    tempname.name "Ahhhhhh so warm."
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_action_ass]"
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_action_ass]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_matingpress_vag_cum_picker:
    $ player.sex_cum_location_offer(
    difficulty=5, choice_inside="Keep going!", choice_pullout="Not inside.",
    cum_want="whore_street_sex_group_matingpress_vag_cum_want", 
    cum_notwant="whore_street_sex_group_matingpress_vag_cum_notwant", 
    cum_pullout="whore_street_sex_group_matingpress_cum_pullout", 
    )

label whore_street_sex_group_matingpress_vag_cum_want:
    $ remove_from_list(player.sex_holes, "vag")
    pc "[rlist.having_sex_pc_cum_inside_vag_want_dialogue]"
    pc "[rlist.having_sex_yes]"
    tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"
    $ player.sex_cum(tempname, "inside", quest_temp)
    "[rlist.having_sex_cumming_inside_vag_want_action]"
    pc "[rlist.having_sex_came_inside_vag_want]"

    show sb_matingpress poke with dissolve
    show sb_matingpress noman with dissolve
    $ npc_race_picker_1()
    jump whore_street_sex_group_picker

label whore_street_sex_group_matingpress_vag_cum_notwant:
    $ remove_from_list(player.sex_holes, "vag")
    pc "[rlist.having_sex_pc_cum_pullout_ask_front]"
    tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"
    $ player.sex_cum(tempname, "inside", quest_temp)
    "[rlist.having_sex_cumming_inside_vag_notwant_action]"
    tempname.name "Ahh yes."
    pc "[rlist.having_sex_came_inside_vag_notwant_reaction]"
    pc "*Sigh*"
    show sb_matingpress poke with dissolve
    show sb_matingpress noman with dissolve
    $ npc_race_picker_1()
    jump whore_street_sex_group_picker

label whore_street_sex_group_matingpress_cum_pullout:
    $ remove_from_list(player.sex_holes, ["vag", "ass"])
    pc "[rlist.having_sex_pc_cum_pullout_ask]"
    tempname.name "[rlist.having_sex_cumming_pullout_man_dialogue]"
    show sb_matingpress poke with dissolve
    $ player.sex_cum(tempname, "belly", quest_temp)
    "[rlist.having_sex_cumming_pullout_action]"
    tempname.name "Ahh yes!"
    pc "[rlist.having_sex_cumming_pullout_reaction]"
    show sb_matingpress noman with dissolve
    $ npc_race_picker_1()
    jump whore_street_sex_group_picker

label whore_street_sex_group_matingpress_ass_cum:
    $ remove_from_list(player.sex_holes, "ass")
    pc "[rlist.having_sex_yes]"
    tempname.name "[rlist.having_sex_man_cum_inside_ass_dialogue]"
    $ player.sex_cum(tempname, "anal", quest_temp)
    "[rlist.having_sex_cumming_inside_ass_want_action]"
    tempname.name "Ahh yes."
    pc "[rlist.having_sex_came_inside_ass_want]"
    show sb_matingpress poke with dissolve
    show sb_matingpress noman with dissolve
    $ npc_race_picker_1()
    jump whore_street_sex_group_picker

label whore_street_sex_group_matingpress_anal_cum_picker:

    jump expression WeightedChoice([
    ("whore_street_sex_group_matingpress_ass_cum", 100),
    ("whore_street_sex_group_matingpress_cum_pullout", 75),
    ])
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
