label haven_ending_leave_gateguard:
    $ walk(loc_haven_toplanding)
    pcm "Hopefully the guard will just let me pass..."
    if player.cum_visible:
        pcm "Better wipe up a bit first so I don't look like a cum whore."
        $ player.cum_clean_outside()
        "I wipe up the cum with my top as best I can."
    $ loc_haven_landing.dict["gate_open"] = False
    $ walk(loc_haven_landing)
    if havengateguard.sex and haven_guard_hours():
        pc "Hey~"
        havengateguard.name "Hey. Heading out are ya."
        pc "Yeah. Too many desperate guys up there. Safer down here if you aren't around."
        havengateguard.name "Ah. Yeah should have thought about that."
        havengateguard.name "Gonna see you later?"
        pc "Maybe~"
        havengateguard.name "Heh. Well if I'm not here, just speak to whoever is. He will give me a shout."
        pc "Sure."
        $ loc_haven_landing.dict["gate_open"] = True
        havengateguard.name "Looking forward to it."
        pc "Eh. I bet."
        pause 0.5
        $ walk(loc_haven_lobby)
        pause 0.5
        pcm "..."
        pcm "Still dont know his name..."
        pcm "Ah well. Probably never see him again anyway."
        pause 0.5
        jump haven_ending_leave
    else:
        pc "Hi, can you open the gate please."
        havguard "Er, one sec..."
        $ loc_haven_landing.dict["gate_open"] = True
        havguard "There we go. Have a good night."
        pc "You too."
        pause 0.5
        $ walk(loc_haven_lobby)
        pause 0.5
        jump haven_ending_leave



label haven_ending_leave_intel:
    pc "Got all the info I need for [tucker.name] so I can leave. But won't be returning any time soon so if there is anything I want to do I had better do it now."
    menu:
        "Leave Haven":
            $ add_to_list(main_quest_05.list, "got_intel")
            jump haven_ending_leave
        "Stay for a bit longer":
            pcm "This place is a shithole so probably shouldn't hang around too much."
            jump travel

label haven_ending_leave_dress:
    pc "Better grab my clothes from the showers first."
    $ walk(loc_haven_hallway_1f)
    pause 0.5
    $ walk(loc_haven_shower)
    pause 0.5
    $ pc_dress_under()
    pause 0.5
    $ pc_dress()
    $ acc_shower_dress()
    $ acc.makeup_on = True
    pc "Great, now better get out of here before I get into more trouble."
    $ walk(loc_haven_hallway_1f)
    pause 0.5
    $ walk(loc_haven_lobby)
    pause 0.5
    jump haven_ending_leave

label haven_ending_leave:
    if c.exposed:
        jump haven_ending_leave_dress
    $ walk(loc_haven_exterior)
    pc "*Phew*"
    pcm "Well, getting out of there was painless. Now to try and meet up with one of [tucker.name]'s goons."
    $ walk(loc_highway, time_amount=15)
    $ haven_complete_questlog()
label haven_ending_leave_fire:
    pcm "Hmm, they should have seen me leaving and hopefully followed me. Maybe I should go somewhere more out of the way. Let's see..."
    $ walk(loc_alley, time_amount=10)
    pcm "Now assuming they weren't passed out drunk or something, they should find me."
    pcm "... ..."
    $ stroll(20)
    pcm "..."
    pcm "Come on you lazy lot. Don't want to be standing here like some alleyway hooker..."
    pcm "... ..."
    $ stroll(20)
    pcm "..."
    if player.tired <= 20:
        pcm "Ah sod this. I am far too tired to be hanging around here. I'll make my way to the hospital."
    else:
        pcm "Ah sod this. I'll just make my way to the hospital."
    $ walk(loc_revel, time_amount=15)
    pause 0.5
    $ walk(loc_hospital_entrance)
    pause 0.5
    $ walk(loc_hospital_lobby)
    if t.hour in workhours:
        jump haven_ending_leave_day
    else:
        jump haven_ending_leave_night

label haven_ending_leave_day:
    show receptionist at right1 with dissolve
    pc "Hi, I am here to see [tucker.name]."
    receptionist.name "Miss [sname]?!"
    pc "That's right."
    receptionist.name "Err, go on in. He is in his office."
    pc "Thanks."
    pause 0.5
    hide receptionist
    $ walk(loc_hospital_office)
    show tucker at right1 with dissolve
    pause 0.5
    pc "[tucker.name]?"
    tucker.name "[fname]? What are you doing here? Come in."
    pc "Didn't come across anyone keeping an eye on [haven] so I just came here."
    jump haven_ending_leave_cont



label haven_ending_leave_night:
    pcm "Wonder if I should have just went home and got some sleep since [tucker.name] probably isn't here"
    pc "Hi, don't suppose [tucker.name] is working late tonight and is still in his office?"
    show receptionist at right1 with dissolve
    receptionist.name "Err, no he isn't. He went home for the night some time ago."
    pc "Thought as much. Thanks."
    hide receptionist with dissolve
    pcm "Ugh, I am exhausted. I think I'll just sit in the waiting room until he arrives."
    pcm "Shouldn't be too long I hope..."
    show screen blackout(75) with dissolve
    hide screen blackout with dissolve
    pcm "Uh, so tired..."
    show screen blackout(100) with dissolve
    show tucker at right1
    $ time_advance_to(7,40)
    if player.tired < 30:
        $ player.set_tired(30)
    $ player.add_drunk(-100)
    if player.mood < 30:
        $ player.set_mood(30)
    $ player.face_normal()
    $ player.eye = 3
    pause 1
    show screen blackout(50) with dissolve
    tucker.name "[fname]!"
    $ player.eye = 2
    pc "Huh?"
    $ player.face_shock()
    hide screen blackout with hpunch
    pc "Ah!"
    tucker.name "Good to see you well. Come to my office."
    $ player.face_normal()
    pc "Ughh. Yeah..."
    $ walk(loc_hospital_office)
    tucker.name "Something hot to drink?"
    pc "Sure."
    tucker.name "So you are in one piece so that's a good sign."

    if main_quest_05.rape >= 10:
        pc "Yeah, considering what went on in there, it's about the only good thing."
    elif main_quest_05.rape > 0:
        pc "Well, suppose that's one way to look at it."
    else:
        pc "Yeah, got away pretty lucky in there."
    tucker.name "Here. Why are you here alone? Why didn't security pick you up?"
    $ player.right_hand = "coffee"
    pc "No idea. After I left I waited for someone to find me. But after an hour no one came and I didn't want to hang round too long at night so just came here."
    jump haven_ending_leave_cont

label haven_ending_leave_cont:
    tucker.name "Hmmm. I will have to have a talk with [miller.name]. There should have been people watching the place and keeping an eye out for you."
    pc "Well, from what I have seen of them they were probably too busy drinking or spending time exploiting some of the whores."
    tucker.name "Hmmm."
    tucker.name "Well, you look a mess. Head to the ward and find a bed and I will prepare things with [nik.name] and [emile.name] while you sleep."
    pc "Sounds good."
    tucker.name "You know where it is?"
    pc "Yeah."
    hide tucker
    $ player.hands_reset()
    $ walk(loc_hospital_ward)
    pcm "Ugh, I feel like shit."
    pcm "Smell like shit as well..."
    pcm "Whatever. Sleep..."
    $ player.eye = 3
    show screen blackout(100) with dissolve
    jump haven_ending_wrapup
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
