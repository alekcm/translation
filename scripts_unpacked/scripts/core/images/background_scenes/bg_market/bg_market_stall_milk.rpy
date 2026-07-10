image bg_market_stall_milk_scene:
    get_background_filename("market_stall_milk")

layeredimage bg_market_stall_milk_people_hucow1:
    always "bg_market_stall_milk_people_maid1_base"
    if hucow.heavy_preg:
        "bg_market_stall_milk_people_maid1_preg2"
    elif hucow.showing:
        "bg_market_stall_milk_people_maid1_preg1"

layeredimage bg_market_stall_milk_people_hucow2:
    always "bg_market_stall_milk_people_maid2_base"
    if hucow.heavy_preg:
        "bg_market_stall_milk_people_maid2_preg2"
    elif hucow.showing:
        "bg_market_stall_milk_people_maid2_preg1"

layeredimage bg_market_stall_milk_layer:

    always:
        "bg_market_stall_milk_scene"

    if hucow_here() and hucow.hour_number > 5 and not renpy.showing("hucow"):
        "bg_market_stall_milk_people_hucow1"
    elif hucow_here() and not renpy.showing("hucow"):
        "bg_market_stall_milk_people_hucow2"

image bg_market_stall_milk:
    "bg_market_stall_milk_layer"
    bg_tint_transform()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
