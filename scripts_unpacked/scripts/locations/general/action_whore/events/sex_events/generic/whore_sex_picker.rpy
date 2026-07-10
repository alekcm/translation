default whore_street_sex_end_jumper = ""

label whore_street_sex_start_picker:
    if player.soldrequest == "hand":
        jump whore_street_sex_handjob_picker
    elif player.soldrequest in ("oral", "blow"):
        jump whore_street_sex_blowjob_picker
    $ rand_choice = WeightedChoice([
    ("whore_street_sex_handjob_picker", 50),
    ("whore_street_sex_blowjob_picker", 50),
    ("whore_street_sex_standing", 150),
    ("whore_street_sex_floor", If(not (loc_cur.loc_type == "conc" or loc_cur.loc_type == "tile"), 150, 0)),
    ("whore_bed_sex_start", If(loc_cur.loc_type == "room", 500, 0)),
    ])

    call whore_street_sex_strip_call (not rand_choice.endswith("job_picker")) from _call_whore_street_sex_strip_call_2

    jump expression rand_choice


label whore_street_sex_sex_picker:
    call whore_street_sex_strip_call from _call_whore_street_sex_strip_call_1
    jump expression WeightedChoice([
    ("whore_street_sex_standing", 50),
    ("whore_street_sex_floor", If (not (loc_cur.loc_type == "conc" or loc_cur.loc_type == "tile"), 100, 0)),
    ("whore_bed_sex_start", If (loc_cur.loc_type == "room", 500, 0)),
    ])

label whore_street_sex_dp_picker:
    call whore_street_sex_strip_call from _call_whore_street_sex_strip_call_6
    jump expression WeightedChoice([
    ("whore_street_sex_dp_bed_start", If(not (loc_cur.loc_type == "conc" or loc_cur.loc_type == "tile"), 100, 0)),
    ("whore_street_sex_dp_stand_start", If(player.soldrequest == "rough", 100, 0)),
    ])

label whore_street_sex_handjob_picker:
    call whore_street_sex_strip_call (False) from _call_whore_street_sex_strip_call_3
    jump expression WeightedChoice([
    ("whore_street_sex_handjob", 50),
    ])

label whore_street_sex_blowjob_picker:
    call whore_street_sex_strip_call (False) from _call_whore_street_sex_strip_call_4
    jump expression WeightedChoice([
    ("whore_street_sex_blowjob", 50),
    ])

label whore_street_sex_nosex_picker:
    call whore_street_sex_strip_call (False) from _call_whore_street_sex_strip_call_8
    jump expression WeightedChoice([
    ("whore_street_sex_handjob_picker", If(player.soldrequest == "hand", 50000, 1)),
    ("whore_street_sex_blowjob_picker", If(player.soldrequest in ("oral", "blow"), 50000, 1)),
    ])

label whore_bed_sex_start:
    call whore_street_sex_strip_call from _call_whore_street_sex_strip_call_7
    jump expression WeightedChoice([
    ("whore_bed_sex_cowgirl", 50),
    ("whore_bed_sex_onback", 50),
    ])

label whore_street_sex_strip_call(pensex=True):
    if dis(dis_pub) and c.outfit == 6 and pub_waitress.workcycle:
        if pensex:
            $ c.pants = 0
    elif not c.nude:
        if not numgen(0,3):


            $ pc_striptease()
            $ renpy.scene()
            if numgen():
                show sb_pose_showbreasts happy
                with dissolve
                pc "[rlist.foreplay_like_boobs_ask]"
            else:
                show sb_pose_lookback happy
                with dissolve
                pc "[rlist.foreplay_like_ass_ask]"

            tempname.name "Mmmm."
            $ renpy.scene()
            with dissolve
        elif numgen():
            if renpy.showing("male_generic"):
                hide male_generic with dissolve
            $ player.grope_breasts()
            $ pc_strip_upper()
            "Without much warning, he comes over to me, kissing and groping me while stripping me off."
            $ player.grope()
            tempname.name "So sexy."
            pc "Oh wow."
            $ player.grope_hips()
            $ pc_strip_lower()
            tempname.name "I am going to have so much fun with you."
            pc "Mmmm..."
            $ player.grope()
            tempname.name "Dirty girl."
            $ player.grope_end()
            show male_generic nude at right5 with dissolve
        else:
            $ pc_strip()
            if renpy.showing("male_generic"):
                show male_generic nude with dissolve

    return

label whore_street_sex_strip_full_call:
    if not c.nude:
        $ pc_striptease()
        $ renpy.scene()
        if numgen():
            show sb_pose_showbreasts happy
            with dissolve
            pc "[rlist.foreplay_like_boobs_ask]"
        else:
            show sb_pose_lookback happy
            with dissolve
            pc "[rlist.foreplay_like_ass_ask]"

        tempname.name "Mmmm."
        $ renpy.scene()
        with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
