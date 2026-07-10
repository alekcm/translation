label pub_waitress_work_table:

    $ rand_choice = WeightedChoice([
    ("pub_waitress_work_table1", If (player.drunk >= 70, 100,0)),
    ("pub_waitress_work_table2", If (player.drunk >= 70, 100,0)),
    ("pub_waitress_work_table3", If (player.drunk >= 70, 100,0)),
    ("pub_waitress_work_table4", If (player.mood < 20, 100,0)),
    ("pub_waitress_work_table5", If (player.check_drunk(5) and player.check_sex_agree(5), 100,0)),
    
    ("pub_waitress_work_cycleend", 1) 
    ])
    jump expression rand_choice


label pub_waitress_work_table1:
    show pub_serve_lap hump with dissolve
    "I try to get off the guys lap, but drunkenly stumble back down on him. He is more than happy to have me there."
    patron "I made that much of an impression on you did I?"
    pc "Maybe, or it was the booze. Probably the booze."
    patron "Well I don't mind, sit as long as you want."
    pcm "I can feel his cock throbbing against me in his trousers. This is making him hard."
    pc "Yeah I suspect not..."
    "I make a weak attempt to get back up, but with him holding my hips in place all I manage to do is grind my arse on his growing cock."
    patron "Keep that up and it's not gonna fit in my pants any more."
    pc "Heh, feels like it's already going to burst out as it is. What is some pervert like you doing with something that big in your pants?"
    patron "It's nothing special. You are just so tiny that everything must feel massive for you."
    pc "Never thought about that."
    show pub_serve_lap prep with dissolve
    show pub_serve_lap hump rub with dissolve
    pc "Errr, what are you doing?"
    patron "Giving it some freedom."
    if c.pants == 0:
        pcm "I have no pants on and it's already rubbing against me. This is a bit dangerous."
        pc "This isn't really the right kind of place for this..."
        patron "Seems like the right place to me."
        "He starts grind underneath me, rubbing his cock along my wet slit."
        $ player.add_desire_random(5)
        pc "Haaaa ♥"
        pc "Hey... You should stop that..."
        if player.check_sex_agree(5):
            "After saying that, I make another weak attempt to get off of him but all I end up doing is hump his cock."
            pc "Haaaa ♥"
            pc "This is too much..."
            "I start rubbing his cock against my clit and humping against him, making me feel even more excited."
            pc "Mmmmmm."
            patron "Enjoying that darling?"
            pc "♥"
            "I can feel him trying to angle himself with my humps in an attempt to get inside me."
            patron "Mmmm, let's put it where it wants to go."
            if player.vvirgin:
                pcm "At this rate he will take my virginity. Maybe I can get him off like this..."
                "I start to press his cock against my clit and grind harder against him trying to get him, and myself, off."
                if player.check_sex_agree(4):
                    jump pub_waitress_work_table_sex_virgin
                else:
                    jump pub_waitress_work_table_hump
            else:

                menu:
                    "Fuck him":
                        jump pub_waitress_work_table_sex
                    "Just keep humping him":
                        jump pub_waitress_work_table_hump
        else:

            "I try and manage to stand up again. And without saying goodbye I head back to the bar to continue work."
            $ player.add_desire_random(10)
            pcm "Whew. That was hot! ♥"
            jump pub_waitress_work_cycleend
    else:

        if player.check_sex_agree(3):
            jump pub_waitress_work_table_sex_pants
        else:
            "I try and manage to stand up again. And without saying goodbye I head back to the bar to continue work."
            $ player.add_desire_random(10)
            pcm "Whew. That was hot! ♥"
            jump pub_waitress_work_cycleend

label pub_waitress_work_table2:
    show pub_serve_lap hump with dissolve
    "I try to get off the guys lap, but drunkenly stumble back down on him. He is more than happy to have me there."
    patron "I could get used to this."
    pcm "Legs are starting to feel like jelly. Maybe I shouldn't have drunk so much"
    pc "Give me a moment."
    patron "Take your time."
    $ player.add_desire_random(5)
    "I attempt to get back up but the guy has his hands on my hips and isn't making it easy for me."
    patron "What's the hurry? Take a breather to get your sea legs back."
    pc "Huff..."
    pcm "This guys hands are all over me..."
    hide pub_serve_lap with dissolve
    "I finally make a proper effort to get up and break away from the perverts grip."
    pcm "Should be a bit more careful in future..."
    jump pub_waitress_work_cycleend

