label whore_street_sex_handjob:

    $ player.cum_locations["cum_hand"] = 0
    pc "[rlist.handjob_expecting_cock]"
    $ player.sex_hand(tempname, quest_temp)
    $ renpy.scene()
    if loc_cur.loc_type == "room":
        $ renpy.show(random(["sb_handjob down ", "sb_spitroast down mast", "sb_layblow down"]))
    else:
        $ renpy.show(random(["sb_handjob down ", "sb_spitroast down mast"]))
    with dissolve

    pc "[rlist.foreplay_nice_cock]"
    $ if_showing("sb_handjob", "up mast", "sb_spitroast", "up", "sb_layblow", "forward")

    tempname.name "[rlist.foreplay_nice_cock_reply]"
    $ if_showing("sb_handjob", "down", "sb_spitroast", "down", "sb_layblow", "down")
    pc "[rlist.handjob_touch_cock]"
    "[rlist.handjob_wank_cock]"

    tempname.name "[rlist.dirtytalk_handob_guy]"

    $ if_showing("sb_handjob", "up", "sb_spitroast", "up", "sb_layblow", "forward")

    pc "[rlist.dirtytalk_handob_pc]"

    tempname.name "[rlist.having_sex_man_yes]"
    if player.soldrequest == "threesome" and numgen():

        jump whore_street_sex_spitroast_blowstart
    if player.soldrequest in ("vag","anal","threesome") or (not numgen(0,3) and not (player.soldrequest == "hand" or player.want_sexlocation == "hand") and ((player.selling and player.check_sex_agree(4)) or (not player.selling and player.check_sex_agree(2)))):


        pc "[rlist.handjob_blow_offer]"
        tempname.name "Ah fuck yes!"
        jump whore_street_sex_blowjob_jump

    $ if_showing("sb_handjob", "down", "sb_spitroast", "down", "sb_layblow", "down")

    pc "[rlist.handjob_wank_pc_say_man_close]"

    tempname.name "[rlist.handjob_wank_man_say_enjoy]"
    tempname.name "[rlist.having_sex_man_yes]"

    if renpy.showing("sb_handjob"):
        pc "[rlist.handjob_man_cum]"
        "[rlist.handjob_man_cum_action_hand]"
        $ player.sex_cum(tempname, "hand", quest_temp)
        tempname.name "[rlist.handjob_man_cum_yes_dialogue]"
    else:
        tempname.name "[rlist.handjob_man_cum_yes_dialogue]"
        $ if_showing("sb_handjob", "closed", "sb_spitroast", "closed")
        "[rlist.handjob_man_cum_action_face]"
        $ player.sex_cum(tempname, "face", quest_temp)
        pc "[rlist.handjob_man_cum]"

    $ if_showing("sb_handjob", "up", "sb_spitroast", "up", "sb_layblow", "forward")
    pc "[rlist.handjob_pc_cum_reaction]"

    tempname.name "*Phew*"
    jump whore_street_sex_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
