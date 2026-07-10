label random_event_generic_drunk:
    jump expression WeightedChoice([
    ("random_event_generic_drunk_1", 100),
    ("random_event_generic_drunk_2", 100),
    
    
    ])

label random_event_generic_drunk_1:
    pcm "Ohh, think I've had a bit much to drink."
    jump travel

label random_event_generic_drunk_2:
    pcm "I need to calm down on the booze..."
    jump travel

label random_event_generic_drunkblackout:
    jump expression WeightedChoice([
    ("random_event_generic_drunkblackout_1", 100),
    ("random_event_generic_drunkblackout_2", 100),
    ("random_event_generic_drunkblackout_3", 100),
    ("random_event_generic_drunkblackout_4", 100),
    ("random_event_generic_drunkblackout_5", 100),
    ("random_event_generic_drunkblackout_6", 100),
    ("random_event_generic_drunkblackout_7", If(travel_toilet_girls(True), 100, 0)),
    ("random_event_generic_drunkblackout_8", 100),
    ])




label random_event_generic_drunkblackout_1:
    pc "Whoo. Heads spinning."
    jump travel

label random_event_generic_drunkblackout_2:
    man "Hey baby. How about sharing a drink with us?"
    if player.has_perk(perk_despondent):
        pcm "Anything to cheer me up."
        jump random_event_generic_drinking_with_men
    elif player.has_perk(perk_alcoholic) and not (inv.qty(item_beer) or inv.qty(item_brew) or inv.qty(item_winebottle)):
        pc "You have some with you?"
        if numgen():
            man "We can get some."
            pc "Pfft. Then speak to me when you have."
            "I walk away from the guys."
            jump travel
        else:
            man "Sure we do. Come join us."
            if player.check_speech(4):
                menu:
                    "Go with them fo a drink":
                        jump random_event_generic_drinking_with_men
                    "Turn them down":
                        pc "no thanks. I think I gotta get home."
                        "I stagger off, leaving the guys behind."
                        jump travel
            else:
                jump random_event_generic_drinking_with_men
    elif player.check_speech(2):
        menu:
            "Go with them fo a drink":
                jump random_event_generic_drinking_with_men
            "Turn them down":
                pc "no thanks. I think I gotta get home."
                "I stagger off, leaving the guys behind."
                jump travel
    else:
        jump random_event_generic_drinking_with_men

label random_event_generic_drunkblackout_3:
    pc "Ugh. I can barely walk..."
    pc "Ughhhh..."
    show screen blackout() with dissolve
    jump random_event_generic_wakedrunk

label random_event_generic_drunkblackout_4:
    with vpunch
    pc "Ah fuck."
    pcm "Can hardly walk..."
    jump travel

label random_event_generic_drunkblackout_5:
    show screen blackout(50) with Dissolve(0.2)
    hide screen blackout with Dissolve(0.2)
    pcm "Ugh, i need to sleep this off..."
    $ travel_isolate()
    pcm "This should be a good place."
    show screen blackout() with dissolve
    jump random_event_generic_wakedrunk

label random_event_generic_drunkblackout_6:
    $ player.grope_breasts()
    man "Hey baby. How about coming to drink with me?"
    pc "Hey!"
    $ player.grope_hips()
    man "Don't be shy, come on."
    $ tempname = streetman
    $ quest_temp = None
    if player.check_drunk(5):
        $ travel_isolate()
        pc "Hey... Where you taking me?"
        man "Somewhere we can have some more fun."
        pc "Ugh..."
        $ player.grope_end()
        jump whore_street_sex_start_picker
    else:
        if player.check_sex_agree_choice(4):
            $ travel_isolate()
            pc "Take me somewhere we can have fun."
            man "Of course."
            $ player.grope_end()
            jump whore_street_sex_start_picker
        else:
            pc "Nooo. Go away."
            if player.check_fight(1):
                $ player.grope_end()
                "I push myself out of the guys arms and walk away."
                jump travel
            else:
                "I try and push out the the guys arms, but am too drunk to do anything."
                $ player.grope()
                man "Aww, don't be like that darling. Come on!"
                pc "Noo. I don't wanna."
                man "Ugh, whatever you drunk bitch."
                if numgen():
                    $ player.grope_end()
                    "The guy let's go of me and walks away."
                    jump travel
                else:
                    $ player.grope()
                    pc "Hey!"
                    $ travel_isolate(trans=hpunch)
                    man "Come on. We could av done this nice."
                    jump random_event_generic_sex_force_bendover

label random_event_generic_drunkblackout_7:
    pcm "Fuck, I drank too much..."
    $ travel_toilet_girls()
    "I splash some water on my face and take a bit of a breather."
    pc "Phew."
    jump travel

label random_event_generic_drunkblackout_8:
    $ player.face_puke()
    pc "*Ubbb*"
    pcm "Nonono..."
    $ player.face_conf()
    pc "*Phew*"
    jump travel


