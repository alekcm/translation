label dani_talk_oskar_dead_0:
    $ dani.dict["oskar_missing_talk"] += 1
    dani.name "You know, [oskar.name] hasn't shown up for a while."
    pc "Well, good. Means you haven't had to bend over."
    dani.name "Yeah, just worried he will come back and demand more than I can pay."
    pc "Hmmm..."
    jump dani_talk_end

label dani_talk_oskar_dead_1:
    $ dani.dict["oskar_missing_talk"] += 1
    pc "Well, let's home he pissed someone off a bit much and they hit him over the head or something."
    dani.name "Haha, yeah I hope so."
    dani.name "Have to find where they buried him and piss on his grave."
    pc "Pfft, even in his grave you are taking your knickers off for him."
    dani.name "This time it would be worth it."
    jump dani_talk_end

label dani_talk_oskar_dead_2:
    $ dani.dict["oskar_missing_talk"] += 1
    pc "Probably just sick or something. Don't get your hopes up."
    pcm "Sick and dead hopefully..."
    dani.name "Yeah, can hope though."
    pc "No harm in that."
    jump dani_talk_end

label dani_talk_oskar_dead_know:
    $ add_to_list(dani.list, "oskar_dead_know")
    dani.name "You know they cleaned out that cunts office?"
    pc "Who did?"
    dani.name "Dunno, some guys."
    pc "What? Like some scavvers or what?"
    dani.name "Don't think so. I think they were people who worked for him. There was a security guy with them."
    pc "Oh? Did they arrest him or something?"
    dani.name "No idea. But seems like it means he won't be coming back."
    pc "Good!"
    if loc_kitchen.locked:
        $ loc_kitchen.locked = False
        pcm "Hmm, With that fucker gone for good. Maybe I can live back in my old room."
    jump dani_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
