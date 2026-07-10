label loc_checkpoint_junk_2_loiter:
    $ walk(loc_junk_2)
    jump jaylee_talk_picker
label loc_checkpoint_junk_trailer_loiter:
    $ walk(loc_junk_trailer)
    jump jaylee_talk_picker
label loc_checkpoint_junk_office_loiter:
    $ walk(loc_junk_office)
    jump junkyard_ash_loiter


label dis_checkpoint_loiter_tombola:
    $ rand_choice = WeightedChoice([
    ("loc_checkpoint_junk_2_loiter", If (can_loiter(loc_junk_2) and jaylee_here(loc_junk_2), 100, 0)),
    ("loc_checkpoint_junk_trailer_loiter", If (can_loiter(loc_junk_trailer) and jaylee_here(loc_junk_trailer), 100, 0)),
    ("loc_checkpoint_junk_office_loiter", If (can_loiter(loc_junk_office) and ashon_here(loc_junk_office), 25, 0)),
    ("loc_junk_1_loiter", If (can_loiter(loc_junk_1), 25, 0)),
    ("loc_checkpoint_loiter", 2),
    ])
    jump expression rand_choice

label loc_checkpoint_loiter:
    $ walk(loc_checkpoint)
    "I hang around the checkpoint just watching whatever is going on and killing time."
    $ loiter()
    jump travel_arrival

label loc_junk_1_loiter:
    $ walk(loc_junk_1)
    "I hang around junk yard and with little to actually do I just wander around killing time."
    $ loiter()
    jump travel_arrival
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
