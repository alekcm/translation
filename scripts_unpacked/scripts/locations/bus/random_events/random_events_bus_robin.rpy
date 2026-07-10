label random_event_bus_robin:
    jump expression WeightedChoice([
    ("random_event_bus_robin_1", 100),
    ("random_event_bus_robin_2", 100),
    ("random_event_bus_robin_3", 100),
    ("random_event_bus_robin_4", If("pc_know_want_bussex" in robin.list, 70, 0)),
    ("random_event_bus_robin_5", If("pc_know_want_bussex" in robin.list, 50, 0)),
    ("random_event_bus_robin_6", If("pc_know_want_bussex" in robin.list, 70, 0)),
    ])

label random_event_bus_robin_1:
    $ player.face_happy()
    pcm "Oooh, I can see [robin.name]!"
    $ player.face_annoyed()
    with vpunch
    pc "Ung!"
    pcm "Too many people though, can't squeeze through."
    pcm "Ah well, I'll see her at home."
    jump bus_travel_end

label random_event_bus_robin_2:
    $ player.face_happy()
    show robin happy at left1 with dissolve
    pc "Oh, hey [robin.name]"
    robin.name "Ah hey!"
    "I hang out with [robin.name] chatting away and waiting for our stop."
    jump bus_travel_end

label random_event_bus_robin_3:
    $ player.face_happy()
    pc "Oh, I can see [robin.name]..."
    $ player.face_annoyed()
    with hpunch
    show robin at right6 with vpunch
    pc "Ung!"
    $ player.face_happy()
    show robin happy
    robin.name "Ah hey!"
    "I hang out with [robin.name] chatting away and waiting for our stop."
    jump bus_travel_end

label random_event_bus_robin_4:
    $ player.face_shock()
    pcm "Oh, is that [robin.name]?"
    show robin_bus_grope_behind grope with dissolve
    pcm "Yes... Yes it is..."
    pcm "Well, looks like she is having fun."
    "I end up standing there watching [robin.name] having some fun with the pervert that's getting handsy with her."
    hide robin_bus_grope_behind with dissolve
    jump bus_travel_end

label random_event_bus_robin_5:
    muff "Haaaaaa..."
    pcm "Huh?"
    pcm "Oh fuck?"
    $ player.face_shock()
    show robin_bus_sex_layered with dissolve
    pcm "Wow... Okay then. Not something I expected to see."
    pcm "Knowing that slut though, she is loving it so no need to try and help her."
    pcm "Yeah, she is loving it."
    $ robin.have_sex(busgroper)
    "I stand there watching [robin.name] getting fucked while I wait for my stop to come."
    hide robin_bus_grope_behind with dissolve
    jump bus_travel_end

label random_event_bus_robin_6:
    $ player.face_shock()
    show robin_bus_grope_front with dissolve
    pc "Oh? Err. Hey?"
    robin.name "Oh [name]! Hey!"
    pc "See you are having fun."
    robin.name "Err, yeah..."
    pc "Right then. Enjoy."
    robin.name "I will!"
    hide robin_bus_grope_behind
    jump bus_travel_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
