label market_stall_milkstand_discover:
    pcm "Hmm, what is this place?"
    $ renpy.scene()
    $ walk(loc_market_stall_milk)
    pc "Hmmm..."
    show hucow at right1 with dissolve
    hucow.name "Heya darling. Selling some milk?"
    pc "Huh?"
    hucow.name "Got some milk to sell?"
    pc "Why would I have milk? What is this place?"
    hucow.name "A new one eh?"
    pc "Errr... Sure?"
    hucow.name "We buy and sell milk here."
    $ player.face_worried()
    pc "..."
    pc "Okay..."
    pcm "Is everyone here crazy like her?"
    hucow.name "So if you got some to sell, come to me."
    pc "Why would I have milk to sell? I don't have a cow hiding in my bedroom."
    hucow.name "Ahh. Hahaha! Silly. You are the cow."
    pc "What?"
    $ player.face_shock()
    hucow.name "Mooo!"
    pc "Whaaa?"
    hucow.name "No one has cows in their bedroom any more. Or on the farms for that matter. So we milk ourselves."
    $ player.face_worried()
    pc "What are you... What? The milk is...?"
    hucow.name "Yup."
    hucow.name "If you start leaking like a cow, come and buy my stuff and make some money out of it."
    pc "What, people actually buy this?"
    hucow.name "Wouldn't stand here \"mooing\" like an idiot if they didn't."
    $ player.face_neutral()
    pc "Right... It make money?"
    hucow.name "Enough to be worth it."
    pc "And the clothes?"
    hucow.name "Most people who buy are perverts. So might as well go the whole hog."
    hucow.name "Sell you a spare set if you want."
    call screen inventory_itemshop_screen(shop_milk, show_locked=True)
    $ shop_milk.open = True
    pc "Wait, so this pill thing?"
    hucow.name "Yup, turns you into a cow."
    pc "Nice way to put it."
    hucow.name "Milk yourself and come sell me the bottles. Basically free money."
    pc "Right... Thanks..."
    hucow.name "See ya round."
    hide hucow
    $ walk(loc_market)
    pcm "What the hell is the world coming to?"
    jump travel

label market_stall_milkstand_shop:
    show hucow at right1 with dissolve
    hucow.name "Mooo!"
    call screen inventory_itemshop_screen(shop_milk, show_locked=True)
    hucow.name "Come again."
    $ renpy.scene()
    with dissolve
    jump travel

label market_stall_milkstand_junk:
    show hucow at right1 with dissolve
    hucow.name "Got milk for me?"
    call screen inventory_junk_choice(shop_milk, choices=[item_scrap_milkbottle])
    if log.interactive("quest_flyers_01") and player.lactating and not "milkmaid_start" in quest_flyers.list:
        jump market_stall_milkstand_flyer_offer
    hucow.name "Mooo!"
    $ renpy.scene()
    with dissolve
    jump travel

label market_stall_milkstand_flyer_offer:
    $ add_to_list(quest_flyers.list, "milkmaid_start")
    hucow.name "You're a good cow now. Want to do some flyering for me?"
    pc "Err, sure? Why does me being a cow have to do with that?"
    hucow.name "Send a cow to advertise the milk."
    pc "Right. Well, sure. Whatever. It pays?"
    hucow.name "Of course. Come see me when you want to earn some more."
    $ renpy.scene()
    with dissolve
    jump travel

label market_stall_milkstand_flyer_firsttime:
    show hucow at right1 with dissolve
    pc "So, want me to do the flyer thing?"
    hucow.name "Moo! I have clothes in the back."
    pc "Clothes?"
    hucow.name "Going to dress you like a cow."
    pc "Err, okay... You giving me the outfit?"
    hucow.name "Giving? No. You wear it and give it back to me."
    pc "But, it's just a pair of pants and other bits."
    if player.lactating:
        hucow.name "Yup. Leak all in the bra and make the rest all smelly. People will pay good money for it."
    else:
        hucow.name "Yup. Walk around a lot in 'em and make 'em all smelly. People will pay good money for it."
    if player.showing:
        hucow.name "You having that fat belly is even better. I'll pay more while you have it."
        hucow.name "Good cows should be fat cows."
    $ player.face_sus()
    pc "Ah fuck... Right, I forget everyone is a damn weirdo..."
    hucow.name "If you come back with missing bits, I'll charge you."
    $ player.face_worried()
    pc "Are you telling me to bring everything back or telling me I need to make more than you charge?"
    hucow.name "Take your pick. I don't much care."
    hucow.name "Just be careful you don't get bent over and milked fresh."
    pc "Is... That something that might happen?"
    hucow.name "Often enough I am thinking to open a back room and charging the weirdos to milk us."
    pc "..."
    $ player.face_neutral()
    pc "Probably not a bad idea to make money..."
    hucow.name "I know! Moooo!"
    hide hucow with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
