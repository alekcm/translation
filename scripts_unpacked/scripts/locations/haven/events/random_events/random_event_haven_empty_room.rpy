label random_event_haven_normal_1:
    show havman at right1 with dissolve
    hav "Ah, hello sweetheart."
    if player.confidence <=20:
        $ player.face_meek()
        pcm "..."
    else:
        pc "Err, hi."
    pcm "Better leave here."
    hide havman
    $ walk(loc_from)
    jump travel

label random_event_haven_normal_2:
    show havman at right1 with dissolve
    hav "Oh, what we got here?"
    $ player.face_worried()
    show haven_grope with dissolve
    hav "What's someone like you doing alone in here?"
    if player.confidence <= 20:
        $ player.face_meek()
        pc "Nothing."
    else:
        pc "That's my business."
    hide haven_grope with dissolve
    "I go to walk away and the guy makes no attempt to stop me leaving, and in fact moves a bit out of my way as I move."
    hide havman
    $ walk(loc_from)
    pause 0.5
    pcm "Too many weirdos in this place."
    jump travel

label random_event_haven_normal_3:
    show havman at right1 with dissolve
    $ player.face_worried()
    hav "Ah! Didn't expect someone else in 'ere."
    hide havman with dissolve
    $ player.face_normal()
    pcm "..."
    pcm "Strange."
    jump travel

label random_event_haven_normal_4:
    show havman at right1 with dissolve
    $ player.face_worried()
    hav "Huh, whacha doin' alone in 'ere?"
    if player.confidence <= 20:
        $ player.face_meek()
        pcm "..."
    else:

        pc "*Sigh*"
        pc "Not your business."
    hide havman
    $ walk(loc_from)
    pause 0.5
    jump travel

label random_event_haven_normal_5:
    show havman at right1 with dissolve
    $ player.face_worried()
    hav "Oooohhhhh!"
    hav "Saxxxxy girllll!"
    hide havman with hpunch
    "Stepping towards me, he trips on some uneven floorboards and faceplants right in front of me."
    pcm "Better not hang around here with that drunken fool."
    $ walk(loc_from)
    pause 0.5
    jump travel

label random_event_haven_normal_6:
    show havman at right1 with dissolve
    $ player.face_worried()
    hav "Oh hello sexy."
    show havman2 at right2 with dissolve
    hav "Whaa! Look where you are..."
    hide havman
    hide havman2
    with vpunch
    hav "Ahhh!"
    pcm "Sod hanging out here with these drunk idiots."
    $ walk(loc_from)
    jump travel

label random_event_haven_normal_7:
    havmuff "♪ Uwaaaaaaa Wooooooo Yeeaaaahhhhh ♪"
    $ player.face_worried()
    pcm "What the...?"
    havmuff "♪ ...on the way to the farm... ♪"
    pcm "Sounds like they passed this room."
    jump travel

label random_event_haven_normal_8:
    show havman at right1
    show havman2 at right3
    with dissolve
    hav "...and was trying to tell me that it would be tomorr... Ah hello luv, don't mind us."
    pc "No worries, was leaving anyway."
    hide havman
    hide havman2
    $ walk(loc_from)
    pause 0.5
    pcm "Shouldn't be hanging around in empty rooms while this place is so busy anyway."
    jump travel

label random_event_haven_normal_9:
    show havman at right1 with dissolve
    hav "Oooh look at that."
    show haven_grope grope with hpunch
    $ player.face_annoyed()
    pc "Ugh you stink!"
    hide haven_grope
    hide havman
    with hpunch
    "The drunk staggers back and lands on his arse on the floor."
    $ walk(loc_from)
    pause 0.5
    pcm "Drunk shit!"
    jump travel

label random_event_haven_normal_10:
    "Someone enters the room just after me while fishing a smoke from his pocket. He doesn't even pay me any mind and just sits on the floor."
    jump travel

label random_event_haven_normal_11:
    "A couple of guys enter just after me while talking to each other. They don't even notice me as they are too engrossed in their topic."
    jump travel

