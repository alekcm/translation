label robin_action_bus_adventure_invite:






    show robin at right1 with dissolve
    pc "Hey, you wanna go for a bus ride somewhere?"





    show robin happy
    robin.name "Oooh? Yeah, sure we can. Let's go."
    if dis(dis_school):
        $ walk(loc_school, trans=False)
        show robin at left1 with dissolve
        $ walk(loc_busstop_school)
    elif dis(dis_home):
        $ walk(loc_stairwell, trans=False)
        show robin at left1 with dissolve
        $ walk(loc_busstop_residential)

    robin.name "Here it comes."
    hide robin with dissolve
    $ walk(loc_bus_interior, trans=False)
    show robin at right6 with dissolve
    jump robin_bus_adventure_picker






label robin_bus_goto_school_event_picker:
    $ dialouge = renpy.random.choice([
    "We squeeze on the bus and manage to find somewhere to stand.",
    "We get on the bus and look for some space to stand.",
    "We work our way through the crowd and find somewhere to stand.",
    "We make our way through the bus and find somewhere to stand."
    ])
    "[dialouge]"

    call expression WeightedChoice([
    ("robin_bus_sex_event_1", 100),
    ("robin_bus_sex_event_2", If("pc_know_want_bussex" in robin.list, 20, 0)),
    ("robin_bus_sex_event_3", If("pc_know_want_bussex" in robin.list and player.has_perk([perk_slut, perk_bimbo, perk_whore, perk_exhibitionist], notif=False), 5, 0)),
    
    ]) from _call_expression_12
    jump robin_goto_school_arrive

label robin_bus_goto_home_event_picker:
    $ dialouge = renpy.random.choice([
    "We squeeze on the bus and manage to find somewhere to stand.",
    "We get on the bus and look for some space to stand.",
    "We work our way through the crowd and find somewhere to stand.",
    "We make our way through the bus and find somewhere to stand."
    ])
    "[dialouge]"

    call expression WeightedChoice([
    ("robin_bus_sex_event_1", 100),
    ("robin_bus_sex_event_2", If("pc_know_want_bussex" in robin.list, 100, 0)),
    ("robin_bus_sex_event_3", If("pc_know_want_bussex" in robin.list and player.has_perk([perk_slut, perk_bimbo, perk_whore, perk_exhibitionist], notif=False), 50, 0)),
    ("robin_bus_sex_event_4", If("pc_know_want_bussex" in robin.list, 50, 0)),
    ]) from _call_expression_13
    jump robin_goto_home_arrive

label robin_bus_adventure_picker:
    $ dialouge = renpy.random.choice([
    "We squeeze on the bus and manage to find somewhere to stand.",
    "We get on the bus and look for some space to stand.",
    "We work our way through the crowd and find somewhere to stand.",
    "We make our way through the bus and find somewhere to stand."
    ])
    "[dialouge]"
    call expression WeightedChoice([
    ("robin_bus_sex_event_4", 100),
    ]) from _call_expression_14
    if robin_here(dis_home.locs):
        jump robin_goto_home_arrive
    elif robin_here(dis_school.locs):
        jump robin_goto_school_arrive
    else:
        "This is a crash preventer, please report as a bug. Sending you home."
        $ walk(loc_busstop_residential)
        jump travel





label robin_bus_sex_event_1:
    $ dialouge = renpy.random.choice([
    "We stand there talking and joking about random stuff.",
    "We wait for our stop while chatting and joking around about random topics.",
    "We stand there talking and laughing about whatever comes up.",
    "We chat and have a bit of a laugh about random stuff."
    ])
    "[dialouge]"
    return

label robin_bus_sex_event_2:
    pc "Packed in here as always."
    robin.name "Yeah."
    robin.name "Oh?"
    with grope_trans
    pc "Hmm... That what I think it is?"
    robin.name "Yeah."
    hide robin
    $ renpy.show(renpy.random.choice(["robin_bus_grope_behind grope", "robin_bus_grope_front"]))
    with dissolve
    if "pc_know_want_bussex" in robin.list:
        pc "Should I leave you both alone?"
        robin.name "Haha, na, our stop isn't far."
        pc "Right..."
        with grope_trans
        robin.name "Ooh!"
        pc "They definitely love you."
        robin.name "Yeah, looks like."
    else:
        pc "What's a bus ride without someone touching your arse?"
        robin.name "Yeah."
        pc "Err, not going to shove him away?"
        robin.name "Our stop isn't far."
        pc "Mhmm."
    return

