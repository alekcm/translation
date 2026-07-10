label kitty_talk_haven_thanks:
    $ add_to_list(kitty.list, "haven_thanks")
    show kitty at right1
    kitty.name "What you want?"
    pc "Err, not sure actually. I met you in [haven] and guess I want to say \"thanks\"."
    kitty.name "Dunno who you are, but whatever. Glad I helped I guess."
    pc "Right..."
    hide kitty with dissolve
    jump travel

label kitty_meet_chain_0:
    $ kitty.dict["kitty_meet_chain"] += 1
    pc "Err, so this whole... Whore stuff..."
    kitty.name "What? You interested? You shouldn't be."
    pc "Err, somewhat. Kinda just want to know what it's all about."
    kitty.name "Get a guy to fuck you, get money for it. Nothing more to know."
    jump kitty_talk_end

label kitty_meet_chain_1:
    $ kitty.dict["kitty_meet_chain"] += 1
    pc "Is it safe to do this?"
    kitty.name "Not really. Gotta have other girls watch your back."
    pc "..."
    jump kitty_talk_end

label kitty_meet_chain_2:
    $ kitty.dict["kitty_meet_chain"] += 1
    kitty.name "Look, if you're gonna do this job. You're gonna end up in some trouble."
    pc "Like what?"
    kitty.name "Someone kicking the shit out of you instead of paying. Plod bullying for freebies..."
    kitty.name "Dragged somewhere and raped. Fucking dealers for free pills. A little shit in your belly."
    pc "..."
    jump kitty_talk_end

label kitty_meet_chain_3:
    $ kitty.dict["kitty_meet_chain"] += 1
    $ add_to_list(kitty.list, "whore_offer")
    kitty.name "If you still wanna do this shit job, I'll show you round."
    kitty.name "But young'un like you better stick to the jobs in Revel. Sell your arse a bit there for extra."
    kitty.name "Much safer to fuck around there than t' come round here."
    pc "Right..."
    jump kitty_talk_end

label kitty_whore_quest_start:
    show kitty at right1 with dissolve
    pc "Err, so this whore stuff..."
    kitty.name "Your funeral."
    pc "Right..."
    kitty.name "Not much to show. Stand here looking like a whore and give the guys you see a look."
    pc "A look?"
    kitty.name "Yeah. One that let's 'em know you're a whore and for sale."
    pc "Wouldn't just being here do that?"
    kitty.name "No. Lot of other girls round here work without their arse."
    pc "Okay."
    if not loc(loc_motel):
        kitty.name "Come here."
        $ walk(loc_motel)
    kitty.name "The bitch in there will rent you a blue room to wash up and stuff."
    kitty.name "She will also rent a pink room for the depraved shits to do depraved shit to you."
    pc "Err..."
    kitty.name "If you in a hurry to be a corpse, get a pink room. They will pay you a lot til someone murders you."
    pc "Okay..."
    kitty.name "And don't have your ghost haunt me when someone is raping your corpse."
    hide kitty with dissolve
    pcm "Right... Okay then..."
    $ log.assign("Street walking")
    $ log.activate("quest_whore_02")
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
