label bus_travel:
    pause 0.5
    $ travel_walk(loc_bus_interior)
    $ player.face_normal()
    $ dialouge = renpy.random.choice([
    "I get on the bus and find somewhere to stand and wait for my stop to arrive.",
    "I hop on and manage to get somewhere to stand and wait for my stop.",
    "I get on and take a place to stand and wait for my stop.",
    ])
    "[dialouge]"
    call expression WeightedChoice([
    ("random_event_bus_geton_1", 100),
    ("random_event_bus_geton_2", If (t.hour in workhours, 100, 0)),
    ("random_event_bus_geton_3", If (t.hour in rushhour, 100, 0)),
    ("random_event_bus_geton_4", If(player.has_perk([perk_wasted, perk_blackout]), player.drunk, 0)),
    ("random_event_bus_geton_5", If (t.timeofday == "night", 100, 0)),
    ]) from _call_expression_3
    jump random_event_picker_bus_tombola

label random_event_picker_bus_tombola:
    jump expression WeightedChoice([
    ("random_event_bus_normal", 100),
    ("random_event_bus_busy", 100),
    ("random_event_bus_grope", If(danger_delay(), player.allure, 0)),
    ("random_event_bus_dirty", If (player.is_dirty(), 500, 0)),
    ("random_event_bus_horny", If (player.check_horny(extreme=True) and not t.hour in (1,2,3,4,5), player.check_horny(extreme=True), 0)),
    ("random_event_bus_drunk", If (player.has_perk([perk_wasted, perk_blackout]), player.drunk, 0)),
    ("random_event_bus_preg", If (player.pregnancy >= 2, 100, 0)),
    ("random_event_bus_robin", If (robin_here(), 100, 0)),
    ])

label random_event_bus_geton_1:
    $ player.face_annoyed()
    pcm "This place stinks as usual..."
    return

label random_event_bus_geton_2:
    $ player.face_worried()
    pcm "Squashed in here like sardines..."
    return

label random_event_bus_geton_3:
    $ player.face_worried()
    pcm "Totally jam packed. Fuck."
    pcm "Damn bus is always a nightmare at this time."
    return

label random_event_bus_geton_4:
    pcm "Ah shit. All wobbly..."
    return

label random_event_bus_geton_5:
    pcm "Night time bus rides. What could go wrong?"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
