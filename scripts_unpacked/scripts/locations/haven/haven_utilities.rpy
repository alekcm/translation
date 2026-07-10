label haven_utilities_arrival_checks:
    if t.hour in irange(6,16):
        pcm "Should be safe to enter with all the girls around. Doubt any guys are going to be sneaking up on me."
    elif t.hour in (20,21,22,23):
        if player.isslut:
            pcm "If I head in there now, one of the guys will see me. But no idea if they will join..."
            jump haven_utilities_arrival_prompt
        else:
            pcm "If I head in there now, one of the guys will no doubt see me. No idea if they will try anything but should I be taking that chance?"
    else:

        pcm "Not really busy in here right now so I shouldn't be spotted going in."
    jump haven_utilities_arrival_prompt


label haven_utilities_arrival_prompt:
    menu:
        "Enter":
            $ walk(loc_haven_utilities)
            jump travel
        "Not right now":
            jump travel

label haven_utilities_join:
    if not renpy.showing("havman"):
        show havman at right1 with dissolve
    if not "joined" in loc_haven_utilities.dict:
        $ loc_haven_utilities.dict["joined"] = 0
    if loc_haven_utilities.dict["joined"] < 5:
        $ loc_haven_utilities.dict["joined"] += 1
        jump expression "haven_utilities_join_" + str(loc_haven_utilities.dict["joined"])
    else:

        jump expression WeightedChoice([
        ("haven_utilities_join_1", 10),
        ("haven_utilities_join_2", 10),
        ("haven_utilities_join_3", 10),
        ("haven_utilities_join_4", 5),
        ("haven_utilities_join_5", 3),
        ])

label haven_utilities_pry_join:
    show havman at right1 with dissolve
    hav "Thought I heard something odd in here."
    jump haven_utilities_join

label haven_utilities_join_1:
    hav "Huh? Whatcha doin' in 'ere?"
    $ player.face_worried()
    pcm "Fuck!"
    pc "Err, went in the wrong door..."
    show haven_corner stand_facing wall with dissolve
    hav "An come in 'ere all naked an alone?"
    pc "Move out my way."
    hav "I'm jus standin' here."
    hide haven_corner
    hide havman
    with dissolve
    "I push past him and head out of the room"
    $ walk(loc_haven_shower)
    pcm "Shit, almost ended up in trouble there..."
    pcm "I need to be more careful."
    jump haven_shower_dress

label haven_utilities_join_2:
    hav "What you doing in 'ere prancing around naked?"
    $ player.face_worried()
    pc "Err, I fell over."
    hav "I can see that. What you doin' naked in 'ere in the first place?"
    hav "Y'know, I don't much care."
    hav "Whores doing weird shit in weird rooms."
    hide havman with dissolve
    pc "..."
    $ player.face_normal()
    pc "*Phew*"
    pcm "I really should pick a better time for messing about in here."
    jump travel

