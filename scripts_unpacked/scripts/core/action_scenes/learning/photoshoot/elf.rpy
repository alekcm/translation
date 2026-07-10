
image ps_elf_arm_open_base_layer:
    "ps_elf_arm_open_base"
    skin_base_colour_transform()
image ps_elf_arm_open_shad_layer:
    "ps_elf_arm_open_shad"
    skin_shad_colour_transform()
image ps_elf_arm_open_nails_layer:
    "ps_elf_arm_open_nails"
    accessories_primary_colour_transform("nails", If(acc.nails, 1, 0))
image ps_elf_arm_open_bits_base_layer:
    "ps_elf_arm_open_bits_base"
    gloves_secondary_colour_transform()
image ps_elf_arm_open_bits_trim_layer:
    "ps_elf_arm_open_bits_trim"
    gloves_primary_colour_transform()

image ps_elf_arm_cover_base_layer:
    "ps_elf_arm_cover_base"
    skin_base_colour_transform()
image ps_elf_arm_cover_shad_layer:
    "ps_elf_arm_cover_shad"
    skin_shad_colour_transform()
image ps_elf_arm_cover_nails_layer:
    "ps_elf_arm_cover_nails"
    accessories_primary_colour_transform("nails", If(acc.nails, 1, 0))
image ps_elf_arm_cover_bits_base_layer:
    "ps_elf_arm_cover_bits_base"
    gloves_secondary_colour_transform()
image ps_elf_arm_cover_bits_trim_layer:
    "ps_elf_arm_cover_bits_trim"
    gloves_primary_colour_transform()


image ps_elf_body_base_layer:
    "ps_elf_body_base"
    skin_base_colour_transform()
image ps_elf_body_shad_layer:
    "ps_elf_body_shad"
    skin_shad_colour_transform()

image ps_elf_body_tanline_base_layer:
    "ps_elf_body_tanline_base"
    skin_base_notan_colour_transform()
image ps_elf_body_tanline_shad_layer:
    "ps_elf_body_tanline_shad"
    skin_shad_notan_colour_transform()

image ps_elf_body_nips_layer:
    "ps_elf_body_nips"
    nipple_colour_transform()
image ps_elf_body_nipring_layer:
    "ps_elf_body_nipring"
    accessories_secondary_colour_transform("nipring")
image ps_elf_body_navring_layer:
    "ps_elf_body_navring"
    accessories_secondary_colour_transform("navelring")
image ps_elf_body_nails_layer:
    "ps_elf_body_nails"
    accessories_primary_colour_transform("nails", If(acc.nails, 1, 0))


image ps_elf_face_mouth_happy_lipstick_layer:
    "ps_elf_face_mouth_happy_lipstick"
    accessories_primary_colour_transform("lipstick", If(acc.lipstick and acc.makeup_on,1,0))
image ps_elf_face_mouth_vhappy_lipstick_layer:
    "ps_elf_face_mouth_vhappy_lipstick"
    accessories_primary_colour_transform("lipstick", If(acc.lipstick and acc.makeup_on,1,0))
image ps_elf_face_mouth_neutral_lipstick_layer:
    "ps_elf_face_mouth_neutral_lipstick"
    accessories_primary_colour_transform("lipstick", If(acc.lipstick and acc.makeup_on,1,0))
image ps_elf_face_mouth_tounge_lipstick_layer:
    "ps_elf_face_mouth_tounge_lipstick"
    accessories_primary_colour_transform("lipstick", If(acc.lipstick and acc.makeup_on,1,0))

image ps_elf_dress_skin_layer:
    "ps_elf_dress_skin"
    skin_base_colour_transform()
image ps_elf_dress_base_layer:
    "ps_elf_dress_base"
    outfit_primary_colour_transform()
image ps_elf_dress_trim_layer:
    "ps_elf_dress_trim"
    outfit_secondary_colour_transform()


image ps_elf_arm_down_base_layer:
    "ps_elf_arm_down_base"
    skin_base_colour_transform()
image ps_elf_arm_down_shad_layer:
    "ps_elf_arm_down_shad"
    skin_shad_colour_transform()

image ps_elf_arm_up_base_layer:
    "ps_elf_arm_up_base"
    skin_base_colour_transform()
image ps_elf_arm_up_shad_layer:
    "ps_elf_arm_up_shad"
    skin_shad_colour_transform()


image ps_elf_bits_base_layer:
    "ps_elf_bits_base"
    gloves_primary_colour_transform()
image ps_elf_bits_trim_layer:
    "ps_elf_bits_trim"
    gloves_secondary_colour_transform()

image ps_elf_hat_base_layer:
    "ps_elf_hat_base"
    hat_primary_colour_transform()
image ps_elf_hat_trim_layer:
    "ps_elf_hat_trim"
    hat_secondary_colour_transform()

image ps_elf_face_mouth_happy_lipstick_layer:
    "ps_elf_face_mouth_happy_lipstick"
    accessories_primary_colour_transform("lipstick", If(acc.lipstick and acc.makeup_on,1,0))
image ps_elf_face_mouth_vhappy_lipstick_layer:
    "ps_elf_face_mouth_vhappy_lipstick"
    accessories_primary_colour_transform("lipstick", If(acc.lipstick and acc.makeup_on,1,0))
