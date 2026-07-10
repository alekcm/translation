label random_event_picker_haven_shower_tombola:

    $ rand_choice = WeightedChoice([
    ("random_event_haven_shower_1", 100),
    ("random_event_haven_shower_2", 100),
    ("random_event_haven_shower_3", 100),
    ("random_event_haven_shower_4", 100),
    ("random_event_haven_shower_5", 100),
    ("random_event_haven_shower_6", 100),
    ("random_event_haven_shower_7", If (player.drunk > 60, 100,0)),
    ("random_event_haven_shower_8", If (player.drunk > 60, 100,0)),
    ("random_event_haven_shower_9", 100),
    ("random_event_haven_shower_10", 100),
    ("random_event_haven_shower_11", 100),

    ("random_event_none", haven_random_event_noevent_weight()),
    ])

    if rand_choice == "random_event_none" or not haven_random_event_can_trigger() or not renpy.has_label(rand_choice):
        jump travel
    else:

        jump expression rand_choice

label random_event_picker_haven_shower_tombola_call:

    $ rand_choice = WeightedChoice([
    ("random_event_haven_shower_1", 100),
    ("random_event_haven_shower_2", 100),
    ("random_event_haven_shower_3", 100),
    ("random_event_haven_shower_4", 100),
    ("random_event_haven_shower_5", 100),
    ("random_event_haven_shower_6", 100),
    ("random_event_haven_shower_7", If (player.drunk > 60, 100,0)),
    ("random_event_haven_shower_8", If (player.drunk > 60, 100,0)),
    ("random_event_haven_shower_9", 100),
    ("random_event_haven_shower_10", 100),
    ("random_event_haven_shower_11", 100),

    ("random_event_none", haven_random_event_noevent_weight()),
    ])

    if rand_choice == "random_event_none" or not haven_random_event_can_trigger() or not renpy.has_label(rand_choice):
        return
    else:

        jump expression rand_choice


label random_event_haven_shower_1:
    "I notice a man in one of the opposite shower stalls doing something."
    pcm "Huh, is that what I think it is?"
    show haven_corner man_mast mast with dissolve
    pcm "Yes, yes is..."
    if player.desire >= 80:
        $ player.face_shy()
        pcm "..."
        pcm "Errm..."
        pcm "*Phew*"
        $ player.add_mood(2)
    else:
        pcm "Okaaaay."
    $ player.add_desire_random(5)
    $ player.add_mood(4)
    hide haven_corner with dissolve
    jump travel

label random_event_haven_shower_2:
    show haven_corner stand_facing with dissolve
    hav "Don't mind me."
    pc "What? Get out of here."
    hav "Shhhhh. Look over there. Can you see him?"
    show haven_corner avoid with dissolve
    pc "..."
    show haven_corner forward with dissolve
    pc "Angry looking man who seems to be looking for you?"
    hav "Yes."
    pc "Ok...?"
    hav "Let me stay here for a bit."
    pc "..."
    pc "*Sigh* Touch me and I will scream."
    hav "Sure, no problem."
    "I stand in silence for a few minutes and the man in front of me makes no attempt to do anything that would upset me and just looks directly at the wall behind me."
    "Eventually I see the angry looking guy leaving the showers."
    pc "Looks like he's gone."
    hav "You sure?"
    pc "I'm sure he left the showers. Might still be waiting outside to kick your arse."
    hav "Mmm..."
    hav "Thanks."
    $ randomnum = renpy.random.randint(1, 10)
    if randomnum == 1:
        hav "Nice tits by the way."
        pc "*Pfft*"
    show haven_corner stand_facing_alone with dissolve
    pcm "..."
    pcm "Wonder why he was hiding from him?"
    hide haven_corner with dissolve
    jump travel

