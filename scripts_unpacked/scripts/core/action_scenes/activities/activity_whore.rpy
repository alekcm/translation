image activity_whore_smile_face_base_layer:
    "activity_whore_smile_face_base"
    skin_base_colour_transform()
image activity_whore_smile_face_shad_layer:
    "activity_whore_smile_face_shad"
    skin_shad_colour_transform()

image activity_whore_smile_brow_layer:
    "activity_whore_smile_brow"
    hair_colour_transform()
image activity_whore_smile_mouth_lipstick_layer:
    "activity_whore_smile_mouth_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image activity_whore_smile_eyeshadow_layer:
    "activity_whore_smile_eyeshad"
    accessories_primary_colour_transform("eyeshadow", If (acc.makeup_on and acc.eyeshadow,0.6,0))
image activity_whore_smile_freckles_layer:
    "activity_whore_smile_freckles"
    skin_shad_colour_transform()
image activity_whore_smile_blush_layer:
    "activity_whore_smile_blush"
    blush_opacity_transform()
image activity_whore_smile_writing_face_layer:
    "activity_whore_smile_writing_face"
    writing_transform("face")
image activity_whore_smile_writing_forehead_layer:
    "activity_whore_smile_writing_forehead"
    writing_transform("forehead")

image activity_whore_smile_eye_eyeliner_layer:
    "activity_whore_smile_eye_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image activity_whore_smile_eye_iris_layer:
    "activity_whore_smile_eye_iris"
    eye_colour_transform()

image activity_whore_smile_hair_back_bun_2 = "activity_whore_smile_hair_back_pony"
image activity_whore_smile_hair_back_bun_3 = "activity_whore_smile_hair_back_pony"
image activity_whore_smile_hair_back_bun_4 = "activity_whore_smile_hair_back_pony"
image activity_whore_smile_hair_back_pony_2 = "activity_whore_smile_hair_back_pony"
image activity_whore_smile_hair_back_pony_3 = "activity_whore_smile_hair_back_pony"
image activity_whore_smile_hair_back_pony_4 = "activity_whore_smile_hair_back_pony"
image activity_whore_smile_hair_back_pig_2 = "activity_whore_smile_hair_back_pony"

image activity_whore_smile_hair_back_layer:
    get_hair_back_cg_filename("activity_whore_smile_hair_back")
    hair_colour_transform()

image activity_whore_smile_hair_front_layer:
    get_hair_front_cg_filename("activity_whore_smile_hair_front")
    hair_colour_transform()

image activity_whore_smile = LayeredImageProxy("activity_whore_smile_layeredimage", Transform(align=(0.8, 0.0)))

layeredimage activity_whore_smile_layeredimage:
    always "activity_whore_smile_bg"
    always "activity_whore_smile_face_base_layer"
    always "activity_whore_smile_face_shad_layer"
    always "activity_whore_smile_brow_layer"
    always "activity_whore_smile_mouth_lipstick_layer"
    always "activity_whore_smile_mouth"
    always "activity_whore_smile_eyeshadow_layer"
    if skin_effect.face:
        "activity_whore_smile_freckles_layer"
    always "activity_whore_smile_blush_layer"
    if writing.face:
        "activity_whore_smile_writing_face_layer"
    if writing.forehead:
        "activity_whore_smile_writing_forehead_layer"

    always "activity_whore_smile_eye_iris_layer"
    always "activity_whore_smile_eye_eye"
    always "activity_whore_smile_eye_eyeliner_layer"

    always "activity_whore_smile_hair_back_layer"
    always "activity_whore_smile_hair_front_layer"

    always "activity_whore_smile_frame"





image activity_whore_finger_face_base_layer:
    "activity_whore_finger_face_base"
    skin_base_colour_transform()
image activity_whore_finger_face_shad_layer:
    "activity_whore_finger_face_shad"
    skin_shad_colour_transform()

image activity_whore_finger_brow_layer:
    "activity_whore_finger_brow"
    hair_colour_transform()
image activity_whore_finger_mouth_lipstick_layer:
    "activity_whore_finger_mouth_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image activity_whore_finger_eyeshadow_layer:
    "activity_whore_finger_eyeshad"
    accessories_primary_colour_transform("eyeshadow", If (acc.makeup_on and acc.eyeshadow,0.6,0))
image activity_whore_finger_freckles_layer:
    "activity_whore_finger_freckles"
    skin_shad_colour_transform()
image activity_whore_finger_blush_layer:
    "activity_whore_finger_blush"
    blush_opacity_transform()
image activity_whore_finger_writing_face_layer:
    "activity_whore_finger_writing_face"
    writing_transform("face")
image activity_whore_finger_writing_forehead_layer:
    "activity_whore_finger_writing_forehead"
    writing_transform("forehead")

image activity_whore_finger_eye_eyeliner_layer:
    "activity_whore_finger_eye_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image activity_whore_finger_eye_iris_layer:
    "activity_whore_finger_eye_iris"
    eye_colour_transform()

image activity_whore_finger_hair_back_bun_2 = "activity_whore_finger_hair_back_pony"
image activity_whore_finger_hair_back_bun_3 = "activity_whore_finger_hair_back_pony"
image activity_whore_finger_hair_back_bun_4 = "activity_whore_finger_hair_back_pony"
image activity_whore_finger_hair_back_pony_2 = "activity_whore_finger_hair_back_pony"
image activity_whore_finger_hair_back_pony_3 = "activity_whore_finger_hair_back_pony"
image activity_whore_finger_hair_back_pony_4 = "activity_whore_finger_hair_back_pony"
image activity_whore_finger_hair_back_pig_2 = "activity_whore_finger_hair_back_pig_3"

image activity_whore_finger_hair_back_layer:
    get_hair_back_cg_filename("activity_whore_finger_hair_back")
    hair_colour_transform()

image activity_whore_finger_hair_front_layer:
    get_hair_front_cg_filename("activity_whore_finger_hair_front")
    hair_colour_transform()

image activity_whore_finger = LayeredImageProxy("activity_whore_finger_layeredimage", Transform(align=(0.8, 0.0)))

layeredimage activity_whore_finger_layeredimage:
    always "activity_whore_finger_bg"
    always "activity_whore_finger_face_base_layer"
    always "activity_whore_finger_face_shad_layer"
    always "activity_whore_finger_brow_layer"
    always "activity_whore_finger_mouth_lipstick_layer"
    always "activity_whore_finger_mouth"
    always "activity_whore_finger_eyeshadow_layer"
    if skin_effect.face:
        "activity_whore_finger_freckles_layer"
    always:
        "activity_whore_finger_blush_layer"

    if writing.face:
        "activity_whore_finger_writing_face_layer"
    if writing.forehead:
        "activity_whore_finger_writing_forehead_layer"

    always "activity_whore_finger_eye_iris_layer"
    always "activity_whore_finger_eye_eye"
    always "activity_whore_finger_eye_eyeliner_layer"

    always "activity_whore_finger_hair_back_layer"
    always "activity_whore_finger_hair_front_layer"

    always "activity_whore_finger_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
