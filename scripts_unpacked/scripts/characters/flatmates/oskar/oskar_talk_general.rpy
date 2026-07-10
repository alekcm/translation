init python:

    def oskar_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        
        if not oskar.isactive:
            cur_location = None
        
        elif (oskar.day_number <= 2 and t.hour == 12) or (oskar.day_number >= 8 and t.hour == 13): 
            cur_location = None
        elif t.time_from_to(10.00, 10.30) and "oskar_sex" in robin.list and t.wkday in weekend: 
            cur_location = loc_bedroom_robin
        elif t.hour in loc_office_ll.opening_hours: 
            cur_location = loc_office_ll
        
        
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where)

label oskar_talk_pay_rent:
    show oskar at right1 with dissolve
    pc "I'm here to pay the rent."
    jump oskar_talk_pay_rent_choices

label oskar_talk_pay_rent_home:
    $ add_to_list(oskar.list, "asked_rent")
    show oskar at right1 with dissolve
    oskar.name "It's [t.wkday], I've come for the rent."
    if c.exposed and not player.has_perk(perk_exhibitionist):
        $ player.cover()
        pc "Ah! Hold on!"
        $ pc_dress_event("daily", loc_bedroom, loc_cur)
        show oskar at right1
        $ player.uncover()
        pc "Sorry..."

    jump oskar_talk_pay_rent_choices

label oskar_talk_pay_rent_raised:
    if "rent_raised" in quest_rent.list:
        $ remove_from_list(quest_rent.list, "rent_raised")
        if not "rent_raised_argue_1" in quest_rent.list:
            $ add_to_list(quest_rent.list, "rent_raised_argue_1")
            oskar.name "Rent has gone up. It's now £[rent_amount] a week from now on."
            $ player.face_annoyed()
            pc "What? Why? Hard enough to make it as it is and you are putting it up."
            oskar.name "You were getting a good deal before. But there is competition for your room."
            oskar.name "I could probably get even more than what I am charging you if I could be bothered to spend time looking for someone new."
            pc "Ugh."
        elif not "rent_raised_argue_2" in quest_rent.list:
            $ add_to_list(quest_rent.list, "rent_raised_argue_2")
            oskar.name "Rent has gone up. It's now £[rent_amount] a week from now on."
            $ player.face_annoyed()
            pc "Again? Fucking hell, this is getting too much."
            oskar.name "Look around you. This place is better than almost anywhere else someone like you would be able to find."
            oskar.name "I only keep it as cheap as it is because of the academy you go to. They push to keep things low."
            pc "Ugh."
        elif not "rent_raised_argue_3" in quest_rent.list:
            $ add_to_list(quest_rent.list, "rent_raised_argue_3")
            oskar.name "Rent has gone up again. It's now £[rent_amount] a week from now on."
            $ player.face_annoyed()
            pc "Of course... Why not take my liver and kidneys while you are at it."
    return

label oskar_talk_pay_rent_choices:
    if not rent_total_owed():
        oskar.name "You are already paid up."
        pc "Oh? Okay..."
    elif rent_weeks_skipped() > 1:
        call oskar_talk_pay_rent_raised from _call_oskar_talk_pay_rent_raised
        if player.cash < rent_total_owed():
            pcm "Shit, I don't have the money..."
        oskar.name "Well, you are behind, paying off the full amount or?"
        $ temp_var_1 = rent_total_owed()
        $ temp_var_2 = rent_debt_owed()
        $ temp_var_3 = player.has_perk([perk_gamine, perk_addict, perk_sucu, perk_whore, perk_slut, perk_bimbo], notif=False) and log.interactive("quest_rent_b")
        menu:
            "Pay the full amount of £[temp_var_1]" if player.cash >= rent_total_owed():
                $ rent_pay(rent_total_owed())
                oskar.name "Great. Then that's us all cleared up."
                pc "Yup."

            "Pay debt of £[temp_var_2]" if player.cash >= rent_debt_owed():
                $ rent_pay(rent_debt_owed())
                oskar.name "Good. But still waiting on this weeks rent."
                pc "Yeah..."

            "Could I pay it off some other way?" if temp_var_3:
                jump oskar_talk_pay_rent_sex_offer

            "I don't have enough..." if not temp_var_3:
                jump oskar_talk_pay_rent_sex_force
    else:

        call oskar_talk_pay_rent_raised from _call_oskar_talk_pay_rent_raised_1
        $ temp_var_1 = rent_total_owed()
        menu:
            "Pay the rent of £[temp_var_1]" if player.cash >= rent_total_owed():
                $ rent_pay(rent_total_owed())
                oskar.name "Great. Then that's us all cleared up."
                pc "Yup."
            "I don't have enough...":

                oskar.name "Better get the money somehow. You don't want to end up out on the streets."
                pc "..."

    hide oskar with dissolve
    jump travel

