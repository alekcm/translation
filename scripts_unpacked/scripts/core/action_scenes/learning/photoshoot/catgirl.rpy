image ps_catgirl_body_base_layer:
    "ps_catgirl_body_base"
    skin_base_colour_transform()
image ps_catgirl_body_shad_layer:
    "ps_catgirl_body_shad"
    skin_shad_colour_transform()
image ps_catgirl_body_nips_layer:
    "ps_catgirl_body_nips"
    nipple_colour_transform()
image ps_catgirl_body_phair_layer:
    "ps_catgirl_body_phair"
    hair_colour_transform()
image ps_catgirl_body_nipring_layer:
    get_skin_filename("ps_catgirl_body_nipring", False)
    accessories_secondary_colour_transform("nipring", If(acc.nipring,1,0))
image ps_catgirl_body_navring_layer:
    get_skin_filename("ps_catgirl_body_navring", False)
    accessories_secondary_colour_transform("navelring", If(acc.navelring,1,0))

image ps_catgirl_bodyc_base_layer:
    "ps_catgirl_bodyc_base"
    skin_base_colour_transform()
image ps_catgirl_bodyc_shad_layer:
    "ps_catgirl_bodyc_shad"
    skin_shad_colour_transform()

image ps_catgirl_body_face_eyeshad_layer:
    "ps_catgirl_body_face_eyeshad"
    accessories_primary_colour_transform("eyeshadow", 0.8)

image ps_catgirl_body_face_mouth_happy_lipstick_layer:
    "ps_catgirl_body_face_mouth_happy_lipstick"
    accessories_primary_colour_transform("lipstick", If(acc.lipstick and acc.makeup_on,1,0))
image ps_catgirl_body_face_mouth_tounge_lipstick_layer:
    "ps_catgirl_body_face_mouth_tounge_lipstick"
    accessories_primary_colour_transform("lipstick", If(acc.lipstick and acc.makeup_on,1,0))
image ps_catgirl_body_face_mouth_oh_lipstick_layer:
    "ps_catgirl_body_face_mouth_oh_lipstick"
    accessories_primary_colour_transform("lipstick", If(acc.lipstick and acc.makeup_on,1,0))

image ps_catgirl_body_face_eye_iris_layer:
    "ps_catgirl_body_face_eye_iris"
    eye_colour_transform()

image ps_catgirl_body_face_eyeliner_layer:
    "ps_catgirl_body_face_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")

image ps_catgirl_body_face_brow_straight_layer:
    "ps_catgirl_body_face_brow_straight"
    hair_colour_transform()
image ps_catgirl_body_face_brow_worried_layer:
    "ps_catgirl_body_face_brow_worried"
    hair_colour_transform()
image ps_catgirl_body_face_brow_cheeky_layer:
    "ps_catgirl_body_face_brow_cheeky"
    hair_colour_transform()

image ps_catgirl_hair_front_layer:
    "ps_catgirl_hair_front_" + str(player.hair_fringe)
    hair_colour_transform()
image ps_catgirl_hair_back_layer:
    "ps_catgirl_hair_back_" + str(player.hair_neck)
    hair_colour_transform()

image ps_catgirl_body_nails_layer:
    "ps_catgirl_body_nails"
    accessories_primary_colour_transform("nails", If(acc.nails, 1, 0))
image ps_catgirl_bodyc_nails_layer:
    "ps_catgirl_bodyc_nails"
    accessories_primary_colour_transform("nails", If(acc.nails, 1, 0))


image ps_catgirl_collar_base_layer:
    "ps_catgirl_collar_base"
    accessories_primary_colour_transform("choker")
image ps_catgirl_collar_trim_layer:
    "ps_catgirl_collar_trim"
    accessories_secondary_colour_transform("choker")

image ps_catgirl_hat_base_layer:
    "ps_catgirl_hat_base"
    hat_primary_colour_transform()
image ps_catgirl_hat_trim_layer:
    "ps_catgirl_hat_trim"

image ps_catgirl_socks_base_layer:
    "ps_catgirl_socks_base"
    socks_primary_colour_transform()
image ps_catgirl_socks_trim_layer:
    "ps_catgirl_socks_trim"
    socks_secondary_colour_transform()

