label whore_street_sex_group_spitroast_doggy_start_picker:
    show sb_doggy1 with dissolve
    "I get on my fours and wiggle my ass, inviting anyone to come and have some fun."
    jump expression WeightedChoice([
    ("whore_street_sex_group_spitroast_doggy_vag", 100),
    ("whore_street_sex_group_spitroast_doggy_anal", If(player.check_anal_agree(), 50, 0)),
    ])

label whore_street_sex_group_spitroast_doggy_picker:
    jump expression WeightedChoice([
    ("whore_street_sex_group_spitroast_doggy_vag", If(not ("vag" in player.sex_holes or "ass" in player.sex_holes) and player.sex_man_amount, 100, 0)),
    ("whore_street_sex_group_spitroast_doggy_vag_cum_picker", If("vag" in player.sex_holes, 50, 0)),

    ("whore_street_sex_group_spitroast_doggy_anal", If(not ("vag" in player.sex_holes or "ass" in player.sex_holes) and player.sex_man_amount and player.check_anal_agree(), 50, 0)),
    ("whore_street_sex_group_spitroast_doggy_anal_cum_picker", If("ass" in player.sex_holes, 50, 0)),

    ("whore_street_sex_group_spitroast_doggy_blow", If(not "mouth" in player.sex_holes and player.sex_man_amount and not player.gagged, 100, 0)),
    ("whore_street_sex_group_spitroast_doggy_blow_continue", If("mouth" in player.sex_holes, 50, 0)),
    ("whore_street_sex_group_spitroast_doggy_blow_cum", If("mouth" in player.sex_holes, 50, 0)),

    ("whore_street_sex_group_spank", If(("ass" in player.sex_holes or "vag" in player.sex_holes), 25, 0)),
    ("whore_street_sex_group_sexytalk", If(any(x in ["ass", "vag", "mouth"] for x in player.sex_holes), 25, 0)),
    ("whore_street_sex_group_beat", If(any(x in ["ass", "vag", "mouth"] for x in player.sex_holes) and player.beingraped, 25, 0)),
    ("whore_street_sex_group_plug_remove", If(acc.anus and player.sex_man_amount > 3, 25, 0)),

    ("whore_street_sex_group_pronesex_switch", If(("ass" in player.sex_holes or "vag" in player.sex_holes) and not "mouth" in player.sex_holes, 50, 0)),
    ("whore_street_sex_group_standing_switch", If(any(x in ["ass"] for x in player.sex_holes) and not any(x in ["vag", "rhand", "lhand", "mouth"] for x in player.sex_holes), 50, 0)),

    ("whore_street_sex_group_watch_robin_picker", If(whore_street_sex_group_can_watch_robin(), 15, 0)),

    ("whore_street_sex_group_reset", If(player.sex_holes == [] and player.sex_man_amount >= 0, 10000, 0)),

    ])

