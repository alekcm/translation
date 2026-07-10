



label pub_waitress_work_harass:
    $ pub_tips()
    $ rand_choice = WeightedChoice([
    ("pub_waitress_work_harass_beer_1", 100),
    ("pub_waitress_work_harass_beer_2", 100),
    ("pub_waitress_work_harass_beer_3", 100),
    ("pub_waitress_work_harass_beer_4", 100),
    ("pub_waitress_work_harass_beer_5", 100),

    ("pub_waitress_work_harass_general_1", 100),
    ("pub_waitress_work_harass_general_2", 100),
    ])
    jump expression rand_choice

label pub_waitress_work_harass_beer_1:
    show pub_stand with dissolve
    patron "Hey [rlist.name_deg]. Got some beers for us?"
    pc "If you ordered, then yes."
    patron "Will it be you giving them to us?"
    pc "Probably."
    patron "Looking forward to it."
    hide pub_stand with dissolve
    jump pub_waitress_work_ogleend

label pub_waitress_work_harass_beer_2:
    show pub_stand with dissolve
    patron "Oooh sexy beer lady!"
    pc "Careful, I'll spill this on you."
    patron "Right. Fucking hell girl you are sexy."
    pc "Thanks..."
    hide pub_stand with dissolve
    jump pub_waitress_work_ogleend

label pub_waitress_work_harass_beer_3:
    show pub_stand with dissolve
    patron "Hey [rlist.name_sexy]. Ditch the beer and I'll pay you to do something better."
    if player.check_nowill():
        pc "Err, I think I should..."
        patron "C'mon. Quickie and job done."
        if player.has_perk([perk_meek, perk_broken], notif=True):
            $ player.set_whore_price(0)
            pc "Right. Let me put these somewhere first."
            patron "Yup."
            $ player.hands_reset()
            jump whore_street_customer_pick_location_tombola
        else:
            pc "I think I'd better go..."
            hide pub_stand with dissolve
            jump pub_waitress_work_ogleend
    else:
        pc "*Tsk*"
        pc "Asking such things like that won't get you anywhere."
        $ player.set_whore_price(0)
        patron "C'mon. Quickie and job done. I'll give you £[player.soldprice]. How's that?"
        if player.check_whore():
            menu:
                "Agree":
                    $ player.hands_reset()
                    jump whore_street_customer_pick_location_tombola
                "Refuse":

                    $ NullAction()
        pc "No thanks. Try being nicer and ask someone else."
        patron "[rlist.name_sexy_upper]."
        pc "Yeah yeah."
        hide pub_stand with dissolve
        $ player.add_mood(-5)
        pcm "Arsehole."
        jump pub_waitress_work_ogleend

label pub_waitress_work_harass_beer_4:
    show pub_stand with dissolve
    patron "Oooh [rlist.name_sexy]!"
    pc "Careful, I've got beers."
    patron "I know."
    show pub_stand mast with dissolve
    pc "*Tsk* Really?"
    patron "Mmmm."
    patron "Interested?"
    if player.has_perk([perk_sucu, perk_bimbo, perk_slut], notif=True) or player.check_sex_agree():
        pc "Err..."
        pc "Not the worst I have seen."
        patron "Wanna suck on it?"
        pc "You try this with all the girls?"
        patron "Sometimes."
        pc "And how's that working out for you?"
        patron "Not well."
        if player.check_sex_agree_choice(diff=2,option1="Suck his cock" ,option2="Leave him to it"):

            pc "Come on then. Let me put these beers down and I'll suck it for you."
            patron "Really?"
            $ player.hands_reset()
            pc "Yup. Come on."
            $ player.soldrequest = "blow"
            jump whore_street_customer_pick_location_tombola
        else:

            $ NullAction()
    pc "I'm gonna get back to work."
    if not numgen(0,15):
        patron "Haaaa!"
        $ player.sex_cum(nosex, "belly", pub_waitress)
        pc "Ugh. Really?"
        patron "Ahhhhhhh..."
        pc "..."
    else:
        patron "Oh?"
        pc "Good luck."
    hide pub_stand with dissolve
    jump pub_waitress_work_ogleend

label pub_waitress_work_harass_beer_5:
    show pub_stand mast with hpunch
    if player.has_perk([perk_sucu, perk_slut, perk_bimbo], notif=True):
        pc "Oh? What's this?"
        patron "Nnnngggg..."
        pc "Been beating off watching us?"
        patron "Haaaa..."
        $ player.sex_cum(nosex, "belly", pub_waitress)
        patron "Ahhhhhhh..."
        pc "..."
        patron "Huuufffff..."
        pc "Right then..."
    elif player.check_nowill():
        $ player.face_shock()
        pc "Ah!"
        patron "Nnnngggg..."
        pc "What are you...?"
        patron "Haaaa..."
        $ player.sex_cum(nosex, "belly", pub_waitress)
        $ player.face_shock()
        patron "Ahhhhhhh..."
        pc "..."
        patron "Huuufffff..."
        pc "..."
    else:
        $ player.face_annoyed()
        pc "Get off!"
        hide pub_stand with vpunch
        pcm "Idiot!"
        jump pub_waitress_work_ogleend
    hide pub_stand with dissolve
    jump pub_waitress_work_ogleend





label pub_waitress_work_cycleend_harass:
    $ pub_tips()
    $ rand_choice = WeightedChoice([
    

    ("pub_waitress_work_harass_general_1", 100),
    ("pub_waitress_work_harass_general_2", 100),
    ])
    jump expression rand_choice

label pub_waitress_work_harass_nobeer_1:
    show pub_stand with dissolve
    "Temp event where you are heading back to the bar and someone approaches you."
    show pub_stand mast with dissolve
    "He might do something more..."
    hide pub_stand with dissolve
    jump pub_waitress_work_picker





label pub_waitress_work_harass_general_1:
    show pub_stand with hpunch
    patron "Ooh, sorry [rlist.name_deg]. Bit much to drink."
    pc "Right. Make sure you can walk out of here later."
    patron "Will do!"
    hide pub_stand with dissolve
    if player.left_hand:
        jump pub_waitress_work_ogleend
    else:
        jump pub_waitress_work_picker

label pub_waitress_work_harass_general_2:
    show pub_stand with dissolve
    patron "Hey [rlist.name_cute]. Up for some extra cash?"
    pc "Oh?"
    $ player.set_whore_price(0)
    patron "£[player.soldprice]?"
    if player.check_whore_agree_choice("Sure, could always do with something extra."):
        patron "Great!"
        $ player.hands_reset()
        jump whore_street_customer_pick_location_tombola
    pc "Sorry mate. Not interested. Ask one of the other girls."
    patron "Right. Ok."
    hide pub_stand with dissolve
    if player.left_hand:
        jump pub_waitress_work_ogleend
    else:
        jump pub_waitress_work_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
