layeredimage betty_base_layered:
    always "betty_base"
    if betty.heavy_preg:
        "betty_preg_2"
    elif betty.showing:
        "betty_preg_1"

layeredimage betty_outfit_uni_layer:
    if betty.heavy_preg:
        "betty_outfit_uni_2"
    elif betty.showing:
        "betty_outfit_uni_1"
    else:
        "betty_outfit_uni_0"

layeredimage betty_outfit_under_layer:
    if betty.heavy_preg:
        "betty_outfit_under_2"
    else:
        "betty_outfit_under_0"

layeredimage betty:
    at sprite_highlight("betty")
    always "betty_base_layered"
    always "betty_tattoo"
    group face auto:
        attribute neutral default
    group outfit:
        attribute uni default "betty_outfit_uni_layer"
        attribute under "betty_outfit_under_layer"
        attribute nude "betty_outfit_nude"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
