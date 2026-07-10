label dis_residential_loiter_tombola:
    jump expression WeightedChoice([
    ("dani_chat_loiter", If (dani_here(loc_stairwell) and not dani.hate, 200, 0)),
    ("dani_chat_loiter", If (dani_here(loc_bedroom_dani) and loc_bedroom_dani.unlocked and not dani.hate and not dis(dis_park), 200, 0)),
    ("robin_chat_loiter", If (robin_here(dis_home.locs) and loc_kitchen.locked, 200, 0)),
    ("loc_park_loiter_arrive", 50),
    ])

label loc_park_loiter_arrive:
    if not loc(loc_park):
        $ walk(loc_park)
    jump loc_park_loiter

label dani_chat_loiter:
    $ walk(dani_here(class_loc=True))
    jump dani_talk_picker

label robin_chat_room_loiter:
    $ walk(loc_bedroom_robin)
    jump robin_talk_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
