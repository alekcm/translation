label whore_sex_debug:
    "Are you selling yourself?"
    menu:
        "Yes":
            $ player.set_whore_price(0)
            "Where did you agree to have sex?"
            menu:
                "Handjob":
                    $ player.soldrequest = "hand"
                    $ player.want_sexlocation = player.soldrequest
                "Blowjob":
                    $ player.soldrequest = "oral"
                    $ player.want_sexlocation = player.soldrequest
                "Anal sex":
                    $ player.soldrequest = "anal"
                    $ player.want_sexlocation = player.soldrequest
                "Vag sex":
                    $ player.soldrequest = "vag"
                    $ player.want_sexlocation = player.soldrequest
                "No agreement was made":
                    $ player.soldrequest = ""
        "No":



            $ NullAction()





    jump whore_sex





label whore_sex:
    $ npc_race_picker()




    if check_if_isolated():
        pc "[rlist.start_location_here_is_good]"
    else:
        pc "Let's go somewhere a bit quieter."
        $ travel_isolate()

label whore_sex_start:

label whore_sex_pay:

    if player.soldprice and not player.has_perk(perk_freeuse):
        $ add_to_list(quest_whore.list, "should_pay")
        $ quest_whore.soldprice = player.soldprice
        if player.isbroken and not numgen(0,10):
            pc "..."
            $ remove_from_list(quest_whore.list, "should_pay")

        elif not player.check_int(notif=False) and not tempname.is_unique and not numgen(0, 30):
            tempname.name "I'll pay after, make sure you are worth it."
            if player.check_nowill():
                pc "..."
            else:
                pc "Now or I'm gone."
                if player.check_victim():
                    jump whore_street_sex_forced_attack
                else:
                    tempname.name "Right..."
                    $ player.add_money_whore()
        else:
            pc "[rlist.whore_start_location_give_money]"
            tempname.name "[rlist.whore_start_location_give_money_reply]"
            $ player.add_money_whore()














    if not player.soldprice and not player.check_nowill(notif=False):
        menu:
            "Actually, I can't do this":
                jump whore_street_sex_bail_picker
            "Let's see your cock" if player.check_sex_agree(1, notif=False):
                jump whore_street_sex_nosex_picker
            "I want to have sex" if player.check_sex_agree(3, notif=False):
                jump whore_street_sex_sex_picker
    else:
        jump whore_street_sex_start_picker

label whore_street_sex_bail_picker:
    $ player.face_worried()
    pc "Err..."
    pc "Actually I don't think I can do this..."
    pc "I am going to go..."
    jump expression WeightedChoice([
    ("whore_street_sex_bail_beat", 130 - player.int),
    ("whore_street_sex_bail_curse", 200 - player.int),
    ("whore_street_sex_bail_pay", If(not player.soldprice, 150, 0)),
    ("whore_street_sex_bail_leave", 500),
    ])

label whore_street_sex_bail_leave:
    tempname.name "Err, okay..."
    pc "Sorry..."
    $ walk(get_isolate_return_locs())
    pc "*Sigh*"
    if pub_waitress.workcycle:
        jump pub_waitress_work_picker
    jump travel

label whore_street_sex_bail_pay:
    tempname.name "What if I offered to pay?"
    pc "Pay?"
    if player.check_whore():
        $ player.set_whore_price(0)
        pc "Hmm, how much?"
        tempname.name "Let's see... How about £[player.soldprice]?"
        pc "..."
        menu:
            "Agree":
                pc "Okay then. I guess so."
                tempname.name "Great!"
                jump whore_sex_pay
            "Refuse":
                pc "Sorry, I can't..."
                jump whore_street_sex_bail_leave
    pc "Sorry, I can't..."
    jump whore_street_sex_bail_leave

label whore_street_sex_bail_curse:
    tempname.name "Fuckin teasing bitch!"
    pc "Wha..."
    pcm "Fuck, better get out of here..."
    tempname.name "CUNT!"
    $ walk(get_isolate_return_locs())
    $ player.add_mood(-20)
    pcm "What the hell... Arsehole."
    jump whore_street_sex_bail_leave

label whore_street_sex_bail_beat:
    tempname.name "Fuckin teasing bitch!"
    pc "Wha..."
    pc "Fuck, better get out of..."
    jump whore_street_sex_forced_attack
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
