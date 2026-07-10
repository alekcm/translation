label pub_drink_start:
    show trixie at right1 with dissolve
    if not trixie.has_met:
        trixie.name "First time seeing your face. I'm [trixie.name]."
        pc "[name]. So easy to spot a new face?"
        trixie.name "One as pretty as yours stands out. What can I get ya sweetie?"
    elif pub_waitress.timesworked > 5:
        trixie.name "Heya [name]. Looking for something to drink?"
    else:
        trixie.name "Heya darlin'. What can I get ya?"

    pc "Beer please [trixie.name]."
    trixie.name "Sure thing hon. Here you go."
    $ player.remove_money(item_beer.value)
    $ player.add_perk(perk_drinking_beer_2, mins=10)
    hide trixie with dissolve
    jump pub_drink_event_picker

label pub_drink_reorder:
    if not player.cash >= item_beer.value:
        pcm "I don't have enough for another..."
        jump pub_drink_reorder_choice_leave
    if not numgen(0,5):

        show trixie at right1 with dissolve
        pc "Another one please [trixie.name]."
        trixie.name "Sure thing hon. Here you go."
        $ player.remove_money(item_beer.value)
        $ player.add_perk(perk_drinking_beer_2, mins=10)
        hide trixie with dissolve
    else:
        "I quicky grab a beer off of [trixie.name] as she is passing."
        $ player.remove_money(item_beer.value)
        $ player.add_perk(perk_drinking_beer_2, mins=10)
    jump pub_drink_event_picker

label pub_drink_reorder_choice:
    pcm "Hmm, finished my drink, should I get another?"
    menu:
        "Get another drink":
            jump pub_drink_reorder
        "That's it for now":
            jump pub_drink_reorder_choice_leave

label pub_drink_reorder_choice_leave:
    pcm "Hmm, I should get going."
    if renpy.showing("male_generic"):
        pc "I'm gonna call it a night."
        pubpatron.name "That's a shame."
        if numgen():
            jump pub_drink_leave_man_attempt_motel
    jump travel

label pub_drink_reorder_force:
    $ player.stat_popup_screen("More booze!")
    pc "More booze!"
    jump pub_drink_reorder

label pub_drink_reorder_too_drunk:
    pcm "Ugh, I am way too pissed to be ordering more..."
    pcm "I should go home or something."
    "I stagger to my feet and look around for the exit."
    $ walk(loc_revel)
    jump travel

label pub_drink_reorder_man_force:
    if not numgen(0,3):
        pubpatron.name "Two more please barmaid."
        show trixie at right1 with dissolve
        trixie.name "Sure thing hon. Here you go."
        pcm "Err, okay..."
        $ player.remove_money(item_beer.value)
        $ player.add_perk(perk_drinking_beer_2, mins=10)
        hide trixie with dissolve
    else:
        "The guy grabs a couple of beers off a passing [trixie.name] and hands me one."

    jump pub_drink_event_picker

