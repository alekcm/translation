

label random_event_generic_exhib_general_1:
    man "Whoo! Nice one darling!"
    pcm "Fuck fuck!"
    $ travel_isolate()
    jump travel

label random_event_generic_exhib_general_2:
    man "You ok darling? I got something to wear if you want."
    pcm "Err..."
    man "Give you my t-shirt. Cover yourself up."
    if player.check_nowill():
        pcm "I can't keep going around like this..."
    else:
        menu:
            "Okay":
                $ NullAction()
            "No thanks":
                pc "I'm fine, thanks."
                pcm "Not heading off with you..."
                jump travel
    $ player.face_worried()
    pc "Err, thanks?"
    man "C'mon."
    $ travel_isolate()
    if not numgen(0, 5):
        "The man takes his top off and hands it to me. He has a vest on under so isn't totally exposed."
        $ wardrobe.take(item_coat_11, all_notif=True)
        $ player.face_happy()
        pc "Oh? Thanks!"
        $ c.coat = 11
        "He walks off without even looking back."
        pcm "Wow. Didn't expect that."
        jump travel
    else:
        "He takes his shirt off and carries on taking off his trousers."
        pc "Err, why are you taking those off?"
        man "Cos you gotta pay for the clothes."
        pc "Ugh..."
        jump random_event_generic_exhib_general_sex_for_clothes

label random_event_generic_exhib_general_sex_for_clothes:
    $ tempname = clothesman
    $ quest_temp = None

    if numgen(0, 2):
        man "Little blowjob is a good price me thinks."
        $ player.soldrequest = "blow"
    else:
        man "Bend over and you can walk away with my stuff after."
        $ player.soldrequest = "sex"
    pc "..."
    if player.check_sex_agree_choice(diff=2,option1="Agree to get clothes" ,option2="Leave naked"):
        pc "Okay..."
        $ event_end_interrupt_label = "random_event_generic_exhib_general_2_sex_end"
        jump whore_street_sex_start_picker
    else:
        pc "Sorry, no."
        if not numgen(0,8):
            $ player.grope()
            man "Hold on, where ya going?"
            pc "Get off!"
            man "I offered the nice way first. But you ain't leavin'!"
            pc "Ah!"
            jump whore_street_sex_start_picker
        $ walk(loc_from)
        pcm "Fuck. Still showing myself off..."
    jump travel

label random_event_generic_exhib_general_2_sex_end:
    man "Cheers love."
    $ renpy.scene()
    with dissolve
    pc "Clothes?"
    man "Sure, take what you want."
    pc "..."
    if not c.top:
        $ wardrobe.take(item_coat_11, all_notif=True, dress=True)
    if not c.bottom:
        $ wardrobe.take(item_bottom_26, all_notif=True, dress=True)
    pc "Thanks..."
    man "No worries love."
    $ walk(loc_from)
    pcm "Well, I am not showing off any more..."
    jump travel

label random_event_generic_exhib_general_3:
    pcm "Gotta get home! Gotta get home!"
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
