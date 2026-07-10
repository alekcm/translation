




label whore_bed_sex_cowgirl:
    $ renpy.scene()
    $ renpy.show(renpy.random.choice(["sb_ontop lay happy down", "sb_cowgirl"]))
    with dissolve
    "[rlist.foreplay_preparesex_ontop]"
    jump whore_bed_sex_cowgirl_picker

label whore_bed_sex_cowgirl_picker:
    "[rlist.having_sex_tease_vag_cowgirl]"
    $ if_showing("sb_cowgirl", "poke")

    if not player.soldrequest:
        menu:
            "Put him in my pussy":
                jump expression WeightedChoice([
                ("whore_bed_sex_cowgirl_vag_rough", If(player.check_horny(extreme=True), 5, 0)),
                ("whore_bed_sex_cowgirl_vag_normal", 5),
                ])
            "Put him up my arse":
                jump whore_bed_sex_cowgirl_anal

    jump expression WeightedChoice([
    ("whore_bed_sex_cowgirl_vag_rough", If(player.check_horny(extreme=True), 5, 0)),
    ("whore_bed_sex_cowgirl_vag_normal", 5),
    ("whore_bed_sex_cowgirl_vag_rough", If(any(pos in player.soldrequest for pos in ["vag", "creampie"]), 100, 0)),
    ("whore_bed_sex_cowgirl_vag_normal", If(any(pos in player.soldrequest for pos in ["vag", "creampie"]), 100, 0)),
    ("whore_bed_sex_cowgirl_anal", If(player.has_perk([perk_buttslut, perk_preg_notwant], notif=True) and not any(pos in player.soldrequest for pos in ["vag", "creampie"]), 30, 0)),
    ("whore_bed_sex_cowgirl_anal", If(player.want_sexlocation == 2, 1, 0)),
    ("whore_bed_sex_cowgirl_anal", If(player.soldrequest == "anal", 100, 0)),
    ])



label whore_bed_sex_cowgirl_vag_normal:


    "[rlist.having_sex_penetrate_vag_cowgirl]"
    $ player.sex_vag(tempname, quest_temp)
    $ player.face_excited()
    $ if_showing("sb_cowgirl", "vag")
    "[rlist.having_sex_action_cowgirl]"

    if not numgen(0,10):
        call whore_street_sex_standing_spank_call from _call_whore_street_sex_standing_spank_call_1

    "[rlist.having_sex_enjoy_cowgirl]"
    if not numgen(0,30):
        jump whore_bed_sex_cowgirl_vag_cum_confused
    tempname.name "[rlist.having_sex_man_dirtytalk]"
    pc "[rlist.having_sex_yes]"
    if not numgen(0,30):
        jump whore_bed_sex_cowgirl_vag_cum_confused

    "[rlist.having_sex_enjoy]"
    $ player.face_orgasm()
    pc "[rlist.having_sex_yes]"
    if not numgen(0,10):
        jump whore_bed_sex_cowgirl_vag_cum_notknow
    "[rlist.having_sex_man_close]"
    tempname.name "[rlist.having_sex_man_close_dialogue]"
    jump whore_bed_sex_cowgirl_vag_cum_picker

label whore_bed_sex_cowgirl_vag_rough:


    "[rlist.having_sex_penetrate_vag_cowgirl_horny]"
    $ player.sex_vag(tempname, quest_temp)
    $ player.face_excited()
    $ if_showing("sb_cowgirl", "vag")
    "[rlist.having_sex_action_cowgirl_rough]"

    if not numgen(0,2):
        call whore_street_sex_standing_spank_call from _call_whore_street_sex_standing_spank_call_2
    if not numgen(0,30):
        jump whore_bed_sex_cowgirl_vag_cum_confused
    "[rlist.having_sex_enjoy_cowgirl]"
    if not numgen(0,5):
        jump whore_bed_sex_cowgirl_vag_cum_notknow
    tempname.name "[rlist.having_sex_man_dirtytalk]"
    pc "[rlist.having_sex_yes]"
    if not numgen(0,5):
        jump whore_bed_sex_cowgirl_vag_cum_notknow
    "[rlist.having_sex_action_cowgirl_continue]"
    "[rlist.having_sex_enjoy]"
    $ player.face_orgasm()
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_man_close]"
    tempname.name "[rlist.having_sex_man_close_dialogue]"
    jump whore_bed_sex_cowgirl_vag_cum_picker

label whore_bed_sex_cowgirl_vag_cum_picker:
    $ player.sex_cum_location_offer(
    difficulty=0, choice_inside="Keep riding him", choice_pullout="Make him cum outside",  
    cum_want="whore_bed_sex_cowgirl_vag_cum_want", 
    cum_notwant="whore_bed_sex_cowgirl_vag_cum_confused", 
    cum_pullout="whore_bed_sex_cowgirl_vag_cum_pullout_blowjob_init",
    cum_pullout_anal="whore_bed_sex_cowgirl_vag_cum_pullout_anal", 
    cum_bj="whore_bed_sex_cowgirl_vag_cum_pullout_blowjob_init",    
    )

label whore_bed_sex_cowgirl_vag_cum_want:
    pc "[rlist.having_sex_pc_cum_inside_vag_want_dialogue_cowgirl]"
    pc "[rlist.having_sex_yes]"
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
    jump whore_street_sex_end

