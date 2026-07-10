label haven_set_fire:
    pcm "I can probably set a fire here. Should I?"
    menu:
        "Yes, let's do this":
            $ inv.drop(item_haven_fluid)
            $ add_to_list(main_quest_05.list, "set_fire")
            $ log.markdone("mq_05_fire")
            jump expression loc_cur.name + "_set_fire"
        "Not now":

            jump travel



label loc_haven_lounge_set_fire:
    if not haven_time_empty():
        pcm "There are people in the room. I'll get spotted before I even manage to set any fires."
        jump travel
    else:
        pcm "Seems like a good place to do this. There are already the firepits so the place already reeks of fire."
        pcm "And it's here where I got the accelerant from so I don't think it will be such a shock if a fire broke out."
        "I gather up some of the tinder that is around the firepits and squirt the accelerant over it. I leave the can near the tinder then get to lighting the fire."
        pcm "Can't make to too big to start with since I need time to leave the room and act all innocent while it spreads."
        $ walk(loc_haven_hallway_2f)
        pcm "Ok, I need to get somewhere the guards won't see me. Where should I go?"
        menu:
            "The room where I can eavesdrop into the lounge.":
                $ walk(loc_haven_room2)
                pcm "Ok, let's wait for the guards to pass then try to head upstairs."
                "I hear the guards rush into the lounge and start franticly trying to stomp out the fire."
                pcm "Ok, now or never."
                "I exit the room and start to make my way down the hallway towards the stairs."
                havguard "Hey, the hell you doing over there. Come here and help!"
                pcm "Fuck, this room was too close to the fire and I was spotted."
                jump haven_set_fire_putout
            "The empty side room near the stairs":

                $ walk(loc_haven_room3)
                pcm "Ok, let's wait for the guards to pass then try to head upstairs."
                "I hear the guards rush the room and hear some muffled commotion down the hallway."
                pcm "Ok, now or never."
                "I exit the room and head straight to the stairs."
                $ walk(loc_haven_landing)
                pcm "Yes! The guards rushing from downstairs didn't bother to lock the gate behind them."
                "I pass through the gate and head up the stairs to the third floor."
                jump haven_access_top_floor
            "Head downstairs out of the way":


                $ walk(loc_haven_landing)
                "I walk to the stairs landing and just as I am about to go down the stairs..."
                havguard "Hey, you smell that?"
                pc "Err, no. What?"
                havguard "Smells like the fires in the lounge have got a bit out of control. Come with me and help me deal with it."
                pcm "Fuck!"
                pc "You are probably imagining things."
                havguard "Just follow me, it happens all the time so I know what I am talking about."
                pcm "Shit, looks like I have no choice."
                pc "Ok..."
                $ walk(loc_haven_hallway_2f)
                pause 0.5
                $ walk(loc_haven_lounge)
                jump haven_set_fire_putout

