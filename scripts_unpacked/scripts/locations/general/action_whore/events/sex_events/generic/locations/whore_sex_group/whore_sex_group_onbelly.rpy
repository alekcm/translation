label whore_street_sex_group_onbelly_picker:
    jump expression WeightedChoice([
    ("whore_street_sex_group_pronesex_vag", If(not ("vag" in player.sex_holes or "ass" in player.sex_holes) and player.sex_man_amount, 100, 0)),
    ("whore_street_sex_group_pronesex_vag_cum_picker", If("vag" in player.sex_holes, 50, 0)),

    ("whore_street_sex_group_pronesex_anal", If(not ("vag" in player.sex_holes or "ass" in player.sex_holes) and player.sex_man_amount and player.check_anal_agree(), 50, 0)),
    ("whore_street_sex_group_pronesex_anal_cum_picker", If("ass" in player.sex_holes, 50, 0)),

    ("whore_street_sex_group_standing_switch", If(any(x in ["ass", "vag"] for x in player.sex_holes) and not any(x in ["rhand", "lhand", "mouth"] for x in player.sex_holes), 50, 0)),

    ("whore_street_sex_group_spank", If(("ass" in player.sex_holes or "vag" in player.sex_holes), 25, 0)),
    ("whore_street_sex_group_sexytalk", If(any(x in ["ass", "vag", "mouth"] for x in player.sex_holes), 25, 0)),
    ("whore_street_sex_group_beat", If(any(x in ["ass", "vag", "mouth"] for x in player.sex_holes) and player.beingraped, 25, 0)),
    ("whore_street_sex_group_plug_remove", If(acc.anus and player.sex_man_amount > 3, 25, 0)),

    ("whore_street_sex_group_watch_robin_picker", If(whore_street_sex_group_can_watch_robin(), 15, 0)),

    ("whore_street_sex_group_reset", If(player.sex_holes == [] and player.sex_man_amount >= 0, 500, 0)),

    ])


label whore_street_sex_group_pronesex_vag:
    $ add_to_list(player.sex_holes, "vag")
    $ renpy.show(renpy.random.choice(["sb_onbelly lay_cum back happy", "sb_onbelly assjob grope back happy"]))
    with dissolve
    if renpy.showing("sb_onbelly lay_cum"):
        show sb_onbelly lay_poke with dissolve
    else:
        show sb_onbelly poke with dissolve
    "[rlist.having_sex_tease_vag]"
    "[rlist.having_sex_penetrate_vag_slow]"
    if renpy.showing("sb_onbelly lay_cum"):
        show sb_onbelly lay_sex with dissolve
    else:
        show sb_onbelly sex with dissolve
    $ player.sex_vag(tempname, quest_temp)
    $ player.face_excited()
    "[rlist.having_sex_action]"
    "[rlist.having_sex_action]"
    tempname.name "[rlist.having_sex_man_dirtytalk]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_pronesex_vag_cont:
    "[rlist.having_sex_action]"
    "[rlist.having_sex_action]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_pronesex_anal:
    $ add_to_list(player.sex_holes, "ass")
    $ renpy.show(renpy.random.choice(["sb_onbelly lay_cum back happy", "sb_onbelly assjob grope back happy"]))
    with dissolve
    if renpy.showing("sb_onbelly lay_cum"):
        show sb_onbelly lay_poke with dissolve
    else:
        show sb_onbelly poke with dissolve
    "[rlist.having_sex_tease_vag]"
    "[rlist.having_sex_vag_to_ass_switch]"
    if renpy.showing("sb_onbelly lay_cum"):
        show sb_onbelly lay_sex with dissolve
    else:
        show sb_onbelly sex with dissolve
    $ player.sex_anal(tempname, quest_temp)
    $ player.face_excited()
    "[rlist.having_sex_penetrate_ass_slow]"
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_action_ass]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_pronesex_anal_cont:
    "[rlist.having_sex_action_ass]"
    "[rlist.having_sex_action_ass]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_pronesex_vag_cum_picker:
    $ player.sex_cum_location_offer(
    difficulty=5, choice_inside="Keep going!", choice_pullout="Not inside.",
    cum_want="whore_street_sex_group_pronesex_vag_cum_want", 
    cum_notwant="whore_street_sex_group_pronesex_vag_cum_notwant", 
    cum_pullout="whore_street_sex_group_pronesex_cum_pullout", 
    )

