image ps_pose_vball_body_base_layer:
    "ps_pose_vball_body_base"
    skin_base_colour_transform()
image ps_pose_vball_body_shad_layer:
    "ps_pose_vball_body_shad"
    skin_shad_colour_transform()
image ps_pose_vball_breasts_layer:
    "ps_pose_vball_breasts_" + str(player.breasts)

image ps_pose_vball_belly_base_layer:
    "ps_pose_vball_belly_base"
    skin_base_colour_transform()
image ps_pose_vball_belly_shad_layer:
    "ps_pose_vball_belly_shad"
    skin_shad_colour_transform()

image ps_pose_vball_face_lipstick_layer:
    "ps_pose_vball_face_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image ps_pose_vball_face_eyeshad_layer:
    "ps_pose_vball_face_eyeshad"
    accessories_primary_colour_transform("eyeshadow", If (acc.makeup_on and acc.eyeshadow,0.6,0))
image ps_pose_vball_face_freckles_layer:
    "ps_pose_vball_face_freckles"
    skin_shad_colour_transform()

image ps_pose_vball_face_eye_iris_layer:
    "ps_pose_vball_face_eye_iris"
    eye_colour_transform()
image ps_pose_vball_face_eye_eyeliner_layer:
    "ps_pose_vball_face_eye_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")


image ps_pose_vball_hair_back_pony_2 = "ps_pose_vball_hair_back_3"
image ps_pose_vball_hair_back_pony_3 = "ps_pose_vball_hair_back_3"
image ps_pose_vball_hair_back_pony_4 = "ps_pose_vball_hair_back_3"

image ps_pose_vball_hair_back_layer:
    get_hair_back_cg_filename("ps_pose_vball_hair_back")
    hair_colour_transform()
image ps_pose_vball_hair_front_layer:
    get_hair_front_cg_filename("ps_pose_vball_hair_front")
    hair_colour_transform()



layeredimage ps_pose_vball:
    always "ps_pose_vball_bg"

    always "ps_pose_vball_body_base_layer"
    always "ps_pose_vball_body_shad_layer"
    always "ps_pose_vball_body_col"
    always "ps_pose_vball_breasts_layer"

    if player.pregnancy >= 2:
        "ps_pose_vball_belly"

    always "ps_pose_vball_face_eyeshad_layer"
    always "ps_pose_vball_face_lipstick_layer"
    if skin_effect.face:
        "ps_pose_vball_face_freckles_layer"

    always "ps_pose_vball_face_eye_iris_layer"
    always "ps_pose_vball_face_eye_eye"
    always "ps_pose_vball_face_eye_eyeliner_layer"

    always "ps_pose_vball_hair_back_layer"
    always "ps_pose_vball_hair_front_layer"

layeredimage ps_pose_vball_belly:
    always "ps_pose_vball_belly_base_layer"
    always "ps_pose_vball_belly_shad_layer"
    always "ps_pose_vball_belly_col"





image ps_pose_vballball_pc_base_layer:
    "ps_pose_vballball_pc_base"
    skin_base_colour_transform()
image ps_pose_vballball_pc_shad_layer:
    "ps_pose_vballball_pc_shad"
    skin_shad_colour_transform()

image ps_pose_vballball = LayeredImageProxy("ps_pose_vballball_layered", Transform(xalign = (0.80)))

layeredimage ps_pose_vballball_layered:
    if loc(loc_school_gym):
        "ps_pose_vballball_bg_gym"

    always "ps_pose_vballball_pc_base_layer"
    always "ps_pose_vballball_pc_shad_layer"
    always "ps_pose_vballball_pc_col"
    if loc(loc_school_gym):
        "ps_pose_vballball_pc_outfit_vball"

    always "ps_pose_vballball_frame"





image ps_pose_vballass_body_base_layer:
    "ps_pose_vballass_body_base"
    skin_base_colour_transform()
image ps_pose_vballass_body_shad_layer:
    "ps_pose_vballass_body_shad"
    skin_shad_colour_transform()

image ps_pose_vballass = LayeredImageProxy("ps_pose_vballass_layered", Transform(xalign = (0.80)))

layeredimage ps_pose_vballass_layered:
    if loc(loc_school_gym):
        "ps_pose_vballass_bg_gym"

    always "ps_pose_vballass_body_base_layer"
    always "ps_pose_vballass_body_shad_layer"
    if loc(loc_school_gym):
        "ps_pose_vballass_outfit_vball"

    always "ps_pose_vballass_frame"





image ps_pose_vballpoint_body_base_layer:
    "ps_pose_vballpoint_body_base"
    skin_base_colour_transform()
image ps_pose_vballpoint_body_shad_layer:
    "ps_pose_vballpoint_body_shad"
    skin_shad_colour_transform()

image ps_pose_vballpoint = LayeredImageProxy("ps_pose_vballpoint_layered", Transform(xalign = (0.80)))

layeredimage ps_pose_vballpoint_layered:
    if loc(loc_school_gym):
        "ps_pose_vballpoint_bg_gym"

    always "ps_pose_vballpoint_body_base_layer"
    always "ps_pose_vballpoint_body_shad_layer"
    if loc(loc_school_gym):
        "ps_pose_vballpoint_outfit_vball"

    always "ps_pose_vballpoint_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
