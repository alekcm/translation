label haven_storage_join:
    jump expression WeightedChoice([
    ("random_event_haven_normal_1", 100),
    ("random_event_haven_normal_2", 100),
    ])

label random_event_haven_storage_1:
    show havman at right1 with dissolve
    $ player.face_worried()
    hav "Ah, didn't know someone was in here."
    pc "Err..."
    hav "No matter, you can help me grab some of those boxes and stick em by the fire barrel."
    $ player.face_normal()
    pc "Err, sure."
    pause 0.5
    $ walk(loc_haven_lounge)
    pause 0.5  
    hav "There we go, just stick em down there."
    pc "Ok."
    hav "Cheers."
    hide havman with dissolve
    $ walk(loc_haven_lounge)
    jump travel

label random_event_haven_storage_2:
    show havman at right1 with dissolve
    $ player.face_worried()
    hav "Huh, what you doing in here?"
    pc "Err..."
    show haven_grope with dissolve
    hav "Doesn't look like you are grabbing wood for the fire an' no other reason t' be in 'ere."
    pc "What do you care?"
    hav "Hmm, I don't care I suppose."
    hav "Whatever, but if you are looking to hide your stash 'ere, it's a bad idea. Too many folk in 'ere all the time."
    hav "Lost stuff myself putting it away in 'ere."
    pc "Ok, thanks?"
    hav "Sure."
    hide haven_grope with dissolve
    hav "See ya."
    hide havman with dissolve
    pcm "..."
    $ player.face_normal()
    pcm "Bit handsy, but at least that was all."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
