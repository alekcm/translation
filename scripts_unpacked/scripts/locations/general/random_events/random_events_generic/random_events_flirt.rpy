label random_event_generic_allure_flirt_start_normal:
    $ male_npc_create_all()
    $ tempname = streetguy
    $ quest_temp = None
    jump random_event_generic_allure_flirt_start

label random_event_generic_allure_flirt_start_scav:
    $ male_npc_create_all(scav=True)
    $ tempname = scavver
    $ quest_temp = None

label random_event_generic_allure_flirt_start:
    show male_generic at right5 with dissolve
    tempname.name "Hey sweetheart, how about we get to know each other?"
    if player.check_nowill(notif=False):
        pc "Err, ummm..."
        tempname.name "Don't worry sweetheart, I don't bite."
        $ player.face_worried()
        pc "Okay..."
        "I stand there listening to the guy talking, not really saying much myself."
        $ relax(5)
        "He generally does all the talking."
        $ travel_isolate()
        call random_event_generic_give_something_picker from _call_random_event_generic_give_something_picker
        "He continues chatting away and I don't really say a lot. I just stand there listening and smiling when he expects it."
        $ player.drink_finish()
        if not numgen(0,10):
            tempname.name "Well, was nice chatting lovely, but I better be heading off."
            pc "Err, okay... Thanks for the chat."
            hide male_generic with dissolve
            pcm "Okay..."
            jump travel
        tempname.name "So what do you say, shall we have a little fun?"
        pc "Errm..."
        if player.check_sex_agree_choice(diff=5, option1="Sounds like fun", option2="No, I should be going"):

            jump whore_street_sex_start_picker
        else:
            pc "Sorry mate, you are on your own."
            jump random_event_generic_allure_flirt_reject
    if player.check_sex_agree_choice(diff=4, option1="Okay, sure", option2="No thanks", notif=False):
        pc "Sure, why not?"
        tempname.name "Couldn't resist coming up and talking after seeing you."
        pc "Oh? Flatterer."
        call random_event_generic_give_something_picker from _call_random_event_generic_give_something_picker_1
        jump random_event_generic_allure_flirt_quality_picker
    else:
        pc "Sorry mate, you are on your own."
        jump random_event_generic_allure_flirt_reject

label random_event_generic_allure_flirt_quality_picker:

    jump expression WeightedChoice([
    ("random_event_generic_allure_flirt_quality_funny", 100),
    ("random_event_generic_allure_flirt_quality_smooth", 100),
    ("random_event_generic_allure_flirt_quality_nice", 100),
    ("random_event_generic_allure_flirt_quality_normal", 100),
    ("random_event_generic_allure_flirt_quality_boring", 100),
    ("random_event_generic_allure_flirt_quality_scum", 100),
    ])




label random_event_generic_allure_flirt_quality_funny:
    "We stand around chatting a bit and he makes a lot of jokes that make me laugh."
    $ relax(5)
    $ player.face_happy()
    "I find talking to him is quite entertaining and his silly jokes put a smile on my face."
    $ player.add_mood(10)
    call random_event_generic_give_something_picker from _call_random_event_generic_give_something_picker_2
    tempname.name "...wasn't worth that many camels!"
    pc "Haha, I can believe it as well."
    tempname.name "Right."
    $ travel_isolate()
    call random_event_generic_give_something_picker from _call_random_event_generic_give_something_picker_3
    $ relax(5)
    "We continue chatting away and he tells me some silly stories that almost seem to crazy to be true."
    $ player.add_mood(10)
    "But I don't care, they are funny regardless."
    pc "...don't believe that happened for a second!"
    tempname.name "Yeah I wouldn't either."
    jump random_event_generic_allure_flirt_close

label random_event_generic_allure_flirt_quality_smooth:
    "We stand around chatting a bit and his complements keep flowing."
    $ relax(5)
    $ player.face_happy()
    "It's clear he is a smooth talker and fairly practised at this, but I don't mind as it's entertaining."
    $ player.add_mood(10)
    call random_event_generic_give_something_picker from _call_random_event_generic_give_something_picker_4
    tempname.name "...eyes, I could get lost just looking in them."
    pc "Oh, and what else?"
    tempname.name "Fishing for complements? Well don't worry, I am happy to shower someone as beautiful as you in them."
    $ travel_isolate()
    call random_event_generic_give_something_picker from _call_random_event_generic_give_something_picker_5
    $ relax(5)
    "We continue chatting away, well, I listen to him trying to sweet talk me the entire time."
    $ player.add_desire(20)
    "And it's working, I enjoy hearing his smooth words. It's a welcome change to the usual brute you meet around here."
    pc "...think so?"
    tempname.name "Absolutely, I could imagine that face on the cover of all of them."
    jump random_event_generic_allure_flirt_close

