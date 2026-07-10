layeredimage bg_bathroom_emile_layer:
    always "bg_bathroom_people_emile_base"
    if emile.heavy_preg:
        "bg_bathroom_people_emile_preg2"
    elif emile.showing:
        "bg_bathroom_people_emile_preg1"


layeredimage bg_bathroom_robin_layer:
    always "bg_bathroom_people_robin_base"
    if robin.heavy_preg:
        "bg_bathroom_people_robin_preg2"
    elif robin.showing:
        "bg_bathroom_people_robin_preg1"

layeredimage bg_bathroom_layer:
    always "bg_bathroom_scene"
    if emile_here() and not renpy.showing("emile"):
        "bg_bathroom_emile_layer"
    if robin_here() and not renpy.showing("robin"):
        "bg_bathroom_robin_layer"
    if emile_here() or robin_here():
        "bg_bathroom_effect_shower"

image bg_bathroom:
    "bg_bathroom_layer"
    bg_tint_transform()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
