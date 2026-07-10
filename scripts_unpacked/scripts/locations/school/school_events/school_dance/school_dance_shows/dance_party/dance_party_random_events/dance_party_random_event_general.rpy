label random_event_picker_dance_party_general_dance_recall:
    $ dance_make_girls_dance()
    show svet at right1 with dissolve
    svet.name "[name]. Time for a dance."
    pc "Okay."
    hide svet with dissolve

    $ walk(loc_party_stage)
    if quest_dancevip.dict["wine_amount"]:
        $ dance_party_empty_wine()
        "I put my wine down and head up to the stage with the rest of the girls."
    else:

        "I head up to the stage with the rest of the girls."

    $ show_dance_pole_image()
    call random_event_picker_dance_party_general_dance_npc_picker from _call_random_event_picker_dance_party_general_dance_npc_picker
    $ exercise(10)
    $ show_dance_pole_image()
    call random_event_picker_dance_party_general_dance_npc_picker from _call_random_event_picker_dance_party_general_dance_npc_picker_1
    $ exercise(10)
    $ show_dance_pole_image()
    "The show starts to come to and end and we all rest for a bit."
    $ renpy.scene()
    with dissolve
    $ dance_stop_girls_dance()
    jump travel


label random_event_picker_dance_party_general_1:
    pc "[rlist.dance_party_wine_offer]"
    pcm "Hmm, no one?"
    pcm "Okay."
    jump travel

label random_event_picker_dance_party_general_2:
    pc "[rlist.dance_party_wine_offer]"
    $ player.grope()
    pc "Ah!"
    $ player.grope_end()
    pc "..."
    jump travel

label random_event_picker_dance_party_general_3:
    pc "[rlist.dance_party_wine_offer]"
    partyman.name "[rlist.dance_party_wine_offer_accept]"
    pc "Here you go."
    $ dance_party_serve_wine()
    partyman.name "Cheers."
    jump travel

label random_event_picker_dance_party_general_4:
    pc "[rlist.dance_party_wine_offer]"
    partyman.name "[rlist.dance_party_wine_offer_accept]"
    pc "Here you go."
    partyman.name "Share some with me [rlist.name_cute]."
    if player.check_nowill(drink_related=True):
        pc "Errr, okay..."
        $ dance_party_serve_wine(drink=True)
    else:
        pc "Too much and I won't be able to serve you. Enjoy your drink."
        if not numgen(0,5):
            partyman.name "C'mon [rlist.name_cute], it's a party. Here, take it."
            pc "Ugh... Fine."
            $ dance_party_serve_wine(drink=True)
    $ dance_party_serve_wine()
    partyman.name "Cheers."
    jump travel

label random_event_picker_dance_party_general_5:
    pc "[rlist.dance_party_wine_offer]"
    partyman.name "[rlist.dance_party_wine_offer_accept]"
    pc "Here you go."
    partyman.name "Share some with me [rlist.name_cute]."
    if player.check_nowill(drink_related=True):
        pc "Errr, okay..."
        $ dance_party_serve_wine(drink=True)
    else:
        pc "Too much and I won't be able to serve you. Enjoy your drink."
        if not numgen(0,5):
            partyman.name "C'mon [rlist.name_cute], it's a party. Here, take it."
            pc "Ugh... Fine."
            $ dance_party_serve_wine(drink=True)
    $ dance_party_serve_wine()
    partyman.name "Cheers."
    jump travel

label random_event_picker_dance_party_general_6:
    pc "[rlist.dance_party_wine_offer]"
    partyman.name "[rlist.dance_party_wine_offer_accept]"
    pc "Here you go."
    $ player.grope(steal=True)
    pc "Ah!"
    jump travel


label random_event_picker_dance_party_takeclothes_1:
    pc "[rlist.dance_party_wine_offer]"
    $ player.grope_breasts()
    partyman.name "Hey [rlist.name_cute], how about we liven up this party?"
    pc "Huh?"
    $ player.set_whore_price(0)
    partyman.name "£[player.soldprice] to get your tits out."
    if player.check_whore_agree_choice(request="strip"):
        pc "Okay..."
        $ c.top = 0
        partyman.name "[rlist.praise_good_upper]."
        $ player.add_money(player.soldprice)
        $ player.grope_breasts()
        pc "Ai!"
    else:
        pc "Err, sorry mate. That's a bit much."
        partyman.name "For now..."
        pc "Ask one of the the girls."
    $ player.grope_end()
    pcm "..."
    jump travel

label random_event_picker_dance_party_takeclothes_2:
    pc "[rlist.dance_party_wine_offer]"
    $ player.grope_hips()
    partyman.name "Hey [rlist.name_cute], how about we liven up this party?"
    pc "Huh?"
    $ player.set_whore_price(0)
    partyman.name "£[player.soldprice] to see what you got under here."
    if player.check_whore_agree_choice(request="strip"):
        pc "Okay..."
        $ c.bottom = 0
        $ c.pants = 0
        partyman.name "[rlist.praise_good_upper]."
        $ player.add_money(player.soldprice)
        $ player.grope_hips()
        pc "Ai!"
    else:
        pc "Err, sorry mate. That's a bit much."
        partyman.name "For now..."
        pc "Ask one of the the girls."
    $ player.grope_end()
    pcm "..."
    jump travel


label random_event_picker_dance_party_drink_1:
    pcm "Hmm, guess no one is stopping me from having some myself..."
    $ dance_party_serve_wine(drink=True)
    jump travel

label random_event_picker_dance_party_drink_2:
    pcm "Only thing to cheer me up in this place is this bottle."
    pcm "Well, why not?"
    $ dance_party_serve_wine(drink=True)
    jump travel


label random_event_picker_dance_party_grope_1:
    if quest_dancevip.dict["wine_amount"]:
        pc "[rlist.dance_party_wine_offer]"
    $ player.grope()
    pc "Ai!"
    partyman.name "Nice!"
    $ player.grope_end()
    jump travel

label random_event_picker_dance_party_grope_2:
    if quest_dancevip.dict["wine_amount"]:
        pc "[rlist.dance_party_wine_offer]"
    $ player.grope()
    pc "..."
    partyman.name "Nice!"
    $ player.grope()
    if quest_dancevip.dict["wine_amount"]:
        pc "Your going to make me spill my wine!"
    else:
        pc "C'mon, hands to yourself."
    $ player.grope_end()
    jump travel

label random_event_picker_dance_party_anabel_taken:
    $ male_npc_create_all()
    $ npc_race = 1
    show anabel at right1:
        xzoom -1
    show male_generic at right2:
        xzoom -1
    with dissolve
    pcm "Hmmm..."
    hide anabel
    hide male_generic
    with dissolve
    pcm "Looks like [anabel.name] is being taken off by some guy."
    $ anabel.have_sex(partyman, preg_force=True)
    $ add_to_list(anabel.list, "party_sex")
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
