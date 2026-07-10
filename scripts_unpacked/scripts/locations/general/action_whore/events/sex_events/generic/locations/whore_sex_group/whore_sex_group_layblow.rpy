label whore_street_sex_group_spitroast_layblow_vag:
    $ add_to_list(player.sex_holes, "vag")
    if not renpy.showing("sb_layblow sex"):
        show sb_layblow sex with dissolve
    "[rlist.having_sex_tease_vag]"
    "[rlist.having_sex_penetrate_vag_slow]"
    $ player.sex_vag(tempname, quest_temp)
    $ player.face_excited()
    "[rlist.having_sex_action]"
    "[rlist.having_sex_action]"
    tempname.name "[rlist.having_sex_man_dirtytalk]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_spitroast_layblow_vag_cont:
    "[rlist.having_sex_action]"
    "[rlist.having_sex_action]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_spitroast_layblow_anal:
    $ add_to_list(player.sex_holes, "ass")
    if not renpy.showing("sb_layblow sex"):
        show sb_layblow sex with dissolve
    "[rlist.having_sex_tease_vag]"
    "[rlist.having_sex_vag_to_ass_switch]"
    $ player.sex_anal(tempname, quest_temp)
    $ player.face_excited()
    "[rlist.having_sex_penetrate_ass_slow]"
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_action_ass]"
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_action_ass]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_spitroast_layblow_anal_cont:
    "[rlist.having_sex_action_ass]"
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_action_ass]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_spitroast_layblow_vag_cum_picker:
    "Vag guy is going to cum, here is the picker of where he will cum"
    $ player.sex_cum_location_offer(
    difficulty=5, choice_inside="Keep going!", choice_pullout="Not inside.",
    cum_want="whore_street_sex_group_spitroast_layblow_vag_cum_want", 
    cum_notwant="whore_street_sex_group_spitroast_layblow_vag_cum_notwant", 
    cum_pullout="whore_street_sex_group_spitroast_layblow_cum_pullout", 
    )

label whore_street_sex_group_spitroast_layblow_vag_cum_want:
    $ remove_from_list(player.sex_holes, "vag")
    pc "[rlist.having_sex_pc_cum_inside_vag_want_dialogue]"
    pc "[rlist.having_sex_yes]"
    tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"
    $ player.sex_cum(tempname, "inside", quest_temp)
    "[rlist.having_sex_cumming_inside_vag_want_action]"
    show sb_doggy1 oh with dissolve
    pc "[rlist.having_sex_yes]"
    pc "[rlist.having_sex_came_inside_vag_want]"
    show sb_layblow nosex with dissolve
    $ npc_race_picker_1()
    jump whore_street_sex_group_picker

label whore_street_sex_group_spitroast_layblow_vag_cum_notwant:
    $ remove_from_list(player.sex_holes, "vag")
    pc "[rlist.having_sex_pc_cum_pullout_ask]"
    tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"
    $ player.sex_cum(tempname, "inside", quest_temp)
    "[rlist.having_sex_cumming_inside_vag_notwant_action]"
    show sb_doggy1 shock with dissolve
    tempname.name "Ahh yes."
    show sb_doggy1 neutral with dissolve
    pc "*Sigh*"
    show sb_layblow nosex with dissolve
    $ npc_race_picker_1()
    jump whore_street_sex_group_picker

label whore_street_sex_group_spitroast_layblow_ass_cum:
    $ remove_from_list(player.sex_holes, "ass")
    pc "[rlist.having_sex_pc_cum_inside_ass_want_dialogue]"
    pc "[rlist.having_sex_yes]"
    tempname.name "[rlist.having_sex_man_cum_inside_ass_dialogue]"
    show sb_doggy1 oh with dissolve
    $ player.sex_cum(tempname, "anal", quest_temp)
    "[rlist.having_sex_cumming_inside_ass_want_action]"
    tempname.name "Ahh yes."
    pc "[rlist.having_sex_came_inside_ass_want]"
    show sb_layblow nosex with dissolve
    $ npc_race_picker_1()
    jump whore_street_sex_group_picker

label whore_street_sex_group_spitroast_layblow_cum_pullout:
    $ remove_from_list(player.sex_holes, ["vag", "ass"])

    pc "[rlist.having_sex_pc_cum_pullout_ask]"
    tempname.name "[rlist.having_sex_cumming_pullout_man_dialogue]"
    $ player.sex_cum(tempname, "ass", quest_temp)
    "[rlist.having_sex_cumming_pullout_action]"
    tempname.name "Ahh yes!"
    pc "[rlist.having_sex_cumming_pullout_reaction]"
    show sb_layblow nosex with dissolve
    $ npc_race_picker_1()
    jump whore_street_sex_group_picker

label whore_street_sex_group_spitroast_layblow_anal_cum_picker:

    jump expression WeightedChoice([
    ("whore_street_sex_group_spitroast_layblow_ass_cum", 100),
    ("whore_street_sex_group_spitroast_layblow_cum_pullout", 75),
    ])



label whore_street_sex_group_spitroast_layblow_blow:
    "[rlist.blowjob_start_suck]"
    tempname.name "[rlist.having_sex_man_yes]"
    "[rlist.blowjob_start_suck_reaction]"
    pc "[rlist.blowjob_muffle]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_spitroast_layblow_blow_cum:
    $ remove_from_list(player.sex_holes, "mouth")
    tempname.name "[rlist.having_sex_man_keep_going]"
    "[rlist.blowjob_cum_close]"
    tempname.name "[rlist.having_sex_man_close_dialogue]"
    tempname.name "[rlist.blowjob_cum_mouth_man_dialogue]"
    $ player.sex_cum(tempname, "mouth", quest_temp)

    "[rlist.blowjob_cum_mouth]"
    tempname.name "[rlist.having_sex_man_yes]"
    pc "[rlist.blowjob_muffle]"
    show sb_layblow mast happy with dissolve
    pc "[rlist.blowjob_cum_mouth_swallow_reaction]"
    tempname.name "[rlist.blowjob_cum_mouth_swallow_reaction_man]"
    jump whore_street_sex_group_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
