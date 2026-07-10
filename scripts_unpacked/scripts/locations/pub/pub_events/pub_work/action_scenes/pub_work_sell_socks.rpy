label pub_waitress_work_sell_socks:

    $ walk(renpy.random.choice([loc_pub_changingroom, loc_pub_toilet_girls, loc_pub_toilet_boys]))
    if loc_cur == loc_pub_changingroom:
        "I head to the back room with the guy so I can show him it is my socks I am selling."
    else:
        "I sneak into a toilet stall with the guy so I can show him it is my socks I am selling."
    show pub_undress with dissolve
    $ dialouge = WeightedChoice([
    ("Is it watching me takes these off that excites him or is it actually the socks?", 100),
    ("I can't imagine why someone would pay so much for some sweaty socks...", 100),
    ("Feels like he is watching my every movement.", 100),
    ("Better not let him see how hot I am or I could end up skewered...", player.desire),
    ("Better be careful, I don't have any pants on and he will no doubt notice", If (c.pants == 0, 500,0))
    ])
    pcm "[dialouge]"
    show pub_undress socks_off with dissolve
    $ dialouge = WeightedChoice([
    ("Damn girl, that uniform doesn't really hide much does it?", 100),
    ("Take your time darling. The view from here is lovely.", 100),
    ("Forget to wear your pants or did you already sell them?", If (c.pants == 0, 200,0)),
    ("Damn girl, you are so wet I can see it in your pants. You love this as much as I do.", If (player.desire > 80 and c.pants, player.desire,0)),
    ("Damn girl, you are so wet I can see it from here. You love this as much as I do.", If (player.desire > 80 and not c.pants , player.desire,0)),
    ("You could hardly walk while coming here girl, you sure you aren't gonna just fall over?", If (player.drunk > 50, player.drunk,0)),
    ("You really are a drunken slut aren't you?", If (player.drunk > 50 and player.desire > 80, (player.drunk + player.desire) / 2,0))
    ])
    patron "[dialouge]"
    $ rand_choice = WeightedChoice([
    ("pub_waitress_work_sell_socks_sold", 300),
    ("pub_waitress_work_sell_socks_paysex_start", If (c.pants > 0, 500,0)),
    ("pub_waitress_work_sell_socks_forcesex", 30),
    ("pub_waitress_work_sell_socks_drunkhornysex", If (player.check_drunk(3, notif=False) and player.check_sex_agree(3, notif=False), 100,0)),
    ("pub_waitress_work_sell_socks_drunkhornysex", If (player.check_drunk(4, notif=False) and player.check_sex_agree(2, notif=False), 100,0)),
    ("pub_waitress_work_sell_socks_masturbate_start", 150)
    ])
    jump expression rand_choice

label pub_waitress_work_sell_socks_end:
    show pub_undress no_man with dissolve
    hide pub_undress with dissolve
    "I fix up my clothes and head out with the pervert and get back to work."
    $ walk(loc_pub)
    patron "See you round darling."
    pc "Sure."
    jump pub_waitress_work_cycleend

label pub_waitress_work_sell_socks_sold:
    pc "..."
    $ wardrobe.drop(item_socks_7)
    show pub_undress stand with dissolve
    patron "Nice. You look so much nicer with your legs bare."
    pc "Err... Thanks? Here you go. Satisfied they are mine?"
    patron "Sure am sweetheart, here's your money."
    hide pub_undress with dissolve
    "He leaves looking quite satisfied with himself."
    pc "Well, easy money I suppose..."
    jump pub_waitress_work_cycleend

label pub_waitress_work_sell_socks_paysex_start:
    pc "..."
    $ wardrobe.drop(item_socks_7)
    show pub_undress stand with dissolve
    patron "Nice. You look so much more lovely with your legs bare."
    show pub_undress man with dissolve