label oskar_talk_pay_rent_late_picker:
    if rent_weeks_skipped() <= 4 and not oskar.can_sex:
        jump oskar_talk_pay_rent_sex_force
    else:
        jump oskar_talk_pay_rent_kick_out

label oskar_talk_pay_rent_sex_force:
    $ player.face_worried()
    oskar.name "You are already behind and you want more time?"
    pc "Err, sorry. I only need a little bit more time."
    oskar.name "*Sigh*"
    oskar.name "Look around you Miss [sname]."
    pc "[name]..."
    oskar.name "Do you think you can get something nice like this elsewhere?"
    $ walk(loc_common)
    oskar.name "This nice common room for example. Glass windows, electricity, walls with no holes in it."
    pc "..."
    $ walk(loc_kitchen)
    oskar.name "This kitchen. Has a working fridge, running water and even a microwave."
    pc "Yes..."
    $ walk(loc_bedroom)
    $ player.face_worried()
    oskar.name "Here you have a bed in it's own room, wardrobes, a window..."
    if log.interactive("quest_rent_b"):
        oskar.name "I even told you to clean up to lower your rent, yes you are still so late."
    pc "I know..."
    oskar.name "So what do you expect from me Miss [sname]? Or [name]?"
    if any([pub_waitress.active, quest_flyers.active, quest_scav.active]):
        if pub_waitress.active:
            pc "I am working the pub to earn some cash to pay it off."
            if quest_flyers.active:
                pc "I am also handing out flyers and stuff to earn some extra."
        elif quest_flyers.active:
            pc "I have been earning some money handing out flyers and stuff, I am working..."
        else:
            pc "I have ben working as a scavver to earn some money, I'm not just doing nothing..."
    else:
        pc "Sorry, I am looking for work an ways to earn, but there isn't a lot of work going..."
    oskar.name "And how does any of that help me now [name]?"
    $ player.face_meek()
    pc "..."
    pc "It doesn't..."
    oskar.name "I am going to give you one last chance [name]."
    $ player.face_worried()
    pc "Thank you..."
    oskar.name "Take off your clothes."
    $ player.face_shock()
    pc "What?!"
    oskar.name "Or you can leave and never come back. The choice is yours."
    $ player.face_worried()
    pc "..."
    pcm "Fuck!"
    pcm "Is it really going to be like this?"
    pc "What if..."
    oskar.name "Goodbye Miss [sname]."
    $ player.face_shock()
    pc "Wait! Errr..."
    menu:
        "Undress":
            pc "Right..."
            $ player.face_meek()
            $ pc_strip_tops(True, True)
            if not c.nude:
                oskar.name "I'm waiting..."
            $ player.face_worried()
            pc "..."
            $ pc_striptease(True)
            oskar.name "Good."
            pc "..."
            oskar.name "Now turn around and bend over."
            $ player.face_shock()
            pc "Wait, I thought..."
            oskar.name "You are doing what you like in my house how you please without paying."
            $ player.face_worried()
            oskar.name "Until you are fully paid up, I will do the same to your body. It is mine to do with as I please."
            oskar.name "Now turn around and bend over."
            if player.vvirgin:
                pcm "Fuck, is my first time really going to be like this?"
                pcm "Bent over by this fucker just to pay the rent?"
                pcm "Ugh..."
            elif player.iswhore:
                pcm "Paying off rent like this? Guess it's better than some punter in a piss stinking alley..."
            else:
                pcm "Fuck, is he really going to make me do this?"
                pcm "Of course he is. Piece of shit!"
            menu:
                "Bend over":
                    $ npc_race_picker(oskar)
                    pc "..."
                    hide oskar
                    show sb_table
                    with dissolve
                    show sb_table bentover up with dissolve
                    pcm "Piece of shit..."
                    $ player.spank()
                    oskar.name "Next time you might consider using your arse to actually pay the rent."
                    oskar.name "Go whoring or pay me a visit in my office."
                    show sb_table mast back with dissolve
                    $ player.spank()
                    oskar.name "You gamines aren't worth much else other than bending over anyway."
                    show sb_table sex with dissolve
                    oskar.name "Maybe I will ask your tomboy friend to bend over to pay as well."
                    pcm "Fuck fuck fuck."
                    $ player.sex_forced(oskar)
                    show sb_table back pain with vpunch
                    $ player.sex_vag(oskar, quest_rent)
                    pc "Ah fuck!"
                    oskar.name "Mmm, get used to this."
                    with hpunch
                    oskar.name "You will be doing a lot of it by the looks of it."
                    oskar.name "You shitty whores aren't worth much else if you can't pay the rent."
                    with hpunch
                    pc "Ah be more gentle!"
                    oskar.name "I'll be more gentle when you come to me yourself."
                    oskar.name "Making me come to you? Then I will treat you like I want."
                    pcm "Fuck!"
                    "I just grit my teeth and let him continue. He keeps saying things to me but I mostly drown them out."
                    "He continues like this for a while and then I can feel him getting close."
                    "And before I know it..."
                    $ player.sex_cum(oskar, "inside", quest_rent)
                    oskar.name "Ahh fuck yes!!"
                    oskar.name "Mmm feels so nice."
                    pc "..."
                    $ player.spank()
                    show sb_table bentover shock mast with dissolve
                    show sb_table bentover noman with dissolve
                    pc "You done?"
                    oskar.name "Don't sound too happy. You are still behind on rent."
                    hide sb_table
                    show oskar at right1
                    with dissolve
                    oskar.name "If you want to knock the rent off, come to my office and we can have fun."
                    oskar.name "If you leave it too long and make me come to you though..."
                    oskar.name "Then I will do what I want without knocking anything off."
                    pc "What?"
                    oskar.name "I am doing you a favour by accepting something you can freely pay with."
                    oskar.name "So don't fuck me around and try and avoid it."
                    pc "Right..."
                    $ oskar.can_sex = True
                    $ oskar.dict["rent_sex_offer_day"] = t.day
                    oskar.name "And don't look so miserable next time."
                    pc "Ugh..."
                    hide oskar with dissolve
                    $ player.face_angry()
                    pc "NNNNNNGGGGGGGG!!!!"
                    pcm "FUCKING PIECE OF SHIT!!!!"
                    pcm "Fuck!!!"
                    pcm "Ugh... Raped in my own bedroom by my fucking landlord!"
                    pcm "And the cunt wants me to smile and give him some more?"
                    pcm "Cunt!"
                    $ oskar.hate = True
                    pc "Ugh..."
                    pcm "Should probably wash up or something."
                    jump travel
                "Dress and leave":

                    pc "No, I can't do this..."
                    $ pc_dress_slow()
                    pc "..."
                    oskar.name "Why are you still here? Goodbye Miss [sname]."
                    pc "Okay..."
        "Leave":


            $ player.face_worried()
            $ player.face_cry()
            pc "I'll..."
            oskar.name "You know where the door is."
            pc "..."
            pc "Okay..."

    hide oskar
    $ walk(loc_stairwell)
    pcm "Fuck!"
    $ add_to_list(loc_stairwell.list, "kicked_out")
    $ add_to_list(loc_kitchen.list, "kicked_out")
    $ loc_kitchen.locked = True

    pcm "I need to find somewhere else to stay..."
    $ player.face_wail()
    pc "*SOB*"
    if loc_highway_slum_home.locked:
        $ log.assign("Homeless")
    $ player.add_mood(-200)
    jump travel

