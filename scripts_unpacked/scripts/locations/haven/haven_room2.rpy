label haven_room2_listen_chainstart:
    if haven_time_empty():
        pcm "Hmm, can't hear anything from the lounge so it's probably empty. I should come back when more people are hanging around in there."
        jump travel
    else:

        jump haven_room2_listen_chain

label haven_room2_listen_goodinfo:
    if not "intel_1" in main_quest_05.conversation_topics:
        jump haven_intel_1
    elif not "intel_2" in main_quest_05.conversation_topics:
        jump haven_intel_2
    else:
        jump haven_room2_listen_genericinfo

label haven_room2_listen_chain:

    call haven_room2_listen_start from _call_haven_room2_listen_start

    if haven_intel_chance():
        call haven_room2_listen_goodinfo from _call_haven_room2_listen_goodinfo
    else:
        call haven_room2_listen_genericinfo from _call_haven_room2_listen_genericinfo

    call random_event_picker_haven_tombola_call from _call_random_event_picker_haven_tombola_call

    call haven_room2_listen_cont from _call_haven_room2_listen_cont

    if haven_intel_chance():
        call haven_room2_listen_goodinfo from _call_haven_room2_listen_goodinfo_1
    else:
        call haven_room2_listen_genericinfo from _call_haven_room2_listen_genericinfo_1

    call random_event_picker_haven_tombola_call from _call_random_event_picker_haven_tombola_call_1

    jump haven_room2_listen_end

label haven_room2_listen_start:
    show haven_wait at right2 with dissolve
    $ dialouge = WeightedChoice([
    ("Let's see if I can overhear anything from the lounge.", 1),
    ("Hopefully I can hear something that can help me find this Doctor.", 1)
    ])
    pcm "[dialouge]"
    return

label haven_room2_listen_cont:
    $ dialouge = WeightedChoice([
    ("So much talking but so little worth listening to.", 1),
    ("Mmm, ok. Anything else?", 1),
    ("Hmm...", 1),
    ])
    pcm "[dialouge]"
    return

label haven_room2_listen_genericinfo:
    $ dialouge = WeightedChoice([
    ("...hadn't paid for weeks. I caught him hiding near the highway but the little shit saw me first and ran faster than...", 1),
    ("...couldn't even scrounge up enough for a few bottles...", 1),
    ("...the security. Luckily it was those fuckers, err, can't remember their names. But a little payment and they fuck off somewhere else.", 1),
    ("...came up to me telling me \"I need it, I need it!\" You need it huh, then pay for it!", 1),
    ("...doesn't really matter. Have less people that want it these days so it doesn't matter that delivery is slow.", 1),
    ("...the lake is a good place. Pretty far from here but there are always people from the housing estates looking to numb the pain as well but too proud to come round here.", 1),
    ("...you better avoid them. Don't have a good relationship and you could end up in some alley getting kicked to shit.", 1),
    ("...industrial area if you can stay hidden. But get caught and you...", 1)
    ])
    hav "[dialouge]"
    $ stroll(10)
    return

label haven_room2_listen_end:
    $ dialouge = WeightedChoice([
    ("Ah well, I think that's enough for now.", 1),
    ("Not sure how much these guys would be in need of a doctor.", 1),
    ("Sounds like we all have our own troubles...", 1),
    ("Listening to these guys makes me dread having to live here permanently.", 1),
    ])
    pcm "[dialouge]"
    hide haven_wait with dissolve
    jump travel_arrival
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
