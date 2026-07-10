image robin_spitroast_man_blow_base_layer:
    "robin_spitroast_man_blow_base"
    npc_skin_base_colour_transform()
image robin_spitroast_man_blow_shad_layer:
    "robin_spitroast_man_blow_shad"
    npc_skin_shad_colour_transform()
image robin_spitroast_man_sex_base_layer:
    "robin_spitroast_man_sex_base"
    npc2_skin_base_colour_transform()
image robin_spitroast_man_sex_shad_layer:
    "robin_spitroast_man_sex_shad"
    npc2_skin_shad_colour_transform()

image robin_spitroast = LayeredImageProxy("robin_spitroast_layered", Transform(align=(0.9, 0.0)))

layeredimage robin_spitroast_layered:
    always "robin_spitroast_bg"
    always "robin_spitroast_man_blow_base_layer"
    always "robin_spitroast_man_blow_shad_layer"
    always "robin_spitroast_man_sex_base_layer"
    always "robin_spitroast_man_sex_shad_layer"
    always "robin_spitroast_robin_base"

    group makeup:
        attribute nomakeup default null
        attribute makeup "robin_spitroast_robin_makeup"

    group eyes:
        attribute up default "robin_spitroast_robin_eye_up"
        attribute front "robin_spitroast_robin_eye_front"

    group outfit:
        attribute nude default null
        attribute bimbo "robin_spitroast_robin_outfit_bimbo"
        attribute slut "robin_spitroast_robin_outfit_slut"

    always if_any "makeup" "robin_spitroast_robin_hair_pink"
    always if_not "makeup" "robin_spitroast_robin_hair_norm" 

    always "robin_spitroast_frame"   
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
