image sb_pose_showbreasts_bg_layer:
    "sb_pose_showbreasts_bg_" + loc_cur.loc_type

image sb_pose_showbreasts_belly_base_layer:
    get_skin_filename("sb_pose_showbreasts_belly_base", preg=True)
    skin_base_colour_transform()
image sb_pose_showbreasts_belly_shad_layer:
    get_skin_filename("sb_pose_showbreasts_belly_shad", preg=True)
    skin_shad_colour_transform()

image sb_pose_showbreasts_breasts_base_layer:
    get_skin_filename("sb_pose_showbreasts_breasts_base", breasts=True)
    skin_base_colour_transform()
image sb_pose_showbreasts_breasts_shad_layer:
    get_skin_filename("sb_pose_showbreasts_breasts_shad", breasts=True)
    skin_shad_colour_transform()

image sb_pose_showbreasts_nip_layer:
    get_skin_filename("sb_pose_showbreasts_nip", breasts=True)
    nipple_colour_transform()
image sb_pose_showbreasts_nipring_layer:
    get_skin_filename("sb_pose_showbreasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")
image sb_pose_showbreasts_breasts_tattoo_layer:
    get_skin_filename("sb_pose_showbreasts_breasts_tattoo", breasts=True)
    skin_shad_colour_transform()

image sb_pose_showbreasts_body_base_layer:
    get_skin_filename("sb_pose_showbreasts_body_base")
    skin_base_colour_transform()
image sb_pose_showbreasts_body_shad_layer:
    get_skin_filename("sb_pose_showbreasts_body_shad")
    skin_shad_colour_transform()

image sb_pose_showbreasts_eye_iris_for_layer:
    "sb_pose_showbreasts_eye_iris_forward"
    eye_colour_transform()
image sb_pose_showbreasts_eye_eyeliner_for_layer:
    "sb_pose_showbreasts_eyeliner_for_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_pose_showbreasts_eye_iris_down_layer:
    "sb_pose_showbreasts_eye_iris_down"
    eye_colour_transform()
image sb_pose_showbreasts_eye_eyeliner_down_layer:
    "sb_pose_showbreasts_eyeliner_down_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_pose_showbreasts_eyeshadow_layer:
    "sb_pose_showbreasts_eyeshadow"
    eyeshadow_colour_transform()
image sb_pose_showbreasts_blush_layer:
    "sb_pose_showbreasts_blush"
    blush_opacity_transform()

image sb_pose_showbreasts_brow_straight_layer:
    "sb_pose_showbreasts_brow_straight"
    hair_colour_transform()
image sb_pose_showbreasts_brow_up_layer:
    "sb_pose_showbreasts_brow_up"
    hair_colour_transform()
image sb_pose_showbreasts_brow_worried_layer:
    "sb_pose_showbreasts_brow_worried"
    hair_colour_transform()


image sb_pose_showbreasts_mouth_neutral_lipstick_layer:
    "sb_pose_showbreasts_mouth_neutral_lipstick"
    accessories_primary_colour_transform("lipstick", If(acc.lipstick and acc.makeup_on, 1, 0))
image sb_pose_showbreasts_mouth_oh_lipstick_layer:
    "sb_pose_showbreasts_mouth_oh_lipstick"
    accessories_primary_colour_transform("lipstick", If(acc.lipstick and acc.makeup_on, 1, 0))
image sb_pose_showbreasts_mouth_tounge_lipstick_layer:
    "sb_pose_showbreasts_mouth_tounge_lipstick"
    accessories_primary_colour_transform("lipstick", If(acc.lipstick and acc.makeup_on, 1, 0))
image sb_pose_showbreasts_mouth_happy_lipstick_layer:
    "sb_pose_showbreasts_mouth_happy_lipstick"
    accessories_primary_colour_transform("lipstick", If(acc.lipstick and acc.makeup_on, 1, 0))

image sb_pose_showbreasts_nails_layer:
    get_skin_filename("sb_pose_showbreasts_nails", breasts=True)
    accessories_primary_colour_transform("nails", If(acc.nails, 1, 0))

image sb_pose_showbreasts_hair_back_bun_2 = "sb_pose_showbreasts_hair_back_bun"
image sb_pose_showbreasts_hair_back_bun_3 = "sb_pose_showbreasts_hair_back_bun"
image sb_pose_showbreasts_hair_back_bun_4 = "sb_pose_showbreasts_hair_back_bun"
image sb_pose_showbreasts_hair_back_pony_4 = "sb_pose_showbreasts_hair_back_pony_3"

