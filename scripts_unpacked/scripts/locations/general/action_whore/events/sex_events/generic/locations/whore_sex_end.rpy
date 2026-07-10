label whore_street_sex_end:
    $ player.face_neutral()
    if event_end_interrupt_label:
        jump expression event_end_interrupt_label

    if not renpy.showing("male_generic"):
        $ renpy.scene()
        show male_generic at right1
        with dissolve
    tempname.name "[rlist.sex_end_compliment]"



    if loc(loc_motel_pinkroom) or (loc(loc_motel_shower) and loc_from == loc_motel_pinkroom):
        jump pinkroom_sex_end

    if any(x in loc_cur.name for x in ("loc_flat","loc_lorry")):
        if "should_pay" in quest_whore.list:
            pc "Okay, now pay up."
            tempname.name "[rlist.whore_start_location_give_money_reply]"
            $ player.soldprice = quest_whore.soldprice
            $ player.add_money_whore()

        $ pc_dress()
        pc "[rlist.sex_end_pc_goodbye]"
        $ renpy.scene()
        with dissolve
        if not loc_from in dis_misc.locs:
            $ walk(loc_from)
        else:
            $ walk(dis_cur.hub)
    else:
        if "should_pay" in quest_whore.list:
            pc "Good, now pay up."
            if player.check_victim() and not dis(dis_partyhouse):
                $ player.face_annoyed()
                $ renpy.scene()
                with hpunch
                "The guy looks at me and then runs off."
                pc "Arsehole!"
                pcm "Should have got paid first..."
            else:
                tempname.name "[rlist.whore_start_location_give_money_reply]"
                $ player.soldprice = quest_whore.soldprice
                $ player.add_money_whore()
        else:
            tempname.name "[rlist.sex_end_goodbye]"
        $ renpy.scene()
        with dissolve

        if any(s in loc_cur.name for s in ("toilet", "bathroom", "shower", "locker", "bedroom", "trailer", "changingroom")):
            pcm "I had better clean up before heading back out there."
            "I head to the sink and clean up any cum from my body."
            $ player.cum_clean_outside()

        if not c.pants and globals()[tab_top].pants and not numgen(0,5):
            $ wardrobe.drop(globals()["item_pants_" + str(globals()[tab_top].pants)])
            $ player.face_angry()
            pc "Did he take my pants as a trophy? Fuck!"
            $ player.face_normal()

        $ pc_dress_slow()

        if quest_cleaner.workcycle:
            pc "Ok, better get back to work."
            jump action_clean_event_picker

        if quest_flyers.workcycle:
            pc "Ok, back to handing out flyers."
            jump action_flyer_event_picker

        if dis(dis_pub) and pub_waitress.workcycle:
            pc "Ok, let's get back to work."
            if not numgen(0,4) and loc(loc_pub_toilet_boys):
                jump whore_street_sex_post_offer
            jump pub_waitress_work_cycleend

        if not numgen(0,10) and loc_cur.outside:
            jump whore_street_sex_post_offer

        if loc_cur.home_location:
            $ NullAction()
        elif not loc_from in dis_misc.locs:
            $ walk(loc_from)
        else:
            $ walk(dis_cur.hub)
    if player.cum_visible:
        pcm "I should probably clean myself up. People can see cum on me."
    jump travel

label whore_street_sex_post_offer:
    $ male_npc_create()
    $ npc_race_picker()
    $ player.reset_sex_status(True)
    $ player.set_whore_price(0)
    $ player.face_confused()

    show male_generic at right1
    with dissolve

    tempname.name "Hey luv. Got time for another customer?"

    if player.check_whore():
        pc "Oh?"
        tempname.name "How does £[player.soldprice] sound?"

        $ player.face_normal()

        if player.cum_locations["cum_vagin"]:
            pc "Err, I'm kind of leaking everywhere down there so probably only good for a blowjob until I clean up."

            if not numgen(0,5):
                tempname.name "I'm fine with sloppy seconds for a discount."
                $ player.soldrequest = "vag"
                $ player.soldprice = int(player.soldprice * 0.7)
            else:
                tempname.name "I can settle for a blowie."
                $ player.soldrequest = "blow"

        if player.check_whore_agree_choice():
            jump whore_sex_start
        else:
            pc "Sorry, not now."
            tempname.name "Ah, ok..."
    else:
        $ player.face_worried()
        pc "Ugh. I'm leaving."

    if dis(dis_pub) and pub_waitress.workcycle:
        jump pub_waitress_work_cycleend

    jump travel

label whore_street_sex_force_end:
    $ player.face_neutral()
    if event_end_interrupt_label:
        jump expression event_end_interrupt_label

    if loc(loc_motel_pinkroom) or (loc(loc_motel_shower) and loc_from == loc_motel_pinkroom):
        jump pinkroom_sex_end

    if any(x in loc_cur.name for x in ("loc_flat","loc_lorry")):
        $ renpy.scene()
        with dissolve
        "The guy seems to have lost interest, so I get out as fast as I can, grabbing whatever clothes I can on the way."
        if not loc_from in dis_misc.locs:
            $ walk(loc_from)
        else:
            $ walk(dis_cur.hub)
        pcm "Fuck."
        $ pc_dress_lost_clothes()
    else:
        pcm "Did the cunt go?"
        $ renpy.scene()
        with dissolve
        pcm "Fuck. What a cunt!"

        call whore_street_sex_force_recover_clothes from _call_whore_street_sex_force_recover_clothes

        pc "Fuck this, I am done."

        if quest_cleaner.workcycle:
            jump action_clean_event_done_change

        if quest_flyers.workcycle:
            jump action_flyer_event_done_change

        if dis(dis_pub) and pub_waitress.workcycle:
            jump pub_waitress_work_home

        if not loc_from in dis_misc.locs:
            $ walk(loc_from)
        else:
            $ walk(dis_cur.hub)
    jump travel

label whore_street_sex_force_recover_clothes:
    "I take a look around, trying to recover what clothes I can find."
    $ pc_dress_lost_clothes()
    pcm "Fucking hell..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