label random_event_generic_drinking_with_men:
    pc "Sure, let's go have a drink."
    man "I know just the place."
    $ travel_hangout_location()
    man "Here ya go."
    $ player.left_hand = "beer_bottle"
    pc "Thanks."
    call random_event_generic_drinking_with_men_cycle from _call_random_event_generic_drinking_with_men_cycle
    call random_event_generic_drinking_with_men_cycle from _call_random_event_generic_drinking_with_men_cycle_1
    call random_event_generic_drinking_with_men_cycle from _call_random_event_generic_drinking_with_men_cycle_2
    $ player.hands_reset()
    if player.check_horny(very_extreme=True):
        pc "So, which one of you perverts are gonna bend me over?"
        man "Wow. Okay. I won't say no to that."
        jump random_event_generic_drinking_with_men_sex_start
    elif player.check_horny(extreme=True):
        pc "Hmm, bunch of guys like you with me? Maybe we can do something?"
        man "Sounds good to me, you boys up for it?"
        guy "Damn right!"
        jump random_event_generic_drinking_with_men_sex_start
    elif numgen(0,5):
        $ player.grope()
        man "So darling, how about we have a little fun now we got to know each other?"
        if player.check_sex_agree_choice(3, "That could be fun", "Sorry, no thanks"):
            pc "You dirty boys."
            $ player.grope_end()
            jump random_event_generic_drinking_with_men_sex_start
    $ player.grope_end()
    pc "Thanks for the fun guys. I'm gonna call it a night."
    if pc_lost_clothes():
        "I look around for my clothes and start to get dressed."
        $ pc_dress_slow()
    man "Okay, see ya round darling."
    $ walk(loc_from)
    pc "Whew. That was nice."
    jump travel

label random_event_generic_drinking_with_men_sex_start:
    $ player.sex_holes = []
    $ player.sex_man_amount = numgen(3,6)
    $ npc_race_picker()
    $ tempname = streetpervert
    $ tempname2 = streetguy
    $ tempname3 = streetman
    $ quest_temp = None
    $ event_end_interrupt_label = "random_event_generic_drinking_with_men_sex_end"
    jump whore_street_sex_group_start_picker

label random_event_generic_drinking_with_men_sex_end:
    man "Damn love, that was amazing. Never thought a girl like you would drink with us like that."
    guy "And let us fuck her silly."
    $ renpy.scene()
    with dissolve
    pc "Yeah yeah."
    "I look around for my clothes and start to get dressed."
    $ pc_dress_slow()
    pc "Well, it was fun boys. But I better go before I get into more trouble."
    man "Okay, see ya round darling."
    $ walk(loc_from)
    pc "Whew. That was nice."
    jump travel

label random_event_generic_drinking_with_men_cycle:
    call expression WeightedChoice([
    ("random_event_generic_drinking_with_men_cycle_1", 100),
    ("random_event_generic_drinking_with_men_cycle_2", 100),
    ("random_event_generic_drinking_with_men_cycle_3", 100),
    ("random_event_generic_drinking_with_men_cycle_4", 100),
    ("random_event_generic_drinking_with_men_cycle_5", 100),
    ("random_event_generic_drinking_with_men_cycle_6", 100),
    ("random_event_generic_drinking_with_men_cycle_7", If(player.check_drunk(5, notif=False), 50, 0)),
    ("random_event_generic_drinking_with_men_cycle_8", If(pc_lost_clothes(), 400, 0)),
    ]) from _call_expression_24
    return

label random_event_generic_drinking_with_men_cycle_1:
    $ player.left_hand = "beer_bottle"
    "They are mostly talking rubbish. But it's fun to listen to them."
    $ relax(15)
    $ player.beer(True)
    pc "Nooo. They wouldn't let me."
    man "Would have been funny if they did."
    return

label random_event_generic_drinking_with_men_cycle_2:
    $ player.left_hand = "beer_bottle"
    "I chat away with the guys while we all share drinks and stories."
    $ relax(15)
    $ player.beer(True)
    guy "So I told him he can for four times the price."
    man "Haha. Did he agree?"
    return

label random_event_generic_drinking_with_men_cycle_3:
    $ player.left_hand = "beer_bottle"
    "The guys are chatting away about some silly stuff that happened to them before."
    $ relax(15)
    $ player.beer(True)
    guy "And the guard was standing right there when I turned the corner."
    pc "Wow. What did he do."
    guy "I just said hello to him and carried on walking. He didn't realise I was the guy since I didn't run away."
    return

label random_event_generic_drinking_with_men_cycle_4:
    $ player.left_hand = "beer_bottle"
    "I sip at my beer and listen to their stories."
    $ relax(15)
    $ player.beer(True)
    guy "With no idea what to do."
    man "I bet What is there to do?"
    return