label oskar_talk_pay_rent_kick_out:
    oskar.name "Then you have to pack your things and go."
    pc "I can get the money."
    if oskar.can_sex:
        oskar.name "You have had plenty of time as well as alternatives to lower it."
    else:
        oskar.name "You have had plenty of time to work for it."
    oskar.name "Yet I don't see the money."
    oskar.name "Goodbye [name]."
    hide oskar with dissolve
    pcm "Fuck!"
    pcm "Ugh..."
    if "home" in tab_top or c.inappropriate:
        $ pc_dress_event("daily", loc_bedroom, loc_stairwell)
    else:
        $ walk(loc_stairwell)
    pcm "Suppose I need to try and find somewhere else to live..."
    $ add_to_list(loc_stairwell.list, "kicked_out")
    $ add_to_list(loc_kitchen.list, "kicked_out")
    $ loc_kitchen.locked = True

    if loc_highway_slum_home.locked:
        $ log.assign("Homeless")
    jump travel

label oskar_talk_pay_rent_sex_offer_pc_ask:
    $ npc_race_picker(oskar)
    $ oskar.can_sex = True
    $ oskar.dict["rent_sex_offer_day"] = t.day
    pc "So, I think I have some rent to pay don't I?"
    $ temp_var_1 = rent_total_owed()
    oskar.name "£[temp_var_1] according to my books."
    pc "I was wondering if I could do other things to help lower it."
    oskar.name "I already offered that you can clean up around here, I don't have any other work you can do."
    if "knows_dani_sex_oskar" in oskar.list:
        pc "What about how [dani.name] gets a discount?"
    else:
        pc "What about some other ways?"
        pc "Like cheering you up?"
    oskar.name "Are you suggesting what I think you are?"
    pc "I am."
    oskar.name "Then aren't you over dressed?"
    pc "Oh?"
    $ tempname = oskar
    $ quest_temp = quest_rent
    call oskar_sex_striptease from _call_oskar_sex_striptease_4
    $ event_end_interrupt_label = "oskar_talk_pay_rent_sex_offer_pc_ask_end"
    jump oskar_sex_lapsit_start

