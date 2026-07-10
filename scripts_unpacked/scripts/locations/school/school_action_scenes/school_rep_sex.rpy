label school_rep_sex_debug:
    "School repeatable sex scene. It is buggy right now and thats the reason this cheat exists. So I can debug"
    "Are you selling yourself?"
    menu:
        "Yes":
            $ player.set_whore_price(0)

            "Where did you agree to have sex?"
            menu:
                "Handjob":
                    $ player.soldrequest = "hand"
                    $ player.want_sexlocation = player.soldrequest
                "Blowjob":
                    $ player.soldrequest = "oral"
                    $ player.want_sexlocation = player.soldrequest
                "Anal sex":
                    $ player.soldrequest = "anal"
                    $ player.want_sexlocation = player.soldrequest
                "Vag sex":
                    $ player.soldrequest = "vag"
                    $ player.want_sexlocation = player.soldrequest
                "No agreement was made":
                    $ player.soldrequest = ""
        "No":



            $ NullAction()
        "I am being assaulted":

            $ player.sex_forced(schoolguy)
            jump school_rep_sex

    jump school_rep_sex





label school_rep_sex:
    $ npc_race_picker()
    if player.beingraped:
        jump school_rep_sex_assault


    if check_if_isolated():
        $ dialouge = WeightedChoice([
        ("Ok, well, this is as good a place as any.", 1),
        ("Right here is fine.", 1),
        ("No one should disturb us here.", 1),
        ("Let's pop into one of the cubicles.", If ("toilet" in loc_cur.name or "locker" in loc_cur.name, 1, 0)),
        ("No one should be able to see us here.", If (loc_cur == loc_bushes, 1, 0)),
        ])
        pc "[dialouge]"
    else:

        $ dialouge = WeightedChoice([
        ("Let's go somewhere more private.", 1),
        ("Let's go somewhere where we won't be caught.", 1),
        ("Somewhere quiet would be better, follow me.", 1),
        ("Let's go somewhere else so I can have fun with that cock of yours.", If (player.soldprice == 0, 1, 0)),
        ("Not very private here, come with me.", 1),
        ])
        pc "[dialouge]"

        $ dialouge = WeightedChoice([
        ("Ok, lead the way.", 1),
        ("Sure.", 1),
        ("Ok, let's go.", 1),
        ("Right, somewhere else would be better.", 1),
        ("Sounds good to me.", 1),
        ])
        guy "[dialouge]"

        $ randomnum = renpy.random.randint(1, 3)
        if randomnum == 1:
            $ walk(loc_school_toilet_girls)
            pc "Looks quiet enough in here. Come on."
            "You check to make sure no one is in the toilets before ushering the guy into one of the cubicles."
        elif randomnum == 2:
            $ walk(loc_school_toilet_boys)
            pc "Let's try in here. Hope no one notices us..."
            "You quickly march the guy into one of the empty cubicles. You didn't check or care if anyone noticed."
        else:
            $ walk(loc_school_locker_girls)
            pc "Sounds like the place is quiet. Come on."
            "You check to make sure no one is around before ushering the guy into one of the changing cubicles."
label school_rep_sex_pay:
    if player.soldprice > 0:
        $ dialouge = WeightedChoice([
        ("So... money first.", 1),
        ("Ok, hand over the money.", 1),
        ("Money before we do anything more.", 1),
        ("Pay up before we do anything more.", 1),
        ])
        pc "[dialouge]"
        $ dialouge = WeightedChoice([
        ("Sure, here you go.", 1),
        ("Right... Here we go.", 1),
        ("Ah right. Here you are.", 1),
        ("Sure.", 1),
        ])
        guy "[dialouge]"

        $ randomnum = renpy.random.randint(1, (130 - player.int))
        if randomnum == 1:
            jump school_rep_sex_forced_attack


        $ player.add_money(player.soldprice)

    if player.soldprice > 0:
        if player.soldrequest == "hand":
            jump school_rep_sex_handjob
        elif player.soldrequest in ("oral", "blow"):
            jump school_rep_sex_blowjob
        elif player.soldrequest in ("anal", "ass"):
            jump school_rep_sex_sex
        elif player.soldrequest == "vag":
            jump school_rep_sex_sex
        else:

            if player.check_sex_agree(4):
                jump school_rep_sex_sex
            elif player.check_sex_agree(2):
                jump school_rep_sex_blowjob
            else:
                jump school_rep_sex_handjob
    else:

        pcm "Hmmm... What should I do..."
        menu:
            "Decide not to and leave":
                jump school_rep_sex_bail
            "Get on my knees" if player.check_sex_agree(1):
                jump school_rep_sex_handjob
            "Turn around and bend over" if player.check_sex_agree(3):
                jump school_rep_sex_sex

label school_rep_sex_bail:
    $ player.face_worried()
    pc "Err..."
    pc "Actually I don't think I can do this..."
    pc "I am going to go..."
    $ rand_choice = WeightedChoice([
    ("school_rep_sex_bail_beat", 130 - player.int),
    ("school_rep_sex_bail_curse", 200 - player.int),
    ("school_rep_sex_bail_pay", 150),
    ("school_rep_sex_bail_leave", 500),
    ])
    jump expression rand_choice

label school_rep_sex_bail_leave:
    guy "Err, okay..."
    pc "Sorry..."
    $ walk(loc_school_hallway)
    pc "*Sigh*"
    jump random_event_school_end_picker

label school_rep_sex_bail_pay:
    guy "What if I offered to pay?"
    pc "Pay?"
    if player.check_whore():
        $ player.set_whore_price(0)
        pc "Hmm, how much?"
        guy "Let's see... How about £[player.soldprice]?"
        pc "..."
        menu:
            "Agree":
                pc "Okay then. I guess so."
                guy "Great!"
                jump school_rep_sex_pay
            "Refuse":
                pc "Sorry, I can't..."
                jump school_rep_sex_bail_leave

label school_rep_sex_bail_curse:
    guy "Fuckin teasing bitch!"
    pc "Wha..."
    pcm "Fuck, better get out of here..."
    guy "CUNT!"
    $ walk(loc_school_hallway)
    $ player.add_mood(-20)
    pcm "What the hell... Arsehole."
    jump random_event_school_end_picker

label school_rep_sex_bail_beat:
    guy "Fuckin teasing bitch!"
    pc "Wha..."
    pcm "Fuck, better get out of..."
    jump school_rep_sex_forced_attack

label school_rep_sex_handjob:
    $ dialouge = WeightedChoice([
    ("Mmm, show me what you have down there.", 1),
    ("Mmm, can't wait to see what you are packing.", 1),
    ("Show me what you got.", 1),
    ])
    pc "[dialouge]"
    $ c.top = 0
    $ c.bra = 0
    $ c.outfit = 0
    pause 0.5
    $ player.sex_hand(schoolguy)
    show sb_handjob down with dissolve
    $ dialouge = WeightedChoice([
    ("Oh, not a disappointment at all.", 1),
    ("Already up eh?", 1),
    ("Looks like your friend is happy to see me.", 1),
    ])
    pc "[dialouge]"
    show sb_handjob up
    $ dialouge = WeightedChoice([
    ("Not every day someone offers to drag you off somewhere alone.", 1),
    ("Mmm. Getting a chance with someone like you makes it stand up pretty quickly.", 1),
    ("A drunk slut rushes me off somewhere alone so of course I am ready to go. Can't have you sobering up and changing your mind.", If (player.check_drunk(2), 1, 0)),
    ("Gotta be ready if you wanna have a go on the school slut.", If (player.isslut, 1, 0)),
    ("When the local bike offers you a go, can't not impress.", If (player.isslut and player.soldprice == 0, 1, 0)),
    ("Gotta be ready if you wanna have a go on the school whore.", If (player.iswhore, 1, 0)),
    ("A freebie off a whore so of course I am ready.", If (player.iswhore and not player.selling, 1, 0)),
    ("Why else would I pay you to get me off if I wasn't already horny?", If (player.selling, 1, 0)),  
    ])
    guy "[dialouge]"
    show sb_handjob down
    $ dialouge = WeightedChoice([
    ("Mmm, so warm and hard in my hand.", 1),
    ("Ha it feels so nice to have it in my hand.", 1),
    ("Solid as a rock. Been a while has it?", 1),
    ("With a cock like this, not even sure why you are paying me. Could easily get someone to do it for free.", If (player.selling, 1, 0)),
    ("Always nice when people paying me have nice cocks like this.", If (player.selling, 1, 0)),
    ])
    pc "[dialouge]"
    $ dialouge = WeightedChoice([
    ("I stroke his cock with a nice rhythm and it seems he's enjoying it by the sounds he is making.", 1),
    ("I grip his warm cock in my hand and stroke it back and forth, slowly picking up the pace as I hear groans of pleasure from his mouth.", 1),
    ("I take his cock in my hand and start working at the shaft, stroking him while he looks at my naked tits.", 1),
    ("It is hardly the first cock I have had in my hand and I start wanking him off with expert skill. The noises he is making letting me know how fast or slow to go.", If (player.hsex > 15,1,0)),
    ("Even though he is paying me to do it, I still try to put in a good performance and make sure he gets as much pleasure out of it as possible.", If (player.selling, 1, 0)),
    ("Even though he is paying me, his cock in my hand still feels nice so I put in effort to make sure to give him as much pleasure as I can give him.", If (player.selling, 1, 0)),
    ])
    "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Ah yes! Keep going like that. So nice!", 1),
    ("Ah fuck it feels nice. Love a little bitch like you wanking me off", 1),
    ("Ah yes, like that.", 1),
    ("Fuck, you know what you are doing don't you?", If (player.hsex > 15,1,0)),
    ("Mmm, whores sure know what they are doing down there.", If (player.selling, 1, 0)),
    ("Having a whore grab your cock is great, they know how to treat it well.", If (player.selling, 1, 0)),
    ])
    guy "[dialouge]"

    show sb_handjob up
    $ dialouge = WeightedChoice([
    ("Mmm you dirty pervert, you like it when I do this?", 1),
    ("Bet you love it seeing a girl on her knees with your cock in her hand.", 1),
    ("Such a big one as well. Feels so nice and firm in my hand.", 1),
    ])
    pc "[dialouge]"

    guy "Mmmmmm!"
    if (player.selling and player.check_sex_agree(4)) or (player.selling == False and player.check_sex_agree(2)):
        $ dialouge = WeightedChoice([
        ("Bet you would like it more if it were my lips around it instead of my hand.", 1),
        ("Wonder what it tastes like. I'm sure you don't mind if I have a try.", 1),
        ("Looks nice and big in my hand, but think I will try it in my mouth just to be sure.", 1),
        ("Mmm, starting to think it might be better off in my mouth.", 1),
        ])
        pc "[dialouge]"
        guy "Ah fuck yes!"
        jump school_rep_sex_blowjob_jump

    show sb_handjob down
    $ dialouge = WeightedChoice([
    ("Oooh, what was that? I think I can feel it pulsing.", 1),
    ("Wow, getting even harder now. Ready to blow on me are you?", 1),
    ("Enjoying that are you? I can feel your cock throbbing.", 1),
    ])
    pc "[dialouge]"

    $ dialouge = WeightedChoice([
    ("Ah fuck yes!", 1),
    ("Ah fuck! Sluts like you know how to work a cock.", 1),
    ("Ah yes, like that.", 1),
    ("Fuck! How many guys have you wanked off? This feels so good!", If (player.hsex > 15,1,0)),
    ("Ah fuck you dirty whore! Keep going.", If (player.selling, 1, 0)),
    ])
    guy "[dialouge]"
    guy "Ahhhhhhhhh..."
    guy "Yes!!"
    $ player.sex_cum(schoolguy, "hand")
    $ dialouge = WeightedChoice([
    ("Oooh, it's coming out.", 1),
    ("Mmm it's throbbing.", 1),
    ("Mmmmm.", 1),
    ("Ooooh.", 1),
    ])
    pc "[dialouge]"
    guy "Haaaaa..."
    $ dialouge = WeightedChoice([
    ("Looks like someone enjoyed himself.", 1),
    ("Mmm, all sticky...", 1),
    ("Mmmmm. Made a bit of a mess there. \u2665", 1),
    ("Mmm so warm.", 1),
    ])
    pc "[dialouge]"
    guy "*Phew*"
    jump school_rep_sex_end

label school_rep_sex_blowjob:
    $ dialouge = WeightedChoice([
    ("Mmm, show me what you have down there.", 1),
    ("Mmm, can't wait to see what you are packing.", 1),
    ("Show me what you got.", 1),
    ("Show me what I am going to be sucking on.", 1),
    ])
    pc "[dialouge]"
    $ c.top = 0
    $ c.bra = 0
    $ c.outfit = 0
    pause 0.5