label random_event_haven_normal_12:
    show havman at right1 with hpunch
    if player.confidence <= 20:
        pc "Ehhh!"
    else:
        pc "Ah, watch it!"
    hav "Sorry luv."
    "He staggers off into the room barely managing to stay on his feet."
    hide havman with dissolve
    pcm "Probably find him in here later on the floor passed out..."
    jump travel

label random_event_haven_normal_13:
    show havman at right1 with dissolve
    hav "Ah 'ello luv."
    if player.confidence <= 20:
        $ player.face_meek()
    hide havman with dissolve
    "He heads out of the room and doesn't pay me any more attention."
    jump travel

label random_event_haven_normal_14:
    "Someone behind me starts entering the room, but as soon as he sees me he swiftly turns around and jog walks down the hallway."
    pcm "Odd..."
    jump travel

label random_event_haven_normal_15:
    "Someone speeds past the doorway running down the hallway shortly followed by someone else..."
    hav "... the fuck back here you cunt! When I..."
    pcm "..."
    pcm "Always trouble in this place."
    jump travel



label random_event_haven_force_1:
    show haven_grope
    show havman at right1
    with hpunch
    $ player.face_worried()
    pc "Ah! Fuck! What you doing sneaking up on people?"
    $ player.sex_forced(havenman, main_quest_05)
    show haven_grope grope with dissolve
    show haven_grope stern avoid with dissolve
    if player.confidence <= 20:
        $ player.face_meek()
    pc "What are you doing?"
    hav "Mmmm."
    if not player.check_nowill():
        pc "Get away from me!"
        if player.check_fight(3):
            hide haven_grope
            hide havman
            with hpunch
            "I shove against the guy and manage to push him off me."
            $ walk(loc_from)
            pause 0.5
            $ player.face_angry()
            pc "Fucking degenerate."
            $ player.face_normal()
            jump travel
        else:
            show haven_grope with hpunch
            "I push against the guy but aren't able to escape his embrace"

    hav "Such nice tits."
    $ player.add_mood(-10)
    pc "Let go of me!"
    if player.check_fight(3):
        hide haven_grope
        hide havman
        with hpunch
        "I shove against the guy and manage to push him off me."
        $ walk(loc_from)
        pause 0.5
        $ player.face_angry()
        pc "Fucking degenerate."
        $ player.face_normal()
        jump travel
    show haven_grope with hpunch
    hav "Stop fighting me!"
    hide haven_grope
    show haven_bentover at right
    with hpunch
    hav "The little bitch has such a perfect arse huh?"
    pc "Stop!"
    show haven_bentover mast with dissolve
    hav "Mmmmm."
    "He starts furiously masturbating and ogling my body, all the while pinning me down with his other arm and making it so I can't struggle free."
    show haven_bentover ah
    "I decide that since he has made no effort to take my shorts off, that it might be safer to just suffer it instead of struggling and risking him pushing things further."
    $ player.sex_cum(havenman,"ass", main_quest_05)
    hav "Ahhhhhh."
    pcm "Bastard!"
    if player.mood <= 20:
        $ player.face_cry()
        pc "*SOB*"
    hav "Sexy little bitch."
    show haven_bentover noman with dissolve
    hide havman
    show haven_bentover nomanfull with dissolve
    show haven_bentover sad with dissolve
    pcm "Did he leave?"
    hide haven_bentover with dissolve
    pcm "Fucking arsehole!"
    if player.mood <= 20:
        $ player.face_cry()
        pc "*SOB*"
    jump travel