label random_event_haven_shower_3:
    show haven_corner stand_facing with dissolve
    pc "Hey!"
    hav "I have 4 jars of brew and 2 packs of cigs."
    pc "Good for you. Now go away."
    hav "All you have to do is turn around and I'll use my hand."
    pc "What? The hell you talking about."
    hav "Let me beat one out over your arse and I can pay 4 jars and 2 packs."
    if player.has_perk(perk_whore):
        pc "Ahh, right."
    elif player.has_perk(perk_slut):
        pc "Err, hmmm."
    else:
        pc "..."
    if player.has_perk(perk_sucu, notif=True):
        pc "Want to fuck instead?"
        hav "What?"
        pc "More fun if we have sex."
        hav "Err, I.. Errmm. Yes?"
        pc "Ok."
        show haven_corner stand_facingaway with dissolve
        hav "You... Sure?"
        pc "Hurry up and stick it in me."
        hav "..."
        show haven_corner penisup mast with dissolve
        pc "Mmmm..."
        hav "Fuck. Didn't expect this."
        pc "I bet."
        show haven_corner man_poke penispoke happy with dissolve
        $ player.sex_vag(havenman, main_quest_05)
        show haven_corner man_sex with dissolve
        hav "Ahhhhh!"
        hav "Fuuuuuu..."
        $ player.sex_cum(havenman, "inside", main_quest_05)
        show haven_corner neutral
        pc "Oh?"
        pcm "That was quick."
        hav "Nnnnng!"
        hav "*Huff* Huff*"
        pc "Ah well. Worth the price of the brews?"
        hav "Uhh huh."
        pc "Ok, so pay up."
        hav "Uuuhhhh."
        pcm "He turn retarded?"
        show haven_corner man_poke penispoke with dissolve
        show haven_corner stand_facingaway_alone with dissolve
        hide haven_corner with dissolve
        pc "Lead the way."
        hav "Huh?"
        pc "The brews and cigs."
        hav "Ahhh..."
        show havman at right1
        $ walk(loc_haven_shower)
        hav "'Ere yaare."
        $ inv.take(item_brew, 6)
        $ inv.take(item_cigs, 10)
        pc "Cheers."
        hide havman with dissolve
        pcm "..."
        pcm "Was way more than he offered."
        jump haven_shower_dress





    elif player.has_perk([perk_whore, perk_slut], notif=True) or player.check_sex_agree(5, exhibitionist=True):
        pcm "Hmmm, should I?"
        pc "Just wanking on my bum?"
        hav "Yeah, so you will do it?"
        show haven_corner mast penisup with dissolve
        pc "Hey not so fast!"
        menu:
            "Let him do it":
                pc "Don't go try poking me with it or something ok?"
                hav "Yeah ok."
                pc "Right."
                $ player.sex_sold(havenman, 0)
                show haven_corner stand_facingaway with dissolve
                pcm "Was this even worth it? Pretty cheap price."
                if havenvik.has_met:
                    pcm "Well, [havenvik.name] would no doubt ask for more off me."
                pcm "Oh well, at least I am in the shower so can wash his cum off quickly."
                pcm "Can see him wanking off. Doesn't look like he will last very long. Probably been ages since he's had someone if these are the prices he's offering."
                pcm "Fuck! That makes me a pretty cheap whore..."
                show haven_corner man_grind with dissolve
                pcm "Huh?"
                pc "Hey, I told you don't try and go poking me."
                hav "Ahh, I'm not, I just wanna feel your nice arse."
                hav "Haaaa..."
                pcm "Ah well, seems like he's close anyway"
                pc "I feel that thing poking between my legs and we are done ok?"
                hav "Aaahhhhh."
                pcm "Hmm, seems we are pretty much done anyway."
                $ player.sex_cum(nosex, "ass")
                $ player.cum_clean()
                hav "Ahh yes. What a nice fucking arse!"
                pcm "Yeah shout louder so everyone knows you are in here with me."
                hav "Haaaa so nice."
                hav "Mmmmmmm."
                show haven_corner stand_facing with dissolve
                hav "Ah fuck that was so nice."
                pc "Mmm, glad you had fun. Now your end of the bargain?"
                hav "Sure. Let's go to the dressing room."
                hide haven_corner with dissolve
                pc "Lead the way."
                show havman at right1
                $ walk(loc_haven_shower)
                hav "Here you go."
                $ inv.take(item_brew, 4)
                $ inv.take(item_cigs, 2)
                pc "Cheers."
                hide havman with dissolve
                jump haven_shower_dress
            "Refuse":

                pc "Sorry mate, you are gonna have to ask one of the other girls."
                hav "What? Really?"
                pc "Yeah, now go take your cock somewhere else."
                hav "*Sigh*"
                hav "Ok..."
                pc "..."
                pc "Go on then, get!"
                hav "Right right."
                show haven_corner stand_facing_alone with dissolve
                pc "..."
                pcm "Perverts."
                hide haven_corner with dissolve
                jump travel
    else:

        pc "No, go and find someone else."
        hav "Really?"
        pc "Of course really. Go away."
        hav "..."
        hav "Ok..."
        show haven_corner stand_facing_alone with dissolve
        pc "*Sigh*"
        pc "Not even safe in the showers..."
        hide haven_corner with dissolve
        jump travel