label school_rep_sex_blowjob_jump:
    $ player.sex_oral(schoolguy)
    $ renpy.scene()
    show sb_blowjob up
    with dissolve
    show sb_blowjob face 1h with dissolve
    $ randomnum = renpy.random.randint(1, 2)
    if randomnum == 1:
        show sb_blowjob 1h suck down with dissolve
    else:
        show sb_blowjob 2h suck down with dissolve
    $ dialouge = WeightedChoice([
    ("He relaxes back against the wall as I take his warm cock in my hand and wrap my lips around it. It feels so nice and warm being there.", 1),
    ("I take his cock in my hands and start to stroke him while I put the tip of his cock in my mouth.", 1),
    ("I see his large cock in front of my face and take it in my hands. Then slowly I lick the tip of his penis and slide my lips around his cockhead.", 1),
    ("Seeing his huge cock in front of me fills me with excitement. I take him fully in my mouth while I wrap my fingers around his cock and stroke it.", 1),
    ("Even though I am being paid to suck him off. Seeing his huge cock in front of me still makes me excited and I happily take it in my hands and wrap my lips around it.", If (player.selling, 1, 0)),
    ])
    "[dialouge]"
    show sb_blowjob up
    pc "Mmmm ♥"
    show sb_blowjob down
    guy "Ahhhh!"
    $ dialouge = WeightedChoice([
    ("It's clear from his reactions that he's enjoying himself so I continue to work at his cock and swirling my tongue around him inside my mouth.", 1),
    ("His actions make it clear he is having fun. I speed up working his shaft with my hands as I use my tongue to pleasure his cockhead.", 1),
    ("He rubs his fingers through my hair and tries to push his cock deeper into my mouth. I happily accept it and start working his shaft with my hands.", 1),
    ("He starts thrusting into my mouth in time with my head bobbing and eventually he is slowly fucking my mouth. I help him out by stroking his cock in time with his thrusts.", 1),
    ])
    "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Mmmfff. Soo nice.", 1),
    ("Ah, more!", 1),
    ("Mmmff. So warm and nice.", 1),
    ("*Slurp*", 1),
    ("*Hyuk* *Hyuk* *Hyuk*", 1),
    ])
    pc "[dialouge]"
    $ randomnum = renpy.random.randint(1, 3)
    if randomnum == 1:
        $ dialouge = WeightedChoice([
        ("Ah so nice. How about you bend over and let me fuck you?", 1),
        ("Mmm, come here. Show me that arse of yours so I can fill you with my cock.", 1),
        ("Ah you dirty slut. Turn around and let me fuck you.", 1),
        ("Such a nice little whore. Turn around so I can put my cock in you.", If (player.selling, 1, 0)),
        ])
        guy "[dialouge]"
        if player.selling and player.check_drunk(4):
            pc "Mmmm."
            jump school_rep_sex_sex
        elif player.selling and player.check_whore():
            show sb_blowjob up
            $ dialouge = WeightedChoice([
            ("That will cost more.", 1),
            ("Offer up more money if you want to fuck me there.", 1),
            ("You didn't pay for that so it will be extra.", 1),
            ])
            pc "[dialouge]"
            $ randomnum = renpy.random.randint(1, 3)
            if randomnum == 1:
                $ dialouge = WeightedChoice([
                ("Shit. I can't afford anything more. Keep sucking then.", 1),
                ("Ah fuck no. Keep sucking me off then.", 1),
                ("Never mind then. I will stick to your mouth.", 1),
                ])
                guy "[dialouge]"
            else:
                $ player.soldprice = player.set_whore_price(0) / 4
                guy "How about an extra £[player.soldprice]?"
                menu:
                    "Agree":
                        $ player.add_money(player.soldprice)
                        jump school_rep_sex_sex
                    "Refuse":
                        $ dialouge = WeightedChoice([
                        ("(Not really worth it. I'll keep sucking him off.", 1),
                        ("(For that I would rather just suck him off.", 1),
                        ])
                        pc "[dialouge]"
        elif player.check_sex_agree(3):
            menu:
                "Agree":
                    jump school_rep_sex_sex
                "Refuse":
                    $ dialouge = WeightedChoice([
                    ("Just keep sucking him. Not interested in being fucked right now.", 1),
                    ("Better not. Stick to him in my mouth", 1),
                    ])
                    pcm "[dialouge]"

    show sb_blowjob down
    $ dialouge = WeightedChoice([
    ("Sexy little slut. Keep going!", 1),
    ("Ah fuck, keep going like that and you will make me cum.", 1),
    ("Yes, fuck! Keep going...", 1),
    ("*Huff* *Huff* *Huffff*", 1),
    ])
    guy "[dialouge]"
    $ dialouge = WeightedChoice([
    ("I start to feel his cock tensing up and his movements become erratic. I know he is about to cum very soon.", 1),
    ("His groaning lets me know he is not far off cumming so I pick up the pace and blow him even faster than I was before.", 1),
    ("He is gripping onto my head and thrusting quite aggressively now. I know he won't last much longer at this rate so I work his shaft harder with my hands to try and push him over the edge.", 1),
    ])
    "[dialouge]"
    show sb_blowjob angry closed
    $ player.sex_cum(schoolguy, "mouth")
    $ dialouge = WeightedChoice([
    ("I feel his start to throb and push his cock deep in my mouth. He starts to cum and I feel his warmth squirting from his cock and get a good taste of his cum.", 1),
    ("He starts throbbing in my mouth and I feel the salty warmth from his cock enter my mouth.", 1),
    ("His cock starts to swell until he tenses up and releases his load in my mouth. Its warmth fill it up and I have no choice but to swallow most of it down.", 1),
    ("He throbs in my mouth and I feel the first wave fill me. I quickly swallow it down before another pulse shoots more on my tongue. I eagerly swallow that down as well until it seems he is all out of steam.", 1),
    ])
    "[dialouge]"
    show sb_blowjob up happy
    guy "Ahhhh! Yeeeeess..."
    guy "Haaaa..."
    pc "Mmmmm..."
    jump school_rep_sex_end

label school_rep_sex_sex:
    $ renpy.scene()
    with dissolve
    $ dialouge = WeightedChoice([
    ("Mmm, show me what you have down there.", 1),
    ("Mmm, can't wait to see what you are packing.", 1),
    ("Show me what you got.", 1),
    ])
    pc "[dialouge]"
    $ pc_striptease()
    pause 0.5

    show sb_againstwall2
    with dissolve
    if player.soldrequest == "anal":
        $ player.want_sexlocation = player.soldrequest
        if not player.check_speech(1):
            $ player.have_sexlocation = "vag"
        else:
            $ player.have_sexlocation = player.soldrequest
    elif player.soldrequest == "vag":
        $ player.want_sexlocation = player.soldrequest
        $ player.have_sexlocation = player.soldrequest
    else:
        $ player.want_sexlocation = ""
        $ player.have_sexlocation = ""
        menu:
            "Take my pussy" if player.check_vag_agree():
                $ player.want_sexlocation = "vag"
                $ player.have_sexlocation = "vag"
                $ dialouge = WeightedChoice([
                ("I want to feel you in my pussy.", If (not player.selling,1,0)),
                ("Let me feel your hard cock in my pussy.", If (not player.selling,1,0)),
                ("You can take me in the pussy if you want.", If (player.selling,1,0)),
                ("You can have my vagina if you want.", If (player.selling,1,0)),
                ("I don't mind you taking me between my legs.", If (player.selling,1,0)),
                ])
                pc "[dialouge]"

                $ dialouge = WeightedChoice([
                ("Mmmm.", 1),
                ("I planned to anyway.", 1),
                ("Where else would I put it?", 1),
                ("Like the perfect slut.", If (player.isslut,1,0)),
                ("Good whore.", If (player.selling,1,0)),
                ("Like all the best whores.", If (player.selling,1,0)),
                ])
                guy "[dialouge]"
                show sb_againstwall2 pokevaghand with dissolve
            "Take me in the bum" if player.check_anal_agree():
                $ player.want_sexlocation = "anal"
                $ dialouge = WeightedChoice([
                ("Fuck me in the arse.", If (not player.selling,1,0)),
                ("Take me in the bum.", If (not player.selling,1,0)),
                ("Mm, I want to feel you up my bum.", If (not player.selling,1,0)),
                ("Hmm, how about you take me in the arse?", If (not player.selling,1,0)),
                ("To be safe you should take me in the arse.", If (player.selling,1,0)),
                ("Best if you put it up my bum.", If (player.selling,1,0)),
                ])
                pc "[dialouge]"

                if player.check_speech(2):
                    $ dialouge = WeightedChoice([
                    ("Really? Okay I can deal with that.", 1),
                    ("No problem. Would love to fuck you in the arse.", 1),
                    ("Sounds good.", 1),
                    ("No problem putting it in your arse.", 1),
                    ])
                    guy "[dialouge]"
                    $ player.have_sexlocation = "anal"
                else:

                    if player.selling:
                        $ dialouge = WeightedChoice([
                        ("No way, I am paying to fuck your pussy!", 1),
                        ("What? I expected to fuck you in the pussy.", 1),
                        ("Since when did whores worry about what hole to use?", 1),
                        ])
                        guy "[dialouge]"
                    else:
                        $ dialouge = WeightedChoice([
                        ("What? I want to fuck you in the pussy.", 1),
                        ("What? After all this you are sheepish about being fucked in the pussy?", 1),
                        ("Really? I want to take you in the pussy.", 1),
                        ])
                        guy "[dialouge]"
                    if player.vvirgin == True:
                        if player.soldprice > 0:
                            pcm "Selling my virginity for £[player.soldprice] just feels dirty..."
                        else:
                            pcm "Not really ready to lose my virginity..."
                        $ dialouge = WeightedChoice([
                        ("Sorry mate, In my bum or nothing.", 1),
                        ("Sorry mate, bum only", 1),
                        ("No, take me in the arse or nothing at all.", 1),
                        ("Sorry mate. My pussy is off limits.", 1),
                        ])
                        pc "[dialouge]"
                        if player.check_speech(2):
                            $ player.have_sexlocation = "anal"

                    elif player.preg_knows:
                        $ dialouge = WeightedChoice([
                        ("Sorry mate, rather you put it in my ass while I am pregnant.", 1),
                        ("Sorry mate. My pussy is off limits while I am pregnant.", 1),
                        ])
                        pc "[dialouge]"
                        if player.check_speech(1):
                            $ player.have_sexlocation = "anal"
                    elif player.pregpills == False and player.cycle_conditions["stage"] == "ovulate":
                        $ dialouge = WeightedChoice([
                        ("It's not a good time of the month to be taking you there.", 1),
                        ("Taking you there at this time of the month is a bad idea.", 1),
                        ("No, right now is a terrible time of the month to be taking you there.", 1),
                        ("Now is a dangerous time and I don't feel like getting knocked up today.", 1),
                        ])
                        pc "[dialouge]"
                        if player.check_speech(1):
                            $ player.have_sexlocation = "anal"
                    else:
                        $ dialouge = WeightedChoice([
                        ("I don't really feel like carrying your baby round for the next few seasons.", 1),
                        ("Not interested in having your child in me.", 1),
                        ("No, getting knocked up is not a good idea.", 1),
                        ])
                        pc "[dialouge]"
                        if player.check_speech(2):
                            $ player.have_sexlocation = "anal"
                    $ dialouge = WeightedChoice([
                    ("Ok, whatever. A hole is a hole.", 1),
                    ("Whatever. I'll take your arse if you insist.", 1),
                    ("Ok, if you say so.", 1),
                    ("Ok, guess it's fine.", 1),
                    ])
                    guy "[dialouge]"
            "Say nothing":

                $ player.want_sexlocation = ""

    $ rand_choice = WeightedChoice([
    ("school_rep_sex_vag", If (player.have_sexlocation == "", 40,0)),
    ("school_rep_sex_ass", If (player.have_sexlocation == "", 10,0)),
    ("school_rep_sex_vag", If (player.have_sexlocation == "vag", 1,0)),
    ("school_rep_sex_ass", If (player.have_sexlocation == "anal", 1,0))
    ])
    jump expression rand_choice

