label haven_bed_sleep:
    if player.tired >= 80:
        pcm "I am not tired and I shouldn't push my luck by closing my eyes around here."
        jump travel
    elif player.tired <= 20:
        show haven_sleep at right2 with dissolve
        $ player.face_sleep()
        pcm "Ugh, I am exhausted. Bu I... Shouldn't fall as... Asleep..."
        show screen blackout(100) with dissolve
        pause 1
        $ time_sleep(60)
        $ haven_bed_join_chance()
        $ time_sleep(120)
        $ haven_bed_join_chance()
        $ time_sleep(60)
        $ haven_bed_join_chance()
        hide screen blackout with dissolve
        hide haven_sleep with dissolve
        $ player.face_worried()
        pcm "Shit, I fell completely asleep..."
        pcm "I should avoid doing that in this shithole place. Small naps where I can try and keep an eye on things."
        jump travel
    else:
        show haven_sleep at right2 with dissolve
        $ player.face_sleep()
        "I lay down in my clothes and try to take a little nap."
        show screen blackout(100) with dissolve
        pause 1
        $ time_sleep(120)
        $ haven_bed_join_chance()
        hide screen blackout with dissolve
        hide haven_sleep with dissolve
        $ player.face_normal()
        jump travel

label haven_tired_trigger:
    $ show_notif_popup("Too tired to stay awake")
    $ player.face_worried()
    if not loc_cur == loc_haven_bed:
        pcm "I am falling asleep on my feet... Better go to my bunk..."
    else:
        pcm "I am ready to pass out. Think I will have a lay down..."
        jump haven_bed_sleep
    if loc_cur in [loc_haven_shower_stall, loc_haven_utilities]:
        call haven_shower_dress_call from _call_haven_shower_dress_call_1

    if not loc_cur == loc_haven_bedroom:
        $ walk(loc_haven_bedroom)
        pcm "Almost..."
    $ walk(loc_haven_bed)
    pause 0.2
    jump haven_bed_sleep

label haven_bed_sleep_join:

    if not "join_1" in loc_haven_bed.list:
        $ add_to_list(loc_haven_bed.list, "join_1")
        jump haven_bed_sleep_join_cumchest
    elif not "join_2" in loc_haven_bed.list:
        $ add_to_list(loc_haven_bed.list, "join_2")
        jump haven_bed_sleep_join_cumface
    elif not "join_3" in loc_haven_bed.list:
        $ add_to_list(loc_haven_bed.list, "join_3")
        jump haven_bed_sleep_join_sleep
    else:
        jump haven_bed_sleep_join_cycle

label haven_bed_sleep_join_cycle:
    $ rand_choice = WeightedChoice([
    ("haven_bed_sleep_join_sleep", 10),
    ("haven_bed_sleep_join_cumchest", 10),
    ("haven_bed_sleep_join_cumass", 10),
    ("haven_bed_sleep_join_cumface", 10),
    ("haven_bed_sleep_join_cummouth", 10),
    ("haven_bed_sleep_join_milk", If(not writing.chest, 10, 0)),
    ("haven_bed_sleep_join_slut", If(not writing.face, 10, 0)),
    ("haven_bed_sleep_join_whore", If(not writing.forehead, 10, 0)),
    ("haven_bed_sleep_join_force", 5),
    ("haven_bed_sleep_join_blackout", If (player.drunk > 100, 3,0)),
    ("haven_bed_sleep_join_paid", If (player.drunk > 70 and (player.iswhore or player.isslut), 15,0)),
    ])
    jump expression rand_choice

label haven_bed_sleep_join_sleep:
    show haven_sleep clothed
    hide screen blackout with dissolve
    show haven_sleep conf with dissolve
    $ player.face_worried()
    pc "..."
    pc "Huh?"
    if player.tired < 40 and (player.iswhore or player.isslut):
        pcm "Ugh, whatever..."
        $ player.face_sleep()
        show haven_sleep sleep with dissolve
        "I just close my eyes and try and get back to sleep."
        show screen blackout(100) with dissolve
        $ time_sleep(60)
        pause 1
        jump haven_bed_sleep_join_cycle
    hide haven_sleep with hpunch
    $ walk(loc_haven_bedroom)
    $ player.face_worried()
    pcm "These idiots need to find their own place to sleep."
    jump travel

