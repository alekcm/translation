image robin_againstwall_man_base_layer:
    "robin_againstwall_man_base"
    npc_skin_base_colour_transform()
image robin_againstwall_man_shad_layer:
    "robin_againstwall_man_shad"
    npc_skin_shad_colour_transform()

image robin_againstwall = LayeredImageProxy("robin_againstwall_layered", Transform(align=(0.7, 0.0)))

layeredimage robin_againstwall_layered:
    if loc_cur.loc_type == "tile":
        "robin_againstwall_bg_tile"
    else:
        "robin_againstwall_bg_grass"

    always "robin_againstwall_base"
    always "robin_againstwall_man_base_layer"
    always "robin_againstwall_man_shad_layer"

    always "robin_againstwall_frame"   
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