label school_rep_sex_vag:

    if player.vvirgin:
        jump school_rep_sex_vag_virgin


    show sb_againstwall2 pokevaghand with dissolve
    $ dialouge = WeightedChoice([
    ("I feel his cock sliding between my lips as he wanks himself off a bit.", 1),
    ("I can feel him stroking his cock as the tip of his penis slides between my wet folds.", 1),
    ])
    "[dialouge]"
    show sb_againstwall2 pokevag with dissolve
    if player.want_sexlocation == "anal":
        $ dialouge = WeightedChoice([
        ("(He is starting to poke me instead of switching to my arse...", 1),
        ("(His cock should be wet enough already so he should have already put it somewhere else...", 1),
        ("(Ah, he is starting to push deeper. If I let this go on he might end up trying to fill my pussy...", 1),
        ])
        pc "[dialouge]"

        $ dialouge = WeightedChoice([
        ("That's not my arse you are poking.", 1),
        ("You are poking at the wrong hole.", 1),
        ("Wrong hole, I told you to take me in the bum.", 1),
        ])
        pc "[dialouge]"
        if player.check_speech(3):
            $ dialouge = WeightedChoice([
            ("I know. Just getting lubed up.", 1),
            ("Ah yeah...", 1),
            ("Did you? Okay sure.", 1),
            ("Don't worry, just getting it ready.", 1),
            ("Mmm, I know.", 1),
            ("Uh huh. Just having a bit of fun where it's wet.", 1),
            ])
            guy "[dialouge]"
            jump school_rep_sex_ass
        else:
            if (not player.check_sex_agree(3)) or (not player.pregpills and player.cycle_conditions["stage"] == "ovulate" and not player.has_perk(perk_preg_want)) or (player.vvirgin):
                jump school_rep_sex_forcesex
            else:
                $ dialouge = WeightedChoice([
                ("I know. Just have some fun with it.", 1),
                ("Mmm, it's so nice here.", 1),
                ("So warm and wet here.", 1),
                ("You are so wet. Sure you want it in the arse?", 1),
                ])
                guy "[dialouge]"

    $ dialouge = WeightedChoice([
    ("His cock starts to push deeper and I feel him slowly start to stretch my pussy and fill me up inside.", 1),
    ("I feel him start to enter deeper and deeper with each poke until he is deep enough inside me that it's no longer poking but actual fucking.", 1),
    ("He gently starts to press his cock against me and in a very slow thrust, stretches my lips and starts to enter me fully.", 1),
    ])
    "[dialouge]"


    $ player.sex_vag(schoolguy)
    $ player.face_excited()
    show sb_againstwall2 insidevag ag wink with dissolve
    if player.want_sexlocation == "anal":
        $ dialouge = WeightedChoice([
        ("Ahhh. \u2665 That's not my bum...", 1),
        ("*Huff* \u2665 Wrong... Hole...", 1),
        ("\u2665", 1),
        ("\u2665 Thats not where I told you to put it.", 1),
        ])
        pc "[dialouge]"
    $ dialouge = WeightedChoice([
    ("I feel him start to take long and deep thrusts inside me. Pushing his cock balls deep into me before pulling almost all the way out, then pushing it back in again. ", 1),
    ("He seems eager and I feel him taking quick and shallow thrusts while gripping onto my hips. He is fucking me like a horny little rabbit.", 1),
    ("He takes it slow and rhythmically thrusts in and out of me. My tits bounce back and forth in time with his thrusting and it feels very pleasant and hypnotic.", 1),
    ("He thrusts deeply into me before slowly sliding his cock out almost all the way. Then aggressively slams back into me in a quick and hard thrust.", 1),
    ])
    "[dialouge]"
    $ dialouge = WeightedChoice([
    ("He starts to get into it more and spanks me or reaches round to grope at my tits as he is thrusting deep inside me.", 1),
    ("He starts to build momentum and it's not long before I hear his body slapping against my ass with each thrust into me.", 1),
    ("He builds up speed as I get used to him inside me and it's not long until he is harshly gripping my sides and pulling me against his thrusting cock.", 1),
    ("I am already soaking wet down there and it doesn't take him long to start hammering away at me. Fucking me hard and fast while smacking me on the arse.", If (player.desire > 80, 1, 0)),
    ("Having a cock in me is a familiar feeling and I start to thrust back against him so he can fill me deeper. He takes notice and grabs my hips and starts to slam into me, gripping hard against me as he thrusts.", If (player.vsex > 10, 1, 0)),
    ])
    "[dialouge]"
    $ randomnum = renpy.random.randint(1, 2)

    if randomnum == 1:
        call school_rep_sex_spank from _call_school_rep_sex_spank

    $ dialouge = WeightedChoice([
    ("Ah fuck this is so nice. You are such a dirty girl!", 1),
    ("Ah yes this is so nice. You are gripping onto my cock!", 1),
    ("Ah fuck you are so warm. So nice having my cock in you.", 1),
    ("Damn you are soaked. Sexy girl, you want this more than me.", If (player.desire > 80, 1, 0)),
    ("Ah fuck, yes keep going like that. Fuck you are such a horny bitch.", If (player.desire > 80, 1, 0)),
    ("Ah fuck so nice. You know perfectly how to make a man feel good.", If (player.vsex > 10, 1, 0)),
    ])
    guy "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Haaaaa... \u2665", 1),
    ("Ah fuck!", 1),
    ("Yes! Yes! Yes!", 1),
    ("Keep going! Fuck yes! Fuck me! Fuck me!", If (player.desire > 80, 1, 0)),
    ("Ahhhhh \u2665 Fuuuuck! \u2665 Take me!", If (player.desire > 80, 1, 0)),
    ])
    pc "[dialouge]"
    $ dialouge = WeightedChoice([
    ("My mind starts to lose focus as I focus only on the cock thrusting in and out of me. I can feel the pleasure building up inside me.", 1),
    ("My mind goes blank as I focus only on the approaching orgasm gripping my body.", 1),
    ("My pussy starts to tighten around his cock as he brings me closer and closer to orgasm.", 1),
    ("I focus only on the man behind me pounding his nice cock in and out of me. I can barely focus as he brings my dripping pussy to orgasm.", If (player.desire > 80, 1, 0)),
    ])
    "[dialouge]"
    $ player.face_orgasm()
    $ dialouge = WeightedChoice([
    ("Yes, yes! \u2665", 1),
    ("Ahhhhh!", 1),
    ("Yes! Yes! Yes!", 1),
    ("Ahhh I am close~.", 1),
    ("Ahhhhh \u2665", 1),
    ])
    pc "[dialouge]"
    jump school_rep_sex_vag_cum

label school_rep_sex_vag_cum:

    if player.check_pullout():
        menu:
            "Mmm, fill me up!" if not player.has_perk(perk_preg_notwant):

                jump school_rep_sex_vag_cum_want
            "Pull out, not inside.":

                if player.check_speech(2):
                    $ randomnum = renpy.random.randint(1, 30)
                    if randomnum == 1 and player.check_anal_agree():
                        jump school_rep_sex_vag_cum_pullout_switch_anal
                    else:
                        jump school_rep_sex_cum_pullout
                else:
                    jump school_rep_sex_vag_cum_notwant
    else:


        jump school_rep_sex_vag_cum_want

label school_rep_sex_ass:
    show sb_againstwall2 pokevaghand with dissolve
    pause 0.5
    show sb_againstwall2 pokeasshand with dissolve
    show sb_againstwall2 pokeass with dissolve
    $ dialouge = WeightedChoice([
    ("I feel slide his cock from my wet vagina and press it against my asshole while masturbating.", 1),
    ("He rubs his cock between my legs, making sure it is nice and slick before pressing it against me asshole.", 1),
    ("He presses his already lubed cock against my ass and he starts to masturbate while putting pressure against it.", 1),
    ("His cock is covered in my juices as he presses it against my asshole, ready to start sliding it inside me.", 1),
    ])
    "[dialouge]"



    $ player.sex_anal(schoolguy)
    $ player.face_excited()
    show sb_againstwall2 insideass ag wink with dissolve
    $ dialouge = WeightedChoice([
    ("He then gently presses it harder against my ass until I feel it easing its way deeper into my arse. Slowly until it is all the way inside me filling me up.", 1),
    ("He wiggles his cock against my asshole as he slowly presses it more firmly against me. It starts to slide inside me until I can feel his pelvis press against my ass checks.", 1),
    ("He gently prods against my asshole, with each prod sliding his cock a little deeper inside me. Eventually the prods turn to thrusting and I realise he has already got it all the way in and is fucking me.", 1),
    ("I gently ease back onto his slick cock and feel him start to enter me. Sliding inside deeper and deeper until he is all the way in.", 1),
    ])
    "[dialouge]"
    guy "Ahhhhhh so warm."
    if player.asex == 0:
        pc "Ahhh fuck! Ahhhhhahhhhh..."
        pc "Nnnnnggggggg."
        pcm "Fuck, never had it in the ass before and without proper lube, this fucking hurts..."
    elif player.asex <= 5:
        pc "Ahhhhh fuck..."
        pcm "I hope this gets easier the more I do it..."
    else:
        $ dialouge = WeightedChoice([
        ("Ahhh \u2665 You are so big!", 1),
        ("Ah fuck! It feels so huge inside me.", 1),
        ("Ah shit. You are opening me up.", 1),
        ("Ahhh haaa, it is so big. It totally fills me up.", 1),
        ])
        pc "[dialouge]"

    pc "Haaaa ♥"
    $ dialouge = WeightedChoice([
    ("He relentlessly fucks me in the ass while pressing me up against the wall. I feel his hard cock pumping in and out as he roughly grips onto my ass cheeks, spreading them so he can thrust in deeper.", 1),
    ("He slowly starts to pick up the pace and places his hands on my arse cheeks, spreading them while also using them as handholds to pull me deeper onto his cock.", 1),
    ("He spreads me as he slowly fucks me in the arse. He starts out gentle but starts picking up the pace once he realises I have adjusted to his huge cock filling me up.", 1),
    ("He seems to take pleasure in pulling his cock out right to the tip, then grabbing me by the hips and pulling me balls deep back onto his cock. While it is a bit rough, it is not without its pleasure.", 1),
    ("He barely waits for me to adjust to him being in my ass before he is pounding away at me with determination. He is gripping onto my hips and thrusting like a madman. While it does hurt a bit, it's far more pleasurable than painful.", 1),
    ])
    "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Haaaaa... \u2665", 1),
    ("Ah fuck!", 1),
    ("Yes! Yes! Yes!", 1),
    ("Keep going! Fuck yes! Fuck me! Fuck me!", If (player.desire > 80, 1, 0)),
    ("Ahhhhh \u2665 Fuuuuck! \u2665 Take me!", If (player.desire > 80, 1, 0)),
    ])
    pc "[dialouge]"
    $ dialouge = WeightedChoice([
    ("He keeps pounding away while groaning or muttering some dirty words. He doesn't make much sense though as he is lost in the pleasure of fucking me in the ass.", 1),
    ("He rhythmically fucks my asshole and I get lost in the hypnotic pleasure it brings. My breasts swinging back and forth in time with each thrust.", 1),
    ("I hear my ass cheeks clapping against his body as he continuously thrusts in and out of me. I find the rhythms and sound quite exciting and get lost in the pleasure of it all.", 1),
    ("He grips me by the hips and thrusts into me again and again, my ass clapping against his body each time.", 1),
    ])
    "[dialouge]"
    if randomnum == 1:
        call school_rep_sex_spank from _call_school_rep_sex_spank_1

    $ dialouge = WeightedChoice([
    ("Ah fuck this is so nice. You are such a dirty girl!", 1),
    ("Ah yes this is so nice. You are gripping onto my cock!", 1),
    ("Ah fuck you are so warm. So nice having my cock in you.", 1),
    ("Damn fucking your ass is great, seems they are teaching you good things in school.", If (player.desire > 80, 1, 0)),
    ("Ah fuck, yes keep going like that. Fuck you are such a horny bitch.", If (player.desire > 80, 1, 0)),
    ("Ah fuck so nice. You know perfectly how to make a man feel good.", If (player.vsex > 10, 1, 0)),
    ])
    guy "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Haaaaa... \u2665", 1),
    ("Ah fuck!", 1),
    ("Yes! Yes! Yes!", 1),
    ("Keep going! Fuck yes! Fuck me! Fuck me!", If (player.desire > 80, 1, 0)),
    ("Ahhhhh \u2665 Fuuuuck! \u2665 Take me!", If (player.desire > 80, 1, 0)),
    ])
    pc "[dialouge]"

    $ dialouge = WeightedChoice([
    ("His grip on me starts to get stronger and a little painful as he gets more and more excited. His breathing is now getting more ragged with each thrust.", 1),
    ("His grip on my cheeks is now hard enough to leave marks on my skin as his thrusts start to become erratic. He is clearly enjoying this and may not last much longer.", 1),
    ("His hands are all over my body as he starts to put himself over the edge. His breathing becoming heavy and he starts to thrust much more aggressively into me.", 1),
    ("He grips me by the hips and thrusts into me again and again, my ass clapping against his body each time.", 1),
    ])
    "[dialouge]"

    $ dialouge = WeightedChoice([
    ("His grip on me starts to get stronger and a little painful as he gets more and more excited. His breathing is now getting more ragged with each thrust.", 1),
    ("His grip on my cheeks is now hard enough to leave marks on my skin as his thrusts start to become erratic. He is clearly enjoying this and may not last much longer.", 1),
    ("His hands are all over my body as he starts to put himself over the edge. His breathing becoming heavy and he starts to thrust much more aggressively into me.", 1),
    ("He grips me by the hips and thrusts into me again and again, my ass clapping against his body each time.", 1),
    ])
    "[dialouge]"

    $ dialouge = WeightedChoice([
    ("He must be close... And so am I, despite his cock being in my ass and not my pussy.", 1),
    ("I can feel myself close to orgasm despite the fact he is fucking me in the ass and not in my vagina.", 1),
    ("My body starts to tense up as I get closer to orgasm. Unexpected as it is my ass he is fucking.", 1),
    ("My body starts to quiver as his ass fucking brings me closer and closer to orgasm.", 1),
    ])
    "[dialouge]"
    $ player.face_orgasm()
    $ dialouge = WeightedChoice([
    ("Ahhh, I'm about to come!", 1),
    ("Ah fuck I am close...", 1),
    ("Fuck so good. I am not going to last much longer.", 1),
    ("Ah yes! I am cumming!", 1),
    ])
    guy "[dialouge]"
    $ player.face_orgasm()
    $ dialouge = WeightedChoice([
    ("Yes, yes! \u2665", 1),
    ("Ahhhhh!", 1),
    ("Yes! Yes! Yes!", 1),
    ("Ahhh so am I~.", 1),
    ("Ahhhhh \u2665", 1),
    ])
    pc "[dialouge]"

    jump school_rep_sex_ass_cum

label school_rep_sex_ass_cum:

    if player.check_pullout():
        jump school_rep_sex_ass_cum_want
    else:

        menu:
            "Mmm, fill me up!":

                jump school_rep_sex_ass_cum_want
            "Mmm. Pull out and cover me with your cum!":

                if player.check_speech(2):
                    jump school_rep_sex_cum_pullout
                else:

                    jump school_rep_sex_ass_cum_notwant