label random_event_haven_shower_4:
    havgirl "Ahhhhh!"
    $ player.face_worried()
    pcm "Huh?"
    havgirl "Fuck off you pervert!"
    pcm "What's going on? Someone sneak in on the girl?"
    pcm "..."
    pcm "Oh well."
    $ player.face_normal()
    jump travel

label random_event_haven_shower_5:
    show haven_corner man_grind ah with hpunch
    $ player.sex_forced(havenman)
    $ player.face_worried()
    pc "Ahhh!"
    show haven_corner tit with dissolve
    if player.confidence <= 20:
        pcm "What the hell. Fuck fuck fuck."
        show haven_corner man_poke with dissolve
        pcm "No no no, this isn't happening..."
        pc "No please no."
        hav "Shush."
        $ player.face_cry()
        pc "*SOB*"

    elif player.check_fight(4):
        pc "Get off me!"
        hide haven_corner with hpunch
        "I manage to shove the guy off me and do a runner."
        $ walk(loc_haven_shower)
        pause 0.5
        pcm "Fucker!"
        jump haven_shower_dress
    else:
        pc "Get off me!"
        show haven_corner man_poke with hpunch
        "I wrestle against the guy but he has a good grip around my body and pushing against him ends up putting his cock in an awkward position."
        pcm "No no no, this isn't happening..."
        pc "No stop this."
        hav "Shush."
        $ player.face_cry()
        pc "*SOB*"
    pcm "Fuck no. This can't be happening."
    show haven_corner penispoke with dissolve
    if player.confidence <= 20:
        pc "Please don't put it in..."
    else:
        pc "Don't you dare!"
    hav "Don't worry little girl, I will be quick."
    pc "No no no..."
    $ player.sex_vag(havenman)
    show haven_corner man_sex facewall with dissolve
    $ player.face_cry()
    pc "Ah fuck!"
    pcm "No no no *SOB*"
    hav "Ah fucking hell, so warm."
    hav "Not had a girl for years, and seeing your sexy arse in the shower, I just couldn't resist taking a piece."
    pcm "Arsehole!"
    pc "*SOB*"
    hav "Ahhhhh!"
    $ player.sex_cum(havenman,"inside")
    hav "Ah fucking yes. Hahaahaaaaaa..."
    hav "Fucking hell, that warm pussy took it right out of me."
    pc "*SOB*"
    show haven_corner man_poke penispoke with dissolve
    hav "Thanks love."
    pc "*Sniff*"
    show haven_corner stand_facingaway_alone with dissolve
    pcm "..."
    hide haven_corner with dissolve
    $ player.cum_clean()
    pcm "..."
    pcm "I fucking hate this place..."
    pcm "*SOB*"
    $ walk(loc_haven_shower)
    call haven_shower_dress_call from _call_haven_shower_dress_call
    $ walk(loc_haven_hallway_1f)
    pause 0.5
    $ walk(loc_haven_bedroom)
    pause 0.5
    $ walk(loc_haven_bed)
    pcm "I want to get out of here..."
    jump haven_bed_sleep

label random_event_haven_shower_6:
    havmuff "Please no."
    $ player.face_worried()
    pcm "Huh?"
    havmuff "*SOB* Please..."
    pcm "What's going on? Someone in there with a girl?"
    pcm "..."
    havmuff "*SOB*"
    pcm "Oh well."
    $ player.face_normal()
    jump travel

label random_event_haven_shower_7:
    $ player.face_happy()
    pc "♪ Please don't stop the music ♪"
    pc "♪ Wasn't looking for nobody when you look my way ♪"
    $ player.add_mood(3)
    jump travel

label random_event_haven_shower_8:
    $ player.face_happy()
    pc "♪ Want you to make me feel ♪"
    pc "♪ Like I'm the only girl in world ♪"
    $ player.add_mood(3)
    jump travel

