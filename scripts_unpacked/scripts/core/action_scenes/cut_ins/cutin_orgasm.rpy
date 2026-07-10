image cutin_orgasm1_pc_base_layer:
    "cutin_orgasm1_pc_base"
    skin_base_colour_transform()
image cutin_orgasm1_pc_shad_layer:
    "cutin_orgasm1_pc_shad"
    skin_shad_colour_transform()

image cutin_orgasm1_pc_hair_back_layer:
    "cutin_orgasm1_pc_hair_back"
    hair_colour_transform()
image cutin_orgasm1_pc_hair_front_layer:
    "cutin_orgasm1_pc_hair_front"
    hair_colour_transform()
image cutin_orgasm1_pc_brow_layer:
    "cutin_orgasm1_pc_brow"
    hair_colour_transform()

image cutin_orgasm1_pc_iris_layer:
    "cutin_orgasm1_pc_iris"
    eye_colour_transform()
image cutin_orgasm1_pc_lipstick_layer:
    "cutin_orgasm1_pc_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and acc.lipstick,1,0))

image cutin_orgasm1 = LayeredImageProxy("cutin_orgasm1_layerd", Transform(xalign = (0.00)))

layeredimage cutin_orgasm1_layerd:
    always "cutin_orgasm1_bg"

    always "cutin_orgasm1_pc_hair_back_layer"
    always "cutin_orgasm1_pc_base_layer"
    always "cutin_orgasm1_pc_shad_layer"
    always "cutin_orgasm1_pc_face"

    always "cutin_orgasm1_pc_brow_layer"
    always "cutin_orgasm1_pc_iris_layer"
    always "cutin_orgasm1_pc_lipstick_layer"

    always "cutin_orgasm1_pc_lines"

    always "cutin_orgasm1_pc_hair_front_layer"

    always "cutin_orgasm1_frame"





image cutin_orgasm2_pc_base_layer:
    "cutin_orgasm2_pc_base"
    skin_base_colour_transform()
image cutin_orgasm2_pc_shad_layer:
    "cutin_orgasm2_pc_shad"
    skin_shad_colour_transform()

image cutin_orgasm2_pc_hair_layer:
    "cutin_orgasm2_pc_hair"
    hair_colour_transform()

image cutin_orgasm2_pc_lipstick_layer:
    "cutin_orgasm2_pc_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and acc.lipstick,1,0))
image cutin_orgasm2_pc_eyeshadow_layer:
    "cutin_orgasm2_pc_eyeshadow"
    accessories_primary_colour_transform("eyeshadow", If (acc.makeup_on and acc.eyeshadow,0.6,0))
image cutin_orgasm2_pc_freckles_layer:
    "cutin_orgasm2_pc_freckles"
    skin_shad_colour_transform()

image cutin_orgasm2 = LayeredImageProxy("cutin_orgasm2_layerd", Transform(xalign = (0.00)))

layeredimage cutin_orgasm2_layerd:
    always "cutin_orgasm2_bg"


    always "cutin_orgasm2_pc_base_layer"
    always "cutin_orgasm2_pc_shad_layer"
    if skin_effect.face:
        "cutin_orgasm2_pc_freckles_layer"
    always "cutin_orgasm2_pc_col"

    always "cutin_orgasm2_pc_hair_layer"
    always "cutin_orgasm2_pc_lipstick_layer"
    always "cutin_orgasm2_pc_eyeshadow_layer"

    always "cutin_orgasm2_pc_lines"


    always "cutin_orgasm2_frame"






image cutin_orgasm3_pc_base_layer:
    "cutin_orgasm3_pc_base"
    skin_base_colour_transform()
image cutin_orgasm3_pc_shad_layer:
    "cutin_orgasm3_pc_shad"
    skin_shad_colour_transform()

image cutin_orgasm3_pc_hair_layer:
    "cutin_orgasm3_pc_hair"
    hair_colour_transform()

image cutin_orgasm3_pc_lipstick_layer:
    "cutin_orgasm3_pc_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and acc.lipstick,1,0))
image cutin_orgasm3_pc_eyeshadow_layer:
    "cutin_orgasm3_pc_eyeshadow"
    accessories_primary_colour_transform("eyeshadow", If (acc.makeup_on and acc.eyeshadow,0.6,0))
image cutin_orgasm3_pc_freckles_layer:
    "cutin_orgasm3_pc_freckles"
    skin_shad_colour_transform()

image cutin_orgasm3 = LayeredImageProxy("cutin_orgasm3_layerd", Transform(xalign = (0.00)))

layeredimage cutin_orgasm3_layerd:
    always "cutin_orgasm3_bg"


    always "cutin_orgasm3_pc_base_layer"
    always "cutin_orgasm3_pc_shad_layer"
    always "cutin_orgasm3_pc_col"

    always "cutin_orgasm3_pc_hair_layer"
    always "cutin_orgasm3_pc_lipstick_layer"
    always "cutin_orgasm3_pc_eyeshadow_layer"

    always "cutin_orgasm3_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
