label random_event_generic_dirty:
    $ player.add_mood(-5)
    jump expression WeightedChoice([
    ("random_event_generic_dirty_1", 100),
    ("random_event_generic_dirty_2", If (loc_cur.population >= 2, 100, 0)),
    
    
    
    
    
    
    ])

label random_event_generic_dirty_1:
    $ player.face_worried()
    $ dialouge = renpy.random.choice([
    "Fuck, I really need a shower.",
    "Ugh! I stink.",
    "I smell. I need to shower."
    ])
    pcm "[dialouge]"
    jump travel

label random_event_generic_dirty_2:
    $ dialouge = renpy.random.choice([
    "SMEEEELLYYYY.",
    "UGH! Stinkin' whore!",
    "Dirty bitch! Take some pride in yourself.",
    "Ya smelly bitch!"
    ])
    man "[dialouge]"
    $ player.face_worried()
    $ dialouge = renpy.random.choice([
    "Fuck!",
    "Ugh!",
    "..."
    ])
    pcm "[dialouge]"
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
