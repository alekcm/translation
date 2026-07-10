label dis_home_loiter_tombola:
    $ rand_choice = WeightedChoice([
    ("loc_common_loiter", If(not loc_kitchen.locked, 100, 0)),
    ("loc_kitchen_loiter", If(not loc_kitchen.locked, 100, 0)),
    ("loc_bedroom_loiter", If(not loc_kitchen.locked, 100, 0)),
    ("robin_chat_loiter", If (not loc_kitchen.locked and robin_here([loc_common, loc_kitchen]), 200, 0)),
    ("robin_chat_room_loiter", If (robin_here(dis_home.locs) and loc_kitchen.locked, 200, 0)),
    ("loc_nowhere_loiter", 1)
    ])
    jump expression rand_choice

label loc_common_loiter:
    $ walk(loc_common)
    jump common_tv

label loc_kitchen_loiter:
    $ walk(loc_kitchen)
    "I hang around in the kitchen killing time and looking out the window."
    $ loiter()
    jump travel

label loc_bedroom_loiter:
    $ walk(loc_bedroom)
    "I hang around in my room just messing about and killing time."
    $ loiter()
    jump travel

label robin_chat_loiter:
    $ walk(robin_here(class_loc=True))
    jump robin_talk_picker

label loc_nowhere_loiter:
    "I don't have much to do so I just hang around killing time."
    $ loiter()
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
