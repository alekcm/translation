label random_event_home_robin_meet_firsttime:
    if c.exposed:
        if not "robin_talk_lesbian_times" in robin.dict:
            $ robin.dict["robin_talk_lesbian_times"] = 0
        $ robin.dict["robin_talk_lesbian_times"] += 1
        show robin worried hoodie at right1 with dissolve
        robin.name "Ah, hey... Err, sorry... I caught you at a bad time."
        pc "Huh?"
        robin.name "I'm [robin.name], your new flatmate. Nice to meet you."
        hide robin with dissolve
        pcm "Err... Okay then."
        $ diary_people_meet_robin_func()
        jump travel
    show robin happy hoodie at right1 with dissolve
    robin.name "Ah, hey!"
    pc "Hey?"
    robin.name "I just moved in. Guess we are flatmates?"
    pc "Ah, yeah. Nice to meet you. I'm [name]."
    show robin neutral
    robin.name "[robin.name]. You been here long?"
    pc "No, just moved in."
    robin.name "Ah good. I have no idea of the place either."
    robin.name "I'll finish packing away my stuff. But nice to meet you."
    pc "Sure, you too."
    hide robin with dissolve
    $ diary_people_meet_robin_func()
    jump travel

label robin_talk_meet_intro_0:
    $ robin.dict["robin_meet_chain"] += 1
    show robin at right1
    pc "Hey."
    robin.name "Hey, so you said you were new here?"
    pc "Yeah, only came into town recently."
    robin.name "Ah, not just new to the flat but [town] as well?"
    pc "Yeah."
    jump robin_talk_end

label robin_talk_meet_intro_1:
    $ robin.dict["robin_meet_chain"] += 1
    show robin at right1
    pc "What about you? New to [town]?"
    robin.name "Sort of. I came during all the chaos and ended up shit creek with all the stuff going on."
    pc "Ah, yeah I wasn't around for most of the chaos so don't know what that was like."
    robin.name "Not good. Ended up getting my arse kicked by people calling themselves the police."
    pc "Oh?"
    jump robin_talk_end

label robin_talk_meet_intro_2:
    $ robin.dict["robin_meet_chain"] += 1
    show robin at right1
    pc "So why'd the police kick your arse?"
    robin.name "They were fucking over everyone. Injecting everyone to stop the spread of the plague."
    robin.name "Anyone who tried to resist got the shit beaten out of them. Then just everyone got a kicking because it was easier that way."
    pc "Oh wow. You resisting or just caught up in the mess?"
    robin.name "I was just running from fuckers with sticks. I just arrived in [town] so had no fucking idea what was going on."
    pc "Hah, Damn..."
    jump robin_talk_end

label robin_talk_meet_intro_3:
    $ robin.dict["robin_meet_chain"] += 1
    show robin at right1
    pc "All good now though after the beating?"
    robin.name "Yeah, took a while to heal up but okay from there."
    robin.name "Then some guy comes through telling me there is a place for me at the academy if I wanted it. Fuck knows why."
    pc "You agreed?"
    robin.name "Yeah, got me set up with this place thanks to that. Better than where I was sleeping before so 'course I agreed."
    jump robin_talk_end

label robin_talk_meet_intro_4:
    $ robin.dict["robin_meet_chain"] += 1
    show robin at right1
    robin.name "What about you? How you end up here?"
    if quest_homeless_start.active:
        pc "Heard it was a safe place so me and my sister drove here."
        pc "She ended up crashing the car and we ran from some weirdos right through the checkpoint."
        robin.name "Oh? Sounds like fun."
        pc "Yeah, ended up separated for a while until we stumbled across each other in the street."
        pc "Didn't get to see any of the fun stuff you mention though."
    else:
        pc "Kind of the same. Arrived here running from all the chaos, ended up crashing and then waking up in hospital."
        robin.name "Oh fuck. It bad?"
        pc "Kind of. Missed out on all the really fun stuff like what you talked about. Got out of hospital and was also told I would be going to the academy."
        pc "No clue what was going on so just agreed until I figure things out."
        if t.day < 5:
            pc "Still trying to see what is going on round here..."
    jump robin_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