label random_event_generic_allure_flirt_quality_nice:
    "We stand around chatting a bit, he seems a normal decent guy."
    $ relax(5)
    $ player.face_happy()
    "We chat away and it's generally enjoyable having a conversation with him. For once someone doesn't make dirty comments about me."
    $ player.add_mood(10)
    call random_event_generic_give_something_picker from _call_random_event_generic_give_something_picker_6
    tempname.name "...you would think so, but no, I didn't end up happening that way."
    pc "No, so what happened?"
    tempname.name "Well, remember the..."
    $ travel_isolate()
    call random_event_generic_give_something_picker from _call_random_event_generic_give_something_picker_7
    $ relax(5)
    "We continue chatting away and sharing stories and some small talk."
    $ player.add_mood(10)
    "It's a nice distraction to chat to someone new, even though I probably wont see him again. It's entertaining none the less."
    pc "...so then I thought to myself why not?"
    tempname.name "That's right, why not? Nothing stopping you."
    jump random_event_generic_allure_flirt_close

label random_event_generic_allure_flirt_quality_normal:
    "We stand around chatting and he seems fairly normal. Well, normal for this place so he is pretty rough around the edges."
    $ relax(5)
    "We chat away and he shares some of his life with me. Living in a shithole an if he isn't working then he is drinking."
    call random_event_generic_give_something_picker from _call_random_event_generic_give_something_picker_8
    tempname.name "...and kinda makes you wonder, what is even the point?"
    pc "Same as it always was, just get by."
    tempname.name "Yeah I guess..."
    $ travel_isolate()
    call random_event_generic_give_something_picker from _call_random_event_generic_give_something_picker_9
    $ relax(5)
    "We continue chatting away and I start to wonder if I should make excuses to be on my way."
    pc "Err, so was nice chatting, but I think it's time I headed off."
    tempname.name "Yeah, or we could turn this up a bit. Do something nice."
    jump random_event_generic_allure_flirt_close

label random_event_generic_allure_flirt_quality_boring:
    "We stand around chatting a bit, but conversation quickly goes to his life and he kinda drones on."
    $ relax(5)
    $ player.face_worried()
    "He doesn't really talk in a way that expects a reply and kind of just talks at me like I am a wall."
    pc "Errm, so I think I had better be going."
    tempname.name "Ah why so fast darling, maybe we could do something more entertaining?"
    jump random_event_generic_allure_flirt_close

label random_event_generic_allure_flirt_quality_scum:
    "We stand around chatting a bit, but it quickly becomes apparent that he is a very dislikable guy"
    $ relax(5)
    $ player.face_worried()
    "He talks in a way as if he has never considered me, or anyone he has spoken to, as a person."
    pc "Errm, yeah, I think I'm gonna head off."
    tempname.name "Already? Let's have some fun before you go."
    pc "No thanks, see ya."
    jump random_event_generic_allure_flirt_reject

label random_event_generic_allure_flirt_close:
    $ player.drink_finish()
    if not numgen(0,10):
        tempname.name "Well, was nice chatting lovely, but I better be heading off."
        pc "Err, okay... Thanks for the chat."
        hide male_generic with dissolve
        pcm "Okay..."
        jump travel
    tempname.name "So what do you say, shall we have a little fun?"
    pc "Errm..."
    if player.check_sex_agree_choice(diff=4, option1="Sounds like fun", option2="No, I should be going"):

        jump whore_street_sex_start_picker
    pc "Sorry mate, you are on your own."
    jump random_event_generic_allure_flirt_reject




label random_event_generic_allure_flirt_reject:
    $ player.drink_finish()
    if not numgen(0,10):
        tempname.name "Aww c'mon darling,don't be like that."
        tempname.name "Lets chat."
        hide male_generic with dissolve
        "I walk away from the guy, not really listening to his protests."
        if weightgen(danger_weight(), 3000):
            jump random_event_generic_danger
    else:

        tempname.name "Okay love."
        tempname.name "See ya around."
        pc "Sure, you too."
        hide male_generic with dissolve
        "Me and the guy walk our separate ways."
    jump travel

