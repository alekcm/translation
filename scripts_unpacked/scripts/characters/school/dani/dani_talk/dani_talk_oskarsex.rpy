label oskar_sex_talk_0:
    $ dani.dict["oskar_sex_talk"] += 1
    $ dani_yan_max_add(20)
    dani.name "So, err. Do you always pay rent with money?"
    if "oskar_sex_comment" in dani.list and oskar.sex:
        pc "I think we both pay the same way."
        dani.name "What do you mean?"
        pc "I mean some of the comments you have made. Sex with [oskar.name]?"
        dani.name "You too?"
        pc "Yeah."
    elif "oskar_sex_comment" in dani.list:
        pc "..."
        pc "You commented something before. [oskar.name] making you do things?"
        dani.name "Something like that..."
        dani.name "It's not like he makes me, sort of..."
        pc "That or be homeless?"
        dani.name "..."
    else:
        pc "Err, of course. What else..."
        pc "Ah..."
        pc "I see..."
        dani.name "Yeah..."
        dani.name "I don't always have the money. So..."
        pc "Yeah..."
    $ add_to_list(dani.list, "knows_dani_sex_oskar")
    jump dani_talk_end

label oskar_sex_talk_1:
    $ dani.dict["oskar_sex_talk"] += 1
    dani.name "Doesn't feel right paying rent that way."
    pc "You have a better way to pay?"
    dani.name "Money."
    pc "Which you don't have..."
    dani.name "..."
    jump dani_talk_end

label oskar_sex_talk_2:
    $ dani.dict["oskar_sex_talk"] += 1
    if quest_homeless.active:
        if not loc_highway_slum_home.locked:
            pc "Well, I ended up in the slums for now paying that shit his rent."
        else:
            pc "I'm still looking for a place after not paying that shit his rent."
        if not oskar.sex:
            pc "Maybe I should have just bent over..."
            pc "Might have made it all easier than it is now."
        else:
            pc "I tried bending over for him, but still couldn't afford it."
        pc "Come and look at places in the slums with me. I'm sure you will only be raped a few times."
    else:
        pc "Dunno about you. But I think I would rather be bent over by [oskar.name] than raped in the highway slums."

    dani.name "Is there not, err, like a place between here and the slums?"

    if main_quest_05.iscomplete():
        pc "I was in a homeless community once. I could show you the way."
        dani.name "Isn't that just as bad as the slums?"
        pc "No, a little better. The slum they will kill you and rape your corpse."
        pc "Haven at least they just rape you."
        if "slave" in main_quest_05.list:
            pc "Someone did sell me to a brothel though. Nice place to live for half a year."
            pc "Tiny little cell, beaten and raped daily."
            pc "No rent and free drugs though. So that's a plus."
            dani.name "Fuck [name]..."
        else:
            dani.name "I think I will pass on that."
    elif "jaylee_meet_events" in jaylee.dict and not renpy.has_label("jaylee_meet_" + str(jaylee.dict["jaylee_meet_events"])):
        pc "I know a girl who lives in a shipping container. I could tell her to let you live there."
        if "slept_together" in jaylee.conversation_topics:
            pc "Although she will probably also want to put things in your ass..."
    elif loc_office_pi.visited:
        pc "I know a guy who lives in a shitty place in Revel. Even uses it as an office. I could send you to him."
        pc "No promises he won't want to fuck you as well though."
    else:
        pc "Maybe. I haven't looked. Some places in Revel"
        dani.name "I might go have a look..."
    jump dani_talk_end

label oskar_sex_talk_3:
    $ dani.dict["oskar_sex_talk"] += 1
    if oskar.rape:
        pc "Well, when he pisses you off too much, just make sure to stab him once more for me."
        dani.name "Haha, okay."
        pc "See how he likes it getting something put inside him he doesn't want."
        jump dani_talk_end

    if loc_kitchen.locked:
        pc "Well, come join the homeless gang with me. No need to ben over for that arse."
        dani.name "Yeah, just everyone else."
        pc "Nooo. Only most of everyone else."
        pc "At least it's mostly your own choice..."
        jump dani_talk_end

    pc "What's the problem anyway with [oskar.name]?"
    if pubpatron.name in dani.sex_who:
        pc "I've seen you go in the back room with a pub drunk before. [oskar.name] drops more rent than they pay you."
        dani.name "I know..."
        dani.name "I've just kind of gotten used to this stuff now."
        dani.name "But when I had to do it with [oskar.name], I wasn't, y'know, prepared."
    elif "dance_waited_during_date" in dani.conversation_topics:
        pc "I waited for you while some guy paid for your company in the park."
        if "dance_waited_interrupt_toilet" in dani.conversation_topics:
            pc "Watched him wank on your tits even..."
            dani.name "[name]!"
        pc "So not like getting money that way is an issue."
        dani.name "I chose to do that. With [oskar.name], it feels like I am being forced."
        pc "All money in the end..."
    else:
        pc "Better that than homeless. He's clean and decent looking I suppose."
        dani.name "Ugh, I just don't like it."
        pc "Don't have to. Just do it and get it over with."
    jump dani_talk_end

