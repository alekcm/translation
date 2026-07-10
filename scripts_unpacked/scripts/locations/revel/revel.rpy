label loc_revel_visit:
    if log.interactive("quest_homeless_start_03"):
        pcm "Seems pretty busy around here. I should have a look and see if there is anything."
    elif log.interactive("quest_homeless_start_04"):
        pcm "Seems pretty busy around here. I should have a look and see if there is anything. The hospital I am supposed to meet [emile.name] at should be around here somewhere."
    else:
        pcm "This place is pretty busy. The hospital [tucker.name] works in should be around here somewhere. Wonder what else might be around?"
    jump travel

label loc_revel_explore:
    pcm "Pretty busy high street. That bridge looks like one for trains. Wonder if there is a station round here somewhere."
    if t.hour in loc_pub.opening_hours:
        pcm "Looks like the pub is open. Might not be a good idea for me to hang out there though considering what I have heard."
    else:
        pcm "Pub is closed but looks like it still functions."
    if log.interactive("quest_homeless_start_03"):
        pcm "And some kind of market over there. I arrived with pretty much nothing so maybe I can find something there."
    else:
        pcm "Ah, there is the hospital [tucker.name] told me to come to if I want to see him."
        pcm "And looks like there are some shops further down. Probably where me and [emile.name] went and got me some clothes."
    jump travel

label loc_revel_backstreet_visit:
    pcm "Err, wow. Looks shady back here..."
    jump travel

label loc_revel_backstreet_explore:
    pcm "Hmm, seems like a few less reputable places here..."
    pcm "Tattoo place. Can't imagine it's very hygienic. Don't wanna die of sepsis because of a tattoo."
    pcm "Some what looks like sexy shops as well..."
    jump travel

label loc_shop_funwear_closed:
label loc_shop_tattoo_closed:
    pcm "Closed. Sign says noon 'til midnight"
    if not loc(loc_revel_backstreet):
        $ walk(loc_revel_backstreet)
    jump travel

label funwear_shop:
    show fun_girl at right1 with dissolve
    fun_girl.name "What can I help you with darling?"
    call screen inventory_itemshop_screen(shop_funwear)
    if quest_flyers.timesworked > 6 and not "funwear_start" in quest_flyers.list:
        pc "Err, you don't need flyers handed out do you?"
        fun_girl.name "We do actually. Hard to find girls to do it though."
        pc "Err, why?"
        fun_girl.name "Look how I am dressed. Not many wanna go out with stickers on their tits to hand them out."
        fun_girl.name "If you are fine with that, come work for me. We pay more than the rest."
        pc "Okay, thanks."
        $ add_to_list(quest_flyers.list, "funwear_start")
        hide fun_girl with dissolve
        jump travel

    fun_girl.name "Hope to see you again."
    hide fun_girl with dissolve
    jump travel

label funwear_shop_flyer_firsttime:
    show fun_girl at right1 with dissolve
    pc "So... Handing out fliers?"
    fun_girl.name "You're up for it? Great! Hold on..."
    hide fun_girl with dissolve
    pc "Okay, what for?"
    pc "..."
    show fun_girl at right1 with dissolve
    fun_girl.name "Okay, I dug something up for you to wear."
    fun_girl.name "Don't worry, it's a bit more modest than I have. Can't have you getting arrested or something."
    pc "Yeah right, those clowns probably wont arrest anyone even for murder."
    fun_girl.name "Yeah, but they have no issue dragging girls in for some fun."
    fun_girl.name "Here, take this."
    hide fun_girl with dissolve
    $ wardrobe.take(item_bottom_34)
    $ wardrobe.take(item_top_42)
    $ wardrobe.take(item_pants_8)
    $ wardrobe.take(item_socks_9)
    $ outfit_funwear()
    $ pc_dress_event("work", loc_mall_changingroom, say="Err, isn't this worse than the stickers?")
    show fun_girl at right1 with dissolve
    fun_girl.name "Wonderful!"
    fun_girl.name "I won't be replacing your stuff if it gets lost. But no problem if you want to go out there in your bare arse."
    fun_girl.name "I'll pay more if you do."
    pc "Pretty much bare arse right now."
    fun_girl.name "Still pay more than others anyway. Don't get into too much trouble now will you."
    pc "Thanks..."
    fun_girl.name "Okay, off you go!"
    return

label loc_party_main_locked:
    if school_dance_waiting_party():
        pcm "The girls are outside, I should meet with them first."
    elif t.hour in (19,20) and t.wkday == "Saturday":
        pcm "Need to wait a bit for the party to start. The girls should arrive around 9ish."
    elif t.hour == 4 and t.wkday == "Sunday":
        pcm "Party is over, I should wait for the girls outside."
    elif t.hour in (5,6) and t.wkday == "Sunday":
        pcm "Party is over and people have gone home. I should head off too."
    else:
        pcm "Nothing going on there, I should come back on Saturday."
    jump travel





label piercing_shop:
    call screen inventory_itemshop_screen(shop_piercings) 
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
