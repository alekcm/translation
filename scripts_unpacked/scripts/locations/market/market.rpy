label loc_market_explore:
    if t.hour >= 21 or t.hour <= 7:
        $ loc_market.explored = False
        pc "The market is closed right now so there isn't much to see. I should come back when it's open to have a look around"
    else:
        "I wander around the market having a look at the stalls and what they have to offer."
        $ player.face_neutral()
        pcm "It looks like they mostly sell odds and ends. I can probably pick things up here for cheaper than the stores but I probably need to buy right away or next time it will be sold to someone else."
        pcm "Hmmm, I can see people handing out flyers, I wonder if that's something I can do?"
        pc "Err, hi."
        show flyergirl at right1 with dissolve
        flyergirl.name "Gossip mags, sports mags, porn mags. All old and new stuff."
        pc "Err, actually I was wondering about a job... With the flyers."
        flyergirl.name "Buncha places wan' a girl t' 'and out dese fings."
        pc "Err, okay... So what do I do."
        flyergirl.name "Ask some stall. Dey giv' ya the stuff, come back with nuttin and get paid."
        pc "Okay... Thanks."
        hide flyergirl with dissolve
        flyergirl.name "Got the good porn and the nasty porn. Come to Jaz 'n Jay's!"
        pcm "Right, okay. I can look around for people who want me to hand these things out."
        if not quest_flyers.active:
            $ log.assign("Flyering")
            $ diary_jobs_flyers_func("market")
        $ stroll(20)
    jump travel

label loc_market_visit:
    if log.interactive("quest_homeless_start_03"):
        pcm "Oooh a market. I wonder what I can pick up?"
    else:
        pcm "Oh, this is the market [emile.name] took me to."
        pcm "Wonder what else they have for sale here?"
    jump travel

label market_flyer_firsttime:
    show flyergirl at right1 with dissolve
    pc "Hey, so these flyers?"
    flyergirl.name "Jus' go to a place an' ask."
    flyergirl.name "Got some 'ere, take 'em and 'and 'em out."
    pc "Right, thanks."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