image ps_elf_face_mouth_open_lipstick_layer:
    "ps_elf_face_mouth_open_lipstick"
    accessories_primary_colour_transform("lipstick", If(acc.lipstick and acc.makeup_on,1,0))
image ps_elf_face_mouth_neutral_lipstick_layer:
    "ps_elf_face_mouth_neutral_lipstick"
    accessories_primary_colour_transform("lipstick", If(acc.lipstick and acc.makeup_on,1,0))

image ps_elf_face_eyeshad_layer:
    "ps_elf_face_eyeshadow"
    accessories_primary_colour_transform("eyeshadow", If(acc.eyeshadow and acc.makeup_on,0.8,0))

image ps_elf_face_eye_iris_open_layer:
    "ps_elf_face_eye_iris_open"
    eye_colour_transform()
image ps_elf_face_eye_iris_wink_layer:
    "ps_elf_face_eye_iris_wink"
    eye_colour_transform()

image ps_elf_face_eyeliner_open_layer:
    "ps_elf_face_eyeliner_open_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image ps_elf_face_eyeliner_wink_layer:
    "ps_elf_face_eyeliner_wink_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")

image ps_elf_face_brow_straight_layer:
    "ps_elf_face_brow_straight"
    hair_colour_transform()
image ps_elf_face_brow_worried_layer:
    "ps_elf_face_brow_worried"
    hair_colour_transform()
image ps_elf_face_brow_slant_layer:
    "ps_elf_face_brow_slant"
    hair_colour_transform()


image ps_elf_hairfront_layer:
    "ps_elf_hairfront_" + str(player.hair_fringe)
    hair_colour_transform()
image ps_elf_hairback_layer:
    "ps_elf_hairback_" + str(player.hair_neck)
    hair_colour_transform()


image ps_elf_dress_base_layer:
    "ps_elf_dress_base"
    outfit_primary_colour_transform()
image ps_elf_dress_trim_layer:
    "ps_elf_dress_trim"
    outfit_secondary_colour_transform()
layeredimage ps_elf:

    always:
        "ps_elf_bg"

    group arm:
        attribute showing default:
            "ps_elf_arm_open_present"
        attribute showing default:
            "ps_elf_arm_open_base_layer"
        attribute showing default:
            "ps_elf_arm_open_shad_layer"
        attribute showing default:
            "ps_elf_arm_open_nails_layer"
        attribute showing default:
            "ps_elf_arm_open_bits_base_layer"
        attribute showing default:
            "ps_elf_arm_open_bits_trim_layer"

    always:
        "ps_elf_body_base_layer"
    always:
        "ps_elf_body_shad_layer"
    always:
        "ps_elf_body_tanline_base_layer"
    always:
        "ps_elf_body_tanline_shad_layer"
    always:
        "ps_elf_body_nips_layer"
    if acc.nipring:
        "ps_elf_body_nipring_layer"
    if acc.navelring:
        "ps_elf_body_navring_layer"
    always:
        "ps_elf_body_nails_layer"
    if tattoo.chest:
        "ps_elf_body_tat_chest"


    group mouth:
        attribute happy:
            "ps_elf_face_mouth_happy_lipstick_layer"
        attribute happy:
            "ps_elf_face_mouth_happy"

        attribute vhappy:
            "ps_elf_face_mouth_vhappy_lipstick_layer"
        attribute vhappy:
            "ps_elf_face_mouth_vhappy"

        attribute neutral default:
            "ps_elf_face_mouth_neutral_lipstick_layer"
        attribute neutral default:
            "ps_elf_face_mouth_neutral"

        attribute tounge:
            "ps_elf_face_mouth_tounge_lipstick_layer"
        attribute tounge:
            "ps_elf_face_mouth_tounge"

    always:
        "ps_elf_face_eyeshad_layer"

    group eye:
        attribute open default:
            "ps_elf_face_eye_iris_open_layer"
        attribute open default:
            "ps_elf_face_eye_eye_open"
        attribute open default:
            "ps_elf_face_eyeliner_open_layer"

        attribute wink:
            "ps_elf_face_eye_iris_wink_layer"
        attribute wink:
            "ps_elf_face_eye_eye_wink"
        attribute wink:
            "ps_elf_face_eyeliner_wink_layer"

    group brows:
        attribute straight default:
            "ps_elf_face_brow_straight_layer"
        attribute worried:
            "ps_elf_face_brow_worried_layer"
        attribute slant:
            "ps_elf_face_brow_slant_layer"

    always:
        "ps_elf_hat_base_layer"
    always:
        "ps_elf_hat_trim_layer"

    always:
        "ps_elf_hairback_layer"
    always:
        "ps_elf_hairfront_layer"

    group outfit_group:
        attribute outfit default:
            "ps_elf_dress_skin_layer"
        attribute outfit default:
            "ps_elf_dress_base_layer"
        attribute outfit default:
            "ps_elf_dress_trim_layer"

        attribute nooutfit:
            null

    always:
        "ps_elf_bits_base_layer"
    always:
        "ps_elf_bits_trim_layer"

    group arm:
        attribute cover :
            "ps_elf_arm_cover_present"
        attribute cover :
            "ps_elf_arm_cover_shad_layer"
        attribute cover :
            "ps_elf_arm_cover_nails_layer"
        attribute cover :
            "ps_elf_arm_cover_bits_base_layer"
        attribute cover :
            "ps_elf_arm_cover_bits_trim_layer"

    always:
        "ps_elf_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
