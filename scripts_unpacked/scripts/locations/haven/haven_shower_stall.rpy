label haven_shower_stall_arrival:

    if main_quest_05.active == 1:
        if not loc_haven_utilities.visited:
            jump loc_haven_utilities_visit
        elif loc_haven_utilities.visited and main_quest_05.stage == 2:

            pc "It's a maintenance room. I should check other places for [ant.name]."
            jump travel

    $ haven_utilities_join_chance()

    if loc_cur == loc_haven_utilities and not player.cum_any_check():
        $ walk(loc_haven_shower_stall)
        jump travel
    else:

        if not loc_cur == loc_haven_utilities:
            if player.drinking:
                "I finish up my drink before heading in."
                $ player.drink_finish()
            $ pc_striptease()
            $ acc_shower()
            pause 0.5


        $ walk(loc_haven_shower_stall)
        pause 0.5
        show shower with dissolve

        if player.cum_any_check():
            pcm "I had better clean this cum off me or I will attract attention."
        elif player.hygiene > 40:
            "I stand in the shower pretending to wash while keeping a discreet eye on other people."
        else:
            "I wash while keeping a discreet eye on other people."

        $ player.shower()
        $ acc.makeup_on = False

        if not loc_from == loc_haven_utilities:
            if haven_time_safe():
                pcm "Lots of women in the shower sticking together right now. If I try to head into the maintenance room now, no doubt one of them will see me."
            elif haven_time_empty():
                pcm "Pretty quiet right now, I should be able to get in the maintenance room no problem"
            elif haven_time_danger():
                pcm "Pretty busy in here and almost entirely men. Now wouldn't be a good time to sneak into the maintenance room."
            else:
                pcm "Some people around but hopefully they won't notice me if I head into the maintenance room."
        hide shower with dissolve

        jump random_event_picker_haven_tombola


label haven_shower_stall_propt:
    pcm "Do I want to go into the showers?"
    menu:
        "Yes":
            $ pc_strip()
            jump haven_shower_stall_arrival
        "Not right now":
            jump travel

label haven_shower_stall_listen:
    if haven_time_empty():
        pcm "So few people in here and none of them talking. I should come back when it's got more people."
        jump travel
    else:
        jump haven_shower_listen_chain

label haven_shower_listen_chain:

    call haven_shower_listen_start from _call_haven_shower_listen_start
    call haven_shower_listen_chain_picker from _call_haven_shower_listen_chain_picker
    call random_event_picker_haven_tombola_call from _call_random_event_picker_haven_tombola_call_3
    if not rand_choice == "random_event_none":
        jump expression rand_choice
    call haven_shower_listen_cont from _call_haven_shower_listen_cont
    call haven_shower_listen_chain_picker from _call_haven_shower_listen_chain_picker_1
    call random_event_picker_haven_tombola_call from _call_random_event_picker_haven_tombola_call_4
    if not rand_choice == "random_event_none":
        jump expression rand_choice
    jump haven_shower_listen_leave

label haven_shower_listen_chain_picker:
    if haven_intel_chance():
        if haven_time_safe():
            call haven_shower_listen_goodinfo_girls from _call_haven_shower_listen_goodinfo_girls

        elif haven_time_normal():
            $ rand_choice = WeightedChoice([
            ("haven_shower_listen_goodinfo_girls", 1),
            ("haven_shower_listen_goodinfo", 1),
            ])
            call expression rand_choice from _call_expression
        else:

            call haven_shower_listen_goodinfo from _call_haven_shower_listen_goodinfo
    else:

        if haven_time_safe():
            call haven_shower_listen_genericinfo_girls from _call_haven_shower_listen_genericinfo_girls

        elif haven_time_normal():
            $ rand_choice = WeightedChoice([
            ("haven_shower_listen_genericinfo_girls", 1),
            ("haven_shower_listen_genericinfo", 1),
            ])
            call expression rand_choice from _call_expression_1
        else:

            call haven_shower_listen_genericinfo from _call_haven_shower_listen_genericinfo

    return

label haven_shower_listen_start:
    $ dialouge = WeightedChoice([
    ("I can't really look around too much or someone might get the wrong idea. But I can listen to them", 1),
    ("Can pretend I am showering and just listen to what these people have to say.", 1),
    ("Watching people can give the wrong idea, but I can eavesdrop on anything they say.", 1),
    ("Mostly girls in here so won't see the Doctor, but I can listen to hear if they say anything interesting.", If (haven_time_safe(),1,0)),
    ("Not very busy in here but I suppose I can listen out for anything.", If (haven_time_empty(),1,0)),
    ("Hanging around here listening might attract the men, but I need to listen out for anything to do with this Doctor.", If (not (haven_time_empty() or haven_time_safe()),1,0)),
    ])
    pcm "[dialouge]"
    return

