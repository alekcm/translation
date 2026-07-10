label pub_waitress_work_lap:
    $ player.face_normal()
    $ dialouge = renpy.random.choice([
    "Wait, have a seat and drink some with me.",
    "Hold on, why not have a seat and join me for a drink",
    "Why not have a seat and help me finish my drink?"
    ])
    patron "[dialouge]"
    if pub_waitress.timesworked <= 3:
        $ dialouge = renpy.random.choice([
        "Sorry, I'm new here and don't want to get caught slacking off.",
        "Sorry, I only started working here recently and don't want to get caught skiving from work.",
        "I'm new here so don't want to get caught lazing about, sorry.",
        ])
        pc "[dialouge]"
        patron "No worries darling, another time then."
        jump pub_waitress_work_cycleend
    elif player.confidence <= 20:
        $ dialouge = renpy.random.choice([
        "Eeh, sorry. I think I had better get back to work.",
        "Err, what? Err, I think I have work to do...",
        "Eh? Ah... Sorry, I have to work.",
        ])
        pc "[dialouge]"
        "I rush off before he is able to respond."
        jump pub_waitress_work_cycleend
    else:
        $ randomnum = renpy.random.randint(30, 100)
        if player.drunk > randomnum:
            $ dialouge = renpy.random.choice([
            "Sure, I'll drink up your beer for you.",
            "Don't complain when your glass is empty.",
            "Don't be upset when I have drunk up all your beer.",
            "Say goodbye to your beer.",
            ])
            pc "[dialouge]"
            hide pub_serve_talking
            if pub_waitress.missionvar1 == True:
                show pub_serve_lap talk penis with dissolve
            else:
                show pub_serve_lap talk
            with dissolve
        else:
            $ dialouge = renpy.random.choice([
            "Sit where?",
            "There is nowhere to sit.",
            "All the seats are taken."
            ])
            pc "[dialouge]"
            "He reaches out and gently pulls me closer and guides me onto his lap."
            hide pub_serve_talking with dissolve
            if pub_waitress.missionvar1:
                show pub_serve_lap talk penis with dissolve
            else:
                show pub_serve_lap talk with dissolve
            pc "Err, ok..."


        if pub_waitress.missionvar1 == True:
            pc "You have me sitting here while still waving that thing around?"
            patron "I'm sure a girl like you doesn't mind."
            pc "..."
        $ dialouge = renpy.random.choice([
        "Here you go, drink up.",
        "Here you are, help yourself."
        ])
        patron "[dialouge]"
        $ player.right_hand = "beer"
        $ pub_tips()

label pub_waitress_work_lap_choices:
    if not pub_waitress.missionvar1:
        $ rand_choice = WeightedChoice([
        ("pub_waitress_work_lap1", If (player.mood < 30, 15, 0)),
        ("pub_waitress_work_lap2", 10),
        ("pub_waitress_work_lap3", If (player.desire + player.drunk > 100, 15, 0)),

        ])
        jump expression rand_choice
    else:
        $ rand_choice = WeightedChoice([
        ("pub_waitress_work_lap4", 10),
        ])
        jump expression rand_choice


label pub_waitress_work_lap1:
    pc "Don't mind if I do. Uff the day I have been having I could do with a drink."
    patron "What's been going on?"
    pc "Ah the usual you know. Hard to keep a smile on your face these days with how things are. It all creeps up on you and wears you down."
    patron "I can drink to that..."
    pc "Hear, hear."
    "I drink up most of the beer that was in my hand"
    $ player.beer(spiked=True)
    pc "But to make matters worse, I still have to get back to the grind to earn money. So I'll head off back to work with my misery."
    patron "Chin up."
    hide pub_serve_lap with dissolve
    jump pub_waitress_work_cycle3

label pub_waitress_work_lap2:
    pc "So what you doing in here?"
    patron "Drowning in my misery after work and enjoying the sights. What else is there to do?"
    pc "Those sights wearing red dresses?"
    patron "Of course. Nothing else worth looking at. Especially not the other miserable faces here drowning in their own misery."
    pc "Then let me drown with you."
    "I drink up most of the beer that was in my hand"
    $ player.beer(spiked=True)
    patron "I can't imagine better company to drink with."
    pc "Well, I'm going to have to leave you without company. Other people also need their beers. Enjoy your evening."
    hide pub_serve_lap with dissolve
    jump pub_waitress_work_cycle3