label haven_utilities_join_3:
    hav "Oh what do we 'ave 'ere?"
    $ player.face_worried()
    show haven_corner stand_facing wall with dissolve
    hav "Wassa sexy little thing like you doin comin in ere? Looking for some fun?"
    show haven_corner grope with dissolve
    pc "Stop that! Get off me!"

    if player.check_fight(3):
        hide haven_corner with hpunch
        "I shove him off me and he stumbles a few steps back. Using this moment I quickly rush out of the room."
        hide havman
        $ walk(loc_haven_shower)
        pcm "..."
        pcm "These dirty shits. I am going to end up in trouble if I keep this up."
        jump haven_shower_dress
    else:
        show haven_corner push with hpunch
        "I try to shove him away but he hardly moves."
        hav "Whas your hurry?"
        show haven_corner avoid with dissolve
        pc "Stop touching me!"
        hav "You come in 'ere all naked and now act all coy? This your game or something?"
        pc "What?"
        hav "Gettin yourself inta trouble? It how you get your kicks?"
        show haven_corner finger with dissolve
        pc "No!"
        hav "Yeah whatever you say."
        show haven_corner forward with dissolve
        pc "Fuck you!"
        hav "Well whatever, there's the door."
        pc "..."
        if player.isslut and player.check_sex_agree(4):
            menu:
                "Leave quickly":
                    $ NullAction()
                "Keep standing here":

                    "I look at the exit then back to the guy cornering me."
                    show haven_corner avoid ah with dissolve
                    pc "I am too scared..."
                    hav "Oh I bet you are... Stuck in here with a big scary guy like me."
                    pc "Mmmmm."
                    hav "Be a shame if somethin' bad were ta happen."
                    show haven_corner forward with dissolve
                    pc "Oh no, please don't."
                    hav "C'mere!"
                    show haven_corner stand_facingaway facewall with dissolve
                    pc "What are you doing? This doesn't feel right."
                    hav "This is what you get for coming in 'ere all alone."
                    show haven_corner penisup mast with dissolve
                    hav "Girls like you should know better. An I'm gonna show you what happens to little girls who end up in the wrong place."
                    show haven_corner back with dissolve
                    pc "Sorry, I won't come in here again. I promise."
                    hav "Mmmm, I'll make sure of that."
                    pc "No please, don't do anything strange..."
                    hav "Shut up!"
                    pc "Eh?"
                    show haven_corner man_poke with dissolve
                    pc "Haaa? What are you doing?"
                    hav "Having fun with that sexy little arse of yours."
                    pc "Please don't, it feels funny..."
                    hav "That will probably be the plug in your arse making you feel funny. Only naughty girls do such things."
                    pc "Oh no! Does that mean you will punish me?"
                    hav "You're damn right I will."
                    pc "Oh no... What will happen to me?"
                    hav "First I'm gonna have some fun with these lovely tits of yours."
                    show haven_corner tit facewall with dissolve
                    pc "Ahhh nooo."
                    hav "Then when I have had my fun with them. I am going to slide my cock between your legs and I am going to fuck you until you tell me you will not be a bad girl anymore."
                    pc "I promise, I won't be bad anymore."
                    hav "Then I am going to cum deep in your pussy and have you milk me of every drop."
                    if player.has_perk(perk_preg_notwant):
                        show haven_corner back neutral with dissolve
                        pc "Seriously, cum in me and I will stab you in the eye. I am not getting knocked up."
                        hav "Err, then I am going to cum all over your sexy little arse and cover you with my seed."
                        show haven_corner facewall with dissolve
                    elif player.has_perk(perk_preg_want):
                        pc "Oh no! Then I will end up with your baby. You will make me all fat with big milk tits."
                        hav "Mmmm, good!"
                    elif player.cycle_conditions["stage"] == "ovulate":
                        show haven_corner back neutral with dissolve
                        pc "Seriously, better pull out. Right now is not a good time."
                        hav "Ok."
                        show haven_corner facewall with dissolve
                    pc "Ah no please..."
                    show haven_corner penispoke with dissolve
                    pc "Ahh no. I can feel you between my legs. Please don't do anything bad..."
                    hav "Shut up you sexy little slut. You have been too naughty!"
                    pc "I haven't, I swear!"
                    $ player.sex_vag(havenman, main_quest_05)

                    show haven_corner man_sex with dissolve
                    pc "Ahhh noooo! You bastard!"
                    hav "Haaa so nice and warm!"
                    pc "Ah fuck. You put your huge cock in me."
                    show haven_corner reach with dissolve
                    hav "Mmmmmm. Little sluts deserve a good punishment."
                    pc "Ah no. I am not a bad girl."
                    "Reaching round and grabbing my hips, he relentlessly fucks me while I flail around and try to \"resist\" him."
                    pc "Ah no this is too much."
                    hav "Shut up and take my cum!"
                    if player.has_perk(perk_preg_notwant) or (player.has_perk(perk_preg_want) == False and player.cycle_conditions["stage"] == "ovulate") or player.check_pullout():
                        show haven_corner stand_facingaway mast penisup with dissolve
                        hav "Ahhhhhhh"
                        $ player.sex_cum(havenman, "pullout")
                        "I feel his warm cum landing on my back and arse in time with his grunts."
                        hav "Ahhh yes you dirty girl."
                        show haven_corner back ah with dissolve
                        pc "Ahh, you are putting it all on me..."
                    else:
                        pc "Ah no, I don't have protection. Please pull out."
                        hav "Ahhhhhhh"
                        $ player.sex_cum(havenman, "inside")
                        "I feel his cock throbbing inside me as he pumps his seed deep inside."
                        hav "Ahhh yes you dirty girl."
                        show haven_corner back ah with dissolve
                        pc "Ah no, I asked you to pull out. I might end up pregnant..."
                        if player.has_perk(perk_preg_want):
                            pc "All fat and swollen with huge tits and a giant belly."

                    hav "Mmmmmmm."
                    pc "Haaa..."
                    show haven_corner stand_facingaway neutral with dissolve
                    hav "That was nice you dirty little girl."
                    pc "Mmmm."
                    show haven_corner stand_facing neutral with dissolve
                    if player.cum_locations["cum_vagin"]:
                        pc "Ok, better jump in the shower and wash your leaking cum out of me."
                    else:
                        pc "Ok, better jump in the shower and wash your cum off my arse."
                    hav "What? No goodbye?"
                    show haven_corner stand_facing penisup mastman happy with dissolve
                    pc "See you round little guy."
                    hide haven_corner with dissolve
                    hav "Little...?"
                    pcm "Heh."
                    hide havman
                    jump haven_shower_stall_arrival


    hide haven_corner with dissolve
    "Before he changes his mind, I quickly head towards the door and the guy does nothing to stop me."
    hide havman
    $ walk(loc_haven_shower)
    pcm "..."
    pcm "These dirty shits. I am going to end up in trouble if I keep this up."
    jump haven_shower_dress

