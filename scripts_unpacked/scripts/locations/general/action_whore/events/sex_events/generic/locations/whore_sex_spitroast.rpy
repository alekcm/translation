label whore_street_sex_spitroast_start:
    jump expression WeightedChoice([
    ("whore_street_sex_spitroast_blowstart", 100),
    ("whore_street_sex_spitroast_sexstart", 100),  
    ])

label whore_street_sex_spitroast_blowstart:
    pc "[rlist.handjob_expecting_cock]"
    $ player.sex_hand(tempname, quest_temp)
    if loc_cur.loc_type == "room":
        $ renpy.show(random(["sb_spitroast down mast", "sb_layblow down"]))
    else:
        $ renpy.show("sb_spitroast down mast")
    with dissolve

    call whore_street_sex_spitroast_blow from _call_whore_street_sex_spitroast_blow

    $ if_showing("sb_spitroast", "back", "sb_layblow", "forward")
    "While I am sucking this guy's cock, I feel something going on behind me and have a pretty good idea what."
    $ renpy.scene()
    show sb_doggy1 poke blow
    with dissolve
    "He starts touching my ass and rubbing his cock against me."
    call expression WeightedChoice([
    ("whore_street_sex_spitroast_sex_vag", 100),
    ("whore_street_sex_spitroast_sex_anal", 10),
    ]) from _call_expression_19

    jump whore_street_sex_spitroast_continue

label whore_street_sex_spitroast_sexstart:
    $ if_showing("sb_doggy1", "poke", "sb_doggy2", "pokevaghold")
    "[rlist.having_sex_tease_vag]"
    "[rlist.having_sex_penetrate_vag_slow]"
    $ if_showing("sb_doggy1", "ag vag head_down", "sb_doggy2", "head_back happy wink insidevag")
    $ player.sex_vag(tempname, quest_temp)
    $ player.face_excited()

    call expression WeightedChoice([
    ("whore_street_sex_spitroast_sex_vag", 100),
    ("whore_street_sex_spitroast_sex_anal", 10),
    ]) from _call_expression_22

    call whore_street_sex_spitroast_blow from _call_whore_street_sex_spitroast_blow_1
    jump whore_street_sex_spitroast_continue

label whore_street_sex_spitroast_blow:
    "I start wanking him off while looking at this cock."
    pc "[rlist.foreplay_nice_cock]"
    $ if_showing("sb_spitroast", "up", "sb_layblow", "forward")

    tempname.name "[rlist.foreplay_nice_cock_reply]"
    $ if_showing("sb_spitroast", "down", "sb_layblow", "down")
    pc "[rlist.handjob_touch_cock]"
    "[rlist.handjob_wank_cock]"

    tempname.name "[rlist.dirtytalk_handob_guy]"

    $ if_showing("sb_spitroast", "up", "sb_layblow", "forward")

    pc "[rlist.dirtytalk_handob_pc]"

    $ player.sex_oral(tempname, quest_temp)
    $ if_showing("sb_spitroast", "blow down", "sb_layblow", "down blow")
    "[rlist.blowjob_start_suck]"
    $ if_showing("sb_blowjob", "up", "sb_spitroast", "up", "sb_layblow", "forward")
    pc "[rlist.blowjob_muffle]"
    $ if_showing("sb_blowjob", "down", "sb_spitroast", "down", "sb_layblow", "down")
    tempname.name "[rlist.having_sex_man_yes]"
    "[rlist.blowjob_start_suck_reaction]"
    return

label whore_street_sex_spitroast_sex_anal:

label whore_street_sex_spitroast_sex_vag:
    $ if_showing("sb_doggy1", "poke", "sb_doggy2", "pokevaghold")
    "[rlist.having_sex_tease_vag]"
    "[rlist.having_sex_penetrate_vag_slow]"
    $ if_showing("sb_onfours", "up vag", "sb_ontop", "back ag", "sb_doggy1", "ag vag head_down", "sb_doggy2", "head_back happy wink insidevag", "sb_assup", "sex")
    $ player.sex_vag(tempname, quest_temp)
    $ player.face_excited()
    return

label whore_street_sex_spitroast_continue:
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
