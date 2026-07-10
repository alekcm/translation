label random_event_bus_busy:
    jump expression WeightedChoice([
    ("random_event_bus_busy_1", 100),
    ])

label random_event_bus_busy_1:
    pcm "Fuck. Bus is ram packed."
    with hpunch
    pcm "Ugh..."
    $ player.grope(hands=False)
    pc "Ah!"
    jump bus_travel_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
