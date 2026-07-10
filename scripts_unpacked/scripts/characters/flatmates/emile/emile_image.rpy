layeredimage emile_base_layer:
    always "emile_base"
    if emile.heavy_preg:
        "emile_base_preg2"
    elif emile.showing:
        "emile_base_preg1"

layeredimage emile_dress_layer:
    always "emile_outfit_dress"
    if emile.heavy_preg:
        "emile_outfit_dress_preg2"
    elif emile.showing:
        "emile_outfit_dress_preg1"

layeredimage emile_casual_layer:
    always "emile_outfit_casual"
    if emile.heavy_preg:
        "emile_outfit_casual_preg2"
    elif emile.showing:
        "emile_outfit_casual_preg1"

layeredimage emile_pyjamas_layer:
    always "emile_outfit_pyjamas"
    if emile.heavy_preg:
        "emile_outfit_pyjamas_preg2"
    elif emile.showing:
        "emile_outfit_pyjamas_preg1"

layeredimage emile_suitshirt_layer:
    always "emile_outfit_suitshirt"
    if emile.heavy_preg:
        "emile_outfit_suitshirt_preg2"
    elif emile.showing:
        "emile_outfit_suitshirt_preg1"

layeredimage emile_suitvest_layer:
    always "emile_outfit_suitvest"
    if emile.heavy_preg:
        "emile_outfit_suitvest_preg2"
    elif emile.showing:
        "emile_outfit_suitvest_preg1"

layeredimage emile_swimwear_layer:
    if emile.heavy_preg:
        "emile_outfit_swimwear_preg2"
    else:
        "emile_outfit_swimwear"

layeredimage emile_swimweartopless_layer:
    always "emile_nude"
    if emile.heavy_preg:
        "emile_outfit_swimweartopless_preg2"
    else:
        "emile_outfit_swimweartopless"

layeredimage emile_underwear_layer:
    if emile.heavy_preg:
        "emile_outfit_underwear_preg2"
    elif emile.showing:
        "emile_outfit_underwear_preg1"
    else:
        "emile_outfit_underwear"

layeredimage emile_underwearsexy_layer:
    always "emile_nude"
    if emile.heavy_preg:
        "emile_outfit_underwearsexy_preg2"
    elif emile.showing:
        "emile_outfit_underwearsexy_preg1"
    else:
        "emile_outfit_underwearsexy"

layeredimage emile_outfit_standard:
    if emile_here(dis_home.locs) and (t.timeofday == "night" or t.hour in (6,7)) and not t.day == 1:
        "emile_pyjamas_layer"
    elif dis(dis_beach):
        "emile_swimwear_layer"
    elif (global_random_number % 2):
        "emile_dress_layer"
    else:
        "emile_casual_layer"
layeredimage emile:
    at sprite_highlight("emile")
    always "emile_base_layer"

    group outfit auto:
        attribute standard default:
            "emile_outfit_standard"
        attribute dress:
            "emile_dress_layer"
        attribute casual:
            "emile_casual_layer"
        attribute swim:
            "emile_swimwear_layer"
        attribute swim_topless:
            "emile_swimweartopless_layer"
        attribute pyjamas:
            "emile_pyjamas_layer"
        attribute suitshirt:
            "emile_suitshirt_layer"
        attribute suitvest:
            "emile_suitvest_layer"
        attribute underwear:
            "emile_underwear_layer"
        attribute underwearsexy:
            "emile_underwearsexy_layer"
        attribute nooutfit:
            "emile_nude"
        attribute nude:
            "emile_nude"

    group face auto:
        attribute neutral default
        attribute angry "emile_face_frown"

    always "emile_hair"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