label oskar_talk_pay_rent_sex_offer_pc_ask_end:
    $ oskar.can_sex = True
    $ oskar.dict["rent_sex_offer_day"] = t.day
    oskar.name "That was fun."
    pc "Mmm."
    $ renpy.scene()
    show oskar at right1
    with dissolve
    $ pc_dress_under()
    pc "So, do I get a discount?"
    $ temp_var_1 = player.set_whore_price(0)
    $ temp_var_2 = player.set_whore_price(2)
    oskar.name "A cheap highway whore probably goes for £[temp_var_1]. You girls are young and look quite nice..."
    $ pc_dress()
    oskar.name "Not like it's really costing me, so I'll pay a bit more, around $[temp_var_2]? Come clean and sexy and I'll pay what you are worth."
    pc "Right... Okay."
    oskar.name "That tomboy could also be good to fuck."
    $ player.face_shock()
    pcm "Shit!! I think I fucked up..."
    hide oskar with dissolve
    if loc(loc_office_ll):
        $ walk(loc_stairwell)
    pcm "Well, kinda worked, kinda didn't. I can pay the rent with my body but I gave him the idea he can also fuck [robin.name]."
    pcm "Better not tell her I am the idiot that gave him the idea."
    jump travel

label oskar_talk_pay_rent_sex_offer:
    $ npc_race_picker(oskar)
    if not oskar.can_sex:
        if rent_weeks_skipped() >= 4:
            jump oskar_talk_pay_rent_punish
        elif not log.interactive("quest_rent_b"):
            oskar.name "Hmmm..."
            jump oskar_talk_ask_work_again_catcher
        else:
            $ oskar.can_sex = True
            $ oskar.dict["rent_sex_offer_day"] = t.day
            $ player.face_shy()
            oskar.name "I already told you you can clean up around here to reduce the rent."
            pc "Yeah, that only drops it a little. I was thinking something a bit more."
            oskar.name "No, cleaning is all the work I have around here."
            pc "What if I offered to make you \"happy\"?"
            oskar.name "You suggesting fucking for rent?"
            $ player.face_worried()
            pc "Err..."
            oskar.name "Hmmm, good idea. You little gamines don't have much else to offer anyway. If ya gonna be late, might as well get some use out of you."
            oskar.name "That tomboy could also be good to fuck."
            $ player.face_shock()
            pcm "Shit!! I think I fucked up..."
            oskar.name "You have better ideas than the idiots I work with."
            $ temp_var_1 = player.set_whore_price(0)
            $ temp_var_2 = player.set_whore_price(2)
            oskar.name "A cheap highway whore probably goes for £[temp_var_1]. You girls are young and look quite nice..."
            oskar.name "Not like it's really costing me, so I'll pay a bit more, around $[temp_var_2]? Come clean and sexy and I'll pay what you are worth."
            pc "Right... Okay."
            hide oskar with dissolve
            if loc(loc_office_ll):
                $ walk(loc_stairwell)
            pcm "Well, kinda worked, kinda didn't. I can pay the rent with my body but I gave him the idea he can also fuck [robin.name]."
            pcm "Better not tell her I am the idiot that gave him the idea."
            jump travel
    else:
        if t.wkday == "Sunday" and loc([loc_kitchen, loc_common, loc_stairwell]) and rent_weeks_skipped() >= 3:
            if rent_weeks_skipped() >= 4:
                jump oskar_talk_pay_rent_punish
            oskar.name "You are already weeks behind. I don't come here so leave empty handed."
            oskar.name "If this gets any more out of hand, you are going to have to find somewhere else to live."
            hide oskar with dissolve
            pcm "Fuck!"
            jump travel
        if not rent_total_owed() and oskar.rape and not player.has_perk([perk_freeuse, perk_sucu]):

            $ dialogue = WeightedChoice([
            ("I'm not offering to do anything with that cunt unless I need to.", 1),
            ("I'm already paid up. I'm not doing anything with him after what he did.", 1),
            ("After what he did? No chance.", 1),
            ("No way, not after what he did.", 1),
            ])
            pcm "[dialogue]"
            jump travel

        elif oskar.rape:
            $ dialogue = WeightedChoice([
            ("Suppose I should pretend to enjoy this...", 1),
            ("Better play nice with this arsehole.", 1),
            ("Ugh, I should put on a happy face.", 1),
            ("Might as well play the nice girl and get this over with.", 1),
            ("Ugh, rent wont pay it's self.", 1),
            ("Might as well get this out of the way and pay some rent.", 1),
            ("Here we go... Gotta pay the rent some how.", 1),
            ])
            pcm "[dialogue]"

        $ dialogue = WeightedChoice([
        ("So, interested in having some fun?", 1),
        ("Want to have a nice break?", 1),
        ("How about we relax a bit?", 1),
        ("Have time to do something more interesting?", 1),
        ])
        pc "[dialogue]"

        if oskar.want_sex():
            if rent_total_owed():
                $ quest_rent.soldprice = player.set_whore_price(2)
            else:
                oskar.name "You know you are already paid up?"
                pc "I know."
                oskar.name "Okay."
            if not loc([loc_bedroom, loc_office_ll]):
                pc "How about we go to my room?"
                $ walk(loc_bedroom)
                pc "Better here."
            if oskar.lust < 50:
                oskar.name "You barely give me time to recover."
                pc "Hmmm. Well let's see if we can get you going."
                jump oskar_sex_foreplay_start
            elif oskar.lust >= 100:
                oskar.name "Sure I would. Come here."
                jump oskar_sex_behind_rough
            else:
                oskar.name "I could do with a break."
                jump expression renpy.random.choice(["oskar_sex_foreplay_start", "oskar_sex_lapsit_start", "oskar_sex_behind_rough"])

            hide oskar with dissolve
            jump travel
        else:

            oskar.name "I can't keep up with you young girls. Give me a bit more time."
            pc "Aww..."
            hide oskar with dissolve
            jump travel