label haven_bed_sleep_join_cummouth:
    $ player.sex_cum(nosex, "mouth")
    hide screen cum_action
    hide screen blackout with dissolve
    $ player.face_worried()
    pc "..."
    hide haven_sleep with dissolve
    $ player.mouth = 10
    pc "*Sigh*"
    if not player.isslut or player.iswhore:
        $ player.face_bleh()
    pcm "Be happy when I can get out of here and get some sleep without someone putting their dick in my mouth."
    if not player.isslut or player.iswhore:
        $ player.face_puke()
    pcm "Oh well..."
    $ player.face_normal()
    jump travel

label haven_bed_sleep_join_cumface:
    $ player.sex_cum(nosex, "face")
    hide screen cum_action
    hide screen blackout with dissolve
    $ player.face_worried()
    pc "..."
    hide haven_sleep with dissolve
    $ player.mouth = 10
    pc "Shit, this stuff stings when it gets in your eye..."
    if not player.isslut or player.iswhore:
        $ player.face_puke2()
    pcm "..."
    if not player.isslut or player.iswhore:
        $ player.face_puke()
    pcm "Gonna have to start sleeping with something sharp. Bet stabbing them in the balls will make them stop messing with me."
    if player.isslut or player.iswhore:
        "I use my top to wipe my face of what is left on my face."
        $ player.cum_clean_outside()
    else:
        pcm "Better go wash my face I suppose..."
        $ player.add_mood(-30)
    $ player.face_normal()
    jump travel

label haven_bed_sleep_join_cumchest:
    $ randomnum = renpy.random.randint(0, 1)
    if randomnum == 1:
        $ player.sex_cum(nosex, "belly")
    else:
        $ player.sex_cum(nosex, "chest")
    hide screen cum_action
    hide screen blackout with dissolve
    $ player.face_normal()
    $ player.face_worried()
    $ player.eye = 6
    hide haven_sleep with dissolve
    pc "Err..."
    $ player.eye = 3
    pc "*Sigh*. This is becoming too much. Can't even sleep in this place without people using me as their porn."
    $ player.eye = 1
    if player.isslut or player.iswhore:
        "I rub what was left on me into my skin and wipe my hands off on my shorts."
        $ player.cum_clean_outside()
    else:
        pcm "Better head to the showers."
    if player.isslut:
        $ player.add_conf(2)
        $ player.add_mood(3)
    else:
        $ player.add_mood(-15)
    jump travel

label haven_bed_sleep_join_cumass:
    $ randomnum = renpy.random.randint(0, 1)
    if randomnum == 1:
        $ player.sex_cum(nosex, "ass")
    else:
        $ player.sex_cum(nosex, "pullout")
    $ c.pants = 0
    $ c.bottom = 0
    show haven_sleep
    hide screen cum_action
    hide screen blackout with dissolve
    $ player.face_worried()
    show haven_sleep conf with dissolve
    pc "What the...?"
    pc "Bastards..."
    hide haven_sleep with dissolve
    $ pc_dress()
    if not player.isslut or player.iswhore:
        pcm "Better head to the showers."
    if player.isslut:
        $ player.add_conf(2)
        $ player.add_mood(3)
    else:
        $ player.add_mood(-15)
    jump travel