label whore_street_sex_group_pronesex_vag_cum_want:
    $ remove_from_list(player.sex_holes, "vag")
    pc "[rlist.having_sex_pc_cum_inside_vag_want_dialogue]"
    pc "[rlist.having_sex_yes]"
    tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"
    $ player.sex_cum(tempname, "inside", quest_temp)
    "[rlist.having_sex_cumming_inside_vag_want_action]"
    pc "[rlist.having_sex_yes]"
    pc "[rlist.having_sex_came_inside_vag_want]"
    if renpy.showing("sb_onbelly lay_sex"):
        show sb_onbelly lay_poke with dissolve
    else:
        show sb_onbelly poke with dissolve
    show sb_onbelly noman with dissolve
    $ npc_race_picker_1()
    jump whore_street_sex_group_picker

label whore_street_sex_group_pronesex_vag_cum_notwant:
    $ remove_from_list(player.sex_holes, "vag")
    pc "[rlist.having_sex_pc_cum_pullout_ask]"
    tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"
    $ player.sex_cum(tempname, "inside", quest_temp)
    "[rlist.having_sex_cumming_inside_vag_notwant_action]"
    show sb_onbelly oh with dissolve
    tempname.name "Ahh yes."
    if renpy.showing("sb_onbelly lay_sex"):
        show sb_onbelly lay_poke with dissolve
    else:
        show sb_onbelly poke with dissolve
    pc "*Sigh*"
    show sb_onbelly noman with dissolve
    $ npc_race_picker_1()
    jump whore_street_sex_group_picker

label whore_street_sex_group_pronesex_ass_cum:
    $ remove_from_list(player.sex_holes, "ass")
    pc "[rlist.having_sex_pc_cum_inside_ass_want_dialogue]"
    pc "[rlist.having_sex_yes]"
    tempname.name "[rlist.having_sex_man_cum_inside_ass_dialogue]"
    $ player.sex_cum(tempname, "anal", quest_temp)
    "[rlist.having_sex_cumming_inside_ass_want_action]"
    tempname.name "Ahh yes."
    pc "[rlist.having_sex_came_inside_ass_want]"
    if renpy.showing("sb_onbelly lay_sex"):
        show sb_onbelly lay_poke with dissolve
    else:
        show sb_onbelly poke with dissolve
    show sb_onbelly noman with dissolve
    $ npc_race_picker_1()
    jump whore_street_sex_group_picker

label whore_street_sex_group_pronesex_cum_pullout:
    if renpy.showing("sb_onbelly lay_sex"):
        show sb_onbelly lay_cum
    else:
        show sb_onbelly assjob
    with dissolve
    pc "[rlist.having_sex_pc_cum_pullout_ask]"
    tempname.name "[rlist.having_sex_cumming_pullout_man_dialogue]"
    $ player.sex_cum(tempname, "ass", quest_temp)
    "[rlist.having_sex_cumming_pullout_action]"
    tempname.name "Ahh yes!"
    pc "[rlist.having_sex_cumming_pullout_reaction]"
    show sb_onbelly noman with dissolve
    jump whore_street_sex_group_picker

label whore_street_sex_group_pronesex_anal_cum_picker:

    jump expression WeightedChoice([
    ("whore_street_sex_group_pronesex_ass_cum", 100),
    ("whore_street_sex_group_pronesex_cum_pullout", 75),
    ])
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
