label dance_party_drink_topup:
    if not loc(loc_party_kitchen):
        pcm "I should probably pick up some more wine from the kitchen."
        $ walk(loc_party_kitchen)
    else:
        pcm "I should top up my wine."
    $ dance_party_get_wine()
    pcm "There we go."
    jump travel

label dance_party_drink_drink:
    $ dialouge = renpy.random.choice([
    "Hmm, guess no one is stopping me from having some myself...",
    "Well, it is free.",
    "Bottoms up!",
    "Why not?",
    "Free booze is the best kind of booze."
    ])
    pcm "[dialouge]"
    $ dance_party_serve_wine(drink=True)
    jump travel

label dance_party_first_event_anabel_harm_picker:
    if not renpy.showing("anabel"):
        show anabel at right1 with dissolve
    jump expression WeightedChoice([
    
    ("dance_party_first_event_anabel_harm_1", 100),
    ("dance_party_first_event_anabel_harm_2", 100),
    ("dance_party_first_event_anabel_harm_3", 100),
    ("dance_party_first_event_anabel_harm_4", If(inv.qty(item_lebo) or inv.qty(item_joy), 100, 0)),

    ])

label dance_party_first_event_anabel_harm_1:
    pc "Hey, how are you keeping?"
    anabel.name "Err, having to deal with these guys..."
    pc "Hmmm, have some wine with me, they will be easier to deal with."
    anabel.name "Err..."
    $ anabel.drink()
    $ dance_party_serve_wine(drink=True)
    jump random_event_picker_dance_party_talk_anabel_end

label dance_party_first_event_anabel_harm_2:
    pc "Hmm, glad the wine is free. Helps with all of this."
    anabel.name "Err..."
    pc "C'mon, drink with me."
    anabel.name "Okay..."
    $ anabel.drink()
    $ dance_party_serve_wine(drink=True)
    jump random_event_picker_dance_party_talk_anabel_end

label dance_party_first_event_anabel_harm_3:
    pc "Keep your belly warm."
    anabel.name "Huh?"
    pc "With the wine. Makes this whole thing easier."
    anabel.name "Okay..."
    $ anabel.drink()
    $ dance_party_serve_wine(drink=True)
    jump random_event_picker_dance_party_talk_anabel_end

label dance_party_first_event_anabel_harm_4:
    if inv.qty(item_lebo):
        pcm "Hmm, should I sneak some Lebo in her drnik?"
    else:
        pcm "Hmm, should I sneak some Joy into her drink?"
    menu:
        "Yes, give it to her":
            if inv.qty(item_lebo):
                pc "Have some fun [anabel.name]."
                anabel.name "Huh?"
                pc "Have a drink with me."
                anabel.name "Errr... Okay."
                $ anabel.drink_max()
                $ dance_party_serve_wine(drink=True)
                $ inv.drop(item_lebo)
                $ show_notif_popup("Shared a Lebo")
                $ player.add_perk(perk_lebo, hours=4)
                $ player.add_desire(1000)
            else:
                pc "Have some fun [anabel.name]."
                anabel.name "Huh?"
                pc "Have a drink with me."
                anabel.name "Errr... Okay."
                $ anabel.drink_max()
                $ dance_party_serve_wine(drink=True)
                $ inv.drop(item_joy)
                $ show_notif_popup("Shared a Joy")
                $ player.add_perk(perk_joy, hours=4)
                $ player.add_mood(200)
            anabel.name "Err, these drinks..."
            pc "Nice stuff right?"
            anabel.name "They seem a bit..."
            pcm "This should set her up for the rest of the night."
        "No, better not":

            pc "Have some fun [anabel.name]."
            anabel.name "Huh?"
            pc "Have a drink with me."
            anabel.name "Errr... Okay."
            $ anabel.drink()
            $ dance_party_serve_wine(drink=True)
    jump random_event_picker_dance_party_talk_anabel_end

label dance_party_first_event_anabel_help_picker:
    if not renpy.showing("anabel"):
        show anabel at right1 with dissolve
    jump expression WeightedChoice([
    
    ("dance_party_first_event_anabel_help_1", 100),
    ("dance_party_first_event_anabel_help_2", 100),
    ("dance_party_first_event_anabel_help_3", 100),

    ])

label dance_party_first_event_anabel_help_1:
    pc "Should have a bit of water while you can, helps calm down the booze."
    anabel.name "Yeah, I think I will."
    $ anabel.undrink(numgen(2,7))
    jump random_event_picker_dance_party_talk_anabel_end

label dance_party_first_event_anabel_help_2:
    pc "Be careful what you drink around here. Don't want to end up piss drunk."
    anabel.name "Yeah, these guys keep pushing me to share their drinks."
    pc "Yeah, just small sips to keep them happy."
    $ anabel.undrink(numgen(2,7))
    jump random_event_picker_dance_party_talk_anabel_end

label dance_party_first_event_anabel_help_3:
    pc "Too much to drink around this lot and you might end up in trouble."
    anabel.name "The other girls seem to be doing okay with it."
    pc "Yeah, but I don't think they much mind the trouble it might bring."
    $ anabel.undrink(numgen(2,7))
    jump random_event_picker_dance_party_talk_anabel_end

label dance_party_ending_goodbye:
    if quest_dancevip.dict["first_party"]:
        jump dance_party_ending_goodbye_first

    jump expression WeightedChoice([
    
    ("dance_party_ending_goodbye_svet", If(svet_here(), 1, 0)),
    ("dance_party_ending_goodbye_dani", If(dani_here(), 1, 0)),
    ("dance_party_ending_goodbye_anabel", If(anabel_here(), 1, 0)),
    ("dance_party_ending_goodbye_rachel", If(rachel_here(), 1, 0)),
    ])

label dance_party_ending_goodbye_svet:
    show svet at right1 with dissolve
    svet.name "Good job [name]. Get home safe."
    if any([dani_here(), rachel_here(), anabel_here()]):
        pc "You too. Goodnight everyone."
    else:
        pc "You too. Don't stay out here too long on your own."
    hide svet wth dissolve
    jump travel

label dance_party_ending_goodbye_dani:
    show dani at right1 with dissolve
    dani.name "Got out safe?"
    pc "Yeah, going to head home now."
    dani.name "Goodnight [name]."
    hide dani with dissolve
    jump travel

label dance_party_ending_goodbye_anabel:
    show anabel at right1 with dissolve
    anabel.name "Phew. That was difficult."
    pc "Yeah, careful heading home after these perverts plied you with booze."
    anabel.name "You too [name]."
    hide anabel with dissolve
    jump travel

label dance_party_ending_goodbye_rachel:
    show rachel at right1 with dissolve
    pc "Surprised you didn't stay the night here."
    rachel.name "Maybe I should."
    pc "Heh, goodnight [rachel.name]."
    hide rachel with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