label haven_bed_sleep_join_force:
    show haven_sleep penisout
    hide screen blackout with dissolve
    pcm "Zzzzzz."
    pcm "..."
    show haven_sleep conf with dissolve
    pcm "The fuck!"
    pcm "Is he poking me with what I think he is?"
    pcm "..."
    pcm "He doesn't know I am awake yet, I should get out of here quickly before he can react."
    if player.iswhore:
        pc "Hey idiot. Pay first or fuck off!"
        hav "Not paying a cunt like you."
        show haven_sleep pain
        $ player.punch()

        pc "Nnng!"
    elif player.check_nowill():
        pcm "But... What if it just makes things worse?"
        show haven_sleep sleep with dissolve
        pcm "*SOB*"
        pcm "..."
        $ c.bottom = 0
        $ c.pants = 0
        with dissolve
        pcm "Fuck..."
        if player.vvirgin == True:
            pcm "If I let him continue, he is going to end up taking my virginity..."
        else:
            pcm "If I let him continue he will fuck me."
        pcm "..."
        if player.check_nowill():
            pcm "Shit shit shit..."
            pcm "*SOB*"
            pcm "I can't make myself move."
            pcm "I am such a coward."
            $ player.sex_forced(havenpsleeper)
            $ player.sex_vag(havenpsleeper)
            show haven_sleep penisin with hpunch
            show haven_sleep pain with dissolve
            if player.virgin_pregcheck == True:
                pcm "Noooooo..."
                pcm "My first time wasn't supposed to be like this."
                pcm "*SOB*"
            pcm "FUCK FUCK!!!"
            pcm "*SOB*"
            pcm "Why am I letting this fucker have his way with me?"

            pcm "*SOB*"
            "He gently fucks me as I pretend to sleep and luckily for me he is not being too aggressive so as to not wake me up."
            pcm "*SOB*"
            pcm "Hurry up..."
            $ player.sex_cum(havenpsleeper, "inside")
            show haven_sleep with hpunch
            hav "Mmmmmmmmmmmm"
            pcm "*SOB*"
            pcm "..."
            show haven_sleep with dissolve
            pcm "..."
            show haven_sleep conf with dissolve
            pcm "*SOB*"
            pcm "Why didn't I stand up for myself?"
            pcm "..."
            show haven_sleep sleep with dissolve
            $ player.eye = 3
            "I lay down sobbing quietly to myself and eventually fall asleep."
            show screen blackout(100) with dissolve
            pause 1
            show haven_sleep noman
            $ time_sleep(60)
            hide screen blackout with dissolve
            show haven_sleep conf
            pcm "..."
            pcm "Wasn't just a dream..."
            $ pc_dress()
            pcm "*SOB*"
            hide haven_sleep with dissolve
            jump travel


    "I push against him and try to make a run for it."
    if player.check_fight(5):
        hide haven_sleep with hpunch
        $ walk(loc_haven_bedroom)
        $ player.face_worried()
        pcm "What the fuck? That cunt was taking things too far..."
        $ player.face_cry()
        $ player.add_mood(-40)
        pcm "*SOB*"
        jump travel


    show haven_sleep pain with hpunch
    hav "Stay still you bitch!"
    show haven_sleep gag with hpunch
    pc "Mmmmffff."
    hav "And keep quiet!"
    $ c.bottom = 0
    $ c.pants = 0
    with vpunch
    pc "Mmmmmffffff!"
    $ player.sex_forced(havenpsleeperforce)
    $ player.sex_vag(havenpsleeperforce)
    show haven_sleep penisin with hpunch
    pc "Aaammmmmmmmfffff!!!"
    hav "Ah yes!"
    pc "Mmmffff."
    show haven_sleep with hpunch
    hav "Shut up bitch."
    pc "..."
    hav "Good, this will be quick."
    show haven_sleep with hpunch
    pc "*SOB*"
    hav "Mmmmmmm."
    $ player.sex_cum(havenpsleeperforce, "inside")
    show haven_sleep with hpunch
    hav "Mmmmmmmmmmmm"
    pcm "*SOB*"
    pcm "..."
    show haven_sleep noman headdown pain with dissolve
    pcm "..."
    pcm "*SOB*"
    pcm "..."
    show haven_sleep sleep with dissolve
    $ player.eye = 3
    "I lay down sobbing quietly to myself and eventually fall asleep."
    show screen blackout(100) with dissolve
    pause 1
    show haven_sleep noman
    $ time_sleep(60)
    hide screen blackout with dissolve
    show haven_sleep conf
    pcm "..."
    pcm "Wasn't just a dream..."
    $ pc_dress()
    pcm "*SOB*"
    hide haven_sleep with dissolve
    jump travel