label school_rep_sex_vag_cum_want:
    $ dialouge = WeightedChoice([
    ("Fuck! I want my first time to end with me being cummed in!", If (player.virgin_pregcheck, 100, 0)),
    ("Ahh! Cum in my virgin pussy!", If (player.virgin_pregcheck, 100, 0)),
    ("Cum inside me.", 1),
    ("You can finish inside me if you want.", 1),
    ("Keep going. Don't stop.", 1),
    ("Yes keep going. \u2665", 1),
    ("I'm close. Don't pull out! \u2665", 1),
    ("Ahh it feels so nice. Don't take it out. \u2665", 1),
    ("Keep going. Yes! Don't stop! \u2665", 1),
    ("Ah yes! \u2665", 1),
    ("I can feel you. Don't you dare pull out!", If (player.has_perk(perk_preg_want), 1, 0)),
    ("Don't pull out. I want to feel you cum inside me! \u2665", If (player.has_perk(perk_preg_want), 1, 0)),
    ("Keep going. Cum inside and give me what I want. \u2665", If (player.has_perk(perk_preg_want), 1, 0)),
    ("Ahh wait. Ahh fuck yes. Stop! Keep going!", If (player.has_perk(perk_preg_notwant), 1, 0)),
    ("Ah fuck yes. Haa, be careful...", If (player.has_perk(perk_preg_notwant), 1, 0)),
    ("Ah fuck unload in me like a slut!", If (player.isslut, 1, 0)),
    ("Ah yes! Get ready to brand me like a slut.", If (player.isslut, 1, 0)),
    ("Keep going. I love it when men cum inside me.", If (player.isslut, 1, 0)),
    ])
    pc "[dialouge]"
    pc "♥"

    $ dialouge = WeightedChoice([
    ("Ah you dirty bitch. Take it inside.", 1),
    ("Ah fuck I'm gonna put it inside you.", 1),
    ("Ah yes. Take it.", 1),
    ("Ah I am cumming!", 1),
    ("Nng fuck I am cumming.", 1),
    ("Come here and let me fill you up.", 1),
    ("Yes, yes!", 1),
    ("Ah yes! I am going to fill you up.", 1),
    ("Ah get ready for carrying my baby!", If (player.has_perk(perk_preg_want), 1, 0)),
    ("Haaa fuck I am going to knock you up!", If (player.has_perk(perk_preg_want), 1, 0)),
    ("Get ready for my baby you bitch.", If (player.has_perk(perk_preg_want), 1, 0)),
    ("Ahhh yes take it deep inside. Hope you're feeling lucky.", If (player.has_perk(perk_preg_notwant), 1, 0)),
    ("Better hope you are lucky cos I am going to fill you up!", If (player.has_perk(perk_preg_notwant), 1, 0)),
    ("You dirty slut. Take me inside you.", If (player.isslut, 1, 0)),
    ("Ah fuck yes you filthy slut.", If (player.isslut, 1, 0)),
    ])
    guy "[dialouge]"

    $ player.sex_cum(schoolguy, "inside")
    $ dialouge = WeightedChoice([
    ("He thrusts deep inside me and keeps his cock buried inside me, making sure he puts everything deep in me.", 1),
    ("I can feel him gripping my hips and pulling me balls deep on his throbbing cock. Unloading everything inside me.", 1),
    ("His cock pulses inside me, unloading his cum deep inside me.", 1),
    ("I push back on his cock as it throbs inside me, making sure everything goes inside me.", 1),
    ("Lost in the throes of orgasm I keep bouncing on his cock even as I feel him cumming inside me and filling me up.", 1),
    ("Him cumming inside me does nothing to slow me from humping his cock to get the most pleasure from my own orgasm.", 1),
    ("I feel his cock pumping me full of cum and hope he is lucky enough to put a baby inside me.", If (player.has_perk(perk_preg_want), 1, 0)),
    ("I feel euphoric as he tries to knock me up by pushing his cock balls deep inside me while it throbs and fill me full of his cum.", If (player.has_perk(perk_preg_want), 1, 0)),
    ("I feel like a right bitch as I hope he can knock me up while cumming inside me.", If (player.has_perk(perk_preg_want), 1, 0)),
    ("I have mixed feelings as I feel his cock throbbing inside me, ready to try and get me pregnant.", If (player.has_perk(perk_preg_notwant), 1, 0)),
    ("I am caught between euphoria and dread as I orgasm on a cock that is trying to put a child inside me.", If (player.has_perk(perk_preg_notwant), 1, 0)),
    ("The familiar feeling of a man fulling my insides full of his cum fills me with excitement.", If (player.isslut, 1, 0)),
    ("Like so many men before, I am filled with euphoria as one of them fills me with their cum.", If (player.isslut, 1, 0)),
    ])
    "[dialouge]"
    show sb_againstwall2 happy with dissolve
    pc "Ahh yes."

    $ dialouge = WeightedChoice([
    ("Ahhh. I can feel it throbbing in me.", 1),
    ("Mmmmm \u2665 I can feel you pumping it in!", 1),
    ("Ah yes. Fill me up.", If (player.has_perk(perk_preg_notwant), 0, 1)),
    ("Haaaaaaaa \u2665", 1),
    ("Mmmmmmmmm \u2665", 1),
    ("Ohhh I feel it throbbing. \u2665", 1),
    ("Yes pump it in me! \u2665", If (player.has_perk(perk_preg_notwant), 0, 1)),
    ("Ah yes! \u2665", 1),
    ("Mmmm pump it in. Make me fat.", If (player.has_perk(perk_preg_want), 1, 0)),
    ("You going to make me carry your baby round for the next few seasons? \u2665", If (player.has_perk(perk_preg_want), 1, 0)),
    ("Mmmm, are you gonna give me huge milk tits? \u2665", If (player.has_perk(perk_preg_want), 1, 0)),
    ("Mmmm I can feel it. But you better not get me pregnant.", If (player.has_perk(perk_preg_notwant), 1, 0)),
    ("Mmmm so nice. Even if there is some risk...", If (player.has_perk(perk_preg_notwant), 1, 0)),
    ("Mmmm. I never get bored of men filling me up.", If (player.isslut, 1, 0)),
    ("Ah yes! Brand me like the slut I am.", If (player.isslut, 1, 0)),
    ("Ahhh! No matter how many guys come in me, I love it every time.", If (player.isslut, 1, 0)),
    ])
    pc "[dialouge]"

    jump school_rep_sex_end

label school_rep_sex_vag_cum_notwant:
    $ dialouge = WeightedChoice([
    ("Pull out. Don't cum inside me.", 1),
    ("Take it out and cum on my ass.", 1),
    ("*Huff* Take it out and put it on my ass.", 1),
    ("Ah yes, cum on my ass. \u2665", 1),
    ("Ahh! \u2665 Not inside...", 1),
    ("Ahh take it out. Cum over me. \u2665", 1),
    ("Make sure to pull out! \u2665", 1),
    ("Ah yes! Cum over me! \u2665", 1),
    ("Ahh wait. Take it out and cum somewhere else! I am not protected.", If (player.has_perk(perk_preg_notwant), 1, 0)),
    ("Don't finish inside me, I don't have protection.", If (player.has_perk(perk_preg_notwant), 1, 0)),
    ("Ah fuck unload it on my arse! Cover me in your cum!", If (player.isslut, 1, 0)),
    ("Ah yes! Get ready to cover me like a slut.", If (player.isslut, 1, 0)),
    ("Come on my ass. I love it when men cover me with it.", If (player.isslut, 1, 0)),
    ])
    pc "[dialouge]"

    $ dialouge = WeightedChoice([
    ("Ah you dirty bitch. Take it inside.", 1),
    ("Ah fuck I'm gonna put it inside you.", 1),
    ("Fuck that. Take it inside!", 1),
    ("Ah I am cumming! Can't stop!", 1),
    ("Nng fuck I am cumming.", 1),
    ("I want to fill you up.", 1),
    ("Yes, yes!", 1),
    ("Ah yes! I am going to fill you up.", 1),
    ("Ah get ready for carrying my baby!", If (not player.pregnancy > 1, 1, 0)),
    ("Haaa fuck I am going to knock you up!", If (not player.pregnancy > 1, 1, 0)),
    ("Get ready for my baby you bitch.", If (not player.pregnancy > 1, 1, 0)),
    ("Ahhh yes take it deep inside. Hope you're feeling lucky.", If (not player.pregnancy > 1, 1, 0)),
    ("Better hope you are lucky cos I am going to fill you up!", If (not player.pregnancy > 1, 1, 0)),
    ("Take it you fat bitch!", If (player.pregnancy > 1, 1, 0)),
    ("Ah bet you love this. How you ended up pregnant in the first place.", If (player.pregnancy > 1, 1, 0)),
    ("You dirty slut. Take me inside you.", 1),
    ("Ah fuck yes you filthy slut.", 1),
    ])
    guy "[dialouge]"

    $ player.sex_cum(schoolguy, "inside")
    show sb_againstwall2 shock with dissolve
    $ dialouge = WeightedChoice([
    ("He thrusts deep inside me and keeps his cock buried inside me, making sure he puts everything deep in me.", 1),
    ("I can feel him gripping my hips and pulling me balls deep on his throbbing cock. Unloading everything inside me.", 1),
    ("His cock pulses inside me, unloading his cum deep inside me.", 1),
    ("I try to move away from him, but his hands grip my thighs and pulls me balls deep on his cock as I feel it throb inside me.", 1),
    ("Lost in the throes of orgasm I am too late to pull away when he starts to cum and I just let him stay there even as I feel him cumming inside me and filling me up.", 1),
    ("Caught between my own orgasm and the feeling of him cumming inside me, I fail to get him to pull out properly and he unloads everything inside me.", 1),
    ("I feel his cock pumping me full of cum and my stomach sinks as I realise that now is a dangerous time to be having a man's cum inside me.", If (player.cycle_conditions["stage"] == "ovulate", 1, 0)),
    ("My orgasm is cut short as I realise that right now is a terrible time of the month to let a man cum inside.", If (player.cycle_conditions["stage"] == "ovulate", 1, 0)),
    ("He grips my hips and pushes his cock deep inside me. I am hit by a wave of terror as I realise right now is the most fertile time of the month.", If (player.cycle_conditions["stage"] == "ovulate", 1, 0)),
    ("I am caught between orgasm and trying to resist the guys attempts to cum inside but the feeling of his throbbing let's me know I didnt do a good enough job of getting off his cock.", 1),
    ("I feel the arsehole throbbing inside me and am filled with horror as I realise he could be getting me pregnant right now.", If (player.has_perk(perk_preg_notwant), 1, 0)),
    ])
    "[dialouge]"
    guy "Ahh yes."
    pc "Ah what are you doing?"
    if player.pregpills:
        $ dialouge = WeightedChoice([
        ("You are lucky I am on the pill or I would kick you for ignoring me and cumming inside.", 1),
        ("*Sigh* I told you to pull out. Now I am going to be leaking.", 1),
        ("Idiot. You are going to have me leaking now.", 1),
        ("Does \"pull out\" mean nothing to you? I'm going to have your cum trickling out of me for ages now...", 1),
        ("*Tsk* What did you go and do that for? You are going to have me leaking now...", 1),
        ])
        pc "[dialouge]"
    else:
        $ dialouge = WeightedChoice([
        ("What the hell? I don't want to be ending up with your shitty child in my belly.", 1),
        ("Idiot. I don't want to be carrying your baby around for the next few seasons.", 1),
        ("You do that on purpose or something? I don't want your accident in me.", 1),
        ("You trying to get me pregnant?", 1),
        ("Fuck, \"pull out\" mean nothing to you? I don't want your baby in me.", 1),
        ])
        pc "[dialouge]"
    $ dialouge = WeightedChoice([
    ("*Huff* It was too nice being inside you to pull out.", 1),
    ("Ah I didn't hear you. Was too busy enjoying that pussy of yours.", 1),
    ("Sorry, I thought I could last longer...", 1),
    ("It felt far too nice to stop.", 1),
    ("Ah it was so good in there.", 1),
    ])
    guy "[dialouge]"
    show sb_againstwall2 frown with dissolve
    pc "*Sigh*"


    jump school_rep_sex_end

label school_rep_sex_ass_cum_want:
    $ dialouge = WeightedChoice([
    ("Ah yes. Put it all in my ass!", 1),
    ("Cum inside me.", 1),
    ("You can finish inside me if you want.", 1),
    ("Keep going. Don't stop.", 1),
    ("Yes keep going. \u2665", 1),
    ("I'm close. Don't pull out! \u2665", 1),
    ("Ahh it feels so nice. Don't take it out. \u2665", 1),
    ("Keep going. Yes! Don't stop! \u2665", 1),
    ("Ah yes! \u2665", 1),
    ("Ah fuck unload in me like a slut!", If (player.isslut, 1, 0)),
    ("Ah yes! Get ready to brand me like a slut.", If (player.isslut, 1, 0)),
    ("Keep going. I love it when men cum inside me.", If (player.isslut, 1, 0)),
    ])
    pc "[dialouge]"
    pc "♥"

    $ dialouge = WeightedChoice([
    ("Ah fuck you dirty little butt slut.", 1),
    ("Ah yes! Take it in your arse.", 1),
    ("Ah you dirty bitch. Take it inside.", 1),
    ("Ah fuck I'm gonna put it inside you.", 1),
    ("Ah yes. Take it.", 1),
    ("Ah I am cumming!", 1),
    ("Nng fuck I am cumming.", 1),
    ("Come here and let me fill you up.", 1),
    ("Yes, yes!", 1),
    ("Ah yes! I am going to fill you up.", 1),
    ("You dirty slut. Take me inside you.", If (player.isslut, 1, 0)),
    ("Ah fuck yes you filthy slut.", If (player.isslut, 1, 0)),
    ])
    guy "[dialouge]"
    show sb_againstwall2 happy with dissolve
    $ player.sex_cum(schoolguy, "anal")
    $ dialouge = WeightedChoice([
    ("He spreads my cheeks and pumps his load deep into my ass. Throb after throb unloading more into me.", 1),
    ("I can feel him gripping my hips and pulling me balls deep on his throbbing cock. Unloading everything into my ass.", 1),
    ("His cock pulses inside me, unloading his cum deep in my ass.", 1),
    ("I push back on his cock as it throbs inside me, making sure everything goes inside me.", 1),
    ("Lost in the throes of orgasm I keep bouncing on his cock even as I feel him cumming inside me and filling me up.", 1),
    ("Him cumming inside me does nothing to slow me from humping his cock to get the most pleasure from my own orgasm.", 1),
    ("The familiar feeling of a man fulling my insides full of his cum fills me with excitement.", If (player.isslut, 1, 0)),
    ("Like so many men before, I am filled with euphoria as one of them fills me with their cum.", If (player.isslut, 1, 0)),
    ])
    "[dialouge]"
    guy "Ahh yes."

    $ dialouge = WeightedChoice([
    ("Ahhh. I can feel it throbbing in me.", 1),
    ("Mmmmm \u2665 I can feel you pumping it in!", 1),
    ("Ah yes. Fill me up.", 1),
    ("Ah yes. Pump my arse full!", 1),
    ("Haaaaaaaa \u2665", 1),
    ("Mmmmmmmmm \u2665", 1),
    ("Ohhh I feel it throbbing. \u2665", 1),
    ("Ah yes! \u2665", 1),
    ("Ah yes! Brand me like the slut I am.", If (player.isslut, 1, 0)),
    ("Ahhh! No matter how many guys come in me, I love it every time.", If (player.isslut, 1, 0)),
    ])
    pc "[dialouge]"
    show sb_againstwall2 neutral with dissolve
    jump school_rep_sex_end

