label loc_revel_market_loiter:
    $ walk(loc_market)
    jump market_wander
label loc_revel_pub_loiter:
    $ walk(loc_pub)
    jump pub_drink_start
label loc_revel_market_needle_loiter:
    $ walk(loc_market_stall_needle)
    jump saskia_frida_talk_picker


label dis_revel_loiter_tombola:
    $ rand_choice = WeightedChoice([
    ("loc_revel_market_loiter", If (can_loiter(loc_market), 50, 0)),
    ("loc_revel_market_needle_loiter", If (can_loiter(loc_market_stall_needle) and any([saskia_here(loc_market_stall_needle), frida_here(loc_market_stall_needle)]), 100, 0)),
    ("loc_revel_pub_loiter", If (can_loiter(loc_pub), If(player.mood <= 20, 150, 50), 0)),
    ])
    jump expression rand_choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
