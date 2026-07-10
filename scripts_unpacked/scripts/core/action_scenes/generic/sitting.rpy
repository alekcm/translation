
image sb_sitting_bg_layer:
    "sb_sitting_bg_" + loc_cur.loc_type


image sb_sitting_pc_body_base_layer:
    "sb_sitting_pc_body_base"
    skin_base_colour_transform()
image sb_sitting_pc_body_shad_layer:
    "sb_sitting_pc_body_shad"
    skin_shad_colour_transform()


image sb_sitting_pc_breasts_base_layer:
    get_skin_filename("sb_sitting_pc_breasts_base", breasts=True)
    skin_base_colour_transform()
image sb_sitting_pc_breasts_shad_layer:
    get_skin_filename("sb_sitting_pc_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image sb_sitting_pc_breasts_nips_layer:
    get_skin_filename("sb_sitting_pc_breasts_nips", breasts=True)
    nipple_colour_transform()
image sb_sitting_pc_breasts_nipring_layer:
    get_skin_filename("sb_sitting_pc_breasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")
image sb_sitting_pc_breasts_tattoo_layer:
    get_skin_filename("sb_sitting_pc_breasts_tattoo", breasts=True)


image sb_sitting_pc_armrest_base_layer:
    "sb_sitting_pc_armrest_base"
    skin_base_colour_transform()
image sb_sitting_pc_armrest_shad_layer:
    "sb_sitting_pc_armrest_shad"
    skin_shad_colour_transform()

image sb_sitting_pc_armmast_base_layer:
    "sb_sitting_pc_armmast_base"
    skin_base_colour_transform()
image sb_sitting_pc_armmast_shad_layer:
    "sb_sitting_pc_armmast_shad"
    skin_shad_colour_transform()
image sb_sitting_pc_armmast_manbase_layer:
    "sb_sitting_pc_armmast_manbase"
    npc_skin_base_colour_transform()
image sb_sitting_pc_armmast_manshad_layer:
    "sb_sitting_pc_armmast_manshad"
    npc_skin_shad_colour_transform()

image sb_sitting_pc_armrest_nails_layer:
    "sb_sitting_pc_armrest_nails"
    accessories_primary_colour_transform("nails", If(acc.nails, 1, 0))
image sb_sitting_pc_armmast_nails_layer:
    "sb_sitting_pc_armmast_nails"
    accessories_primary_colour_transform("nails", If(acc.nails, 1, 0))



image sb_sitting_pc_face_eye_eyeliner_layer:
    "sb_sitting_pc_face_eye_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_sitting_pc_face_eye_iris_left_layer:
    "sb_sitting_pc_face_eye_iris_left"
    eye_colour_transform()
image sb_sitting_pc_face_eye_iris_right_layer:
    "sb_sitting_pc_face_eye_iris_right"
    eye_colour_transform()


image sb_sitting_pc_face_brow_neutral_layer:
    "sb_sitting_pc_face_brow_neutral"
    hair_colour_transform()
image sb_sitting_pc_face_brow_worried_layer:
    "sb_sitting_pc_face_brow_worried"
    hair_colour_transform()

image sb_sitting_pc_face_mouth_neutral_lipstick_layer:
    "sb_sitting_pc_face_mouth_neutral_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not acc.gagged and acc.lipstick,1,0))
image sb_sitting_pc_face_mouth_worried_lipstick_layer:
    "sb_sitting_pc_face_mouth_worried_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not acc.gagged and acc.lipstick,1,0))

image sb_sitting_pc_face_gag_lipstick_layer:
    "sb_sitting_pc_face_gag_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and acc.lipstick,1,0))
image sb_sitting_pc_face_gag_base_layer:
    "sb_sitting_pc_face_gag_base"
    gag_colour_transform()
image sb_sitting_pc_face_gag_metal_layer:
    "sb_sitting_pc_face_gag_metal"
    gag_metal_transform()


image sb_sitting_pc_face_eyeshad_layer:
    "sb_sitting_pc_face_eyeshad"
    eyeshadow_colour_transform()
image sb_sitting_pc_face_freckles_layer:
    "sb_sitting_pc_face_freckles"
    skin_shad_colour_transform()
image sb_sitting_pc_face_blush_layer:
    "sb_sitting_pc_face_blush"
    blush_opacity_transform()



image sb_sitting_pc_hair_front_layer:
    get_hair_front_cg_filename("sb_sitting_pc_hair_front")
    hair_colour_transform()
image sb_sitting_pc_hair_back_bun_2 = "sb_sitting_pc_hair_back_bun"
image sb_sitting_pc_hair_back_bun_3 = "sb_sitting_pc_hair_back_bun"
image sb_sitting_pc_hair_back_bun_4 = "sb_sitting_pc_hair_back_bun"
image sb_sitting_pc_hair_back_pony_4 = "sb_sitting_pc_hair_back_pony_3"
image sb_sitting_pc_hair_back_layer:
    get_hair_back_cg_filename("sb_sitting_pc_hair_back")
    hair_colour_transform()



image sb_sitting_man_base_layer:
    "sb_sitting_man_base"
    npc_skin_base_colour_transform()
image sb_sitting_man_shad_layer:
    "sb_sitting_man_shad"
    npc_skin_shad_colour_transform()
image sb_sitting_man_arm_base_layer:
    "sb_sitting_man_arm_base"
    npc_skin_base_colour_transform()
image sb_sitting_man_arm_shad_layer:
    "sb_sitting_man_arm_shad"
    npc_skin_shad_colour_transform()

image sb_sitting = LayeredImageProxy("sb_sitting_layered", Transform(xalign = (0.7)))

layeredimage sb_sitting_layered:

    always "sb_sitting_bg_layer"

    group man:
        attribute no_man null default

        attribute man "sb_sitting_man_base_layer"
        attribute man "sb_sitting_man_shad_layer"
        attribute man "sb_sitting_man_clothes1"

    always "sb_sitting_pc_body_base_layer"
    always "sb_sitting_pc_body_shad_layer"

    group arm:
        attribute rest "sb_sitting_pc_armrest_base_layer" default
        attribute rest "sb_sitting_pc_armrest_shad_layer" default
        attribute rest "sb_sitting_pc_armrest_nails_layer" default

        attribute mast if_not "man" "sb_sitting_pc_armrest_base_layer"
        attribute mast if_not "man" "sb_sitting_pc_armrest_shad_layer"
        attribute mast if_not "man" "sb_sitting_pc_armrest_nails_layer"

        attribute mast if_any "man" "sb_sitting_pc_armmast_manbase_layer"
        attribute mast if_any "man" "sb_sitting_pc_armmast_manshad_layer"
        attribute mast if_any "man" "sb_sitting_pc_armmast_base_layer"
        attribute mast if_any "man" "sb_sitting_pc_armmast_shad_layer"
        attribute mast if_any "man" "sb_sitting_pc_armmast_nails_layer"

    always "sb_sitting_pc_face_eyeshad_layer"
    always "sb_sitting_pc_face_blush_layer"
    if skin_effect.face:
        "sb_sitting_pc_face_freckles_layer"

    group eye:
        attribute left "sb_sitting_pc_face_eye_iris_left_layer" default
        attribute left "sb_sitting_pc_face_eye_eye_left" default

        attribute right "sb_sitting_pc_face_eye_iris_right_layer"
        attribute right "sb_sitting_pc_face_eye_eye_right"

    always "sb_sitting_pc_face_eye_eyeliner_layer"



    group face:
        attribute neutral "sb_sitting_pc_face_brow_neutral_layer" default
        attribute neutral "sb_sitting_pc_face_mouth_neutral_lipstick_layer" default
        attribute neutral "sb_sitting_pc_face_mouth_neutral" default

        attribute worried "sb_sitting_pc_face_brow_worried_layer"
        attribute worried "sb_sitting_pc_face_mouth_worried_lipstick_layer"
        attribute worried "sb_sitting_pc_face_mouth_worried"

    if player.gagged:
        "sb_sitting_pc_face_gag_lipstick_layer"
    if player.gagged:
        "sb_sitting_pc_face_gag_base_layer"
    if player.gagged:
        "sb_sitting_pc_face_gag_metal_layer"

    if player.blind:
        "sb_sitting_pc_face_blind"



    always "sb_sitting_pc_breasts_base_layer"
    always "sb_sitting_pc_breasts_shad_layer"
    always "sb_sitting_pc_breasts_nips_layer"
    if acc.nipring:
        "sb_sitting_pc_breasts_nipring_layer"
    if tattoo.chest:
        "sb_sitting_pc_breasts_tattoo_layer"

    always "sb_sitting_pc_hair_back_layer"

    group man:
        attribute no_man null default

        attribute man "sb_sitting_man_arm_base_layer"
        attribute man "sb_sitting_man_arm_shad_layer"

    always "sb_sitting_pc_hair_front_layer"

    if dis(dis_school):
        "sb_sitting_fg"
    always "sb_sitting_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