label school_rep_sex_ass_cum_notwant:
    $ dialouge = WeightedChoice([
    ("Pull out. Don't cum inside me.", 1),
    ("Take it out and cum on my ass.", 1),
    ("*Huff* Take it out and put it on my ass.", 1),
    ("Ah yes, cum on my ass. \u2665", 1),
    ("Ahh! \u2665 Not inside...", 1),
    ("Ahh take it out. Cum over me. \u2665", 1),
    ("Ah yes! Cum over me! \u2665", 1),
    ("Ah fuck unload it on my arse! Cover me in your cum!", If (player.isslut, 1, 0)),
    ("Ah yes! Get ready to cover me like a slut.", If (player.isslut, 1, 0)),
    ("Come on my ass. I love it when men cover me with it.", If (player.isslut, 1, 0)),
    ])
    pc "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Ah fuck you dirty little butt slut.", 1),
    ("Ah yes! Take it in your arse.", 1),
    ("Ah you dirty bitch. Take it inside.", 1),
    ("Ah fuck I'm gonna put it inside you.", 1),
    ("Ah yes. Take it.", 1),
    ("Ah I am cumming!", 1),
    ("Nng fuck I am cumming.", 1),
    ("Come here and let me fill you up.", 1),
    ("Yes, yes!", 1),
    ("Ah yes! I am going to fill you up.", 1),
    ("You dirty slut. Take me inside you.", If (player.isslut, 1, 0)),
    ("Ah fuck yes you filthy slut.", If (player.isslut, 1, 0)),
    ])
    guy "[dialouge]"

    $ player.sex_cum(schoolguy, "anal")
    $ dialouge = WeightedChoice([
    ("He spreads my cheeks and pumps his load deep into my ass. Throb after throb unloading more into me.", 1),
    ("I can feel him gripping my hips and pulling me balls deep on his throbbing cock. Unloading everything into my ass.", 1),
    ("His cock pulses inside me, unloading his cum deep in my ass.", 1),
    ("Lost in the throes of orgasm I keep bouncing on his cock even as I feel him cumming inside me and filling me up.", 1),
    ("Him cumming inside me does nothing to slow me from humping his cock to get the most pleasure from my own orgasm.", 1),
    ("The familiar feeling of a man fulling my insides full of his cum fills me with excitement.", If (player.isslut, 1, 0)),
    ("Like so many men before, I am filled with euphoria as one of them fills me with their cum.", If (player.isslut, 1, 0)),
    ])
    "[dialouge]"
    guy "Ahh yes."
    show sb_againstwall2 frown with dissolve
    $ dialouge = WeightedChoice([
    ("I told you outside. It's gonna be leaking for the rest of my shift.", 1),
    ("You arse. It's going to be leaking while I work.", 1),
    ("Ugh, I told you outside.", 1),
    ("...", 1),
    ("Now it's going to get all sticky...", 1),
    ("*Sigh* It's going to get all sticky and make it hard to walk", 1),
    ("*Sigh* Just cum where you want why don't you?", 1),
    ("Just because you are paying me, doesn't mean you can just ignore me.", If (player.soldprice, 1, 0)),
    ])
    pc "[dialouge]"
    $ dialouge = WeightedChoice([
    ("*Huff* It was too nice being inside you to pull out.", 1),
    ("Ah I didn't hear you. Was too busy enjoying that pussy of yours.", 1),
    ("Sorry, I thought I could last longer...", 1),
    ("It felt far too nice to stop.", 1),
    ("Ah it was so good in there.", 1),
    ])
    guy "[dialouge]"
    pc "*Sigh*"
    pc "Whatever..."
    jump school_rep_sex_end

label school_rep_sex_cum_pullout:

    $ dialouge = WeightedChoice([
    ("Pull out. Don't cum inside me.", 1),
    ("Take it out and cum on my ass.", 1),
    ("*Huff* Take it out and put it on my ass.", 1),
    ("Ah yes, cum on my ass. \u2665", 1),
    ("Ahh! \u2665 Not inside...", 1),
    ("Ahh take it out. Cum over me. \u2665", 1),
    ("Make sure to pull out! \u2665", 1),
    ("Ah yes! Cum over me! \u2665", 1),
    ("Ah fuck unload it on my arse! Cover me in your cum!", If (player.isslut, 1, 0)),
    ("Ah yes! Get ready to cover me like a slut.", If (player.isslut, 1, 0)),
    ("Come on my ass. I love it when men cover me with it.", If (player.isslut, 1, 0)),
    ])
    pc "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Ahh yes you dirty slut. Take it over you!", 1),
    ("Ah yes! Take it on your arse.", 1),
    ("Ah you dirty bitch. Take it all over you.", 1),
    ("Ah fuck I'm gonna cover you in it.", 1),
    ("Ah yes. Take it over you.", 1),
    ("Ah I am cumming!", 1),
    ("Nng fuck I am cumming.", 1),
    ("Yes, yes!", 1),
    ("Ah yes! I am going to cover you with my cum.", 1),
    ("You dirty slut. Take me over you.", If (player.isslut, 1, 0)),
    ("Ah fuck yes you filthy slut.", If (player.isslut, 1, 0)),
    ])
    guy "[dialouge]"
    show sb_againstwall2 cum with dissolve
    $ player.sex_cum(schoolguy, "ass")
    $ dialouge = WeightedChoice([
    ("He pulls out and starts to come on my pussy lips and arse.", 1),
    ("He pulls out and I can feel his warm cum hitting my naked arse.", 1),
    ("He pulls his cock out and starts jerking it. I can hear him moaning as he cums all over my bum.", 1),
    ("He pulls out at the last moment and with a loud grunt, I feel him spraying his load all over my arse and pussy.", 1),
    ("He pulls his cock out of me then presses his cockhead against my arsehole. I feel it throbbing as he grunts and then a warm trickle running down my arsehole and pussy.", 1),
    ("He pulls out and furiously masturbates as he starts to groan. He sprays his load all over my ass cheeks and the back of my thighs. He then rubs his cock against my arsehole to get the last bits out.", 1),
    ("He pulls out and masturbates with one hand while gripping my arse cheek with the other. I feel him cumming over my bum and then he uses his hand to rub it all over my cheeks and between my legs.", 1),
    ("He pulls out and humps his cock between my bum cheeks. I can hear him groaning at the same time as I feel a wet warmth on my lower back. He slows as I start to feel the wetness run down to my arse and pussy.", 1),
    ])
    "[dialouge]"
    guy "Ahh yes!"
    $ dialouge = WeightedChoice([
    ("Mmmmm \u2665 I can feel it on my arse.", 1),
    ("Mmm. I can feel you have put it all over me.", 1),
    ("Ah yes. Put it all on me!", 1),
    ("Ah yes. Cover me in your cum!", 1),
    ("Ahh. \u2665 Now I am even wetter than when we started.", 1),
    ("Mmmm. I hope it's true that this stuff makes a good skin cream. \u2665", 1),
    ])
    pc "[dialouge]"

    jump school_rep_sex_end

label school_rep_sex_vag_cum_pullout_switch_anal:
    $ dialouge = WeightedChoice([
    ("Pull out. Don't cum inside me.", 1),
    ("Take it out and cum on my ass.", 1),
    ("*Huff* Take it out and put it on my ass.", 1),
    ("Ah yes, cum on my ass. \u2665", 1),
    ("Ahh! \u2665 Not inside...", 1),
    ("Ahh take it out. Cum over me. \u2665", 1),
    ("Make sure to pull out! \u2665", 1),
    ("Ah yes! Cum over me! \u2665", 1),
    ("Ahh wait. Take it out and cum somewhere else! I am not protected.", If (player.has_perk(perk_preg_notwant), 1, 0)),
    ("Don't finish inside me, I don't have protection.", If (player.has_perk(perk_preg_notwant), 1, 0)),
    ("Ah fuck unload it on my arse! Cover me in your cum!", If (player.isslut, 1, 0)),
    ("Ah yes! Get ready to cover me like a slut.", If (player.isslut, 1, 0)),
    ("Come on my ass. I love it when men cover me with it.", If (player.isslut, 1, 0)),
    ])
    pc "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Then I'll put it somewhere else warm.", 1),
    ("If not your pussy, then...", 1),
    ("Then take it in your arse!", 1),
    ("Ah then I'm gonna fuck your arse.", 1),
    ("I paid to put it somewhere warm. Then take it in your arse.", If (player.selling, 1, 0)),
    ("Ah you shitty whore. Take it in your arse then.", If (player.selling, 1, 0)),
    ("AH, then in your arse. Slut like you probably have enough cocks in there for it to be ready.", If (player.isslut, 1, 0)),
    ("Ah pulling out of a slut like you? Na, take it in the arse instead.", If (player.isslut, 1, 0)),
    ])
    guy "[dialouge]"
    show sb_againstwall2 pokevag with dissolve
    show sb_againstwall2 pokeass with dissolve
    $ player.sex_anal(schoolguy)
    show sb_againstwall2 insideass with dissolve
    $ dialouge = WeightedChoice([
    ("I feel slide his cock out of my wet vagina and press it against my asshole and slide it inside.", 1),
    ("He pulls his cock out of my vagina and presses it against my asshole. Already slick with my juices and precum, he is able to easily penetrate me without issue.", 1),
    ("He pulls out of my vagina and presses his already lubed cock against my ass and he starts to masturbate while putting pressure against it and gently sliding it inside me.", 1),
    ("He pulls out and his cock is covered in my juices as he presses it against my asshole, wasting no time to start sliding it inside me.", 1),
    ])
    "[dialouge]"
    pc "♥"

    $ player.sex_cum(schoolguy, "anal")
    $ dialouge = WeightedChoice([
    ("He spreads my cheeks and pumps his load deep into my ass. Throb after throb unloading more into me.", 1),
    ("I can feel him gripping my hips and pulling me balls deep on his throbbing cock. Unloading everything into my ass.", 1),
    ("His cock pulses inside me, unloading his cum deep in my ass.", 1),
    ("I push back on his cock as it throbs inside me, making sure everything goes inside me.", 1),
    ("Lost in the throes of orgasm I keep bouncing on his cock even as I feel him cumming inside me and filling me up.", 1),
    ("Him cumming inside me does nothing to slow me from humping his cock to get the most pleasure from my own orgasm.", 1),
    ("The familiar feeling of a man fulling my insides full of his cum fills me with excitement.", If (player.isslut, 1, 0)),
    ("Like so many men before, I am filled with euphoria as one of them fills me with their cum.", If (player.isslut, 1, 0)),
    ])
    "[dialouge]"
    guy "Ahh yes."

    $ dialouge = WeightedChoice([
    ("Ahhh. I can feel it throbbing in me.", 1),
    ("Mmmmm \u2665 I can feel you pumping it in!", 1),
    ("Ah yes. Fill me up.", 1),
    ("Ah yes. Pump my arse full!", 1),
    ("Haaaaaaaa \u2665", 1),
    ("Mmmmmmmmm \u2665", 1),
    ("Ohhh I feel it throbbing. \u2665", 1),
    ("Ah yes! \u2665", 1),
    ("Ah yes! Brand me like the slut I am.", If (player.isslut, 1, 0)),
    ("Ahhh! No matter how many guys come in me, I love it every time.", If (player.isslut, 1, 0)),
    ])
    pc "[dialouge]"

    jump school_rep_sex_end