label haven_bed_sleep_join_blackout:
    $ time_sleep(120)
    $ c.bottom = 0
    $ c.pants = 0
    $ c.top = 0
    show haven_spitroast at right
    show screen blackout(75) with dissolve
    pause 0.2
    show screen blackout(100) with dissolve
    hide haven_spitroast
    show haven_gangbang blow manblow at right
    show screen blackout(75) with dissolve
    pause 0.2
    show screen blackout(100) with dissolve
    hide haven_gangbang
    $ writing.add_writing("ass", "perm")
    $ haven_sleep_sex_loop()
    $ pc_dress_upper()
    $ player.add_mood(-40)
    pause 0.5
    hide screen blackout with dissolve
    show haven_sleep conf with dissolve
    pc "Uggghhhh..."
    pcm "..."
    show haven_sleep pain with dissolve
    pcm "What the hell did I get up to?"
    pcm "Feels like I have been fucked by a train."
    pcm "..."
    show haven_sleep conf with dissolve
    pcm "Getting drunk here is too dangerous..."
    hide haven_sleep with dissolve
    $ pc_dress()
    if player.drunk > 50:
        $ player.face_puke()
        pcm "Better take a shower. Hope I don't pass out on the way..."
    else:
        pcm "Better take a shower. These bastards made me all dirty..."
    $ walk(loc_haven_bedroom)
    pc "Hope I don't end up attracting attention to myself looking like this."
    if haven_time_safe():
        show kitty at right1
        kitty.name "Have fun last night?"
        pc "Huh?"
        kitty.name "Sounded like you had half the guys in this place in your little bunk."
        pc "Err... I was a bit..."
        kitty.name "Drunk? Yeah could have guessed."
        if player.has_perk(perk_preg_want):
            kitty.name "No sober person would demand they take turns in trying to knock you up."
            pc "What? I..."
            pc "Did I?"
            kitty.name "Hope you get your wish."
            hide kitty with dissolve
            pcm "..."
            pcm "Damn."
            pcm "Did I just get wasted and ask everyone to try and put a baby in me?"
            pcm "..."
            $ player.add_mood(20)
            $ player.face_normal()
            pcm "Oh well, that's one way of getting what I want I suppose. Even if it does feel like half the guys in the place fucked me."
        else:

            kitty.name "No sober person would act the way you were."
            pc "What? I..."
            pc "Then why did you let them carry on if you knew I was plastered?"
            kitty.name "Not my business love. You look after you and I'll look after me."
            hide kitty with dissolve
            pcm "..."
            pcm "Damn."
    $ walk(loc_haven_hallway_1f)
    pause 0.5
    $ walk(loc_haven_shower)
    pcm "This place is as lovely as always..."
    jump haven_shower_stall_arrival

label haven_bed_sleep_join_paid:
    $ time_sleep(120)
    $ c.bottom = 0
    $ c.pants = 0
    $ c.top = 0
    $ player.sex_forced(havenman, main_quest_05)
    $ player.sex_vag(havenman, main_quest_05)
    if numgen(0,1):
        $ player.sex_cum(havenman, "pullout", main_quest_05)
    else:
        $ player.sex_cum(havenman, "inside", main_quest_05)
    show haven_sleep
    hide screen cum_action
    hide screen blackout with dissolve
    $ player.face_worried()
    show haven_sleep conf with dissolve
    pcm "What the...?"
    pcm "You have got to be kidding me."
    hide haven_sleep with dissolve
    $ pc_dress()
    $ haven_whore_pay()
    pcm "The arsehole couldn't wait...?"
    jump travel

label haven_bed_sleep_join_milk:
    $ c.top = 0
    $ writing.add_writing("chest", "perm")
    hide screen blackout with dissolve
    $ player.face_worried()
    pc "..."
    hide haven_sleep with dissolve
    $ player.face_meek()
    pc "What the fuck?"
    $ pc_dress()
    pcm "Arseholes!"
    $ player.face_normal()
    jump travel