label pub_drink_leave_man_attempt_motel:
    pubpatron.name "How about I walk you home?"
    if player.check_nowill(drink_related=True):
        pc "Err, I think I can manage on my own."
        if player.check_nowill(drink_related=True):
            pubpatron.name "Cmon, it's no trouble. Let's go."
            pc "Err, I suppose."
            show male_generic at left1 with dissolve
            $ walk(loc_revel)
            pubpatron.name "I know where, don't worry."
            pc "Okay..."
            show screen blackout() with dissolve
            $ loiter()
            $ walk(loc_motel_lobby)
            hide screen blackout with dissolve
            motel_recep.name "Enjoy your stay."
            $ walk(loc_motel)
            pubpatron.name "Here we go."
            pc "Errr..."
            pubpatron.name "Come on."
            if player.check_nowill(drink_related=True):
                $ motel_book_blue_room(men_amount=1, charge=False)
                $ walk(loc_motel_room)
                pc "We are..."
                pubpatron.name "Yes we are."
                $ event_end_interrupt_label = "pub_drink_motel_sex_end"
                jump whore_street_sex_start_picker
    else:
        if player.selling:
            pc "Oh? Offering more money for something?"
            $ player.set_whore_price(0)
            pubpatron.name "Err, sure. £[player.soldprice] sound good?"
            if player.check_whore_agree_choice():
                pc "Sure, sounds good to me."
                if not numgen(0,3):
                    pubpatron.name "I'm not after a night of fun though, how about something quick?"
                    pc "Oh? I can do that."
                    jump whore_street_customer_pick_location_tombola
                else:
                    "*** TODO JUMP TO FLIRT HEAD TO MODEL FOR WHORE"
        else:
            pc "Oh? I can see what you have in mind."
            pubpatron.name "Yeah, nothing wrong with that."
            if player.check_sex_agree_choice(3, "Sure, let's go somewhere for fun", "No thanks"):
                if not numgen(0,3):
                    pubpatron.name "How about something more local?"
                    pc "Oh? That's what you are after is it?"
                    jump whore_street_customer_pick_location_tombola
                else:
                    "*** TODO JUMP TO FLIRT HEAD TO MODEL FOR CASUAL SEX"
    pc "No thanks mate, I'm just looking to relax a bit."
    if player.selling:
        pc "You should offer some of that money to the bar girls. I'm sure they will be up for something extra."
        pubpatron.name "Sure, I'll give that a try. Enjoy your evening."
    else:
        pubpatron.name "Suit yourself. Have fun."
    pc "You too."
    $ player.reset_sex_status(True)
    hide male_generic with dissolve
    jump pub_drink_reorder_choice

label pub_drink_leave_offer:
    pubpatron.name "Looks like you might have had a bit much to drink."
    jump pub_drink_leave_man_attempt_motel

label pub_drink_leave_closed:
    $ player.hands_reset()
    "Temp label for when the pub is closed."
    $ walk(loc_revel)
    jump travel

label pub_drink_event_picker:
    if not t.hour in loc_pub.opening_hours:
        jump pub_drink_leave_closed
    jump expression WeightedChoice([
    ("pub_drink_reorder_choice", If(not player.drinking and not renpy.showing("male_generic"), 500, 0)),
    ("pub_drink_reorder_force", If(not player.drinking and player.check_nowill(drink_related=True, notif=False) and not player.drink > 90 and not renpy.showing("male_generic"), 2000, 0)),
    ("pub_drink_reorder_too_drunk", If(not player.drinking and player.drunk > 140 and not renpy.showing("male_generic"), 2000, 0)),

    ("pub_drink_reorder_man_force", If(not player.drinking and renpy.showing("male_generic"), 500, 0)),
    ("pub_drink_leave_offer", If(not player.drinking and renpy.showing("male_generic") and player.drunk > 60, player.drunk * 2, 0)),

    ("pub_drink_relax_core", If(player.drinking and not renpy.showing("male_generic"), 500, 0)),
    ("pub_drink_relax_1", If(player.drinking and not renpy.showing("male_generic") and pub_waitress.timesworked > 5, 100, 0)),
    ("pub_drink_relax_2", If(player.drinking and not renpy.showing("male_generic") and dani_here() and not dani.hate, 100, 0)),
    ("pub_drink_relax_3", If(player.drinking and not renpy.showing("male_generic") and simon.has_met and simon_here() and not loc_office_pi.locked, 100, 0)),
    ("pub_drink_relax_4", If(player.drinking and not renpy.showing("male_generic") and bob.has_met and bob_here(), 100, 0)),
    
    
    

    ("pub_drink_relax_robin_1", If(player.drinking and not renpy.showing("male_generic") and robin_here(), 100, 0)),
    ("pub_drink_relax_robin_2", If(player.drinking and not renpy.showing("male_generic") and robin_here(), 100, 0)),
    ("pub_drink_relax_robin_3", If(player.drinking and not renpy.showing("male_generic") and robin_here(), 100, 0)),

    ("pub_drink_relax_robin_leave", If(robin_here() and t.hour == 1 and t.minute > 40 and not "pub_leave_offer" in robin.list, 1000, 0)),


    ("pub_drink_relax_man_1", If(player.drinking and renpy.showing("male_generic"), 500, 0)),

    ("pub_drink_drinkoffer", If(not player.drinking and not renpy.showing("male_generic"), allure_weight(), 0)),
    ("pub_drink_whore_offer", If(not renpy.showing("male_generic") and player.slutty, allure_weight() / 2, 0)),
    
    ])