label haven_utilities_join_4:
    "I notice someone opening the door and coming inside."
    $ player.face_worried()
    pcm "Better get out of here."
    show haven_corner stand_facing wall with hpunch
    hav "What's the hurry sweet thing? Stay a while and we can have some fun."
    show haven_corner grope with dissolve
    pc "Ah."
    hav "Mmmm, such a tasty little thing. Wonder if your pussy is just as sweet."
    show haven_corner finger with dissolve
    pc "Move!"
    show haven_corner push with vpunch
    if player.check_fight(3):
        hide haven_corner
        hide havman
        with hpunch
        "I shove him out the way and quickly head out the door."
        $ walk(loc_haven_shower)
        pcm "Good, got out of there with no trouble."
        jump haven_shower_dress
    else:
        $ player.sex_forced(havenman, main_quest_05)
        show haven_corner stand_facingaway facewall holdarm with hpunch
        "I shove him out of the way but he pushes back against me and presses me against the wall."
        hav "Get back ere!"
        pcm "Ahh shit!"
        hav "What you up to you strange little thing?"
        pc "Getting away from you."
        hav "Just wanna have a little fun is all."
        show haven_corner back with dissolve
        pc "Yeah have fun with your hand."
        hav "Ok..."
        show haven_corner man_grind tit penisnone ah with dissolve
        pc "Ah! Alone you idiot. Not with me."
        hav "Ah really? This seems a lot more fun."
        show haven_corner facewall with dissolve
        hav "These tits are lovely. And this ass..."
        show haven_corner ass with dissolve
        hav "Mmmmm."
        pcm "Bastard is just groping me all over..."
        show haven_corner man_poke penispoke with dissolve
        pcm "What the hell is that? Something poking at my pussy."
        show haven_corner back with dissolve
        pc "Hey! The fuck you think you are doing?"
        hav "Having some fun with you."
        "I quickly thrust my back against him hoping to push him off balance and find a moment to escape."
        if player.check_fight(3):
            hide haven_corner
            hide havman
            with hpunch
            "I manage to get him off balance long enough to make for the door."
            $ walk(loc_haven_shower)
            pcm "Fuck. That almost went very badly... Better get out of here."
            jump haven_shower_dress
        show haven_corner man_sex facewall with hpunch

        $ player.sex_vag(havenman, main_quest_05)
        "I almost get him off balance but then he holds onto me and pushes me against the wall again."
        pc "AH Fuck!!"
        hav "Mmmmm."
        show haven_corner back with dissolve
        pc "You shit!"
        hav "Mmmm, if you wanted it that badly all you had to do was ask."
        pc "..."
        show haven_corner facewall with dissolve
        pcm "Fuck. I ended up making it worse..."
        pc "*SOB*"
        "I just stand there facing the wall as he pumps in and out of me. He doesn't seem to care about me in the slightest and uses my body only for his pleasure."
        show haven_corner tit with dissolve
        hav "Not so mouthy now are ya?"
        "I don't respond and just wait for him to get this over and done with..."
        hav "Haaaaaa!"
        if player.check_fight(3):
            $ player.sex_cum(havenman, "pullout", main_quest_05)
            hide haven_corner
            hide havman
            with hpunch
            "I use this moment to quickly push away again and get out of the room."
        else:
            $ player.sex_cum(havenman, "inside", main_quest_05)
            "I feel him cumming inside me and hope that this ordeal is over with."
            hav "Aaaa you lovely little whore!"
            pc "You done?"
            show haven_corner stand_facingaway penisnone with dissolve
            "I feel his softening and slippery cock slip out of me followed by his cum leaking down my leg."
            hav "Ahhh. Next time show a little love instead of trying to shove someone over."
            pc "Fuck you."
            hide haven_corner
            hide havman
            with dissolve

        "I head straight for the door while he's enjoying his post orgasm bliss."
        $ walk(loc_haven_shower)
        pcm "..."
        pc "*SOB*"
        jump haven_shower_dress