label haven_shower_listen_cont:
    $ dialouge = WeightedChoice([
    ("So much talking but so little worth listening to.", 1),
    ("Mmm, ok. Anything else?", 1),
    ("Hmm...", 1),
    ])
    pcm "[dialouge]"
    return

label haven_shower_listen_goodinfo_girls:
    if not "intel_3" in main_quest_05.conversation_topics:
        jump haven_intel_3
    elif not "intel_4" in main_quest_05.conversation_topics:
        jump haven_intel_4
    else:
        jump haven_shower_listen_genericinfo_girls

label haven_shower_listen_goodinfo:
    if not "intel_5" in main_quest_05.conversation_topics:
        jump haven_intel_5
    elif not "intel_6" in main_quest_05.conversation_topics:
        jump haven_intel_6
    else:
        jump haven_shower_listen_genericinfo

label haven_shower_listen_genericinfo_girls:

    $ dialouge = WeightedChoice([
    ("...like I can't even wash it off. It got everywhere! How does one person manage to...", 1),
    ("...didn't even know what was going on. I drank so many jars just to get through the day and before I knew it I woke up covered in...", 1),
    ("...hate them so much. I am just trying to work and they constantly harass us. Trying to get money off us or put their dick in us. Getting to the point where there isn't enough time...", 1),
    ("...told him \"no\". But you know how much these idiots listen when you tell them to go away. They think you are just trying to bump up the price so they either get...", 1),
    ("...would avoid them if I were you. Any place that has girls from over the wall working there is somewhere that you want to stay as far away from as you possibly...", 1),
    ("...the look on her face? It was like she had nothing behind her eyes. Someone so worn down that they have given up and just carries on as if on automatic.", 1),
    ("...security bastards. Can't even work at the highway properly anymore without them expecting some freebies. Tryina make enough to eat a meal but dealing with those bastards takes time away...", 1),
    ("...arresting you if you go down Revel. Gotta be sneaky about it these days and look normal, but then you can't get the customers to notice...", 1)
    ])
    havgirl "[dialouge]"
    $ working(15)
    return

label haven_shower_listen_genericinfo:

    $ dialouge = WeightedChoice([
    ("...like I can't even wash it off. It got everywhere! How does one person manage to...", 1),
    ("...didn't even know what was going on. I drank so many jars just to get through the day and before I knew it I woke up covered in...", 1),
    ("...hate them so much. I am just trying to work and they constantly harass us. Trying to get money off us or put their dicks in us. Getting to the point where there isn't enough time...", 1),
    ("...told him \"no\". But you know how much these idiots listen when you tell them to go away. They think you are just trying to bump up the price so they either get...", 1),
    ("...would avoid them if I were you. Any place that has girls from over the wall working there is somewhere that you want to stay as far away from as you possibly...", 1),
    ("...the look on her face? It was like she had nothing behind her eyes. Someone so worn down that they have given up and just carries on as if on automatic.", 1),
    ("...security bastards. Can't even work at the highway properly anymore without them expecting some freebies. Tryina make enough to eat a meal but dealing with those bastards takes time away...", 1),
    ("...arresting you if you go down Revel. Gotta be sneaky about it these days and look normal, but then you can't get the customers to notice...", 1)
    ])
    hav "[dialouge]"
    $ working(15)
    return

label haven_shower_listen_leave:
    $ dialouge = WeightedChoice([
    ("Ah well, I think that's enough for now.", 1),
    ("Not sure how much these guys would be in need of a doctor.", 1),
    ("Sounds like we all have our own troubles...", 1),
    ("Listening to this lot makes me dread having to live here permanently.", 1),
    ])
    pcm "[dialouge]"
    jump travel_arrival

label haven_shower_stall_join:
    jump expression WeightedChoice([
    ("random_event_haven_shower_1", haven_random_event_room_weight(shower=True)),
    ("random_event_haven_shower_2", haven_random_event_room_weight(shower=True)),
    ("random_event_haven_shower_3", haven_random_event_room_weight(shower=True)),
    ("random_event_haven_shower_4", haven_random_event_room_weight(shower=True)),
    ("random_event_haven_shower_5", haven_random_event_room_weight(shower=True)),
    ("random_event_haven_shower_6", haven_random_event_room_weight(shower=True)),
    ("random_event_haven_shower_7", If (player.drunk > 60, haven_random_event_room_weight(shower=True),0)),
    ("random_event_haven_shower_8", If (player.drunk > 60, haven_random_event_room_weight(shower=True),0)),
    ("random_event_haven_shower_9", haven_random_event_room_weight(shower=True)),
    ("random_event_haven_shower_10", haven_random_event_room_weight(shower=True)),
    ("random_event_haven_shower_11", haven_random_event_room_weight(shower=True)),
    ("random_event_haven_shower_12", haven_random_event_room_weight(shower=True)),
    ])
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
