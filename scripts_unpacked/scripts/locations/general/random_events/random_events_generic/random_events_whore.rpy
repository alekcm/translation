label random_event_generic_whore_approach_normal:
    $ male_npc_create_all()
    $ tempname = streetguy
    $ quest_temp = None
    jump random_event_generic_whore_approach

label random_event_generic_whore_approach_start_scav:
    $ male_npc_create_all(scav=True)
    $ tempname = scavver
    $ quest_temp = None
    jump random_event_generic_whore_approach

label random_event_generic_whore_approach:
    show male_generic at right5 with dissolve
    tempname.name "Hey darling, you on the job?"
    if player.has_perk(perk_freeuse):
        pc "No, but I mess around for free. Want some fun?"
        tempname.name "Err, of course."
        jump whore_street_customer_pick_location_tombola
    $ player.set_whore_price(1)
    tempname.name "How does £[player.soldprice] sound?"
    if player.check_whore():
        menu:
            "Sounds good":
                if whore_experiance_weight():
                    call whore_street_customer_whatsex from _call_whore_street_customer_whatsex_1
                jump whore_street_customer_pick_location_tombola
            "Not right now":
                pc "Sorry mate, not working right now."
                tempname.name "That's a pity."
                hide male_generic with dissolve
                jump travel
    else:

        $ player.face_annoyed()
        pc "I'm not a whore, go somewhere else."
        if not numgen(0,10):
            tempname.name "Well, you look like a whore."
            pc "And yet I am not."
        hide male_generic with dissolve
        "I walk away from the guy."
        jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