label loc_haven_storage_set_fire:
    if not haven_time_empty():
        pcm "Better be quick or I will be caught."
        "I gather up a pile of burnable junk from the storage room and pour the accelerant over it. I set it on fire and then leave the room."
        $ walk(loc_haven_lounge)
        pcm "Act innocent, innocent."
        $ walk(loc_haven_hallway_2f)
        show havman at right1 with dissolve
        hav "What the fuck? There is a fire in there!"
        $ player.face_worried()
        pcm "Shit, they noticed already? Should have done it while the room was empty."
        havmuff "Fire? Guys! Fire!"
        show haven_guard3 at right3 with dissolve:
            xzoom -1
        havguard "Fuck, there is a fire. Help put it out!"
        hav "Was her. I saw her leaving there and now the place is on fire."
        $ player.face_shock()
        havguard "What?"
        show haven_guard3 with dissolve:
            xzoom 1
        show haven_guard2 with dissolve
        havguard "Get her, she caused this."
        jump haven_caught_and_beaten
    else:
        $ add_to_list(main_quest_05.list, "burnt_building")
        $ loc_haven_landing.dict["gate_open"] = True
        pcm "Seems like a good place to do this. Secluded and won't be noticed for a while so will give me time to get somewhere else and look innocent."
        "I gather up a pile of burnable junk from the room and pour the accelerant over it. I set it on fire and then leave the room."
        $ walk(loc_haven_lounge)
        pcm "Act innocent, innocent."
        $ walk(loc_haven_hallway_2f)
        pcm "Ok, I have time so I should head downstairs before it is noticed."
        $ walk(loc_haven_landing)
        pause 0.5
        $ walk(loc_haven_lobby)
        pcm "Ok, now just listen out for the commotion..."
        pc "..."
        $ player.face_worried()
        pc "... ..."
        show haven_smoke with dissolve:
            alpha 0.5
        $ player.face_shock()
        pc "... ... ..."
        $ stroll(5)
        pcm "Finally I can hear something going on upstairs. Now just wait for the guards to get moving."
        pcm "..."
        pcm "Should be good."

        $ walk(loc_haven_landing)
        show haven_smoke:
            alpha 1

        $ player.face_worried()
        "I notice the guards franticly running up and down the stairs trying to grab buckets and shouting at each other."
        $ player.face_shock()
        pcm "Fuck! This got way out of hand."
        havguard "...the lounge. It's out of control..."
        havguard "...water from upstairs or the whole place will go..."
        havguard "...through the wall and upstairs now..."
        $ player.face_worried()
        pcm "Fuck, this didn't go at all to plan."
        pcm "Gate is open but no way am I heading upstairs while the building is on fire..."
        havguard "...now! If you don't this will..."
        $ walk(loc_haven_lobby)
        show haven_smoke:
            alpha .7
        $ player.face_worried()
        hav "...will burn. Get it and go..."
        pcm "Shit shit shit shit."
        hav "...not gonna loose all my..."
        pcm "The fire was left alone for too long and has a grip on the building."
        "I hang around downstairs for some time hoping the fire can be brought under control and I can find a way to sneak upstairs."
        $ stroll(15)
        "But as time passes and the chaos around me continues, it is looking increasingly less likely that the fire will be brought under control."
        pcm "..."
        $ stroll(5)
        show haven_guard3 at right3:
            xzoom -1
        show haven_smoke:
            alpha .7
        with dissolve
        havguard "EVERYONE! Grab your stuff and get out of here."
        hav "What? There nothing we can do?"
        havguard "We have been doing what we could but it's too late. Whole place is going up."
        pcm "Fuck!"
        havguard "Grab your shit and get out or you will go with it."
        pcm "..."
        $ walk(loc_haven_exterior, trans=False)
        hide haven_smoke
        show haven_fire
        hide haven_guard3
        with dissolve
        $ player.face_shock()
        pcm "This did not go to plan at all..."
        if "intel_done" in main_quest_05.list:
            pc "Well, at least I got the info I needed on [ant.name]."
        elif "intel_mid" in main_quest_05.list:
            pc "At least [ant.name] wasn't planning to return here. But I still have no idea where he might be."
        elif "intel_first" in main_quest_05.list:
            pcm "At least I know [ant.name] wasn't in the building but I never managed to find out if he would return."
        else:
            pcm "Still no idea where [ant.name] is though. Hope he isn't still in the building."
        "I stand around with the rest of the [haven] residents aghast at what is going on in front of me."
        $ relax(60)
        "As time passes it becomes clear that this fire is not going to get dealt with anytime soon."
        "I notice in the distance a group of guards. Among the guards is someone dressed a lot nicer than the rest of them."
        pcm "That must be [alex.fname] [alex.sname]."
        if "intel_done" in main_quest_05.list:
            pcm "No point in disturbing him. I have what I came for so might as well just make my way out of here."
        else:

            pcm "Well, I suppose now is a chance to speak to him..."
            pcm "Ok, need to seem worried and find out where he is."
            $ player.face_cry()
            show haven_alex at right1
            show haven_guard3 at right3
            with dissolve
            pc "Sorry, but I am looking for someone and can't see them in the crowd. Do you know if they got out?"
            havguard "Who you lookin' for?"
            pc "I don't know his name. He is a doctor. Had some skin problem. I can't see him anywhere and I am afraid he was in there."
            havguard "I don't know any doctors round here."
            alex.nname "He wouldn't have been in there."
            pc "What? No, he might have been. He was supposed to be here."
            alex.nname "Look, I know it's hard for you girls to get treatment, but you should forget about him."
            alex.nname "He is a nutter who has no intention of helping you out and will probably do a lot more harm."
            pc "What? What do you mean?"
            alex.nname "He was using girls like you to test god knows what on them. Nothing good no doubt. So I kicked him out of here an' told him I'd kill him if he returns."
            alex.nname "So I know he's not in there."
            alex.nname "And don't go looking for him. Find someone else to deal with your baby or whatever."
            pc "..."
            pc "... Thanks..."
            alex.nname "Hrmf! Get going now."
            hide haven_alex
            hide haven_guard3
            with dissolve
            $ player.face_normal()
            pcm "Ok..."
            pcm "Kicked him out?"
            pcm "Well whatever. I have what I came for so might as well just make my way out of here."
        pause 0.5
        hide haven_fire
        $ walk(loc_highway, time_amount=15)
        pause 0.5
        jump haven_ending_leave_fire

