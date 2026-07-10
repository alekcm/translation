label whore_street_sex_group_cowgirl_start_picker:
    "I pick one of the guys, lead him to the bed and lay him down."
    jump expression WeightedChoice([
    ("whore_street_sex_group_3p_cow_vag_normal", If(player.check_horny(extreme=True), 100, 0)),
    ("whore_street_sex_group_3p_cow_vag_rough", 100),
    ])

label whore_street_sex_group_cowgirl_picker:
    jump expression WeightedChoice([
    
    
    ("whore_street_sex_group_3p_cow_vag_cum_picker", If("vag" in player.sex_holes, 25, 0)), 
    ("whore_street_sex_group_3p_cow_vag_cont", If("vag" in player.sex_holes, 50, 0)),

    ("whore_street_sex_group_3p_cow_anal", If(not "ass" in player.sex_holes and player.sex_man_amount and player.check_anal_agree(), 100, 0)),
    ("whore_street_sex_group_3p_cow_anal_cum_picker", If("ass" in player.sex_holes, 50, 0)),

    ("whore_street_sex_group_3p_cow_blow", If(not "mouth" in player.sex_holes and player.sex_man_amount and not player.gagged, 100, 0)),
    ("whore_street_sex_group_3p_cow_blow_cum_mouth", If("mouth" in player.sex_holes, 50, 0)),

    ("whore_street_sex_group_3p_cow_spit_switch", If(not "vag" in player.sex_holes, 300, 0)),

    ("whore_street_sex_group_spank", If("ass" in player.sex_holes, 25, 0)),
    ("whore_street_sex_group_sexytalk", If(any(x in ["ass", "vag", "mouth"] for x in player.sex_holes), 25, 0)),
    ("whore_street_sex_group_plug_remove", If(acc.anus and player.sex_man_amount > 3, 25, 0)),

    ("whore_street_sex_group_reset", If(player.sex_holes == [] and player.sex_man_amount, 1000, 0)),
    ("whore_street_sex_group_watch_robin_picker", If(whore_street_sex_group_can_watch_robin(), 15, 0)),
    ])







label whore_street_sex_group_3p_cow_vag_normal:
    $ add_to_list(player.sex_holes, "vag")
    $ renpy.show(renpy.random.choice(["sb_ontop lay happy down", "sb_cowgirl"]))
    with dissolve
    "[rlist.foreplay_preparesex_ontop]"
    $ if_showing("sb_cowgirl", "poke")
    "[rlist.having_sex_penetrate_vag_cowgirl]"
    $ if_showing("sb_cowgirl", "vag")
    $ player.sex_vag(tempname, quest_temp)
    $ player.face_excited()
    tempname.name "[rlist.having_sex_man_dirtytalk]"
    pc "[rlist.having_sex_yes]"
    if renpy.showing("sb_cowgirl"):
        $ renpy.scene()
        show sb_ontop lay happy down
        with dissolve
    jump whore_street_sex_group_picker

label whore_street_sex_group_3p_cow_vag_rough:
    $ add_to_list(player.sex_holes, "vag")
    $ renpy.show(renpy.random.choice(["sb_ontop lay happy down", "sb_cowgirl"]))
    with dissolve
    "[rlist.foreplay_preparesex_ontop]"
    $ if_showing("sb_cowgirl", "poke")
    "[rlist.having_sex_penetrate_vag_cowgirl_horny]"
    $ if_showing("sb_cowgirl", "vag")
    $ player.sex_vag(tempname, quest_temp)
    $ player.face_excited()
    "[rlist.having_sex_action_cowgirl_rough]"
    "[rlist.having_sex_enjoy_cowgirl]"
    tempname.name "[rlist.having_sex_man_dirtytalk]"
    pc "[rlist.having_sex_yes]"
    if renpy.showing("sb_cowgirl"):
        $ renpy.scene()
        show sb_ontop lay happy down
        with dissolve
    jump whore_street_sex_group_picker

label whore_street_sex_group_3p_cow_vag_cont:
    if not "ass" in player.sex_holes and numgen():
        show sb_cowgirl vag with dissolve
    elif "ass" in player.sex_holes and numgen():
        show sb_dpbed banal vag with dissolve
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_action_cowgirl_continue]"
    "[rlist.having_sex_enjoy]"
    $ player.face_orgasm()
    pc "[rlist.having_sex_yes]"
    if renpy.showing("sb_cowgirl") or renpy.showing("sb_dpbed"):
        hide sb_dpbed
        hide sb_cowgirl
        with dissolve
    jump whore_street_sex_group_picker

