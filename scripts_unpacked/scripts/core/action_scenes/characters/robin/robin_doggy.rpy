
image robin_doggy_bg_plaster = "robin_doggy_bg_room"
image robin_doggy_bg_conc = "robin_doggy_bg_grass"
image robin_doggy_bg_tile = "robin_doggy_bg_room"
image robin_doggy_bg_layer:
    "robin_doggy_bg_" + loc_cur.loc_type

image robin_doggy_man_base_layer:
    "robin_doggy_man_base"
    npc_skin_base_colour_transform()
image robin_doggy_man_shad_layer:
    "robin_doggy_man_shad"
    npc_skin_shad_colour_transform()

image robin_doggy = LayeredImageProxy("robin_doggy_layered", Transform(align=(0.8, 0.0)))

layeredimage robin_doggy_layered:
    always "robin_doggy_bg_layer"
    always "robin_doggy_robin"
    always "robin_doggy_man_base_layer"
    always "robin_doggy_man_shad_layer"
    always "robin_doggy_frame"   
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
