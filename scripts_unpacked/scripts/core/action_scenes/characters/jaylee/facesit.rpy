image jaylee_facesit_pc_head_base_layer:
    "jaylee_facesit_pc_head_base"
    skin_base_colour_transform()
image jaylee_facesit_pc_head_shad_layer:
    "jaylee_facesit_pc_head_shad"
    skin_shad_colour_transform()

image jaylee_facesit_pc_head_freckles_layer:
    "jaylee_facesit_pc_head_freckles"
    skin_shad_colour_transform()
image jaylee_facesit_pc_head_lipstick_layer:
    "jaylee_facesit_pc_head_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image jaylee_facesit_pc_brow_layer:
    "jaylee_facesit_pc_brow"
    hair_colour_transform()
image jaylee_facesit_pc_hair_layer:
    "jaylee_facesit_pc_hair"
    hair_colour_transform()
image jaylee_facesit_pc_nails_layer:
    "jaylee_facesit_pc_nails"
    accessories_primary_colour_transform("nails", If(acc.nails and acc.makeup_on, 1, 0))

image jaylee_facesit_pc_eye_eyeshad_open_layer:
    "jaylee_facesit_pc_eye_eyeshad_open"
    accessories_primary_colour_transform("eyeshadow", If (acc.makeup_on and acc.eyeshadow,0.6,0))
image jaylee_facesit_pc_eye_eyeshad_closed_layer:
    "jaylee_facesit_pc_eye_eyeshad_closed"
    accessories_primary_colour_transform("eyeshadow", If (acc.makeup_on and acc.eyeshadow,0.6,0))

image jaylee_facesit_pc_eye_eyeliner_closed_layer:
    "jaylee_facesit_pc_eye_eyeliner_closed_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image jaylee_facesit_pc_eye_eyeliner_open_layer:
    "jaylee_facesit_pc_eye_eyeliner_open_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")

image jaylee_facesit_pc_eye_iris_layer:
    "jaylee_facesit_pc_eye_iris"
    eye_colour_transform()

image jaylee_facesit = LayeredImageProxy("jaylee_facesit_layered", Transform(align=(0.8, 0.0)))

layeredimage jaylee_facesit_layered:
    always "jaylee_facesit_bg"

    always "jaylee_facesit_jaylee"

    always "jaylee_facesit_pc_head_base_layer"
    always "jaylee_facesit_pc_head_shad_layer"
    always "jaylee_facesit_pc_head_col"
    always "jaylee_facesit_pc_nails_layer"
    if skin_effect.face:
        "jaylee_facesit_pc_head_freckles_layer"
    always "jaylee_facesit_pc_head_lipstick_layer"
    always "jaylee_facesit_pc_brow_layer"
    always "jaylee_facesit_pc_hair_layer"

    group eye:
        attribute closed default "jaylee_facesit_pc_eye_eyeshad_closed_layer"
        attribute closed default "jaylee_facesit_pc_eye_eyeliner_closed_layer"

        attribute open "jaylee_facesit_pc_eye_eyeshad_open_layer"
        attribute open "jaylee_facesit_pc_eye_iris_layer"
        attribute open "jaylee_facesit_pc_eye_eye"
        attribute open "jaylee_facesit_pc_eye_eyeliner_open_layer"

    always "jaylee_facesit_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
