layeredimage trixie_nude_layer:
    always "trixie_nude_breasts"
    if trixie.heavy_preg:
        "trixie_nude_preg2"
    elif trixie.showing:
        "trixie_nude_preg1"

layeredimage trixie_pub_layer:
    always "trixie_bar_base"
    if trixie.heavy_preg:
        "trixie_bar_preg2"
    elif trixie.showing:
        "trixie_bar_preg1"

layeredimage trixie:
    at sprite_highlight("trixie")
    always "trixie_base"

    group face auto:
        attribute neutral default

    always "trixie_hair"

    group outfit:
        attribute nude:
            "trixie_nude_layer"
        attribute pub default:
            "trixie_pub_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
