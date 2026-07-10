



image cutin_ass_pc_base_layer:
    "cutin_ass_pc_base"
    skin_base_colour_transform()
image cutin_ass_pc_shad_layer:
    "cutin_ass_pc_shad"
    skin_shad_colour_transform()


image cutin_ass_penis_base_layer:
    "cutin_ass_penis_base"
    npc_skin_base_colour_transform()
image cutin_ass_penis_shad_layer:
    "cutin_ass_penis_shad"
    npc_skin_shad_colour_transform()


image cutin_ass = LayeredImageProxy("cutin_ass_layerd", Transform(xalign = (1.00)))

layeredimage cutin_ass_layerd:
    always "cutin_ass_bg"

    always "cutin_ass_pc_base_layer"
    always "cutin_ass_pc_shad_layer"

    always "cutin_ass_penis_base_layer"
    always "cutin_ass_penis_shad_layer"
    always "cutin_ass_cum"

    always "cutin_ass_frame"





image cutin_mouth_pc_base_layer:
    "cutin_mouth_pc_base"
    skin_base_colour_transform()
image cutin_mouth_pc_shad_layer:
    "cutin_mouth_pc_shad"
    skin_shad_colour_transform()
image cutin_mouth_pc_lipstick_layer:
    "cutin_mouth_pc_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image cutin_mouth_pc_freckles_layer:
    "cutin_mouth_pc_freckles"
    skin_shad_colour_transform()
image cutin_mouth_pc_eyeshadow_layer:
    "cutin_mouth_pc_eyeshadow"
    accessories_primary_colour_transform("eyeshadow", If (acc.makeup_on and acc.eyeshadow,0.6,0))
image cutin_mouth_pc_hair_layer:
    "cutin_mouth_pc_hair"
    hair_colour_transform()


image cutin_mouth_penis_base_layer:
    "cutin_mouth_penis_base"
    npc_skin_base_colour_transform()
image cutin_mouth_penis_shad_layer:
    "cutin_mouth_penis_shad"
    npc_skin_shad_colour_transform()


image cutin_mouth = LayeredImageProxy("cutin_mouth_layerd", Transform(xalign = (1.00)))

layeredimage cutin_mouth_layerd:
    always "cutin_mouth_bg"

    always "cutin_mouth_pc_base_layer"
    always "cutin_mouth_pc_shad_layer"
    always "cutin_mouth_pc_lipstick_layer"
    if skin_effect.face:
        "cutin_mouth_pc_freckles_layer"
    always "cutin_mouth_pc_eyeshadow_layer"
    always "cutin_mouth_pc_hair_layer"

    always "cutin_mouth_penis_base_layer"
    always "cutin_mouth_penis_shad_layer"
    always "cutin_mouth_main_col"

    always "cutin_mouth_frame"





image cutin_face_pc_base_layer:
    "cutin_face_pc_base"
    skin_base_colour_transform()
image cutin_face_pc_shad_layer:
    "cutin_face_pc_shad"
    skin_shad_colour_transform()
image cutin_face_pc_lipstick_layer:
    "cutin_face_pc_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image cutin_face_pc_freckles_layer:
    "cutin_face_pc_freckles"
    skin_shad_colour_transform()
image cutin_face_pc_eyeshadow_layer:
    "cutin_face_pc_eyeshadow"
    accessories_primary_colour_transform("eyeshadow", If (acc.makeup_on and acc.eyeshadow,0.6,0))
image cutin_face_pc_hair_layer:
    "cutin_face_pc_hair"
    hair_colour_transform()


image cutin_face_penis_base_layer:
    "cutin_face_penis_base"
    npc_skin_base_colour_transform()
image cutin_face_penis_shad_layer:
    "cutin_face_penis_shad"
    npc_skin_shad_colour_transform()


image cutin_face = LayeredImageProxy("cutin_face_layerd", Transform(xalign = (1.00)))

layeredimage cutin_face_layerd:
    always "cutin_face_bg"

    always "cutin_face_pc_base_layer"
    always "cutin_face_pc_shad_layer"
    always "cutin_face_pc_lipstick_layer"
    if skin_effect.face:
        "cutin_face_pc_freckles_layer"
    always "cutin_face_pc_eyeshadow_layer"
    always "cutin_face_pc_hair_layer"

    always "cutin_face_penis_base_layer"
    always "cutin_face_penis_shad_layer"
    always "cutin_face_main_col"

    always "cutin_face_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
