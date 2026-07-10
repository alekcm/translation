label random_event_generic_allure:
    jump expression WeightedChoice([
    ("random_event_generic_allure_1", If(loc_cur.population >= 2, 100, 0)),
    ("random_event_generic_allure_2", If(player.has_perk(perk_slutty) and loc_cur.population >= 2, 50, 0)),
    ("random_event_generic_allure_3", 20),
    
    ])

label random_event_generic_allure_1:
    man "Damn girl, looking good!"
    $ player.face_shy()
    jump travel

label random_event_generic_allure_2:
    man "Ohh girl. Looking nice!"
    $ player.face_shy()
    man "How about we go somewhere and get to know each other some more?"
    if player.check_sex_agree_choice(diff=4,option1="Get to know him more" ,option2="No thanks"):
        pc "Sure, I wouldn't mind that."
        man "Really? Wow."
        $ tempname = streetguy
        $ quest_temp = None
        $ event_end_interrupt_label = "random_event_generic_allure_2_goodbye"
        jump whore_sex
    else:
        pc "No thanks."
        "I walk away without looking back."
    jump travel

label random_event_generic_allure_2_goodbye:
    man "Well, that was the best way to get to know a girl like you."
    pc "Sure it was."
    $ renpy.scene()
    with dissolve
    pc "Thanks for the fun."
    man "Anytime."
    $ pc_dress_slow()
    $ walk(loc_from)
    pcm "Hehe."
    jump travel

label random_event_generic_allure_3:
    pcm "I feel kinda sexy dressed like this."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
