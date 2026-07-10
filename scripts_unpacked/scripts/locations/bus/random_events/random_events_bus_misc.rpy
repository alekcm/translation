label random_event_bus_dirty:
    jump expression WeightedChoice([
    ("random_event_bus_busy_1", 100),
    ])

label random_event_bus_dirty_1:
    with vpunch
    guy "You stink!"
    pcm "Ugh..."
    man "Ugh, go away you dirty bitch."
    with hpunch
    pc "..."
    $ player.add_mood(-15)
    jump bus_travel_end

label random_event_bus_dirty_2:
    with vpunch
    pc "Ugh!"
    guy "Dirty bitch!"
    pcm "..."
    $ player.add_mood(-15)
    with vpunch
    guy "Go somewhere else!"
    pc "..."
    $ walk(renpy.random.choice(busstops), trans=hpunch)
    pc "Ouch!"
    pc "Fuckers!"
    pcm "Where am I?"
    $ relax(15)
    jump travel_arrival

label random_event_bus_preg:
    jump expression WeightedChoice([
    ("random_event_bus_preg_1", 100),
    ("random_event_bus_preg_2", 100),
    ])

label random_event_bus_preg_1:
    $ player.face_worried()
    pcm "Ugh, bad enough on these buses without having a giant belly."
    with vpunch
    pcm "Impossible to squeeze by."
    $ player.grope(hands=False)
    pc "Ah!"
    pcm "..."
    jump bus_travel_end

label random_event_bus_preg_2:
    $ player.face_worried()
    pcm "Ugh, feet are killing me and still need to stand."
    pcm "Maybe I could sit?"
    pcm "Err, better not. Will have some pervert trapping me in right away."
    jump bus_travel_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
