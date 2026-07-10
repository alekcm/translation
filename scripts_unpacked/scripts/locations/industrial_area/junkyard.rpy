label loc_junk_entrance_visit:
    if t.hour in dark:
        pcm "Hmm, not sure what this place is, but looks like something could fall on me at any moment. Looks a shithole."
        pcm "I should come back in the day."
    else:
        pcm "A scrapyard? Maybe I should have a look around."
    jump travel

label loc_junk_entrance_explore:
    if t.hour in dark:
        pcm "I should come back during daylight to have a look around."
        $ loc_junk_entrance.explored = False
        jump travel
    $ loc_junk_office.locked = False
    $ jaylee.dict["jaylee_meet_events"] = 0
    pcm "Place is probably a scrapyard. Maybe a landfill?"
    pcm "A bunch of people climbing over the heaps so it looks like they are after something."
    pcm "Doesn't look like this was a scrapyard before all the trouble went down."
    show jaylee at right1 with dissolve
    jaylee.name "What you staring at?"
    $ player.face_frown()
    pc "Err, just looking around."
    jaylee.name "First time being here?"
    pc "Err, yeah."
    jaylee.name "Well it's what it looks like. A place for all the junk. You interested in scavving?"
    pc "Err, not sure. What is \"scavving\"?"
    jaylee.name "\"What is scavving?\" You just drag your arse into town or something?"
    $ player.face_neutral()
    pc "Something like that."
    jaylee.name "Oh? Okay then."
    jaylee.name "Scavving is looking for shit that others want to buy. No new stuff being made so gotta make do with what we find mosta the time."
    jaylee.name "All the shit you see here was dragged from the outside. Get killed if you are picky so it gets grabbed and hauled here for us cunts to go through it all."
    pc "Recycling all the stuff you find outside?"
    jaylee.name "Recycling, reusing, repairing. Whatever is easiest."
    jaylee.name "If you wanna have a go, just get your ass in there and start digging about. Lotsa people willing to buy stuff and won't be long 'fore you know what to look for."
    pc "Right. Thanks."
    if c.slutty:
        jaylee.name "An' don't dress like a whore while scavving. I don't wanna dig up your raped corpse from one o' the piles."
    elif c.skirt:
        jaylee.name "Wear better clothes if you gonna dig about. That skirt will have you fucked in the arse in no time."
    elif c.clevage:
        jaylee.name "Wear better clothes if you gonna dig about. Flashing those tits will draw attention from this shitty lot."
    else:
        jaylee.name "And be careful. This lot are scum. I don't wanna have to dig out your corpse cos one 'o this lot took a likin' to your arse."
    $ player.face_shock()
    pc "Oh? Okay. Thanks."
    hide jaylee with dissolve
    $ player.face_neutral()
    pcm "So I can make some money off of digging this stuff up and selling it?"
    pcm "Not the worst way to make money."
    $ quest_scav.activate()
    $ log.assign("Scavenger")
    $ diary_jobs_scavving_func()
    with dissolve
    jump travel

label loc_junk_office_visit:
    if ashon_here():
        show ashon at right1 with dissolve
        ashon.name "What you got to sell, new face?"
        pc "What do you buy?"
        ashon.name "Prefer electronics but will also take scrap. So, come to me if you get your hands on any."
        pc "Okay."
        hide ashon with dissolve
        pcm "Okay, so here is where I sell off some of the junk I can pick up."
    else:
        pcm "This the managers office? Sign says they buy scrap so I guess this is where I come to offload any junk I pick up."
    jump travel

label loc_junk_trailer_visit:
    pcm "Bit small but otherwise it looks alright."
    pcm "Stinks a bit though, no windows at all. Better not mention that to [jaylee.name]."
    pcm "Does she keep a lot of the stuff she scavs up around this place?"
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
