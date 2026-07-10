label random_event_generic_badchoices:
    if player.has_perk(perk_deadinside):
        $ show_notif_popup("I want to feel alive!")
    else:
        $ show_notif_popup("Making stupid choices")
    jump expression WeightedChoice([
    ("random_event_generic_badchoices_1", If(inv.qty(item_lebo), 100, 0)),
    ("random_event_generic_badchoices_2", 100),
    ("random_event_generic_badchoices_3", If (inv.qty(item_sucu_pill), 100, 0)),
    ("random_event_generic_badchoices_4", If (inv.qty(item_ballgag_locked) and not player.gagged, 100, 0)),
    ("random_event_generic_badchoices_5", If (inv.qty(item_milktab) and not player.lactating, 100, 0)),
    ("random_event_generic_badchoices_6", If (inv.qty(item_blindfold) and not player.blind, 100, 0)),
    ("random_event_generic_badchoices_7", 20),
    ("random_event_generic_badchoices_8", If(inv.qty(item_perm_marker) or inv.qty(item_felt_marker), 100, 0)),

    ("random_event_generic_addict_alcohol_1", If(inv.qty(item_beer) or inv.qty(item_brew), 100, 0)),
    ("random_event_generic_addict_cigs_1", If(inv.qty(item_cigs), 100, 0)),
    ("random_event_generic_addict_joy_1", If(inv.qty(item_joy), 100, 0)),
    
    ])

label random_event_generic_badchoices_1:
    pcm "Hmmmm..."
    call item_lebo_action from _call_item_lebo_action_2
    jump travel

label random_event_generic_badchoices_2:
    pcm "A bit of fun?"
    pcm "Yeah..."
    $ pc_strip_random()
    jump travel

label random_event_generic_badchoices_3:
    call item_sucu_pill_action from _call_item_sucu_pill_action
    jump travel

label random_event_generic_badchoices_4:
    pcm "Hmm, might be fun..."
    call item_ballgag_locked_action from _call_item_ballgag_locked_action
    jump travel

label random_event_generic_badchoices_5:
    pcm "Wonder what its like to be milky?"
    call item_milktab_action from _call_item_milktab_action
    jump travel

label random_event_generic_badchoices_6:
    pcm "Heh."
    call item_blindfold_action from _call_item_blindfold_action
    jump travel

label random_event_generic_badchoices_7:
    jump random_event_generic_desirenocontrol

label random_event_generic_badchoices_8:
    pcm "Okay... Let's see..."
    if inv.qty(item_perm_marker):
        $ writing.add_writing_random("perm")
    else:
        $ writing.add_writing_random("temp")
    pcm "There we go."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