label whore_street_sex_group_spitroast_assup_picker:
    jump expression WeightedChoice([
    ("whore_street_sex_group_spitroast_layblow_vag", If(not ("vag" in player.sex_holes or "ass" in player.sex_holes) and player.sex_man_amount, 100, 0)),
    ("whore_street_sex_group_spitroast_layblow_vag_cum_picker", If("vag" in player.sex_holes, 50, 0)),

    ("whore_street_sex_group_spitroast_layblow_anal", If(not ("vag" in player.sex_holes or "ass" in player.sex_holes) and player.sex_man_amount and player.check_anal_agree(), 50, 0)),
    ("whore_street_sex_group_spitroast_layblow_anal_cum_picker", If("ass" in player.sex_holes, 50, 0)),

    ("whore_street_sex_group_spitroast_layblow_blow", If(not "mouth" in player.sex_holes and player.sex_man_amount and not player.gagged, 100, 0)),
    
    ("whore_street_sex_group_spitroast_layblow_blow_cum", If("mouth" in player.sex_holes, 50, 0)),

    ("whore_street_sex_group_lay_doggy_switch", If(not "mouth" in player.sex_holes and player.sex_man_amount >= 0, 1000, 0)),
    ("whore_street_sex_group_standing_switch", If(any(x in ["ass", "vag"] for x in player.sex_holes) and not any(x in ["rhand", "lhand", "mouth"] for x in player.sex_holes), 500, 0)),

    ("whore_street_sex_group_spank", If(("ass" in player.sex_holes or "vag" in player.sex_holes), 25, 0)),
    ("whore_street_sex_group_sexytalk", If(any(x in ["ass", "vag", "mouth"] for x in player.sex_holes), 25, 0)),
    ("whore_street_sex_group_beat", If(any(x in ["ass", "vag", "mouth"] for x in player.sex_holes) and player.beingraped, 25, 0)),
    ("whore_street_sex_group_plug_remove", If(acc.anus and player.sex_man_amount > 3, 25, 0)),

    ("whore_street_sex_group_watch_robin_picker", If(whore_street_sex_group_can_watch_robin(), 15, 0)),

    ("whore_street_sex_group_reset", If(player.sex_holes == [] and player.sex_man_amount >= 0, 1000, 0)),

    ])

label whore_street_sex_group_spitroast_doggy_vag:
    $ add_to_list(player.sex_holes, "vag")
    show sb_doggy1 poke with dissolve
    "[rlist.having_sex_tease_vag]"
    "[rlist.having_sex_penetrate_vag_slow]"
    show sb_doggy1 vag ag with dissolve
    $ player.sex_vag(tempname, quest_temp)
    $ player.face_excited()
    "[rlist.having_sex_action]"
    "[rlist.having_sex_action]"
    tempname.name "[rlist.having_sex_man_dirtytalk]"
    pc "[rlist.having_sex_yes]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_spitroast_doggy_vag_cont:
    "[rlist.having_sex_action]"
    "[rlist.having_sex_action]"
    tempname.name "[rlist.having_sex_man_dirtytalk]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_spitroast_doggy_anal:
    $ add_to_list(player.sex_holes, "ass")

    show sb_doggy1 poke with dissolve
    "[rlist.having_sex_tease_vag]"
    "[rlist.having_sex_vag_to_ass_switch]"
    $ player.sex_anal(tempname, quest_temp)
    $ player.face_excited()
    show sb_doggy1 anal oh with dissolve
    "[rlist.having_sex_penetrate_ass_slow]"
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_action_ass]"
    pc "[rlist.having_sex_yes]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_spitroast_doggy_anal_cont:
    "[rlist.having_sex_action_ass]"
    "[rlist.having_sex_action_ass]"
    tempname.name "[rlist.having_sex_man_dirtytalk]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_spitroast_doggy_vag_cum_picker:
    $ player.sex_cum_location_offer(
    difficulty=5, choice_inside="Keep going!", choice_pullout="Not inside.",
    cum_want="whore_street_sex_group_spitroast_doggy_vag_cum_want", 
    cum_notwant="whore_street_sex_group_spitroast_doggy_vag_cum_notwant", 
    cum_pullout="whore_street_sex_group_spitroast_doggy_cum_pullout", 
    )

label whore_street_sex_group_spitroast_doggy_vag_cum_want:
    $ remove_from_list(player.sex_holes, "vag")

    pc "[rlist.having_sex_pc_cum_inside_vag_want_dialogue]"
    pc "[rlist.having_sex_yes]"
    tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"
    $ player.sex_cum(tempname, "inside", quest_temp)
    "[rlist.having_sex_cumming_inside_vag_want_action]"
    show sb_doggy1 oh with dissolve
    pc "[rlist.having_sex_yes]"
    pc "[rlist.having_sex_came_inside_vag_want]"
    show sb_doggy1 poke with dissolve
    show sb_doggy1 noman with dissolve
    $ npc_race_picker_1()
    jump whore_street_sex_group_picker