label random_event_generic_allure_flirt_motel_sleep_loop:
    if loc_cur.man_amount and not numgen(0,4):
        $ player.sex_blackout(tempname, quest_temp, 1)
        if numgen(0,4):
            $ loc_cur.man_amount -= 1
    jump bed_sleep_loop

label random_event_generic_allure_flirt_motel_sleep_wake:
    $ player.face_sleep()
    $ player.inhib_sleep()

    if numgen():
        $ player.sex_vag(tempname, quest_temp)
        $ player.sex_hideaction()
        show sb_onback hump worried
        $ player.face_shock()
        hide screen blackout with hpunch
        $ player.face_angry()
        $ player.eye = 2
        show sb_onback look_right with dissolve
        show sb_onback look_up with dissolve
        "I look around wondering where I am, and realise I am at the motel."
        if player.check_sex_agree():
            show sb_onback pout
            pc "Could have at least waited until I woke up."
            show sb_onback ooh
            if loc_cur.man_amount > 1:
                $ player.sex_man_amount = loc_cur.man_amount
                $ add_to_list(player.sex_holes, "vag")
                $ event_end_interrupt_label = "random_event_generic_allure_flirt_motel_sleep_wake_sex_end_group"
                jump whore_street_sex_group_onback_vag_cont_sexonly
            else:
                $ event_end_interrupt_label = "random_event_generic_allure_flirt_motel_sleep_wake_sex_end"
                jump whore_bed_sex_onback_vag_normal_inturrupt
        else:
            pc "What do you think you are doing?"
            tempname.name "Ah so nice."
            "I wiggle under him to try and get him off of me, he doesn't seem to want to stop but doesn't hold me or anything."
            if not numgen(0,30) and not npc_any_here():
                jump whore_bed_sex_onback_forcesex
            "Eventually I manage to squeeze away from under him."
            $ renpy.scene()
            with dissolve
            pc "Shoo you pervert. Fucking me while I was asleep."
            tempname.name "You didn't seem to mind last night."
            pc "Last night I wasn't asleep."
            $ pc_dress_slow()
            $ walk(loc_motel)
            pcm "Fucking hell..."
            jump travel
    else:
        $ player.face_sleep()
        if renpy.get_screen("blackout"):
            hide screen blackout with dissolve
        $ player.face_normal()
        if player.drunk or player.high:
            $ player.inhib_sleep()

        show male_generic nude at right5 with dissolve
        tempname.name "Morning sleeping beauty."
        pc "Ugh, morning."
        if numgen(0,3):
            tempname.name "How about some more fun?"
            if player.check_sex_agree_choice(diff=2,option1="Sounds like fun" ,option2="I gotta go"):
                if loc_cur.man_amount > 1:
                    $ player.sex_man_amount = loc_cur.man_amount
                    $ event_end_interrupt_label = "random_event_generic_allure_flirt_motel_sleep_wake_sex_end_group"
                    jump whore_street_sex_group_start_picker
                else:
                    $ event_end_interrupt_label = "random_event_generic_allure_flirt_motel_sleep_wake_sex_end"
                    jump whore_street_sex_start_picker
            else:

                pc "Sorry mate, I should get going."
                $ pc_dress_slow()
                pc "It was fun, see you around."
                $ walk(loc_motel)
                jump travel
        else:

            show male_generic dressed with dissolve
            tempname.name "See ya round darling."
            pc "Ah, you are heading off?"
            tempname.name "Yeah, got places to be. It was fun."
            pc "Yeah."
            hide male_generic with dissolve
            jump travel

label random_event_generic_allure_flirt_motel_sleep_wake_sex_end:
    $ renpy.scene()
    show male_generic at right4
    with dissolve
    $ player.face_neutral()
    tempname.name "[rlist.sex_end_compliment]"
    pc "Mmmm, something nice to wake up to."
    tempname.name "Well, thanks for a fun night, but I had better be leaving now."
    pc "Oh? Okay, see you around."
    tempname.name "You too darling."
    hide male_generic with dissolve
    jump travel

label random_event_generic_allure_flirt_motel_sleep_wake_sex_end_group:
    $ renpy.scene()
    show male_generic at right4
    show male2_generic at right3
    with dissolve
    $ player.face_neutral()
    tempname.name "[rlist.sex_end_compliment]"
    pc "Mmmm, a few men in the morning to wake me up."
    tempname.name "Well, thanks for a fun night, but I think we had better head off and let you recover."
    pc "Oh? Okay, see you around."
    tempname.name "You too darling."
    hide male_generic with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
