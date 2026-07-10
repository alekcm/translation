label pinkroom_customer_event_drugdeal:
    pc "[rlist.pinkroom_welcome_single]"
    tempname.name "Hey, I just want somewhere out of the way for a bit."
    pc "Huh?"
    tempname.name "I'm here to meet someone in private, so take a break or something."
    $ inv.take(item_pinkticket, 2)
    pc "Err, okay then. I guess."
    if player.is_dirty():
        pc "I'll take a shower then while you do whatever it is you are doing."
        tempname.name "Cheers love."
        call shower_event_call from _call_shower_event_call
        "Looks like the guy has gone."
    else:
        pc "Okay, i'll just take a break then."
        tempname.name "Cheers love."
        show sb_onback look_up relaxed pout with dissolve
        "I lay on the bed and just relax a bit. I am getting paid for this so the rest is welcome."
        "Someone knocks on the door but the guy gets up and answers it and lets him in. He just glances at me then carries on talking to my punter."
        "Look like they exchange something. I am trying not to look in case it's something I shouldn't see so I can't quite tell what it is. Probably a drug deal or something."
        "Then the guy leaves, leaving me alone again with my punter."
        $ relax(10)
        tempname.name "Cheers darling. I'll just wait here for a minute and you can get back to doing your job."
        pc "Paid to relax? Stay here longer if you want."
        tempname.name "Haha."
        "Me and the guy chats about mundane things for a bit, then he gets up and leaves."
        $ relax(3)
    pcm "Well, I could do with more customers like that."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
