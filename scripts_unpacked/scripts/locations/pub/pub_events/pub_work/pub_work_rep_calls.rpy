label pub_waitress_work_cumevent:
    $ player.sex_cum_location_offer(difficulty=2, 
    cum_want="pub_waitress_work_cumevent_want",
    cum_notwant="pub_waitress_work_cumevent_notwant",
    cum_pullout="pub_waitress_work_cumevent_pullout",
    cum_pullout_poke="pub_waitress_work_cumevent_poke" 
    )

label pub_waitress_work_cumevent_want:
    if player.virgin_pregcheck:
        pc "Fill me up for my first time ♥"
        patron "Oh? I can do that."
        if player.has_perk(perk_preg_want):
            pc "Put a little baby in me."
            patron "Fuck. Little virgin wants to be knocked up?"
            pc "Yes!"
    patron "Ahhhhh..."
    $ player.face_orgasm()
    $ player.sex_cum(pubpatron, "inside", pub_waitress)
    "I feel his cock throbbing inside me filling my wet pussy with his sperm. Pulse after pulse I know he is pumping me full of his life making seed."
    pc "Ahhhh ♥"
    $ player.face_normal()
    pc "Mmmm, you filled me up..."
    patron "Haaaa. It was so nice and warm in there. I wanted it to last as long as possible."
    return

label pub_waitress_work_cumevent_pullout:
    if player.virgin_pregcheck == True:
        patron "Ahhhhh..."
        $ player.face_orgasm()
        $ player.sex_cum(pubpatron, "inside", pub_waitress)
        "I feel his cock throbbing inside me filling my wet pussy with his sperm. Pulse after pulse let's me know he is pumping me full of his life making seed."
        pc "Ahhhh ♥"
        pc "Fuck, I told you outside!"
        patron "How can I take your virginity and not leave you with my baby in return?"
        pc "What? Fuck! You want to get me pregnant?"
        patron "Of course. It's what sexy little sluts like you are best for."
        hide pub_serve_lap with dissolve
        "I stand up and immediately walk away. Probably leaving a trail of cum behind me."
        pc "Bastard!"
        pc "Ugh, I should have known better..."
        $ walk(loc_pub_toilet_girls)
        "I head to the toilet to wash my vagina."
        pc "Dammit, I shouldn't have let that fool take me like that. I need to be more careful with the booze."
        pc "School did warn me that people like him will try and give me a fat belly."
        $ player.pregnancy = 3
        pc "..."
        pc "Will I really end up like that if I am not careful?"
        pc "All bloated and milky with something growing inside me..."
        $ player.add_preg_desire(5)
        pc "*Sigh*"
        $ player.pregnancy = 0
        pc "I had better get back to it."
        jump pub_waitress_work_cycleend
    else:
        show pub_serve_lap prep with dissolve
        show pub_serve_lap hump rub with dissolve
        $ player.face_orgasm()
        $ player.sex_cum(pubpatron, "pullout", pub_waitress)
        "I feel his cock throbbing between my ass cheeks and some of it squirting on me. Pulse after pulse lets me feel his warmth against my skin."
        pc "Ahhhh ♥"
        pc "Mmmm, you covered me in your sperm..."
        $ player.face_normal()
        patron "Haaaa. It was so nice and warm in there. Next time I will fill you up."
        pc "Mmm will you now?"
        return


label pub_waitress_work_cumevent_notwant:
    patron "Ahhhhh..."
    $ player.face_orgasm()
    $ player.sex_cum(pubpatron, "inside", pub_waitress)
    "I feel his cock throbbing inside me filling my wet pussy with his sperm. Pulse after pulse let's me know he is pumping me full of his life making seed."
    pc "Ahhhh ♥"
    $ player.face_normal()
    pc "Mmmm, you filled me up... I told you outside..."
    patron "Haaaa. It was so nice and warm in there. I wanted it to last as long as possible."
    pc "I could end up..."
    pc "Ugh."
    return

label pub_waitress_work_cumevent_poke:
    show pub_serve_lap prep with dissolve
    $ player.face_orgasm()
    $ player.sex_cum(pubpatron, "pullout", pub_waitress)
    "I feel his cock throbbing between my legs. Pulse after pulse lets me feel his warmth against my skin."
    pc "Ahhhh ♥"
    pc "Mmmm, you covered me in your sperm..."
    $ player.face_normal()
    patron "Haaaa. It was so nice and warm in there. Next time I will fill you up."
    pc "Mmm will you now?"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
