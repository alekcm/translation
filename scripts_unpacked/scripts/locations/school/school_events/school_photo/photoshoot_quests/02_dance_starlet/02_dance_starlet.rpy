label quest_photo_dancestarlet_picker:


label quest_photo_dancestarlet_start:
    felix.name "So I am thinking for the next issue we should revisit your dance clothes."
    pc "What about money from the last one?"
    felix.name "Ah, yes. Hold on..."
    $ player.add_money(200)
    pc "Oooh. Err, not bad but could be better."
    felix.name "I think once things start picking up we will do better. But it's enough to make things worth it for now."
    pc "So, short skirt and tiny pants?"
    felix.name "Yeah, I'm not sure how far we should go with this one."
    felix.name "The skirt barely hides anything and might be too on the nose."
    pc "It was the one that kept getting stolen."
    felix.name "It was..."
    felix.name "I see you girls have also been making... err... \"adustments\" to your dance gear as well."
    if player.has_perk(perk_exhibitionist, notif=True):
        pc "No knickers and tits out when we lift our arms?"
        felix.name "No knickers?"
        pc "Ah, well, that one is just me."
        felix.name "Right. Well, that's too far for sure. So try your best to keep your knickers on."
        pc "No promises."
    elif player.has_perk([perk_bimbo, perk_slut, perk_whore, perk_sucu]):
        pc "Upskirts and upboobs?"
        felix.name "Upboobs?"
        pc "Yeah, small crop top that flashes too much when you lift your arms up."
        if player.breasts == 3:
            pc "Well, for the other girls anyway. Me and [anabel.name] can barely keep them hidden even when we try."
        felix.name "Right. Well I think having them on display is too much, so maybe try and keep them hidden?"
        if player.breasts == 3:
            pc "These things do as they please. I have no control over them."
        else:
            pc "That's on you to pick the right angles."
    else:
        pc "Yeah, parts keep going missing and we are making more money. So more goes missing."
        felix.name "Well, let's try and keep it so most of your clothes are still on."
        pc "We will see about that."
    felix.name "Might be better for now to focus on... well. Not up your skirt."
    pc "Why? That's what got all the fliers taken."
    felix.name "Might also be what gets us shut down."
    felix.name "Still trying to keep it innocent for now."
    pc "Sure..."
    pc "So what do you have in mind?"
    felix.name "Well, let's have you change into your dance gear and see how things go from there."
    pc "Okay."
    hide felix
    $ walk(loc_school_locker_girls)
    $ photo_clothes_dance_revealing()
    $ pc_strip_tops()
    pause 0.5
    $ pc_strip()
    pause 0.5
    $ pc_dress_quick("work")
    $ player.set_hair("bun")
    pc "There we go..."
    $ walk(loc_school_gym, trans=False)
    show felix at right1 with dissolve
    pc "Sure you are going to manage this?"
    felix.name "Well, it's what you dance in so there is at least an excuse."
    pc "Right."
    felix.name "Maybe just try not to flap your skirt too much."
    pc "Last time you wanted me to pull my shorts up the crack of my ass and now you want me to cover up?"
    felix.name "Haha. Yes."
    felix.name "Remember, don't move too much or the photos will blur."
    show ps_dance
    hide felix
    with dissolve
    "I start doing some dancing poses and watch as [felix.name] circles me taking photos."
    if player.breasts == 3:
        felix.name "You actually dance like this?"
        pc "Yeah, brings in th tips."
        felix.name "I expect so..."
        pc "What?"
        felix.name "You said upskirt and upboob. But this is full boob boob."
        pc "Ah?"
        pc "Really?"
        felix.name "You didn't know?"
        pc "Ehhh. I guessed there would be some slippage. Didn't realise they were on full display."
    else:
        felix.name "I'm guessing your underwear is that colour so it can be noticed?"
        pc "Yeah. [rachel.name] had us all wear them and we brought in a lot more tips."
        felix.name "I bet it did."
        pc "It no good?"
        felix.name "A bit too obvious I think."
    felix.name "Try a different pose."
    pc "Okay."
    hide ps_dance
    show dance_behind
    with dissolve
    "I strike a new pose and wait for [felix.name] to start taking photos."
    felix.name "Hmmm..."
    pc "Problem?"
    felix.name "Sort of. With these knickers you are wearing, all I am getting are shots of your bare arse."
    pc "Normally my bare arse makes people happy."
    felix.name "I'm sure it would. Could also end up shutting us down."
    pc "Maybe stop trying to take sexy ones then and just aim at plain?"
    felix.name "Okay. Try another pose."
    "*New shot that isnt drawn yet. it will be more of a top down view of sammy."
    "It will be okay and end the shoot."
    hide dance_behind
    show felix at right1
    with dissolve
    felix.name "Okay. I'll see what I can get out of these shots. Might end up having to crop them though."
    pc "Okay, well I'll leave that up to you."
    felix.name "Come see me when I have these developed and we can have a look at them."
    pc "Right."
    hide felix with dissolve
    $ pc_dress_event("party", loc_school_locker_girls)

    $ quest_photo.workedtoday = t.day
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
