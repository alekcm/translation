label school_photo_quest_photoshoot_virgin:
    "*** NOT WRITTEN YET ***"
    "This is just here as a teaser for what is to come."
    "Sammy can trigger this shoot if she is a virgin or has had very little sex."
    if player.pregnant:
        "You are pregnant so wouldn't be able to claim you are a virgin."
    elif player.pregbabies:
        "You have had a baby already so wouldn't be able to pull off being a virgin."
    elif player.vvirgin:
        "You are a virgin so will trigger this event no problem."
    elif player.vsex <= 5:
        "You have had sex [playr.vsex] times. So would be able to lie and trigger this event."
    else:
        "You have had too much sex so wouldn't be able to pull this off."
    "The guy will offer to take your virginity on camera and will offer to pay a fortune to do so."
    "It will be a considerable amount of money."
    "You will only be able to trigger this if you are not on your period, so if you are not on pills there will be a pregnancy chance as he will want to cum inside."
    "If you are an actual virgin, you will speak to [felix.name] about it and the chance to have sex with him first will be presented."
    "Otherwise you will have sex with the guy while [felix.name] takes photos, it will be a fairly lengthy scene and he will cum multiple times."
    "It will finish, you clean up and the shoot ends."
    $ walk(loc_school_hallway)
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