label haven_bed_sleep_join_slut:
    $ writing.add_writing("face", "perm")
    hide screen blackout with dissolve
    hide haven_sleep with dissolve
    $ player.face_normal()
    jump travel

label haven_bed_sleep_join_whore:
    $ writing.add_writing("forehead", "perm")
    hide screen blackout with dissolve
    hide haven_sleep with dissolve
    $ player.face_normal()
    jump travel

label haven_bed_listen_chainstart:
    jump haven_bed_listen_chain

label haven_bed_listen:

    if haven_intel_chance():
        jump expression renpy.random.choice(["haven_intel_7", "haven_intel_8"])
    else:
        jump haven_bed_listen_genericinfo

label haven_bed_listen_chain:
    show haven_sleep peek at right2 with dissolve
    "I lay down on my bedroll and try to look inconspicuous while eavesdropping on the girls' conversations."

    call haven_bed_listen_start from _call_haven_bed_listen_start
    call haven_bed_listen from _call_haven_bed_listen
    call haven_bed_listen_cont from _call_haven_bed_listen_cont
    call haven_bed_listen from _call_haven_bed_listen_1
    jump haven_bed_listen_end

label haven_bed_listen_start:
    $ dialouge = WeightedChoice([
    ("Let's see if I can overhear the girls talking about anything interesting.", 1),
    ("Hopefully I can hear the girls talk about something that can help me find this Doctor.", 1)
    ])
    pcm "[dialouge]"
    return

label haven_bed_listen_cont:
    $ dialouge = WeightedChoice([
    ("So much talking but so little worth listening to.", 1),
    ("Mmm, ok. Anything else?", 1)
    ])
    pcm "[dialouge]"
    return

label haven_bed_listen_genericinfo:
    $ dialouge = WeightedChoice([
    ("...always wants to do me in the bum. End up not being able to sit down after...", 1),
    ("...and tried to run away while I was putting my pants back on. Kicked him right in the balls and took all his money while he was keeled over. He wasn't expecting the pointed toes on these heels.", 1),
    ("...should get used to it. If you do it there then you don't have to worry about the time of the month and just go with it.", 1),
    ("...no way. Really? I can't believe he asked you that. What are you gonna tell him?", 1),
    ("...over by the diner. Y'know the place near the truck stop. I saw them taking in those boxes...", 1),
    ("...not sure, but I don't envy them. You seen the state o' some o' them trucks come back in? Like they were attacked by savages with spears or summit.", 1),
    ("...not a chance... Well maybe not... Ahh I don't know! Maybe I should. I need some time to think about it but he is pushing me for an answer and I don't know what I want yet.", 1),
    ("...the old fella is one of the best ones. Too old to get it up so he just likes to watch. Much better to have that old perv than some o' the young ones who can go to town on...", 1)

    ])
    havgirl "[dialouge]"
    $ working(15)
    return

label haven_bed_listen_end:
    $ player.add_desire_random(5)
    $ working(20)
    $ dialouge = WeightedChoice([
    ("Ah well, I think that's enough for now.", 1),
    ("Would think a bunch of whores would have a lot more to say about doctors or medical things.", 1),
    ("I don't much envy these girls...", 1),
    ("Listening to these girls makes me dread having to live here permanently.", 1),
    ])
    pcm "[dialouge]"
    hide haven_sleep with dissolve
    jump travel

label haven_bed_whore_offer:
    show havman at right1
    if writing.forehead:
        hav "Hey whore. Available for company?"
    elif writing.face:
        hav "Hey slut. Interested in come company?"
    else:
        hav "Hey sexy. Want some company?"
    if player.check_whore():
        pcm "Hmmm..."
        if player.check_sex_agree_choice(0, "Sure I'll keep you warm", "Not right now"):
            pc "Pay first though."
            hav "No problem."

            jump haven_sex_repeatable_start
        else:
            $ NullAction()
    pc "Sorry mate. Going to have to find someone else to keep you warm."
    hav "Right."
    hide havman with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