label oskar_talk_pay_rent_punish:
    if not renpy.showing("oskar"):
        show oskar at right1 with dissolve
    oskar.name "[fname]. You are not keeping up with payments."
    $ player.face_shock()
    pc "I..."
    oskar.name "I don't care what you have to say, unless it's \"here is your money\"."
    oskar.name "Is that what you have to say?"
    $ player.face_worried()
    menu:
        "Here is your money" if player.cash >= rent_total_owed():
            $ rent_pay(rent_total_owed())
            oskar.name "Okay then. Thank you."
            if loc(loc_office_ll):
                oskar.name "You can go now."
            hide oskar with dissolve
            pc "Right..."
            jump travel
        "...":
            jump oskar_talk_pay_rent_kick_out
            $ NullAction()


    $ add_to_list(oskar.list, "demanded_casino_work")
    oskar.name "Thought so."
    oskar.name "Look, if you are not paying, then I'll have to kick you out."
    pc "Shit. Look I haven't anywhere else to go."
    oskar.name "That's not my problem."
    pc "Please, is there something else I can do?"
    $ player.face_meek()
    if player.has_perk([perk_whore, perk_slut, perk_gamine, perk_bimbo], notif=True):
        pc "I could pay with my body..."
        oskar.name "Look, I have more gamine whores in my flats than I know what to do with."
        oskar.name "Fucking you is enough to let me knock a bit off, but you are long past that."
    else:
        pc "I don't know... Something."
        $ player.face_shock()
        oskar.name "Look. Even if I told you right now to bend over, that would only get you a little bit off."
        oskar.name "You are in far too deep to fuck your way out of it."
    $ player.face_meek()
    pc "..."
    oskar.name "I'm going to give you one choice here. I'm getting my money if you accept or not. But you won't like what happens if you refuse."
    oskar.name "You are going to work in my casino and accept everything you are told to do there."
    oskar.name "I don't care if you are fucked, knocked up, sold or gambled away. You will say \"yes\" to everything."
    pc "..."
    oskar.name "If what you owe me continues to go up, I will get my money from you in a way you probably won't recover from."
    pcm "Fuck... He's being serious..."
    if not quest_casino.active:
        $ quest_casino.activate()
        $ log.assign("Casino girl")
    oskar.name "I expect you there tonight and every night until what you owe me is zero."
    hide oskar with dissolve
    pcm "Fuck..."
    pcm "Working at his casino. [emile.name] warned me about that ages ago. Mentioned I won't like it at all..."
    pcm "Not much of a choice though..."
    jump travel

