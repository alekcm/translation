layeredimage jaylee_body_layered:
    always "jaylee_base"
    if jaylee.days_pregnant > (global_pregnancy_length * 0.75):
        "jaylee_base_preg2"
    elif jaylee.days_pregnant > (global_pregnancy_length * 0.3):
        "jaylee_base_preg1"

layeredimage jaylee_outfit_scav:
    if jaylee.days_pregnant > (global_pregnancy_length * 0.75):
        "jaylee_outfit_scav_2"
    elif jaylee.days_pregnant > (global_pregnancy_length * 0.3):
        "jaylee_outfit_scav_1"
    else:
        "jaylee_outfit_scav_0"

layeredimage jaylee_outfit_nude:
    always "jaylee_breasts"
    always "jaylee_hair"

layeredimage jaylee_outfit_underwear:
    always "jaylee_breasts"
    always "jaylee_hair"
    always "jaylee_outfit_underwear_base"

layeredimage jaylee_outfit_standard:
    if loc(loc_junk_trailer_bathroom):
        "jaylee_outfit_nude"
    elif t.time_from_to(23.00,07.59) and loc([loc_junk_trailer]):
        "jaylee_outfit_underwear"
    else:
        "jaylee_outfit_scav"

layeredimage jaylee:
    at sprite_highlight("jaylee")
    always "jaylee_body_layered"
    group outfit auto:
        attribute standard default


    group face auto:
        attribute neutral default
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
