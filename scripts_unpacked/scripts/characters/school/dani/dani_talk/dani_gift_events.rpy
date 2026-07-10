label dani_gift_picker:
    if loc(loc_bedroom_dani):
        show dani happy at right5 with dissolve
    else:
        show dani happy at right1 with dissolve
    $ temp_var_1 = True
    dani.name "Huh, giving me something?"
    call screen inventory_gift_choice([item_beer, item_map_pill, item_abort_pill, item_joy, item_pepperspray, item_winebottle])
    if buy_inv.qty(item_winebottle):
        if not log.interactive("quest_daniwine_02"):
            dani.name "Ah you have wine? But maybe another time."
            $ inv_transfer(buy_inv, inv)
        elif not (loc(loc_bedroom_dani) and t.hour in (19,20,21,22,23,0,1)):
            dani.name "Ah you got some wine? Bring it in the evening then and we can drink it."
            $ inv_transfer(buy_inv, inv)
        else:
            if not "dani_drinking_wine_counter" in dani.dict:
                $ dani.dict["dani_drinking_wine_counter"] = 0
            jump dani_drinkwine_subject
    elif buy_inv.qty(item_joy):
        if dani.inv.qty(item_joy) >= 3:
            dani.name "I think I have enough of these [name]. You are better keeping them."
            $ temp_var_1 = False
        else:
            dani.name "Oooh, that will keep me happy when things go to shit. Thanks [name]!"
    elif buy_inv.qty(item_beer):
        if dani.inv.qty(item_beer) >= 3:
            dani.name "I think I have enough of these [name]. You are better keeping them."
            $ temp_var_1 = False
        else:
            dani.name "Oooh, that will keep me happy when things go to shit. Thanks [name]!"
    elif buy_inv.qty(item_map_pill):
        if dani.is_pregnant:
            $ temp_var_1 = False
            dani.name "Err... I think it's a bit late for me to be accepting those."
            if not dani.showing:
                pc "Oh? I didn't know. You don't look it."
                dani.name "Well, soon I guess..."
        elif dani.inv.qty(item_map_pill) >= 3:
            dani.name "I think I have enough of these [name]. You are better keeping them."
            $ temp_var_1 = False
        else:
            dani.name "Oooh, these are expensive. It will help me if something happens."
    elif buy_inv.qty(item_abort_pill):
        if dani.is_pregnant and dani.pregnant_who.abort:
            dani.name "Thanks, you don't know how handy this will come in."
            if dani.showing:
                pc "Yeah, seeing the belly I thought I would offer."
        elif dani.is_pregnant:
            dani.name "Thanks... But I don't think I want to use it. Think I will be seeing this one though."
            pc "Oh? Okay then."
            $ temp_var_1 = False
        elif dani.inv.qty(item_map_pill) >= 2:
            dani.name "I already have some of those stashed away so probably better you keep hold of it."
            $ temp_var_1 = False
        else:
            dani.name "Oooh, these are expensive. It will help me if I get a bit carried away."
    elif buy_inv.qty(item_pepperspray):
        if dani.inv.qty(item_pepperspray):
            dani.name "I already have one of those [name]. Better give to someone who needs it."
        else:
            dani.name "Ah shit. This stuff is expensive. You just giving it to me? Thanks!"
    else:
        show dani neutral
        dani.name "Ah, getting my hopes up?"
    if temp_var_1:
        $ dani._love += (inv_value(buy_inv) / 4)
        $ dani_yan_remove(numgen(1,4))
        $ inv_transfer(buy_inv, dani.inv)
    else:
        $ inv_transfer(buy_inv, inv)
    show dani neutral
    jump dani_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
