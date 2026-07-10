label anabel_gift_picker:
    show anabel happy at right1 with dissolve
    $ temp_var_1 = True
    anabel.name "Hmm, you are giving me something?"
    call screen inventory_gift_choice([item_beer, item_map_pill, item_abort_pill, item_joy, item_pepperspray])

    if buy_inv.qty(item_joy) or buy_inv.qty(item_beer):
        anabel.name "No thanks [name]. I don't really want anything like that."
        $ temp_var_1 = False

    elif buy_inv.qty(item_map_pill):
        if anabel.is_pregnant:
            $ temp_var_1 = False
            anabel.name "Ugh, thanks [name], but not much I can do with that now."
            if not anabel.showing:
                pc "Oh? I didn't know. You don't look it."
                anabel.name "..."
        elif anabel.inv.qty(item_map_pill) >= 1:
            anabel.name "I have one already [name]. I don't have much need for more."
            $ temp_var_1 = False
        else:
            anabel.name "Oooh, thanks [name]. Doubt I will need it but can't be too careful."
    elif buy_inv.qty(item_abort_pill):
        if anabel.is_pregnant and anabel.pregnant_who.abort:
            anabel.name "Oh Christ! Thanks, I really need this."
            if anabel.showing:
                pc "Yeah, seeing the belly I thought I would offer."
            else:
                pc "Oh? I didn't know. Just thought it might come in handy."
        elif anabel.is_pregnant:
            anabel.name "Thanks... But I don't think I will use it."
            pc "Oh? Okay then."
            $ temp_var_1 = False
        elif anabel.inv.qty(item_map_pill) >= 1:
            anabel.name "I have one already, so I think you should keep hold of that one."
            $ temp_var_1 = False
        else:
            anabel.name "Ah thanks [name]. I don't think I will need it, but can't be too careful these days."
    elif buy_inv.qty(item_pepperspray):
        if anabel.inv.qty(item_pepperspray):
            anabel.name "I already have one of those [name]. Better give to someone who needs it."
        else:
            anabel.name "Ah shit. This stuff is expensive. You just giving it to me? Thanks!"
    else:
        show anabel neutral
        anabel.name "Ah, okay then..."
    if temp_var_1:
        $ anabel._love += (inv_value(buy_inv) / 4)
        $ inv_transfer(buy_inv, anabel.inv)
    else:
        $ inv_transfer(buy_inv, inv)
    show anabel neutral
    jump anabel_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