label pub_waitress_work_lap3:
    pc "So what you up to sitting alone in here?"
    patron "Watching the short skirts while enjoying a beer, same as everyone else I imagine."
    pc "Well, pretty much."
    patron "You don't mind?"
    pc "What's to mind? People have to take what little enjoyment they can."
    patron "Even if that means looking up your skirt?"
    pc "Pfft. I've had a lot worse. Perverts looking at my pants are the least of my worries these days."
    if pub_waitress.pants == 0:
        patron "Didn't see any pants when looking up your skirt."
        $ player.face_shy()
        pc "Well, what can I say. Not every one is content with just looking."
        patron "Can't blame them with a tiny cutie like you around flashing your arse."
        $ player.face_normal()
    pc "Also brings in more tips. And making rent money is one of my worries."
    "I drink up most of the beer that he gave me."
    $ player.beer(spiked=True)
    pc "And speaking of, I don't get paid for sitting on your lap all evening, so I had better get to it."
    if numgen(0,6) >= 2:
        patron "And what if I paid you to keep sitting on my lap."
        pc "I would ask how much."
        $ player.set_whore_price(0)
        patron "Let's see..."
        patron "£ [player.soldprice]"
        pc "That much doesn't sound like you just want my company."
        patron "No, let's call it an extra service."
        if not pub_waitress.pants:
            patron "Probably the same service you gave to whoever made off with your pants."

        if player.check_whore():
            if player.sold > 0 and player.iswhore == False:
                pcm "I have done it before, should I again?"
            else:
                pcm "Should I do it? No doubt this will end in sex..."
            if player.check_whore_agree_choice():

                "I don't answer and just start groping at his crotch instead."
                show pub_serve_lap mast penis with dissolve
                pc "Bit of a monster you have hiding here. I'm sure most girls would service it for free."
                patron "You want to do it here in front of everyone???"

                if c.pants:
                    hide pub_serve_lap with dissolve
                    jump whore_street_customer_pick_location_tombola
                else:

                    if player.check_sex_agree(3, exhibitionist=True):
                        pc "Not doing anything yet till you hand over the money."
                        patron "Err, here..."
                        $ player.add_money(player.soldprice)
                        pc "Mmmm. Thank you ♥"
                        show pub_serve_lap hump rub with dissolve
                        if player.has_perk(perk_exhibitionist):
                            pc "Here is good. Let people see you fucking me."
                        else:
                            pc "Here is fine, just don't make too much noise."
                        patron "Damn, didn't realise how much of a dirty girl you are."
                        if player.has_perk(perk_exhibitionist):
                            pcm "Fucked in front of everyone is so fucking hot!"
                        else:
                            pcm "In public like this I can control everything, but better not tell him that."
                        with grope_trans
                        pc "Seems your friend is already standing to attention. ♥"
                        patron "With you on my lap, of course he is."
                        show pub_serve_lap prep with dissolve
                        pc "Now let's see..."
                        "I sit up a bit and guide his cock between my lips then slowly slide down it feeling every vein as it enters me."

                        $ player.sex_vag(pubpatron, pub_waitress)
                        show pub_serve_lap hump with dissolve
                        pc "Ahh fuck yes!"
                        patron "Shhhh."
                        pc "Huff huff."
                        if player.has_perk(perk_exhibitionist):
                            pcm "I make little attempt to be discreet about what we are doing. Rhythmically fucking the hard cock that just entered my wet pussy."
                        else:
                            "I gently ride backward and forwards trying not to draw too much attention to what we are doing. Rhythmically fucking the hard cock that just entered my wet pussy."
                        patron "Ah yes you dirty little slut."
                        pc "Huff huff."

                        if player.check_pullout():
                            patron "Haaaaa..."
                            patron "I can feel it..."
                            menu:
                                "Keep going" if not player.has_perk(perk_preg_notwant):
                                    patron "Ahhhhh..."
                                    $ player.face_orgasm()
                                    $ player.sex_cum(pubpatron, "inside", pub_waitress)
                                    "I feel his cock throbbing inside me filling my wet pussy with his sperm. Pulse after pulse I know he is pumping me full of his life making seed."
                                    pc "Ahhhh ♥"
                                    $ player.face_normal()
                                    pc "Mmmm, you filled me up..."
                                    patron "Haaaa. It was so nice and warm in there. I wanted it to last as long as possible."
                                    hide pub_serve_lap with dissolve


                                "Outside, outside" if not player.has_perk(perk_preg_want):
                                    if player.check_pullout_agree():
                                        show pub_serve_lap prep with dissolve
                                        show pub_serve_lap hump rub with dissolve
                                        $ player.face_orgasm()
                                        $ player.sex_cum(pubpatron, "pullout", pub_waitress)
                                        "I feel his cock throbbing and squirting his warm cum on my stomach and pubis. Pulse after pulse lets me feel his warmth against my skin."
                                        pc "Ahhhh ♥"
                                        pc "Mmmm, you covered me in your sperm..."
                                        $ player.face_normal()
                                        patron "Haaaa. It was so nice and warm in there. Next time I will fill you up."
                                        pc "Mmm will you now?"
                                    else:
                                        patron "Ahhhhh..."
                                        $ player.face_orgasm()
                                        $ player.sex_cum(pubpatron, "inside", pub_waitress)
                                        "I feel his cock throbbing inside me filling my wet pussy with his sperm. Pulse after pulse I know he is pumping me full of his life making seed."
                                        pc "Ahhhh ♥"
                                        $ player.face_normal()
                                        pc "Mmmm, you filled me up... I told you outside."
                                        patron "Haaaa. It was so nice and warm in there. I wanted it to last as long as possible."
                                        pc "So what? This could be dangerous for me... Idiot."
                                        pc "Ugh... Well..."
                                        hide pub_serve_lap with dissolve
                        else:


                            patron "Haaaaa..."
                            $ player.face_orgasm()
                            patron "Ahhhhh..."
                            $ player.sex_cum(pubpatron, "inside", pub_waitress)
                            "Without any warning I feel his cock throbbing inside me filling my wet pussy with his sperm. Pulse after pulse I know he is pumping me full of his life making seed."
                            pc "Ahhhh ♥"
                            $ player.face_normal()
                            pc "You didn't warn me..."
                            patron "Haaaa. It was so nice and warm in there. I wanted it to last as long as possible."

                        pc "Hope that service was what you were after. I am going to head back to work now."
                        hide pub_serve_lap with dissolve
                        jump pub_waitress_work_cycleend
                    else:

                        jump whore_street_customer_pick_location_tombola
            else:
                jump pub_waitress_work_lap3_refuse
        else:

            jump pub_waitress_work_lap3_refuse
    else:
        patron "Ok, thanks for the company."
        hide pub_serve_lap with dissolve
        jump pub_waitress_work_cycle3