label haven_utilities_join_5:
    hav "Whassa whore doin in here makin all that noise anyway?"
    $ player.face_worried()
    hav "Keepin your stash in 'ere or somethin?"
    pc "Errr..."
    show haven_corner stand_facing wall avoid with dissolve
    hav "Come ere. Keep quiet and so will I."
    $ player.sex_forced(havenman)
    if player.confidence <= 20:
        $ player.face_meek()
        pc "Please go away."
    else:
        pc "Get away from me."
    if player.confidence >= 40:
        if player.check_fight(4):
            hide haven_corner with hpunch
            "I shove the guy out the way and quickly head for the door."
            jump haven_utilities_join_5_resist_win
        else:
            show haven_corner push with hpunch
            "I try to shove the guy away but he is too strong for me."

    hav "Wassa matter love? We just getting to know each other."
    pc "No interest in getting to know you."
    show haven_corner finger ah with dissolve
    hav "Seein that little black bush you have makes me wanna get to know you real good."
    if player.confidence >= 30:
        if player.check_fight(4):
            hide haven_corner with hpunch
            "I shove the guy out the way and quickly head for the door."
            jump haven_utilities_join_5_resist_win
        else:
            show haven_corner push with hpunch
            "I try shoving him away but he hardly moves."
    else:
        show haven_corner push with dissolve
        "I meekly try shoving him away but he hardly moves."
    hav "Try that again an I won't be so nice anymore."
    if player.confidence >= 70:
        jump haven_utilities_join_5_resist_check

    elif player.confidence >= 40:
        menu:
            "Try shoving him away again.":
                jump haven_utilities_join_5_resist_check
            "Do nothing":

                jump haven_utilities_join_5_submit
    else:
        jump haven_utilities_join_5_submit

label haven_utilities_join_5_resist_win:
    pause 0.5
    hide havman
    $ walk(loc_haven_shower)
    pause 0.5
    $ pc_dress()
    $ acc_shower_dress()
    $ acc.makeup_on = True
    pcm "Damn pervert!"
    pcm "That almost got dangerous..."
    if player.mood <= 20:
        pc "*SOB*"
    pause 0.5
    $ walk(loc_haven_hallway_1f)

    jump travel

label haven_utilities_join_5_resist_check:
    if player.check_fight(5):
        hide haven_corner with hpunch
        "I try with all my strength to push the guy away one final time."
        jump haven_utilities_join_5_resist_win
    else:
        jump haven_utilities_join_5_resist

label haven_utilities_join_5_resist:
    show haven_corner with hpunch
    "I try with all my strength to push the guy away one final time, But I am unable to wrestle away from him."
    hav "Little cunt, I told you to stop!"
    $ player.punch()
    show haven_corner grope with hpunch
    "He starts getting really agressive with me and tries to pin me against the wall."
    $ player.punch()
    show haven_corner stand_facingaway holdarm facewall with hpunch
    hav "Could have done this the easy way."
    show haven_corner penisup mast with dissolve
    pc "No stop! What are you doing?"
    $ player.face_cry()
    pc "*SOB*"
    hav "Shut up!"
    $ player.punch()
    show haven_corner with hpunch
    pc "Ahhh it hurts. Stop hitting me!"
    show haven_corner man_poke penispoke ass with dissolve
    pc "*SOB*"
    $ player.sex_forced(havenman)
    $ player.sex_vag(havenman)
    $ player.face_cry()
    show haven_corner man_grind with dissolve
    "I feel an unwelcome invasion between my legs and no amount of struggling can prevent it. It slides its way deep inside me and I just give up any attempt to prevent it."
    "I try to block out what is happening to me, but the odd punch to the ribs brings me back to what I am suffering."
    "But he doesn't let up and keeps brutally fucking me against the wall, now and then shoving my face painfully against the bricks in front of me."
    pc "*SOB*"
    hav "Shut up!"
    jump random_event_haven_ko