label random_event_haven_drunk_1:
    show havman at right1 with dissolve
    hav "Whacha doing hanging round 'ere?"
    pc "What's it to you?"
    show haven_grope with dissolve
    hav "See a pretty girl hanging out alone round 'ere makes you think."
    pc "That's not something an idiot like you should be doing."
    hide haven_grope with hpunch
    "I shove the guy away, but in doing so I stagger over and end up bashing myself against the wall."
    hav "Here love, lemme help you. Been drinking?"
    pc "Don't need your help."
    hav "Come here."
    $ player.face_worried()
    show haven_bentover at right with dissolve
    pc "Ah what are you doing?"
    hav "Helping myself to some drunken pussy."
    pc "Get off!"
    $ player.sex_forced(havenman, main_quest_05)
    if player.check_fight(5):
        hide haven_bentover with hpunch
        "I manage to jump up and it feels like I might have cracked my head against his face. Either way I quickly head out of the room."
        $ walk(loc_from)
        havmuff "Bitch!"
        pcm "Yeah whatever."
        jump travel
    else:
        show haven_bentover with hpunch
        "I try to struggle against him but I am not strong enough, or just too drunk, to push him off of me."
        pc "Nnnnhg!"
        $ c.bottom = 0
        $ c.pants = 0
        show haven_bentover ah with vpunch
        pc "No no no!"
        pc "Let me go."
        show haven_bentover with hpunch
        hav "Don't worry love, I'll be gentle."
        show haven_bentover mast with dissolve
        hav "Such a nice arse. I'm gonna enjoy fucking you. Might even take that plug out and give your arse a fucking as well."
        pc "No no!"
        hav "You're right, better the pussy."
        show haven_bentover poke with dissolve
        pc "Ah fuck no take it away!"
        $ player.sex_vag(havenman, main_quest_05)
        $ player.face_cry()
        $ player.eye = 3
        show haven_bentover inside with dissolve
        pc "Ah you bastard!"
        hav "Ah fuck yes! So nice."
        hav "And this view. Nothing better than looking down on some drunk bitch and watching her take your cock."
        pc "*SOB*"
        "I lay there crying from the pain as he rocks me from behind. I don't pay much attention to what he is doing or saying and just hope for it to be over soon."
        "The one saving grace is that he is true to his word and is fairly gentle and doesn't do anything rough, other than making sure my arms are pinned."
        $ player.sex_cum(havenman, "inside", main_quest_05)
        pc "*SOB*"
        hav "Haaaa yes. Been ages since I have fucked someone as pretty as you. I won't be forgetting you anytime soon."
        show haven_bentover poke with dissolve
        show haven_bentover noman with dissolve
        show haven_bentover nomanfull
        hide havman
        with dissolve
        pc "*SOB*"
        "I lay crying and hoping what just happened was a dream. But of course I know it wasn't."
        "Eventually I come to mt senses and get myself fixed up before someone else walks in and sees a bent over naked girl and decides to also have a turn."
        hide haven_bentover with dissolve
        pcm "Fuck..."
        $ pc_dress()
        pcm "Scum!"
        pc "*SOB*"
        jump travel

label random_event_haven_drunk_2:
    show havman at right1 with dissolve
    hav "Ah, hi..."
    hav "Someone been hitting the brew a bit hard?"
    pause 0.5
    hide havman
    $ walk(loc_from)
    pause 0.5
    pcm "Can't trust anyone round here."
    jump travel

label random_event_haven_drunk_3:
    show havman at right1 with dissolve
    hav "Hmm, what we got 'ere. Been knocking 'em back?"
    pcm "*Sigh*"
    hav "Wait hold on. I got some brew if you have some cigs. 2 packs for a jar?"
    if inv.qty(item_cigs):
        menu:
            "Ok, sounds good":
                hav "Fucking yes. Been dying for a smoke. Here."
                $ inv.drop(item_cigs, 2)
                $ inv.take(item_brew)
                pc "Cheers."
                pcm "Still, better get out of here before he gets any ideas."
            "No thanks":
                pc "Sorry, not got any."

    pause 0.5
    hide havman
    $ walk(loc_from)
    pause 0.5
    pcm "Can't trust anyone round here."
    jump travel

label random_event_haven_drunk_4:
    with hpunch
    pc "Ugh, move out the way you damn doorframe!"
    jump travel

label random_event_haven_drunk_5:
    with vpunch
    pc "Ouch!"
    pcm "Damn floorboards are a death trap!"
    jump travel

label random_event_haven_drunk_6:
    with hpunch
    "I walk directly into some guy who was coming into the room."
    hav "Careful luv."
    pc "Sorry, sorry..."
    jump travel

