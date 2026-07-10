label random_event_bus_grope:
    jump expression WeightedChoice([
    ("random_event_bus_grope_1", 100),
    ("random_event_bus_grope_2", 100),
    ("random_event_bus_grope_3", 100),
    ("random_event_bus_grope_4", 100),
    ])

label random_event_bus_grope_1:
    $ player.face_worried()
    $ player.sex_forced(busgroper)
    $ player.grope_hips()
    if player.has_perk([perk_slut, perk_sucu, perk_bimbo], notif=True):
        pc "Oh?"
        pc "Errr..."
    else:
        pc "Ugh!"
        pc "Piss off..."
    $ player.grope_poke()
    pervert "Nnng!"
    $ player.sex_cum(busgroper, "ass", no_sex=True)
    $ player.face_annoyed()
    pervert "Ahhhh!"
    if player.has_perk([perk_slut, perk_sucu, perk_bimbo]):
        pc "*Tsk*"
        $ player.grope_end()
    else:
        $ player.face_angry()
        pc "Ugh, fuck off!"
        $ player.grope_end()
        with hpunch
        $ player.face_annoyed()
        pcm "Ugh, dirty fuck!"
    jump bus_travel_end

label random_event_bus_grope_2:
    $ player.sex_forced(busgroper)
    $ grope_mastleft = True
    $ player.sex_cum(busgroper, "ass", no_sex=True)
    $ player.face_worried()
    pervert "Ahhhh!"
    $ player.face_angry()
    pc "Ugh!"
    $ grope_mastleft = False
    with hpunch
    $ player.face_annoyed()
    if player.has_perk([perk_slut, perk_sucu, perk_bimbo]):
        pc "Ugh..."
    else:
        pcm "Ugh, dirty fuck!"
    jump bus_travel_end

label random_event_bus_grope_3:
    $ player.grope(steal=True)

    if player.has_perk([perk_sucu, perk_slut], notif=True) or player.check_sex_agree(5):
        pcm "Oh? A pervert?"
        $ player.grope(steal=True)
        pcm "Whatever..."
        $ player.grope(steal=True)
        "I just stand there letting him do what he wants. It's not worth the trouble of pushing back."
        $ player.grope(steal=True)
        pcm "..."
        $ player.grope(steal=True)
        if numgen(0,200) < player.allure:
            jump random_event_bus_sex_hump_want
        pcm "Ah, close to my stop..."
    elif player.check_nowill():
        $ player.sex_forced(busgroper)
        pcm "Shit. A pervert..."
        $ player.grope(steal=True)
        pcm "..."
        $ player.grope(steal=True)
        pcm "I just stand there like an idiot letting him feel me up and hoping others on the bus don't realise what's going on."
        $ player.grope(steal=True)
        pcm "..."
        $ player.grope(steal=True)
        if not numgen(0,10):
            jump random_event_bus_sex_passive
        pcm "Ah, close to my stop..."
    else:
        "Ah!"
        $ player.face_angry()
        $ player.grope_end()
        with vpunch
        if player.check_sex_agree(3,notif=False):
            $ player.face_shy()
        else:
            pcm "Idiot."
    $ player.grope_end()
    jump bus_travel_end

label random_event_bus_grope_4:
    $ grope_mastleft = True
    $ player.face_worried()
    pc "Err..."
    $ grope_mastright = True
    pcm "What the fuck?"
    if player.has_perk([perk_slut, perk_sucu, perk_bimbo], notif=True):
        pcm "The perverts are multiplying."
        pcm "Whatever"
        pcm "Weirdos."
        $ player.grope(steal=True)
        pc "Ah!"
        pcm "Someone else joined the party?"
        $ player.grope(steal=True)
        pc "*Tsk*"
        pcm "Not the right place guys."
        $ player.sex_cum(busgroper, "ass", no_sex=True)
        pc "Ah."
        $ player.grope(steal=True)
        pc "*Sigh*"
        $ player.sex_cum(busgroper, "belly", no_sex=True)
        pcm "Gonna leave here looking like a hooker."
        $ player.grope(steal=True)
        $ player.sex_cum(busgroper, "ass", no_sex=True)
        pcm "Ugh..."
        pc "Ok, enough. Shoo!"
        pc "Go away."
        $ player.grope_end()
        pcm "..."
        pcm "Get some peace..."
    elif player.check_nowill():
        $ player.sex_forced(busgroper)
        pcm "Shit..."
        pcm "Go away. Please!"
        $ player.grope(steal=True)
        pc "Ah!"
        pcm "More of them?"
        $ player.grope(steal=True)
        pcm "Nonono!"
        pc "Please... Don't..."
        $ player.sex_cum(busgroper, "ass", no_sex=True)
        pc "Ah."
        $ player.grope(steal=True)
        pcm "Fuck"
        $ player.sex_cum(busgroper, "belly", no_sex=True)
        pcm "..."
        $ player.grope(steal=True)
        $ player.sex_cum(busgroper, "ass", no_sex=True)
        pcm "Ugh..."
        $ player.grope_end()
        pcm "Thank fuck they left..."
        pcm "Leaving me all dirty..."
    else:
        pc "*Tsk*"
        $ player.grope_end()
        with hpunch
        "I push against them and stand somewhere else on the bus."
        pcm "Damn perverts..."
        pcm "Ugh."
    jump bus_travel_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
