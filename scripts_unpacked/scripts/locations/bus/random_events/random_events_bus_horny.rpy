label random_event_bus_horny:
    jump expression WeightedChoice([
    ("random_event_bus_horny_1", 100),
    ("random_event_bus_grope_2", 100),
    ("random_event_bus_grope_3", 100),
    ("random_event_bus_grope_4", 100),
    ])

label random_event_bus_horny_1:
    $ player.face_shy()
    pcm "..."
    pcm "Maybe I can relieve some tension in here."
    "I go over and stand between a bunch of guys."
    pcm "Hmmm..."
    $ player.grope(steal=True)
    pcm "Oh? Thought so."
    $ player.grope(steal=True)
    pcm "Mmmmm."
    jump random_event_bus_sex_stumble
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