label pub_waitress_work_table3:
    show pub_serve_lap hump with dissolve
    "I try to get off the guys lap, but drunkenly stumble back down on him. He is more than happy to have me there."
    patron "If you wanted me between your legs, you could have just asked."
    pc "Very funny..."
    patron "Who's joking?"
    show pub_serve_lap prep with dissolve
    show pub_serve_lap hump rub with dissolve
    "The man shifts under me and pulls his trousers down."
    pc "Fuck, calm down fella."
    "His hands start to grope me all over my body."
    if c.pants == 0:
        patron "Good job you came prepared, not wearing anything under this tiny skirt of yours."
        patron "Now be a good little whore and sit on it."
        menu:
            "Whores get paid" if player.check_whore():
                pc "Good little whores get paid first."
                $ player.set_whore_price(0)
                patron "Tsk, here you go then."
                show pub_serve_lap prep with dissolve
                "He hands me £ [player.soldprice] then starts to shift under me planning to have me sit on his cock."
            "Ok..." if player.check_sex_agree(4):
                show pub_serve_lap prep with dissolve
                "I shift on top of him and position myself over his cock."
            "Get off.":
                if player.check_fight(2):
                    "I struggle against him and manage to disentangle myself from his grip. Having gained my freedom I walk away from him."
                    hide pub_serve_lap with dissolve
                    pc "Idiot!"
                    jump pub_waitress_work_cycleend
                else:
                    show pub_serve_lap prep with dissolve
                    "I struggle against him and start to stand up, but I am pulled back down on top of him."


                    $ player.sex_vag(pubpatron, pub_waitress)
                    show pub_serve_lap hump with dissolve
                    "Without intending to, I end up sitting on his cock, which he is quick to take advantage of and makes sure it finds it's way inside me."
                    patron "Mmmmmmm good girl."
                    pc "Shit, what are you doing?"
                    patron "Giving a dirty little girl what she wants."
                    pc "Huff huff"
                    pc "You arsehole..."
                    patron "Haaaaa..."
                    $ player.face_orgasm()
                    patron "Ahhhhh..."
                    $ player.sex_cum(pubpatron, "inside", pub_waitress)
                    "Without any warning, I feel his cock throbbing inside me and filling my wet pussy with his sperm. Pulse after pulse let's me know he is pumping me full of his life making seed."
                    pc "Ahhhh ♥"
                    $ player.face_normal()
                    pc "You didn't warn me..."
                    patron "Haaaa. It was so nice and warm in there. I wanted it to last as long as possible."
                    pc "Idiot, I didn't ask for this."
                    patron "No, but your pussy did."
                    show pub_serve_lap prep with dissolve
                    hide pub_serve_lap with dissolve
                    "I stand up, feeling his cock slide out of me, and without saying anything I go to the bathroom to clean up."
                    $ walk(loc_pub_toilet_girls)
                    pc "Ugh, what an arse..."
                    "I splash water on my face."
                    pc "Well whatever, let's get back to it."
                    jump pub_waitress_work_cycleend

        "I slide myself down the shaft of his cock until I am sitting on him again, but this time with him entirely inside me."


        $ player.sex_vag(pubpatron, pub_waitress)
        show pub_serve_lap hump with dissolve
        patron "Mmmmmmm good girl."
        pcm "This guy is a bit of a cunt."
        "I gently ride backward and forwards trying not to draw too much attention to what we are doing. Rhythmically fucking the hard cock that just entered my wet pussy."
        patron "Ah yes you dirty little slut."
        pc "Huff huff"
        patron "Haaaaa..."
        patron "I can feel it..."

        call pub_waitress_work_cumevent from _call_pub_waitress_work_cumevent_2

        hide pub_serve_lap with dissolve
        "I stand up, feeling his cock slide out of me, and without saying anything I go to the bathroom to clean up."
        $ walk(loc_pub_toilet_girls)
        pc "Not sure why I accepted an arsehole like him..."
        "I splash water on my face."
        pc "Well whatever, let's get back to it."
        jump pub_waitress_work_cycleend

    elif player.check_sex_agree(1):
        pc "People can probably see you."
        patron "And?"
        pc "Ugh."
        $ player.sex_hand(pubpatron, pub_waitress)
        "I let him be and slowly start to hump him, masturbating him as I grind forwards and backwards."
        patron "Mmmm, perfect service from a lovely little bitch."
        pc "You have such a way with words."
        patron "Treat 'em mean, keep 'em keen."
        patron "Now lets get those pants off you."
        menu:
            "Take him somewhere alone" if player.check_sex_agree(4):
                jump whore_street_customer_pick_location_tombola
            "Ignore him and keep humping" if player.check_sex_agree(2):
                "I ignore him and carry on grinding on his cock. Pressing it deep into my pants so I can enjoy as much as I can."
                pc "Mmmm, this feels good."
                patron "Ah baby."
                "I grind on him more vigorously and can feel some throbs from his cock. He is close so I press myself against him so he doesn't spray it everywhere."
                $ player.sex_cum(pubpatron, "ass", pub_waitress)
                patron "Haaaaaa ahhhaa."
                "I feel him squirting it in my hand and my pants start to feel warmer."
                pc "Mmmmmm."
                pc "That was fun."
                patron "Sure was."
                hide pub_serve_lap with dissolve
                "I get up off of him and go to the bathroom to clean myself up without even saying goodbye."
                $ walk(loc_pub_toilet_girls)
                pc "Ufff, that was a bit much doing that in public."
                "I clean my hands but there isn't much I can do about my wet pants."
                pcm "I'll just have to wait for them to dry on their own."
                pcm "Ok, back to earning money."
                jump pub_waitress_work_cycleend
            "Get up and leave":
                pc "Na, I'm out of here. You are far too much of a cunt to have fun with."
                patron "Hey."
                "I walk away ignoring him"
                jump pub_waitress_work_cycleend
    else:

        "I try and manage to stand up again. And without saying goodbye I head back to the bar to continue work."
        $ player.add_desire_random(10)
        pcm "Whew. That was hot! ♥"
        jump pub_waitress_work_cycleend