label haven_utilities_join_5_submit:
    $ player.face_meek()
    pcm "..."
    show haven_corner neutral up with dissolve
    hav "That's better."
    pc "Please don't..."
    hav "Shhh. Relax."
    show haven_corner penisup mast with dissolve
    pc "*SOB*"
    hav "Turn around and let me see that ass of yours."
    pc "..."
    pc "No."
    hav "I said turn around. Now!"
    pc "Please don't ma..."
    $ player.punch()
    show haven_corner with hpunch
    hav "Now!"
    pc "*SOB*"
    show haven_corner stand_facingaway facewall with dissolve
    hav "That's more like it. Now be a good girl and be quiet."
    pc "*SOB*"
    show haven_corner man_grind with dissolve
    hav "Mmmm, such a tasty little thing you are. Asking to be fucked all night."
    pc "No..."
    $ player.punch()
    pc "Nnnnn."
    hav "I told you to be quiet."
    pc "..."
    hav "Mmmm, fucking these cheeks of yours is something else. Shame about the plug in your arse."
    hav "Half a mind to pull it out, stick it in your mouth and fuck you in the arse."
    pc "*SOB*"
    $ player.punch()
    pc "Hmmmmt!"
    hav "Your pussy will do instead."
    pc "Please no, not th..."
    $ player.punch()
    pc "Ahhh!"
    hav "One more sound and you will wish you kept quiet."
    pc "..."
    show haven_corner man_poke tit penispoke with dissolve
    hav "I'm gonna fuck your pussy, cum inside you and you will say nothing."
    hav "Isn't that right?"
    if player.confidence >= 20:
        menu:
            "Plead":
                pc "Please, I don't want to en..."
                jump random_event_haven_ko
            "...":
                $ NullAction()
    else:
        pc "..."
    hav "Thought so."
    $ player.sex_vag(havenman)
    show haven_corner man_sex with dissolve
    pcm "Nnnnnnng"
    hav "Little girls like you should know yer place."
    hav "You should have a man's cock in you or his baby. Better both."
    pcm "*SOB*"
    hav "You got my cock an Imma give you my baby to carry with you."
    hav "Shitty little slut."
    hav "Ahhhhh yes."
    $ player.sex_cum(havenman, "inside")
    hav "Ahhhhh yes. Take it in you."
    pcm "Fuck no..."
    hav "Mmmmmm."
    hav "Should invite the rest of the guys out there to come and take turns fucking you."
    hav "You need a bit of training, but you have been somewhat obedient so I will let you off with just my cock in you."
    hide haven_corner with dissolve
    hav "Now, say thank you."
    $ player.face_meek()
    pc "..."
    hav "Do I need to go and invite them in here?"
    pc "..."
    pc "Thank you."
    hav "For what?"
    pc "..."
    pc "For having sex with me."
    hav "Good enough."
    hide havman with dissolve
    pcm "Fuck no. What a cunt!"
    $ player.face_cry()
    pc "*SOB*"
    pc "*Sniff*"
    pcm "I want out of here..."
    jump travel


label haven_utilities_pipes_break_prompt:
    if inv.qty(item_haven_crowbar):
        pcm "These pipes look like they can be broken if I pry them from the wall with the tool I got from the storage room. I should make sure no one can hear me in the showers though."
        menu:
            "Pry the pipes":
                jump haven_utilities_pipes_break
            "Not now":

                jump travel

