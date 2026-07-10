label pub_waitress_work_talk:


    $ rand_choice = WeightedChoice([
    ("pub_waitress_work_talk10", If (player.iswhore and not player.has_perk(perk_freeuse), 2,0)),
    ("pub_waitress_work_talk11", If ((player.check_sex_agree(5, notif=False) and player.has_perk(perk_preg_want)) and not player.preg_knows, 1,0)),
    ("", 100)
    ])
    if not rand_choice == "":
        jump expression rand_choice

    $ player.face_normal()
    $ dialouge = renpy.random.choice([
    "Why don't you stay for a chat sweetie?",
    "Why not keep me company for a bit darlin'?",
    "Stay and chat with me for a bit before you head back why don't you?",
    "Stay for a bit before you leave darling."
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
    else:




















        if pub_waitress.timesworked <= 10:
            $ dialouge = renpy.random.choice([
            "I wonder if I will get a nice tip out of him if I chat with him for a bit?",
            "Keeping him company for a bit might get me a nice tip.",
            "Could help with tips if I chat a bit with him.",
            "Might manage some nice tips if I pretend to care what he has to say.",
            ])
            pcm "[dialouge]"
        $ dialouge = renpy.random.choice([
        "Sure thing.",
        "Might as well.",
        "Yeah why not?",
        "Ok.",
        ])
        pc "[dialouge]"
        $ pub_tips()
        $ renpy.scene()
        show pub_serve_talking
        with dissolve
        $ player.hands_reset()
        jump expression WeightedChoice([
        ("pub_waitress_work_talk1", 10),
        ("pub_waitress_work_talk2", 10),
        ("pub_waitress_work_talk3", 10),
        ("pub_waitress_work_talk4", If (c.socks > 0, 10, 0)),
        ("pub_waitress_work_talk5", If (c.pants > 0, 10, 3)),
        ("pub_waitress_work_talk6", 10),
        ("pub_waitress_work_talk7", If (player.mood < 40, 15, 0)),
        ("pub_waitress_work_talk8", If (player.mood < 25, 20, 0)),
        ("pub_waitress_work_talk9", 10),
        ("pub_waitress_work_talk10", If (player.iswhore and not player.has_perk(perk_freeuse), 10,0)),
        ])

label pub_waitress_work_talk1:
    patron "What is a pretty girl like you doing working here?"
    pc "Same as all the other pretty girls here. To pay the bills."
    patron "You could work up by the highway."
    if quest_whore.sex > 5:
        pc "I do now and then, but safer in here."
        patron "Oh? Then why work here at all?"
        pc "Safer. And can't spend all day on the street whoring. Plus, here gets guys like you buying me drinks."
        if numgen():
            patron "Well, good for me then to get your company."
            "I stand there chatting away for some more time, perfectly aware of his hand slowly creeping up my thigh."
            pcm "These tips better be worth it."
            $ player.add_desire_random(10)
            $ player.add_mood(-5)
            jump pub_waitress_work_cycle2
        else:
            patron "So not interested if I offer you some money?"
            pc "You can always offer."
            $ player.set_whore_price(0)
            patron "Err, how does £[player.soldprice] sound?"
            if player.check_whore_agree_choice():
                jump whore_street_customer_pick_location_tombola
            else:
                jump pub_waitress_work_talk3_refuse
    elif player.check_nowill():
        pc "Eh, I couldn't do that. Far too scary."
        patron "Better paid than here I would think."
        pc "Yeah, I don't think my raped corpse has much use for money."
        show pub_serve_talking touch with dissolve
        patron "Well, good for me then to get your company."
        "I stand there chatting away for some more time, perfectly aware of his hand slowly creeping up my thigh."
        pcm "These tips better be worth it."
        $ player.add_desire_random(10)
        $ player.add_mood(-5)
        jump pub_waitress_work_cycle2
    else:
        if player.has_perk(perk_preg_want):
            pc "And end up with some filth giving me a baby? No thanks, I'd prefer someone a bit better for that job."
        else:
            pc "Then I'd be fat with a baby in no time. No thanks."
        patron "Could always do it in the other hole."
        if player.check_anal_agree(notif=False) and player.check_sex_agree(2, notif=False):
            pc "Still means I have to walk the highway letting men take me in the arse. Rather just sit on mine and talk to you lot."
            show pub_serve_talking touch with dissolve
            patron "Well, good for me then to get your company."
            "I stand there chatting away for some more time, perfectly aware of his hand slowly creeping up my thigh."
            pcm "These tips better be worth it."
            $ player.add_desire_random(10)
            $ player.add_mood(-5)
            jump pub_waitress_work_cycle2
        elif player.check_sex_agree(1, notif=False):
            $ pub_tips()
            pc "Then I would have a sore arse and couldn't sit here talking to you."
            show pub_serve_talking touch with dissolve
            patron "Ahh, we wouldn't want that now would we?"
            "I stand there chatting away for some more time, perfectly aware of his hand slowly creeping up my thigh."
            pcm "These tips better be worth it."
            $ player.add_desire_random(10)
            $ player.add_mood(-5)
            jump pub_waitress_work_cycle2
        else:
            $ player.face_happy()
            pc "Pffft. Hahahaha!"
            $ player.add_mood(3)
            hide pub_serve_talking with dissolve
            "I walk away laughing at the guy's comment."
            jump pub_waitress_work_cycleend

label pub_waitress_work_talk2:
    $ player.set_whore_price(0)
    patron "So how much for you and me to have fun somewhere alone?"
    if player.has_perk([perk_meek, perk_broken], notif=True):
        pc "Whatever you are offering."
        patron "Err, how does £[player.soldprice] sound?"
        pc "Okay."
        jump whore_street_customer_pick_location_tombola

    elif player.has_perk([perk_whore, perk_sucu], notif=True):
        pc "Name a price."
        patron "Hmm, how does £[player.soldprice] sound?"
    else:
        pc "I think you came to the wrong place if that's what you are after."
        patron "It wasn't what I came here for, but after seeing you, I just had to ask."
        if not player.sold:
            pcm "Never sold myself before, but I guess it can't hurt to hear him out."
        elif player.sold == 1:
            pcm "Well, I did it once before, so maybe I could at least hear him out."
        elif player.sold < 10:
            pcm "Well, it's not like I haven't sold myself before. I can at least hear him out."
        if player.sold:
            pc "You had better have a fat wallet to be asking such things."
            patron "Well lets see if it's fat enough. How does £[player.soldprice] sound?"
        else:
            pc "Err, what did you have in mind?"
            patron "How does £[player.soldprice] sound?"
    if player.check_whore_agree_choice():
        jump whore_street_customer_pick_location_tombola
    else:
        jump pub_waitress_work_talk3_refuse






































label pub_waitress_work_talk3_refuse:
    pc "Heh, no thanks. Maybe you should offer it to one of the other girls."
    patron "No harm done. Have a nice evening."
    pc "You too."
    $ player.add_desire_random(10)
    $ player.add_mood(-5)
    $ player.add_conf(3)
    hide pub_serve_talking with dissolve
    pc "..."
    if player.soldprice > 0:
        pc "£ [player.soldprice] isn't a small amount of money..."
    else:
        pc "Earning money in such a way..."
    jump pub_waitress_work_cycleend

label pub_waitress_work_talk3:
    patron "Here, you might as well have this beer. My friend went to the toilet ages ago and hasn't come back."
    pc "What happened to him?"
    $ player.right_hand = "beer"
    patron "Let's pretend he has a nice barmaid in there with him and not that he is hugging the toilet bowl after drinking so much."
    $ pub_tips()
    if player.drunk >= 60:
        pc "At this rate a might have to join him in hugging the bowl."
        show pub_serve_talking touch with dissolve
        patron "Hah, don't worry darling, I'll take care of you if that happens."
        pc "I'll hold you to that..."
        $ player.add_desire_random(20)
        $ player.beer(spiked=True)
        "I hang out with the guy drinking his beer while chatting away. All the while I am perfectly aware of his hand climbing up my bare leg until eventually he is rubbing at my labia."




        jump pub_waitress_work_cycle2

    pc "Ah, hope he doesn't make too much of a mess. Might be me having to clean it up."
    $ player.beer(spiked=True)
    patron "Let's hope he is with a barmaid then."
    pc "Heh, let's."
    "I hang out with the guy drinking his beer while chatting away."
    jump pub_waitress_work_cycle2

label pub_waitress_work_talk4:
    patron "So darling. I want to ask a question."
    pc "Ok, go for it."
    show pub_serve_talking touch with dissolve
    patron "How much to buy these socks off you?"
    $ player.add_desire_random(10)
    if player.check_sell_clothes("socks"):
        pc "What are you offering?"
        $ pub_sell_socks()
        patron "How about £[pub_waitress.missionvar2]?"
        if player.has_perk([perk_meek, perk_broken], notif=True):
            $ NullAction()
        else:
            menu:
                "Sounds good":
                    $ NullAction()
                "No thanks":

                    if pub_waitress.missionvar2 <= item_socks_7.value:
                        pc "No thanks. Costs me more than that to replace them."
                    else:
                        pc "Sorry mate, not interested."
                    patron "You sure? Ah well, was worth asking."
                    $ pub_waitress.missionvar2 = 0
                    pc "Sure..."
                    pcm "The hell does someone want my socks for? Perverts of all types in this place."
                    "I spend the next few minutes chatting with him, wondering if he will bother to remove his hand from between my legs."
                    jump pub_waitress_work_cycle2

        pc "Sure, why not?"
        patron "Great!"
        pc "I'll go to the changing room to take them off then come back. Make sure you have the money ready."
        $ randomnum = renpy.random.randint(0, 5)
        if randomnum == 0:
            patron "Wait, let me watch you taking them off so I know they are the same ones."
            pc "Ugh really? Okay whatever."
            hide pub_serve_talking with dissolve
            jump pub_waitress_work_sell_socks
        else:
            hide pub_serve_talking with dissolve
            $ walk(loc_pub_changingroom)
            "I go into the back room and quickly remove my socks."
            $ c.socks = 0
            $ wardrobe.drop(item_socks_7)
            pcm "The hell does someone want my socks for? Perverts of all types in this place."
            $ walk(loc_pub)
            show pub_serve_talking with dissolve
            pc "Here you go. Enjoy whatever you plan to do with them."
            patron "Don't worry sweetie, I will."
            show pub_serve_talking touch with dissolve
            patron "And your legs look so much more sexy without those socks hiding them."
            pc "Err, thanks..."
            pc "Well I had better get back to it, enjoy your evening."
            jump pub_waitress_work_cycle2
    else:

        pc "Hah, enjoy your beer mate."
        $ player.add_conf(3)
        $ player.add_mood(-5)
        jump pub_waitress_work_cycle2

label pub_waitress_work_talk5:
    patron "So darling. I want to ask a question."
    pc "Ok, go for it."
    show pub_serve_talking touch with dissolve
    patron "How much to buy what you are wearing under your skirt?"
    $ player.add_desire_random(10)
    if not c.pants:
        pc "Sorry mate, there isn't anything under there to buy."
        patron "Oh..."
        if not numgen(0,5):
            patron "Then how much to buy you?"
            pc "Seriously?"
            if player.check_whore():
                if player.sold == 1:
                    pcm "Well, I did it once before, so maybe I could at least hear him out."
                elif player.sold < 10:
                    pcm "Well, it's not like I haven't sold myself before. I can at least hear him out."
                elif player.check_poor():
                    pcm "I am in desperate need for money..."
                pc "Make an offer and I'll consider it."
                $ player.set_whore_price(0)
                patron "How does £[player.soldprice] sound?"
                if player.check_whore_agree_choice():

                    jump whore_street_customer_pick_location_tombola
                else:

                    pc "Heh, no thanks. Maybe you should offer it to one of the other girls."
                    patron "No harm done. Have a nice evening."
                    pc "You too."
                    $ player.add_desire_random(10)
                    hide pub_serve_talking with dissolve
                    pc "..."
                    pc "£ [player.soldprice] isn't a small amount of money..."
                    jump pub_waitress_work_cycleend
            else:

                pc "Heh, no thanks. Maybe you should offer it to one of the other girls."
                patron "No harm done. Have a nice evening."
                pc "You too."
                $ player.add_desire_random(10)
                hide pub_serve_talking with dissolve
                pc "..."
                jump pub_waitress_work_cycleend



        patron "Wow! Nice."
        pc "Enjoy your beer."
        jump pub_waitress_work_cycle2

    elif player.check_sell_clothes("pants"):
        pc "What are you offering?"
        $ pub_sell_pants()
        patron "How about £[pub_waitress.missionvar3]?"
        if player.has_perk([perk_meek, perk_broken], notif=True):
            $ NullAction()
        else:
            menu:
                "Sounds good":
                    $ NullAction()
                "No thanks":

                    $ pub_waitress.missionvar3 = 0
                    pc "Sorry mate, not interested."
                    patron "You sure? Ah well, was worth asking."
                    pc "Sure..."
                    pcm "Offering to buy pants? Not sure what good they will do him but perverts come in all types."
                    "I spend the next few minutes chatting with him, wondering if he will bother to remove his hand from between my legs."
                    jump pub_waitress_work_cycle2

        pc "Sure, why not?"
        patron "Great!"
        pc "I'll go to the changing room to take them off then come back. Make sure you have the money ready."
        if not numgen(0,5):
            patron "Wait, let me watch you taking them off so I know they are the same ones."
            pc "What? Really...?"
            pc "Ok, but nothing funny ok?"
            hide pub_serve_talking with dissolve
            jump pub_waitress_work_sell_pants
        else:
            hide pub_serve_talking with dissolve
            $ walk(loc_pub_changingroom)
            "I go into the back room and quickly remove my pants."
            show pub_undress with dissolve
            show pub_undress pants_off with dissolve
            pcm "Offering to buy pants? Not sure what good they will do him but perverts come in all types."
            $ wardrobe.drop(item_pants_6)
            show pub_undress stand with dissolve
            hide pub_undress with dissolve
            $ walk(loc_pub)
            show pub_serve_talking with dissolve
            pc "Here you go. Enjoy whatever you plan to do with them."
            patron "Don't worry sweetie, I will."
            show pub_serve_talking touch with dissolve
            pc "Ah hey."
            patron "Just making sure you are missing them and didn't just get some random pair from the back."
            $ player.add_desire_random(10)
            pc "Err, well, as you can feel, nothing under there any more."
            patron "Mmmmm. Yes I can feel."
            pc "Well I had better get back to it, enjoy your evening."
            jump pub_waitress_work_cycle2
    else:

        pc "Sorry mate, not interested."
        patron "You sure? Ah well, was worth asking."
        pc "Sure..."
        pcm "Offering to buy pants? Not sure what good they will do him but perverts come in all types."
        "I spend the next few minutes chatting with him, wondering if he will bother to remove his hand from between my legs."
        jump pub_waitress_work_cycle2

label pub_waitress_work_talk6:
    patron "You know all the guys here come to watch you girls prance around in your tiny skirts?"
    pc "Prance around? We are serving beers, not my fault you are all perverts."
    patron "Haha. Sure."
    show pub_serve_talking mast with dissolve
    $ pub_waitress.missionvar1 = True
    $ player.add_desire_random(5)
    if not player.check_sex_agree(0):
        $ player.face_shock()
        pc "Ehhhh?"
        hide pub_serve_talking with vpunch
        "I quickly leave the pervert."
        pc "Christ... Getting his cock out like that..."
        jump pub_waitress_work_cycleend

    if player.check_sex_agree(1, notif=False):
        pc "Kinda bold of you to whip your cock out here. We aren't a porn show you know?"
    else:
        pc "Errm what are you doing?"
        patron "Enjoying you prancing around."
        pc "This isn't a live porn show you know?"

    if c.pants == 0:
        show pub_serve_talking touch with dissolve
        patron "You are walking around flashing that bare arse of yours and you are telling me this isn't a live porn show? Who are you kidding?"
        pc "I lost my pants..."
        patron "Yeah, \"lost\". Were they taken as a souvenir by someone after fucking you or did you just sell them to some pervert?"
        patron "Or maybe you want to flash your arse to people to let them know you are up for sale?"
        pc "..."
        patron "So how much do you cost?"
        if player.check_whore():
            pc "Make an offer."
            $ player.set_whore_price(0)
            patron "Lets see how much I have... £ [player.soldprice]?"
            pcm "£ [player.soldprice]? It's not bad..."
            if player.check_whore_agree_choice():
                pc "Okay then, lets go."
                $ randomnum = renpy.random.randint(0, 30)
                if randomnum == 0:
                    patron "No thanks, I just wanted to confirm how much of a whore you girls are in this place. Now that I know you can fuck off now you dirty slut."
                    $ player.face_angry()
                    pc "Fucker!"
                    hide pub_serve_talking with dissolve
                    pc "What a prick!"
                    $ player.add_mood(-15)
                    jump pub_waitress_work_cycleend
                else:
                    jump whore_street_customer_pick_location_tombola
            else:
                $ NullAction()


        pc "Not for sale I'm afraid. Just here to keep you chaps company."
        patron "Well, I can settle for that. What more could a guy ask for than the company of someone as pretty as you are?"
        "I chat away to the guy for some time while he gropes at my leg and touches himself."
        pcm "Ugh, I need the money but this..."
        $ player.add_desire_random(10)
        $ player.add_mood(-5)
        jump pub_waitress_work_cycle2

    elif pub_waitress.socks == 0:
        show pub_serve_talking touch with dissolve
        patron "Strutting those bare legs of yours makes people round here a bit excited sweetheart."
        pc "They are too hot to be wearing all the time..."
        patron "And nothing to do with the extra tips they bring in?"
        pc "Extra tips are always welcome."
        "He pulls my thigh towards him and sits me down on his lap."
        jump pub_waitress_work_lap

    patron "Maybe not, but a mans gotta try and enjoy himself any way he can. And you aren't running off to security so it doesn't seem you mind."
    pc "I have seen a lot worse in this place. You are all a bunch of dirty perverts."
    patron "Heh, such a pretty flower in this shithole. Managing to stay sweet while being hardened to all this shit around you."
    pc "Wha...? Sure, whatever you say."
    pc "So, you gonna put your cock away or what?"
    $ randomnum = renpy.random.randint(0, 35)
    if randomnum <= 5:
        show pub_serve_talking touch with dissolve
        patron "No, I am happy like this."
        "He pulls my thigh towards him and sits me down on his lap."
        jump pub_waitress_work_lap
    elif randomnum > 20:
        patron "If you insist."
        show pub_serve_talking down with dissolve
        $ pub_waitress.missionvar1 = False
        pc "I'm kinda surprised you did."
        patron "Ah well, It's no fun with you being so indifferent."
        if player.check_sex_agree(2):
            pc "Not indifferent, it was a nice cock. But to pull it out in such a public place is a bit much."
        else:
            pc "Well to do it in such a public place is a little much."
        "I chat away with the guy for a little bit."
        jump pub_waitress_work_cycle2
    else:
        patron "No, I think I'll keep touching myself. Not like I have anything better to do."
        pc "Well don't be making a mess on the seats since other people will sit there. Aim it to the floor if it comes to that..."
        patron "Would probably aim it at you if it comes to that."
        pc "Such a gentleman..."
        "I chat to the masturbating pervert for a little more, making sure to do a runner if he aims his thing at me."
        $ player.add_desire_random(10)
        $ player.add_mood(-5)
        $ player.add_conf(3)
        jump pub_waitress_work_cycle2

label pub_waitress_work_talk7:
    $ dialouge = renpy.random.choice([
    "Christ girl. It looks like you need one of these more than I do.",
    "You look like you are sucking on a lemon. Why not have a drink yourself?",
    "Think you could do with one of these more than me.",
    "Here, looks like you need one of these as well"
    ])
    patron "[dialouge]"
    $ player.right_hand = "beer"
    pc "Yeah tell me about it..."
    "I relax with the guy and drink some beer with him."
    $ player.beer(spiked=True)
    pc "Cheers mate, but I had better get back to it. Thanks for the beer."
    patron "No problem."
    jump pub_waitress_work_cycle2

label pub_waitress_work_talk8:
    $ dialouge = renpy.random.choice([
    "One of these are for you sweetheart. That look on your face tells me you need it.",
    "This ones yours darling. Looks like you are having one of those days.",
    "After seeing that look on your face I got this one for you."
    ])
    patron "[dialouge]"
    $ player.right_hand = "beer"
    pc "Mmm, cheers. I could do with it."
    "I relax with the guy and drink some beer with him."
    $ player.beer(spiked=True)
    pc "Cheers mate, but I had better get back to it. Thanks for the beer."
    patron "No problem."
    jump pub_waitress_work_cycle2

label pub_waitress_work_talk9:
    show pub_serve_talking mast with dissolve
    $ pub_waitress.missionvar1 = True
    patron "Lucky me getting the prettiest girl in this place to keep me company."
    pc "Pretty sure the other girls here..."
    "I notice he has his cock out and has his hand wrapped around it."
    if player.check_sex_agree(2, notif=False):
        $ player.face_conf()
    else:
        $ player.face_shock()
    pc "Err..."
    patron "Like what you see?"
    $ player.add_desire_random(5)
    if player.has_perk([perk_meek, perk_broken], notif=True):
        pc "I guess..."
    elif player.has_perk([perk_slut, perk_sucu], notif=True):
        pc "Not bad looking. You enjoying yourself there?"
    elif not player.check_sex_agree(1):
        pc "Ehhhh?"
        hide pub_serve_talking with dissolve
        "I quickly leave the pervert."
        pc "Christ..."
        jump pub_waitress_work_cycleend
    elif player.check_sex_agree(1, notif=False):
        pc "Should have known when you asked me to chat you would be touching yourself..."
    else:
        pc "Is everyone in this place a pervert?"
        patron "Suppose you would have to ask them."
        pc "This isn't a live porn show you know?"
    if c.pants == 0:
        patron "Well, seeing you flashing your sweet cheeks around the pub made him want to say hello to you."
    elif pub_waitress.socks == 0:
        patron "Well, seeing your lovely legs made him want to say hello to you."
    elif player.breasts == 3:
        patron "Well, seeing those giant tits of yours bouncing around while you're walking around made him want to say hello to you."
    else:
        patron "Well, seeing you prancing around in that tiny skirt made him want to say hello to you."
    pc "Hello and goodbye to your friend. Stick him back in before someone notices"
    patron "The one person I wanted to notice already has, and she hasn't taken her eyes off it since she did see it."
    $ player.face_shy()
    pc "..."

    if player.has_perk(perk_whore, notif=True):
        pc "Going to have to get your wallet out as well as your cock if you want to continue."
        patron "Oh? You are up for that?"
        pc "Make an offer."
        $ player.set_whore_price(0)
        patron "Err, how about £[player.soldprice]"
        if player.check_whore_agree_choice():
            jump whore_street_customer_pick_location_tombola
        else:
            pc "I'll leave you and your friend alone and get back to work. Enjoy your evening."
            jump pub_waitress_work_cycle2
    elif player.has_perk([perk_slut, perk_sucu], notif=True):
        pc "Well I'm not on to shy away from a nice cock."
        patron "Oh? And you called me bold."
        "He wraps his arm around my waist and pulls me to sit on his lap."
        hide pub_serve_talking with dissolve
        jump pub_waitress_work_lap_choices
    elif player.has_perk([perk_meek, perk_broken], notif=True):
        pc "Errm..."
        pc "..."
        patron "You like it do you?"
        patron "Come here."
        "He wraps his arm around my waist and pulls me to sit on his lap."
        hide pub_serve_talking with dissolve
        jump pub_waitress_work_lap_choices
    elif player.check_sex_agree(4):
        pcm "It's huge... How can I not stare..."
        pc "I'll, err... Leave you and your friend alone and get back to work. Enjoy your evening."
        pc "..."
        patron "Normally when you tell someone you are leaving, you actually leave."
        patron "Come here."
        "He wraps his arm around my waist and pulls me to sit on his lap."
        hide pub_serve_talking with dissolve
        jump pub_waitress_work_lap_choices
    else:
        pc "I'll leave you and your friend alone and get back to work. Enjoy your evening."
        jump pub_waitress_work_cycle2

label pub_waitress_work_talk10:
    pcm "Hmm, he's alone. Should I offer him some company?"
    menu:
        "Get back to work":
            jump pub_waitress_work_cycleend
        "Offer company":


            pc "You know if you are lonely you can pay for some company."
            $ randomnum = renpy.random.randint(1, 10)
            if randomnum == 1:
                patron "Yeah, but I would prefer not to. Any girl I would like to be with would be out of my price range. And ones I can afford..."
                patron "Well, I'm sure you have seen the dirty girls on the highway."
                pc "What's your price range?"
                $ player.set_whore_price(-4)
                patron "Pfft, about ... £ [player.soldprice]"
                pc "Not much is it?"
                patron "That's why I am sitting here with cheap beers and not a sexy girl."
                if player.check_sex_agree(4):
                    pcm "I'm kinda excited, should I fuck him for that price?"
                    if player.check_whore_agree_choice(option1="Fuck him", option2="Say goodbye"):
                        pc "It's not a lot, but I'm not doing much else right now. You can have me for that."
                        patron "What? Really?"
                        patron "Na, you are just messing with me."
                        jump whore_street_customer_pick_location_tombola
                    else:

                        pc "Well enjoy the beer. They will never reject you."
                        patron "Ain't that the truth."
                        jump pub_waitress_work_cycleend
                else:
                    pc "Not gonna get a sexy girl for that. That is highway prices."
                    patron "Don't I know it."
                    jump pub_waitress_work_cycleend
            else:
                patron "And how much will come company cost?"
                $ player.set_whore_price(4)
                pc "Hmm, let's say £ [player.soldprice]"
                $ randomnum = renpy.random.randint(1, 50)
                if randomnum == 1:
                    patron "Now, we are talking me fucking you right? Not some sexless date."
                    pc "Sure, we will go to the back and I'll ride your cock."
                    patron "Ok, let's go then."
                    jump whore_street_customer_pick_location_tombola
                elif randomnum < 20:
                    $ player.set_whore_price(0)
                    patron "That's a bit rich for my blood. How about £ [player.soldprice]"
                    pc "Sounds good, follow me."
                    jump whore_street_customer_pick_location_tombola
                elif randomnum == 50:
                    $ player.set_whore_price(-4)
                    patron "Pfft, that is way out of my price range. I can offer £ [player.soldprice]"
                    pc "Not much is it?"
                    patron "That's why I am sitting here with cheap beers and not a sexy girl."
                    if player.check_sex_agree(4):
                        pcm "I'm kinda excited, should I fuck him for that price?"
                        if player.check_whore_agree_choice(option1="Fuck him", option2="Say goodbye"):
                            pc "It's not a lot, but I'm not doing much else right now. You can have me for that."
                            patron "What? Really?"
                            patron "Na, you are just messing with me."
                            pc "I'm not. Let's go somewhere more private."
                            jump whore_street_customer_pick_location_tombola
                        else:

                            pc "Well enjoy the beer. They will never reject you."
                            patron "Ain't that the truth."
                            jump pub_waitress_work_cycleend
                    else:
                        pc "Not gonna get a sexy girl for that. That is highway prices."
                        patron "Don't I know it."
                        jump pub_waitress_work_cycleend
                else:

                    patron "Sorry love, someone like you is way out of my price range."
                    pc "No worries, enjoy your beer."
                    jump pub_waitress_work_cycleend

label pub_waitress_work_talk11:
    pc "Beers are up."
    patron "Thanks..."
    pcm "Hmm, he's alone. Maybe I should... ♥"
    pc "This might sound a little bold. But can I ask you something?"
    patron "Pretty girl like you can ask anything she wants."
    pc "So..."
    pc "I want a baby."
    patron "*Cough*"
    pc "Problem is, I can't do that alone."
    patron "And you... *Ahem* Want my help?"
    pc "Yup ♥"
    patron "Ok... Sure."
    hide pub_serve_talking with dissolve
    "I grab his shirt and practically drag him out of his chair and across the pub."
    jump whore_street_customer_pick_location_tombola
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
