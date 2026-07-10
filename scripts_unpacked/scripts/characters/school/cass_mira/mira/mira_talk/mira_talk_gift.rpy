
label mira_gift_picker:
    show mira at right1 with dissolve
    $ temp_var_1 = True
    mira.name "Have something for me?"

    $ temp_var_1 = [item_beer, item_map_pill, item_abort_pill, item_joy]
    if "pc_knows_whore" in mira.list and (not cass_here() or (cass_here() and cass.iswhore)):
        $ add_to_list(temp_var_1, [item_lebo, item_wakeup, item_pepperspray])
    call screen inventory_gift_choice(temp_var_1)

    $ temp_var_1 = True

    if buy_inv.qty(item_beer):
        if mira.inv.qty(item_beer) >= 3:
            mira.name "Think I am okay on the beer [name]."
            $ temp_var_1 = False
        else:
            mira.name "Thanks [name]!"

    elif buy_inv.qty(item_map_pill):
        if mira.is_pregnant:
            $ temp_var_1 = False
            mira.name "I think it's a bit late for these [name]."
            if not mira.showing:
                pc "Oh? I didn't know. You don't look it."
                mira.name "..."
        elif mira.inv.qty(item_map_pill) >= 5:
            if "pc_knows_whore" in mira.list:
                mira.name "I managed to keep a few I got from the whores, so I think I am okay for now."
            else:
                mira.name "I think I have enough of these [name]. You are better keeping them."
            $ temp_var_1 = False
        else:
            if "pc_knows_whore" in mira.list:
                mira.name "These really come in handy when working the highway. Thanks [name]."
            else:
                mira.name "Thanks [name]. These are hard to come by"

    elif buy_inv.qty(item_abort_pill):
        if mira.is_pregnant and mira.pregnant_who.abort:
            mira.name "Oh thank you [name]!"
            if mira.showing:
                pc "Yeah, seeing the belly I thought I would offer."
        elif mira.is_pregnant:
            mira.name "Thanks [name]. But I think I will keep this one"
            pc "Oh? Really? Okay then."
            $ temp_var_1 = False
        elif mira.inv.qty(item_map_pill) >= 2:
            mira.name "I already have some of these [name]. I think you should keep them."
            $ temp_var_1 = False
        else:
            if "pc_knows_whore" in mira.list:
                mira.name "These really come in handy when working the highway. Thanks [name]."
            else:
                mira.name "Thanks [name]. These are hard to come by"

    elif buy_inv.qty(item_joy):
        if mira.inv.qty(item_joy) >= 3:
            mira.name "I think I have enough of these [name]. You are better keeping them."
            $ temp_var_1 = False
        else:
            mira.name "Oooh, that will keep me happy when things go to shit. Thanks [name]!"

    elif buy_inv.qty(item_lebo):
        if mira.inv.qty(item_lebo) >= 3:
            mira.name "I think I have enough of these [name]. You are better keeping them."
            $ temp_var_1 = False
        else:
            pc "This might make hanging around the highway easier for you."
            mira.name "It does... Thanks [name]."

    elif buy_inv.qty(item_wakeup):
        if mira.inv.qty(item_wakeup) >= 3:
            mira.name "I think I have enough of these [name]. You are better keeping them."
            $ temp_var_1 = False
        else:
            pc "This might make hanging around the highway easier for you."
            mira.name "It does... Thanks [name]."

    elif buy_inv.qty(item_pepperspray):
        if mira.inv.qty(item_pepperspray):
            mira.name "I already have one of these [name]. Better give to someone else to keep them safe."
        else:
            mira.name "Oh wow. Thanks [name]. This will keep the cunts at bay."
            pc "Yeah, was thinking the same."
    else:

        show mira worried
        mira.name "Ah... Okay."
    if temp_var_1:
        $ mira._love += (inv_value(buy_inv) / 4)
        $ inv_transfer(buy_inv, mira.inv)
    else:
        $ inv_transfer(buy_inv, inv)

    show mira happy
    jump mira_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
