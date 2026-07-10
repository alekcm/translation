layeredimage ali_body_layered:
    always "ali_base"
    if ali.heavy_preg:
        "ali_base_preg_2"
    elif ali.showing:
        "ali_base_preg_1"

layeredimage ali_outfit_mech:
    if ali.heavy_preg:
        "ali_outfit_mech_preg_2"
    elif ali.showing:
        "ali_outfit_mech_preg_1"
    else:
        "ali_outfit_mech_preg_0"

layeredimage ali_outfit_under:
    if ali.heavy_preg:
        "ali_outfit_under_preg_2"
    elif ali.showing:
        "ali_outfit_under_preg_1"
    else:
        "ali_outfit_under_preg_0"

layeredimage ali:
    at sprite_highlight("ali")
    always "ali_body_layered"

    group outfit auto:
        attribute mech default
        attribute nude null
        attribute under
    group face auto:
        attribute neutral default
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