label pub_drink_relax_core:
    $ loiter(numgen(3,10))
    "[rlist.pub_drink_relax_action]"
    pcm "[rlist.pub_drink_relax_thinking]"
    jump pub_drink_event_picker

label pub_drink_relax_1:
    $ loiter(numgen(3,10))
    "Someone who recognises me as a waitress passes by and stop for a bit of chit chat."
    pc "...haha yeah, you know how it is. Relaxing a bit after a busy day."
    pubpatron.name "Yeah you and me both. Have a good night."
    pc "You too."
    jump pub_drink_event_picker

label pub_drink_relax_2:
    $ loiter(numgen(3,10))
    show dani at right5 with dissolve
    dani.name "Having a relaxing night?"
    pc "Yeah, just thought I would hang ou for a bit."
    dani.name "Have fun."
    pc "You too."
    hide dani with dissolve
    jump pub_drink_event_picker

label pub_drink_relax_3:
    $ loiter(numgen(3,10))
    show simon at right5 with dissolve
    simon.name "Hey [name], keeping yourself safe?"
    pc "As much as I can."
    simon.name "Good, I'll be over here if you want to chat."
    pc "Sure, enjoy yourself."
    hide simon with dissolve
    jump pub_drink_event_picker

label pub_drink_relax_4:
    $ loiter(numgen(3,10))
    show bob at right5 with dissolve
    bob.name "Good to see you again darling."
    pc "You too [bob.name], how's things?"
    bob.name "Shit as usual, but I get by."
    pc "Good to hear."
    hide bob with dissolve
    jump pub_drink_event_picker



label pub_drink_relax_robin_1:
    $ loiter(numgen(3,10))
    "I sit and relax, drinking my beer and watching what [robin.name] is getting up to."
    pcm "She plays coy like the men are annoying her, but makes sure they stay and keep talking to her."
    jump pub_drink_event_picker

label pub_drink_relax_robin_2:
    $ loiter(numgen(3,10))
    "I sit and sip at my beer while glancing at whatever [robin.name] is getting up to."
    pcm "She's got like four guys surrounding her chatting away."
    pcm "Pretending to be all shy but loving the attention."
    jump pub_drink_event_picker

label pub_drink_relax_robin_3:
    $ loiter(numgen(3,10))
    "I sit drinking my beer and notice [robin.name] doing something at the other side of the bar."
    pcm "Does she have her hand in that guys trousers?"
    pcm "Hard to see from here, but pretty sure she does."
    jump pub_drink_event_picker

