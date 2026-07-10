label dis_haven_loiter_tombola:
    $ rand_choice = WeightedChoice([
    ("loc_haven_bedroom_loiter", If (can_loiter(loc_haven_bedroom), 100, 0)),
    
    ("loc_haven_lounge_loiter", If (can_loiter(loc_haven_lounge), 100, 0)),
    ])
    jump expression rand_choice

label loc_haven_bed_loiter:
    $ walk(loc_haven_bed)
    jump haven_bed_listen_chainstart

label loc_haven_bedroom_loiter:
    $ walk(loc_haven_bedroom)
    show haven_wait with dissolve
    if haven_time_safe():
        pcm "Lot of girls around so will be pretty safe here."
        "I hang around and chat with the girls a little to kill some time."
    elif haven_time_danger():
        $ player.face_worried()
        pcm "Only guys here..."
        "I try and keep my head down and kill some time while keeping an eye over my shoulder."
    elif haven_time_empty():
        pcm "This place is deserted."
        "Since it's pretty quiet, I just hang around and try and kill some time."
    else:
        pcm "A fair few people in here."
        "I stick close to the girls and have a bit of chit chat to kill some time."
    $ loiter()
    hide haven_wait with dissolve
    jump travel_arrival

label loc_haven_lounge_loiter:
    $ walk(loc_haven_lounge)
    show haven_wait with dissolve
    if haven_time_danger():
        $ player.face_worried()
        pcm "Packed in here..."
        "I try and keep my head down and kill some time while keeping an eye over my shoulder."
    elif haven_time_empty():
        pcm "This place is deserted."
        "Since it's pretty quiet, I just hang around and try and kill some time."
    else:
        pcm "A few people in here."
        "I try and keep my head down and kill some time while keeping an eye over my shoulder."
    $ loiter()
    hide haven_wait with dissolve
    jump travel_arrival
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