label robin_bus_sex_event_3:
    robin.name "Hmm..."
    pc "What?"
    $ player.face_shock()
    with hpunch
    pc "What are... Oh?"
    robin.name "Time to watch you have some fun."
    pc "You dirty pervert."
    $ player.grope(steal=True)
    pc "Ah!"
    robin.name "Yup. Now let's see how far he goes."
    $ player.grope(steal=True)
    pc "He can probably hear you..."
    robin.name "And?"
    with hpunch
    pc "Ah, pushing me?"
    robin.name "I want to see you get fucked like a cheap whore."
    $ player.grope(steal=True)
    pc "..."
    if player.check_sex_agree_choice(3, "Right... Whatever", "Not this time"):
        jump robin_bus_sex_event_sex_robin
    else:
        pc "Hey now, c'mon. It's you that has the bus fantasy."
        "I manage to wiggle my way out between [robin.name] and the pervert."
        $ player.grope_end()
        robin.name "Oh? Only me who can be fucked on the bus?"
        pc "Yeah. You are the deviant one after all."
        robin.name "Yeah, like you are one to talk."
        return

label robin_bus_sex_event_4:
    "[robin.name] wastes no time though and ends up pressing her arse against one of the guys on the bus."
    hide robin
    show robin_bus_grope_front
    with dissolve
    pcm "Wow, okay then."
    menu:
        "Watch her":
            jump robin_bus_sex_event_watch
        "Find someone myself":
            hide robin_bus_grope_front with dissolve
            pcm "Hmm, no point in me standing here scratching my arse I suppose..."
            with hpunch
            if not numgen(0,5):
                "I pretend to stumble onto some guy, but he is not best pleased and ends up shoving me away."
                pcm "Fuck you too then..."
                pcm "Ugh..."
                pcm "Might as well just watch robin then..."
                show robin_bus_grope_front
                with dissolve
                jump robin_bus_sex_event_watch
            $ player.grope(steal=True)
            pcm "Mmm, yup..."
            $ player.grope(steal=True)
            jump robin_bus_sex_event_sex_alone







label robin_bus_sex_event_hump_alone:
    $ player.grope()
    pcm "Mmmmm..."
    "I gently fall into his rhythm and press back against him as he is rubbing his cock against me."
    $ player.grope(steal=True)
    pcm "Mmm, kinda fun."
    $ player.grope(steal=True)
    pc "Oooh."
    pcm "Shit, need to be quiet."
    $ player.grope(steal=True)
    pcm "Nnng. Not easy..."
    $ player.grope(steal=True)
    $ player.grope(steal=True)
    pcm "Oooh?"
    $ player.sex_cum(busgroper, "ass")
    pervert "Ahhhh!"
    pcm "..."
    pc "*Phew*"
    pcm "Well that was fun..."
    $ player.grope_end()
    "The guy let's go of me and I don't even look back to see who it was."
    jump robin_bus_sex_event_sex_alone_reunite



label robin_bus_sex_event_sex_alone:
    "I stumble more into the guy and press my ass against him, letting him clearly know I am up for some fun."
    $ player.grope(steal=True)
    "I wiggle some more against his groin so I can excite him some more."
    pcm "Mmm, I can feel you against me."
    pcm "Oh?"
    pcm "Taking it out are you?"
    $ player.grope_poke(steal=True)
    pcm "Upp. Yes he is."
    if not c.can_access_vag():
        pcm "Mmmm..."
        $ c.bottom = 0
        $ c.outfit = 0
        pcm "Dirty man stripping me."
        if not c.can_access_vag():
            $ c.pants = 0
    pcm "..."
    $ player.sex_vag(busgroper)
    $ player.grope_insert(steal=True)
    pc "Haaaa... ♥"
    pcm "Ahh yes, fuck me on the bus like a slut!"
    if player.has_perk(perk_exhibitionist, notif=True):
        pcm "In front of so many people. So fucking HOT!"
        pcm "Mmmmmm..."
    $ player.grope(steal=True)
    pcm "Mmmmmm. Keep going you pervert!"
    "I gently fall into his rhythm and press back against him as he is thrusting into me."
    $ player.grope(steal=True)
    "We don't have much room so we need to be somewhat discreet. Though the bus is always full of deviants so probably not the first time they have seen this."
    pc "Oooh."
    pcm "Shit, need to be quiet."
    $ player.grope(steal=True)
    pcm "Nnng. Not easy..."
    $ player.grope(steal=True)
    $ player.grope(steal=True)
    pcm "Oooh?"
    $ player.sex_cum_location_offer( 
    difficulty=3, 
    cum_want="robin_bus_sex_event_sex_alone_cum_want", 
    cum_notwant="robin_bus_sex_event_sex_alone_cum_notwant", 
    cum_pullout="robin_bus_sex_event_sex_alone_cum_pullout",
    )