label pub_waitress_work_table4:
    "I try to get off the guys lap but his hands on my hips pull me back down on top of him."
    show pub_serve_lap hump with dissolve
    patron "Hey now, don't be in such a hurry to leave. I still have plenty of beer here."
    pc "Uff. Ok, nothing better to do."
    $ player.right_hand = "beer"
    patron "One of those days?"
    pc "Isn't it always? I just feel like shit."
    pc "Hey, your hands are wandering a bit much. Your supposed to listen to me complaining not try and get yourself off."
    patron "Sorry, sorry. Can do both though."
    pc "*Sigh*"
    $ player.beer()
    "I spend some time grumbling to the guy and enjoying his beer while his hands wander all over my body."
    $ player.add_desire_random(5)
    pc "Ok, that's enough groping for now. I'm heading back to it."
    hide pub_serve_lap with dissolve
    jump pub_waitress_work_cycleend

label pub_waitress_work_table5:

    show pub_serve_lap hump with dissolve
    "Instead of getting off the guys lap, I press forward so I am straddling him and rubbing my crotch into his groin."
    pc "You still have some beer left right?"
    patron "Sure do, here you go."
    $ player.right_hand = "beer"
    pc "Great."
    "I relax sitting on the guy and try to drink his beer whenever his tongue isn't in my mouth."
    "His cock grows bigger as I grind on him and his hands wander all over my body. Neither of us say anything but it's clear he's enjoying himself."
    pc "Think your friend is getting a bit excited. Gonna be hard to keep him there at this rate."
    patron "I think so too. Why don't we free him?"
    show pub_serve_lap prep with dissolve
    "I lift my weight off the guy, allowing him to undo his trousers and pull his cock out."
    show pub_serve_lap hump rub with dissolve
    if not c.pants:
        pc "That's better, I'm sure it wanted some fresh air."
        patron "Well, it certainly wanted something..."
        "He grips my hips and starts humping me. I can feel his cock between my ass cheeks and it feels like he is trying to angle for somewhere else."
        $ player.add_desire_random(5)
        with grope_trans
        pc "Haaaa ♥"
        with grope_trans
        pc "Mmmm, it seems your friend is having fun."
        "I start rubbing his cock against my wet slit, making me feel even more excited."
        pc "Mmmmmm."
        patron "Enjoying that darling?"
        pc "♥"
        "I can feel him pulling his cock further back with each trust and trying to find it's way inside me when pushing forward."
        patron "Mmmm, let's put it where it wants to go."

        if player.vvirgin:
            pcm "At this rate he will take my virginity. Maybe I can get him off just humping him..."
            "I press my arse down on his cock and grind harder against him trying to get him, and myself, off."

            if player.check_sex_agree(3):
                jump pub_waitress_work_table_sex_virgin
            else:

                jump pub_waitress_work_table_hump
        else:

            menu:
                "Fuck him":
                    jump pub_waitress_work_table_sex
                "Just keep humping him":
                    jump pub_waitress_work_table_hump
    else:
        jump pub_waitress_work_table_sex_pants