label whore_bed_sex_cowgirl_vag_cum_confused:
    tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"
    $ player.sex_cum(tempname, "inside", quest_temp)
    pcm "Huh?"
    $ player.spank()
    tempname.name "[rlist.having_sex_man_yes]"
    if player.has_perk(perk_preg_notwant):
        pc "Did you cum?"
        tempname.name "[rlist.having_sex_came_inside_vag_notwant_excuse]"
        pc "[rlist.having_sex_came_inside_vag_notwant_reaction]"
    else:
        pcm "He came already?"
        "Too late to pull out now so I keep riding on his cock until I feel him getting softer inside me."
    $ if_showing("sb_cowgirl", "out", "sb_dpbed", "poke")
    "[rlist.having_sex_came_take_cock_out_vag]"
    jump whore_street_sex_end

label whore_bed_sex_cowgirl_vag_cum_notknow:
    $ player.sex_cum(tempname, "inside", quest_temp)
    "[rlist.having_sex_action_cowgirl_continue]"
    "[rlist.having_sex_enjoy]"
    $ player.face_orgasm()
    pc "[rlist.having_sex_yes]"
    $ player.spank()
    tempname.name "Huff"
    "[rlist.having_sex_came_take_cock_out_vag]"
    pc "You're getting soft, did you cum?"
    tempname.name "[rlist.having_sex_came_inside_vag_notwant_excuse]"
    if player.has_perk(perk_preg_notwant):
        pc "[rlist.having_sex_came_inside_vag_notwant_reaction]"
    else:
        pc "Ah. I got a bit excited and didn't notice."
    $ if_showing("sb_cowgirl", "out", "sb_dpbed", "poke")
    jump whore_street_sex_end

label whore_bed_sex_cowgirl_vag_cum_pullout_anal:
    pc "[rlist.having_sex_pc_cum_pullout_ask_cowgirl_anal]"
    $ if_showing("sb_cowgirl", "poke")
    "I lift my hips up and make sure he slides out of me, then align his cock with my ass."
    "[rlist.having_sex_penetrate_ass_cowgirl]"
    $ player.sex_anal(tempname, quest_temp)
    $ if_showing("sb_cowgirl", "ass")
    "[rlist.having_sex_action_cowgirl]"
    jump whore_bed_sex_cowgirl_anal_cum_want

label whore_bed_sex_cowgirl_vag_cum_pullout_blowjob_init:
    $ renpy.scene()
    $ renpy.show(random(["sb_spitroast down", "sb_layblow"]))
    "I get off of him and lower myself down so I can suck him off."
    jump whore_street_sex_blowjob_jump_cum



label whore_bed_sex_cowgirl_anal:


    "[rlist.having_sex_penetrate_ass_cowgirl]"
    $ player.sex_anal(tempname, quest_temp)
    $ player.face_excited()
    $ if_showing("sb_cowgirl", "ass")
    "[rlist.having_sex_action_cowgirl]"

    if not numgen(0,10):
        call whore_street_sex_standing_spank_call from _call_whore_street_sex_standing_spank_call_3

    "[rlist.having_sex_enjoy_cowgirl_anal]"
    if not numgen(0,30):
        jump whore_bed_sex_cowgirl_anal_cum_confused
    tempname.name "[rlist.having_sex_man_dirtytalk]"
    pc "[rlist.having_sex_yes]"
    if not numgen(0,30):
        jump whore_bed_sex_cowgirl_anal_cum_confused

    "[rlist.having_sex_enjoy]"
    $ player.face_orgasm()
    pc "[rlist.having_sex_yes]"
    if not numgen(0,10):
        jump whore_bed_sex_cowgirl_vag_cum_notknow
    "[rlist.having_sex_man_close]"
    tempname.name "[rlist.having_sex_man_close_dialogue]"
    jump whore_bed_sex_cowgirl_anal_cum_want





label whore_bed_sex_cowgirl_anal_cum_want:
    pc "[rlist.having_sex_pc_cum_inside_ass_want_dialogue_cowgirl]"
    pc "[rlist.having_sex_yes]"
    tempname.name "[rlist.having_sex_man_cum_inside_ass_dialogue]"

    $ player.sex_cum(tempname, "anal", quest_temp)

    $ if_showing("sb_ontop", "happy")
    pc "[rlist.having_sex_yes]"
    pc "[rlist.having_sex_came_inside_ass_want]"
    tempname.name "[rlist.sex_end_man_tired]"
    $ if_showing("sb_cowgirl", "poke")
    "[rlist.having_sex_came_take_cock_out_ass]"
    $ if_showing("sb_cowgirl", "out")
    jump whore_street_sex_end

label whore_bed_sex_cowgirl_anal_cum_confused:
    tempname.name "[rlist.having_sex_man_cum_inside_ass_dialogue]"
    $ player.sex_cum(tempname, "anal", quest_temp)
    pcm "Huh?"
    $ player.spank()
    tempname.name "[rlist.having_sex_man_yes]"
    pcm "He came already?"
    "Too late to pull out now so I keep riding on his cock until I feel him getting softer inside me."
    $ if_showing("sb_cowgirl", "out")
    "[rlist.having_sex_came_take_cock_out_vag]"
    jump whore_street_sex_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