label robin_bus_sex_event_sex_alone_cum_want:
    pcm "Mmmmmm..."
    $ player.grope(steal=True)
    pcm "Keep... Going... ♥"
    pervert "Nnnnnngggg..."
    $ player.sex_cum(busgroper, "inside")
    pcm "Mmmmmmm..."
    $ player.grope()
    pervert "Haaaaa..."
    $ player.grope()
    pc "*Huff*"
    pcm "Mmmmmm..."
    pcm "Well that was fun..."
    $ player.grope_end()
    "I let the guy slip out of me and pretend like nothing happened."
    jump robin_bus_sex_event_sex_alone_reunite

label robin_bus_sex_event_sex_alone_cum_notwant:
    pcm "No no. Not inside..."
    $ player.grope(steal=True)
    "I press against the guy and try to push him away hoping he gets the message."
    pervert "Nnnnnngggg..."
    $ player.sex_cum(busgroper, "inside")
    pcm "Fuuuuuck!!!"
    $ player.grope()
    pcm "Outside! Outside!"
    pervert "Haaaaa..."
    $ player.grope()
    pc "*Huff*"
    pcm "..."
    $ player.grope_end()
    "The guy slips out of me and I try to pretend like nothing happened."
    jump robin_bus_sex_event_sex_alone_reunite

label robin_bus_sex_event_sex_alone_cum_pullout:
    pcm "No no. Not inside..."
    $ player.grope(steal=True)
    "I press against the guy and try to push him away hoping he gets the message."
    pervert "Nnnnnngggg..."
    $ player.grope_poke()
    $ player.sex_cum(busgroper, "pullout")
    pcm "Mmmmmmm..."
    $ player.grope()
    pervert "Haaaaa..."
    $ player.grope()
    pc "*Huff*"
    pcm "Mmmmmm..."
    pcm "Well that was fun..."
    $ player.grope_end()
    "The guy pulls his cock from between my legs and I just pretend like nothing happened."
    jump robin_bus_sex_event_sex_alone_reunite

label robin_bus_sex_event_sex_alone_reunite:
    show robin at right6 with dissolve
    robin.name "Have fun?"
    pc "Yup."
    robin.name "Heh, slut!"
    pc "Yeah, you're one to talk."
    return



label robin_bus_sex_event_sex_robin:
    pc "You dirty slut."
    robin.name "You're the one who is going to get fucked."
    if not c.can_access_vag():
        $ c.bottom = 0
        $ c.outfit = 0
        robin.name "Oh wow!"
        if not c.can_access_vag():
            $ c.pants = 0
    $ player.grope_poke(steal=True)
    pc "Ah shit."
    robin.name "Wow, I can see it..."
    with hpunch
    pc "Ah ♥"
    $ player.sex_vag(busgroper)
    $ player.grope_insert(steal=True)
    pc "Nnng!"
    robin.name "He put it somewhere nice?"
    pc "Uhh, Yeah..."
    robin.name "Slut!"
    $ player.spank()
    pc "Oi, don't you start as well."
    robin.name "Why not? It's fun watching you get a cock in you."
    pc "You damn deviant."
    robin.name "Mmm, now the question is, where is he going to cum?"
    if player.has_perk(perk_preg_notwant):
        pc "Ah shit. Better outside!"
        pc "Don't want that kind of trouble."
        robin.name "Mmm, I wouldn't mind watching as you get in that trouble."

    if "can_lesbian" in robin.list:
        hide robin
        show robin_kiss robin_open
        with grope_trans
        "She kisses me while pressing me further against the guy, making sure I cannot escape his grasp"
        pc "Mmmff..."
        pcm "This dirty bitch really gets off on watching me have sex..."
    else:
        with grope_trans
        "[robin.name] presses herself against me, pushing me more against the guy fucking me and making sure I cannot squeeze away."
        pc "Ah you dirty bitch. You really get off to this stuff."
        robin.name "Shut up and get fucked!"
    pcm "Fuck, this has been going on for a while. He has to be close..."
    $ player.sex_cum_location_offer( 
    difficulty=3, 
    cum_want="robin_bus_sex_event_3_cum_want", 
    cum_notwant="random_event_bus_sex_cum_inside_notwant", 
    cum_pullout="random_event_bus_sex_cum_pullout",
    )

label robin_bus_sex_event_sex_robin_cum_want:
    pc "I think he is going to fill me up."
    if not player.preg_knows:
        if renpy.showing("robin_kiss"):
            hide robin_kiss
            show robin at right6
            with dissolve
        robin.name "Let me watch you get knocked up you cunt."
    $ player.grope(steal=True)
    pcm "Keep... Going... ♥"
    pervert "Nnnnnngggg..."
    $ player.sex_cum(busgroper, "inside")
    pc "Mmmmmmm..."
    $ player.grope()
    pervert "Haaaaa..."
    $ player.grope()
    pc "*Huff*"
    pc "Mmmmmm..."
    if renpy.showing("robin_kiss"):
        hide robin_kiss
        show robin at right6
        with dissolve
    "[robin.name] eases up and gives me space between me and the guy so he can slip out of me."
    $ player.grope_end()
    pc "Shit. You are such a bitch."
    robin.name "I am."
    return