label haven_utilities_pipes_break:
    if not "pipes_pry" in loc_haven_utilities.dict:
        $ loc_haven_utilities.dict["pipes_pry"] = 0
    if not inv.qty(item_haven_crowbar):
        pcm "Not going to be able to do much with my bare hands. I need to find something to help me break it."
        jump travel
    if player.tired <= 20:
        pcm "I am far too exhausted to be trying to break those pipes. I should rest a bit before giving it a go."
        jump travel
    if player.mood <= 20:
        pcm "Fuck sticking round here with my arse hanging out. I want a pick me up!"
        jump travel
    if loc_haven_utilities.dict["pipes_pry"] < 3 and not player.check_strength(2, notif=False):
        pcm "Ok, let's see here."
        "I wedge the crowbar behind one of the pipes but no matter how hard I pull, I am unable to make any headway in prying it off the wall."
        $ player.stat_popup_screen("Not strong enough")
        $ dialouge = renpy.random.choice([
        "Fuck, I am not strong enough to get the damn thing off the wall.",
        "Damn, this is harder than I thought.",
        "Ugh, I am too small to get the weight I need behind it.",
        "Uff. C'mon! It shouldn't be this hard."
        ])
        pcm "[dialouge]"
        $ dialouge = renpy.random.choice([
        "Oh well, I'll have to keep trying. I will manage to do it eventually.",
        "Need to keep trying.",
        "I will get it eventually.",
        "Ok, let's try again."
        ])
        pcm "[dialouge]"
        $ exercise(20)
        $ haven_utilities_pry_join_chance()
        jump travel_arrival
    if loc_haven_utilities.dict["pipes_pry"] == 0:
        $ loc_haven_utilities.dict["pipes_pry"] += 1
        pcm "Ok, let's give this a go."
        "I wedge the crowbar behind one of the pipes and put all my weight behind it trying to pull the pipe from the wall."
        $ player.stat_popup_screen("Got it!")
        with hpunch
        "The pipe starts to give way but then the crowbar slips and I go tumbling backwards onto the floor."
        "The pipes snapping back against the wall creates a huge *CLANG* sound."
        pc "Fuck."
        pcm "Did anyone hear that...?"
        $ exercise(20)
        $ haven_utilities_pry_join_chance()
        pcm "... ..."
        $ haven_utilities_pry_join_chance()
        pcm "..."
        pcm "Phew, getting caught in here butt naked would be pretty bad."
        jump travel_arrival
    elif loc_haven_utilities.dict["pipes_pry"] == 1:
        $ loc_haven_utilities.dict["pipes_pry"] += 1
        pcm "Ok, let's try again, and this time not fall on my bare arse."
        "Once again, I wedge the crowbar behind the pipes and put my weight behind it trying to pull them from the wall."
        $ player.stat_popup_screen("Got it!")
        with hpunch
        "Again just as I am getting it from the wall, the bar slips and I am hurled to the ground following a huge *CLANG*"
        pcm "FUCK FUCK FUCK!"
        $ exercise(20)
        $ haven_utilities_pry_join_chance()
        pcm "... ..."
        $ haven_utilities_pry_join_chance()
        pcm "..."
        pcm "*Phew*"
        jump travel_arrival
    elif loc_haven_utilities.dict["pipes_pry"] == 2:
        $ loc_haven_utilities.dict["pipes_pry"] += 1
        pcm "Ok, third times a charm."
        "I again attempt to pull the pipe from the wall. The pipe is giving a lot easier than my first attempts and it starts to loudly groan. But just before it is about to break, the bar slips."
        $ player.stat_popup_screen("Got it!")
        with hpunch
        "*CLANG*"
        "I jump up to my feet and watch the door for anyone coming to investigate."
        $ exercise(20)
        $ haven_utilities_pry_join_chance()
        pcm "... ..."
        $ haven_utilities_pry_join_chance()
        pcm "..."
        pcm "*Phew*"
        pcm "Well, looks like I might have it now. I have got the hang of using this tool and the pipe is starting to break at the seam. There is already a fair amount of leakage right now."
        pcm "So one more try should have it. But I need to make sure to wait for the right time to make a run for it after it's broken."
        jump travel_arrival
    else:
        pcm "The pipe is ready to give way. Am I prepared for the chaos it is going to cause?"
        menu:
            "Break the pipe and prepare to make a run for it":
                $ log.markdone("mq_05_pipesbreak")
            "Not right now. I should wait for a better time":
                jump travel
        pcm "Ok, another try..."
        "I wedge the bar behind the pipe and pull at it with all my weight. I am suddenly thrown back on the floor as the pipe gives way off the wall and I am covered in water pouring from the freshly broken pipe."
        $ player.stat_popup_screen("Got it!")
        with vpunch
        pcm "Okay ok. Finally! Now to get the fuck out of here."

        jump haven_pipes_break_ending

label haven_utilities_investigate_picker:
    $ dialouge = renpy.random.choice([
    "Let's see here. Better be quiet.",
    "Don't make too much noise...",
    "Hopefully I can find something useful.",
    "Hmmm...",
    ])
    pcm "[dialouge]"

    $ rand_choice = WeightedChoice([
        
    ("haven_utilities_boiler", If(not "checked_boiler" in loc_haven_utilities.list, 1000, 0)),
    ("haven_utilities_bigpipe", If(not "checked_bigpipe" in loc_haven_utilities.list, 1000, 0)),
    ("haven_utilities_bluepipes", If(not "checked_bluepipes" in loc_haven_utilities.list, 1000, 0)),
    ("haven_utilities_cables", If(not "checked_cables" in loc_haven_utilities.list, 1000, 0)),
    ("haven_utilities_ceilingpipe", If(not "checked_ceilingpipe" in loc_haven_utilities.list, 1000, 0)),
    ("haven_utilities_cutoff", If(not "checked_cutoff" in loc_haven_utilities.list, 1000, 0)),
    ("haven_utilities_elebox", If(not "checked_elebox" in loc_haven_utilities.list, 1000, 0)),
    ("haven_utilities_fire", If(not "checked_fire" in loc_haven_utilities.list, 1000, 0)),
    ("haven_utilities_gas", If(not "checked_gas" in loc_haven_utilities.list, 1000, 0)),
    ("haven_utilities_redpipes", If(not "checked_redpipes" in loc_haven_utilities.list, 1000, 0)),
    ("haven_utilities_trash", If(not "checked_trash" in loc_haven_utilities.list, 1000, 0)),
    ("haven_utilities_vents", If(not "checked_vents" in loc_haven_utilities.list, 1000, 0)),
    ("haven_utilities_redpipes_post_sprinkler", If(log.interactive("mq_05_pipes"), 1000, 0)),
    ])
    jump expression rand_choice