label pub_waitress_work_lap3_refuse:
    $ player.soldprice = 0
    pc "Sorry mate, but I don't really feel comfortable providing that kind of service. But enjoy the rest of your evening."
    patron "Ok, thanks for the company."
    hide pub_serve_lap with dissolve
    jump pub_waitress_work_cycle3


label pub_waitress_work_lap4:
    $ pub_tips()
    $ pub_tips()
    pc "Ugh, Ok..."
    show pub_serve_lap talk penis with dissolve
    pc "So you gonna keep that thing flapping in the wind?"
    $ player.beer(spiked=True)
    patron "If you have a problem with it, you deal with it."
    pc "Mmmm, can I now?"

    if player.check_sex_agree(1):
        menu:
            "Leave him" if not player.has_perk([perk_meek, perk_broken], notif=True):
                jump pub_waitress_work_lap4_leave
            "Put him back in his pants":
                jump pub_waitress_work_lap4_putback
            "Play with it" if player.check_sex_agree(3, notif=False):
                jump pub_waitress_work_lap4_mast
            "Hump him" if player.check_sex_agree(5, notif=False):
                jump pub_waitress_work_lap4_hump
    else:
        jump pub_waitress_work_lap4_leave

label pub_waitress_work_lap4_hump:
    show pub_serve_lap mast with dissolve
    pc "Doubt this is going to fit back in your pants."
    patron "No, but it will fit somewhere else."
    pc "Is that so? Seems too big for there as well."
    patron "Then lets try."
    pc "Hmmmm."
    show pub_serve_lap prep with dissolve
    show pub_serve_lap hump rub with dissolve
    "I press myself against him and feel his cock rub against me as I slide forward."
    patron "I knew you were a dirty girl the moment I saw you."
    pc "Did you now?"
    if not c.pants:
        patron "Only a dirty slut walks around a pub with a bunch of perverts without wearing pants."
        patron "You were just inviting people to fuck you."
        pc "My pants keep going missing. Seems they have a mind of their own."
        patron "I'm sure they do. I bet you don't put up much of a struggle when they are taken."
        pc "Well, why should I?"
    else:
        patron "Sexy little thing like you strutting around with that tiny skirt, showing your arse off to all the perverts in this place."
        pc "Not my fault, it's the uniform I have to wear."
        patron "And swinging your hips or squeezing your tits together?"
        pc "Well. That's just normal to get tips from you perverts."

    patron "Heh, I knew it."
    pc "Wasn't this supposed to be going somewhere it can't be seen. It's a bit impolite to have it out in the open."
    if c.pants:
        patron "Seems something is in the way."
        if player.check_sex_agree_choice(diff=2,option1="Let's go somewhere to remove them" ,option2="..."):
            hide pub_serve_lap with dissolve
            jump whore_street_customer_pick_location_tombola
        else:
            jump pub_waitress_work_table_hump
    else:

        show pub_serve_lap prep with dissolve
        patron "Sit up a bit, yeah like that... Now slide down..."
        if player.vvirgin:
            pc "Whaaa... No no. I am a virg..."
        $ player.sex_vag(pubpatron, pub_waitress)
        show pub_serve_lap hump with dissolve
        patron "Haaaaaa."
        if player.virgin_pregcheck:
            patron "Was a virgin."
        pc "Ahh fuck!"
        patron "Shhhh."
        pc "Huff huff."
        "I gently ride backward and forwards trying not to draw too much attention to what I am doing. Rhythmically fucking the hard cock that just entered my wet pussy."
        patron "Ah yes you dirty little slut."
        pc "Huff huff."
        patron "Haaaaa..."
        patron "I can feel it..."

        call pub_waitress_work_cumevent from _call_pub_waitress_work_cumevent
        show pub_serve_lap prep with dissolve
        show pub_serve_lap talk penis with dissolve
        show pub_serve_lap talk mast with dissolve
        show pub_serve_lap talk no_penis hold with dissolve

        pc "Well there we go, now it fits in your pants again so I am going back to work. Enjoy your evening."
        hide pub_serve_lap with dissolve
        jump pub_waitress_work_cycleend