label random_event_haven_shower_9:
    show haven_corner stand_facing with dissolve
    hav "Hey baby, not seen you around here before. Girl like you I would remember."
    menu:
        "Respond" if player.isslut or player.confidence >= 70 or player.check_sex_agree(4):
            pc "Yeah not long got here."
            show haven_corner grope with dissolve
            hav "Well, Would be happy to help a girl out as pretty as you."
            if player.iswhore:
                pc "Good for you. Now I'm gonna charge you if you keep touching my tits like that."
                hav "Ah, a whore?"
                pc "Any other kind of girl that lives here?"
                hav "..."
                show haven_corner stand_facing_alone with dissolve
                pc "Did he think he could develop some kind of romance in the shower or something?"
            else:
                pc "I'm sure you would. Does that include more than touching up my tits?"
                hav "Err, it can."
                pc "And I will just bend over and scream \"ravish me!\"?"
                hav "Errr..."
                pc "*Sigh*"
                pc "Did you really expect coming up to a naked girl in the shower would end that way?"
                hav "I... Just saw someone nice..."
                pc "Yeah, you and every arsehole in this place. I just want to clean myself. Leave the flirting for when I am not boxed in a corner butt naked."
                hav "..."
                hav "Sorry..."
                show haven_corner stand_facing_alone with dissolve
                pcm "..."
                pcm "He actually seemed a bit nicer than most of the people in this place."
        "Ignore":
            pc "Not interested."
            hav "C'mon girl, no need to be so cold."
            show haven_corner avoid with dissolve
            pc "..."
            hav "We can be nice together."
            show haven_corner push with dissolve
            pc "Not interested."
            hav "..."
            hav "Ok..."
            show haven_corner stand_facing_alone up forward with dissolve
            pcm "..."
    hide haven_corner with dissolve
    jump travel

label random_event_haven_shower_10:
    show haven_corner stand_facing with dissolve
    hav "Mind if I jump in 'ere with you, the others are full."
    if player.has_perk([perk_exhibitionist, perk_sucu], notif=True):
        show haven_corner happy
        pc "Sure."
        hav "Best! Don't wanna shower with some other sausage and the stalls are full."
        if player.has_perk(perk_sucu, notif=True):
            pc "Want help washing?"
            pc "Stupid question, of course you do."
            show haven_corner mastman penisup neutral with dissolve
            hav "Ah! Not gonna complain' 'bout that."
            pc "Mmmm, I bet."
            hav "Sure you don't mind if I return the favour."
            show haven_corner grope with dissolve
            pc "Nope."
            pc "In fact, why not help wash me somewhere else?"
            hav "Oh?"
            show haven_corner stand_facingaway with dissolve
            hav "Ooooh?"
            hav "I can do that."
            show haven_corner man_poke with dissolve
            pc "Mmmm."
            show haven_corner penispoke with dissolve
            hav "Didn't 'cpect this when a came in here."
            pc "I bet."
            $ player.sex_vag(havenman, main_quest_05)
            show haven_corner man_sex facewall with dissolve
            pc "Haaaaa!"
            pc "Fuck!"
            hav "Ahhh."
            show haven_corner back happy with dissolve
            pc "Mmm, keep going."
            hav "Ahh. Not done... This in ages..."
            hav "Not..."
            pc "Just do it inside me."
            hav "Haaaaaa..."
            $ player.sex_cum(havenman, "inside", main_quest_05)
            hav "Haaa fuck!"
            hav "Nnnngg!"
            pc "Mmmmm."
            show haven_corner man_poke penispoke with dissolve
            hav "Been ages. It didn't last long."
            pc "No worries. I got what I wanted."
            hav "Errm. I'm gonna..."
            pc "Sure. It was fun."
            hav "..."
            show haven_corner stand_facingaway_alone with dissolve
            hide haven_corner with dissolve
            jump travel

        elif player.has_perk(perk_exhibitionist, notif=True):
            pc "Whatever. Just no touching."
            show haven_corner gropeself neutral with dissolve
            "I stand there pretending to wash and look at the guy while doing so."
            show haven_corner penisup with dissolve
            pc "You know, you should at least pretend you came here for the shower."
            hav "Huh?"
            pc "Been staring at me the whole time and no attempt to wash."
            hav "Oh? Shit."
            pc "It's fine."
            hav "Yeah?"
            pc "Go on. Do what you want to do."
            hav "Oh?"
            show haven_corner grope with dissolve
            pc "Not touching me you idiot. Yourself."
            show haven_corner mandown with vpunch
            hav "Ah!"
            hav "It ok?"
            pc "Yeah, have fun."
            show haven_corner mast with dissolve
            pc "Mmm. Like what you see?"
            hav "Mmm. Sexy tits on a tiny body. And loves being watched."
            pc "Mmm, would let everyone watch if they would keep their hand to themselves."
            pc "I got a nice arse too."
            show haven_corner stand_facingaway with dissolve
            pc "Like it?"
            hav "Fuck!"
            $ player.sex_cum(nosex, "ass", main_quest_05)
            hav "Ahhhhh!"
            show haven_corner happy with dissolve
            pc "Oh? I guess you do like my arse."
            hav "Nnnnnngg..."
            hav "Haaaaa."
            pc "Have fun?"
            show haven_corner stand_facingaway_alone neutral with dissolve
            pcm "Err. Okay then..."
            hide haven_corner with dissolve
            jump travel

    pc "They are?"
    hav "Mmmm."
    pc "Hey wait, I do mind. Go hang out with someone else."
    hav "C'mon sweetheart, I don't wanna shower with some other guy."
    pc "Nor do I. Sod off."
    hav "..."
    show haven_corner stand_facing_alone with dissolve
    pcm "Thank fuck he left..."
    hide haven_corner with dissolve
    jump travel