label random_event_generic_drinking_with_men_cycle_5:
    $ player.left_hand = "beer_bottle"
    "I drink some beer and entertain the guys a bit."
    $ relax(15)
    $ player.beer(True)
    pc "[rlist.singing_dialogue_1]"
    pc "[rlist.singing_dialogue_2]"
    return

label random_event_generic_drinking_with_men_cycle_6:
    $ player.left_hand = "beer_bottle"
    "I drink some beer while the guys are getting a bit handsy."
    $ relax(15)
    $ player.beer(True)
    $ player.grope(strip=True)
    pc "Focus on your beer you perverts."
    $ player.grope(strip=True)
    pc "Haa!"
    $ player.grope_end()
    return

label random_event_generic_drinking_with_men_cycle_7:
    $ player.left_hand = "beer_bottle"
    "I drink some beer but struggle to focus on what is going on."
    $ relax(15)
    $ player.beer(True)
    show screen blackout(50) with dissolve
    pc "Spinning..."
    $ player.face_sleep()
    show screen blackout() with dissolve
    jump random_event_generic_wakedrunk

label random_event_generic_drinking_with_men_cycle_8:
    $ player.left_hand = "beer_bottle"
    "The guys are teasing me about my missing clothes while I try to get them back."
    $ relax(15)
    $ player.beer(True)
    pc "Idiots' give it back."
    man "You are much nicer like this."
    $ pc_dress()
    return


label random_event_generic_wakedrunk:
    $ player.hands_reset()

    if not danger_weight():
        jump random_event_generic_wakedrunk_1

    jump expression WeightedChoice([
    ("random_event_generic_wakedrunk_1", 100),
    ("random_event_generic_wakedrunk_2", 50),
    ("random_event_generic_wakedrunk_3", 50),
    ("random_event_generic_wakedrunk_4", 50),
    ("random_event_generic_wakedrunk_5", 30),
    ])

label random_event_generic_wakedrunk_1:
    $ travel_isolate(trans=False)
    $ player.face_sleep()
    pause 1
    show screen blackout(50) with dissolve
    pc "Uuuugggggg..."
    hide screen blackout 
    $ player.face_shock()
    with hpunch
    pc "Ahhhhh..."
    pcm "Where the fuck am I?"
    $ player.face_worried()
    pcm "Ah, yeah... I remember."
    pcm "Too much to drink."
    jump travel

label random_event_generic_wakedrunk_2:
    $ travel_isolate(trans=False)
    $ randomnum = renpy.random.randint(1,5)
    $ npc_race = randomnum
    $ temp_var_1 = player.vvirgin
    $ player.sex_forced(rapist)
    $ player.sex_vag(rapist)
    $ pc_strip()
    show sb_assup closed frown worried sex
    $ player.eye = 3
    pause 1
    show screen blackout(50) with dissolve
    pc "Uuuugggggg..."
    show sb_assup squint sex with dissolve
    pc "Whhhhhhhaaaaaa..."
    rapist.fname "Ahhhh..."
    $ player.sex_cum(rapist, "inside")
    $ player.eye = 3
    rapist.fname "Ahhhaaaahhh........"
    show sb_assup closed sex with dissolve
    $ player.eye = 3
    pc "Oooowhaaaaaa..."
    show screen blackout(100) with dissolve
    $ time_sleep_rough()
    hide sb_assup
    pause 3
    hide screen blackout 
    $ player.face_shock()
    with hpunch
    pc "Ahhhhh..."
    pc "Fuck, Ahhhh! What the hell. My body is so fucking sore..."
    pc "Did...?"
    $ player.eye = 3
    pc "Ah fuck..."
    $ player.face_cry()
    if temp_var_1 == True:
        pc "Did I really lose my virginity to some shit while passed out?"
    pc "And where the fuck are my clothes...?"
    pc "*SOB* *SOB*"
    $ player.face_normal
    jump travel

label random_event_generic_wakedrunk_3:
    $ travel_dump_location()
    $ pc_strip()
    $ temp_var_1 = player.vvirgin
    $ player.sex_forced(rapist)
    $ player.sex_vag(rapist)
    $ player.sex_cum(rapist, "inside")
    $ player.sex_hideaction()
    $ player.face_sleep()
    show screen blackout(50) with dissolve
    pc "Uuuugggggg..."
    hide screen blackout 
    $ player.face_shock()
    with hpunch
    pc "Ahhhhh..."
    pcm "Where the fuck am I?"
    $ player.face_worried()
    pcm "Why am I naked?"
    pcm "Ah fuck. Did I really get..."
    $ player.face_cry()
    if temp_var_1 == True:
        pc "Did I really lose my virginity to some shit while passed out?"
    pc "*SOB*"
    jump travel

label random_event_generic_wakedrunk_4:
    jump sleep_rough_wake_vrare_1

label random_event_generic_wakedrunk_5:
    jump sleep_rough_wake_vrare_2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
