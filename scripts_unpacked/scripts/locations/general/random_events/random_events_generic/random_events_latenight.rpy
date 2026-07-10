label random_event_generic_latenight:
    $ player.add_mood(-5)
    jump expression WeightedChoice([
    ("random_event_generic_latenight_1", 500),
    ("random_event_generic_latenight_2", 100),
    ("random_event_generic_latenight_3", 100),
    ("random_event_generic_latenight_4", danger_weight()),
    
    
    
    
    ])

label random_event_generic_latenight_1:
    $ player.face_worried()
    $ dialouge = renpy.random.choice([
    "Fuck, I really don't like being out this late at night...",
    "I really should head home. I really hate being out this late.",
    "It's not safe to be out here while it's dark. I should go home."
    ])
    pcm "[dialouge]"
    jump travel

label random_event_generic_latenight_2:
    $ player.face_shock()
    pc "Ah!"
    pcm "The fuck was that?"
    $ player.face_worried()
    pcm "I should go home. I am jumping at shadows."
    jump travel

label random_event_generic_latenight_3:
    $ player.face_worried()
    pcm "Too dark I can't see. Are those people over there or just something else..."
    pcm "Ugh, it's just a bush..."
    jump travel

label random_event_generic_latenight_4:
    $ player.mug()
    pc "Ahh!"
    $ player.grope_end()
    "The guy runs off without saying anything."
    pcm "Fuck!"
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
