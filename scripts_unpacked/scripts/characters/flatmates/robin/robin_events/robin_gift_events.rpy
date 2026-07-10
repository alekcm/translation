label robin_gift_picker:
    if t.hour in irange(0,5) or (t.time_from_to(23.30, 00.00) and loc(loc_common)):
        pcm "It can wait until she is awake."
        jump travel
    if oskar_here():
        pcm "Unless I am going to give [oskar.name] some Lebo, I think it can wait."
        jump travel
    show robin happy at right1 with dissolve
    $ temp_var_1 = True
    robin.name "Oooh, got something nice?"
    call screen inventory_gift_choice()
    if buy_inv.qty(item_joy):
        if robin.inv.qty(item_joy) >= 3:
            robin.name "I think I have enough of these [name]. You are better keeping them."
            $ temp_var_1 = False
        else:
            robin.name "Oooh, that will keep me happy when things go to shit. Thanks [name]!"
    elif buy_inv.qty(item_beer):
        if robin.inv.qty(item_beer) >= 3:
            robin.name "I think I have enough of these [name]. You are better keeping them."
            $ temp_var_1 = False
        else:
            robin.name "Oooh, that will keep me happy when things go to shit. Thanks [name]!"
    elif buy_inv.qty(item_map_pill):
        if robin.is_pregnant:
            $ temp_var_1 = False
            robin.name "Err... I think it's a bit late for me to be accepting those."
            if not robin.showing:
                pc "Oh? I didn't know. You don't look it."
                robin.name "Well, soon I guess..."
        elif robin.inv.qty(item_map_pill) >= 3:
            robin.name "I think I have enough of these [name]. You are better keeping them."
            $ temp_var_1 = False
        else:
            robin.name "Oooh, these are expensive. It will help me if I get a bit carried away."
    elif buy_inv.qty(item_abort_pill):
        if robin.is_pregnant and robin.pregnant_who.abort:
            robin.name "Thanks, you don't know how handy this will come in."
            if robin.showing:
                pc "Yeah, seeing the belly I thought I would offer."
        elif robin.is_pregnant:
            if any(x == robin.pregnant_who for x in [drake, nate, dan]):
                robin.name "Not sure I want to use this when it's [robin.pregnant_who.name]'s baby inside me. Thanks anyway though."
            else:
                robin.name "Thanks... But I don't think I want to use it. Think I will be seeing this one though."
                pc "Oh? Okay then."
                $ temp_var_1 = False
        elif robin.inv.qty(item_map_pill) >= 2:
            robin.name "I already have some of those stashed away so probably better you keep hold of it."
            $ temp_var_1 = False
        else:
            robin.name "Oooh, these are expensive. It will help me if I get a bit carried away."
    elif buy_inv.qty(item_pepperspray):
        if robin.inv.qty(item_pepperspray):
            robin.name "I already have one of those [name]. Better give to someone who needs it."
        else:
            robin.name "Ah shit. This stuff is expensive. You just giving it to me? Thanks!"
    else:
        show robin neutral
        robin.name "Ah, getting my hopes up?"
    if temp_var_1:
        $ robin._love += (inv_value(buy_inv) / 4)
        $ inv_transfer(buy_inv, robin.inv)
    else:
        $ inv_transfer(buy_inv, inv)
    show robin neutral
    jump robin_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