label pub_waitress_work_table_hump:
    "I can feel his cock getting harder and the pervert I am sitting on is breathing heavily."
    pc "Mmmm, this feels good."
    patron "Ah baby."
    "I grind on him more vigorously and can feel some throbs from his cock. I can feel he is close..."
    $ player.sex_cum(pubpatron, "ass", pub_waitress)
    patron "Haaaaaa ahhhaa."
    "I continue to grind on his cock until he is done spraying his load all over my arse and probably on the floor."
    pc "Mmmmmm."
    pc "That was fun."
    patron "Sure was."
    hide pub_serve_lap with dissolve
    $ walk(loc_pub_toilet_girls)
    pc "Ufff, that was a bit much..."
    pc "..."
    "I splash water on my face."
    pc "Ok, back to earning money."
    jump pub_waitress_work_cycleend

label pub_waitress_work_table_sex:
    pc "Mmmmmm..."
    show pub_serve_lap prep with dissolve
    "I sit up a bit and guide his cock between my lips then slowly slide down it feeling every vein as it enters me."
    $ player.sex_vag(pubpatron, pub_waitress)
    show pub_serve_lap hump with dissolve
    pc "Ahh fuck yes!"
    patron "Shhhh"
    pc "Huff huff."
    "I gently ride backward and forwards trying not to draw too much attention to what I am doing. Rhythmically fucking the hard cock that just entered my wet pussy."
    patron "Ah yes you dirty little slut."
    pc "Huff huff"
    patron "Haaaaa..."
    patron "I can feel it..."

    call pub_waitress_work_cumevent from _call_pub_waitress_work_cumevent_1


    show pub_serve_lap prep with dissolve
    hide pub_serve_lap with dissolve
    "I stand up, feeling his cock slide out of me, and without saying goodbye to him, I go to the bathroom to clean up."
    $ walk(loc_pub_toilet_girls)
    pc "Ufff, that was too much. Fucking him in the open like that..."
    "I splash water on my face."
    pc "Well whatever, let's get back to it."
    jump pub_waitress_work_cycleend

label pub_waitress_work_table_sex_pants:
    pc "That's better, I'm sure it wanted some fresh air."
    patron "Well, it certainly wanted something..."
    with grope_trans
    "I grind against him and feel his cock rubbing against my ass all the while his tongue invades my mouth."
    patron "Mmmm, perfect service from a lovely little barmaid."
    pc "Think yourself lucky, I just happened to have a need that you can fill."
    patron "Then how about we get those pants off you and a can fully fill your need?"
    pc "Mmmmm."
    $ player.beer()
    if player.check_sex_agree_choice(diff=2,option1="Sure, let's go" ,option2="Calm down fella"):
        $ player.left_hand = ""
        $ player.right_hand = ""
        hide pub_serve_lap with dissolve
        jump whore_street_customer_pick_location_tombola
    else:
        jump pub_waitress_work_table_hump

label pub_waitress_work_table_sex_virgin:
    "I can feel his cock getting harder and the pervert is breathing heavily while groping me and trying to kiss me."
    "When suddenly after sliding my pussy up his cock..."
    show pub_serve_lap prep with dissolve
    "It finds it's way between my legs and the tip of his penis poking right at my vagina..."
    pcm "Fuck, what do I do?"
    "The pervert presses down on my thighs and starts to lower me onto his cock."
    "I first feel my vagina stretching open as his cock head slides inside me. Then I start to feel full as it goes inside me deeper and I can feel myself sliding down his shaft."
    show pub_serve_lap hump with dissolve
    $ player.sex_vag(pubpatron, pub_waitress)
    $ player.face_excited()
    pcm "Ah fuck ♥ Virginity is overrated anyway. This is far too nice."
    "I give up even trying to resist and let his hands rove over my body and his tongue invade my mouth all while his cock takes my first time."
    "He starts to gently thrust inside me, not managing to get much leverage as I am putting most of my weight on him. But it doesn't matter."
    "I already had him on the verge while humping him."
    $ player.sex_cum(pubpatron, "inside", pub_waitress)
    patron "Ahhhhhhh."
    pc "♥ I can feel you pumping inside me."
    "I continue to grind on top of him enjoying the feeling of being full for the first time. Until his cock eventually deflates and slips out of me followed my a trickle of his cum."
    pc "That was fun."
    patron "Sure was."
    show pub_serve_lap prep with dissolve
    hide pub_serve_lap with dissolve
    "I get up off of him and go to the bathroom to collect myself."
    $ walk(loc_pub_toilet_girls)
    pc "Ufff, that was too much..."
    pc "..."
    "I splash water on my face."
    pc "Ok, ok. Not a virgin any more. But still need to earn money so better get back to it."
    jump pub_waitress_work_cycleend
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
