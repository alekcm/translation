
image ps_santa_body_base_layer:
    "ps_santa_body_base"
    skin_base_colour_transform()
image ps_santa_body_shad_layer:
    "ps_santa_body_shad"
    skin_shad_colour_transform()

image ps_santa_body_tanlines_base_layer:
    "ps_santa_body_tanlines_base"
    skin_base_notan_colour_transform()
image ps_santa_body_tanlines_shad_layer:
    "ps_santa_body_tanlines_shad"
    skin_shad_notan_colour_transform()

image ps_santa_body_nip_layer:
    "ps_santa_body_nip"
    nipple_colour_transform()
image ps_santa_body_nipring_layer:
    "ps_santa_body_nipring"
    accessories_secondary_colour_transform("nipring")
image ps_santa_body_nails_layer:
    "ps_santa_body_nails"
    accessories_primary_colour_transform("nails", If(acc.nails, 1, 0))


image ps_santa_dress_base_layer:
    "ps_santa_dress_base"
    outfit_primary_colour_transform()
image ps_santa_dress_trim_layer:
    "ps_santa_dress_trim"
    outfit_secondary_colour_transform()


image ps_santa_arm_down_base_layer:
    "ps_santa_arm_down_base"
    skin_base_colour_transform()
image ps_santa_arm_down_shad_layer:
    "ps_santa_arm_down_shad"
    skin_shad_colour_transform()

image ps_santa_arm_up_base_layer:
    "ps_santa_arm_up_base"
    skin_base_colour_transform()
image ps_santa_arm_up_shad_layer:
    "ps_santa_arm_up_shad"
    skin_shad_colour_transform()


image ps_santa_bits_base_layer:
    "ps_santa_bits_base"
    outfit_primary_colour_transform()
image ps_santa_bits_trim_layer:
    "ps_santa_bits_trim"
    outfit_secondary_colour_transform()


image ps_santa_face_mouth_happy_lipstick_layer:
    "ps_santa_face_mouth_happy_lipstick"
    accessories_primary_colour_transform("lipstick", If(acc.lipstick and acc.makeup_on,1,0))
image ps_santa_face_mouth_vhappy_lipstick_layer:
    "ps_santa_face_mouth_vhappy_lipstick"
    accessories_primary_colour_transform("lipstick", If(acc.lipstick and acc.makeup_on,1,0))
image ps_santa_face_mouth_open_lipstick_layer:
    "ps_santa_face_mouth_open_lipstick"
    accessories_primary_colour_transform("lipstick", If(acc.lipstick and acc.makeup_on,1,0))
image ps_santa_face_mouth_neutral_lipstick_layer:
    "ps_santa_face_mouth_neutral_lipstick"
    accessories_primary_colour_transform("lipstick", If(acc.lipstick and acc.makeup_on,1,0))

image ps_santa_face_eyeshad_layer:
    "ps_santa_face_eyeshadow"
    accessories_primary_colour_transform("eyeshadow", 0.8)

image ps_santa_face_eye_iris_layer:
    "ps_santa_face_eye_iris"
    eye_colour_transform()

image ps_santa_face_eyeliner_layer:
    "ps_santa_face_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")

image ps_santa_face_brow_up_layer:
    "ps_santa_face_brow_up"
    hair_colour_transform()
image ps_santa_face_brow_worried_layer:
    "ps_santa_face_brow_worried"
    hair_colour_transform()
image ps_santa_face_brow_slant_layer:
    "ps_santa_face_brow_slant"
    hair_colour_transform()
image ps_santa_face_brow_cheeky_layer:
    "ps_santa_face_brow_cheeky"
    hair_colour_transform()

image ps_santa_hairfront_layer:
    "ps_santa_hairfront_" + str(player.hair_fringe)
    hair_colour_transform()
image ps_santa_hairback_layer:
    "ps_santa_hairback_" + str(player.hair_neck)
    hair_colour_transform()

layeredimage ps_santa:

    always:
        "ps_santa_bg"

    always:
        "ps_santa_body_rope"
    always:
        "ps_santa_body_base_layer"
    always:
        "ps_santa_body_shad_layer"
    always:
        "ps_santa_body_tanlines_base_layer"
    always:
        "ps_santa_body_tanlines_shad_layer"
    always:
        "ps_santa_body_nip_layer"
    if acc.nipring:
        "ps_santa_body_nipring_layer"
    always:
        "ps_santa_body_nails_layer"
    if tattoo.ass:
        "ps_santa_body_tat"

    group outfit_group:

        attribute outfit default:
            "ps_santa_dress_base_layer"
        attribute outfit default:
            "ps_santa_dress_trim_layer"
        attribute nooutfit:
            null



    always:
        "ps_santa_bits_base_layer"
    always:
        "ps_santa_bits_trim_layer"



    group mouth:
        attribute happy:
            "ps_santa_face_mouth_happy_lipstick_layer"
        attribute happy:
            "ps_santa_face_mouth_happy"

        attribute vhappy:
            "ps_santa_face_mouth_vhappy_lipstick_layer"
        attribute vhappy:
            "ps_santa_face_mouth_vhappy"

        attribute neutral default:
            "ps_santa_face_mouth_neutral_lipstick_layer"
        attribute neutral default:
            "ps_santa_face_mouth_neutral"

        attribute open:
            "ps_santa_face_mouth_open_lipstick_layer"
        attribute open:
            "ps_santa_face_mouth_open"

    always:
        "ps_santa_face_eyeshad_layer"

    always:
        "ps_santa_face_eye_iris_layer"
    always:
        "ps_santa_face_eye_white"
    always:
        "ps_santa_face_eyeliner_layer"

    group brows:
        attribute up default:
            "ps_santa_face_brow_up_layer"
        attribute worried:
            "ps_santa_face_brow_worried_layer"
        attribute slant:
            "ps_santa_face_brow_slant_layer"
        attribute cheeky:
            "ps_santa_face_brow_cheeky_layer"

    always:
        "ps_santa_hairback_layer"
    always:
        "ps_santa_hairfront_layer"

    group arm:
        attribute armup:
            "ps_santa_arm_up_base_layer"
        attribute armup:
            "ps_santa_arm_up_shad_layer"
        attribute armdown default:
            "ps_santa_arm_down_base_layer"
        attribute armdown default:
            "ps_santa_arm_down_shad_layer"

    always:
        "ps_santa_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