label pub_waitress_work_sell_socks_paysex_start_1:
    pc "Err... Thanks? Here you go..."
    pc "Erm... What are you doing?"
    $ dialouge = WeightedChoice([
    ("Getting my moneys worth.", 5),
    ("I'm enjoying the sight of you bent over.", 5),
    ("Enjoying the view of your naked arse.", If (c.pants == 0, 5,0)),
    ("Seeing you bent over with your bare pussy on display, how can I resist?", If (c.pants == 0, 5,0)),
    ("With a little slut in front of me who is soaking through her pants, how can I resist?", If (player.desire > 80 and c.pants > 0, 10,0)),
    ("How can I resist that soaked pussy?", If (player.desire > 80 and c.pants == 0, 10,0)),
    ("Making the most out of the situation.", If (player.drunk > 50, 10,0)),
    ("Having fun with a drunk little slut.", If (player.drunk > 50 and player.desire > 80, 10,0))
    ])
    patron "[dialouge]"
    pc "This isn't some private show you know?"
    patron "But it can be..."
    if player.vvirgin and not player.check_sex_agree(5):
        if player.vvirgin:
            pc "Fuck no! The way you are rubbing me there is no way I leave still a virgin."
        else:
            pc "Fuck no! You will stick it in me the moment they are down."
        hide pub_undress with dissolve
        pc "You got what you paid for, now leave while I get back to work."
        if danger_gen(200, 1):
            "I start to usher the pervert out the room when..."
            jump pub_waitress_work_ko
        "I usher the pervert out and get back to work."
        $ walk(loc_pub)
        if player.vvirgin == True:
            pcm "No way am I going to sell a pervert like him my virginity."
        jump pub_waitress_work_cycleend

    if c.pants == 0:
        pc "Hey. Don't be rubbing me there."
        if player.desire >= 80:
            patron "Fuck, you are so wet there."
            pc "All the more reason for you to stop. Don't want you trying to slip it in."
        patron "You love it just as much as me. Why else would you be walking around without anything on under your skirt?"
        pc "Perverts keep taking them from me."
        patron "So how much to fuck you?"
        if player.check_whore():
            pc "Make an offer."
            $ player.set_whore_price(0)
            patron "How about £ [player.soldprice]?"
            if player.sold <= 5:
                pcm "That's not a bad amount of money. Am I really willing to sell myself for £ [player.soldprice]?"

            menu:
                "Agree":
                    jump pub_waitress_work_sell_socks_paysex_sex
                "Refuse":
                    jump pub_waitress_work_sell_socks_sex_reject
        else:
            pc "What? I am not a whore!"
            patron "My hard cock is rubbing your slit, I think it's a bit late to keep lying to yourself."
            pc "..."
            if player.check_sex_agree(4):
                pc "You are teasing me too much."
                jump pub_waitress_work_sell_socks_sex_want
            else:
                pc "I don't want your money! And I am out of here."
                hide pub_undress with dissolve
                if danger_gen(200, 1):
                    "I start to leave the room when..."
                    jump pub_waitress_work_ko
                "I quickly rush out before anything else can happen."
                jump pub_waitress_work_cycleend
    else:

        $ player.spank()
        pc "Ahh. "
        patron "Mmmmm..."
        pc "Hey, I didn't agree to this."
        patron "No? Okay then. How much for your pants then?"
        jump pub_waitress_work_sell_socks_paysex_sex

label pub_waitress_work_sell_socks_drunkhornysex:
    pc "..."
    $ wardrobe.drop(item_socks_7)
    show pub_undress stand with dissolve
    patron "Nice. You look so much nicer with your legs bare."
    show pub_undress man with dissolve
    pc "Thanks sweetie? Here you go..."
    pc "Hey now ♥ Socks was the deal here."
    jump pub_waitress_work_sell_socks_drunkhornysex_1