image sb_pose_showbreasts_hair_back_layer:
    get_hair_back_cg_filename("sb_pose_showbreasts_hair_back")
    hair_colour_transform()
image sb_pose_showbreasts_hair_front_layer:
    get_hair_front_cg_filename("sb_pose_showbreasts_hair_front")
    hair_colour_transform()

image sb_pose_showbreasts_writing_chest_layer:
    "sb_pose_showbreasts_writing_chest"
    writing_transform("chest")
image sb_pose_showbreasts_writing_face_layer:
    "sb_pose_showbreasts_writing_face"
    writing_transform("face")
image sb_pose_showbreasts_writing_forehead_layer:
    "sb_pose_showbreasts_writing_forehead"
    writing_transform("forehead")

image sb_pose_showbreasts_rain:
    "sb_pose_showbreasts_rain1"
    .03
    "sb_pose_showbreasts_rain2"
    .03
    "sb_pose_showbreasts_rain3"
    .03
    repeat

layeredimage sb_pose_showbreasts:

    always "sb_pose_showbreasts_bg_layer"

    always "sb_pose_showbreasts_body_base_layer"
    always "sb_pose_showbreasts_body_shad_layer"

    always "sb_pose_showbreasts_blush_layer"

    always "sb_pose_showbreasts_belly_base_layer"
    always "sb_pose_showbreasts_belly_shad_layer"

    always "sb_pose_showbreasts_breasts_base_layer"
    always "sb_pose_showbreasts_breasts_shad_layer"

    always "sb_pose_showbreasts_nip_layer"
    if acc.nipring:
        "sb_pose_showbreasts_nipring_layer"
    if tattoo.chest:
        "sb_pose_showbreasts_breasts_tattoo_layer"
    if writing.chest:
        "sb_pose_showbreasts_writing_chest_layer"
    if writing.face:
        "sb_pose_showbreasts_writing_face_layer"
    if writing.forehead:
        "sb_pose_showbreasts_writing_forehead_layer"
    if writing.special == "glasses":
        "sb_pose_showbreasts_writing_glasses"

    if acc.eyeshadow and acc.makeup_on:
        "sb_pose_showbreasts_eyeshadow_layer"

    group eye:
        attribute forward default:
            "sb_pose_showbreasts_eye_iris_for_layer"
        attribute forward default:
            "sb_pose_showbreasts_eye_eye_forward"
        attribute forward default:
            "sb_pose_showbreasts_eye_eyeliner_for_layer"

        attribute down:
            "sb_pose_showbreasts_eye_iris_down_layer"
        attribute down:
            "sb_pose_showbreasts_eye_eye_down"
        attribute down:
            "sb_pose_showbreasts_eye_eyeliner_down_layer"

    group brow:
        attribute straight default:
            "sb_pose_showbreasts_brow_straight_layer"

        attribute up:
            "sb_pose_showbreasts_brow_up_layer"

        attribute worried:
            "sb_pose_showbreasts_brow_worried_layer"

    group mouth:
        attribute neutral default:
            "sb_pose_showbreasts_mouth_neutral_lipstick_layer"
        attribute neutral default:
            "sb_pose_showbreasts_mouth_neutral"

        attribute happy:
            "sb_pose_showbreasts_mouth_happy_lipstick_layer"
        attribute happy:
            "sb_pose_showbreasts_mouth_happy"

        attribute tounge:
            "sb_pose_showbreasts_mouth_tounge_lipstick_layer"
        attribute tounge:
            "sb_pose_showbreasts_mouth_tounge"

        attribute oh:
            "sb_pose_showbreasts_mouth_oh_lipstick_layer"
        attribute oh:
            "sb_pose_showbreasts_mouth_oh"



    always:
        "sb_pose_showbreasts_nails_layer"
    always:
        "sb_pose_showbreasts_hair_back_layer"
    always:
        "sb_pose_showbreasts_hair_front_layer"

    group water:
        attribute shower:
            "sb_pose_showbreasts_rain"
        attribute shower:
            "sb_pose_showbreasts_steam"
    always:
        "sb_pose_showbreasts_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
