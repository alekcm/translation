layeredimage haven_spitroast:

    if loc_cur == loc_haven_bed:
        "haven_spitroast_bg_bunk"
    else:
        "haven_spitroast_bg_room"


    always:
        "haven_spitroast_base"

    if c.socks:
        "haven_spitroast_clothes"
    if player.pregnancy == 1:
        "haven_spitroast_belly_1"
    elif player.pregnancy == 2:
        "haven_spitroast_belly_2"
    elif player.pregnancy == 3:
        "haven_spitroast_belly_3"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