label loc_haven_room1_set_fire:
    pcm "Right. Not too big. Need time to get out of here before anyone notices it."
    pcm "Ok, there we go. Now to get out of here."
    pause 0.5
    $ walk(loc_haven_hallway_1f)
    if haven_time_safe():
        havwhore "Hey! I saw that!"
        $ player.face_shock()
        pcm "Fuck fuck!"
        havwhore "FIRE!"
        pc "Wait, what? No..."
        havwhore "This one here. I saw her."
        show haven_guard3 at right1 with dissolve
        havguard "Fire is still small so you lot deal with that. I will sort this one out."
        jump haven_caught_and_beaten

    elif haven_time_danger():
        hav "Oi bitch! I saw what you just done!"
        $ player.face_shock()
        pcm "Fuck fuck!"
        hav "Hey, someone set a fire!"
        pc "Wait, what? No..."
        hav "This one here. I saw her."
        show haven_guard3 at right1 with dissolve
        havguard "Fire is still small so you lot deal with that. I will sort this one out."
        jump haven_caught_and_beaten

    elif haven_time_normal():
        pause 0.5
        $ walk(loc_haven_lobby)
        pause 0.5
        havmuff "FIRE!!"
        $ player.face_shock()
        pcm "Fuck, they noticed quicker than I expected..."
        pcm "Better get out of here."
        pause 0.5
        $ walk(loc_haven_landing)
        $ loc_haven_landing.dict["gate_open"] = True
        show haven_guard3 at right1
        havguard "You, come here."
        $ player.face_worried()
        pc "What? Why?"
        havguard "Didn't you hear the shouting? Follow me."
        pc "Huh?"
        havguard "Need more hands to put the fire out you dumb cunt. Now come on."
        pcm "Fuck. No choice..."
        pause 0.5
        $ walk(loc_haven_lobby)
        $ loc_haven_landing.dict["gate_open"] = False
        pause 0.5
        $ walk(loc_haven_hallway_1f)
        havguard "Where is it?"
        hav "Ah it was small so already dealt with. Bit o' stomping got rid of it."
        havguard "Right. How did it happen?"
        hav "No idea."
        havguard "..."
        havguard "Right... Okay then. Good job."
        hide haven_guard3 with dissolve
        pc "..."
        pcm "Well that didn't go to plan..."
        jump travel
    else:
        pause 0.5
        $ walk(loc_haven_lobby)
        pause 0.5
        $ walk(loc_haven_landing)
        pause 0.5
        $ walk(loc_haven_hallway_2f)
        havmuff "Fire!!"
        $ player.face_worried()
        pcm "Sounds like they spotted it."
        pcm "..."
        with hpunch
        pause 0.2
        with hpunch
        $ loc_haven_landing.dict["gate_open"] = True
        pcm "That sounded like the guard rushing off..."
        pcm "Let's see."
        pause 0.5
        $ walk(loc_haven_landing)
        pcm "YES!"
        pcm "Okay quickly."
        jump haven_access_top_floor

label loc_haven_room3_set_fire:
    pcm "Right. Not too big. Need time to get out of here before anyone notices it."
    pcm "Ok, there we go. Now to get out of here."
    if haven_guard_hours():
        show haven_guard1 with hpunch
    else:
        show haven_guard2 with hpunch
    $ player.face_shock()
    havguard "..."
    havguard "Thought I smelled something. The fuck are you doing?"
    pc "I... Ah..."
    havguard "No matter. Come here!"
    jump haven_caught_and_beaten

label loc_haven_room2_set_fire:
    if not haven_time_empty():
        pcm "People are in here. No way will I get away with setting a fire now."
        jump travel
    else:
        pcm "It's quiet now but someone might come at any moment so need to be quick."
        pcm "Ok, just make it look like a spark set it off or something..."
        pcm "There we go. Now to get out of here."
        pause 0.5
        $ walk(loc_haven_hallway_2f)
        pause 0.5
        $ walk(loc_haven_room3)
        pause 0.5
        pcm "Now just wait..."
        havmuff "Fire!!"
        pcm "Sounds like they spotted it."
        pcm "..."
        with hpunch
        pause 0.2
        with hpunch
        $ loc_haven_landing.dict["gate_open"] = True
        pcm "That sounded like the guard rushing off..."
        pcm "Quickly before he spots me."
        $ walk(loc_haven_hallway_2f)
        pause 0.5
        $ walk(loc_haven_landing)
        pcm "YES!"
        pcm "Okay quickly."
        jump haven_access_top_floor


label haven_set_fire_putout:
    $ remove_from_list(main_quest_05.list, "set_fire")
    havguard "Great, it's still small. Just stomp it out."
    pc "Ok."
    with vpunch
    pause 0.3
    with vpunch
    pause 0.3
    with vpunch
    havguard "Good, that will do the job. You, bring some water from the showers and bring it here. I will douse the area so it can't revive."
    hav "Ok."
    havguard "Good job. This should do it. The rest of you, either bring water or get out of here to make space."
    pcm "Ok, better get out of here..."
    $ walk(loc_from)
    pcm "..."
    pcm "Well that didn't go as planned. But at least I didn't get into trouble."
    pc "Not got any more fluid so can't be trying that again unless I can find some more. So better look for some other way to get upstairs."
    pc "*Sigh*"
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