label haven_utilities_boiler:
    pcm "Looks like boiler to heat the water up. Considering the showers are stone cold I am going to guess that it doesn't work."
    $ add_to_list(loc_haven_utilities.list, "checked_boiler")
    $ working(10)
    jump travel_arrival

label haven_utilities_bigpipe:
    pcm "Hmm, not sure what this one does but I doubt I will have the strength to turn that valve. Looks pretty rusted."
    $ add_to_list(loc_haven_utilities.list, "checked_bigpipe")
    $ working(10)
    jump travel_arrival

label haven_utilities_bluepipes:
    pcm "Some kind of water pipe. Feels colder than the other pipes so probably has water running through it."
    if player.int >= 30:
        pcm "Considering the size, for draining away wastewater?"
    $ add_to_list(loc_haven_utilities.list, "checked_bluepipes")
    $ working(10)
    jump travel_arrival

label haven_utilities_cables:
    if player.int >= 40:
        pcm "Some kind of cladding for protecting electrical cables. Not in good condition considering a bunch of wires are just hanging out."
    else:
        pcm "Doesn't look like a water pipe and has some wires or cables hanging from it."
    pcm "Considering I am soaking wet, I should stay away from anything that looks electrical. I haven't seen much evidence that this building has power but I am not taking that risk."
    $ add_to_list(loc_haven_utilities.list, "checked_cables")
    $ working(10)
    jump travel_arrival

label haven_utilities_ceilingpipe:
    pcm "Even if I could reach that valve, all I am going to end up doing is dangling naked from it. No chance would I be able to turn it."
    $ add_to_list(loc_haven_utilities.list, "checked_ceilingpipe")
    $ working(10)
    jump travel_arrival

label haven_utilities_cutoff:
    pcm "Some weird cut off pipe sticking out the floor. No idea what that thing does..."
    $ add_to_list(loc_haven_utilities.list, "checked_cutoff")
    $ working(10)
    jump travel_arrival

label haven_utilities_elebox:
    pcm "Doubt I could reach it that thing up there. But no chance am I climbing up naked and wet to mess with what looks like an electrical box."
    $ add_to_list(loc_haven_utilities.list, "checked_elebox")
    $ working(10)
    jump travel_arrival

label haven_utilities_fire:
    pcm "The pipe is labelled \"Fire\". I am guessing this is where they shut the water off when the fire suppression system goes off."
    pcm "..."
    pcm "I might be able to take advantage of this. If I set off the sprinklers, then the guard will have to come running in here to turn it off."
    pcm "If I am lucky, he will be in too much of a rush to lock the gate behind him and I can slip by and make my way up to the third floor."
    pcm "Let's check out the building's sprinkler system and see if I can set it off somewhere."
    $ log.activate("mq_05_sprinklers", notify=True)
    $ add_to_list(loc_haven_utilities.list, "checked_fire")
    $ working(10)
    jump travel_arrival

label haven_utilities_gas:
    if player.int >= 30:
        pcm "Pretty sure they are gas meters. No one uses gas anymore but I should still be careful with them. If I am unlucky I could end up blowing up the whole building."
    else:
        pcm "They look like some kind of meter judging by the dials on it. I probably shouldn't mess with something I am unfamiliar with."
    $ add_to_list(loc_haven_utilities.list, "checked_gas")
    $ working(10)
    jump travel_arrival

label haven_utilities_redpipes:

    pcm "Water pipes? Considering how cold they are I am guessing they work."
    if player.int >= 30:
        pcm "Considering where they are coming from and the colour, I would guess they are supposed to be hot water pipes. But since the boilers don't work there is just cold water coming from them"
    $ add_to_list(loc_haven_utilities.list, "checked_redpipes")
    $ working(10)
    jump travel_arrival