label pub_waitress_work_sell_socks_drunkhornysex_1:

    if player.drunk > player.desire:
        $ dialouge = WeightedChoice([
        ("How can I resist a drunken barmaid bent over in front of me?", 5),
        ("A little drunk slut showing me her ass, How can I resist?", 5),
        ("With a drunk little slut in front of me who is soaking through her pants, how can I resist?", 5),
        ("I'm just having fun with a drunk little slut.", 5)
        ])
    else:
        $ dialouge = WeightedChoice([
        ("How can I resist a horny little barmaid bent over in front of me?", 5),
        ("I can see you soaking into your pants. Don't try and tell me you don't want this.", 5),
        ("With a horny little slut in front of me who is soaking through her pants, how can I resist?", 5),
        ("Having fun with a dirty little slut.", 5)
        ])
    patron "[dialouge]"
    pc "You are such a romantic."
    patron "Let me show you how romantic."
    hide pub_undress with dissolve
    $ renpy.show(renpy.random.choice(["sb_againstwall2 pokevaghand wink worried", "sb_againstwall3 poke wink"]))
    pc "Ahh. "
    patron "Mmmmm..."
    pc "And here I thought you was going to give me flowers. Or at least some more beer."
    patron "I'll give you something much deeper than that."
    $ rand_choice = WeightedChoice([
    ("pub_waitress_work_sell_socks_paysex_sex", 5),
    ("pub_waitress_work_sell_socks_sex_want", player.drunk + player.desire / 25),
    ("pub_waitress_work_sell_socks_sex_reject", 3),
    ])
    if rand_choice == "pub_waitress_work_sell_socks_paysex_sex":
        patron "How about I buy those pants off you?"
    jump expression rand_choice

label pub_waitress_work_sell_socks_sex_reject:
    pc "Sorry, I can't do that."

    patron "No? Hmmm. Okay then..."
    if danger_gen(200, 1):
        pc "Enjoy the..."
        jump pub_waitress_work_ko

    pc "Enjoy the socks though."
    $ rand_choice = WeightedChoice([
    ("pub_waitress_work_sell_socks_end", 200),
    ("pub_waitress_work_sell_socks_forcesex", 30),
    ("pub_waitress_work_sell_socks_masturbate", 100),
    ])
    jump expression rand_choice

label pub_waitress_work_sell_socks_sex_want:
    $ player.sex_location_offer(
        diff=0,
        option1="Guide his cock into my pussy",option2="Press his cock against my ass", option3="Let him decide",
        sex_vag_want="whore_street_sex_standing_vag_picker",
        sex_vag_notwant="pub_waitress_work_sex_forced_anal",
        sex_anal="whore_street_sex_standing_anal",
        who=patron
    )

label pub_waitress_work_sell_socks_paysex_sex:
    if c.pants:
        pc "For my pants?"
        patron "Yup, how much for you to slide them down your legs right now?"
        $ dialouge = WeightedChoice([
        ("The moment I do that, he will be balls deep.", 1),
        ("I will be skewered right away if I sell them.", 1),
        ("He's already pressing against me, without my pants on there will be nothing stopping him...", 1),
        ("If I agree, there is no way I am leaving this room still a virgin.", If (player.vvirgin == True, 50,0)),
        ("Then I will get a good hammering hmmm?", If (player.drunk > 50 and player.desire > 80, 10,0)),
        ("Just take them off yourself and fuck me already!", If (player.drunk > 70 and player.desire >= 100, 50,0)),
        ])
        pcm "[dialouge]"
        $ player.set_whore_price(0)
        patron "How about £ [player.soldprice]?"
        if player.check_whore():
            menu:
                "Agree":
                    show pub_undress pants_off with dissolve
                    pc "Hmm, and what will you do with that thing? I can feel it pressing against me."
                    patron "Don't worry, it will go somewhere warm."
                    $ c.pants = 0
                    show pub_undress stand with dissolve
                    pc "Is that so?"
                    hide pub_undress
                    $ renpy.show(renpy.random.choice(["sb_againstwall2 pokevaghand wink worried", "sb_againstwall3 poke wink"]))
                    with dissolve
                    patron "Fuck yes!"
                    jump pub_waitress_work_sell_socks_sex_want
                "Refuse":
                    jump pub_waitress_work_sell_socks_sex_reject
        else:

            jump pub_waitress_work_sell_socks_sex_reject
    else:

        hide pub_undress
        $ renpy.show(renpy.random.choice(["sb_againstwall2 pokevaghand wink worried", "sb_againstwall3 poke wink"]))
        with dissolve
        jump pub_waitress_work_sell_socks_sex_want