label whore_street_sex_group_3p_cow_vag_cum_picker:
    $ player.sex_cum_location_offer(
    difficulty=5, choice_inside="Keep going!", choice_pullout="Not inside.",
    cum_want="whore_street_sex_group_3p_cow_vag_cum_want", 
    cum_notwant="whore_street_sex_group_3p_cow_vag_cum_notknow", 
    cum_pullout="whore_street_sex_group_3p_cow_vag_cum_pullout", 
    )

label whore_street_sex_group_3p_cow_vag_cum_want:
    $ remove_from_list(player.sex_holes, "vag")
    if not "ass" in player.sex_holes and numgen():
        show sb_cowgirl vag with dissolve
    elif "ass" in player.sex_holes and numgen():
        show sb_dpbed banal vag with dissolve
    pc "[rlist.having_sex_pc_cum_inside_vag_want_dialogue_cowgirl]"
    tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"
    $ player.sex_cum(tempname, "inside", quest_temp)
    "[rlist.having_sex_cumming_inside_vag_want_action_cowgirl]"
    $ if_showing("sb_ontop", "happy")
    pc "[rlist.having_sex_yes]"
    pc "[rlist.having_sex_came_inside_vag_want]"
    tempname.name "[rlist.sex_end_man_tired]"
    $ if_showing("sb_cowgirl", "poke")
    "[rlist.having_sex_came_take_cock_out_vag]"
    $ if_showing("sb_cowgirl", "out", "sb_dpbed", "poke")
    if renpy.showing("sb_cowgirl") or renpy.showing("sb_dpbed"):
        hide sb_dpbed
        hide sb_cowgirl
        with dissolve
    jump whore_street_sex_group_picker

label whore_street_sex_group_3p_cow_vag_cum_notknow:
    $ remove_from_list(player.sex_holes, "vag")
    if not "ass" in player.sex_holes and numgen():
        show sb_cowgirl vag with dissolve
    elif "ass" in player.sex_holes and numgen():
        show sb_dpbed banal vag with dissolve
    pc "[rlist.having_sex_yes]"
    $ player.sex_cum(tempname, "inside", quest_temp)
    "[rlist.having_sex_action_cowgirl_continue]"
    "[rlist.having_sex_enjoy]"
    $ player.face_orgasm()
    pc "[rlist.having_sex_yes]"
    tempname.name "Huff"
    "[rlist.having_sex_came_take_cock_out_vag]"
    pc "You're getting soft, did you cum?"
    $ if_showing("sb_cowgirl", "out", "sb_dpbed", "poke")
    if renpy.showing("sb_cowgirl") or renpy.showing("sb_dpbed"):
        hide sb_dpbed
        hide sb_cowgirl
        with dissolve
    jump whore_street_sex_group_picker

label whore_street_sex_group_3p_cow_vag_cum_pullout:
    $ remove_from_list(player.sex_holes, "vag")
    if not "ass" in player.sex_holes and numgen():
        show sb_cowgirl vag with dissolve
    elif "ass" in player.sex_holes and numgen():
        show sb_dpbed banal vag with dissolve

    if "ass" in player.sex_holes:
        "The guy under me is pressing against my ass while fucking me, so I can't lift my hips up to get the guy in my pussy out."
        $ player.sex_cum(tempname, "inside", quest_temp)
        "With not much choice, I just carry on getting fucked."
        "[rlist.having_sex_action_cowgirl_continue]"
        "[rlist.having_sex_enjoy]"
        $ player.face_orgasm()
        pc "[rlist.having_sex_yes]"
        tempname.name "Huff"
    else:
        "The guy under me is about to cum, so I lift my ass off of him so he slips out of me, then put him between my ass cheeks."
        show sb_cowgirl poke with dissolve
        show sb_cowgirl out with dissolve
        $ player.sex_cum(tempname, "pullout", quest_temp)
        tempname.name "[rlist.having_sex_man_yes]"
        pc "[rlist.having_sex_cumming_pullout_reaction]"

    if renpy.showing("sb_cowgirl") or renpy.showing("sb_dpbed"):
        hide sb_dpbed
        hide sb_cowgirl
        with dissolve
    jump whore_street_sex_group_picker