label haven_utilities_redpipes_post_sprinkler:
    if inv.qty(item_haven_crowbar):

        pcm "These pipes have water running through them and they aren't as sturdy looking as some of the other pipes."
        pcm "I might be able to use that tool I found to try and pry the pipes away from the wall to cause a leak."
        pcm "I don't need to destroy the whole thing. Just enough to cause a large enough leak to get the guards attention."
    else:


        pcm "These pipes have water running through them and they aren't as sturdy looking as some of the other pipes."
        pcm "I might be able to do something to cause a leak, but not with my bare hands. I would need some kind of tool to help me cause enough damage to cause a leak big enough to attract the guards's attention."
    $ working(10)
    $ loc_haven_utilities.dict["pipes_pry"] = 0
    $ log.deactivate("mq_05_pipes")
    $ log.activate("mq_05_pipesbreak", notify=True)
    jump travel_arrival

label haven_utilities_trash:
    pcm "Some junk in the corner. Wonder if there is anything worthwhile in it..."
    pcm "Ugh, I am not going to go through any of that stuff. Might end up poked with a needle or something..."
    $ add_to_list(loc_haven_utilities.list, "checked_trash")
    $ working(10)
    jump travel_arrival

label haven_utilities_vents:
    pcm "Pretty sure they are air vents. Probably to get rid of all the humid air from the room."
    if player.int >= 20:
        pcm "Not at all humid in here right now but no idea if that is because the vents are doing their job or because none of the boilers work so there is no hot water to create the humidity."
    $ add_to_list(loc_haven_utilities.list, "checked_vents")
    $ working(10)
    jump travel_arrival

label haven_utilities_scav_generic_1:
    pcm "Hmm, just some soaked pack of cigs. Not going to be able to dry them out or anything."
    $ working(10)
    jump travel_arrival

label haven_utilities_scav_generic_2:
    pcm "Some junk in the corner. Are those needles? Fuck I am not going near those."
    $ working(10)
    jump travel_arrival

label haven_utilities_scav_generic_3:
    pcm "Nothing really behind the pipes. On top of the pipes... Nothing..."
    $ working(10)
    jump travel_arrival

label haven_utilities_scav_generic_4:
    pcm "How about between these construction pallets?"
    if not inv.qty(item_brew):
        pcm "Ah! Some brew hiding here. At least thats what I hope it is..."
        $ inv.take(item_brew)
    else:
        pcm "Nothing."
    $ working(10)
    jump travel_arrival

label haven_utilities_scav_generic_5:
    if not inv.qty(item_cigs):
        pcm "Hmm, looks like someone has been smoking in here and using this can as an ash tray. I can probably break down the ends and roll into new cigs."
        $ inv.take(item_cigs)
    else:
        pcm "Hmm, looks like someone has been smoking in here. Nothing I can take though."
    $ working(10)
    jump travel_arrival

label haven_utilities_scav_generic_6:
    pcm "Hmm, what we got here?"
    pcm "Just a mushy pack of cigs. Hmmm?"
    pcm "Ah, looks like they kept their lighter in the pack. This will dry off no problem."
    $ inv.take(item_haven_lighter)
    $ working(10)
    jump travel_arrival





label haven_check_sprinklers:
    if log.have("mq_05_sprinklers") == 0:
        pcm "Not sure I can even see any sprinklers in here. The ceiling is such a wreck."
        pcm "I should check out other rooms and see if I have any luck there."
        $ log.find("mq_05_sprinklers", next=False)
        $ add_to_list(loc_cur.list, "checked_sprinkler")
        $ working(10)

    elif log.have("mq_05_sprinklers") == 1:
        pcm "Nothing here. Looks like they might have been ripped out."
        $ log.find("mq_05_sprinklers", next=False)
        $ add_to_list(loc_cur.list, "checked_sprinkler")
        $ working(10)

    elif log.have("mq_05_sprinklers") == 2:
        pcm "Nothing. Not even some rusted old sprinklers or some broken down pipes. Just nothing here."
        $ log.find("mq_05_sprinklers", next=False)
        $ add_to_list(loc_cur.list, "checked_sprinkler")
        $ working(10)

    elif log.have("mq_05_sprinklers") == 3:
        pcm "*Sigh*... Nothing. Either this building never had them to begin with or they have all been ripped out."
        pcm "Considering there is the shut off valve in that maintenance room, this place must have had them at some point."
        pcm "Wonder if they had already been set off at some point and were ripped out to prevent them going off again..."
        pcm "Well no matter. This plan is a bust regardless. I should head back to the maintenance room and see if there is anything else I can mess with."
        $ log.find("mq_05_sprinklers", next=False)
        $ log.deactivate("mq_05_sprinklers")
        $ log.activate("mq_05_pipes", notify=True)
        $ working(10)

    jump travel_arrival
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
