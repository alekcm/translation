image pub_dani_spitroast_pc_main_base_layer:
    "pub_dani_spitroast_pc_main_base"
    skin_base_colour_transform()
image pub_dani_spitroast_pc_main_shad_layer:
    "pub_dani_spitroast_pc_main_shad"
    skin_shad_colour_transform()

image pub_dani_spitroast_pc_lipstick_layer:
    "pub_dani_spitroast_pc_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))

image pub_dani_spitroast_pc_freckles_layer:
    "pub_dani_spitroast_pc_freckles"
    skin_shad_colour_transform()

image pub_dani_spitroast_pc_eyeshad_layer:
    "pub_dani_spitroast_pc_eyeshad"
    accessories_primary_colour_transform("eyeshadow", If (acc.makeup_on and acc.eyeshadow,0.6,0))

image pub_dani_spitroast_pc_eye_iris_layer:
    "pub_dani_spitroast_pc_eye_iris"
    eye_colour_transform()

image pub_dani_spitroast_pc_eye_eyeliner_layer:
    "pub_dani_spitroast_pc_eye_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")

image pub_dani_spitroast_pc_brow_layer:
    "pub_dani_spitroast_pc_brow"
    hair_colour_transform()
image pub_dani_spitroast_pc_hair_front_layer:
    get_hair_front_cg_filename("pub_dani_spitroast_pc_hair_front")
    hair_colour_transform()

image pub_dani_spitroast_man_penis_base_layer:
    "pub_dani_spitroast_man_penis_base"
    npc_skin_base_colour_transform()
image pub_dani_spitroast_man_penis_shad_layer:
    "pub_dani_spitroast_man_penis_shad"
    npc_skin_shad_colour_transform()

image pub_dani_spitroast_man_behind_base_layer:
    "pub_dani_spitroast_man_behind_base"
    npc2_skin_base_colour_transform()
image pub_dani_spitroast_man_behind_shad_layer:
    "pub_dani_spitroast_man_behind_shad"
    npc2_skin_shad_colour_transform()

image pub_dani_spitroast = LayeredImageProxy("pub_dani_spitroast_layered", Transform(align=(0.8, 0.0)))

layeredimage pub_dani_spitroast_layered:

    always "pub_dani_spitroast_bg"
    always "pub_dani_spitroast_man_penis_base_layer"
    always "pub_dani_spitroast_man_penis_shad_layer"

    group pc_group:
        attribute pc "pub_dani_spitroast_pc"
        attribute no_pc default null

    group man_behind_g:
        attribute man_behind "pub_dani_spitroast_man_behind_base_layer"
        attribute man_behind "pub_dani_spitroast_man_behind_shad_layer"
        attribute man_behind "pub_dani_spitroast_man_behind_col"

        attribute no_man default null

    always "pub_dani_spitroast_frame"

layeredimage pub_dani_spitroast_pc:
    always "pub_dani_spitroast_pc_main_base_layer"
    always "pub_dani_spitroast_pc_main_shad_layer"
    always "pub_dani_spitroast_pc_main_col"
    always "pub_dani_spitroast_pc_lipstick_layer"
    if skin_effect.face:
        "pub_dani_spitroast_pc_freckles_layer"
    always "pub_dani_spitroast_pc_eyeshad_layer"
    always "pub_dani_spitroast_pc_eye_iris_layer"
    always "pub_dani_spitroast_pc_eye_eye"
    always "pub_dani_spitroast_pc_eye_eyeliner_layer"
    always "pub_dani_spitroast_pc_brow_layer"
    always "pub_dani_spitroast_pc_hair_front_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
