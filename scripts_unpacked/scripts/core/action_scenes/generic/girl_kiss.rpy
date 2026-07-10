image girl_kiss_pc_face_base_layer:
    "girl_kiss_pc_face_base"
    skin_base_colour_transform()
image girl_kiss_pc_face_shad_layer:
    "girl_kiss_pc_face_shad"
    skin_shad_colour_transform()

image girl_kiss_pc_eyeshad_layer:
    "girl_kiss_pc_eyeshad"
    accessories_primary_colour_transform("eyeshadow", If (acc.makeup_on and acc.eyeshadow,0.6,0))

image girl_kiss_pc_freckles_layer:
    "girl_kiss_pc_face_freckles"
    skin_shad_colour_transform()
image girl_kiss_pc_lipstick_layer:
    "girl_kiss_pc_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image girl_kiss_pc_brow_layer:
    "girl_kiss_pc_brow"
    hair_colour_transform()

image girl_kiss_pc_eye_eyeliner_open_layer:
    "girl_kiss_pc_eye_eyeliner_open_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image girl_kiss_pc_eye_eyeliner_closed_layer:
    "girl_kiss_pc_eye_eyeliner_closed_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image girl_kiss_pc_eye_iris_layer:
    "girl_kiss_pc_eye_iris"
    eye_colour_transform()

image girl_kiss_pc_hair_layer:
    get_hair_front_cg_filename("girl_kiss_pc_hair")
    hair_colour_transform()

image jaylee_kiss = LayeredImageProxy("jaylee_kiss_layered", Transform(align=(0.8, 0.0)))

layeredimage jaylee_kiss_layered:
    always "girl_kiss_bg"

    always "girl_kiss_pc_face_base_layer"
    always "girl_kiss_pc_face_shad_layer"
    always "girl_kiss_pc_face_blush"
    always "girl_kiss_pc_eyeshad_layer"
    if skin_effect.face:
        "girl_kiss_pc_freckles_layer"
    always "girl_kiss_pc_lipstick_layer"
    always "girl_kiss_pc_brow_layer"

    group pc_eye:
        attribute pc_open default:
            "girl_kiss_pc_eye_iris_layer"
        attribute pc_open default:
            "girl_kiss_pc_eye_eye"
        attribute pc_open default:
            "girl_kiss_pc_eye_eyeliner_open_layer"

        attribute pc_closed:
            "girl_kiss_pc_eye_eyeliner_closed_layer"

    always "girl_kiss_jaylee_hand"
    always "girl_kiss_pc_hair_layer"

    always "girl_kiss_jaylee_head"
    group jaylee_eye:
        attribute jaylee_closed default:
            "girl_kiss_jaylee_eye_closed"
        attribute jaylee_open:
            "girl_kiss_jaylee_eye_open"

    group jaylee_hair:
        attribute hat default:
            "girl_kiss_jaylee_hat"
        attribute hair:
            "girl_kiss_jaylee_hair"

    always "girl_kiss_frame"

image robin_kiss = LayeredImageProxy("robin_kiss_layered", Transform(align=(0.8, 0.0)))

layeredimage robin_kiss_layered:
    always "girl_kiss_bg"

    always "girl_kiss_pc_face_base_layer"
    always "girl_kiss_pc_face_shad_layer"
    always "girl_kiss_pc_face_blush"
    always "girl_kiss_pc_eyeshad_layer"
    if skin_effect.face:
        "girl_kiss_pc_freckles_layer"
    always "girl_kiss_pc_lipstick_layer"
    always "girl_kiss_pc_brow_layer"

    group pc_eye:
        attribute pc_open default:
            "girl_kiss_pc_eye_iris_layer"
        attribute pc_open default:
            "girl_kiss_pc_eye_eye"
        attribute pc_open default:
            "girl_kiss_pc_eye_eyeliner_open_layer"

        attribute pc_closed:
            "girl_kiss_pc_eye_eyeliner_closed_layer"

    always "girl_kiss_robin_hand"
    group makeup:
        attribute bimbo "girl_kiss_robin_hand_makeup"
        attribute normal default null
    always "girl_kiss_pc_hair_layer"

    always "girl_kiss_robin_head"
    group makeup:
        attribute bimbo "girl_kiss_robin_makeup"
        attribute normal default null
    group jaylee_eye:
        attribute robin_closed default "girl_kiss_jaylee_eye_closed"
        attribute robin_open "girl_kiss_robin_eye_open"

    group makeup:
        attribute normal default "girl_kiss_robin_hair"
        attribute bimbo "girl_kiss_robin_hair_bimbo"

    always "girl_kiss_frame"

image dani_kiss = LayeredImageProxy("dani_kiss_layered", Transform(align=(0.8, 0.0)))

layeredimage dani_kiss_layered:
    always "girl_kiss_bg"

    always "girl_kiss_pc_face_base_layer"
    always "girl_kiss_pc_face_shad_layer"
    always "girl_kiss_pc_face_blush"
    always "girl_kiss_pc_eyeshad_layer"
    if skin_effect.face:
        "girl_kiss_pc_freckles_layer"
    always "girl_kiss_pc_lipstick_layer"
    always "girl_kiss_pc_brow_layer"

    group pc_eye:
        attribute pc_open default:
            "girl_kiss_pc_eye_iris_layer"
        attribute pc_open default:
            "girl_kiss_pc_eye_eye"
        attribute pc_open default:
            "girl_kiss_pc_eye_eyeliner_open_layer"

        attribute pc_closed:
            "girl_kiss_pc_eye_eyeliner_closed_layer"

    always "girl_kiss_dani_hand"

    always "girl_kiss_pc_hair_layer"

    always "girl_kiss_dani_head"

    group dani_eye:
        attribute dani_closed default "girl_kiss_jaylee_eye_closed"
        attribute dani_open "girl_kiss_dani_eye_open"
    always "girl_kiss_dani_hair"

    always "girl_kiss_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