label random_event_haven_drunk_7:
    pcm "*Phew* These brews really do have a kick to them."
    jump travel

label random_event_haven_drunk_8:
    pcm "♪ I said maaaaaybeeeeeee... ♪"
    pcm "♪ I don't really wanna know! ♪"
    pcm "♪ How ya garden grows! ♪"
    jump travel

label random_event_haven_drunk_9:
    pc "Ub!"
    with hpunch
    pcm "Careful... Careful... These feet are a deathtrap."
    jump travel



label random_event_haven_sex_1:
    show havman at right1 with hpunch
    $ player.face_worried()
    pc "Ah!"
    hav "Watch where ya going luv."
    if player.check_nowill():
        $ player.face_meek()
        pc "Sorry."
    else:
        pc "Sorry, mind moving?"
    hav "Hmm."
    hav "Show us ya tits first."
    if player.has_perk(perk_exhibitionist, notif=True):
        $ player.face_happy()
        pc "Sure."
        jump random_event_haven_sex_1_show
    pc "Let me past."
    hav "Tits."
    if player.check_drunk(4) or player.check_nowill():
        jump random_event_haven_sex_1_show
    elif player.confidence >= 60:
        jump random_event_haven_sex_1_refuse
    else:
        menu:
            "Show him":
                jump random_event_haven_sex_1_show
            "Refuse":
                jump random_event_haven_sex_1_refuse

label random_event_haven_sex_1_show:
    pcm "..."
    $ c.top = 0
    pause 0.5
    hav "Whooo! Nice!"
    pcm "..."
    "He moves out of the way of the door with a stupid grin on his face."
    hide havman with dissolve
    pcm "Arsehole."
    $ pc_dress()
    pause 0.5
    jump travel

label random_event_haven_sex_1_refuse:
    pc "No, now get out of the way."
    "I try to shove past the guy and get out of the room."
    if player.check_fight(3):
        with vpunch
        hide havman
        hav "Woah."
        if loc_cur == loc_haven_room1:
            $ walk(loc_haven_hallway_1f)
        else:
            $ walk(loc_haven_hallway_2f)
        $ player.face_angry()
        pc "Arsehole!"
        jump random_event_leaving
    else:
        show havman with vpunch
        hav "Woah. What do you think you doin?"
        hav "Show down bitch!"
        show haven_grope grope stern with vpunch
        $ player.sex_forced(havenman, main_quest_05)
        hav "Didn't hafta be all nasty about it."
        pc "Please, leave me alone."
        hav "..."
        if haven_time_empty() or haven_time_danger():
            $ randomnum = renpy.random.randint(1, 10)
            if randomnum == 1:
                jump random_event_haven_sex_1_forced
        hav "*Tsk*"
        hide haven_grope with dissolve
        hav "Next time don't be such a bitch about it. Jus tryna have fun."
        hide havman with dissolve
        pcm "Arsehole!"
        pcm "Better get out of here in case more trouble comes in."
        jump travel

