label random_event_bus_drunk:
    jump expression WeightedChoice([
    ("random_event_bus_drunk_1", 100),
    ("random_event_bus_drunk_2", 100),
    ("random_event_bus_drunk_3", If(player.tired < 30, 200, 0)),
    ])

label random_event_bus_drunk_1:
    with hpunch
    pcm "Whoa..."
    with hpunch
    pcm "Ugh... Damn bus moving all around..."
    jump random_event_bus_sex_drunk

label random_event_bus_drunk_2:
    with hpunch
    pcm "Whoa..."
    with hpunch
    pcm "Shit, this is harder than I thought..."
    "I stand there gripping onto the handrail and hope the bus doesn't throw me on my arse."
    pcm "Almost..."
    jump bus_travel_end

label random_event_bus_drunk_3:
    with hpunch
    pcm "Whoa..."
    with hpunch
    pcm "Shit, this is harder than I thought..."
    "I find somewhere to stand and just zone out hoping not to miss my stop."
    show screen blackout(50) with dissolve
    pause 0.5
    hide screen blackout
    $ player.grope()
    pc "Ah!"
    pcm "Errr..."
    pcm "Shit..."
    jump random_event_bus_sex_drunk
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