image ps_catgirl_top_base_layer:
    "ps_catgirl_top_base"
    top_primary_colour_transform()
image ps_catgirl_top_trim_layer:
    "ps_catgirl_top_trim"
    top_secondary_colour_transform()

image ps_catgirl_bottom_base_layer:
    "ps_catgirl_bottom_base"
    bottom_primary_colour_transform()
image ps_catgirl_bottom_trim_layer:
    "ps_catgirl_bottom_trim"
    bottom_secondary_colour_transform()

image ps_catgirl_gloves_base_layer:
    "ps_catgirl_gloves_base"
    gloves_primary_colour_transform()
image ps_catgirl_gloves_trim_layer:
    "ps_catgirl_gloves_trim"
    gloves_secondary_colour_transform()
image ps_catgirl_glovesc_base_layer:
    "ps_catgirl_glovesc_base"
    gloves_primary_colour_transform()
image ps_catgirl_glovesc_trim_layer:
    "ps_catgirl_glovesc_trim"
    gloves_secondary_colour_transform()
layeredimage ps_catgirl:

    always:
        "ps_catgirl_bg"

    always:
        "ps_catgirl_hair_back_layer"

    group pose:
        attribute open default:
            "ps_catgirl_body_base_layer"
        attribute open default:
            "ps_catgirl_body_shad_layer"
        attribute open default:
            "ps_catgirl_body_nips_layer"
        attribute open default:
            "ps_catgirl_body_nipring_layer"
        attribute open default:
            "ps_catgirl_body_navring_layer"
        attribute open default:
            "ps_catgirl_body_nails_layer"

        attribute closed:
            "ps_catgirl_bodyc_base_layer"
        attribute closed:
            "ps_catgirl_bodyc_shad_layer"
        attribute closed:
            "ps_catgirl_bodyc_nails_layer"
    if player.phair:
        "ps_catgirl_body_phair_layer"

















    always:
        "ps_catgirl_body_face_eyeshad_layer"

    group mouth:
        attribute happy default:
            "ps_catgirl_body_face_mouth_happy_lipstick_layer"
        attribute happy default:
            "ps_catgirl_body_face_mouth_happy"

        attribute tounge:
            "ps_catgirl_body_face_mouth_tounge_lipstick_layer"
        attribute tounge:
            "ps_catgirl_body_face_mouth_tounge"

        attribute oh:
            "ps_catgirl_body_face_mouth_oh_lipstick_layer"
        attribute oh:
            "ps_catgirl_body_face_mouth_oh"

    group brow:
        attribute straight default:
            "ps_catgirl_body_face_brow_straight_layer"

        attribute worried:
            "ps_catgirl_body_face_brow_worried_layer"

        attribute cheeky:
            "ps_catgirl_body_face_brow_cheeky_layer"

    always:
        "ps_catgirl_body_face_eye_iris_layer"
    always:
        "ps_catgirl_body_face_eye_eye"
    always:
        "ps_catgirl_body_face_eyeliner_layer"






    if c.hat:
        "ps_catgirl_hat_base_layer"
    if c.hat:
        "ps_catgirl_hat_trim_layer"

    always:
        "ps_catgirl_hair_front_layer"

    if acc.choker:
        "ps_catgirl_collar_base_layer"
    if acc.choker:
        "ps_catgirl_collar_trim_layer"

    if c.socks:
        "ps_catgirl_socks_base_layer"
    if c.socks:
        "ps_catgirl_socks_trim_layer"

    if c.gloves:
        if_any "closed" "ps_catgirl_glovesc_base_layer"
    if c.gloves:
        if_any "closed" "ps_catgirl_glovesc_trim_layer"
    if c.gloves:
        if_any "open" "ps_catgirl_gloves_base_layer"
    if c.gloves:
        if_any "open" "ps_catgirl_gloves_trim_layer"

    if c.top:
        "ps_catgirl_top_base_layer"
    if c.top:
        "ps_catgirl_top_trim_layer"

    if c.bottom:
        "ps_catgirl_bottom_base_layer"
    if c.bottom:
        "ps_catgirl_bottom_trim_layer"




    always:
        "ps_catgirl_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