label pub_drink_relax_robin_leave:
    $ add_to_list(robin.list, "pub_leave_offer")
    $ loiter(numgen(3,10))
    "I sit sipping my beer and notice [robin.name] coming up to me."
    show robin at right4 with dissolve
    robin.name "Hey [name], I'm heading off with some friends, you interested in coming?"
    if renpy.showing("male_genric"):
        robin.name "Bring your friend if you want, the more the merrier."
    pc "Oh? Heading off?"
    menu:
        "Join her and her friends":
            pc "Okay, sure."
            if renpy.showing("male_genric"):
                pc "You coming with us?"
                pubpatron.name "Err, sure. Sounds like fun."
            robin.name "Ohh this will be fun. Let's go."
            hide robin with dissolve
            if player.drinking:
                $ player.drink_finish()
                "I finish up my drink and head out with them."
            hide male_generic with dissolve
            $ walk(loc_revel)
            show robin at left1 with dissolve
            robin.name "Heading to the motel, don't get lost."
            pc "Sure."
            show screen blackout() with dissolve
            $ tempname = robinpubmotel
            $ tempname2 = robinpubmotel2
            $ tempname3 = robinpubmotel3
            $ quest_temp = None
            jump robin_talk_pub_leave_motel
        "Stay here":



            pc "No thanks, you head off without me."
            robin.name "Okay, have fun."
            pc "You too."
            hide robin with dissolve

            if renpy.showing("male_genric"):
                pubpatron.name "Your friend looks like she is in for a fun night."
                pc "Yeah, looks like it."
            jump pub_drink_event_picker


label pub_drink_relax_man_1:
    $ loiter(numgen(3,10))
    "[rlist.pub_drink_talk_relax]"
    pubpatron.name "[rlist.pub_drink_talk_man]"
    pc "[rlist.pub_drink_talk_man_reply]"
    jump pub_drink_event_picker

label pub_drink_relax_man_2:
    $ loiter(numgen(3,10))
    "I sit and chat with the guy who is drinking with me, and he makes it mostly clear he is interested in something."
    pubpatron.name "...to go away and be like that one."
    pc "Haha yeah."
    jump pub_drink_event_picker

label pub_drink_drinkoffer:
    $ male_npc_create_all()
    $ tempname = pubpatron
    $ quest_temp = None
    show male_generic at right5 with dissolve

    pubpatron.name "Hey darling, looks like you're empty."
    pc "Yeah seems so."
    pubpatron.name "Good job I have extra. Here."
    if player.check_nowill(drink_related=True):
        pc "Err, okay. Cheers."
        $ player.add_perk(perk_drinking_beer_2, mins=10)
    else:

        menu:
            "Take the drink":
                pc "Cheers!"
                $ player.add_perk(perk_drinking_beer_2, mins=10)
            "Turn him down":
                pc "No thanks mate, I think I'll just relax alone a bit."
                pubpatron.name "Suit yourself darlin'"
                hide male_generic with dissolve
    jump pub_drink_event_picker

label pub_drink_whore_offer:
    $ male_npc_create_all()
    $ tempname = pubpatron
    $ quest_temp = None
    show male_generic at right5 with dissolve
    $ loiter(numgen(3,10))
    "I sit and relax, drinking my beer when I notice a guy looking to approach me."
    pubpatron.name "Hey darling, you on the job? I'm just looking for someone to chat to."
    if player.check_whore_agree_choice(request="nosex"):
        pc "Bit of cash and free beer, how could I refuse."
        pubpatron.name "Oh nice. Though the beer being free is still over priced."
        pc "Tell me about it..."
        $ player.selling = True
        $ player.set_whore_price(0)
        "The guy sits down and slides £[player.soldprice] over to me."
        $ player.add_money_whore()
    else:
        pc "Sorry mate, just looking to have a drink."
        pubpatron.name "Okay darling, enjoy your night."
        hide male_generic with dissolve
    jump pub_drink_event_picker




label pub_drink_motel_sex_end:
    if player.tired < 20 or player.drunk > 80:
        $ pc_set_temp_outfit()
        "I can barely keep my eyes open after all that, and slowly drift off to sleep while in bed with the guy."
        $ player.eye = 3
        show screen blackout() with dissolve
        jump bed_sleep_loop
    show male_generic at right5 with dissolve
    pubpatron.name "That was fun love."
    pc "Mmmm."
    pubpatron.name "You can keep the room, I'm going to head out."
    pc "Okay, be safe."
    hide male_generic with dissolve
    pcm "I should probably clean up a bit."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
