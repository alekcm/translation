label random_event_generic_give_something_picker(force=False):
    if numgen(0,10) and not force:
        return
    tempname.name "Want something fun?"
    if player.check_nowill(block_face=True, drink_related=True):
        pc "Umm, what is it?"
        tempname.name "Here."
    elif player.check_int():
        pcm "I probably shouldn't be taking things of strange guys..."
        pc "Err, no thanks. I am good."
        tempname.name "Suit yourself."
        return
    else:
        pc "Errm, okay..."
    call expression WeightedChoice([
    ("random_event_generic_give_booze", If(not player.drinking, 100, 0)),
    ("random_event_generic_give_brew", If(not player.drinking, 100, 0)),
    ("random_event_generic_give_joy", 20),
    ("random_event_generic_give_lebo", 20),
    ]) from _call_expression_30
    return

label random_event_generic_give_booze:
    "He opens a bottle of beer and hands it to me."
    $ player.add_perk(perk_drinking_beerbottle_2, mins=10)
    pc "Thanks."
    $ player.drink()
    return

label random_event_generic_give_brew:
    "He opens a bottle of brew and hands it to me."
    $ player.add_perk(perk_drinking_brew_1, mins=10)
    pc "Thanks."
    $ player.drink(amount=40, spiked=True)
    return

label random_event_generic_give_joy:
    "He hands me something to pop in my mouth."
    $ player.add_perk(perk_joy, hours=4)
    $ player.add_mood(200)
    pc "Thanks."
    return

label random_event_generic_give_lebo:
    "He hands me something to pop in my mouth."
    $ player.add_perk(perk_lebo, hours=4)
    $ player.add_desire(1000)
    pc "Thanks."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
