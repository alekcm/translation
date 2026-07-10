image bg_market_stall_needle_scene:
    get_background_filename("market_stall_needle")

layeredimage bg_market_stall_needle_people_saskia1:
    always "bg_market_stall_needle_people_saskia1_base"
    if saskia.heavy_preg:
        "bg_market_stall_needle_people_saskia1_preg2"
    elif saskia.showing:
        "bg_market_stall_needle_people_saskia1_preg1"

layeredimage bg_market_stall_needle_people_frida1:
    always "bg_market_stall_needle_people_frida1_base"
    if frida.heavy_preg:
        "bg_market_stall_needle_people_frida1_preg2"
    elif frida.showing:
        "bg_market_stall_needle_people_frida1_preg1"

layeredimage bg_market_stall_needle_layer:

    always:
        "bg_market_stall_needle_scene"

    if t.hour in workhours and girl_dummy_1.hour_number > 3:
        "bg_market_stall_needle_people_girl1"
    if t.hour in workhours and girl_dummy_2.hour_number > 3:
        "bg_market_stall_needle_people_girl2"
    if saskia_here() and saskia.hour_number > 5 and not renpy.showing("saskia"):
        "bg_market_stall_needle_people_saskia1"
    elif saskia_here() and not renpy.showing("saskia"):
        "bg_market_stall_needle_people_saskia2_base"

    if frida_here() and frida.hour_number > 5 and not renpy.showing("frida"):
        "bg_market_stall_needle_people_frida1"
    elif frida_here() and not renpy.showing("frida"):
        "bg_market_stall_needle_people_frida2_base"

image bg_market_stall_needle:
    "bg_market_stall_needle_layer"
    bg_tint_transform()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