label school_rep_sex_end:
    if renpy.showing("sb_againstwall2"):
        show sb_againstwall2 pokevag with dissolve
    if renpy.showing("sb_againstwall2"):
        show sb_againstwall2 noman with dissolve
    else:
        $ renpy.scene()
    with dissolve
    $ dialouge = WeightedChoice([
    ("That was fun.", 1),
    ("Should do that again some time.", 1),
    ("Next time maybe we should try something more.", 1),
    ])
    pc "[dialouge]"
    if renpy.showing(("sb_againstwall2")):
        show sb_againstwall2 noman with dissolve
    $ dialouge = WeightedChoice([
    ("Mmm, next time I should put it in your mouth.", 1),
    ("Should try one of your holes next time.", 1),
    ("Mmm, would love to do that again.", 1),
    ("Gotta love little sluts. Always ready to please.", 1),
    ("This place is so much nicer with little bitches like you around.", 1),
    ])
    guy "[dialouge]"
    if renpy.showing(("sb_againstwall2")):
        hide sb_againstwall2 with dissolve
    $ dialouge = WeightedChoice([
    ("Heh, well I am going to clean up now so I'll see you round.", 1),
    ("Well, I need to clean up now so see you.", 1),
    ("Sure, but for now I need to clean up your mess so I'll be seeing you.", 1),
    ])
    pc "[dialouge]"
    $ dialouge = WeightedChoice([
    ("I head to the sink and clean up any cum from my body as the guy heads out seemingly pleased with himself.", If (not loc_cur == loc_bushes, 1, 0)),
    ("The guy is clearly quite chuffed with himself as I see him off. I then head over to the sinks to clean up a bit.", If (not loc_cur == loc_bushes, 1, 0)),
    ("I watch the guy head off as I walk over to the sinks to clean off his cum from my body.", If (not loc_cur == loc_bushes, 1, 0)),
    ("The guy heads off looking pretty happy with himself while I clean his cum up as best I can.", 1),
    ("I start cleaning up the guys cum and didn't even notice he had already left.", 1),
    ])
    "[dialouge]"
    if outside:
        $ player.cum_clean_outside()
    else:
        $ player.cum_clean()
    $ pc_dress_slow()
    pause 0.5
    $ acc_dress()
    $ dialouge = WeightedChoice([
    ("There we go. I shouldn't look too much of a mess after that.", 1),
    ("That should be alright. Don't think anyone will be able to notice what I have just done.", 1),
    ("Right, no one should be able to tell I was just playing around.", 1),
    ])
    pcm "[dialouge]"

    jump random_event_school_end_picker

label school_rep_sex_spank:
    $ player.spank()
    show sb_againstwall2 closed shock with dissolve
    $ dialouge = WeightedChoice([
    ("Haa \u2665", 1),
    ("Ooooh!", 1),
    ("Unnngg. \u2665", 1),
    ("Oh yes!", If (player.desire > 80, 1, 0)),
    ("Ah fuck.", If (player.desire > 80, 1, 0)),
    ])
    pc "[dialouge]"
    show sb_againstwall2 wink happy with dissolve
    $ player.spank()
    $ dialouge = WeightedChoice([
    ("Oh you like that?", 1),
    ("Knew a bitch like you would like that.", 1),
    ("Dirty girls always love their ass being beat.", 1),
    ("Knew a dirty slut like you would love that.", If (player.isslut, 1, 0)),
    ("Ah the slut likes being spanked?", If (player.isslut, 1, 0)),
    ("Oh even whores love a good spanking?", If (player.iswhore, 1, 0)),
    ])
    guy "[dialouge]"
    show sb_againstwall2 open vhappy with dissolve
    $ dialouge = WeightedChoice([
    ("Yes! Do it again. \u2665", 1),
    ("Ah fuck!", 1),
    ("Mmmmmm.", 1),
    ("\u2665", 1),
    ("More!", 1),
    ])
    pc "[dialouge]"
    $ player.spank()
    show sb_againstwall2 wink ag with dissolve
    return


label school_rep_sex_forcesex:
    show sb_againstwall2 vagin pain closed angry with dissolve
    $ player.sex_forced(schoolguy)
    $ player.sex_vag(schoolguy)
    $ player.face_angry()
    $ dialouge = WeightedChoice([
    ("His cock starts to push deeper and I feel him slowly start to stretch my pussy and fill me up inside.", 1),
    ("I feel him start to enter deeper and deeper with each poke until he is deep enough inside me that it's no longer poking but actual fucking.", 1),
    ("He gently starts to press his cock against me and in a very slow thrust, stretches my lips and starts to enter me fully.", 1),
    ("He gently starts to press his cock against me and in a very slow thrust, stretches my lips and starts to enter me fully.", 1),
    ])
    "[dialouge]"
    show sb_againstwall2 wink with dissolve
    $ dialouge = WeightedChoice([
    ("Fuck I told you not inside me. Take it out now!", 1),
    ("You deaf? I tld you in my arse. Take it out right fucking now!", 1),
    ("Ah take it out. I told you not to put it in there!", 1),
    ("Ah take it out, now!", 1),
    ])
    pc "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Don't worry, I'll pull out.", 1),
    ("It's ok. I'll try not to cum inside.", 1),
    ("Don't worry. Just relax and enjoy.", 1),
    ("It's ok. I just want to make you feel good.", 1),
    ])
    guy "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Take it out!", 1),
    ("Get it out of me.", 1),
    ("I told you take it out!", 1),
    ("I said take it out of me.", 1),
    ])
    pc "[dialouge]"

    if player.check_fight(2):
        $ player.face_angry()
        show sb_againstwall2 noman with hpunch
        $ dialouge = WeightedChoice([
        ("I push as hard as I can against the wall, managing to push him off me and he stumbles backwards on the floor. Realising his predicament, he quickly pulls his trouser up and flees.", 1),
        ("I struggle backwards and flail my elbows around hoping to hit him in the face. I must have done something because he stumbles back. I turn to face him but he is already running away while tripping over his trousers.", 1),
        ("I try to twist around so he can't keep his cock inside me and swing my elbows to where I think his face is. I feel an impact and by the time I am able to turn around, I already see his bare arse running away.", 1),
        ("I push off against the wall and swing my foot against his legs. My heel impacts something and I am able to then push him off me. By the time I can gather my wits, he has already done a runner.", 1),
        ])
        "[dialouge]"
        $ player.sex_end()
        hide sb_againstwall2 with dissolve
        pc "What the fuck! What a cunt!"
        jump school_rep_sex_forcesex_end
    else:

        $ player.face_angry()
        $ dialouge = WeightedChoice([
        ("I push as hard as I can against the wall to try and push him off me. But I am not strong enough and I feel his arm impact my back and press me against the wall.", 1),
        ("I struggle backwards and flail my elbows around hoping to hit him in the face. It doesn't seem like I managed to hit him because I am quickly pinned against the wall.", 1),
        ("I try to twist around so he can't keep his cock inside me and swing my elbows to where I think his face is. But he is quick to hammer his arm into my back and press against me so I can't push back anymore.", 1),
        ("I push off against the wall and swing my foot against his legs. My heel impacts something but then the air is quickly pushed from my lungs as he thumps me in the back and presses his weight against me to keep me pinned.", 1),
        ])
        "[dialouge]"
        $ player.face_cry()
        pc "Fuck!"
        guy "Mmmm. Take it easy and lets enjoy this."
        pc "Fuck you!"
        $ dialouge = WeightedChoice([
        ("He continues to pin me against the wall as he thrusts inside me. Fucking me with increased vigour knowing that I can't push him off of me.", 1),
        ("He keeps me pressed against the wall as I feel him thrust inside me. Paying no heed to me struggling, he just takes me as he pleases.", 1),
        ("I try to block out the pain in my back as he is pinning me against the wall. But it is hard to ignore him thrusting inside me, taking me as he pleases.", 1),
        ("My face is pressed against the wall with his elbow digging into my back. I can do nothing to stop him from taking me as he pleases.", 1),
        ])
        "[dialouge]"
        show sb_againstwall2 closed with dissolve
        if player.virgin_pregcheck:
            guy "Mmmmm, such a lovely young slut. And is that blood? Were you a virgin?"
            guy "Oh man having popped the cherry of some little teenage slut. I will have to tell everyone."
            pc "*SOB*"
        else:
            guy "Mmmmm, such a lovely young slut."
            pc "*SOB*"
        guy "Ahhhhhh!"
        $ player.sex_cum(schoolguy, "inside")
        guy "Ahhh yes!"
        pc "*SOB*"
        show sb_againstwall2 pokevag with dissolve
        show sb_againstwall2 noman with dissolve
        "Once he is finished inside me, he quickly pulls out, pulls his trousers up and leaves. Leaving me the room alone."
        jump school_rep_sex_forcesex_end

label school_rep_sex_forcesex_end:
    $ renpy.scene()
    with dissolve
    $ player.face_cry()
    pc "Bastard!"
    pc "*SOB*"
    pause 1
    $ pc_dress()
    pc "*SOB*"
    pc "I can't believe that just happened..."
    pc "..."
    jump random_event_school_end_picker

label school_rep_sex_vag_virgin:

    if not player.want_sexlocation == "":
        if player.desire >= 80:
            pcm "I am so fucking wet right now and I can feel him prodding at me down there."
        elif player.desire <= 20:
            pcm "Maybe I shouldn't have offered my pussy. I can feel him poking me but I am not really wet..."
        else:
            pcm "I can feel him poking me and has starting to make me all wet."
        guy "You dirty little girl."
        if player.soldprice > 0:
            pcm "Hope he makes me feel good. Even though I am selling myself to him, I still want to enjoy my first time..."
            pcm "Fuck... I am such a whore..."
        else:
            pcm "Hope he makes me feel good. I still want to enjoy my first time..."
        "I can feel his penis start to enter me. This is the first time I have ever felt such an intrusion, and while is it a bit uncomfortable, he isn't so deep yet so I still enjoy it."
        guy "Fuck, you are so tight."
        show sb_againstwall2 insidevag ag wink with dissolve


        $ player.sex_vag(schoolguy)
        "He pulls out a little and his next thrust is much more persistent. I feel my lips being stretched and a fullness I have never felt before as he enters me fully."
        "There is a fair amount of pain, but my mind is swimming with euphoria as I feel for the first time what it's like to have a sex. A virile man penetrating and having his way with me."
        $ player.face_excited()
        pc "Ahh ♥ Fuck yes!"
        pc "Haaaaa"
        guy "Ahhhhhh yes. Take it!"

    elif player.check_sex_agree(3):
        "I feel his penis rubbing my slit to get it ready for my arse when I can feel a stretching in my lips as his cockhead pokes inside me."
        pc "Ahh ♥ I told you to put it in my bum!"
        "He pulls out a little and starts rubbing deep in my slit."
        "But his next thrust is much more persistent. Instead of pulling out and aiming at my arse, he instead enters me fully and deeply."
        show sb_againstwall2 insidevag ag wink with dissolve


        $ player.sex_vag(schoolguy)
        "There is a fair amount of pain, but my mind is swimming with euphoria as I feel for the first time what it's like to have a sex. A virile man penetrating and having his way with me."
        $ player.face_excited()
        pc "Ahh ♥ That's not my bum!"
        pc "Haaaaa"
        guy "Ahhhhhh so warm and tight. I couldn't resist."
    else:

        jump school_rep_sex_forcesex


    pc "Ahhh ♥ You are so big!"
    pc "Haaaa ♥"
    "He relentlessly fucks me up against the wall. I can feel his hard cock pumping in and out as he roughly grips onto my ass cheeks to pull himself deeper into me."
    "Pounding into me, he gets faster and faster as I get more and more excited. His grip on my arse no doubt leaving red marks on my skin and his breathing getting more ragged with every thrust."
    guy "Ah yes this is so nice. You are gripping onto my cock!"
    pc "Haaaaa... ♥"
    "My mind starts to lose focus as I focus only on the cock thrusting in and out of me. I can feel the pleasure building up inside me."
    "This is the first time I have ever felt such a thing. Being brought to orgasm my a man's cock thrusting in and out of me. My mind is swimming with the feeling of pleasure and fullness I have never known before."
    pc "Yes, yes! ♥"
    $ player.face_orgasm()
    guy "Ahhh, I'm about to come!"
    jump school_rep_sex_vag_cum