label oskar_talk_pay_rent_kickout:
    $ player.grope_breasts()
    $ player.face_shock()
    $ oskar.hate = True
    thug "Got her!"
    pcm "Whaaaa!"
    thug "[oskar.name] told you he would get his money one way or another."
    $ player.punch()
    pc "Nnng!"
    $ player.grope_breasts()
    thug "So you got money on you?"
    $ walk(loc_cur.isolate_loc, trans=hpunch)
    thug "Let's see here..."
    if player.cash >= rent_total_owed():
        thug "Wow, she's actually got the money."
        thug "Thinking you can just avoid him eh bitch?"
        pc "I was going to..."
        $ player.punch()
        thug "Shut up!"
        $ rent_pay(rent_total_owed())
        $ player.spend(player.cash)
        thug "I'm going to take this."
        pc "Ah, no!"
        $ player.punch()
        thug "Shut up!"
        $ player.punch()
        pc "Ah!"
        show screen blackout(50)
        $ player.punch()
        pc "Haaaa fuck!"
        show screen blackout(100)
        $ player.punch()
        $ player.grope_end()
        $ pc_strip()
        $ ko_assault(who=oskar_thug, quest=quest_rent)
        pause 2
        $ player.face_sleep()
        hide screen blackout with dissolve
        pc "Nnnng..."
        $ player.face_pain()
        pc "What the fuck!"
        pc "Ahhh shit!"
        $ player.face_cry()
        pc "Ah fuck it hurts so much!"
        pc "*Sniff*"
        pc "Fuck, even after he took my money for the rent..."
        pc "Cunts!"
        pc "*SOB*"
        jump travel
    else:
        $ add_to_list(oskar.list, "beaten_kicked_out")
        $ rent_pay(player.cash)
        thug "She ain't got enough."
        pc "Give me some time to..."
        $ player.punch()
        thug "Shut up!"
        $ player.punch()
        pc "Ah!"
        show screen blackout(50)
        $ player.punch()
        pc "Haaaa fuck!"
        show screen blackout(100)
        $ player.punch()
        $ player.grope_end()
        $ pc_strip()
        $ ko_assault(who=oskar_thug, quest=quest_rent)
        pause 2
        $ player.face_sleep()
        hide screen blackout with dissolve
        pc "Nnnng..."
        $ player.face_pain()
        pc "What the fuck!"
        pc "Ahhh shit!"
        $ player.face_cry()
        pc "Ah fuck it hurts so much!"
        pc "*Sniff*"
        pc "Fuck, even after he took my money for the rent..."
        pc "Cunts!"
        pc "*SOB*"
        $ add_to_list(loc_stairwell.list, "kicked_out")
        $ add_to_list(loc_kitchen.list, "kicked_out")
        $ loc_kitchen.locked = True

        if loc_highway_slum_home.locked:
            $ log.assign("Homeless")

        $ rent_pay(rent_total_owed(), cash=False)

        jump travel

label oskar_talk_pay_rent_oskardead_1:
    $ oskar.dict["dead_rent_reminder"] += 1
    $ oskar.dict["dead_rent_reminder_date"] = t.day
    pcm "Hmm, with [oskar.name] dead, I wonder if someone will come for the rent today."
    jump travel

label oskar_talk_pay_rent_oskardead_2:
    $ oskar.dict["dead_rent_reminder"] += 1
    $ oskar.dict["dead_rent_reminder_date"] = t.day
    pcm "No one came for the rent last week. Hope it stays that way."
    jump travel

label oskar_talk_pay_rent_oskardead_3:
    $ oskar.dict["dead_rent_reminder"] += 1
    $ oskar.dict["dead_rent_reminder_date"] = t.day
    pcm "Still no one coming for the rent. Hopefully it stays that way."
    pcm "Maybe [dani.nname] killing that shit has something good come from it."
    jump travel

label oskar_poison_event:
    pcm "Hmmm, I could sneak those beers I have in his drawers or something..."
    pcm "Is that something I really want to do though?"
    pcm "I mean I know he is a cunt, but this?"
    menu:
        "Sneak the beers":
            $ inv.drop(item_beer_poison, 4)
            $ oskar.inv.take(item_beer_poison, 4)
            $ add_to_list(oskar.list, "gave_poison_beer")
            pcm "Right, there we go."
            pcm "Not even sure he drinks beer, but I guess I will soon find out..."
        "Don't do it.":

            pcm "No, it's probably a bad idea..."
    jump travel

