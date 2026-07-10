image robin_onback_man_base_layer:
    "robin_onback_man_base"
    npc_skin_base_colour_transform()
image robin_onback_man_shad_layer:
    "robin_onback_man_shad"
    npc_skin_shad_colour_transform()

image robin_onback = LayeredImageProxy("robin_onback_layered", Transform(align=(0.8, 0.0)))

layeredimage robin_onback_layered:
    always "robin_onback_base"
    group face:
        attribute oh default "robin_onback_face_oh"
        attribute pout "robin_onback_face_pout"
    always "robin_onback_man_base_layer"
    always "robin_onback_man_shad_layer"
    if robin.days_pregnant > (global_pregnancy_length * 0.3):
        "robin_onback_robin_belly"
    always "robin_onback_frame"   
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