label school_rep_sex_assault:
    $ dialouge = WeightedChoice([
    ("Take off your clothes.", 1),
    ("Undress. Now!", 1),
    ("Get your clothes off. Let me see that body of yours.", 1),
    ("Let me see what you have under those clothes. Take them off.", 1),

    ("Show me that pregnant body of yours. Take off your clothes.", If (player.pregnancy > 2, 1, 0)),
    ("I want to see what a pregnant bitch looks like naked. Take off your clothes.", If (player.pregnancy > 2, 1, 0)),

    ("Dirty slut. Show me that body of yours.", If (player.isslut, 1, 0)),
    ("Slut like you should be used to being naked. Now show me what you have.", If (player.isslut, 1, 0)),

    ("Take off your clothes you fat bitch.", If (player.isfat, 1, 0)),
    ("Come on fatty, take those clothes off now.", If (player.isfat, 1, 0)),
    ])
    guy "[dialouge]"
    $ player.face_worried()
    if player.isbroken:
        $ player.face_meek()
        pc "..."
        $ player.face_normal()
        pc "Ok..."
    else:
        pc "Wha...? But..."
        guy "DO IT!"
        pcm "Fuck fuck fuck!"
        if not player.check_nowill():
            pcm "I might be able to run away. But if he catches me it might make him more angry."
            menu:
                "Try to run away":
                    if player.check_fight(2):
                        $ walk(loc_school_hallway)
                        with hpunch
                        $ dialouge = WeightedChoice([
                        ("I raise my hands to my top to look like I am about to undress, then quickly make a break for it and don't look back", 1),
                        ("I spit in his face and quickly make a run for it. I keep going without looking back until I am somewhere much more public.", 1),
                        ("I pretend to get ready to undress before quickly doing a runner. I keep going until I am somewhere with other people around.", 1),
                        ])
                        "[dialouge]"
                        $ player.face_exercise()
                        pcm "*Phew*"
                        pcm "Fuck..."
                        $ player.face_cry()
                        pcm "*SOB*"
                        pcm "Thank fuck I got away..."
                        jump random_event_school_end_picker
                    else:

                        $ dialouge = WeightedChoice([
                        ("I raise my hands to my top to look like I am about to undress, then quickly make a break for it. But he was ready and trips my ankle as I try to run.", 1),
                        ("I spit in his face and quickly make a run for it. But he was prepared for me and pushes me as I run and I end up tumbling over and hitting the floor.", 1),
                        ("I pretend to get ready to undress before quickly doing a runner. He isn't fooled though and trips me as I try to run.", 1),
                        ])
                        "[dialouge]"
                        $ player.punch()
                        guy "Right! You asked for it!"
                        jump school_rep_sex_forced_attack
                "Submit":
                    $ NullAction()

        $ player.face_meek()
        pcm "Trying to fight back will just end up in making it worse..."
        $ player.face_worried()
        guy "Well...?"
        $ dialouge = WeightedChoice([
        ("He steps forward in a threatening manner and I take a step back to try to avoid him.", 1),
        ("He steps forward with a clenched fist raised and I put up hands up in a pleading manner to try to placate him.", 1),
        ("He steps menacingly towards me and I meekly take a step backwards.", 1),
        ])
        "[dialouge]"
        $ player.face_shock()
        pc "Okay okay..."
    $ player.face_meek()
    $ pc_striptease()
    $ acc_strip()
    $ randomnum = renpy.random.randint(1, 20)
    if randomnum < 3:
        jump school_rep_sex_forced_sex_vag
    elif randomnum < 3:
        jump school_rep_sex_forced_sex_anal
    elif randomnum > 10:
        jump school_rep_sex_forced_hand
    else:
        jump school_rep_sex_forced_blow

label school_rep_sex_forced_attack:

    $ player.punch()
    pc "Ahh!"
    $ player.punch()
    pause 0.2
    $ player.punch()
    pc "Stoooo..."
    jump school_rep_sex_ko

label school_rep_sex_forced_hand:
    $ dialouge = WeightedChoice([
    ("Get on your knees and let's see what those hands can do.", 1),
    ("Put your fingers round my cock, bitch.", 1),
    ("Get down and work those hands.", 1),
    ("You are gonna wank me off and I don't want to hear any complaining.", 1),
    ("On your knees you little bitch.", 1),
    ("Good whore. Now on your knees. You are going to wank me off for free.", If (player.iswhore, 1, 0)),
    ("Now whore, get on your knees and give me a free handjob.", If (player.iswhore, 1, 0)),
    ])
    guy "[dialouge]"
    pc "..."
    $ player.sex_hand(schoolguy)
    show sb_handjob down with dissolve

    $ dialouge = WeightedChoice([
    ("Bitch like you should get used to this. Your only use is to get a guy off.", 1),
    ("Good, right where you belong.", 1),
    ("Good, you know your place. Bitch like you is good for only one thing.", 1),
    ("That's better bitch!", 1),
    ("Good whore. Now show me why people pay for you to get them off.", If (player.iswhore, 1, 0)),
    ("Good little whore. Now show me how good a whore who fucks men off for a living is.", If (player.iswhore, 1, 0)),
    ])
    guy "[dialouge]"
    show sb_handjob up
    pc "..."
    pcm "Fuck, how did it come to this...?"
    show sb_handjob down
    $ dialouge = WeightedChoice([
    ("Ah fuck yes, you little slut.", 1),
    ("Ah fuck you little slut. You were born to take cocks in you.", 1),
    ("Bet you are loving this. All bitches want to be dominated and put on their knees by a man.", 1),
    ("Good bitch knows her place. Keep going and you might even make me happy.", 1),
    ("Ah good little bitch.", 1),
    ("Ah yes. Looks like you have enough practice. But you need to do better if you expect to make a living.", If (player.iswhore, 1, 0)),
    ("Is this the best a whore can do?", If (player.iswhore, 1, 0)),
    ])
    guy "[dialouge]"
    $ randomnum = renpy.random.randint(1, 5)
    if randomnum == 1:
        "I stay giving him a handjob and he cums."
        $ player.sex_cum(schoolguy, "hand")
        jump school_rep_sex_forcesex_end
    elif randomnum == 5:
        "He tells me he wants to fuck me."
        jump school_rep_sex_forced_sex_choice
    else:
        $ dialouge = WeightedChoice([
        ("Ah yes thats good. But let's see those lips sucking me off.", 1),
        ("Now I want to put my cock in your mouth.", 1),
        ("Now open your mouth you little bitch.", 1),
        ("Now you are gonna suck on my cock and I don't want to hear any complaining.", 1),
        ("Good whore. Now you are going to suck me off for free.", If (player.iswhore, 1, 0)),
        ])
        guy "[dialouge]"
        guy "Come here."
        jump school_rep_sex_forced_blow_jump

label school_rep_sex_forced_blow:
    $ dialouge = WeightedChoice([
    ("Get on your knees and let's see those lips sucking me off.", 1),
    ("On your knees bitch. I want to put my cock in your mouth.", 1),
    ("Get down and open your mouth.", 1),
    ("You are gonna suck on my cock and I don't want to hear any complaining.", 1),
    ("On your knees you little bitch.", 1),
    ("Good whore. Now on your knees. You are going to suck me off for free.", If (player.iswhore, 1, 0)),
    ("Now whore, get on your knees and give me a free blowjob.", If (player.iswhore, 1, 0)),
    ])
    guy "[dialouge]"
    pc "..."
    $ player.sex_oral(schoolguy)
    $ renpy.scene()
    show sb_blowjob angry eangry poke
    with dissolve
    $ dialouge = WeightedChoice([
    ("Bitch like you should get used to this. Plenty of guys are going to make use of you.", 1),
    ("Good, right where you belong.", 1),
    ("Good, you know your place. Bitch like you is good for only one thing.", 1),
    ("Cock in the mouth of a bitch like you is almost too good.", 1),
    ("That's better bitch!", 1),
    ("Good whore. Now show me why people pay for you to suck them off.", If (player.iswhore, 1, 0)),
    ("Good little whore. Now show me how good a whore who sucks men off for a living is.", If (player.iswhore, 1, 0)),
    ])
    guy "[dialouge]"
label school_rep_sex_forced_blow_jump:

    show sb_blowjob suck closed with hpunch

    pcm "..."
    pcm "Fucking arsehole..."
    $ dialouge = WeightedChoice([
    ("Ah fuck yes, you little cock sucking slut.", 1),
    ("Ah fuck you little slut. You were born to take cocks in you.", 1),
    ("Bet you are loving this. All bitches want to be dominated and put on their knees by a man.", 1),
    ("Good bitch knows her place. Keep sucking and you might even make me happy.", 1),
    ("Ah good little bitch.", 1),
    ("Ah yes. Looks like you have enough practice. But you need to do better if you expect to make a living.", If (player.iswhore, 1, 0)),
    ("Is this the best a whore can do?", If (player.iswhore, 1, 0)),
    ])
    guy "[dialouge]"

    $ dialouge = WeightedChoice([
    ("I should tie you down and invite the school to have you as free use. Bet someone like you would love that.", 1),
    ("Bet you are getting off on this you little cunt. Bitch like you knows no better than to please a cock.", 1),
    ("You belong on your knees.", 1),
    ("Ah you dirty little girl. Didn't even need to hit you. Bet you're happy to suck me off.", 1),
    ("Maybe next time I will come by the highway and get another freebie off you.", If (player.iswhore, 1, 0)),
    ("Keep going you dirty whore. Suck it and take what's inside.", If (player.iswhore, 1, 0)),
    ])
    guy "[dialouge]"

    $ dialouge = WeightedChoice([
    ("Mmmfff.", 1),
    ("Ah! *Ugg*", 1),
    ("Mmmff. *Hyuk* *Hyuk*", 1),
    ("*Slurp*", 1),
    ("*Hyuk* *Hyuk* *Hyuk*", 1),
    ])
    pc "[dialouge]"

    $ dialouge = WeightedChoice([
    ("Dirty little slut. Keep going!", 1),
    ("Ah fuck, keep going like that and I will cum in your filthy mouth.", 1),
    ("Yes, fuck! Keep going you fucking whore.", 1),
    ("*Huff* *Huff* *Huffff*", 1),
    ])
    guy "[dialouge]"
    $ dialouge = WeightedChoice([
    ("I start to feel his cock tensing up and his movements become erratic. He is being much more aggressive now and grabbing my hair while thrusting into my mouth. Seems he is not far off...", 1),
    ("His groaning lets me know he is not far off cumming so I pick up the pace and blow him even faster than I was before to get this ordeal over with.", 1),
    ("He is gripping onto my head and thrusting quite aggressively now. I know he won't last much longer at this rate so I work his shaft harder with my hands to try and push him over the edge.", 1),
    ])
    "[dialouge]"

    $ randomnum = renpy.random.randint(1, 5)
    if randomnum <= 3:
        $ dialouge = WeightedChoice([
        ("Ah stop. Stop. It's better if I finish while fucking you.", 1),
        ("Ah fuck. Haaa. This would be so much better if I have you bent over on my cock.", 1),
        ("Ah yes. Fuck I really should take one of your holes and finish in there.", 1),
        ])
        guy "[dialouge]"
        $ dialouge = WeightedChoice([
        ("Come here. Bend over so I can stick it in you like a good little bitch.", 1),
        ("Turn around so I don't need to look at your crying face while I stick it in you.", 1),
        ("Come here you little bitch. I'm gonna fuck you like a shitty tramp.", 1),
        ])
        guy "[dialouge]"
        pc "*SOB*"
        jump school_rep_sex_forced_sex_choice
label school_rep_sex_forced_blow_cum:
    show sb_blowjob angry closed
    $ player.sex_cum(schoolguy, "mouth")
    $ dialouge = WeightedChoice([
    ("I feel his start to throb and push his cock deep in my mouth. He starts to cum and I feel his vile load squirting from his cock and into my mouth.", 1),
    ("He starts throbbing in my mouth and I feel disgust as he cums into my mouth.", 1),
    ("His cock starts to swell until he tenses up and releases his vile load in my mouth and I have no choice but to swallow most of it down.", 1),
    ("He throbs in my mouth and I feel the first wave fill me. I quickly resist the urge to puke as I swallow it down before another pulse shoots more on my tongue.", 1),
    ])
    "[dialouge]"
    show sb_blowjob eangry with dissolve
    guy "Ahhhh! Yeeeeess..."
    guy "Haaaa..."
    pc "Ubbb..."
    $ dialouge = WeightedChoice([
    ("Ah good little slut. Keep that on your face as a present.", 1),
    ("That's how a bitch should treat their betters. Next time I will give you a good fucking.", 1),
    ("Good. Swallow it down like the little cum whore you are.", 1),
    ])
    guy "[dialouge]"
    show sb_blowjob poke ub with dissolve
    show sb_blowjob noman with dissolve
    $ dialouge = WeightedChoice([
    ("I watch as he pulls his trousers up and without giving me a second look he heads off, leaving me naked and alone.", 1),
    ("I sit there naked, holding back tears as he dresses and heads off without another word.", 1),
    ])
    "[dialouge]"
    $ player.face_puke()
    show sb_blowjob swallow down with dissolve
    pc "Bleh..."
    show sb_blowjob frown with dissolve
    pc "..."
    jump school_rep_sex_forcesex_end

label school_rep_sex_forced_sex_choice:
    $ renpy.scene()
    show sb_againstwall2 cum wink frown worried with dissolve
    $ randomnum = renpy.random.randint(1, 5)
    if randomnum == 1:
        jump school_rep_sex_forced_sex_anal
    else:
        jump school_rep_sex_forced_sex_vag

label school_rep_sex_forced_sex_vag:
    show sb_againstwall2 pokevaghand wink frown worried with dissolve
    $ dialouge = WeightedChoice([
    ("I feel his cock sliding between my lips as he wanks himself off a bit.", 1),
    ("I can feel him stroking his cock as the tip of his penis slides between my wet folds.", 1),
    ])
    "[dialouge]"
    show sb_againstwall2 pokevag with dissolve
    if player.vvirgin:
        pcm "Fuck, he is poking me there. I don't want to lose my virginity to this dirty shit."
    elif player.cycle_conditions["stage"] == "ovulate":
        pcm "Fuck, right now is a dangerous time of the month. Doubt this shit will bother to pull out..."
    elif not player.pregpills or not player.cycle_conditions["stage"] == "mens" or not player.preg_knows:
        pcm "Fuck, without protection this can be a bit dangerous. I don't want to end up pregnant here..."
    if (not player.pregpills or not player.cycle_conditions["stage"] == "mens") or player.vvirgin or player.cycle_conditions["stage"] == "ovulate":
        menu:
            "Beg him not to put it inside":
                if player.vvirgin:
                    pc "No please don't. I don't want my first time to be with you. Please don't put it in me..."
                elif player.cycle_conditions["stage"] == "ovulate":
                    pc "Please, now is a bad time of the month. Please don't put it inside me."
                elif not player.pregpills or not player.cycle_conditions["stage"] == "mens":
                    pc "Please don't. I am not on any protection and I don't want to be getting pregnant by you..."
                if player.check_speech(4):
                    guy "*Tsk*"
                    guy "Whatever. One hole is as good as another."
                    jump school_rep_sex_forced_sex_anal
            "Keep silent":
                pcm "I am not going to beg at this shit's feet..."