label pub_waitress_work_sell_socks_forcesex:
    show pub_undress man with dissolve
    pc "Hey! What are yo..."
    if c.pants > 0:
        $ player.face_surprised()
        patron "Taking these off you."
        $ c.pants = 0

        pc "Hey! I didn't agr..."
    hide pub_undress
    show sb_againstwall3 poke squint worried pout
    with vpunch
    $ player.sex_forced(pubpatron, pub_waitress)
    $ player.sex_vag(pubpatron, pub_waitress)
    show sb_againstwall3 sex grit angry with hpunch
    $ player.face_pain()
    pc "AHH! What the fuck are you doing?!"
    pc "Get off!"
    jump pub_waitress_work_forcesex

label pub_waitress_work_sell_socks_masturbate_start:
    pc "..."
    $ wardrobe.drop(item_socks_7)
    show pub_undress stand with dissolve
    patron "Nice. You look so much nicer with your legs bare."
    show pub_undress man with dissolve
    pc "Err... Thanks? Here you go..."
    jump pub_waitress_work_sell_socks_masturbate

label pub_waitress_work_sell_socks_masturbate:
    pc "Erm... What are you doing?"
    $ dialouge = WeightedChoice([
    ("Getting my moneys worth.", 5),
    ("I'm enjoying the sight of you bent over.", 5),
    ("Enjoying the view of your naked arse.", If (c.pants == 0, 5,0)),
    ("With a little slut in front of me who is soaking through her pants, how can I resist?", If (player.desire > 80 and c.pants > 0, 10,0)),
    ("How can I resist that soaked pussy?", If (player.desire > 80 and c.pants == 0, 10,0)),
    ("Making the most out of the situation.", If (player.drunk > 50, 10,0)),
    ("Having fun with a drunk little slut.", If (player.drunk > 50 and player.desire > 80, 10,0))
    ])
    patron "[dialouge]"
    pc "You have porn mags for this kind of thing."
    patron "The real thing is so much better."
    "I feel him behind me furiously masturbating while looking at my body."
    pc "..."

    if player.check_sex_agree(2, exhibitionist=True):
        pc "Ok, let's get this over with."
        $ renpy.scene()
        if numgen():
            show sb_againstwall3 cum wink
        else:
            show sb_againstwall2 cum
        with dissolve
        "I bend over to give him a better view to use me as his porn."
        if player.has_perk([perk_sucu, perk_preg_want]) and not player.vvirgin:
            pc "Stick it in me."
            patron "Oh?"
            $ if_showing("sb_againstwall3", "poke", "sb_againstwall2", "pokevaghand")
            $ player.sex_vag(pubpatron, pub_waitress)
            $ if_showing("sb_againstwall3", "sex", "sb_againstwall2", "insidevag")
            patron "Not... Going to..."
            pc "Good. Put it in me."
            $ player.sex_cum(nosex, "inside")
            patron "Ahhhhh."
        else:
            patron "Ahhhhh."
            "Behind me, I can hear him speeding up and grunting a lot more until..."
            $ player.sex_cum(nosex, "ass")
            patron "Ahhhh yes!!!"
            pc "..."
            patron "Ahhh so nice."
        $ if_showing("sb_againstwall2", "happy", "sb_againstwall3", "happy")
        pc "Had your fun?"
        patron "Sure did. It was great."
        $ if_showing("sb_againstwall2", "noman", "sb_againstwall3", "noman")
        pc "Good for you. I had better get back to work now."
        $ renpy.scene()
        with dissolve
        patron "Ok. See you in the bar."
        "He puts his trousers on and quickly leaves."
        if c.pants:
            pc "My pants are soaked with his cum now. *Sigh*"
        pc "Better wash this off before I head back out there."
        "I head to the sink and clean myself off."
        $ player.cum_clean_outside()
        pc "Ok, better get back out there."
        jump pub_waitress_work_cycleend
    else:

        pc "Well, good for you. I will leave you to it."
        hide pub_selling
        "I quickly grab my money and head out of the back room."
        $ walk(loc_pub)
        pc "Pervert"
        jump pub_waitress_work_cycleend
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