label oskar_talk_poison_dead_picker:
    jump expression WeightedChoice([

    ("oskar_talk_poison_dead_1", 100),
    ("oskar_talk_poison_dead_2", 100),
    ("oskar_talk_poison_dead_3", 100),
    ])

label oskar_talk_poison_dead_1:
    pcm "Not seen [oskar.name] for a while. Wonder if those beers got him?"
    jump travel

label oskar_talk_poison_dead_2:
    pcm "No [oskar.name] for a while..."
    pcm "Hopefully he doesn't ever come back."
    jump travel

label oskar_talk_poison_dead_3:
    pcm "Still not seen [oskar.name]..."
    pcm "Hopefully he is rotting somewhere."
    jump travel

label oskar_talk_subject:
    jump expression WeightedChoice([

    ("robin_talk_general_1", 100),
    ("robin_talk_general_2", 100),
    ("robin_talk_general_3", 100),

    ("robin_talk_school_1", If(t.day > 4, 100, 0)),
    ("robin_talk_school_2", If(t.day > 4, 100, 0)),
    ("robin_talk_school_3", If(t.day > 4, 100, 0)),
    ("robin_talk_school_4", If(t.day > 4, 100, 0)),

    ("robin_talk_perk_ex_1", If(robin.love > 60 and player.has_perk(perk_exhibitionist), 100, 0)),
    ("robin_talk_perk_ex_2", If(robin.love > 60 and player.has_perk(perk_exhibitionist), 100, 0)),
    ("robin_talk_perk_bimbo_1", If(robin.love > 60 and player.has_perk(perk_bimbo), 100, 0)),
    ("robin_talk_perk_bimbo_2", If(robin.love > 60 and player.has_perk(perk_bimbo), 100, 0)),
    ("robin_talk_perk_gym_1", If(robin.love > 60 and player.has_perk(perk_gym_bunny), 100, 0)),
    ("robin_talk_perk_whore_1", If(robin.love > 60 and player.has_perk(perk_whore), 100, 0)),
    ("robin_talk_perk_whore_2", If(robin.love > 60 and player.has_perk(perk_exhibitionist), 100, 0)),
    ("robin_talk_perk_whore_3", If(robin.love > 60 and player.has_perk(perk_exhibitionist), 100, 0)),
    ("robin_talk_perk_slut_1", If(robin.love > 60 and player.has_perk(perk_slut), 100, 0)),


    ("robin_talk_scav_1", If((t.day + 2) > robin.dict["robin_talk_scav_chain"] and "is_scavver" in robin.list, 100, 0)),
    ("robin_talk_scav_2", If((t.day + 2) > robin.dict["robin_talk_scav_chain"] and "is_scavver" in robin.list, 100, 0)),
    ("robin_talk_scav_3", If((t.day + 2) > robin.dict["robin_talk_scav_chain"]  and "is_scavver" in robin.list and jaylee.love >= 20, 100, 0)),
    ("robin_talk_scav_4", If((t.day + 2) > robin.dict["robin_talk_scav_chain"]  and "is_scavver" in robin.list, 100, 0)),
    ("robin_talk_scav_5", If((t.day + 2) > robin.dict["robin_talk_scav_chain"]  and "is_scavver" in robin.list, 100, 0)),
    ("robin_talk_scav_6", If((t.day + 2) > robin.dict["robin_talk_scav_chain"]  and "is_scavver" in robin.list, 100, 0)),

    ("robin_talk_soccer_play_1", If("soccerboys_ask_tell" in robin.list, 100, 0)),
    ("robin_talk_soccer_play_2", If("soccerboys_ask_tell" in robin.list, 100, 0)),

    ("robin_talk_soccer_hangout_1", If("soccer_hangout" in robin.list, 100, 0)),
    ("robin_talk_soccer_hangout_2", If("soccer_hangout" in robin.list, 100, 0)),
    ("robin_talk_soccer_hangout_3", If("soccer_hangout" in robin.list, 100, 0)),
    ("robin_talk_soccer_hangout_4", If("soccer_hangout" in robin.list, 100, 0)),
    

    ("robin_talk_soccer_sex_1", If("soccerboys_can_sex" in robin.list, 100, 0)),
    ("robin_talk_soccer_sex_2", If("soccerboys_can_sex" in robin.list, 100, 0)),
    ("robin_talk_soccer_sex_3", If("soccerboys_can_sex" in robin.list and player.has_perk(perk_whore), 100, 0)),
    ("robin_talk_soccer_sex_4", If("soccerboys_can_sex" in robin.list, 100, 0)),
    ("robin_talk_soccer_sex_5", If("soccerboys_can_sex" in robin.list and "told_sex_" + rachel._original_name in nate.conversation_topics, 100, 0)),

    ("robin_talk_bussex_1", If("pc_know_want_bussex" in robin.list and busgroper.name in robin.sex_who, 100, 0)),
    ("robin_talk_bussex_2", If("pc_know_want_bussex" in robin.list and busgroper.name in robin.sex_who and busgroper.name in robin.conversation_topics, 100, 0)),
    ("robin_talk_bussex_3", If("pc_know_want_bussex" in robin.list and busgroper.name in robin.sex_who, 100, 0)),
    ("robin_talk_bussex_4", If("pc_know_want_bussex" in robin.list and busgroper.name in robin.sex_who, 100, 0)),
    ("robin_talk_bussex_5", If("pc_know_want_bussex" in robin.list and busgroper.name in robin.sex_who, 100, 0)),
    ("robin_talk_bussex_6", If("pc_know_want_bussex" in robin.list and busgroper.name in robin.sex_who, 100, 0)),
    ("robin_talk_bussex_7", If("pc_know_want_bussex" in robin.list and busgroper.name in robin.sex_who, 100, 0)),
    ("robin_talk_bussex_8", If("pc_know_want_bussex" in robin.list and busgroper.name in robin.sex_who, 100, 0)),
    ("robin_talk_bussex_9", If("pc_know_want_bussex" in robin.list and busgroper.name in robin.sex_who, 100, 0)),
    ("robin_talk_bussex_10", If("pc_know_want_bussex" in robin.list and busgroper.name in robin.sex_who, 100, 0)),

    ("robin_talk_insem_1", If("pc_know_want_sexstories" in robin.list and not player.preg_knows and player.has_perk(perk_preg_want) and player.has_perk(perk_inseminated) and not player.has_perk(perk_period), 100, 0)),
    ("robin_talk_insem_2", If("pc_know_want_sexstories" in robin.list and not player.preg_knows and player.has_perk(perk_preg_want) and player.has_perk(perk_inseminated) and not player.has_perk(perk_period), 100, 0)),
    ("robin_talk_robinfirst_preg_1", If(robin.love > 50 and robin.preg == 0 and player.pregnancy >= 2, 100, 0)),
    ("robin_talk_robinfirst_preg_2", If(robin.love > 50 and robin.preg == 0 and player.pregnancy >= 2, 100, 0)),
    ("robin_talk_robinfirst_robinpreg_1", If(robin.love > 50 and robin.showing and robin.pregbabies == 0 and player.pregbabies, 100, 0)),
    ("robin_talk_robinfirst_robinpreg_2", If(robin.love > 50 and robin.showing and robin.pregbabies == 0 and player.pregbabies, 100, 0)),
    ("robin_talk_robinpreg_1", If(robin.love > 50 and robin.showing, 100, 0)),
    ("robin_talk_robinpreg_2", If(robin.love > 50 and robin.showing, 100, 0)),
    ("robin_talk_preg_1", If(robin.love > 50 and player.showing, 100, 0)),
    ("robin_talk_preg_2", If(robin.love > 50 and player.showing, 100, 0)),
    ("robin_talk_preglate_1", If(robin.love > 50 and player.has_perk(perk_period_late), 100, 0)),
    ("robin_talk_preglate_2", If(robin.love > 50 and player.has_perk(perk_period_late), 100, 0)),

    ("robin_talk_sexgossip_1", If("pc_know_want_sexstories" in robin.list and "soccer_hangout" in robin.list and all([drake.sex, nate.sex, dan.sex]) and not "soccerboys_knows_pc_sex" in robin.list, 100, 0)),
    ("robin_talk_sexgossip_2", If("pc_know_want_sexstories" in robin.list and bob.sex, 100, 0)),
    ("robin_talk_sexgossip_3", If("pc_know_want_sexstories" in robin.list, 100, 0)),
    ("robin_talk_sexgossip_4", If("pc_know_want_sexstories" in robin.list and "licked_ass" in jaylee.conversation_topics and robin.dict["robin_talk_scav_chain"] > (t.day + 5) and "is_scavver" in robin.list, 100, 0)),
    ("robin_talk_sexgossip_5", If("pc_know_want_sexstories" in robin.list and schoolguy.sold and schoolguy.creamvag, 100, 0)),
    ("robin_talk_sexgossip_6", If("pc_know_want_sexstories" in robin.list and parkpervert_dani.sex, 100, 0)),
    ])
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