label school_rep_sex_forced_sex_vag_jump:
    $ dialouge = WeightedChoice([
    ("His cock starts to push deeper and I feel him slowly start to stretch my pussy and fill me up inside.", 1),
    ("I feel him start to enter deeper and deeper with each poke until he is deep enough inside me that it's no longer poking but actual fucking.", 1),
    ("He gently starts to press his cock against me and in a very slow thrust, stretches my lips and starts to enter me fully.", 1),
    ])
    "[dialouge]"
    $ player.sex_vag(schoolguy)
    show sb_againstwall2 insidevag pain angry closed with hpunch
    $ dialouge = WeightedChoice([
    ("Ah! Fucking cunt!", 1),
    ("Ah this fucking arsehole!", 1),
    ("Ah fuck this shitty cunt.", 1),
    ])
    pcm "[dialouge]"
    $ dialouge = WeightedChoice([
    ("I feel him start to take long and deep thrusts inside me. Pushing his cock balls deep into me before pulling almost all the way out, then ramming it back in again. ", 1),
    ("He takes it slow and rhythmically thrusts making sure I feel his disgusting cock in me. He paws at my tits as he does so and I just accept what is happening.", 1),
    ("He thrusts deeply into me before slowly sliding his cock out almost all the way. Then aggressively slams back into me in a quick and hard thrust.", 1),
    ])
    "[dialouge]"
    $ player.spank()
    $ dialouge = WeightedChoice([
    ("He starts to get into it more and spanks me or reaches round to claw at my tits as he is thrusting deep inside me.", 1),
    ("He starts to build momentum and it's not long before I hear his body slapping against my ass with each thrust into me.", 1),
    ("He builds up speed as I try not to cry and it's not long until he is harshly gripping my sides and pulling me against his thrusting cock.", 1),
    ("He cares nothing for my wellbeing and just rams away as he pleases. Fucking me hard and fast while smacking me on the arse.", If (player.desire > 80, 1, 0)),
    ])
    "[dialouge]"
    $ player.spank()
    $ dialouge = WeightedChoice([
    ("Ah fuck this is so nice. You are such a dirty girl!", 1),
    ("Ah yes this is so nice. You are gripping onto my cock!", 1),
    ("Ah fuck you are so warm. So nice having my cock in you.", 1),
    ("Ah fuck so nice. You know perfectly how to make a man feel good.", If (player.vsex > 10, 1, 0)),
    ])
    guy "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Cunt!", 1),
    ("Fucking cunt!", 1),
    ("Disgusting shit!", 1),
    ("Should have tried to bite his cock off...",1),
    ])
    pcm "[dialouge]"
    $ dialouge = WeightedChoice([
    ("His breathing starts to become ragged and it seems like it will be over soon.", 1),
    ("His thrusting and pawing at my body has become more aggressive and it sounds like he might be reaching his limit.", 1),
    ("He is thrusting faster now and squeezing at my arse. It seems like he won't last much longer.", 1),
    ])
    "[dialouge]"
    $ player.face_cry()
    $ dialouge = WeightedChoice([
    ("Yes, yes!", 1),
    ("Ahhhhh fuck yes.", 1),
    ("Yes! Yes! Yes!", 1),
    ("Ahhh I am close.", 1),
    ("Ahhhhh yes you dirty bitch.", 1),
    ])
    guy "[dialouge]"

    if (not player.pregpills or not player.cycle_conditions["stage"] == "mens") or player.vvirgin or player.cycle_conditions["stage"] == "ovulate":
        menu:
            "Beg him not to cum inside.":
                show sb_againstwall2 wink shock with dissolve
                pc "Please no. Not inside. Pull out, pull out! Please!"
                if player.check_speech(4):
                    jump school_rep_sex_forced_sex_vag_pullout
                else:

                    $ player.punch()
                    show sb_againstwall2 closed pain with dissolve
                    guy "Shut up bitch. Stop ruining it for me!"
            "Keep silent.":

                $ NullAction()

    $ dialouge = WeightedChoice([
    ("Ah you dirty bitch. Take it inside.", 1),
    ("Ah fuck I'm gonna put it inside you.", 1),
    ("Ah yes. Take it you cunt.", 1),
    ("Ah I am cumming!", 1),
    ("Nng fuck I am cumming.", 1),
    ("Yes, yes!", 1),
    ("Ah yes you shitty bitch! I am going to fill you up.", 1),
    ("Ah get ready for carrying my baby, bitch!", 1),
    ("Haaa fuck I am going to knock you up like a dirty slut you are!", 1),
    ("Get ready for my baby you bitch.", 1),
    ("Ahhh yes take it deep inside. Hope you're feeling lucky.", 1),
    ("Better hope you are lucky cos I am going to fill you up!", 1),
    ("You dirty slut. Take me inside you.", 1),
    ("Ah fuck yes you filthy slut.", 1),
    ])
    guy "[dialouge]"

    $ dialouge = WeightedChoice([
    ("He thrusts deep inside me and keeps his cock buried inside me, making sure he puts everything deep in me.", 1),
    ("I can feel him gripping my hips and pulling me balls deep on his throbbing cock. Unloading everything inside me.", 1),
    ("His cock pulses inside me, unloading his cum deep inside me.", 1),
    ])
    "[dialouge]"

    $ player.sex_cum(schoolguy, "inside")
    $ dialouge = WeightedChoice([
    ("No plea...", 1),
    ("Fuck...", 1),
    ("Stop...", 1),
    ("*SOB* *SOB*", 1),
    ("Shit!", 1),
    ])
    pc "[dialouge]"
    show sb_againstwall2 pokevag with dissolve
    show sb_againstwall2 noman wink with dissolve
    guy "Thanks you little whore."
    $ player.spank()
    $ player.face_cry()
    pc "*SOB*"
    $ dialouge = WeightedChoice([
    ("I stand there with his cum dripping out of me and watch as he leaves.", 1),
    ("I try to hold back tears as I watch the cunt leave with his cum still inside me dripping out.", 1),
    ("I try not to curse at him as he is leaving in case he comes and hits me. But internally I am screaming at him.", 1),
    ])
    "[dialouge]"
    jump school_rep_sex_forcesex_end

label school_rep_sex_forced_sex_anal:
    show sb_againstwall2 pokeasshand with dissolve
    $ dialouge = WeightedChoice([
    ("He pokes at my ass and without much lube, tries to push it inside but is unable to.", 1),
    ("I feel him press against my asshole and try to put it inside me, but without any lube it has no chance of getting in.", 1),
    ("I feel him put the tip of his cock against my ass and press against it. But my asshole is dry and he has no chance of getting inside.", 1),
    ])
    "[dialouge]"
    show sb_againstwall2 pokevaghand with dissolve
    $ dialouge = WeightedChoice([
    ("He then decides to rub against my pussy. Unfortunately it is not very wet so I am probably in for a painful time.", 1),
    ("He decides to try and lube his cock up by rubbing it between my legs. But since I am not wet he doesn't manage to lube up much.", 1),
    ])
    "[dialouge]"
    $ randomnum = renpy.random.randint(1, 15)
    if randomnum == 1:
        guy "Ah fuck it..."
        jump school_rep_sex_forced_sex_vag_jump
    show sb_againstwall2 pokeasshand shock worried with dissolve
    $ dialouge = WeightedChoice([
    ("I then feel him poke at my asshole again. At least his cock feels somewhat slicker than before and may not be as harsh when he enters me..", 1),
    ("His cock then presses against my arse again. Hopefully he managed to lube up a bit...", 1),
    ])
    "[dialouge]"
    show sb_againstwall2 pokeass with dissolve
    $ dialouge = WeightedChoice([
    ("He applies pressure with his cock against me and slowly starts to enter. But it is still too dry to get fully in.", 1),
    ("He starts to try and push it in, but without enough lube he is having a hard time.", 1),
    ])
    "[dialouge]"
    "Until eventually..."
    $ player.sex_anal(schoolguy)
    show sb_againstwall2 insideass pain closed angry with hpunch
    $ player.face_cry()
    $ dialouge = WeightedChoice([
    ("Ah fuck it hurts!", 1),
    ("Ahhh! Shit!!", 1),
    ("Ahhh! Fuck that hurts!", 1),
    ])
    pc "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Shut up bitch!", 1),
    ("Shut the fuck up!", 1),
    ("Be quiet!", 1),
    ])
    guy "[dialouge]"
    $ randomnum = renpy.random.randint(1, 10)
    if randomnum == 1:
        $ player.punch()
    $ dialouge = WeightedChoice([
    ("The pain is overwhelming and I don't even try to stifle my sobs. I just close my eyes and hope it will be over as quick as possible.", 1),
    ("The pain is excruciating and I just cry as he fucks me. All I can do is hope it will be over soon.", 1),
    ("The pain of him entering me is unbearable and all I can do is cry and hope it will end soon.", 1),
    ])
    "[dialouge]"

    $ dialouge = WeightedChoice([
    ("His grip on me starts to get stronger and more painful as he gets more and more excited. His breathing is now getting more ragged with each thrust.", 1),
    ("His grip on my cheeks is now hard enough to leave marks on my skin as his thrusts start to become erratic. He is clearly enjoying this and may not last much longer.", 1),
    ("His hands are all over my body as he starts to put himself over the edge. His breathing becoming heavy and he starts to thrust much more aggressively into me.", 1),
    ("He grips me by the hips and thrusts into me again and again, my ass clapping against his body each time.", 1),
    ])
    "[dialouge]"

    $ dialouge = WeightedChoice([
    ("He must be close. At least I hope he is.", 1),
    ("The way he is grunting it sounds like it might be over soon.", 1),
    ])
    "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Ahhh, I'm about to come!", 1),
    ("Ah fuck I am close...", 1),
    ("Fuck so good. I am not going to last much longer.", 1),
    ("Ah yes! I am cumming!", 1),
    ])
    guy "[dialouge]"
label school_rep_sex_forced_sex_anal_jump:
    pc "*SOB*"
    $ player.sex_cum(schoolguy,"anal")
    guy "Ahhhh fuck yes."
    $ player.spank()
    guy "Haaaaaa..."
    pc "*SOB*"
    guy "Ah fuck yes. Nice little bitch."
    show sb_againstwall2 pokeass with dissolve
    show sb_againstwall2 noman with dissolve
    $ dialouge = WeightedChoice([
    ("I sit on the floor and cry as he cleans himself up and leaves without another word.", 1),
    ("I break down and cry and the guy pays me no heed as he dresses and heads off.", 1),
    ("I sit down and sob as he dresses and leaves without saying anything more.", 1),
    ])
    "[dialouge]"
    jump school_rep_sex_forcesex_end

label school_rep_sex_forced_sex_vag_pullout:
    $ randomnum = renpy.random.randint(1, 2)
    if randomnum == 1:
        $ dialouge = WeightedChoice([
        ("Come here then you little bitch. Open your mouth.", 1),
        ("On your knees then you little whore. I will come in at least one of your holes.", 1),
        ("Come here then you fucking whore.", 1),
        ])
        guy "[dialouge]"
        $ renpy.scene()
        $ player.sex_oral(schoolguy)
        show sb_blowjob closed angry
        with hpunch
        $ dialouge = WeightedChoice([
        ("Mmmfff.", 1),
        ("Ah! *Ugg*", 1),
        ("Mmmff. *Hyuk* *Hyuk*", 1),
        ("*Hyuk* *Hyuk* *Hyuk*", 1),
        ])
        pc "[dialouge]"
        jump school_rep_sex_forced_blow_cum
    else:
        guy "*Tsk*"
        show sb_againstwall2 pokevaghand with dissolve
        show sb_againstwall2 pokeasshand with dissolve
        show sb_againstwall2 pokeass with dissolve
        $ player.sex_anal(schoolguy)
        show sb_againstwall2 insideass pain angry closed with hpunch

        $ dialouge = WeightedChoice([
        ("Ah fuck it hurts!", 1),
        ("Ahhh! Shit!!", 1),
        ("Ahhh! Fuck that hurts!", 1),
        ])
        pc "[dialouge]"
        jump school_rep_sex_forced_sex_anal_jump

label school_rep_sex_ko:
    show screen blackout() with Dissolve(0.2)
    pause 3
    $ temp_var_1 = player.vvirgin
    $ player.sex_forced(schoolguy)
    $ player.sex_vag(schoolguy)
    $ player.sex_hideaction()

    $ pc_strip()
    show sb_assup worried closed frown sex
    $ player.eye = 3
    show screen blackout(25) with dissolve
    pc "Uuuugggggg..."
    show sb_assup squint grit with dissolve
    pc "Whhhhhhhaaaaaa..."
    guy "Ahhhh..."
    $ player.sex_cum(schoolguy, "inside")
    $ player.eye = 3
    guy "Ahhhaaaahhh........"
    show sb_assup closed with dissolve
    $ player.eye = 3
    pc "Oooowhaaaaaa..."
    show screen blackout() with dissolve
    $ time_sleep_rough()
    hide sb_assup
    pause 3
    hide screen blackout with dissolve
    pc "Ahhhhh..."
    pc "Fuck fuck!"
    pc "Did...?"
    $ player.eye = 3
    pc "Ah fuck..."
    $ player.face_cry()

    if temp_var_1 == True:
        pc "Did I really lose my virginity to some shit like that?"

    "I spot my clothes laying in a pile on the floor so I head over to pick them up."
    pc "*SOB* *SOB*"
    $ pc_dress()
    pc "..."
    pc "*SOB* *SOB*"
    pc "I can't believe that just happened..."
    pc "..."
    jump random_event_school_end_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