label random_event_haven_sex_1_forced:
    hav "Maybe, after some fun."
    hide haven_grope with hpunch
    "He grabs me and tries to pin my hands behind my back. Realising where this is going I start to struggle."
    if player.check_fight(4):
        "I manage to slip out of his grasp and rush to the door to escape the empty room"
        if loc_cur == loc_haven_room1:
            $ walk(loc_haven_hallway_1f)
            pcm "Fuck! Bedroom, he won't carry on in there."
            $ walk(loc_haven_bedroom)
            pcm "..."
            pcm "That almost turned nasty. I need to hurry and get out of here."
            jump travel
        else:
            $ walk(loc_haven_hallway_2f)
            pcm "Fuck! Need to go to the landing, he won't mess about with the gate guard there."
            $ walk(loc_haven_landing)
            pcm "..."
            pcm "That almost turned nasty. I need to hurry and get out of here."
            jump travel
    else:
        show haven_bentover at right with hpunch
        pc "Ah!"
        pc "Stop, please!"
        hav "Too late for that darlin."
        $ c.bottom = 0
        $ c.pants = 0
        show haven_bentover with vpunch
        pc "Fuck no! What are you doing?!"
        hav "Wouldn't show me yer tits so gonna take a piece of ass instead."
        show haven_bentover poke with dissolve
        $ player.sex_vag(havenman, main_quest_05)
        show haven_bentover inside ah with dissolve
        $ player.face_cry()
        pc "Ah fuck no no no no!"
        hav "Ah fuck yes!"
        "He relentlessly fucks me while keeping a good grip of my arms. I try to struggle but he has too tough a grip. Eventually I give up resisting and just hope for it to be over quickly."
        pc "*SOB*"
        pcm "How did this happen? All because I wouldn't flash him...?"
        pc "*SOB*"
        pcm "This is too much. I want out of this shithole. It is nothing but trouble."
        if player.virgin_pregcheck:
            pcm "Having this arsehole take my virginity like this..."
            pc "*SOB*"
        else:

            if main_quest_05.rape > 5:
                pcm "Can't even count how many of these shits have raped me while I have been in this place. Everywhere I go some cunt is forcing themselves on me..."
            elif main_quest_05.rape > 1:
                pcm "Not even the first time some cunt in this place is forcing themselves onto me..."
        pc "*SOB*"
        $ player.sex_cum(havenman,"inside", main_quest_05)
        $ player.face_cry()
        hav "Ahhhhh yes!"
        if not player.has_perk(perk_preg_want):
            pc "Not inside..."
        pc "*SOB*"
        hav "Haaaaa. Hope you enjoyed yourself bitch."
        pc "..."
        show haven_bentover poke with dissolve
        show haven_bentover noman with dissolve
        hav "Next time, show a little love and I won't have to take it."
        show haven_bentover nomanfull with dissolve
        pc "..."
        pc "*SOB*"
        hide haven_bentover with dissolve
        pc "Fuck this place."
        $ pc_dress()
        pause 0.5
        if not loc_cur == loc_haven_room1:
            pause 0.5
            $ walk(loc_haven_hallway_2f)
            pause 0.5
            $ walk(loc_haven_landing)
            pause 0.5
            $ walk(loc_haven_lobby)
        pause 0.5
        $ walk(loc_haven_hallway_1f)
        pause 0.5
        $ walk(loc_haven_bedroom)
        pause 0.5
        $ walk(loc_haven_bed)
        pause 0.5
        jump haven_bed_sleep

label random_event_haven_sex_2:
    show havman at right1 with dissolve
    hav "Hey."
    $ player.face_worried()
    pc "Hi"
    pcm "Better get out of here."
    hav "Hold on, want some brew? I have some extra jars."
    if player.check_drunk(2) or (inv.qty(item_brew) < 2 and havenvik.has_met):
        $ player.face_normal()
        pc "Brew?"
        hav "Yeah, show me ya tits and you can have these 2 jars."
        if player.has_perk(perk_exhibitionist, notif=True):
            pc "Sure."
            $ c.top = 0
            pc "You like?"
            hav "Nice!"
            hav "Pierced nipples as well. Mmmm."
            show haven_pose1 with dissolve
            pc "Take your time."
            hav "Mmm, I will."
            pc "Wanna see my arse as well?"
            hav "You're enjoying this aren't ya?"
            $ c.bottom = 0
            $ c.pants = 0
            pc "Maybe."
            hav "Not gonna complain. Weird bitches in this place."
            pc "Mmm."
            if player.has_perk(perk_sucu, notif=True):
                pc "Wanna go to my bunk and have more fun?"
                hav "Fuck I am already hard. Sure."
                hide haven_pose1 with dissolve
                jump haven_sex_repeatable_start
            elif player.has_perk([perk_slut], notif=True):
                pcm "Maybe I can take him somewhere and have more fun."
                menu:
                    "Offer to go somewhere else":
                        pc "Wanna go to my bunk and have more fun?"
                        hav "Fuck I am already hard. Sure."
                        hide haven_pose1 with dissolve
                        jump haven_sex_repeatable_start
                    "Don't offer":
                        $ NullAction()
            pc "Ok, think that's more than enough for the jars. Hand 'em over."
            hav "Well worth it."
            $ inv.take(item_brew, 2)
            pc "Mmm."
            hide haven_pose1 with dissolve
            $ pc_dress()
            pause 0.5
            hide havman
            pause 0.5
            if havenvik.has_met:
                pcm "Nice, that was cheaper than that bastard [havenvik.name] will make me pay."
            jump travel


        pc "..."
        menu:
            "Show him":
                pc "*Sigh*"
                $ c.top = 0
                pc "..."
                hav "Nice!"
                hav "Pierced nipples as well. Mmmm."
                pc "Jars?"
                hav "Sure, but let me enjoy a bit more."
                pc "..."
                hav "Here. Enjoy them."
                $ inv.take(item_brew, 2)
                pc "Mmm."
                $ pc_dress()
                pause 0.5
                hide havman
                pause 0.5
                if havenvik.has_met:
                    pcm "Nice, that was cheaper than that bastard [havenvik.name] will make me pay."
                jump travel
            "Leave":


                $ NullAction()
    hide havman
    $ walk(loc_from)
    pcm "..."
    jump travel

