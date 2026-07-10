image robin_doubleblow_man_blow_base_layer:
    "robin_doubleblow_man_blow_base"
    npc_skin_base_colour_transform()
image robin_doubleblow_man_blow_shad_layer:
    "robin_doubleblow_man_blow_shad"
    npc_skin_shad_colour_transform()
image robin_doubleblow_man_mast_base_layer:
    "robin_doubleblow_man_mast_base"
    npc2_skin_base_colour_transform()
image robin_doubleblow_man_mast_shad_layer:
    "robin_doubleblow_man_mast_shad"
    npc2_skin_shad_colour_transform()

image robin_doubleblow = LayeredImageProxy("robin_doubleblow_layered", Transform(align=(0.7, 0.0)))

layeredimage robin_doubleblow_layered:
    always "robin_doubleblow_bg"
    always "robin_doubleblow_man_blow_base_layer"
    always "robin_doubleblow_man_blow_shad_layer"
    always "robin_doubleblow_man_mast_base_layer"
    always "robin_doubleblow_man_mast_shad_layer"
    always "robin_doubleblow_robin_base"

    group makeup:
        attribute nomakeup default null
        attribute makeup "robin_doubleblow_robin_makeup"

    group eyes:
        attribute down default "robin_doubleblow_robin_eye_down"
        attribute front "robin_doubleblow_robin_eye_front"

    group outfit:
        attribute nude default null
        attribute bimbo "robin_doubleblow_robin_bimbo"
        attribute slut "robin_doubleblow_robin_slut"

    always if_any "makeup" "robin_doubleblow_robin_hair_pink"
    always if_not "makeup" "robin_doubleblow_robin_hair_norm" 

    always "robin_doubleblow_frame"   
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
