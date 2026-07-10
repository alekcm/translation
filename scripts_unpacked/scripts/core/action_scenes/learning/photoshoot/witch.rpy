image ps_witch_hat_behind_layer:
    "ps_witch_hat_behind"
    hat_secondary_colour_transform()

image ps_witch_body_base_layer:
    "ps_witch_body_base"
    skin_base_colour_transform()
image ps_witch_body_shad_layer:
    "ps_witch_body_shad"
    skin_shad_colour_transform()
image ps_witch_arm_open_base_layer:
    "ps_witch_arm_open_base"
    skin_base_colour_transform()
image ps_witch_arm_open_shad_layer:
    "ps_witch_arm_open_shad"
    skin_shad_colour_transform()
image ps_witch_arm_cover_base_layer:
    "ps_witch_arm_cover_base"
    skin_base_colour_transform()
image ps_witch_arm_cover_shad_layer:
    "ps_witch_arm_cover_shad"
    skin_shad_colour_transform()

image ps_witch_body_nips_layer:
    "ps_witch_body_nips"
    nipple_colour_transform()
image ps_witch_body_phair_layer:
    "ps_witch_body_phair"
    hair_colour_transform()
image ps_witch_body_nipring_layer:
    get_skin_filename("ps_witch_body_nipring", False)
    accessories_secondary_colour_transform("nipring")
image ps_witch_body_navring_layer:
    get_skin_filename("ps_witch_body_navring", False)
    accessories_secondary_colour_transform("navelring")

image ps_witch_face_eyeshad_layer:
    "ps_witch_face_eyeshad"
    accessories_primary_colour_transform("eyeshadow", 0.8)
image ps_witch_face_mouth_happy_lipstick_layer:
    "ps_witch_face_mouth_happy_lipstick"
    accessories_primary_colour_transform("lipstick", If(acc.lipstick and acc.makeup_on,1,0))

image ps_witch_hair_front_layer:
    "ps_witch_hair_front_" + str(player.hair_fringe)
    hair_colour_transform()
image ps_witch_hair_back_layer:
    "ps_witch_hair_back_" + str(player.hair_neck)
    hair_colour_transform()
image ps_witch_face_brow_neutral_layer:
    "ps_witch_face_brow_neutral"
    hair_colour_transform()

image ps_witch_face_eye_iris_forward_layer:
    "ps_witch_face_eye_iris_forward"
    eye_colour_transform()

image ps_witch_hat_base_layer:
    "ps_witch_hat_base"
    hat_primary_colour_transform()
image ps_witch_hat_trim_layer:
    "ps_witch_hat_trim"
    hat_secondary_colour_transform()

image ps_witch_socks_base_layer:
    "ps_witch_socks_base"
    socks_primary_colour_transform()
image ps_witch_socks_trim_layer:
    "ps_witch_socks_trim"
    socks_secondary_colour_transform()

image ps_witch_outfit_base_layer:
    "ps_witch_outfit_base"
    outfit_primary_colour_transform()
image ps_witch_outfit_trim_layer:
    "ps_witch_outfit_trim"
    outfit_secondary_colour_transform()

image ps_witch_pants_layer:
    "ps_witch_pants"
    pants_primary_colour_transform()

layeredimage ps_witch:

    always:
        "ps_witch_bg"

    always:
        "ps_witch_hat_behind_layer"

    always:
        "ps_witch_hair_back_layer"

    always:
        "ps_witch_body_base_layer"
    always:
        "ps_witch_body_shad_layer"
    always:
        "ps_witch_body_nips_layer"
    if player.phair:
        "ps_witch_body_phair_layer"
    if acc.nipring:
        "ps_witch_body_nipring_layer"
    if acc.navelring:
        "ps_witch_body_navring_layer"

    group arms:
        attribute open default:
            "ps_witch_arm_open_base_layer"
        attribute open default:
            "ps_witch_arm_open_shad_layer"

        attribute cover:
            "ps_witch_arm_cover_base_layer"
        attribute cover:
            "ps_witch_arm_cover_shad_layer"

    if acc.eyeshadow and acc.makeup_on:
        "ps_witch_face_eyeshad_layer"


    group mouth:
        attribute happy default:
            "ps_witch_face_mouth_happy_lipstick_layer"
        attribute happy default:
            "ps_witch_face_mouth_happy"

    always:
        "ps_witch_face_eye_iris_forward_layer"
    always:
        "ps_witch_face_eye_eye_forward"
    always:
        "ps_witch_face_eyeliner"
    always:
        "ps_witch_face_brow_neutral_layer"

    if c.pants:
        "ps_witch_pants_layer"


    always:
        "ps_witch_hair_front_layer"

    if c.hat:
        "ps_witch_hat_base_layer"
    if c.hat:
        "ps_witch_hat_trim_layer"

    if c.socks:
        "ps_witch_socks_base_layer"
    if c.socks:
        "ps_witch_socks_trim_layer"

    if c.outfit:
        "ps_witch_outfit_base_layer"
    if c.outfit:
        "ps_witch_outfit_trim_layer"

    always:
        "ps_witch_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