label pub_waitress_work_lap4_mast:
    $ player.sex_hand(pubpatron, pub_waitress)
    pc "You pervert, this is going back in your pants for sure."
    show pub_serve_lap mast with dissolve
    "I start pumping on his massive, hard cock. Not even trying to pretend I am trying to put it back in his pants."
    pc "I can feel it throbbing in my hand."
    patron "Keep trying to put it in there. You are doing good."
    pc "Oh thank you for the compliment..."
    patron "Heh, always."
    "I carry on masturbating his cock while his hands are all over my body."
    pcm "I wonder if I should sit on it..."
    pcm "Huh?"
    patron "Haaaaa ahhhh"
    $ player.sex_cum(pubpatron, "hand", pub_waitress)
    "His cock starts to throb even harder as he comes in my hand. Covering my fingers with his sticky sperm and dripping down the shaft of his cock."
    pc "Hmm, didn't expect that to happen while I was trying to put it back in your pants. ♥"
    "I feel his cock getting softer while it's in my hand, so I playfully put it back in his trousers, cum and all."
    show pub_serve_lap no_penis hold with dissolve
    pc "There we go, I managed to get it back in your trousers. ♥"
    pc "Enjoy your evening."
    hide pub_serve_lap with dissolve
    $ walk(loc_pub_toilet_girls)
    pcm "Better wash my hands."
    jump pub_waitress_work_cycleend

label pub_waitress_work_lap4_putback:
    pc "You pervert, this is going back in your pants for sure."
    show pub_serve_lap mast with dissolve
    "I start to put it back in his pants being a lot more handy than is necessary. The pervert just sits back enjoying having my hand on his cock."
    pc "Almost..."
    pc "Not as easy as it looks. ♥"
    show pub_serve_lap no_penis hold with dissolve
    pc "There we go you dirty pervert."
    patron "Thank you for your hands on service. I knew I came here for a reason."
    pc "Sure you did. Enjoy your evening"
    hide pub_serve_lap with dissolve
    jump pub_waitress_work_cycleend

label pub_waitress_work_lap4_leave:
    pc "Heh, enjoy your evening."
    hide pub_serve_lap with dissolve
    jump pub_waitress_work_cycle3
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
