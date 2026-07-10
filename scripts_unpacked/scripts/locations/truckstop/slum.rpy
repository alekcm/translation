label loc_highway_slum_still_closed:
    pcm "Sign says 3pm to 3am."
    jump travel

label loc_highway_slum_still_visit:
    if log.interactive("quest_homeless_start_01") or log.interactive("quest_homeless_start_02"):

        if log.interactive("quest_homeless_start_01"):
            pcm "No [emile.name] here."
        else:
            pcm "Hmm, occupied. I better leave before the guy gets any ideas."
        $ loc_highway_slum_still.visited = False
        $ walk(loc_highway_slum_street)
        jump travel

    if havenvik.has_met:
        $ player.face_worried()
        pcm "Ah shit. I know him. We met in [haven]."
        if havenvik.pregbabies:
            pcm "And I ended up giving birth to his kid."
        elif havenvik.preg:
            pcm "He ended up getting me pregnant."
        elif havenvik.sex:
            pcm "Ended up having sex with him to get some booze to deal with that shithole."
        elif havenvik.naughty:
            pcm "Ended up doing stuff to get some booze from him."
        else:
            pcm "He sold some homebrew booze in there."
        pcm "Hopefully he won't recognise me..."
    else:
        pcm "Errr, this place looks as much a dump as I thought it would..."
    show haven_viktor at right1 with dissolve
    havenvik.name "This isn't a sight seeing tour. What you want?"
    pc "You selling stuff?"
    havenvik.name "Yeah, have a look."
    call screen inventory_itemshop_screen(havenvik.inv)
    pc "That's... A lot of booze."
    havenvik.name "Make it here, the brew anyway. The beer is recycled."
    pc "Recycled, I know it tastes like piss but to think it actually was."
    havenvik.name "Ha! Not that bad. Rebottled from kegs. So if you get any bottles, come sell 'em to me."
    pc "Right, okay. Anything else you buy?"
    havenvik.name "Drugs and cigs. I'll take anything you don't need off your hands."
    pc "Okay. Good to know."
    if log.interactive("quest_daniwine_01"):
        pc "Wait, do you also sell wine?"
        havenvik.name "Hmm, you aren't the first to ask. Think I'll try and get my hands on some."
        havenvik.name "Wont be cheap though."
        pc "How much?"
        havenvik.name "Dunno, come back in a few days when I restock and I should have some."
        pc "Okay."
        $ item_winebottle.locked = False
        $ log.markdone("quest_daniwine_01")
    hide haven_viktor with dissolve
    jump travel

label slum_havenvik_shop:
    show haven_viktor at right1 with dissolve
    havenvik.name "Come 'n' get it."
    call screen inventory_itemshop_screen(havenvik.inv)
    havenvik.name "Cheers."
    if log.interactive("quest_daniwine_01"):
        pc "No wine? Was hoping to find some here."
        havenvik.name "Hmm, you aren't the first to ask. Think I'll try and get my hands on some."
        havenvik.name "Wont be cheap though."
        pc "How much?"
        havenvik.name "Dunno, come back in a few days when I restock and I should have some."
        pc "Okay."
        $ item_winebottle.locked = False
        $ log.markdone("quest_daniwine_01")
    hide haven_viktor with dissolve
    jump travel

label slum_havenvik_sell:
    show haven_viktor at right1 with dissolve
    havenvik.name "Got some bottles?"
    call screen inventory_junk_choice(havenvik.inv, choices=[item_scrap_junk, item_cigs, item_map_pill, item_abort_pill, item_joy, item_lebo, item_wakeup, item_mag_felix])
    havenvik.name "Cheers."
    hide haven_viktor with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
