label action_flyer_event_motel_1:
    "Man" "What's a pink room?"
    pc "Rooms with a naked girl inside. Buy tickets and do what you want with her."
    "Man" "Thanks."
    pc "[rlist.flyering_area_dialogue]"
    jump action_flyer_event_picker

label action_flyer_event_motel_2:
    $ player.grope()
    "Man" "You workin' the pink rooms [rlist.name_cute]?"
    pc "No, I'm just doing the flyering. Take this with you for a discount."
    "Man" "Cheers [rlist.name_deg]."
    $ player.grope_end()
    $ player.spank()
    pc "[rlist.flyering_area_dialogue]"
    jump action_flyer_event_picker

label action_flyer_event_motel_3:
    $ player.grope_breasts()
    "Man" "How much to buy these [rlist.name_cute]?"
    pc "I'm handing out fliers here. Not whoring."
    "Man" "And? What's your price?"
    if player.check_whore_agree_choice("Hmm, how about...", "No thanks"):
        $ player.set_whore_price(3)
        pc "£[player.soldprice] for some fun?"
        "Man" "Sounds good to me."
        $ player.grope_end()
        $ player.left_hand = ""
        $ male_npc_create()
        $ tempname = punter
        $ quest_temp = quest_flyers
        jump whore_street_customer_pick_location_tombola

    pc "I just hand out the fliers. Take this for a discount."
    "Man" "Okay, cheers [rlist.name_deg]."
    $ player.grope_end()
    $ player.spank()
    pc "[rlist.flyering_area_dialogue]"
    jump action_flyer_event_picker

label action_flyer_event_motel_4:
    "Man" "The motel provide whores?"
    pc "Sort of, plenty of whores outside the motel waiting for customers."
    "Man" "Cheers [rlist.name_deg]."
    pc "[rlist.flyering_area_dialogue]"
    jump action_flyer_event_picker

label action_flyer_event_motel_5:
    "Man" "How about you keep me warm in one of your beds [rlist.name_deg]?"
    pc "Plenty of girls outside the rooms willing to warm you up."
    if not numgen(0,10) and player.allure > 300:
        $ player.grope_breasts()
        "Man" "Asking for you to keep me company, not some random whore."
        pc "What's the difference? I'm just here handing out flyers."
        $ player.grope()
        "Man" "Rather a young thin like you over those used up whores."
        pc "Ugh..."
        if player.check_whore_agree_choice("Hmm, how about...", "No thanks"):
            $ player.set_whore_price(3)
            pc "£[player.soldprice] for some fun?"
            "Man" "Sounds good to me."
            $ player.grope_end()
            $ player.left_hand = ""
            $ male_npc_create()
            $ tempname = punter
            $ quest_temp = quest_flyers
            jump whore_street_customer_pick_location_tombola

        pc "I just hand out the fliers. Take this for a discount."
        $ player.grope_end()
        $ player.spank()

    "Man" "Alright, thanks [rlist.name_deg]."
    pc "[rlist.flyering_area_dialogue]"
    jump action_flyer_event_picker

label action_flyer_event_motel_6:
    $ player.grope()
    "Man" "Bet we're gonna see you posing in a pink room one day."
    pc "Well, take a flier and I'll give a discount if you see me there."
    "Man" "Heh, [rlist.name_sexy]."
    $ player.grope_end()
    pc "[rlist.flyering_area_dialogue]"
    jump action_flyer_event_picker

label action_flyer_event_motel_7:
    "Man" "How's the pink rooms work [rlist.name_sexy]?"
    pc "Window looking into the girls room, see someone you like you go knock on the door."
    "Man" "Right, thanks."
    pc "[rlist.flyering_area_dialogue]"
    jump action_flyer_event_picker

label action_flyer_event_motel_8:
    "Man" "Hey [rlist.name_deg], Where do I get tickets for the whores in the room?"
    pc "Girl at reception sells them, take a flier for a discount."
    "Man" "Right, thanks."
    pc "[rlist.flyering_area_dialogue]"
    jump action_flyer_event_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
