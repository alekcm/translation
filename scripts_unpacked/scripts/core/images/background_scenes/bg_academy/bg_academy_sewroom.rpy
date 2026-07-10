layeredimage bg_school_sewroom_frida_layer:
    always "bg_school_sewroom_people_frida_base"
    if frida.showing:
        "bg_school_sewroom_people_frida_preg"

layeredimage bg_school_sewroom_saskia_layer:
    always "bg_school_sewroom_people_saskia_base"
    if saskia.heavy_preg:
        "bg_school_sewroom_people_saskia_preg2"
    elif saskia.showing:
        "bg_school_sewroom_people_saskia_preg1"

layeredimage bg_school_sewroom_layered:
    always "bg_school_sewroom_scene"
    if saskia_here() and not renpy.showing("saskia"):
        "bg_school_sewroom_saskia_layer"
    if frida_here() and not renpy.showing("frida"):
        "bg_school_sewroom_frida_layer"

image bg_school_sewroom:
    "bg_school_sewroom_layered"
    bg_tint_transform()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