label whore_street_sex_group_spitroast_doggy_vag_cum_notwant:
    $ remove_from_list(player.sex_holes, "vag")
    pc "[rlist.having_sex_pc_cum_pullout_ask]"
    tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"
    $ player.sex_cum(tempname, "inside", quest_temp)
    "[rlist.having_sex_cumming_inside_vag_notwant_action]"
    show sb_doggy1 shock with dissolve
    tempname.name "Ahh yes."
    show sb_doggy1 neutral with dissolve
    pc "*Sigh*"
    show sb_doggy1 poke with dissolve
    show sb_doggy1 noman with dissolve
    $ npc_race_picker_1()
    jump whore_street_sex_group_picker

label whore_street_sex_group_spitroast_doggy_ass_cum:
    $ remove_from_list(player.sex_holes, "ass")
    pc "[rlist.having_sex_pc_cum_inside_ass_want_dialogue]"
    pc "[rlist.having_sex_yes]"
    tempname.name "[rlist.having_sex_man_cum_inside_ass_dialogue]"
    show sb_doggy1 oh with dissolve
    $ player.sex_cum(tempname, "anal", quest_temp)
    "[rlist.having_sex_cumming_inside_ass_want_action]"
    tempname.name "Ahh yes."
    pc "[rlist.having_sex_came_inside_ass_want]"
    show sb_doggy1 poke with dissolve
    show sb_doggy1 noman with dissolve
    $ npc_race_picker_1()
    jump whore_street_sex_group_picker

label whore_street_sex_group_spitroast_doggy_cum_pullout:
    $ remove_from_list(player.sex_holes, ["vag", "ass"])

    pc "[rlist.having_sex_pc_cum_pullout_ask]"
    tempname.name "[rlist.having_sex_cumming_pullout_man_dialogue]"

    show sb_doggy1 poke with dissolve
    $ player.sex_cum(tempname, "ass", quest_temp)
    "[rlist.having_sex_cumming_pullout_action]"
    tempname.name "Ahh yes!"
    pc "[rlist.having_sex_cumming_pullout_reaction]"
    show sb_doggy1 noman with dissolve
    $ npc_race_picker_1()
    jump whore_street_sex_group_picker

label whore_street_sex_group_spitroast_doggy_anal_cum_picker:

    jump expression WeightedChoice([
    ("whore_street_sex_group_spitroast_doggy_ass_cum", 100),
    ("whore_street_sex_group_spitroast_doggy_cum_pullout", 75),
    ])



label whore_street_sex_group_spitroast_doggy_blow:
    $ add_to_list(player.sex_holes, "mouth")
    "A guy comes up to the front of me and pulls a bit at my hair to lift my head up."
    show sb_doggy1 blow with dissolve
    $ player.sex_oral(tempname, quest_temp)
    "[rlist.blowjob_start_suck]"
    pc "[rlist.blowjob_muffle]"
    tempname.name "[rlist.having_sex_man_yes]"
    "[rlist.blowjob_start_suck_reaction]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_spitroast_doggy_blow_continue:
    pc "[rlist.blowjob_muffle]"
    "[rlist.blowjob_start_suck_reaction]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_spitroast_doggy_blow_cum:
    $ remove_from_list(player.sex_holes, "mouth")
    tempname.name "[rlist.blowjob_cum_mouth_man_dialogue]"
    $ player.sex_cum(tempname, "mouth", quest_temp)
    "[rlist.blowjob_cum_mouth]"
    tempname.name "[rlist.having_sex_man_yes]"
    pc "[rlist.blowjob_muffle]"
    show sb_doggy1 no_blow no_head with dissolve
    pc "[rlist.blowjob_cum_mouth_swallow_reaction]"
    show sb_doggy1 head_down ah with dissolve
    $ npc_race_picker_2()
    jump whore_street_sex_group_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
