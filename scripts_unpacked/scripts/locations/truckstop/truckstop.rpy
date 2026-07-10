label loc_truckstop_visit:
    pcm "Seems like where all the delivery trucks wait until they have to go back out for a delivery."
    pcm "There is a diner just over there and looks like a motel as well."
    if t.hour in dark:
        pcm "Also seems like a lot of prostitutes hanging around. I guess they are looking to take the truck drivers back to the motel."
    if log.interactive("quest_homeless_start_01"):
        pcm "Maybe [emile.name] is around the motel. Although she wouldn't have money to rent a room."
    jump travel

label loc_motel_visit:
    $ player.face_worried()
    pcm "Ugh, this place looks just as seedy as I thought it would be."
    pcm "Truckers staying here overnight and no doubt inviting hookers to join them."
    pcm "..."
    if log.interactive("quest_homeless_start_01"):
        pcm "Hope [emile.name] hasn't been dragged off as a hooker..."
        pcm "Can't see her anywhere. Doubt she will be in one of the rooms since neither of us have any money."
    else:
        pcm "They might need cleaners though..."
        pcm "Fuck, having to clean up after... Them..."
        pcm "Need to earn money though, and don't much fancy being the whore in bed with them."
    jump travel

label loc_motel_pool_visit:
    pcm "Nice..."
    pcm "More piss and puke than actual water."
    jump travel

label loc_diner_visit:
    "On first entering a woman will approach you and tell you to sit where you like"
    "You will respond saying you are actually looking for work."
    "She will tell you to come see her at whatever point in the day this place will allow you to work."
    "Much like the pub, you will arrive, start your first day and be able to repeat hours."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