label random_event_haven_sex_3:
    "Someone enters the room, sees me me and walks straight up to me."
    show haven_grope grope at right3 with hpunch:
        xzoom -1
    $ player.sex_forced(havenman, main_quest_05)
    pc "Hey! The fuck?!"
    hav "Shut up!"
    if player.check_nowill():
        "I stand there like a deer in headlights not knowing what to do. Too afraid to resist the guy in case he pushes things further."
        hide haven_grope
        show haven_blow ah wait
        with vpunch
        "Eventually he puts his hands on my shoulders and pushes me down"
        pc "Hey!"
        hav "Be quiet."
        show haven_blow neutral
        pc "..."
        if player.check_sex_agree(4):
            pc "*Sigh*"
            $ player.sex_oral(havenman, main_quest_05)
            show haven_blow cum with dissolve
            show haven_blow 1h with dissolve
            pcm "Get this over with before he tries to stick it in me..."
            hav "Fuck!"
            hav "Ahh fuck didn't expect that. Fucking quality slut!"
            pcm "Idiot!"
            pc "*Hyuk* *Hyuk* *Hyuk*"
            show haven_blow 2h with dissolve
            hav "Ahhh yes good girl!"
            hav "Fuck yes!"
            $ player.sex_cum(nosex,"mouth", main_quest_05)
            hav "Haaa yes! Fuck!"
            hav "Ahhhhhh."
            show haven_blow wait ub with dissolve
            show haven_blow neutral with dissolve
            pc "Can I go now?"
            hav "*Pheew*"
            hav "Huh?"
            hide haven_blow with dissolve
            "I get off my knees and start walking out the room. The guy does nothing to stop me."
            hide havman
            $ walk(loc_from)
            pcm "*Sigh* I hate this place."
            pcm "Got to suck some idiots cock in case they try to fuck me instead..."
            jump travel
        else:

            hav "Gonna put it all over your face. Girls like you deserve nothing less."
            pcm "Fuck."
            pcm "Better be quiet in case he wants to put it somewhere else..."
            "I stay on my knees just looking at him stroking his cock, not knowing what else to do. I don't really pay attention to what he is saying, although the words \"Whore\" and \"Slut\" seem to come up a lot."
            pcm "Why is he harassing me for this. Idiot can just do this in his bunk..."
            pcm "Better not tell him that though. He will push for more if he realises."
            $ player.sex_cum(nosex,"face", main_quest_05)
            pc "Ahhh!"
            hav "Haaaaa. Ahhhhhhhh!"
            pc "*Bleh*"
            pcm "Ah shit, my eye stings!"
            pc "..."
            pc "Can I go now?"
            hav "*Pheew*"
            hav "Huh?"
            hide haven_blow with dissolve
            "I get off my knees and start walking out the room. The guy does nothing to stop me."
            hide havman
            $ walk(loc_from)
            pcm "*Sigh* I hate this place."
            pcm "Got to take it in the face in case they try to fuck me instead..."
            jump travel
    else:

        hide haven_grope with hpunch
        "I shove past the guy and he doesn't make much of an attempt to stop me."
        hide havman
        $ walk(loc_from)
        pcm "Fuck."
        jump travel

