label random_event_generic_addict_joy:
    jump expression WeightedChoice([
    ("random_event_generic_addict_joy_1", If(inv.qty(item_joy), 100, 0)),
    ("random_event_generic_addict_joy_2", If(not inv.qty(item_joy), 100, 0)),
    ("random_event_generic_addict_joy_3", If(not inv.qty(item_joy), 100, 0)),
    ])

label random_event_generic_addict_joy_1:
    call item_joy_action from _call_item_joy_action_2
    jump travel

label random_event_generic_addict_joy_2:
    pcm "I want some Joy!"
    $ player.add_mood(-10)
    pc "UGH!"
    jump travel

label random_event_generic_addict_joy_3:
    $ player.face_worried()
    "I look around in my purse hoping to find some Joy."
    $ player.face_angry()
    pc "FUCK!"
    $ player.add_mood(-10)
    if inv.qty(item_beer):
        pcm "This will have to do."
        call item_beer_action from _call_item_beer_action_1
    elif inv.qty(item_wakeup):
        pcm "This will have to do."
        call item_wakeup_action from _call_item_wakeup_action_3
    elif inv.qty(item_lebo):
        pcm "Fuck it, I'll take this and fuck someone happy."
        call item_lebo_action from _call_item_lebo_action
    else:
        pc "Piece of shit!"
    jump travel

label random_event_generic_addict_alcohol:
    jump expression WeightedChoice([
    ("random_event_generic_addict_alcohol_1", If(inv.qty(item_beer) or inv.qty(item_brew), 100, 0)),
    ("random_event_generic_addict_alcohol_2", If(not (inv.qty(item_beer) or inv.qty(item_brew)), 100, 0)),
    ("random_event_generic_addict_alcohol_3", If(not (inv.qty(item_beer) or inv.qty(item_brew)), 100, 0)),
    ])

label random_event_generic_addict_alcohol_1:
    if inv.qty(item_beer):
        call item_beer_action from _call_item_beer_action_2
    elif inv.qty(item_brew):
        call item_brew_action from _call_item_brew_action
    jump travel

label random_event_generic_addict_alcohol_2:
    pcm "I want something to drink!"
    $ player.add_mood(-10)
    pc "UGH!"
    jump travel

label random_event_generic_addict_alcohol_3:
    $ player.face_worried()
    "I look around in my purse hoping to find something to drink."
    $ player.face_angry()
    pc "FUCK!"
    $ player.add_mood(-10)
    if inv.qty(item_joy):
        pcm "This will have to do."
        call item_joy_action from _call_item_joy_action_3
    elif inv.qty(item_wakeup):
        pcm "This will have to do."
        call item_wakeup_action from _call_item_wakeup_action_4
    elif inv.qty(item_lebo):
        pcm "Fuck it, I'll take this and fuck someone happy."
        call item_lebo_action from _call_item_lebo_action_1
    else:
        pc "Piece of shit!"
    jump travel

label random_event_generic_addict_cigs:

    jump expression WeightedChoice([
    ("random_event_generic_addict_cigs_1", If(inv.qty(item_cigs), 100, 0)),
    ("random_event_generic_addict_cigs_2", If(not inv.qty(item_cigs), 100, 0)),
    ])

label random_event_generic_addict_cigs_1:
    $ item_inv_call = True
    jump item_cigs_action

label random_event_generic_addict_cigs_2:
    pcm "I really want a smoke."
    $ player.add_mood(-3)
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