label whore_street_sex_group_3p_cow_anal:
    $ add_to_list(player.sex_holes, "ass")
    show sb_ontop doggy with dissolve
    "I feel hands on my ass and the guy lining himself up behind me."
    if numgen() and "vag" in player.sex_holes:
        show sb_dpbed vag bpoke with dissolve
    tempname2.name "Sexy ass."
    $ if_showing("sb_dpbed", "banal")
    $ player.sex_anal(tempname, quest_temp)
    $ player.face_excited()
    "[rlist.having_sex_penetrate_ass_slow]"
    tempname2.name "Ahhhhhh so warm."
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_action_ass]"
    if renpy.showing("sb_dpbed"):
        hide sb_dpbed with dissolve
    jump whore_street_sex_group_picker

label whore_street_sex_group_3p_cow_anal_cum_picker:

    jump expression WeightedChoice([
    ("whore_street_sex_group_3p_cow_anal_cum_want", 100),
    ("whore_street_sex_group_3p_cow_anal_cum_pullout", 75),
    ])

label whore_street_sex_group_3p_cow_anal_cum_want:
    $ remove_from_list(player.sex_holes, "ass")
    if numgen() and "vag" in player.sex_holes:
        show sb_dpbed vag banal with dissolve
    pc "[rlist.having_sex_yes]"
    tempname2.name "[rlist.having_sex_man_cum_inside_ass_dialogue]"
    $ player.sex_cum(tempname, "anal", quest_temp)
    "[rlist.having_sex_cumming_inside_ass_want_action]"
    tempname2.name "Ahh yes."
    pc "[rlist.having_sex_came_inside_ass_want]"
    $ if_showing("sb_dpbed", "bpoke")
    $ if_showing("sb_ontop", "no_doggy", "sb_dpbed", "b_noman")
    if "vag" in player.sex_holes:
        "With the cock in my arse gone, I keep riding the guy below me."
        "[rlist.having_sex_action_cowgirl_continue]"
    if renpy.showing("sb_dpbed"):
        hide sb_dpbed with dissolve
        $ npc_race_picker_2()
    jump whore_street_sex_group_picker

label whore_street_sex_group_3p_cow_anal_cum_pullout:
    $ remove_from_list(player.sex_holes, "ass")
    if numgen() and "vag" in player.sex_holes:
        show sb_dpbed vag banal with dissolve
    pc "[rlist.having_sex_yes]"
    $ if_showing("sb_dpbed", "bpoke")
    tempname2.name "[rlist.having_sex_cumming_pullout_man_dialogue]"
    "[rlist.having_sex_cumming_pullout_action]"
    $ player.sex_cum(tempname, "ass", quest_temp)
    tempname2.name "Ahh yes."
    pc "[rlist.having_sex_cumming_pullout_reaction]"
    $ if_showing("sb_ontop", "no_doggy", "sb_dpbed", "b_noman")
    if "vag" in player.sex_holes:
        "With the cock in my arse gone, I keep riding the guy below me."
        "[rlist.having_sex_action_cowgirl_continue]"
    if renpy.showing("sb_dpbed"):
        hide sb_dpbed with dissolve
        $ npc_race_picker_2()
    jump whore_street_sex_group_picker



label whore_street_sex_group_3p_cow_blow:
    $ add_to_list(player.sex_holes, "mouth")
    "One of the guys comes up to me and puts his cock in my mouth."
    show sb_ontop blow with dissolve
    $ player.sex_oral(tempname, quest_temp)
    "[rlist.blowjob_start_suck]"
    pc "[rlist.blowjob_muffle]"
    tempname.name "[rlist.having_sex_man_yes]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_3p_cow_blow_cum_mouth:
    $ remove_from_list(player.sex_holes, "mouth")
    tempname.name "[rlist.blowjob_cum_mouth_man_dialogue]"
    $ player.sex_cum(tempname, "mouth", quest_temp)
    "[rlist.blowjob_cum_mouth]"
    tempname.name "[rlist.having_sex_man_yes]"
    pc "[rlist.blowjob_muffle]"
    show sb_ontop no_blow with dissolve
    pc "[rlist.blowjob_cum_mouth_swallow_reaction]"
    $ npc_race_picker_2()
    jump whore_street_sex_group_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