label random_event_haven_shower_11:
    show haven_corner stand_facing with dissolve
    pc "..."
    hav "..."
    show haven_corner mast penisup avoid with dissolve
    pc "What the fuck?"
    hav "Mmmmm."
    if player.has_perk(perk_sucu, notif=True):
        show haven_corner forward with dissolve
        pc "*Tsk* Pervert!"
        show haven_corner stand_facingaway with dissolve
        hav "Oooh!"
        if numgen():
            show haven_corner man_grind penispoke with dissolve
            hav "Ah fuck!"
            pcm "Better inside I think..."
            show haven_corner man_sex with dissolve
            $ player.sex_vag(havenman, main_quest_05)
            "I press against him making sure he enters me, knowing he will cum at any moment."
            hav "Oooh! Fuckfuckfuckfuck!"
            pcm "Seems to perk me up longer when it's inside."
            hav "Ahhhmmmmm."
            $ player.sex_cum(havenman, "inside", main_quest_05)
            hav "Haaaaaarmmmmmmmmmmm..."
            hav "*Huff* *Huff*"
        else:
            show haven_corner man_grind with dissolve
            hav "Ah fuck!"
            "I grind my arse against his cock knowing he will cum at any moment."
            hav "Oooh! Fuckfuckfuckfuck!"
            hav "Ahhhmmmmm."
            $ player.sex_cum(havenman, "ass", main_quest_05)
            hav "Haaaaaarmmmmmmmmmmm..."
            hav "*Huff* *Huff*"
        pc "Now go away you pervert."
        pc "Go on, shoo!"
        show haven_corner stand_facingaway_alone with dissolve
        pc "..."
        hide haven_corner with dissolve
        jump travel

    elif not player.check_nowill():
        hide haven_corner with hpunch
        $ walk(loc_haven_shower)
        pcm "What the hell was that..."
        pcm "Damn pervert!"
        jump haven_shower_dress
    else:
        pc "Go away and do that you pervert!"
        hav "Ahhhmmmmm."
        show haven_corner with hpunch
        $ player.sex_cum(nosex, "stomach", main_quest_05)
        show haven_corner ah with dissolve
        pc "Ugh fuck!"
        pc "The hell?"
        show haven_corner push with dissolve
        pc "Get out of here!"
        show haven_corner stand_facing_alone forward neutral up with dissolve
        pc "Ugh..."
        $ player.cum_clean()
        pcm "Fuck this place..."
        hide haven_corner with dissolve
        jump travel

label random_event_haven_shower_12:
    show haven_corner stand_facing with dissolve
    pc "What do you think you ..."
    hav "How about this one?"
    havmuff "Yeah she'll do."
    havmuff "Take her before someone comes."
    pc "What?"
    hav "C'mere love."
    $ player.punch()
    show haven_corner ah
    pc "Ah! The fuck!!"
    show haven_corner push with vpunch
    if player.check_fight(3):
        hide haven_corner with hpunch
        $ walk(loc_haven_shower)
        havmuff "Fuck!"
        $ walk(loc_haven_hallway_1f)
        pc "HELP!!!"
        pc "Fuck..."
        pcm "They aren't coming..."
        show havguard1 at right1 with dissolve
        havguard "You the one shouting?"
        pc "Yeah. Some fuckers tried to drag me off in the showers."
        havguard "*Sigh* Degenerates..."
        havguard "Go grab your clothes, I'll keep an eye out."
        pc "Thanks..."
        hide havguard1
        call haven_shower_dress_call from _call_haven_shower_dress_call_3
        pause 0.5
        show havguard1 at right1
        $ walk(loc_haven_hallway_1f)
        havguard "You good?"
        pc "Yeah..."
        pc "Thanks."
        havguard "Mmmm. Stick to somewhere safer next time."
        hide havguard1 with dissolve
        pcm "No where is safe round here..."
        $ walk(loc_haven_bedroom)
        jump travel
    else:

        show screen blackout(50) with hpunch
        $ player.punch()
        pc "Ahhh!"
        $ player.punch()
        show screen blackout(100) with hpunch
        $ writing.add_writing("ass", "tattoo")
        $ walk(loc_haven_utilities, trans=False)
        jump random_event_haven_ko
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
