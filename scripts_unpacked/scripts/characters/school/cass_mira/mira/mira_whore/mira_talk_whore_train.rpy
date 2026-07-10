label mira_whore_train_start:
    if not dis(dis_truckstop):
        pcm "I should speak to her at the highway if I want to do this."
        jump travel

    $ player.face_worried()
    if not player.check_whore(vag_sex=False):
        pcm "I know I can make money doing this. But it is whoring..."
        pcm "[mira.name] does it though. And it's not like she is some junkie waster."
        pcm "..."
        pcm "Ugh..."
    pcm "Do I really want to ask her about it?"
    pcm "Hanging out the highway and fucking strangers for money?"
    menu:
        "Yes, ask":
            $ NullAction()
        "No, Don't bother":
            pcm "Probably best not to."
            jump travel
    pc "Errm... Your offer before."
    show mira at right1 with dissolve
    mira.name "My offer?"
    pc "About making extra money. Y'know. Doing this job."
    mira.name "Oh? You interested?"
    pc "Well, maybe you can just show me how it all works?"
    mira.name "You sure about this?"
    pc "No."
    mira.name "..."
    pc "But show me anyway."
    if player.has_perk(perk_slutty):
        mira.name "Well, you are already doing a good job of looking the part."
        pc "Thanks?"
        if "school" in tab_top:
            mira.name "The uniform is okay as well. But people might ask for weird things if you wear it. So kinda of a double edges sword."
    else:
        mira.name "Okay. Well not much to show. You see how I am dressed?"
        pc "Yeah..."
        mira.name "Well, I am probably over dressed for this job."
        mira.name "Best to wear as little as possible. No clothes also works but that invites way too much trouble to be worth it."
    pc "Right..."
    mira.name "That guy over there is looking at you. You could probably go over there now and fuck him."
    pc "Err, let's take it easy for now."
    mira.name "Okay. Well you just stand around here and look inviting. Make it clear you are looking for company."
    pc "Aren't pretty much all girls doing that round here?"
    mira.name "Not all. Some are keeping watch for security. Others work the Diner over there and have no interest in this stuff."
    mira.name "Some are junkies. They would fuck for money but don't really get any customers because they look a mess."
    mira.name "Maids for the motel, people cleaning the trucks, scavvers. Lot of girls round here that aren't working. So you should make it a bit obvious what you are doing."
    pc "Right. Okay."
    if not loc(loc_motel):
        show mira at left1 with dissolve
        mira.name "Follow me."
        $ walk(loc_motel)
    mira.name "The motel here has special rooms for whores."
    mira.name "Speak to the girl at reception and ask for a pink room. You go inside, strip off, show off by the window and have people come in the room for fun."
    pc "Why aren't you in there?"
    mira.name "I do sometimes. But people who go there usually want crazy stuff. Can earn a lot of money but might not be able to work for a bit after."
    pc "Err, what kind of stuff?"
    mira.name "Gangbangs, beat you up, hardcore anal. One guy even offered me money to let him practice tattooing on me."
    pc "Right, so not just a blowjob and done."
    mira.name "No..."
    pc "be prepared for a difficult time if you get a pink room."
    mira.name "That's about it. Not much else to know."
    mira.name "Oh, stay with other girls around. Guys can get a bit out of hand if you aren't careful. Make friends with people and stick together."
    pc "Make friends? With the other whores?"
    mira.name "Yeah."
    pc "Right... Okay. Thanks."
    mira.name "Good luck. You can hang out with me if you want."
    pc "Right."
    hide mira with dissolve
    $ log.assign("Street walking")
    $ log.activate("quest_whore_02")
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