label random_event_haven_sex_4:
    hav "Ahhh whadda we av here? A princess all for me?"
    pcm "Drunk fuck. Better get out of here."
    show haven_grope with hpunch
    $ player.sex_forced(havenman, main_quest_05)
    hav "Gotta catch 'em or they will escape."
    pc "Get off!"
    show haven_grope stern with hpunch
    if player.check_fight(3):
        hide haven_grope
        hav "Woah..."
        $ walk(loc_from)
        pcm "Fuck."
        jump travel
    hav "Woah, wriggling like a worm."
    show haven_grope grope with dissolve
    hav "Have to beat them to stop em sometimes."
    pcm "What? Beat them? Fuck! Is he going to..."
    $ player.punch()
    pc "Ah fuck! OW!"
    hav "Keep them calm."
    pcm "Fuck! This guy is a nut job!"
    hav "Only these should wiggle wiggle."
    pcm "What the hell do I do?"
    "He starts to try and kiss me. Without thinking I pull my face back and try to push him away."
    show haven_grope with hpunch
    if player.check_fight(3):
        hide haven_grope
        hav "Woah..."
        $ walk(loc_from)
        pcm "Fuck."
        jump travel
    hav "Little worms shouldn't wriggle!"
    hide haven_grope
    $ player.punch()
    pc "Ah fuck that hurts!"
    "He grabs me and pulls me over to some boxes and tries to force me over them"
    show haven_bentover at right with hpunch
    pc "Ah no stop!"
    hav "Lovely little princess will have to play."
    "Another swift punch to my ribs blows the air from me."
    show haven_bentover ah
    $ player.punch()
    pc "Agg! Ahh stop please!"
    pc "*SOB*"
    hav "Let us play little princess. Wiggling is only for worms."
    pc "Sure yes. Play. Stop punching me!"
    hav "Good princess."
    $ c.bottom = 0
    $ c.pants = 0
    show haven_bentover with hpunch
    pc "No no no not this!"
    hav "Be quiet little worm. We are playing."
    pcm "Fuck, what do I do?"
    if not player.check_nowill():
        menu:
            "Struggle and run":
                pc "Nnnng."
                show haven_bentover with hpunch
                if player.check_fight(3):
                    hide haven_bentover
                    pcm "Run, run!"
                    if player.check_fight(3):
                        if loc_cur == loc_haven_room1:
                            $ walk(loc_haven_hallway_1f)
                            pcm "Bedroom, he won't carry on in there."
                            $ walk(loc_haven_bedroom)
                            pcm "..."
                        else:
                            $ walk(loc_haven_hallway_2f)
                            pcm "Need to go to the landing, he won't mess about with the gate guard there."
                            $ walk(loc_haven_landing)
                            pcm "..."

                        pcm "He didn't follow me... Did he?"
                        pcm "... ..."
                        pcm "..."
                        pcm "Looks like he didn't"
                        pc "*Phew*"
                        pcm "Almost fell on my face with these shorts wrapped round my legs."
                        $ pc_dress()
                        pcm "Fuck, what a messed up freak."
                        pc "*Sigh*"
                        jump travel
                    else:
                        "I start to run for the door, but my shorts that are still wrapped around my legs trip me up and I faceplant on the floor."
                        $ player.punch()
                        pc "Fuck!"
                        "I hear the lumbering footsteps coming up behind me and..."
                        show screen blackout_screen
                        jump random_event_haven_sex_4_wake
                else:


                    hav "Wiggle worms don't learn?"
                    $ player.punch()
                    pc "Uuug!"
                    $ player.punch()
                    pc "Ahhh! Stop plea..."
                    $ player.punch()
                    pc "Uuug!"
                    show screen blackout_screen with dissolve
                    jump random_event_haven_sex_4_wake
            "Keep quiet":

                $ NullAction()
    pcm "This guy is messed up. I better not provoke him more or I might never leave this place..."
    show haven_bentover mast with dissolve
    hav "Good little worm will play."
    pcm "..."
    show haven_bentover poke with dissolve
    hav "Good good. Stay good."
    pcm "..."
    $ player.sex_vag(havenman, main_quest_05)
    show haven_bentover inside with dissolve
    hav "Ooh she is a princess. Or not a princess."
    show haven_bentover sleep
    pcm "Fucking messed up lunatic."
    pcm "Just lay here and hope he doesn't want to hit me anymore..."
    $ player.sex_cum(havenman,"inside", main_quest_05)
    hav "Ahhhhhhh!"
    pcm "Is he done already."
    show haven_bentover ah
    $ player.punch()
    hav "Little worm made it go away!"

    pc "Ow fuck stop!"
    show haven_bentover poke with dissolve
    show haven_bentover noman with dissolve
    $ player.punch()
    hav "Stupid worm!"
    $ player.punch()

    pc "Ugg!"
    show haven_bentover nomanfull with dissolve
    pcm "Fuck!"
    "I hear him lumbering around the room muttering something I don't understand. I just stay there keeping quiet and hoping he doesn't turn on me again."
    "Until eventually I hear him leaving the room."
    hide haven_bentover with dissolve
    pcm "Better get out of here before he comes back."
    $ pc_dress()
    pause 0.5
    if loc_cur == loc_haven_room1:
        $ walk(loc_haven_hallway_1f)
        pcm "Bedroom, should be safe in there with other people."
        $ walk(loc_haven_bedroom)
        pcm "..."
    else:
        $ walk(loc_haven_hallway_2f)
        pcm "Need to go to the landing, if he causes trouble there then hopefully the guard will deal with him."
        $ walk(loc_haven_landing)
        pcm "..."
    pcm "What a messed up shit!"
    pcm "Fuck I am all sore everywhere..."
    pcm "*Sigh* This place is going to kill me if I don't leave soon."
    jump travel