label robin_bus_sex_event_sex_robin_notwant:
    "I try to pull away from the guy, but [robin.name] is pressing against me too much and I can't get the space."
    $ player.grope(steal=True)
    "I try to wiggle my bum in the hope he gets the message, but it only seems to make him happier."
    pervert "Nnnnnngggg..."
    $ player.sex_cum(busgroper, "inside")
    pcm "Fuuuuuck!!!"
    $ player.grope()
    pcm "Outside! Outside!"
    pervert "Haaaaa..."
    $ player.grope()
    if renpy.showing("robin_kiss"):
        hide robin_kiss
        show robin at right6
        with dissolve
    "[robin.name] eases up and gives me space between me and the guy so he can slip out of me."
    $ player.grope_end()
    pc "Shit. You are such a bitch."
    robin.name "I am."
    return

label robin_bus_sex_event_sex_robin_pullout:
    "I try to pull away from the guy, [robin.name] isn't giving my much space but I manage to buck forward enough for him to slip out."
    $ player.grope_poke()
    "With me still pressed against the guy and his cock between my legs, I hump back and forward to get him off."
    pervert "Nnnnnngggg..."
    $ player.sex_cum(busgroper, "pullout")
    pcm "Mmmmmmm..."
    $ player.grope()
    pervert "Haaaaa..."
    $ player.grope()
    if renpy.showing("robin_kiss"):
        hide robin_kiss
        show robin at right6
        with dissolve
    pc "*Huff*"
    pc "Well that was fun..."
    $ player.grope_end()
    pc "Shit. You are such a bitch."
    robin.name "I am."
    return



label robin_bus_sex_event_watch:
    pc "Not messing about are you?"
    robin.name "Why should I?"
    "I stand there watching as [robin.name] pretends to try to wiggle out of his grasp."
    "But I know her and know she is just wiggling her bum against him, inviting him to do more."
    if numgen():
        "It doesn't look like he is taking the bait though and I end up standing there watching [robin.name] touched all over."
        "She doesn't seem to mind though. Rubbing herself against him and seems he is humping back in return."
        pcm "Maybe I should have had my own fun. She likes watching way more than I do..."
        if "can_lesbian" in robin.list:
            pcm "Maybe I can tease her some more..."
            show robin_kiss with dissolve
            "I put my lips against hers and help the guy out in groping her all over."
            pcm "No idea what the guy is thinking how."
            "The guy groping her seems to ease off eventually though."
            pcm "Did he cum or just give up?"
            hide robin_bus_grope_front with dissolve
            hide robin_kiss with dissolve
            "I just carry on standing there pretending to wait for my stop."
        else:
            pcm "C'mon, fuck her..."
            "I see [robin.name] grinding more on the guys crotch and the way he is squeezing her boobs makes it clear what is happening here."
            pcm "Ah, getting off now are you?"
            "The guy then eases off her and fades back into the bus while me and [robin.name] stand there waiting for our stop."
    else:
        pcm "Is he?"
        pcm "Need a better look..."
        pcm "Ah, yeah. He's got his thing out."
        pc "You being poked?"
        robin.name "Allllmooossst..."
        robin.name "Nnng!"
        robin.name "Oooh! Yeah... He put it in me..."
        hide robin_bus_grope_front
        show robin_bus_sex
        with dissolve
        pc "Nice."
        robin.name "Uggghh..."
        pc "Dirty slut!"
        robin.name "Mmm yeah. Dirty fucking slut letting this idiot fuck me."
        robin.name "Mmmmm..."
        "I stand there watching [robin.name] getting fucked and giving little notice to the other people on the bus."
        "She is not being very quiet so it is pretty obvious to everyone what it going on..."
        if not numgen(0,6):
            hide robin_bus_sex
            $ player.grope(steal=True)
            pc "Ah?"
            pcm "Oh? Want in on the action as well?"
            pcm "Pervert!"
            $ robin.have_sex(busgroper)
            jump robin_bus_sex_event_hump_alone
        "Almost abandoning all pretence, the guy speeds up and fucks her as if they were alone in a motel room."
        robin.name "Ooooh fuuuuck!"
        robin.name "Yes, keep going!"
        $ renpy.show_screen("cum_action")
        $ robin.have_sex(busgroper)
        pervert "Nnnnnnggg!"
        robin.name "Ooooh fuck."
        robin.name "Mmmmm."
        pc "Oh, gave you something?"
        robin.name "Yeah..."
        hide robin_bus_sex
        show robin at right6
        with dissolve
        "[robin.name] pulls away from the guy and fixes her clothes."
        pc "Happy?"
        robin.name "Yup. Next time I will watch you get taken."
        pc "Yeah yeah."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