label oskar_sex_talk_4:
    $ dani.dict["oskar_sex_talk"] += 1
    pc "When are you going to show me your place anyway?"
    dani.name "There isn't much to show. It's tiny."
    pc "Can't be that bad if you are fucking [oskar.name] for it."
    dani.name "Ugh."
    jump dani_talk_end

label oskar_sex_talk_5:
    $ dani.dict["oskar_sex_talk"] += 1
    dani.name "Not worth what I pay for it. But sure, I'll show you."
    pc "Okay."
    $ loc_bedroom_dani.locked = False

    dani.name "Have to climb through the window here."
    pc "Window? You aren't having me break in some persons house are you?"
    dani.name "Ha. No."
    pc "You don't have a door?"
    dani.name "Not really. My room was cut in half to shove more people in. Someone else got the door."
    pc "Wait, really?"
    dani.name "Yup."
    $ add_to_list(dani.list, "no_location")
    hide dani with dissolve
    $ dani_here()
    pc "..."
    show dani casual at right5
    $ walk(loc_bedroom_dani)
    dani.name "Home sweet home."
    pc "Wow, you weren't kidding..."
    dani.name "Yup. Tiny."
    show dani at left2 with dissolve
    dani.name "There isn't even a wall behind those shelves. Just another part of the room."
    pc "Wow. That person got the door?"
    show dani happy at right5 with dissolve
    dani.name "Ha, yeah. Doubt he is getting fucked by [oskar.name] for it though."
    pc "Who knows."
    dani.name "Come by if you want. Though I usually hang about outside."
    pc "Sure. Climb in your window like some street rapist."
    pc "Wait. Is it safe?"
    dani.name "Safe as anywhere here can be."
    hide dani with dissolve

    pc "..."
    $ walk(loc_stairwell)
    show dani casual at right1 with dissolve
    dani.name "Now you see why I hang out here."
    pc "Yeah..."
    $ remove_from_list(dani.list, "no_location")
    jump dani_talk_end

label oskar_sex_force_talk:
    $ add_to_list(dani.conversation_topics, "forced_oskar_talk")
    $ player.face_angry()
    pc "So I can see now why you hate that fucker."
    show dani worried
    dani.name "[oskar.name]? Oh? What happened?"
    pc "Probably the same thing as with you."
    pc "I wasn't keeping up with rent and he basically came into my room and raped me."
    dani.name "..."
    dani.name "Wont be the last time he does that..."
    pc "Ugh!"
    jump dani_talk_end

label oskar_sex_kickedout_talk:
    $ add_to_list(dani.conversation_topics, "kickedout_oskar_talk")
    $ player.face_angry()
    pc "I... Wasn't managing to keep up rent."
    show dani worried
    dani.name "Oh shit. What happened?"
    if "beaten_kicked_out" in oskar.list:
        pc "[oskar.name] had some thugs waiting for me when I got home..."
        pc "Kicked the shit out of me, robbed me... And... Yeah..."
        dani.name "Fuck!"
    else:
        pc "As you would guess. [oskar.name] kicked me out."
        if not oskar.rape:
            dani.name "Just like that?"
            pc "Did try and force me to fuck him first..."
            dani.name "Ugh, yeah. That's how it started with me..."
        else:
            if "forced_oskar_talk" in dani.conversation_topics:
                pc "Well, you know before he forced me to do things with him."
                dani.name "Wasn't enough?"
                pc "I still fell behind so, yeah. Kicked out..."
            else:
                $ add_to_list(dani.conversation_topics, "forced_oskar_talk")
                pc "Well, before that he forced himself on me..."
                pc "But I still fell behind and that wasn't enough."
                pc "So got kicked out..."
    if loc_bedroom_dani.locked:
        dani.name "Ugh, hope that doesn't happen to me..."
    else:
        dani.name "Well, he doesn't come around here much, so you can crash here if you want."
        dani.name "But better you find someone else. If he catches you here we will both be fucked."
        pc "Yeah... I know..."
    jump dani_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