label random_event_haven_sex_4_wake:
    $ player.sex_forced(havenman, main_quest_05)
    $ player.sex_vag(havenman, main_quest_05)
    $ player.sex_cum(havenman, "inside", main_quest_05)
    hide screen cum_action
    $ time_sleep(120)
    $ c.top = 0
    $ c.bottom = 0
    $ c.pants = 0
    $ bruise.belly = 4
    $ bruise.face = 4
    $ bruise.chest = 4
    hide haven_bentover
    pause 1
    $ player.eye = 3
    $ player.mouth = 8
    hide screen blackout_screen with dissolve
    pc "Uhhhhhh."
    $ player.face_pain()
    pc "Ow ow ow!"
    pc "Ah fuck!"
    $ player.eye = 4
    $ player.mouth = 8
    pcm "What the fuck did I do to deserve that?"
    pcm "Fucked up monsters in this place..."
    $ pc_dress()
    $ c.top = 0
    $ player.face_pain()
    pc "Ow ow."
    pcm "Feels like I have been run over by a train."
    $ pc_dress()
    $ player.face_puke()
    pc "*Ub*"
    $ player.face_puke2()
    pc "*Bleh*"
    $ player.face_worried()
    pc "*Cough*"
    $ player.face_normal()
    pcm "Fuck!"
    pcm "I should lay down..."
    pause 0.5
    if not loc_cur == loc_haven_room1:
        pause 0.5
        $ walk(loc_haven_hallway_2f)
        pause 0.5
        $ walk(loc_haven_landing)
        pause 0.5
        $ walk(loc_haven_lobby)
    pause 0.5
    $ walk(loc_haven_hallway_1f)
    pause 0.5
    $ walk(loc_haven_bedroom)
    pause 0.5
    $ walk(loc_haven_bed)
    pause 0.5
    jump haven_bed_sleep

label random_event_leaving:
    if loc_cur in (loc_haven_room1, loc_haven_bedroom):
        $ walk(loc_haven_hallway_1f)
    elif loc_cur == loc_haven_storage:
        $ walk(loc_haven_lounge)
    else:
        $ walk(loc_haven_hallway_2f)
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
