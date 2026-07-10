

label whore_street_sex_blowjob:
    pc "[rlist.handjob_expecting_cock]"
    $ renpy.scene()
    if loc_cur.loc_type == "room":
        $ renpy.show(random(["sb_blowjob down", "sb_spitroast down", "sb_layblow"]))
    else:
        $ renpy.show(random(["sb_blowjob down", "sb_spitroast down"]))
    with dissolve
    $ if_showing("sb_blowjob", "face up 1h", "sb_spitroast", "mast up", "sb_layblow", "blow")
    pc "[rlist.foreplay_nice_cock]"
    tempname.name "[rlist.foreplay_nice_cock_reply]"
    pc "[rlist.handjob_touch_cock]"
    jump whore_street_sex_blowjob_jump

label whore_street_sex_blowjob_jump:
    if renpy.showing("sb_handjob"):
        $ renpy.scene()
        if loc_cur.loc_type == "room":
            $ renpy.show(random(["sb_blowjob down", "sb_spitroast down", "sb_layblow"]))
        else:
            $ renpy.show(random(["sb_blowjob down", "sb_spitroast down"]))
        with dissolve
    $ player.sex_oral(tempname, quest_temp)
    $ if_showing("sb_blowjob", random(["suck down", "suck 2h down"]), "sb_spitroast", "blow down", "sb_layblow", "down blow")
    "[rlist.blowjob_start_suck]"
    $ if_showing("sb_blowjob", "up", "sb_spitroast", "up", "sb_layblow", "forward")
    pc "[rlist.blowjob_muffle]"
    $ if_showing("sb_blowjob", "down", "sb_spitroast", "down", "sb_layblow", "down")
    tempname.name "[rlist.having_sex_man_yes]"
    "[rlist.blowjob_start_suck_reaction]"
    $ if_showing("sb_blowjob", "up", "sb_spitroast", "up", "sb_layblow", "forward")
    pc "[rlist.blowjob_muffle]"
    if player.soldrequest == "threesome":
        jump whore_street_sex_spitroast_blowstart

    if not ((player.soldrequest in ("vag","anal")) ^ bool(numgen(0,2))):
        jump whore_street_sex_blowjob_sexask_jump
    else:
        jump whore_street_sex_blowjob_jump_cum

label whore_street_sex_blowjob_sexask_jump:
    tempname.name "[rlist.blowjob_sex_ask]"
    if player.check_drunk(5, notif=True) or player.has_perk([perk_broken, perk_sucu], notif=True):
        pc "Mmmm..."
        jump whore_street_sex_sex_picker
    elif player.selling and player.soldrequest in ("hand", "blow", "oral"):
        $ if_showing("sb_blowjob", "poke up 1h", "sb_spitroast", "mast up", "sb_layblow", "forward mast")
        pc "That's not what you paid for."
        $ randomnum = renpy.random.randint(1, 3)
        if randomnum == 1:
            $ dialouge = WeightedChoice([
            ("Shit. I can't afford anything more. Keep sucking then.", 1),
            ("Ah fuck no. Keep sucking me off then.", 1),
            ("Never mind then. I will stick to your mouth.", 1),
            ])
            tempname.name "[dialouge]"
            jump whore_street_sex_blowjob_jump_cum
        else:
            $ temp_var_1 = player.set_whore_price(0) / 4
            tempname.name "How about an extra £[temp_var_1]?"
            menu:
                "Agree":
                    if "should_pay" in quest_whore.list:
                        $ quest_whore.soldprice += temp_var_1
                    else:
                        $ player.add_money_whore(temp_var_1)
                    jump whore_street_sex_sex_picker
                "Refuse":
                    $ dialouge = WeightedChoice([
                    ("Not really worth it. I'll keep sucking him off.", 1),
                    ("For that I would rather just suck him off.", 1),
                    ])
                    pcm "[dialouge]"
                    jump whore_street_sex_blowjob_jump_cum
    elif player.soldrequest in ("vag","anal"):
        jump whore_street_sex_sex_picker
    else:
        menu:
            "Agree" if player.selling or player.check_sex_agree(3):
                jump whore_street_sex_sex_picker
            "Refuse":
                $ dialouge = WeightedChoice([
                ("Just keep sucking him. Not interested in being fucked right now.", 1),
                ("Better not. Stick to him in my mouth", 1),
                ])
                pcm "[dialouge]"
                jump whore_street_sex_blowjob_jump_cum


label whore_street_sex_blowjob_jump_cum:
    $ if_showing("sb_blowjob", "down suck", "sb_spitroast", "down blow", "sb_layblow", "down blow")
    tempname.name "[rlist.having_sex_man_keep_going]"
    "[rlist.blowjob_cum_close]"
    tempname.name "[rlist.having_sex_man_close_dialogue]"
    $ if_showing("sb_blowjob", "angry closed", "sb_spitroast", "angry closed")
    tempname.name "[rlist.blowjob_cum_mouth_man_dialogue]"
    $ player.sex_cum(tempname, "mouth", quest_temp)

    "[rlist.blowjob_cum_mouth]"
    tempname.name "[rlist.having_sex_man_yes]"
    pc "[rlist.blowjob_muffle]"
    $ if_showing("sb_blowjob", "face 1h up happy ub", "sb_spitroast", "straight up neutral mast", "sb_layblow", "forward")
    $ if_showing("sb_blowjob", "laugh", "sb_spitroast", "happy")
    pc "[rlist.blowjob_cum_mouth_swallow_reaction]"
    tempname.name "[rlist.blowjob_cum_mouth_swallow_reaction_man]"
    jump whore_street_sex_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
