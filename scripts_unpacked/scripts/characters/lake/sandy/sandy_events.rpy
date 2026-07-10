label boardwalk_bikini_kiosk:
    show sandy at right1 with dissolve
    if not sandy.has_met:
        jump boardwalk_bikini_kiosk_first
    sandy.name "Hey [name]. Wanna buy something?"
    call screen inventory_itemshop_screen(sandy.inv)
    sandy.name "Come back if you wanna sell something."
    hide sandy with dissolve
    jump travel

label boardwalk_shell_kiosk:
    show sandy happy at right1 with dissolve
    sandy.name "Hey! Got something cute for me [name]?"
    call screen inventory_junk_choice(sandy.inv, choices=[item_scrap_seashell, item_scrap_jewel, item_scrap_gem, item_scrap_cloth])
    sandy.name "Come back if you wanna sell something."
    hide sandy with dissolve
    jump travel

label boardwalk_bikini_kiosk_first:
    sandy.name "Hey sweetie. I'm [sandy.name]. Come have a look at what I got."
    pc "[name]. What is this place?"
    sandy.name "Got swimwear for you so you can have fun in the water."
    sandy.name "Or I'll take some o' the stuff you find in the sand off you."
    pc "Find in the sand?"
    sandy.name "Yeah. I make some cute jewellery from the shells. Sometimes something prettier washes up."
    sandy.name "If it's cute or shiny, I might buy."
    pc "Ok, I'll keep that in mind."
    sandy.name "Wanna buy something to swim in? I got something you might like."
    pc "Hmm, let's have a look."
    call screen inventory_itemshop_screen(sandy.inv)
    sandy.name "Can also hand out flyers if you want. I'll pay."
    if quest_flyers.active:
        pc "Oh, sounds good."
    else:
        pc "Flyers?"
        sandy.name "Bits of paper with my stall name on it showing what I sell."
        pc "Okay, what, hand them out on the beach here?"
        sandy.name "Yeah, send people here for swimwear or drinks."
        pc "Okay, thanks."
        $ log.assign("Flyering")
        $ diary_jobs_flyers_func("sandy")
    hide sandy with dissolve
    jump travel

label boardwalk_bikini_kiosk_flyers_first:
    show sandy at right1 with dissolve
    pc "So, just hand out the flyers on the beach?"
    sandy.name "That's right. Wear a bikini or something while you do it."
    pc "Ah, okay."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
