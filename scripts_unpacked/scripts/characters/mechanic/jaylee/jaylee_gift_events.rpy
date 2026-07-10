label jaylee_gift_picker:
    if t.hour in irange(1,6):
        pcm "It can wait until she is awake."
        jump travel
    show jaylee happy at right1 with dissolve
    $ temp_var_1 = True
    jaylee.name "Oooh, giving me something are ya?"
    call screen inventory_gift_choice()
    if buy_inv.qty(item_joy):
        if jaylee.inv.qty(item_joy) >= 3:
            jaylee.name "Don't think I have need of any more of these cutie."
            $ temp_var_1 = False
        else:
            jaylee.name "Oh? Trying to keep me happy eh? Thanks."
    elif buy_inv.qty(item_beer):
        jaylee.name "I thought being piss drunk was your thing? You keep em. If I drink round here I'll end up bent over a junkheap."
        $ temp_var_1 = False
    elif buy_inv.qty(item_map_pill):
        if jaylee.is_pregnant:
            $ temp_var_1 = False
            jaylee.name "Think those things were a bit late to the party."
            if not jaylee.showing:
                pc "Oh? Really?"
                jaylee.name "Shush!"
        elif jaylee.inv.qty(item_map_pill) >= 3:
            jaylee.name "I think you will need these a lot more than me sweetie."
            $ temp_var_1 = False
        else:
            jaylee.name "Oooh, can't dig these up round the junkheaps."
    elif buy_inv.qty(item_abort_pill):
        if jaylee.is_pregnant and jaylee.pregnant_who.abort:
            jaylee.name "Thanks, be glad to get rid of this..."
            if jaylee.showing:
                pc "Yeah, seeing the belly I thought I would offer."
        elif jaylee.is_pregnant:
            if jaylee.pregnant_who == ashon.setname:
                jaylee.name "No thanks. I'll be seeing this one to the end."
            else:
                jaylee.name "Thanks... But I don't think I want to use it. Think I will be seeing this one though."
            pc "Oh? Okay then."
            $ temp_var_1 = False
        elif jaylee.inv.qty(item_map_pill) >= 2:
            jaylee.name "Got a few of those in my trailer. You might see more use out of them."
            $ temp_var_1 = False
        else:
            jaylee.name "Err, not sure I'll have need of those..."
            jaylee.name "Best to take them anyway in case. Thanks cutie!"
    elif buy_inv.qty(item_pepperspray):
        if jaylee.inv.qty(item_pepperspray):
            jaylee.name "You already have me one of these. Keep it to shoo away the folk who jump on you out there."
        else:
            jaylee.name "Wow. Never dug one of these up. Thanks."
    else:
        show jaylee neutral
        jaylee.name "Aw you tease."
    if temp_var_1:
        $ jaylee._love += (inv_value(buy_inv) / 4)
        $ inv_transfer(buy_inv, jaylee.inv)
    else:
        $ inv_transfer(buy_inv, inv)
    show jaylee neutral
    jump jaylee_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
